import asyncio
import os
import subprocess

from libqtile import hook


@hook.subscribe.client_new
async def client_new(client):
    await asyncio.sleep(0.3)
    if client.name == "Spotify":
        client.togroup("Music")


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/scripts/autostart.sh"])
