# pychartjs/plugins.py

from dataclasses import dataclass
from typing import Optional, Dict


@dataclass
class DecimationOptions:
    enabled: bool = True
    algorithm: str = "lttb"  # 'lttb' or 'min-max'
    samples: int = 1000

    def to_dict(self) -> Dict:
        return {
            "enabled": self.enabled,
            "algorithm": self.algorithm,
            "samples": self.samples,
        }


@dataclass
class Plugin:
    plugin_name: str
    options: Optional[Dict] = None
    beforeInit: Optional[str] = None
    afterDraw: Optional[str] = None

    def to_dict(self) -> Dict:
        plugin_dict = {
            "plugin_name": self.plugin_name,
            "options": self.options,
        }
        if self.beforeInit:
            plugin_dict["beforeInit"] = self.beforeInit
        if self.afterDraw:
            plugin_dict["afterDraw"] = self.afterDraw
        return plugin_dict
