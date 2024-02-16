from talon import Module

mod = Module()

mod.apps.cmd = r"""
app: vim
win.title: /TERM:C:\\Windows\\system32\\cmd.exe/
"""

mod.apps.repl = r"""
app: vim
win.title: /TERM:Talon - REPL/
"""

mod.apps.git_bash = r"""
app: vim
win.title: /TERM:MINGW64/
"""

# this assumes this change in ~/.bashrc in wsl
# case "$TERM" in
# xterm*|rxvt*)
#   PS1="\[\e]0;${debian_chroot:+($debian_chroot)}wsl: \w\a\]$PS1"
mod.apps.wsl = r"""
app: vim
win.title: /TERM:wsl/
"""
