from talon import Context, Module, actions, app, cron, settings, ui

import re
import time
from timeit import default_timer as timer

mod = Module()

ctx = Context()

ctx_terminal = Context()
ctx_terminal.matches = r"""
tag: user.vim_terminal_mode
"""

last_title = None
last_window = None


def title_parse_TERM(window):
    """check if neovim window is focused and enable/disable monitoring the
    vim features by parsing the shell command from the embedded terminal title.
    """
    global last_window, last_title

    current_title = window.title
    if not current_title.startswith("VIM MODE:"):
        print("title_parse_TERM(): Skipping due to not in neovim")
        return

    if last_window == window and last_title == current_title:
        print("title_parse_TERM(): Skipping due to duplicate window/title")
        return
    if (
        window != ui.active_window()
        or not current_title.startswith("VIM MODE:t")
        or "TERM:" not in current_title
    ):
        print("title_parse_TERM(): Skipping due to not a terminal")
        return

    last_window = window
    last_title = current_title

    shell_command = title_parse_shell_command(current_title)

    tags = title_set_tags(shell_command, current_title)
    print(f"title_parse_TERM(): setting shell tags: {tags}")
    ctx_terminal.tags = tags

    title_set_languages(shell_command)


def title_parse_shell_command(current_title):
    """Parse the shell command from the embedded terminal title that is exposed
    in the parent vim window title.
    """

    # pull a "TERM:..." line out of something like:
    # VIM MODE:t RPC:/tmp/nvimlVeccr/0  TERM:gdb (term://~//161917:/usr/bin/zsh) zsh
    # VIM MODE:t RPC:\\.\pipe\nvim.15116.0 FILETYPE:  TERM:C:\Windows\system32\cmd.exe (term://~\AppData\Roaming\talon//38792:C:\Windows\system32\cmd.exe) cmd.exe
    index = current_title.find("TERM:")
    shell_command = current_title[index + len("TERM:") :]

    # pull out the first element which is something like "gdb" or "C:\Windows\system32\cmd.exe"
    index = shell_command.find(" (term://")
    if index != -1:
        shell_command = shell_command[:index]

    if shell_command.startswith("sudo"):
        # strip the "sudo" word from something like:
        # VIM MODE:t RPC:/tmp/nvimlVeccr/0  TERM:sudo gdb (term://~//161917:/usr/bin/zsh) zsh
        shell_command = shell_command.split(" ")[1]
    return shell_command


# tags to enable for certain shell names
shell_tags = {
    "zsh": ["terminal"],
    "bash": ["terminal"],
    "sh": ["terminal"],
    "ssh": ["terminal"],
    "sudo": ["terminal"],
    "gdb": ["user.gdb"],
    "pwndbg": ["user.gdb", "user.pwndbg"],
    "gef": ["user.gdb", "user.gef"],
    "htop": ["user.htop"],
    "taskwarrior-tui": ["user.taskwarrior_tui"],
    "~/.talon/bin/repl": ["user.talon_repl"],
    # "~/.talon/bin/repl": ["user.talon_repl", "user.python"], # Doesn't work because of the switch back to language modes
    # "python": ["user.python"], # Doesn't work because of the switch back to language modes
    # NOTE: we are using specific tags so we can enable the responding app commands
    "C:\\Windows\\system32\\cmd.exe": [
        "user.vim_terminal_cmd"
    ],  # "terminal" not needed because "vim_terminal_cmd" triggers it among other things
    "Talon - REPL": ["user.vim_terminal_repl"],
}

# tags to enable for certain shell commands
# XXX - there's probably a better way to deal with this
fuzzy_shell_tags = {
    # Match on stuff like fzf running in floating term
    # "term://": ["user.readline"],
    "root@": ["terminal"],  # hacky match for docker containers
    # "python:": ["user.python"], # Doesn't work because of the switch back to language modes
}

# tags to enable for certain shell regular expressions
# XXX - should I pre compile these so we don't do it on every single window
# update?
regex_shell_tags = {
    r"^\w*@\w*": ["terminal"],
    # this is redundant with above, but ideally I would rather have something like this
    r"^\w*@\w*:.*[$#]": ["terminal"],
    ".*virsh start --console.*": ["terminal"],  # hacky match for libvirt containers
}


def title_set_tags(shell_command, window_title):
    """TODO: Docstring for title_set_tags.
    :returns: TODO

    """
    print(f"title_set_tags(shell_command={shell_command},window_title={window_title})")

    tags = []
    print(f"title_set_tags(): trying shell command")
    if shell_command in shell_tags:
        print(f"title_set_tags(): found shell command: {shell_command}")
        tags = shell_tags[shell_command]
        return tags

    print(f"title_set_tags(): trying fuzzy")
    for prompt in fuzzy_shell_tags:
        if shell_command.startswith(prompt):
            print(f"title_set_tags(): found fuzzy prompt: {prompt}")
            tags = [fuzzy_shell_tags[prompt]]
            return tags

    print(f"title_set_tags(): trying expression")
    for expression in regex_shell_tags:
        m = re.match(expression, shell_command)
        if m is not None:
            tags = [regex_shell_tags[expression]]
            print(f"title_set_tags(): found expression: {expression} in shell command")
            return tags
        m = re.match(expression, window_title)
        if m is not None:
            tags = [regex_shell_tags[expression]]
            print(f"title_set_tags(): found expression: {expression} in window title")
            return tags

    print(
        f"WARNING: missing support for shell command: {shell_command}, consider updating vim_terminal_mode.py"
    )

    return tags


language_specific_commands = {
    "repl": "python",
}


def title_set_languages(shell_command):
    """Tries to enable language modes based off special cases of programs being
    run, for instance running debuggers to enable gdb language, or running
    repl to enable python language

    :shell_command: The shell command being run by the terminal
    """

    for command in language_specific_commands.keys():
        if shell_command.endswith(command):
            print("vim_terminal_mode.py: setting context-specific language")
            actions.user.code_set_context_language(language_specific_commands[command])
            return

    # XXX - sometimes this throws an exception saying it's not declared, but it
    # should be a global module action from code.py
    # Why do I clear the context language if there's no match?
    # actions.user.code_clear_context_language()
    return


def title_win_title_hook(window):
    print(f"title_win_title_hook(window={window})")
    title_parse_TERM(window)


def title_win_focus_hook(window):
    print(f"title_win_focus_hook(window={window})")
    title_parse_TERM(window)


def register_events():
    ui.register("win_title", title_win_title_hook)
    ui.register("win_focus", title_win_focus_hook)


app.register("ready", register_events)
