tag: user.vim_mode_insert
-
# tag(): user.vim_luasnip
# tag(): user.vim_nvim_cmp

(dup | duplicate) line:
    user.vim_run_normal_np("yyp")

yank line:
    user.vim_run_normal_np("yy")

push:
    key('end')

push <user.key_unmodified>:
    key('end')
    key('{key_unmodified}')

push it:
    key('end')
    edit.paste()
