from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
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
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "r", lazy.spawn("rofi -show drun -show-icons"), desc="Spawn a command using a prompt widget"),
    Key([], "Print", lazy.spawn(" import -window root screenshot.jpg")),
    Key([], "F1", lazy.spawn("amixer sset Master toggle")),
    Key([], "F2", lazy.spawn("amixer sset Master 3%-")),
    Key([], "F3", lazy.spawn("amixer sset Master 3%+")),
    Key([], "F5", lazy.spawn("brightnessctl set 2.5%-")),
    Key([], "F6", lazy.spawn("brightnessctl set 2.5%+")),


    
]


group_names = [
    "WWW-1",
    "DEV-2",
    "TERM-3",
    "SYS-4",
    "WKSP-5",
    "WKSP-6",
    "WKSP-7",
    "WKSP-8",
    "WKSP-9",
]

groups = [Group(i) for i in group_names]

layouts = [
    layout.Max(margin=[20, 20, 20, 20]),
    layout.Columns(
	border_focus_stack=["#d75f5f", "#8f3d3d"], 
	border_focus=["#a8eb12", "#2cd261", "#b7f92c"],
	border_width=4,
	margin=[20, 20, 20, 20]
	),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# If resolution is 3840 x 2160 
fontsize = 22
padding = 8
top_bar_height = 40
bottom_bar_height = 42

# If resolution is 1920 * 1080
# fontsize = 16
# padding = 4
# top_bar_height = 30
# bottom_bar_height = 32

widget_defaults = dict(
    font="Source Code Pro Semibold",
    fontsize=fontsize,
    padding=padding,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar([
                widget.Sep(
			    background="#000000", linewidth=0, padding=10),
                widget.GroupBox(highlight_method="block"),
                widget.WindowName(format='{name}',padding=10),
                widget.Systray(),

		        #Memeory
		        widget.Image(filename="~/.config/qtile/icons/powerline-head-light.svg"),
		        widget.Image(filename="~/.config/qtile/icons/ram.svg",background="#46d93c",margin=4),
		        widget.Memory(format='{MemUsed:.0f}{mm}',background="#46d93c",foreground="#fafafa",padding=10),

		        # Time
		        widget.Image(filename="~/.config/qtile/icons/powerline-dark.svg"),
		        widget.Image(filename="~/.config/qtile/icons/time.svg",background="#428c00",margin=6),
                widget.Clock(format="%b %d %H:%M", background="#428c00", foreground="#fafafa",padding=5),

		        # Volume
		        widget.Image(filename="~/.config/qtile/icons/powerline-light.svg"),
		        widget.Image(filename="~/.config/qtile/icons/volume.svg",background="#46d93c", foreground="#fafafa",margin=5),
		        widget.Volume(background="#46d93c", padding=5),

		        # Logout
		        widget.Image(filename="~/.config/qtile/icons/powerline-dark.svg"),
        		widget.Image(filename="~/.config/qtile/icons/logout.svg",background="#428c00",margin=4),
                widget.QuickExit( default_text="Logout",countdown_format='In {} s',background="#428c00", foreground="#fafafa", padding=10)],
                top_bar_height),
	    bottom=bar.Bar([
		widget.Image(
			filename="~/.config/qtile/icons/layout.svg",
			background="#75bb00",
            foreground="#fafafa",
			margin=5
		),
                widget.CurrentLayout(
			background="#75bb00", padding=10),
		widget.Spacer(),
		widget.Image(
			filename="~/.config/qtile/icons/network.svg",
			background="#54bac2",
            foreground="#fafafa",
			margin=6
		),
		widget.Net(format="Network:{up} \u2191  \u2193{down}",background="#54bac2", padding=10, prefix="M"),

	],
    bottom_bar_height),
	wallpaper="~/.config/qtile/background.svg",
	wallpaper_mode="fill"
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder(mod)

dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
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
