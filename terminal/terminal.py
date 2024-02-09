from talon import Module, Context, actions

mod = Module()
# ctx = Context()
# ctx.matches = r"""
# tag: user.vim_terminal
# """


@mod.action_class
class Actions:
    def bring_line(row: int):
        """bring the content of the specified line to the current position"""
        actions.user.vim_normal_mode_exterm()
        actions.user.move_to_column_zero()
        actions.user.yank_to_end_of_line()
        actions.user.paste_after_cursor()
        actions.user.vim_set_insert_mode()
        # append a space after the brought line
        actions.key("space")

    def bring_tail_line_fuzzy(text: str):
        """bring the content of the line from the text found with fuzzy search to the current position"""
        actions.user.vim_normal_mode_exterm()
        actions.user.fuzzy_search_backward(f"{text}")
        actions.user.yank_to_end_of_line()
        # this doesn't seem to be needed (on Windows)
        # actions.user.highlights_matches_from_previous_search(False)
        actions.user.paste_after_cursor()
        actions.user.vim_set_insert_mode()

    def bring_tail_line_fuzzy_row(text: str, row: int):
        """bring the content of the specified line from the text found with fuzzy search to the current position"""
        actions.user.vim_normal_mode_exterm()
        actions.user.move_up(f"{row}")
        actions.user.move_to_column_zero()
        actions.user.fuzzy_search_current_line(f"{text}")
        actions.user.yank_to_end_of_line()
        # this doesn't seem to be needed (on Windows)
        # actions.user.highlights_matches_from_previous_search(False)
        actions.user.paste_after_cursor()
        actions.user.vim_set_insert_mode()
