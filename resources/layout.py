import PySimpleGUI as sg


# Set window = layout.main() when using this in main.py
def main(save_list):

    sg.theme('Dark Blue 12')   

    # Save data input, listbox, and buttons
    col1 = [
        [sg.Text("Saved Monsters:")],
        [sg.Input(key='-SAVE_IN-'), sg.B('Add', k='-ADD-')],
        [sg.Listbox((save_list), k='-SAVES-', s=(40, 60), enable_events=True)],
        [sg.B('Delete', k='-DELETE-')]
        ]

    #Search Result Display
    col2 = [
        [sg.Multiline(k='-OUT-'+sg.WRITE_ONLY_KEY, s=(120, 80))]
        ]


    # Main layout. Search bar at the top plus the two columns and an exit button
    layout = [
        [sg.Text('Search:'), sg.Input(k='-IN-', s=(35,1), enable_events=True)],
        [sg.Column(col1), sg.Column(col2)],
        [sg.Push(), sg.Exit()]
        ]

    # Returns window object. Set window = layout.main()
    return sg.Window('Monster Search', layout)