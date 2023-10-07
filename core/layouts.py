from libqtile.config import Match
from libqtile.layout.floating import Floating
from libqtile.layout.max import Max
from libqtile.layout.xmonad import MonadTall
from utils.settings import colors

layout_theme = {
    "align": 0,
    "border_focus": colors[8],
    "border_normal": colors[12],
    "border_width": 2,
    "margin": 6,
}

layouts = [
    MonadTall(
        ratio=0.6, change_size=5, single_border_width=0, single_margin=6, **layout_theme
    ),
    Max(),
]

floating_layout = Floating(
    border_focus=colors[6],
    border_normal=colors[14],
    border_width=2,
    fullscreen_border_width=4,
    max_border_width=0,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="matplotlib")  # Graficas
        # TODO add matches
    ],
)
