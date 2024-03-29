from talon import Context, actions

# This matches when were are in normal mode in a terminal buffer. If we do a draft line
# on a command line, we want to special case the reinsertion of the drafted text, so we
# override the action here. This is a bit of a hack, but it works.

# TODO: commenting for now since we are only enabling terminal mode when nt is enabled: this needs to be changed now
# ctx_title = Context()
# ctx_title.matches = r"""
# win.title: /VIM MODE:nt/
# """
# TODO: "nt" is supposed to enable terminal mode only
# ctx_title.tags = ["user.vim_mode_normal", "user.vim_mode_terminal"]

# ctx = Context()
# ctx.matches = r"""
# tag: user.vim_mode_normal
# and tag: user.vim_mode_terminal
# """


# @ctx.action_class("user")
# class UserActions:
#     def draft_app_submit(text: str):
#         # Re-enter terminal mode
#         actions.user.vim_set_terminal()
#         actions.sleep("100ms")
#         # actions.insert("i")
#         actions.sleep("100ms")
#         # Kill the existing command line
#         actions.key("ctrl-a ctrl-k")
#         # Re-insert the drafted text
#         actions.user.paste(text)
