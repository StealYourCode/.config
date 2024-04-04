#   ___ _____ ___ _     _____    ____             __ _       
#  / _ \_   _|_ _| |   | ____|  / ___|___  _ __  / _(_) __ _ 
# | | | || |  | || |   |  _|   | |   / _ \| '_ \| |_| |/ _` |
# | |_| || |  | || |___| |___  | |__| (_) | | | |  _| | (_| |
#  \__\_\|_| |___|_____|_____|  \____\___/|_| |_|_| |_|\__, |
#                                                      |___/ 
#
# Icons: https://fontawesome.com/search?o=r&m=free
# Fork of https://gitlab.com/stephan-raabe/dotfiles/-/blob/main/qtile/config.py?ref_type=heads

import os
import re
import socket
import subprocess
import psutil
import json
from libqtile import hook, layout
from libqtile import qtile
from typing import List  
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget import Spacer, Backlight
from libqtile.widget.image import Image
from libqtile.dgroups import simple_key_binder
from pathlib import Path
from libqtile.log_utils import logger


# --------------------------------------------------------
# Your configuration
# --------------------------------------------------------

# Show wlan status bar widget (set to False if wired network)
show_wlan = False


# Show bluetooth status bar widget
show_bluetooth = False

# --------------------------------------------------------
# General Variables
# --------------------------------------------------------

# Get home path
home = str(Path.home())

# --------------------------------------------------------
# Check for Desktop/Laptop
# --------------------------------------------------------

# 3 = Desktop
platform = int(os.popen("cat /sys/class/dmi/id/chassis_type").read())

# --------------------------------------------------------
# Set default apps
# --------------------------------------------------------

terminal = "kitty"        

# --------------------------------------------------------
# Keybindings
# --------------------------------------------------------


mod = "mod4" # SUPER KEY

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    # Focus
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    
    # Move
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Size
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    # Start Terminal
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle Workspace
    Key([mod], "Tab", lazy.screen.next_group(), desc="Toggle between workspaces/groups"),
    Key([mod, "control"], "Tab", lazy.screen.prev_group(), desc="Toggle between workspaces/group"),


    # Toggle between active groups
    Key([mod, "shift"], "Tab", lazy.screen.toggle_group(), desc="Toggle between active groups"),

    # Move focused window to a specific group (change the index accordingly)
    Key([mod, "shift"], "KP_1", lazy.window.togroup("1")),  # Moves focused window to group 1
    Key([mod, "shift"], "KP_2", lazy.window.togroup("2")),  # Moves focused window to group 2

    # Toggle layouts
    Key([mod, "control"], "l", lazy.next_layout(), desc="Toggle between layouts"),

    # Kill
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    # Switch to full screen
    Key([mod],"f",lazy.window.toggle_fullscreen(),desc="Toggle fullscreen on the focused window",),

    # Floating
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),

    # Reload Config
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),

    # Shutdown Qtile
    Key([mod, "control"], "w", lazy.shutdown(), desc="Shutdown Qtile"),
    
    # Widget Promp
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )



# --------------------------------------------------------
# Pywal Colors
# --------------------------------------------------------

colors = os.path.expanduser('~/.cache/wal/colors.json')
colordict = json.load(open(colors))
Color0=(colordict['colors']['color0'])
Color1=(colordict['colors']['color1'])
Color2=(colordict['colors']['color2'])
Color3=(colordict['colors']['color3'])
Color4=(colordict['colors']['color4'])
Color5=(colordict['colors']['color5'])
Color6=(colordict['colors']['color6'])
Color7=(colordict['colors']['color7'])
Color8=(colordict['colors']['color8'])
Color9=(colordict['colors']['color9'])
Color10=(colordict['colors']['color10'])
Color11=(colordict['colors']['color11'])
Color12=(colordict['colors']['color12'])
Color13=(colordict['colors']['color13'])
Color14=(colordict['colors']['color14'])
Color15=(colordict['colors']['color15'])




# --------------------------------------------------------
# Setup Layout Theme
# --------------------------------------------------------

layout_theme = { 
    "border_width": 3,
    "margin": 15,
    "border_focus": "Color2",
    "border_normal": "FFFFFF",
    "single_border_width": 3
}



# --------------------------------------------------------
# Groups
# --------------------------------------------------------

groups = [
    Group("1", layout='monadtall'),
    Group("2", layout='monadtall'),
    Group("3", layout='monadtall'),
    Group("4", layout='monadtall'),
    Group("5", layout='monadtall'),
]

dgroupskey_binder = simple_key_binder(mod)



# --------------------------------------------------------
# Scratchpads
# --------------------------------------------------------

