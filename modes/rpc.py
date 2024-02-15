from talon import Context, Module, actions, app, ui, cron, settings
from ..vim.vim import VimMode

ctx = Context()

monitor_job = None
v = None
tags: set[str] = set()

last_title = None
last_window = None


def rpc_parse_mode(window):
    """check if neovim window is focused and enable/disable monitoring the
    vim mode through rpc.
    """
    global monitor_job, v
    global last_window, last_title
    current_title = window.title
    if last_window == window and last_title == current_title:
        print("rpc_parse_mode(): Skipping due to duplicate window/title")
        return

    last_window = window
    last_title = current_title

    print(f"rpc_parse_mode(): current_title={current_title}")

    # TODO: it is not working for the commandline version yet due to the windows title not containing "VIM MODE:" yet
    if current_title.startswith("VIM MODE:"):  # or current_title.startswith("NeoVim"):
        # TODO: is it the right way to initialize this VimMode?
        if v is None:
            v = VimMode()
        # TODO: change this to 100ms
        # monitor_job = cron.interval("1000ms", rpc_monitor_mode)
        # monitor_job = cron.interval("100ms", rpc_monitor_mode)
        rpc_monitor_mode()
    else:
        print("rpc_parse_mode(): Skipping due to not in neovim")
        ctx.tags = []
        if monitor_job:
            print(f"rpc_parse_mode(): deleting monitor_job={monitor_job}")
            cron.cancel(monitor_job)
            monitor_job = None


def rpc_monitor_mode():
    """Get the mode from Neovim rpc and enable the corresponding tags."""
    global v, ctx, tags

    tags = set(ctx.tags)
    if v.nvrpc.init_ok is True:
        mode = v.current_mode_id()
        print(f"rpc_monitor_mode(): mode={mode}")
        tags = [VimMode.mode_to_tag(mode)]
        print(f"rpc_monitor_mode(): tags={tags}")
        ctx.tags = tags
    else:
        print(f"rpc_monitor_mode(): nvrpc is not initialized")


def rpc_win_title_hook(window):
    print(f"rpc_win_title_hook(window={window})")
    rpc_parse_mode(window)


def rpc_win_focus_hook(window):
    print(f"rpc_win_focus_hook(window={window})")
    rpc_parse_mode(window)


def register_events():
    ui.register("win_title", rpc_win_title_hook)
    ui.register("win_focus", rpc_win_focus_hook)


app.register("ready", register_events)
