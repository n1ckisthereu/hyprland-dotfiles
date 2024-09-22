from dataclasses import dataclass, field, asdict
from os import path
from typing import List
import json


@dataclass()
class reloading_app:
    app: str
    cmd: str

    def __getitem__(self, index):
        return self.cmd[index]

    def __len__(self):
        return len(self.cmd)


@dataclass
class bg_config:
    wallpaper_dir: str = ""
    updatebg_cmd: str = ""
    to_reloading: List[reloading_app] = field(default_factory=list)


@dataclass
class config_model:
    bg: bg_config = field(default_factory=bg_config)


class config:
    def __init__(self) -> None:
        self.file_path = path.join(
            path.dirname(path.abspath(__file__)), "../config.json"
        )
        self.config_data: config_model = self._load_config()

    def _load_config(self):
        try:
            with open(self.file_path, "r") as f:
                content = f.read().strip()
                if not content:
                    return config_model()
                loaded_config = json.loads(content)
                return config_model(bg=bg_config(**loaded_config["bg"]))
        except (FileNotFoundError, KeyError):
            return config_model()

    def save(self):
        with open(self.file_path, "w") as f:
            json.dump(asdict(self.config_data), f, indent=2)


class cfg_bg:
    def __init__(self):
        self.cfg_manager = config()
        self.cfg_bg = self.cfg_manager.config_data.bg

    def update_dir(self, new_path):
        self.cfg_bg.wallpaper_dir = new_path
        self.cfg_manager.save()

    def updatebg_cmd(self, cmd):
        self.cfg_bg.updatebg_cmd = cmd
        self.cfg_manager.save()

    def add_app_reload(self, app: str, cmd: str):
        item = reloading_app(app, cmd)
        self.cfg_bg.to_reloading.append(item)
        self.cfg_manager.save()

    def remove_app_reload(self, app: str):
        self.cfg_bg.to_reloading = [
            obj for obj in self.cfg_bg.to_reloading if obj["app"] != app
        ]

        self.cfg_manager.save()
