#!/bin/bash

udiskie -a &
picom &
dusnt &
eww daemon &
volctl &
nm-applet &
xfce4-power-manager &
mkfifo /tmp/vol-icon && ~/.config/qtile/scripts/vol_icon.sh &
dbus-update-activation-environment DISPLAY XAUTHORITY WAYLAND_DISPLAY
dbus-update-activation-environment --all
albert &
# setxkbmap -layout us,us -variant ,intl -option grp:ctrl_shift_toggle &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/var/lib/flatpak/exports/bin/com.dropbox.Client &
