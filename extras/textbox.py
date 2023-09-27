import random

from libqtile.widget import base


class Test(base.ThreadPoolText):
    defaults = [
        (
            "initial_text",
            "",
            "Draw the widget immediately with an initial text, "
            "useful if it takes time to check system updates.",
        ),
        ("icon", "icon", "Icon show"),
        ("display_format", "{icon}", "Comment"),
        ("update_interval", 1, "Update interval in seconds."),
    ]

    def __init__(self, **config):
        base.ThreadPoolText.__init__(self, config.pop("initial_text", ""), **config)
        self.add_defaults(Test.defaults)

        self.execute_polling_interval = 1

    def _update(self):
        a = random.randint(0, 10)

        self.layout.colour = "#fff"
        if a >= 5:
            self.layout.colour = "#000"
        return self.display_format.format(**{"icon": f"{self.icon}"})

    def poll(self):
        return self._update()

    def do_execute(self):
        self.timeout_add(self.execute_polling_interval, self._refresh_count)

    def _refresh_count(self):
        # self.timeout_add(self.execute_polling_interval, self._refresh_count)
        self.timer_setup()
