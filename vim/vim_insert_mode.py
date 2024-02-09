from talon import Context, actions

ctx_title = Context()
ctx_title.matches = r"""
win.title: /VIM MODE:i/
"""
ctx_title.tags = ["user.vim_insert_mode"]


ctx = Context()
ctx.matches = r"""
tag: user.vim_insert_mode
"""


@ctx.action_class("edit")
class EditActions:
    def delete_line():
        actions.user.vim_normal_mode("dd")
