import re
import time
from timeit import default_timer as timer

from talon import Context, Module, actions, app, settings, ui

mod = Module()

ctx = Context()
ctx.matches = r"""
tag: user.vim_mode_terminal
"""


@ctx.action_class("edit")
class EditActions:
    def page_up():
        actions.key("ctrl-\\ ctrl-n ctrl-b")

    # XXX - this might be a bit much if eventually we want this to mean to let
    # everything on the command-line itself, although then we might be able to
    # just use things like select line/graph, etc
    def select_all():
        actions.user.vim_run_normal_exterm("ggVG")

    def select_line(n: int = None):
        if n is not None:
            app.notify(
                "vim_terminal_mode.py: select_line() with argument not implemented"
            )
            return
        actions.user.vim_run_normal_exterm("V")
        time.sleep(1)

    # def paste():
    #     actions.key("ctrl-shift-v")
    # https://stackoverflow.com/questions/54734173/how-to-copy-and-paste-in-vims-terminal-mode
    def paste():
        actions.user.vim_run_normal_exterm()
        # actions.key("ctrl-v")
        actions.next()
        actions.user.vim_set_insert()


# @mod.action_class
# class Actions:
#     # FIXME: This needs to import VimMode() from vim.py I guess?
#     def vim_set_normal():
#         """set normal mode"""
#         v = VimMode()
#         v.set_normal_mode(auto=False)
