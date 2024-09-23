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

    def define_wallpaper(self, wal):
        updatebg_cmd = self.bg.cfg_bg.updatebg_cmd
        fullpath = self.bg.cfg_bg.wallpaper_dir

        self.system_utils.run_command(f"{updatebg_cmd} {fullpath}/{wal}")

    # TODO: Create option to use filters on matugen command
    def gencolor_scheme(self, wal, mode):
        fullpath = self.bg.cfg_bg.wallpaper_dir
        self.system_utils.run_command(
            f"/usr/bin/matugen image {fullpath}/{wal} -m {mode}"
        )

    def reload_apps(self):
        for a in self.bg.cfg_bg.to_reloading:
            self.system_utils.run_command(a["cmd"])

    def available(self) -> list[str]:
        return listdir(self.bg.cfg_bg.wallpaper_dir)

    def gen_full(self, wal, mode):
        availables = self.available()

        if wal not in availables:
            raise FileNotFoundError("this wallpaper does not exist")

        self.define_wallpaper(wal)
        self.gencolor_scheme(wal, mode)
        self.toggle_theme(mode)
        self.reload_apps()

    # TODO: Generate papirus theme using this font
    # https://github.com/InioX/matugen/issues/83

    # TODO: Implement colorschema for qt to

    # BUG: New gnome 47 only gets the theme if the theme is defined in the GTK_THEME variable
