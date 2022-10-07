import PySimpleGUI as sg
import sys

sg.LOOK_AND_FEEL_TABLE['Custom 1'] = {'BACKGROUND': '#FDFAD0',
                                        'TEXT': '#A30404',
                                        'INPUT': '#EDE8B1',
                                        'TEXT_INPUT': '#A30404',
                                        'SCROLL': '#F7F2B4',
                                        'BUTTON': ('#003333', '#FEF6A2'),
                                        'PROGRESS': ('#D1826B', '#CC8019'),
                                        'BORDER': 1, 'SLIDER_DEPTH': 0, 
                                        'PROGRESS_DEPTH': 0, }


def window_set_up():
    primary = 'American Typewriter'
    fonts = {
        'b1': (primary, 20, 'bold'),
        'b2': (primary, 14, 'bold'),
        'i1': (primary, 16, 'italic'),
        't1': (primary, 16),
        't2': (primary, 20)
    }
    

    size_dict = {
    '-SAVE_IN-': (30, 1),
    '-SAVES-': (25, 35),
    '-traits-': (60, 20),
    '-spells-': (70, 10),
    '-actions-': (70, 25),
    '-legendary_actions-': (70, 12)
    }


    if sys.platform == 'win32':
        
        primary = 'Footlight MT Light'

        fonts = {
        'b1': (primary, 16, 'bold'),
        'b2': (primary, 12, 'bold'),
        'i1': (primary, 12, 'italic'),
        't1': (primary, 12),
        't2': (primary, 16)
        }
    

        size_dict = {
        '-SAVE_IN-': (30, 1),
        '-SAVES-': (25, 35),
        '-traits-': (60, 20),
        '-spells-': (70, 10),
        '-actions-': (70, 25),
        '-legendary_actions-': (70, 12)
        }


    return fonts, size_dict