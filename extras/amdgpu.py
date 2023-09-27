import pyamdgpuinfo
from libqtile.widget import base


class Sensors:
    def __init__(self, temperature, percentage, vram) -> None:
        self.temperature = temperature
        self.percentage = percentage
        self.vram = vram


class Amdgpu(base.ThreadPoolText):
    defaults = [
        (
            "format",
            "  {temperature}°C  {percentage}%  {vram}M",
            "Display string format.",
        ),
        ("foreground_alert", "#ff0000", "Foreground colour alert"),
        ("update_interval", 2, "Update interval in seconds."),
        (
            "threshold",
            60,
            "If the current temperature value is above, "
            "then change to foreground_alert colour",
        ),
        (
            "gpu_id",
            0,
            "Id GPU's",
        ),
    ]

    def __init__(self, **config):
        base.ThreadPoolText.__init__(self, "", **config)
        self.add_defaults(Amdgpu.defaults)
        self.foreground_normal = self.foreground

        self.gpu = pyamdgpuinfo.get_gpu(self.gpu_id)
        self.vram_size = self.gpu.memory_info["vram_size"]
        self.gtt_size = self.gpu.memory_info["gtt_size"]

    def gpu_sensors(self) -> Sensors:
        temperature = round(self.gpu.query_temperature())
        vram_used = self.gpu.query_vram_usage()
        percentage = round(100 * vram_used / self.vram_size)
        vram = round(vram_used / 1e6)

        return Sensors(
            temperature=temperature,
            percentage=percentage,
            vram=vram,
        )

    def poll(self) -> str:
        sensors = self.gpu_sensors()
        if sensors.temperature > self.threshold:
            self.foreground = self.foreground_alert
        else:
            self.foreground = self.foreground_normal

        return str(self.format).format(
            temperature=sensors.temperature,
            percentage=sensors.percentage,
            vram=sensors.vram,
        )
