tag: user.vim_normal_mode
-

(shift | indent) right:
    insert(">>")
(shift | indent) left:
    insert("<<")

(dup | duplicate) line:
    insert("yy")
    insert("p")

yank line:
    insert("yy")

push:
    user.vim_normal_mode_np("$a")

# NOTE - We need a separate key() call because some unmodified keys have
# special names, like backspace.
push <user.key_unmodified>:
    user.vim_normal_mode_np("$a")
    key('{key_unmodified}')

# paste to the end of a line
# XXX
push it:
    user.vim_normal_mode_np("A ")
    key(escape p)
