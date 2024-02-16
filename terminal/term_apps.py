from talon import Module

mod = Module()

mod.apps.cmd = r"""
win.title: /TERM:C:\\Windows\\system32\\cmd.exe/
"""

mod.apps.repl = r"""
win.title: /TERM:Talon - REPL/
"""

mod.apps.git_bash = r"""
win.title: /TERM:MINGW64/
"""

# this assumes this change in ~/.bashrc in wsl
# case "$TERM" in
# xterm*|rxvt*)
#   PS1="\[\e]0;${debian_chroot:+($debian_chroot)}wsl: \w\a\]$PS1"
mod.apps.wsl = r"""
win.title: /TERM:wsl/
"""
