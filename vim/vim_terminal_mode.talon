tag: user.vim_mode_terminal
-

normal [mode]:
    key(ctrl-\ ctrl-n)
poppy:
    key(ctrl-\ ctrl-n)

# pop terminal mode and scroll up once, from this point onward you can scroll
# like normal
# TODO: not working
scroll up:
    key(ctrl-\ ctrl-n ctrl-b)

# this causes exclusive terminal windows to exit without requiring key press or
# dropping to a new empty buffer
exit (terminal | term):
    key(ctrl-\)
    key(ctrl-n)
    insert("ZQ")

# TODO: seems not useful to port here? or move to different file?

# copy a function name on the specified line
# XXX - it would be nice to have this you something like treesitter on a single
# line (even though it would be broken syntax) and be able to specify which
# element we want...
# copy funk name row <number_small>:
yank words <number_small> funk:
    user.vim_run_normal_exterm()
    user.move_up(number_small)
    user.move_to_column_zero()
    # see :h f
    # To first occurrence of "left parenthesis" to the right.
    insert("f(")
    # see :h B
    # yank WORD(=paint) backward
    insert("yB")
    user.vim_set_insert()

# copy a function name on the specified line
# XXX - it would be nice to have this you something like treesitter on a single
# line (even though it would be broken syntax) and be able to specify which
# element we want...
# bring funk name row <number_small>:
bring <number_small> funk:
    user.vim_run_normal_exterm()
    user.move_up(number_small)
    user.move_to_column_zero()
    insert("f(")
    insert("yB")

    user.paste_after_cursor()
    user.vim_set_insert()
    # edit.paste()
    # disable weird highlight
    key(down:5)

# TODO: continue from here

yank line command:
    user.vim_run_normal_exterm("0f y$")
    user.vim_run_command(":let @+=substitute(strtrans(@+), '\\_s\\{{2,}}', '', 'g')\n")
    user.vim_set_insert()

    # this is used for pexpect interactive environments
    # https://pexpect.readthedocs.io/en/stable/api/pexpect.html#spawn-class
    # note that you can't use this from within command line itself, because the
    # terminal may not trigger depending on what the interactive command is. who
    # had actually needs to be global

python escape:
    key(ctrl-])

# this assumes you list some directories with find or whatever, then you want
# to pivot into one of them based on what was listed. you say the relative
# number, and it will jump to that point, copy the line and then jump you in
pivot line <number_small>:
    insert("cd ")
    user.vim_run_normal_exterm()
    user.move_up(number_small)
    user.move_to_column_zero()
    user.yank_to_end_of_line()
    user.vim_run_command(":let @+=substitute(strtrans(@+), '\\_s\\{{2,}}', '', 'g')\n")
    user.paste_after_cursor()
    user.vim_set_insert()
    # edit.paste()
    key(enter)

pivot river <number_small>:
    insert("cd ")
    user.vim_run_normal_exterm()
    user.move_up(number_small)
    user.move_to_column_zero()
    key(ctrl-w)
    key(f)

pivot pillar <number_small>:
    insert("cd ")
    user.vim_run_normal_exterm()
    user.move_up(number_small)
    user.move_to_column_zero()
    user.vim_run_command(":vertical wincmd f\n")

edit line <number_small>:
    user.vim_run_normal_exterm()
    user.move_up(number_small)
    user.move_to_column_zero()
    insert("gf")

river line <number_small>:
    user.vim_run_normal_exterm()
    user.move_up(number_small)
    user.move_to_column_zero()
    key('ctrl-w')
    key('f')

pillar line <number_small>:
    user.vim_run_normal_exterm()
    user.move_up(number_small)
    user.move_to_column_zero()
    user.vim_run_command(":vertical wincmd f\n")

# Combine the pwd with the path at a relative offset and place the result in
# the clipboard
folder yank merge <number_small>:
    user.vim_run_command_exterm(":let @+ = getcwd() . '/'\n")
    user.vim_run_normal("{number_small}k0")
    user.vim_run_command(":let @+ .= substitute(strtrans(getline('.')), '\\_s\\{{2,}}', '', 'g')\n")
    user.vim_set_insert()

# TODO: seems not useful to port here? or move to different file?

# this assumes you executed the "ps" command
# $ ps
#        PID    PPID    PGID     WINPID   TTY         UID    STIME COMMAND
#       1886       1    1886      14988  cons3     197610   Feb  8 /usr/bin/bash
#  S    2355    2222    2355      34704  cons5     197610 16:06:25 /usr/bin/bash
# TODO: what cursorless command could we use?
process kill line <number_small>:
    insert("kill -9 ")
    user.vim_run_normal_exterm()
    user.move_up(number_small)
    key('0 w y e')
    user.paste_after_cursor()
    user.vim_set_insert()
    key(right)
