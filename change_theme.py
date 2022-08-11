import os
import sys
import json
from rich.console import Console
# Improved print from the rich package
print = Console().print
# Check for the arguments
if len(sys.argv) < 2:
    print("Usage: python change_theme.py theme", style="yellow")
    exit()
new_theme = sys.argv[1]
with open("current_theme.txt") as f:
    current_theme = f.read()
with open("themes.json") as f:
    themes = json.load(f)
with open("locations.json") as f:
    locations = json.load(f)


def backup(config: str, file_name: str):
    """Backup config"""
    with open(f"config_backup/{file_name}.bak", "w") as f:
        f.write(config)


def replace(config: str, app: str, setting: str = None) -> str:
    """Replace current setting with the new one"""
    if setting is None:
        return config.replace(themes[current_theme][app], themes[new_theme][app])
    return config.replace(themes[current_theme][app][setting], themes[new_theme][app][setting])


if __name__ == "__main__":
    if new_theme not in themes:
        print("[ERROR] Theme doesnt exist.", style="red")
        exit()

    if new_theme == current_theme:
        print("[ERROR] Theme is the same as the old one.", style="red")
        exit()

    print(
        f"[INFO] Changing theme from {current_theme} to {new_theme}", style="blue")
    print("[INFO] Backing up old configs", style="blue")
    if locations["zsh"]:
        print("[INFO] Changing zsh config", style="blue")
        with open(locations["zsh"]) as f:
            zsh_config = f.read()
        backup(zsh_config, "zsh_config")
        zsh_config = replace(zsh_config, "zsh")
        with open(locations["zsh"], "w") as f:
            f.write(zsh_config)
        print("[SUCCESS] Finished ZSH", style="green")
    if locations["i3"]:
        print("[INFO] Changing i3 config", style="blue")
        with open(locations["i3"]) as f:
            i3_config = f.read()
        backup(i3_config, "i3_config")
        i3_config = replace(i3_config, "i3", "text")
        if locations["pictures"]:
            i3_config = replace(i3_config, "wallpaper")
        with open(locations["i3"], "w") as f:
            f.write(i3_config)
        print("[SUCCESS] Finished i3", style="green")
        print("[INFO] Please reload i3", style="blue")
    if locations["polybar"]:
        print("[INFO] Changing polybar config", style="blue")
        with open(locations["polybar"]) as f:
            pb_config = f.read()
        backup(pb_config, "polybar_config")
        pb_config = replace(pb_config, "polybar", "foreground")
        pb_config = replace(pb_config, "polybar", "background")
        pb_config = replace(pb_config, "polybar", "secondary")
        with open(locations["polybar"], "w") as f:
            f.write(pb_config)
        print("[SUCCESS] Finished polybar", style="green")
    if locations["spicetify"]:
        print("[INFO] Changing Spotify", style="blue")
        os.system(
            f"cd {locations['spicetify']}; ./spicetify config current_theme " \
            f"{themes[new_theme]['spotify']['theme']}")
        os.system(
            f"cd {locations['spicetify']}; ./spicetify config color_scheme " \
            f"{themes[new_theme]['spotify']['color']}")
        os.system(f"cd {locations['spicetify']}; ./spicetify apply")
        print("[SUCCESS] Finished Spotify", style="green")
    if locations["pictures"]:
        print("[INFO] Changing the Wallpaper", style="blue")
        os.system(
            f"feh --bg-fill {locations['pictures']}{themes[new_theme]['wallpaper']}")
        print("[SUCCESS] Changed Wallpaper", style="green")
    # Save theme as current one
    with open("current_theme.txt", "w") as f:
        f.write(new_theme)
