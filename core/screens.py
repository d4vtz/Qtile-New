from core.widgets import Widget
from libqtile import bar
from libqtile.config import Screen

from .settings import colors, wallpaper

widgets = Widget()
widget_defaults = dict(
    font="Roboto Condense",
    fontsize=12,
    background=colors[0],
)
extension_defaults = widget_defaults.copy()


def create_bar():
    widget = Widget()
    return bar.Bar(
        widget.widgets,
        26,
        margin=[10, 8, 8, 10],
        background=widgets.colors.background,
    )


screens = [
    Screen(
        wallpaper=wallpaper,
        wallpaper_mode="fill",
        top=create_bar(),
        bottom=bar.Gap(2),
        left=bar.Gap(2),
        right=bar.Gap(2),
    ),
]
