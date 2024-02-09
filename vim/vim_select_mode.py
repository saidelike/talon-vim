from talon import Context, actions

ctx_title = Context()
ctx_title.matches = r"""
win.title: /VIM MODE:s/
"""
ctx_title.tags = ["user.vim_select_mode"]


ctx = Context()
ctx.matches = r"""
tag: user.vim_select_mode
"""
