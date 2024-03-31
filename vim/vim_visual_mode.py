import logging
import pprint

from talon import Context, Module, actions, clip

mod = Module()
mod.list("vim_visual_actions", desc="Vim visual mode actions")
mod.list(
    "vim_visual_counted_actions", desc="Vim visual mode actions that can be repeated"
)

ctx = Context()
ctx.matches = r"""
tag: user.vim_mode_visual
"""

# These override the ones in normal mode currently set in vim.py
ctx.lists["user.vim_visual_actions"] = {
    "yank": "y",
    "opposite": "o",
    "drop": "d",
}

ctx.lists["user.vim_visual_counted_actions"] = {
    "dedent": "<",
    "indent": ">",
}
