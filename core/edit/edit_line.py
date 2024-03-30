from talon import Context, actions

ctx_command = Context()
ctx_command.matches = r"""
tag: user.vim_mode_command
"""


@ctx_command.action_class("edit")
class EditActions:
    def line_start():
        actions.key("ctrl-b")

    def line_end():
        actions.key("ctrl-e")

    def delete_line():
        actions.key("ctrl-u")
