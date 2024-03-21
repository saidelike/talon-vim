from talon import Context, Module, actions, clip
import re

mod = Module()


# we define new actions that are "edition" related
@mod.action_class
class Actions:
    # ----- Vim -----
    def line_find_forward(key: str):
        """Finds the next character in the line"""

    def line_find_backward(key: str):
        """Finds the previous character in the line"""

    def delete_line_beginning():
        """Delete to beginning of current line"""
        actions.edit.extend_line_start()
        actions.edit.delete()

    def delete_line_remaining():
        """Delete to end of current line"""
        actions.edit.extend_line_beginning()
        actions.edit.delete()

    # TODO: merge with draft_editor_submit
    def draft_app_submit(text: str):
        """Submit drafted text ot editor"""
        actions.user.paste(text)
