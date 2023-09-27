from libqtile.config import Match
from libqtile.layout.floating import Floating
from libqtile.layout.max import Max
from libqtile.layout.tree import TreeTab
from libqtile.layout.xmonad import MonadTall
from utils.settings import colors

layout_theme = {
    "border_width": 4,
    "margin": 4,
    "border_focus": colors[8],
    "border_normal": colors[12],
    "font": "JetBrainsMono Nerd Font",
    "single_border_width": 0,
    "single_margin": 10,
}

layouts = [
    MonadTall(**layout_theme, ratio=0.6),
    TreeTab(
        previous_on_rm=True,
        name="looking good",
        bg_color=colors[0],
        inactive_bg=colors[3],
        panel_width=100,
        margin_left=0,
        margin_y=0,
        sections=["TreeTab"],
        section_left=0,
        padding_x=4,
        active_bg=colors[7],
        rounded=False,
    ),
    Max(),
]

floating_layout = Floating(
    border_focus=colors[8],
    border_normal=colors[14],
    border_width=4,
    fullscreen_border_width=0,
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
