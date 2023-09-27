import shlex
from subprocess import Popen, run

# from libqtile.command.base import expose_command
from libqtile.widget import base


class Update:
    def __init__(self) -> None:
        self.updates = []

    def _get_updates(self, commands):
        updates = 0
        for _, cmd in commands.items():
            update = run(
                shlex.split(cmd),
                capture_output=True,
                encoding="UTF-8",
                universal_newlines=True,
            )
            if update.returncode == 0:
                packages = update.stdout.split("\n")[:-1]
                updates += len(packages)
                self.updates.extend(packages)
        return updates


class CheckUpdate(base.ThreadPoolText, Update):
    CMD_DICT = {
        "pacman": "checkupdates",
        "paru": "paru -Qu",
    }

    def __init__(
        self,
        distro: dict,
        initial_text: str = "",
        update_interval: int = 3600,
        display_format="Updates {updates}",
        no_update_string="Sistema Actualizado",
        execute=None,
        **config,
    ) -> None:
        base.ThreadPoolText.__init__(self, config.pop("initial_text", ""), **config)
        self.add_defaults(CheckUpdate.defaults)
        Update.__init__(self)

        self.distro = distro or self.CMD_DICT
        self.initial_text = initial_text
        self.update_interval = update_interval
        self.display_format = display_format
        self.no_update_string = no_update_string
        self.execute = execute

        if self.execute:
            self.add_callbacks(
                {"Button1": self.get_updates, "Button2": self.update_hook}
            )

        self.updates = []

    def _check_updates(self) -> str:
        # updates = 0
        # try:
        #     self.updates = []
        #     for repo, cmd in self.distro.items():
        #         update = self.call_process(cmd, shell=True).splitlines()
        #         packages = [package.split()[0] for package in update]
        #
        #         updates += len(update)
        #         if repo != "pacman":
        #             self.updates.append("---------- AUR ----------")
        #         self.updates.extend(packages)
        # except CalledProcessError:
        #     updates += 0
        #
        # if self.layout:
        #     if updates == 0:
        #         self.layout.colour = self.colour_no_updates
        #         return self.no_update_string
        #
        #     self.layout.colour = self.colour_have_updates
        # return self.display_format.format(**{"updates": updates})
        updates = self._get_updates(self.distro)
        if self.layout:
            if updates == 0:
                self.layout.colour = self.colour_no_updates
                return self.no_update_string

            self.layout.colour = self.colour_have_updates
        return self.display_format.format(**{"updates": updates})

    def poll(self) -> str:
        return self._check_updates()

    def do_execute(self) -> None:
        if self.execute:
            self._process = Popen(self.execute, shell=True)
            self.timeout_add(self.execute_polling_interval, self._refresh_count)

    def _refresh_count(self) -> None:
        if self._process.poll() is None:
            self.timeout_add(self.execute_polling_interval, self._refresh_count)

        else:
            self.timer_setup()

    def get_updates(self) -> None:
        updates = "\n".join(self.updates)
        Popen(f"notify-send '{updates}'", shell=True)

    # @expose_command()
    def update_hook(self) -> None:
        self.poll()
