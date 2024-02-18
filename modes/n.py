from talon import Context, Module, actions

mod = Module()


@mod.action_class
class Actions:
    # ----- Move -----
    def move_to_column_zero():
        """jump to the start of the line: 0"""
        # https://vim.rtorr.com/
        actions.key("0")

    def move_up(n: int):
        """move up n lines: {n}k"""
        # https://stackoverflow.com/questions/4917030/move-cursor-x-lines-from-current-position-in-vi-vim
        actions.insert(f"{n}k")

    def move_next_word(n: int):
        """move to the next WORD(=paint) n times on the current line from the current position: {n}W"""
        # see :h WORDS
        # A WORD consists of a sequence of non-blank characters, separated with white
        # space.  An empty line is also considered to be a WORD.
        # see :h W
        # 0 means do nothing, 1 means move to the next word, etc.
        if n > 0:
            actions.insert(f"{n}W")

    def move_previous_word(n: int):
        """move to the previous WORD(=paint) n times on the current line from the current position: {n}B"""
        # see :h B
        # 0 means do nothing, 1 means move to the previous word, etc.
        if n > 0:
            actions.insert(f"{n}B")

    def move_to_beginning_of_the_last_word():
        """move to the beginning of the last WORD(=paint) of the line from the current position: '$T '"""
        # see :h $
        # To the end of the line.
        # see :h T
        # "T ": Till after first occurrence of the "space" to the left.
        actions.insert(f"$T ")

    def move_to_end_of_line():
        """move to the end of the line from the current position: '$'"""
        # see :h $
        # To the end of the line.
        actions.insert(f"$")

    # NOTE: it is not safe to move to use it if we're on the first word
    # because it won't do anything if there is no space before this first word
    def move_to_beginning_of_the_word():
        """move to the beginning of the current WORD(=paint) from the current position: 'T '"""
        # see :h T
        # "T ": Till after first occurrence of the "space" to the left.
        actions.insert(f"T ")

    # ----- Copy -----
    def yank_current_word():
        """yank the current WORD(=paint): yE"""
        # see :h iW
        # "inner WORD"
        actions.insert(f"yiW")

    def yank_to_end_of_word():
        """yank to the end of the current WORD(=paint): yE"""
        # see :h E
        # Forward to the end of WORD [count] |inclusive|.
        # Does not stop in an empty line.
        actions.insert(f"yE")

    def yank_to_end_of_line():
        """yank to the end of the current line: y$"""
        # https://vim.fandom.com/wiki/Copy,_cut_and_paste
        actions.insert("y$")

    # ----- Paste -----
    def paste_after_cursor():
        """paste after the cursor: p"""
        # https://vim.fandom.com/wiki/Copy,_cut_and_paste#Pasting_in_normal_mode
        actions.key("p")

    # ----- Search -----
    # NOTE: it's not safe to use it because it won't move the cursor if the text is not found
    def fuzzy_search_backward(text: str):
        """search for the regex's text backward and move the cursor to that position"""
        # https://stackoverflow.com/questions/8676070/how-to-search-using-the-value-returned-by-function/8676233#8676233
        # see :h search()
        # b: search Backward instead of forward
        # c: accept a match at the Cursor position
        # W: don't Wrap around the end of the file
        actions.insert(f":call search(\"{text}\", 'bcW')\n")

    # NOTE: it's not safe to use it because it won't move the cursor if the text is not found
    def fuzzy_search_current_line(text: str):
        """search for the regex's text, stopping the search after this line, and move the cursor to that position"""
        # see :h search()
        # c: accept a match at the Cursor position
        # line('.'): stop the search after this line (instead of the whole file)
        actions.insert(f":call search(\"{text}\", 'c', line('.'))\n")

    # NOTE: it's not safe to use it because it won't move the cursor if the character is not found
    def find_character(character: str):
        """move to the next occurrence of the specified character in the line from the current position: 'f{c}'"""
        # see :h f
        # To first occurrence of {char} to the right.
        actions.insert(f"f{character}")

    # ----- Various -----
    def highlights_matches_from_previous_search(enable: bool = True):
        """highlight all matches from the previous search"""
        # https://vim.fandom.com/wiki/Highlight_all_search_pattern_matches
        if enable:
            actions.insert(":set hlsearch\n")
        else:
            actions.insert(":set nohlsearch\n")
