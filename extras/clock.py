from datetime import datetime, timezone

from libqtile.widget import clock


class Clock(clock.Clock):
    defaults = [
        (
            "long_format",
            "%A %d %B %Y",
            "Format to show when widget is clicked.",
        ),
    ]

    def __init__(self, long_format: str, **config):
        super().__init__(**config)
        self.add_defaults(Clock.defaults)
        self.long_format = long_format
        self.short_format = self.format
        self.toggled = False
        self.add_callbacks({"Button1": self.toggle})

    def toggle(self):
        if self.toggled:
            self.format = self.short_format
        else:
            self.format = self.long_format

        self.toggled = not self.toggled
        self.update(self.poll())

    @staticmethod
    def post_meridian(now: datetime) -> str:
        if now.hour < 12:
            return "AM"
        else:
            return "PM"

    def poll(self):
        if self.timezone:
            now = datetime.now(timezone.utc).astimezone(self.timezone)
        else:
            now = datetime.now(timezone.utc).astimezone()
        if "%p" in self.format:
            self.format = self.format.replace("%p", self.post_meridian(now))
        return now.strftime(self.format)
