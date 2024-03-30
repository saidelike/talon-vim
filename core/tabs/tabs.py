from talon import Context, actions

# TODO: should we also match tag: user.tabs or tabs are always present anyway so does not matter?
ctx = Context()
ctx.matches = r"""
app: vim
and not tag: user.vim_mode_command
"""


@ctx.action_class("app")
class AppActions:
    def tab_open():
        actions.user.vim_run_command_exterm(":tabnew\n")

    def tab_close():
        actions.user.vim_run_command_exterm(":tabclose\n")

    def tab_next():
        actions.user.vim_run_command_exterm(":tabnext\n")

    def tab_previous():
        actions.user.vim_run_command_exterm(":tabprevious\n")
