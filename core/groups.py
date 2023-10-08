from libqtile.config import DropDown, Group, Key, Match, ScratchPad
from libqtile.lazy import lazy
from utils.functions import focus_next_group, focus_previous_group

from .keys import keys, mod, shift

groups = [
    Group(
        name="Home",
        label="",
        matches=[Match(wm_class="obsidian")],
    ),
    Group(
        name="Web",
        label="",
        matches=[Match(wm_class="google-chrome")],
    ),
    Group(
        name="Code",
        label="",
        matches=[Match(wm_class="code")],
    ),
    Group(
        name="Physic",
        label="",
        matches=[Match(wm_class="Zathura")],
        layout="max",
    ),
    Group(
        name="Media",
        label="",
    ),
    Group(name="Social", label="", matches=[Match(wm_class="telegram-desktop")]),
    Group(
        name="System",
        label="",
        matches=[Match(wm_class="pavucontrol")],
    ),
]

for index, group in enumerate(groups, start=1):
    keys.append(
        Key(
            [mod],
            str(index),
            lazy.group[group.name].toscreen(),
            desc="Focus this desktop",
        )
    )
    keys.append(
        Key(
            [mod, shift],
            str(index),
            lazy.window.togroup(group.name),
            lazy.group[group.name].toscreen(),
            desc="Move focused window to another group",
        )
    )

    keys.extend(
        [
            Key(
                [mod],
                "Left",
                lazy.function(focus_previous_group),
            ),
            Key(
                [mod],
                "Right",
                lazy.function(focus_next_group),
            ),
        ]
    )

kitty_scratchpad = dict(
    opacity=1,
    x=0.1,
    y=0.15,
    width=0.8,
    height=0.7,
    on_focus_lost_hide=True,
)

groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown("term", "kitty", **kitty_scratchpad),
        ],
    )
)
