from talon import Context, Module, actions, clip
import re

mod = Module()


# we define new actions that are "edition" related
@mod.action_class
class Actions:
    # TODO: merge with draft_editor_submit
    def draft_app_submit(text: str):
        """Submit drafted text ot editor"""
        actions.user.paste(text)
