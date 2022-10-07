import PySimpleGUI as sg
import json

import resources.monster as MonsterFile
import resources.layout as gui


# Setup for main function. Generates monster dictionary, loads save data, and initalizes main window from layout.py
def set_up():

    monster_dict = {}

    for monster in MonsterFile.monster_generator(MonsterFile.load_monster_data()):
        monster_dict[monster.getName().lower()] = monster

    with open("./resources/saves.json", "r", encoding="utf8") as save_file:
            file_obj = json.load(save_file)
            save_list = file_obj["save data"]

    return monster_dict, gui.make_window(save_list).Finalize(), save_list


# Dumps save data to saves.json
def dump_save_data(data):

    with open('./resources/saves.json', "w", encoding="utf8") as save_file:
        json_obj = json.dumps({"save data": data}, indent=4)
        save_file.write(json_obj)


# Checks if save data actually saved
def check_save_data(data):
    with open("./resources/saves.json", "r", encoding="utf8") as save_file:
        file_obj = json.load(save_file)
        save_check = file_obj["save data"]

    if save_check == data:
        return True
    else:
        return False


# Used for when user manually saves. It confirms that the save was successful and shows a popup for it.
def user_save_data(data):

    dump_save_data(data)
    
    if check_save_data(data):
        sg.popup('Save successful.', font=('Ariel', 12))

    else:
        sg.popup('An error occured while trying to save data.', font=('Ariel', 12))


# Add save to save list
def add_save(window, monster_dict, save_list, value):

    if (value in monster_dict.keys()) and (value not in save_list):
        save_list.append(value)
        window['-SAVES-'].update(values=save_list)

    else:
        if value not in monster_dict.keys():
            sg.popup(f'Error: No monster with name "{value}" found.')

        elif (value in save_list) and (value in monster_dict.keys()):
            sg.popup(f'Error: {value} is already saved.')

    return save_list


# delete save from save list
def delete_save(window, save_list, value):

    if value in save_list:
        save_list.remove(value)
        window['-SAVES-'].update(values=save_list)

    else:
        sg.popup(f'Error: {value} is not a saved monster.')

    return save_list



