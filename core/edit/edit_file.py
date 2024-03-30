from talon import Context, actions

# Context valid in some sort of motion mode, so not including terminal or command mode
ctx_motion = Context()
ctx_motion.matches = r"""
app:vim
not tag: user.vim_mode_terminal
and not tag: user.vim_mode_command
"""


@ctx_motion.action_class("edit")
class EditActions:
    def file_start():
        actions.user.vim_run_any_motion("gg")

    def file_end():
        actions.user.vim_run_any_motion_key("G")

    def select_all():
        actions.user.vim_run_normal("ggVG")
        # See vim_normal.talon and vim_visual.talon for edit.extend_ commands

    def extend_file_start():
        actions.user.vim_run_visual("gg0")

    def extend_file_end():
        actions.user.vim_run_visual("G")
