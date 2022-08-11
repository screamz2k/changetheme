# changetheme.py
A simple script to change themes for you applications and wm easily.
## Currently supported
- i3
- polybar
- ohmyzsh theme
- feh wallpaper
- spicetify
## Setup
### 1. Clone this repo and install the requirements
```
git clone https://github.com/screamz2k/changetheme/
cd changetheme
python -m pip install -r requirements.txt
```
### 2. Change locations.json
> If you dont want to change something just leave the location empty
```
{
    "polybar": "/home/screamz/.config/polybar/config.ini",
    "i3": "/home/screamz/.config/i3/config",
    "spicetify": "/home/screamz/.spicetify/",
    "zsh": "/home/screamz/.zshrc",
    "pictures": "/home/screamz/pictures"
}
```
### 3. Configure themes.json
Make sure one of the themes inside is your __current__ one
### 4. Write your current theme inside current_theme.txt
### 5. Run the script
```
python change_theme.py red
```
