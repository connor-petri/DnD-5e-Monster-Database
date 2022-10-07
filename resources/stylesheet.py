import PySimpleGUI as sg


sg.LOOK_AND_FEEL_TABLE['Custom 1'] = {'BACKGROUND': '#FDFAD0',
                                        'TEXT': '#A30404',
                                        'INPUT': '#EDE8B1',
                                        'TEXT_INPUT': '#A30404',
                                        'SCROLL': '#F7F2B4',
                                        'BUTTON': ('#003333', '#FEF6A2'),
                                        'PROGRESS': ('#D1826B', '#CC8019'),
                                        'BORDER': 1, 'SLIDER_DEPTH': 0, 
                                        'PROGRESS_DEPTH': 0, }


def fonts():
    primary = 'American Typewriter'
    return {
        'b1': (primary, 20, 'bold'),
        'b2': (primary, 14, 'bold'),
        'i1': (primary, 16, 'italic'),
        't1': (primary, 16),
        't2': (primary, 20)
    }