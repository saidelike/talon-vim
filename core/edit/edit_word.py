from talon import Context, actions

ctx_command = Context()
ctx_command.matches = r"""
tag: user.vim_mode_command
"""


@ctx_command.action_class("edit")
class EditActions:
    def word_left():
        actions.key("shift-left")

    def word_right():
        actions.key("shift-right")


@ctx_command.action_class("user")
class UserActions:
    def delete_word_left():
        actions.key("ctrl-w")
