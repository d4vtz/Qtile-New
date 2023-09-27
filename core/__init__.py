from core import hooks
from core.groups import groups
from core.keys import keys
from core.layouts import floating_layout, layouts
from core.screens import screens, widget_defaults


class Settings:
    groups = groups
    keys = keys
    floating_layout = floating_layout
    layouts = layouts
    screens = screens
    widget_defaults = widget_defaults
    hooks = hooks

    def __init__(self) -> None:
        pass
