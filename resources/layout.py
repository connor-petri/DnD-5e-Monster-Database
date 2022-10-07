import PySimpleGUI as sg

import resources.stylesheet as stylesheet
    

# Set window = layout.main() when using this in main.py
def make_window(save_list):

    f = stylesheet.fonts()

    sg.theme('Custom 1')   

    stre = [
        [sg.Push(), sg.T('STR', font=f['b2']), sg.Push()],
        [sg.Push() ,sg.T('10 (+0)', k='-str-', font=f['t1']), sg.Push()]
    ]
    dext = [
        [sg.Push(), sg.T('DEX', font=f['b2']), sg.Push()],
        [sg.Push() ,sg.T('10 (+0)', k='-dex-', font=f['t1']), sg.Push()]
    ]
    cons = [
        [sg.Push(), sg.T('CON', font=f['b2']), sg.Push()],
        [sg.Push() ,sg.T('10 (+0)', k='-con-', font=f['t1']), sg.Push()]
    ]
    inte = [
        [sg.Push(), sg.T('INT', font=f['b2']), sg.Push()],
        [sg.Push() ,sg.T('10 (+0)', k='-int-', font=f['t1']), sg.Push()]
    ]
    wisd = [
        [sg.Push(), sg.T('WIS', font=f['b2']), sg.Push()],
        [sg.Push() ,sg.T('10 (+0)', k='-wis-', font=f['t1']), sg.Push()]
    ]
    char = [
        [sg.Push(), sg.T('CHA', font=f['b2']), sg.Push()],
        [sg.Push() ,sg.T('10 (+0)', k='-cha-', font=f['t1']), sg.Push()]
    ]


    # Save data input, listbox, and buttons
    col1 = [
        [sg.Text("Saved Monsters:", font=f['t1'])],
        [sg.Input(key='-SAVE_IN-', font=f['t1'], s=(30, 1)), sg.B('Add', k='-ADD-', font=f['t1'])],
        [sg.Listbox((save_list), k='-SAVES-', s=(25, 35), font=f['t2'], enable_events=True)],
        [sg.B('Save', k='-SAVE_DATA-', font=f['t1']), sg.Push(), sg.B('Delete', k='-DELETE-', font=f['t1'])]
        ]


    #Stat Block Parts. 1 is left side and 2 is right side
    stat_block_1 = [
        [sg.HSeparator()], # Header
        [sg.T('Name', k='-name-', font=f['b1'])],
        [sg.T('Size Type (subtype), Alignment', k='-size_type_alignment-', font=f['i1'])],

        [sg.HSeparator()], # AC, HP, and Speed
        [sg.T('Armor Class', font=f['b2']), sg.T('10', k='-ac-', font=f['t1'])],
        [sg.T('Hit Points', font=f['b2']), sg.T('10 (4d10)', k='-hp-', font=f['t1'])],
        [sg.T('Speed', font=f['b2']), sg.T('10', k='-speed-', font=f['t1'])],

        [sg.HSeparator()], # Stats
        [sg.Column(stre), sg.Column(dext), sg.Column(cons), sg.Column(inte), sg.Column(wisd), sg.Column(char)],

        [sg.HSeparator()], # Misc Stats
        [sg.T('Saving Throws', font=f['b2']), sg.T('', k='-saving_throws-', font=f['t1'])],
        [sg.T('Skills', font=f['b2']), sg.T('', k='-skillsaves-', font=f['t1'])],
        [sg.T('Damage Vulnerabilities', font=f['b2']), sg.T('', k='-d_vulnerabilities-', font=f['t1'])],
        [sg.T('Damage Resistances', font=f['b2']), sg.T('', k='-d_resistances-', font=f['t1'])],
        [sg.T('Damage Immunities', font=f['b2']), sg.T('', k='-d_immunities-', font=f['t1'])],
        [sg.T('Condition Immunities', font=f['b2']), sg.T('', k='-c_immunities-', font=f['t1'])],
        [sg.T('Senses', font=f['b2']), sg.T('', k='-senses-', font=f['t1'])],
        [sg.T('Languages', font=f['b2']), sg.T('', k='-languages-', font=f['t1'])],
        [sg.T('Challenge', font=f['b2']), sg.T('', k='-cr-', font=f['t1'])],

        [sg.HSeparator()], # Traits
        [sg.Multiline('Traits', k='-traits-', s=(60, 20), disabled=True, font=f['t1'])],
        ]

    stat_block_2 = [
        [sg.Multiline('Spells', k='-spells-', font=f['t1'], disabled=True, s=(70, 10))],
        [sg.HSeparator()],
        [sg.Multiline('Actions', k='-actions-', font=f['t1'], disabled=True, s=(70, 25))],
        [sg.HSeparator()],
        [sg.Multiline('Legendary Actions', k='-legendary_actions-', font=f['t1'], disabled=True, s=(70, 12))]
        ]


    # Column containing the whole stat block
    col2 = [
        [sg.Text('Search:', font=f['t1']), sg.Input(k='-IN-', s=(35,1), font=f['t1'], enable_events=True)],
        [sg.Column(stat_block_1), sg.VSeparator(), sg.Column(stat_block_2)],
        [sg.Push(), sg.Exit(font=f['t1'])]
    ]


    # Main layout. Search bar at the top plus the two columns and an exit button
    layout = [
        [sg.Column(col1), sg.VSeparator(), sg.Column(col2, k='-statblock-')]
        ]

    # Returns window object. Set window = layout.main()
    return sg.Window('Monster Search', layout, resizable=True)