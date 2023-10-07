from pathlib import Path
from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from utils.functions import (
    backlight,
    resize_down,
    resize_left,
    resize_right,
    resize_up,
    float_to_front,
)


class KeysMode:
    def __init__(self, vim: bool = True) -> None:
        self.vim = vim
        if self.vim:
            self.left = "h"
            self.down = "j"
            self.up = "k"
            self.right = "l"
        else:
            self.left = "Left"
            self.down = "Down"
            self.up = "Up"
            self.right = "Right"


mod = "mod4"
control = "control"
shift = "shift"
alt = "mod1"

mode = KeysMode(vim=True)

terminal = guess_terminal()
home = Path.home().as_posix()

keys = [
    # qtile
    Key([mod, shift], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, shift], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # essentials
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "q", lazy.window.kill(), desc="Kill active window"),
    Key([mod], "w", lazy.spawn("google-chrome-stable"), desc="Launch Google Chrome"),
    Key([mod], "e", lazy.spawn("thunar"), desc="Launch Thunar"),
    Key([mod], "s", lazy.spawn("spotify"), desc="Launch Spotify"),
    # menus
    Key(
        [mod, shift],
        "Return",
        lazy.spawn(f"{home}/.local/bin/launcher.sh"),
        desc="Launch Rofi",
    ),
    Key(
        [mod, shift],
        "e",
        lazy.spawn(f"{home}/.local/bin/powermenu.sh"),
        desc="Power Menu",
    ),
    # Layouts
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle forward layout"),
    Key([mod, shift], "Tab", lazy.prev_layout(), desc="Toggle last layout"),
    # focus, move windows and screens
    Key(
        [control],
        mode.down,
        lazy.layout.down(),
        desc="Move focus down in current stack pane",
    ),
    Key(
        [control], mode.up, lazy.layout.up(), desc="Move focus up in current stack pane"
    ),
    Key(
        [control],
        mode.left,
        lazy.layout.left(),
        desc="Move focus left in current stack pane",
    ),
    Key(
        [control],
        mode.right,
        lazy.layout.right(),
        desc="Move focus right in current stack pane",
    ),
    Key(
        [control, shift],
        mode.down,
        lazy.layout.shuffle_down(),
        lazy.layout.move_down(),
        desc="Move windows down in current stack",
    ),
    Key(
        [control, shift],
        mode.up,
        lazy.layout.shuffle_up(),
        lazy.layout.move_up(),
        desc="Move windows up in current stack",
    ),
    Key(
        [control, shift],
        mode.left,
        lazy.layout.shuffle_left(),
        lazy.layout.move_left(),
        desc="Move windows left in current stack",
    ),
    Key(
        [control, shift],
        mode.right,
        lazy.layout.shuffle_right(),
        lazy.layout.move_right(),
        desc="Move windows right in the current stack",
    ),
    Key(
        [mod],
        "x",
        lazy.next_screen(),
        desc="Move focus to next monitor",
    ),  # TODO find a better hotkey
    Key([mod, control], mode.down, lazy.layout.flip_down(), desc="Flip layout down"),
    Key([mod, control], mode.up, lazy.layout.flip_up(), desc="Flip layout up"),
    Key(
        [mod, control],
        mode.left,
        lazy.layout.flip_left(),
        lazy.layout.swap_column_left(),
        desc="Flip layout left",
    ),
    Key(
        [mod, control],
        mode.right,
        lazy.layout.flip_right(),
        lazy.layout.swap_column_left(),
        desc="Flip layout right",
    ),
    # window resizing
    Key([mod, alt], mode.left, resize_left, desc="Resize window left"),
    Key([mod, alt], mode.right, resize_right, desc="Resize window Right"),
    Key([mod, alt], mode.up, resize_up, desc="Resize windows upward"),
    Key([mod, alt], mode.down, resize_down, desc="Resize windows downward"),
    Key([mod, alt], "n", lazy.layout.normalize(), desc="Normalize window size ratios"),
    # window states
    Key(
        [mod],
        "m",
        lazy.window.toggle_maximize(),
        desc="Toggle window between minimum and maximum sizes",
    ),
    Key([mod, shift], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key(
        [mod],
        "i",
        lazy.window.toggle_floating(),
        desc="Toggle floating mode for a window",
    ),
    Key([], "F11", lazy.window.toggle_fullscreen()),
    # Floating window management
    Key([mod], "space", lazy.window.toggle_floating()),
    Key([mod], "c", lazy.window.center()),
    Key([mod], "f", lazy.function(float_to_front)),
    # program launches
    # Key(
    #     [mod],
    #     "t",
    #     lazy.group["scratchpad"].dropdown_toggle("kitty"),
    #     desc="Scratchpad",
    # ),
    # screenshots
    Key(
        [],
        "Print",
        lazy.spawn(f"{home}/.local/bin/screenshots"),
        desc="Print Screen",
    ),
    # audio stuff
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"),
        desc="Increase volume",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"),
        desc="Decrease volume",
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"),
        desc="Toggle volume mute",
    ),
    Key(
        [],
        "XF86AudioPrev",
        lazy.spawn("playerctl previous"),
        desc="Play last audio",
    ),
    Key(
        [],
        "XF86AudioNext",
        lazy.spawn("playerctl next"),
        desc="Play next audio",
    ),
    Key(
        [],
        "XF86AudioPlay",
        lazy.spawn("playerctl play-pause"),
        desc="Toggle play/pause audio",
    ),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop"), desc="Stop audio"),
    # brightness
    Key([mod], "Prior", lazy.function(backlight("inc")), desc="Increase brightness"),
    Key([mod], "Next", lazy.function(backlight("dec")), desc="Decrease brightness"),
    # LayoutKey
    Key(
        [mod, shift],
        "k",
        lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Swich layout key",
    ),
]


def show_keys():
    key_help = ""
    for k in keys:
        mods = ""

        for m in k.modifiers:
            if m == "mod4":
                mods += "Super + "
            else:
                mods += m.capitalize() + " + "

        if len(k.key) > 1:
            mods += k.key.capitalize()
        else:
            mods += k.key

        key_help += "{:<25} {}".format(mods, k.desc + "\n")

    return key_help


keys.extend(
    [
        Key(
            [mod],
            "a",
            lazy.spawn("sh -c 'echo \"" + show_keys() + '" | rofi -dmenu -i -p ""\''),
            desc="Print keyboard bindings",
        ),
    ]
)
