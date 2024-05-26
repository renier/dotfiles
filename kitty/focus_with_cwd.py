import os
from kittens.tui.handler import result_handler
from kitty.fast_data_types import current_focused_os_window_id


def main():
    pass


@result_handler(no_ui=True)
def handle_result(args, result, target_window_id, boss):
    # focus neighboring window
    boss.active_tab.neighboring_window(args[1])
    if target_window_id == current_focused_os_window_id():
        return

    # get currently focused window
    w = boss.active_tab.active_window
    if w is None:
        return

    # get window's current working directory
    try:
        cwd = os.path.basename(w.child.foreground_processes[0]["cwd"])
    except KeyError:
        return

    # with open("/tmp/focus_with_cwd.log", "a") as f:
    #     f.write(f"{cwd}\n")
    if cwd == os.environ["USER"]:
        cwd = "~"
    if cwd == "":
        return

    # set the current tab's title to that directory's basename
    boss.active_tab.set_title(cwd)
