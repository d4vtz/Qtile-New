from core import Settings

settings = Settings()

groups = settings.groups
keys = settings.keys
floating_layout = settings.floating_layout
layouts = settings.layouts
screens = settings.screens
widget_defaults = settings.widget_defaults
hooks = settings.hooks

# REVIEW options
auto_fullscreen = True
auto_minimize = False
bring_front_click = False
cursor_warp = False
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
focus_on_window_activation = "smart"
reconfigure_screens = True
wl_input_rules = None
wmname = "qtile"
