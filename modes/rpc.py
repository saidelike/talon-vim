from talon import Context, Module, actions, app, ui, cron, settings
from ..vim.vim import VimMode

ctx = Context()

v = None

last_title = None
last_window = None


def rpc_get_mode_main(window):
    """check if neovim window is focused, get the vim mode through rpc and set the corresponding tags."""
    global v, ctx
    global last_window, last_title

    current_title = window.title

    print(f"rpc_get_mode_main(): window={window}")

    # this is needed to avoid any call due to background applications that would reset the tags to [],
    # which will basically unset the previously set tags for the neovim window
    if window != ui.active_window():
        print(
            f"title_parse_TERM(): Skipping due to not active window: {window} != {ui.active_window()}"
        )
        return

    # this is mostly an optimization to avoid unnecessary calls but sometimes because it fails to set the right mode,
    # it is better to call it every time to make sure it's taken into account
    # if last_window == window and last_title == current_title:
    #     print("rpc_get_mode_main(): Skipping due to duplicate window/title")
    #     return

    # this is to make sure we are actually focusing neovim
    # NOTE: this check is not working for the commandline version yet due to the windows title not containing "VIM MODE:" yet
    if not current_title.startswith("VIM MODE:"):
        print(f"rpc_get_mode_main(): Skipping due to not in neovim, window={window}")
        ctx.tags = []
        return

    last_window = window
    last_title = current_title

    tags = rpc_get_mode_and_deduce_tags()
    ctx.tags = tags


def rpc_get_mode_and_deduce_tags():
    """Get the mode from Neovim rpc and deduce the corresponding tags."""
    global v, ctx

    # TODO: is it the right way to initialize this VimMode?
    if v is None:
        v = VimMode()

    if v.nvrpc.init_ok is True:
        mode = v.current_mode_id()
        print(f"rpc_get_mode_and_deduce_tags(): mode={mode}")
        tags = [VimMode.mode_to_tag(mode)]
        print(f"rpc_get_mode_and_deduce_tags(): tags={tags}")
        return tags
    else:
        print(f"rpc_get_mode_and_deduce_tags(): nvrpc is not initialized")
        return []


def rpc_win_title_hook(window):
    # print(f"rpc_win_title_hook(window={window})")
    rpc_get_mode_main(window)


def rpc_win_focus_hook(window):
    # print(f"rpc_win_focus_hook(window={window})")
    rpc_get_mode_main(window)


def register_events():
    ui.register("win_title", rpc_win_title_hook)
    ui.register("win_focus", rpc_win_focus_hook)


app.register("ready", register_events)
