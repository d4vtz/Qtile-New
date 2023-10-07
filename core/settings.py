# General
wallpaper = "~/.config/qtile/wallpapers/wallpaper.png"
vimmode = False


class Colors:
    black = "#2E3440"
    white = "#ECEFF4"
    gray = "#4C566A"
    blue = "#5E81AC"
    cyan = "#88C0D0"
    dark_blue = "#81A1C1"
    red = "#BF616A"
    orange = "#D08770"
    yellow = "#EBCB8B"
    green = "#A3BE8C"
    violet = "#B48EAD"

    background = black
    foreground = white
    active = cyan
    inactive = gray
    alert = red

    # GroupBox color
    home = cyan
    web = yellow
    code = white
    read = violet
    music = green
    media = orange
    social = blue
    system = red


colors = [
    "#2E3440",  # nord0
    "#3B4252",  # nord1
    "#434C5E",  # nord2
    "#4C566A",  # nord3
    "#D8DEE9",  # nord4
    "#E5E9F0",  # nord5
    "#ECEFF4",  # nord6
    "#8FBCBB",  # nord7
    "#88C0D0",  # nord8
    "#81A1C1",  # nord9
    "#5E81AC",  # nord10
    "#BF616A",  # nord11
    "#D08770",  # nord12
    "#EBCB8B",  # nord13
    "#A3BE8C",  # nord14
    "#B48EAD",  # nord15
]

# Hardware
network = "wlp2s0"  # network interface name
two_monitors = True  # number of screens in the system
with_battery = True  # whether the system uses a battery or not
with_wlan = True  # whether the system uses wlan/internet or not
