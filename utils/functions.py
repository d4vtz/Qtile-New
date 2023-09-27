import subprocess

from libqtile.lazy import lazy


# resize functions
def resize(qtile, direction):
    layout = qtile.current_layout
    child = layout.current
    parent = child.parent

    while parent:
        if child in parent.children:
            layout_all = False

            if (direction == "left" and parent.split_horizontal) or (
                direction == "up" and not parent.split_horizontal
            ):
                parent.split_ratio = max(5, parent.split_ratio - layout.grow_amount)
                layout_all = True
            elif (direction == "right" and parent.split_horizontal) or (
                direction == "down" and not parent.split_horizontal
            ):
                parent.split_ratio = min(95, parent.split_ratio + layout.grow_amount)
                layout_all = True

            if layout_all:
                layout.group.layout_all()
                break

        child = parent
        parent = child.parent


@lazy.function
def resize_left(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "left")
    elif current == "columns":
        layout.cmd_grow_left()


@lazy.function
def resize_right(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "right")
    elif current == "columns":
        layout.cmd_grow_right()


@lazy.function
def resize_up(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "up")
    elif current == "columns":
        layout.cmd_grow_up()


@lazy.function
def resize_down(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "down")
    elif current == "columns":
        layout.cmd_grow_down()


def backlight(action):
    def f(qtile):
        brightness = int(
            subprocess.run(["brightnessctl", "g"], stdout=subprocess.PIPE).stdout
        )
        max_brightness = int(
            subprocess.run(["brightnessctl", "m"], stdout=subprocess.PIPE).stdout
        )
        step = int(max_brightness / 10)

        if action == "inc":
            if brightness < max_brightness - step:
                subprocess.run(
                    ["brightnessctl", "set", str(brightness + step)],
                    stdout=subprocess.PIPE,
                ).stdout
            else:
                subprocess.run(
                    ["brightnessctl", "set", str(max_brightness)],
                    stdout=subprocess.PIPE,
                ).stdout
        elif action == "dec":
            if brightness > step:
                subprocess.run(
                    ["brightnessctl", "set", str(brightness - step)],
                    stdout=subprocess.PIPE,
                ).stdout
            else:
                subprocess.run(
                    ["brightnessctl", "set", "0"], stdout=subprocess.PIPE
                ).stdout

    return f


def focus_previous_group(qtile):
    group = qtile.current_screen.group
    group_index = qtile.groups.index(group)
    previous_group = group.get_previous_group(skip_empty=True)
    previous_group_index = qtile.groups.index(previous_group)
    if previous_group_index < group_index:
        qtile.current_screen.set_group(previous_group)


def focus_next_group(qtile):
    group = qtile.current_screen.group
    group_index = qtile.groups.index(group)
    next_group = group.get_next_group(skip_empty=True)
    next_group_index = qtile.groups.index(next_group)
    if next_group_index > group_index:
        qtile.current_screen.set_group(next_group)


def float_to_front(qtile) -> None:
    for window in qtile.current_group.windows:
        if window.floating:
            window.bring_to_front()
