#!/bin/bash
#   ___ _____ ___ _     _____   ____  _             _    
#  / _ \_   _|_ _| |   | ____| / ___|| |_ __ _ _ __| |_  
# | | | || |  | || |   |  _|   \___ \| __/ _` | '__| __| 
# | |_| || |  | || |___| |___   ___) | || (_| | |  | |_  
#  \__\_\|_| |___|_____|_____| |____/ \__\__,_|_|   \__| 
#                                                        
#  
# ----------------------------------------------------- 
# Fork of https://gitlab.com/stephan-raabe/dotfiles/-/blob/main/qtile/autostart.sh?ref_type=heads

# My screen resolution
 xrandr --output VGA-1 --mode 1920x1080

# Keyboard layout
setxkbmap be

# Load picom
picom &

# Set Wallpaper
~/.fehbg &

# Set termianl Colors
wal -R
