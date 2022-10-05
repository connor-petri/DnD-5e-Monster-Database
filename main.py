import PySimpleGUI as sg
import json

import resources.monster as MonsterFile
import resources.layout as gui
import resources.functions as functions


# Setup for main function. Generates monster dictionary, loads save data, and initalizes main window from layout.py
def set_up():

    monster_dict = {}

    for monster in MonsterFile.monster_generator(MonsterFile.monster_data):
        monster_dict[monster.getName().lower()] = monster

    with open("./resources/saves.json", "r", encoding="utf8") as save_file:
            file_obj = json.load(save_file)
            save_list = file_obj["save data"]

    return monster_dict, gui.main(save_list), save_list



# Main function. Sets up and runs event loop.
def main():

    # Set up
    monster_dict, window, save_list = set_up()

    #Window event loop
    while True:

        event, values = window.read()
        print(event, values)
    
        # Breaks event loop if window is closed
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        
        # Search functionality
        if event in ('-IN-', '-SAVES-'):

            if event == '-IN-':
                search_queary = values['-IN-'].lower()
            else:
                search_queary = values['-SAVES-'][0].lower()
            
            if search_queary in monster_dict.keys():
                window['-OUT-'+sg.WRITE_ONLY_KEY].update('')
                window['-OUT-'+sg.WRITE_ONLY_KEY].print(monster_dict[search_queary].make_stat_block())


        # Add save functionality
        if event == '-ADD-':
            save_list = functions.add_save(window, monster_dict, save_list, values['-SAVE_IN-'])


        # Delete save functionality
        if event == '-DELETE-':
            print(values['-SAVES-'])
            save_list = functions.delete_save(window, save_list, values['-SAVES-'][0])

    
    # When window is closed or event loop is broken, dump save data and close the window.
    functions.dump_save_data('./saves.json', save_list)
    window.close()



if __name__ == '__main__':
    main()