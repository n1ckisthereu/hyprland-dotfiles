from .system import system
from .config import cfg_bg
from os import listdir


class theme:
    def __init__(self):
        self.system_utils = system()
        self.bg = cfg_bg()

    def toggle_theme(self, mode):
        if mode != "dark":
            self.system_utils.run_command(
                'gsettings set org.gnome.desktop.interface gtk-theme "adw-gtk3" && gsettings set org.gnome.desktop.interface color-scheme "default"'
            )
        else:
            self.system_utils.run_command(
                'gsettings set org.gnome.desktop.interface gtk-theme "adw-gtk3-dark" && gsettings set org.gnome.desktop.interface color-scheme "prefer-dark"'
            )

    # TODO: Define wallpaper with configured command
    def define_wallpaper(self, wal):
        updatebg_cmd = self.bg.cfg_bg.updatebg_cmd
        fullpath = self.bg.cfg_bg.wallpaper_dir

        self.system_utils.run_command(f"{updatebg_cmd} {fullpath}/{wal}")

    # TODO: List available wallpapers in defined path
    # - maybe pagination skip take
    def available(self, take, skip):
        listdir(self.bg.cfg_bg.wallpaper_dir)
