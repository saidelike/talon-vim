from enum import Enum

from talon import Context, Module, actions

from ..vim.vim import VimError

mod = Module()
ctx_normal_terminal = Context()


ctx_normal_terminal.matches = r"""
tag: user.vim_normal_mode
and win.title: /VIM MODE:nt/
"""


# this allows using "bring" in normal terminal mode and that will insert
# into the previous position in the terminal mode
@ctx_normal_terminal.action_class("main")
class MainActions:
    def insert(text):
        actions.user.vim_set_insert_mode()
        actions.next(text)


class TargetType(Enum):
    WORD = 1
    LINE = 2


class ActionType(Enum):
    COPY = 1
    BRING = 2


@mod.action_class
class Actions:

    # ----- (copy|bring) [tail line] fuzzy <text> [row <number>] -----

    def copy_tail_line_fuzzy(text: str):
        """copy the content of the line from the text found with fuzzy search to the clipboard"""
        actions.user.act_tail_line_fuzzy(ActionType.COPY, text)

    def bring_tail_line_fuzzy(text: str):
        """bring the content of the line from the text found with fuzzy search to the current position"""
        actions.user.act_tail_line_fuzzy(ActionType.BRING, text)

    def copy_tail_line_fuzzy_row(text: str, row: int):
        """copy the content of the specified line from the text found with fuzzy search to the clipboard"""
        actions.user.act_tail_line_fuzzy(ActionType.COPY, text, row)

    def bring_tail_line_fuzzy_row(text: str, row: int):
        """bring the content of the specified line from the text found with fuzzy search to the current position"""
        actions.user.act_tail_line_fuzzy(ActionType.BRING, text, row)

    def act_tail_line_fuzzy(action_type: ActionType, text: str, row: int = None):
        """act on the content of the (potentially specified) line from the text found with fuzzy search"""
        ret = actions.user.vim_normal_mode_exterm()
        if row is not None:
            actions.user.move_up(row)
            actions.user.move_to_column_zero()
            actions.user.fuzzy_search_current_line(f"{text}")
        else:
            actions.user.fuzzy_search_backward(f"{text}")
        actions.user.yank_to_end_of_line()
        # this doesn't seem to be needed (on Windows)
        # actions.user.highlights_matches_from_previous_search(False)
        if action_type == ActionType.COPY:
            # do not go back to terminal mode if we were currently scrolling in normal mode
            if ret == VimError.SUCCESS:
                actions.user.vim_set_insert_mode()
        elif action_type == ActionType.BRING:
            actions.user.paste_after_cursor()
            actions.user.vim_set_insert_mode()
            # append a space after the brought line
            actions.key("space")

    # ----- (copy|bring) [tail line] <ordinal> paint row <number> -----

    def copy_paint_row(paint: int, row: int):
        """copy the nth paint of the specified line to the clipboard"""
        actions.user.act_paint_row(ActionType.COPY, paint, row)

    def bring_paint_row(paint: int, row: int):
        """bring the nth paint of the specified line to the current position"""
        actions.user.act_paint_row(ActionType.BRING, paint, row)

    def copy_tail_line_paint_row(paint: int, row: int):
        """copy the content of the specified line from the paint number to the clipboard"""
        actions.user.act_paint_row(ActionType.COPY, paint, row, tail_line=True)

    def bring_tail_line_paint_row(paint: int, row: int):
        """bring the content of the specified line from the paint number to the current position"""
        actions.user.act_paint_row(ActionType.BRING, paint, row, tail_line=True)

    # paint: 0 means the first paint, 1 means the second paint, etc.
    #       -1 means the last paint, -2 means the second last paint, etc.
    # tail_line: if True, it will copy from the paint to the end of the line instead of just the paint
    # Known issues:
    # "copy second last paint row one" will copy "|  ........^.h.xV4."
    # instead of just the "|" from the current line:
    # 0xa8c3c480: b0 c1 c3 a8 80 c9 c3 a8 5e 87 68 08 78 56 34 12  |  ........^.h.xV4.
    def act_paint_row(
        action_type: ActionType, paint: int, row: int, tail_line: bool = False
    ):
        """act on the nth paint of the specified line"""
        ret = actions.user.vim_normal_mode_exterm()
        actions.user.move_up(row)
        if paint >= 0:
            actions.user.move_to_column_zero()
            actions.user.move_next_word(paint)
        else:
            actions.user.move_to_beginning_of_the_last_word()
            actions.user.move_previous_word(-paint - 1)
        if tail_line:
            actions.user.yank_to_end_of_line()
        else:
            # this doesn't seem to be needed (on Windows)
            # sometimes there are extra whitespace that get copied so this trims it
            # TODO: make it its own action when we need it
            # See `:help pattern`
            # \_s   - match single white space
            # \{2,} - at least two in a row
            # actions.user.vim_command_mode(":set nohls | let @+=substitute(strtrans(@+), '\\_s\\{{2,}}', '', 'g')\n")
            actions.user.yank_to_end_of_word()
        if action_type == ActionType.COPY:
            # do not go back to terminal mode if we were currently scrolling in normal mode
            if ret == VimError.SUCCESS:
                actions.user.vim_set_insert_mode()
        elif action_type == ActionType.BRING:
            actions.user.paste_after_cursor()
            actions.user.vim_set_insert_mode()
            # append a space after the brought line
            actions.key("space")

    # ----- (copy|bring) row <number> -----

    def copy_row(row: int):
        """copy the content of the specified line to the clipboard"""
        actions.user.act_row(ActionType.COPY, row)

    def bring_row(row: int):
        """bring the content of the specified line to the current position"""
        actions.user.act_row(ActionType.BRING, row)

    def act_row(action_type: ActionType, row: int):
        """act on the specified line"""
        ret = actions.user.vim_normal_mode_exterm()
        actions.user.move_up(row)
        actions.user.move_to_column_zero()
        actions.user.yank_to_end_of_line()
        # user.vim_command_mode(":let @+=substitute(strtrans(@+), '\\_s\\{{2,}}', '', 'g')\n")
        if action_type == ActionType.COPY:
            # do not go back to terminal mode if we were currently scrolling in normal mode
            if ret == VimError.SUCCESS:
                actions.user.vim_set_insert_mode()
        elif action_type == ActionType.BRING:
            actions.user.paste_after_cursor()
            actions.user.vim_set_insert_mode()
            # append a space after the brought line
            actions.key("space")

    # ----- (copy|bring) [tail] paint first glyph <character> row <number> -----

    def copy_paint_first_glyph_row(glyph: str, row: int):
        """copy the first found paint containing the specified key/letter(=glyph) in the specified line to the clipboard"""
        actions.user.act_paint_first_glyph_row(ActionType.COPY, glyph, row)

    def copy_tail_paint_first_glyph_row(glyph: str, row: int):
        """copy the end of the first found paint containing the specified key/letter(=glyph) in the specified line to the clipboard"""
        actions.user.act_paint_first_glyph_row(
            ActionType.COPY, glyph, row, tail_paint=True
        )

    def bring_paint_first_glyph_row(glyph: str, row: int):
        """bring the first found paint containing the specified key/letter(=glyph) in the specified line to the current position"""
        actions.user.act_paint_first_glyph_row(ActionType.BRING, glyph, row)

    def bring_tail_paint_first_glyph_row(glyph: str, row: int):
        """bring the end of the first found paint containing the specified key/letter(=glyph) in the specified line to the current position"""
        actions.user.act_paint_first_glyph_row(
            ActionType.BRING, glyph, row, tail_paint=True
        )

    # avoid having to count how many words, though not really reliable
    # due to the fact you have to check the key/letter you say is not in a word before the one you target
    # but also because if the key/letter is not found, it will just copy the first word
    def act_paint_first_glyph_row(
        action_type: ActionType, glyph: str, row: int, tail_paint: bool = False
    ):
        """act on the first found paint containing the key/letter(=glyph) in the specified line"""
        ret = actions.user.vim_normal_mode_exterm()
        actions.user.move_up(row)
        actions.user.move_to_column_zero()
        actions.user.find_character(glyph)
        if tail_paint:
            actions.user.yank_to_end_of_word()
        else:
            actions.user.yank_current_word()
        if action_type == ActionType.COPY:
            # do not go back to terminal mode if we were currently scrolling in normal mode
            if ret == VimError.SUCCESS:
                actions.user.vim_set_insert_mode()
        elif action_type == ActionType.BRING:
            actions.user.paste_after_cursor()
            actions.user.vim_set_insert_mode()
            # append a space after the brought line
            actions.key("space")
            # this doesn't seem to be needed (on Windows)
            # TODO: make it its own action when we need it
            # disable weird highlight
            # actions.key("down:5")