groups.append(ScratchPad("6", [
    DropDown("chatgpt", "chromium --app=https://chat.openai.com", x=0.3, y=0.1, width=0.40, height=0.4, on_focus_lost_hide=False ),
    DropDown("mousepad", "mousepad", x=0.3, y=0.1, width=0.40, height=0.4, on_focus_lost_hide=False ),
    DropDown("terminal", "kitty", x=0.3, y=0.1, width=0.40, height=0.4, on_focus_lost_hide=False ),
    DropDown("scrcpy", "scrcpy -d", x=0.8, y=0.05, width=0.15, height=0.6, on_focus_lost_hide=False )
]))

keys.extend([
    Key([mod], 'F10', lazy.group["6"].dropdown_toggle("chatgpt")),
    Key([mod], 'F11', lazy.group["6"].dropdown_toggle("mousepad")),
    Key([mod], 'F12', lazy.group["6"].dropdown_toggle("terminal")),
    Key([mod], 'F9', lazy.group["6"].dropdown_toggle("scrcpy"))
])



# --------------------------------------------------------
# Layouts
# --------------------------------------------------------

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(),
    layout.MonadWide(),
    layout.RatioTile(),
    layout.Floating()
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]



# --------------------------------------------------------
# Setup Widget Defaults
# --------------------------------------------------------

widget_defaults = dict(
    font="sans",
    fontsize=14,
    padding=3
)
extension_defaults = widget_defaults.copy()



# --------------------------------------------------------
# Widgets
# --------------------------------------------------------

widget_list = [
    widget.TextBox(
        background=Color1+".4",text="",foreground="ffffff",padding=10,mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("kitty")},
    ),
    widget.TextBox(
        background=Color1+".4",text="",foreground="ffffff",padding=10,mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("rofi -show drun")},
    ),
    widget.TextBox(
        background=Color1+".4",text="",foreground="ffffff",padding=10,mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("sh firefox")},
    ),
     widget.TextBox(
	background=Color1+".4",text="",foreground="ffffff",padding=10,mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("thunar")},
    ),
    widget.TextBox(
	background=Color1+".4",text="",foreground="ffffff",padding=10,mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("teams")},
    ),
    widget.TextBox(
        background=Color1+".4",text="",foreground="ffffff",padding=10,mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("discord")},
    ),
    widget.TextBox(
        background=Color1+".4",text="",foreground="ffffff",padding=10,mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("chromium --app=https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://mail.google.com/mail/u/0/&ved=2ahUKEwiBkOuG0aGFAxUwUqQEHT6oCQUQFnoECBoQAQ&usg=AOvVaw1GRqnzaEzJ-JntPiR5Sc98")},
    ),
    widget.WindowName(
        max_chars=50,background=Color1+".4",width=400,padding=10
    ),
    widget.Spacer(lenght=15
    ),
    widget.GroupBox(
        background=Color1+".4",highlight_method='block',highlight='ffffff',block_border='ffffff',highlight_color=['ffffff','ffffff'],block_highlight_text_color='000000',foreground='ffffff',rounded=True,this_current_screen_border='ffffff',active='ffffff',
    ),
    widget.Spacer(lenght=15
    ),
    widget.TextBox(
	background=Color1+".4",text="",foreground="ffffff",padding=10,mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("wal -i /usr/share/wallpapers/")},
    ),
    widget.TextBox(
        background=Color1+".4",text='',foreground='ffffff',padding=10,mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("nm-connection-editor")},
    ),
    widget.Clock(
        background=Color1+".4",padding=10,format="%d-%m-%Y / %H:%M %p",
    ),
    widget.TextBox(
        background=Color1+".4",text='',foreground='ffffff',padding=10,mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(home + "/.config/qtile/script/power.sh")},
    ),



]



# --------------------------------------------------------
# Screens
# --------------------------------------------------------

screens = [
    Screen(
        top=bar.Bar(
            widget_list,
            30,
            padding=20,
            opacity=0.7,
            border_width=[0, 0, 0, 0],
            margin=[0,0,0,0],
            background=Color1+".1"
        ),
    ),
]



# --------------------------------------------------------
# Drag floating layouts
# --------------------------------------------------------

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]



# --------------------------------------------------------
# Define floating layouts
# --------------------------------------------------------

floating_layout = layout.Floating(
    border_width=3,
    border_focus="#194D33",
    border_normal="FFFFFF",
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)



# --------------------------------------------------------
# General Setup
# --------------------------------------------------------

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False



auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"



# --------------------------------------------------------
# Hooks
# --------------------------------------------------------

# STARTUP
@hook.subscribe.startup_once
def autostart():
    autostartscript = "~/.config/qtile/script/autostart.sh"
    home = os.path.expanduser(autostartscript)
    subprocess.Popen([home])
