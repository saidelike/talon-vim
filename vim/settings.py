from talon import Context, Module, actions, app, settings, ui

mod = Module()

# TODO: not sure if we want to move any of the below to neovim-talon?

# mod.setting(
#     "vim_preserve_insert_mode",
#     type=int,
#     default=1,
#     desc="If normal mode actions are called from insert mode, stay in insert",
# )

mod.setting(
    "vim_adjust_modes",
    type=int,
    default=1,
    desc="User wants talon to automatically adjust modes for commands",
)

# mod.setting(
#     "vim_notify_mode_changes",
#     type=int,
#     default=0,
#     desc="Notify user about vim mode changes as they occur",
# )

mod.setting(
    "vim_escape_terminal_mode",
    type=int,
    default=0,
    desc="When set won't limit what motions and commands will pop out of terminal mode",
)
mod.setting(
    "vim_cancel_queued_commands",
    type=int,
    default=1,
    desc="Press escape before issuing commands, to cancel previously queued command that might have been in error",
)

mod.setting(
    "vim_cancel_queued_commands_timeout",
    type=float,
    default=0.05,
    desc="How long to wait in seconds before issuing the real command after canceling",
)

mod.setting(
    "vim_mode_change_timeout",
    type=float,
    default=0.2,
    desc="It how long to wait before issuing commands after a mode change",
)

# mod.setting(
#     "vim_mode_switch_moves_cursor",
#     type=int,
#     default=0,
#     desc="Preserving insert mode will automatically move the cursor. Setting this to 0 can override that.",
# )

mod.setting(
    "vim_use_rpc",
    type=int,
    default=0,
    desc="Whether or not to use RPC if it is available. Useful for testing or avoiding bugs",
)
mod.setting(
    "vim_debug",
    type=int,
    default=0,
    desc="Debugging used for development",
)
