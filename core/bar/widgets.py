import os
from typing import Optional

#from extras.amdgpu import Amdgpu
from extras.clock import Clock
from extras.groupbox import GroupBox
from extras.updates import CheckUpdate
from libqtile.bar import CALCULATED
from libqtile.lazy import lazy

color = Optional[str]
from core.settings import Colors
# from libqtile import widget
from libqtile.widget import TextBox
from qtile_extras import widget


class Widget:
    def __init__(self) -> None:
        self.colors = Colors()

    def sep(self, padding: int = 8) -> TextBox:
        return TextBox(
            foreground=self.colors.gray,
            padding=padding,
            font="Iosevka Nerd Font",
            fontsize=20,
            text="",
        )

    def logo(self) -> TextBox:
        return TextBox(
            foreground=self.colors.cyan,
            mouse_callbacks={"Button1": lazy.restart()},
            padding=12,
            font="Iosevka Nerd Font",
            fontsize=16,
            text=" ",
        )

    def groups(self) -> GroupBox:
        return GroupBox(
            font="Iosevka Nerd Font",
            fontsize=16,
            colors=[
                self.colors.home,
                self.colors.web,
                self.colors.code,
                self.colors.read,
                self.colors.music,
                self.colors.media,
                self.colors.social,
                self.colors.system,
            ],
            highlight_color=self.colors.background,
            highlight_method="line",
            invert=True,
            rainbow=True,
            this_current_screen_border=self.colors.cyan,
            urgent_border=self.colors.alert,
            inactive=self.colors.inactive,
            disable_drag=True,
            padding_x=3,
            center_aligned=True,
        )

    def updates(self) -> list:
        return [
            # TextBox(
            #     foreground=self.colors.yellow,
            #     font="Iosevka Nerd Font",
            #     fontsize=18,
            #     text=" ",
            # ),
            CheckUpdate(
                foreground=self.colors.foreground,
                colour_have_updates=self.colors.red,
                colour_no_updates=self.colors.foreground,
                display_format="{updates} updates",
                distro={"pacman": "checkupdates", "aur": "paru -Qu"},
                initial_text="No updates  ",
                no_update_string="Updated",
                execute=True,
                padding=0,
                update_interval=3600,
                markup=True,
                fmt='<span font_desc="Iosevka Nerd Font" size="x-large"> </span>  {}',
            ),
        ]

    def window_name(self) -> widget.WindowName:
        return widget.WindowName(
            format="{name}",
            max_chars=60,
            width=CALCULATED,
            empty_group_string="Desktop",
        )

    def clock(self) -> list:
        return [
            TextBox(
                foreground=self.colors.orange,
                font="Iosevka Nerd Font",
                fontsize=16,
                text="",
            ),
            Clock(
                foreground=self.colors.foreground,
                format="%A  %-I:%M %p ",
                long_format="%-d de %B del %Y ",
                padding_x=-15,
            ),
        ]

    def gen_current_layout(self):
        return widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            padding=3,
            scale=0.65,
            use_mask=True,
            foreground=self.colors.white,
        )

    def exit(self):
        return widget.TextBox(
            foreground=self.colors.red,
            font="Iosevka Nerd Font",
            fontsize=16,
            mouse_callbacks={"Button1": lazy.restart()},
            text=" ",
        )

    def status_notifier(self):
        return widget.StatusNotifier(
            icon_size=24,
            icon_theme="/usr/share/icons/Papirus",
            padding=10,
            hide_after=5,
            menu_width=250,
            show_menu_icons=True,
            background=self.colors.background,
            highlight_colour=self.colors.gray,
            menu_background=self.colors.background,
            menu_foreground=self.colors.white,
            menu_foreground_disabled=self.colors.red,
            menu_icon_size=16,
            menu_fontsize=16,
            menu_foreground_highlighted=self.colors.violet,
            highlight_radius=7.5,
            separator_colour=self.colors.gray,
            menu_border=self.colors.white,
            menu_border_width=1,
            menu_offset_x=2,
            menu_offset_y=6,
        )

    @property
    def widgets(self):
        return [
            self.logo(),
            self.sep(),
            self.gen_current_layout(),
            self.sep(),
            self.groups(),
            widget.Spacer(),
            self.window_name(),
            widget.Spacer(),
            #Amdgpu(),
            widget.Systray(padding=8),
            # self.status_notifier(),
            self.sep(),
            widget.KeyboardLayout(
                configured_keyboards=["us", "us intl"],
                display_map={"us": "us", "us intl": "US"},
                fmt='<span font_desc="Iosevka Nerd Font" size="large"> </span>  {}',
                markup=True,
            ),
            *self.updates(),
            *self.clock(),
            self.sep(),
            self.exit(),
        ]
