import os
from kittens.tui.handler import result_handler
from kitty.fast_data_types import current_focused_os_window_id


def main():
    pass


@result_handler(no_ui=True)
def handle_result(args, result, target_window_id, boss):
    w1 = boss.window_id_map.get(target_window_id)
    if w1 is None:
        return

    boss.call_remote_control(w1, ("launch", "--cwd=current", "--location=vsplit"))

    # get currently focused window
    w2 = boss.active_tab.active_window
    if w2 is None:
        return

    boss.call_remote_control(
        w2,
        ("resize-window", "--self", "--axis=reset"),
    )
