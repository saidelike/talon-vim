tag: user.vim_terminal_mode
tag: user.vim_normal_mode
and win.title: /VIM MODE:nt/
-

# this conflicts with cursorless-neovim so disabling it for now
# Cursorless spoken forms
# copy row <number_small>:
#     user.copy_row(number_small)
# bring row <number_small>:
#     user.bring_row(number_small)

# copy tail line fuzzy <user.text>:
#     user.copy_tail_line_fuzzy(text)
# bring tail line fuzzy <user.text>:
#     user.bring_tail_line_fuzzy(text)

# copy tail line fuzzy <user.text> row <number_small>:
#     user.copy_tail_line_fuzzy_row(text, number_small)
# bring tail line fuzzy <user.text> row <number_small>:
#     user.bring_tail_line_fuzzy_row(text, number_small)

# copy <user.ordinal_or_last> paint row <number_small>:
#     user.copy_paint_row(ordinal_or_last, number_small)
# bring <user.ordinal_or_last> paint row <number_small>:
#     user.bring_paint_row(ordinal_or_last, number_small)

# copy tail line <user.ordinals> paint row <number_small>:
#     user.copy_tail_line_paint_row(ordinals, number_small)
# bring tail line <user.ordinals> paint row <number_small>:
#     user.bring_tail_line_paint_row(ordinals, number_small)

# copy paint first glyph <user.key_unmodified> row <number_small>:
#     user.copy_paint_first_glyph_row(key_unmodified, number_small)
# bring paint first glyph <user.key_unmodified> row <number_small>:
#     user.bring_paint_first_glyph_row(key_unmodified, number_small)

# copy tail paint first glyph <user.key_unmodified> row <number_small>:
#     user.copy_tail_paint_first_glyph_row(key_unmodified, number_small)
# bring tail paint first glyph <user.key_unmodified> row <number_small>:
#     user.bring_tail_paint_first_glyph_row(key_unmodified, number_small)

# old spoken forms
yank line <number_small>:
    user.copy_row(number_small)
bring line <number_small>:
    user.bring_row(number_small)
bring line fuzzy <user.text>$:
    user.bring_tail_line_fuzzy(text)
bring line <number_small> <user.text>:
    user.bring_tail_line_fuzzy_row(text, number_small)
bring line <number_small> <user.ordinals>:
    user.bring_tail_line_paint_row(ordinals, number_small)
yank line <number_small> <user.ordinals>:
    user.copy_tail_line_paint_row(ordinals, number_small)
yank [words] <number_small>:
    user.copy_paint_row(1, number_small)
yank [words] <number_small> <user.ordinals>:
    user.copy_paint_row(ordinals, number_small)
yank [words] (last <number_small> | <number_small> last):
    user.copy_paint_row(-1, number_small)
yank [words] <number_small> <user.key_unmodified>:
    user.copy_tail_paint_first_glyph_row(key_unmodified, number_small)
bring [words] (last <number_small> | <number_small> last):
    user.bring_paint_row(-1, number_small)
bring [words] <number_small>:
    user.bring_paint_row(1, number_small)
bring [words] <number_small> <user.ordinals>:
    user.bring_paint_row(ordinal_or_last, number_small)
bring [words] <number_small> <user.key_unmodified>:
    user.bring_tail_paint_first_glyph_row(key_unmodified, number_small)
