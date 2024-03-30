# File is for any sort of generic file editing that works in most modes. If you
# want to add something with more restricted modes then you should pick one of
# the different by them files.
from talon import Context, actions

ctx = Context()
ctx.matches = r"""
app:vim
and not tag: user.vim_mode_command
"""


# Since this file includes anything that could by running in terminal mode or
# other modes, they should use the exterm version of the API in almost all
# cases.
@ctx.action_class("edit")
class EditActions:
    # ----- Navigation -----
    def up():
        actions.key("up")

    def down():
        actions.key("down")

    def left():
        actions.key("left")

    def right():
        actions.key("right")

    def page_up():
        # Use ctrl-u for half page. Use ctrl-b for full page

        # actions.user.vim_run_normal_exterm_key("ctrl-u")
        actions.user.vim_run_normal_exterm_key("ctrl-b")

    def page_down():
        # Use ctrl-d for half page. Use ctrl-f for full page
        # actions.user.vim_run_normal_exterm_key("ctrl-d")
        actions.user.vim_run_normal_exterm_key("ctrl-f")

    # ----- Find -----
    def find(text: str = None):
        actions.user.vim_run_normal_exterm_key("/")
        # TODO: support inserting text to find
        # if text:
        #     actions.insert(text)

    # ----- Zoom -----
    # FIXME: This wrong depending on the terminal. Gnome is ctrl--
    def zoom_out():
        actions.key("ctrl-shift--")

    def zoom_in():
        actions.key("ctrl-shift-+")
