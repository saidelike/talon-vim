from talon import Context, Module, actions, app, ui, cron, settings
from ..vim.vim import VimMode

ctx = Context()

monitor_job = None
v = None
tags: set[str] = set()


def win_focus_hook(window):
    global monitor_job, v

    current_title = window.title
    print(f"current_title={current_title}")
    # TODO: it is not working for the commandline version yet due to the windows title not containing "VIM MODE:" yet
    if current_title.startswith("VIM MODE:"):  # or current_title.startswith("NeoVim"):
        # TODO: is it the right way to initialize this VimMode?
        if v is None:
            v = VimMode()
        # TODO: change this to 100ms
        monitor_job = cron.interval("1000ms", vim_monitor_mode)
    else:
        ctx.tags = []
        if monitor_job:
            print(f"deleting monitor_job={monitor_job}")
            cron.cancel(monitor_job)
            monitor_job = None


def vim_monitor_mode():
    global v, ctx, tags

    tags = set(ctx.tags)
    if v.nvrpc.init_ok is True:
        mode = v.current_mode_id()
        print(f"vim_monitor_mode(): mode={mode}")
        tags = [VimMode.mode_to_tag(mode)]
        print(f"vim_monitor_mode(): tags={tags}")
        ctx.tags = tags
    else:
        print(f"vim_monitor_mode(): nvrpc is not initialized")


def register_events():
    ui.register("win_focus", win_focus_hook)


app.register("ready", register_events)
