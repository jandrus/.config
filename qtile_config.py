#!/usr/bin/python3
#
#

import os
from libqtile import bar, layout, widget, extension, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.dgroups import simple_key_binder



# Globals
MOD             = "mod4"
ALT_KEY         = "mod1"
TERMINAL        = "alacritty"
BROWSER         = "firefox"
FILE_MANAGER    = "pcmanfm-qt"


# Key Bindings
keys = [
    Key([MOD], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([MOD], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([MOD], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([MOD], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([MOD], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([MOD], "j", lazy.layout.down(), desc="Move focus down"),
    Key([MOD], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([MOD], "k", lazy.layout.up(), desc="Move focus up"),
    Key([MOD], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([MOD, "shift"], "Down",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        desc='Move windows down in current stack'
        ),
    Key([MOD, "shift"], "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        desc='Move windows down in current stack'
        ),
    Key([MOD, "shift"], "Up",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc='Move windows up in current stack'
        ),
    Key([MOD, "shift"], "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc='Move windows up in current stack'
        ),
