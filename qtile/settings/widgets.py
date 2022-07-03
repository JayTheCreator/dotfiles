from libqtile import widget
from settings.theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="█", # Icon: nf-oct-triangle_left
        fontsize=37,
        padding=-1
    )


def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=12,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),

        separator(),
        #widget.WindowName(**base(fg='focus'), fontsize=20, padding=3),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
        separator(),
    ]


primary_widgets = [
    *workspaces(),

    separator(),

    powerline('color4', 'dark'),

    icon(bg="color4", text=' '), # Icon: nf-fa-download
    
    widget.CheckUpdates(
        background=colors['color4'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
    ),
 
    #powerline('color1', 'color2'),

    #icon(bg="color1", text='墳 '),  # Icon: nf-fa-feed
    
    #widget.Volume(**base(bg='color1'), channel='Master'),

    powerline('color1', 'color2'),

    icon(bg="color1", text='  '),  # Icon: nf-fa-feed
    
    widget.Battery(**base(bg='color1'), charge_char='!', discharge_char='-', format='{percent:2.0%}'),

    powerline('color1', 'color2'),

    icon(bg="color1", text='  '),  # Icon: nf-fa-feed
    
    widget.ThermalSensor(**base(bg='color1'), tag_sensor='Package id 0', update_interval=10, threshold=70, max_chars=8),

    #powerline('color2', 'color3'),

    #widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),

    #widget.CurrentLayout(**base(bg='color2'), padding=5),

    powerline('color1', 'color2'),

    icon(bg="color1", fontsize=14, text=' '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color1'), format='%d/%m - %H:%M '),

    widget.Systray(background=colors['dark'], padding=3),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    #powerline('color1', 'dark'),

    #widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    #widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 12,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()