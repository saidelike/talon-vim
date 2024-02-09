from talon import Context, Module, actions, app, ui, cron, settings
from ..vim.vim import NeoVimRPC

ctx = Context()

monitor_job = None
nvrpc = None
tags: set[str] = set()


def win_focus_hook(window):
    global monitor_job, nvrpc

    current_title = window.title
    print(f"current_title={current_title}")
    if current_title.startswith("VIM MODE:"):
        # TODO: is it the right way to initialize this NeoVimRPC?
        if nvrpc is None:
            nvrpc = NeoVimRPC()
        # TODO: change this to 100ms
        monitor_job = cron.interval("1000ms", vim_monitor_mode)
    else:
        if monitor_job:
            cron.cancel(monitor_job)
            monitor_job = None


def vim_monitor_mode():
    global nvrpc, ctx, tags

    tags = set(ctx.tags)
    if nvrpc.init_ok is True:
        mode = nvrpc.get_active_mode()["mode"]
        print(f"nvrpc: mode={mode}")
        # TODO: is "nt" supposed to enable both normal and terminal modes? or just terminal one? see vim_normal_term_mode.py
        if "n" in mode:
            tags.add("user.vim_normal_mode")
        else:
            tags.discard("user.vim_normal_mode")
        if "i" in mode:
            tags.add("user.vim_insert_mode")
        else:
            tags.discard("user.vim_insert_mode")
        if "s" in mode:
            tags.add("user.vim_select_mode")
        else:
            tags.discard("user.vim_select_mode")
        if "t" in mode:
            tags.add("user.vim_terminal")
        else:
            tags.discard("user.vim_terminal")
        if "c" in mode:
            tags.add("user.vim_command_mode")
        else:
            tags.discard("user.vim_command_mode")
        if "v" in mode or "V" in mode:
            tags.add("user.vim_visual_mode")
        else:
            tags.discard("user.vim_visual_mode")
        ctx.tags = tags
    else:
        print(f"nvrpc is not initialized")


def register_events():
    ui.register("win_focus", win_focus_hook)


app.register("ready", register_events)
