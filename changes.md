<!-- vim-markdown-toc GFM -->

- [this need to be reverted for the final public version](#this-need-to-be-reverted-for-the-final-public-version)
- [pasting on Linux](#pasting-on-linux)

<!-- vim-markdown-toc -->

# this need to be reverted for the final public version

unmodified_key => key_unmodified
https://github.com/talonhub/community/blob/fce77d0a1a3825cc77ea91b487b4276024ec475f/core/keys/keys.py#L96
https://github.com/AndreasArvidsson/andreas-talon/blob/master/core/keys/keys.py#L45

# pasting on Linux

the below I have tested on windows actually should work everywhere. this is because I used the command `p` instead of `edit.paste()`

```talon
bring (line|row) <number_small>:
    user.vim_normal_mode_exterm("{number_small}k")
    key("0")
    insert("y$")
    # works on windows
    key('p')
    user.vim_set_insert_mode()
    # works on linux
    # edit.paste()
    key(space)
```
