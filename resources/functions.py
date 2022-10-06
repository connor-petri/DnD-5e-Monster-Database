import PySimpleGUI as sg
import json

import resources.monster as MonsterFile
import resources.layout as gui


# Setup for main function. Generates monster dictionary, loads save data, and initalizes main window from layout.py
def set_up():

    monster_dict = {}

    for monster in MonsterFile.monster_generator(MonsterFile.monster_data):
        monster_dict[monster.getName().lower()] = monster

    with open("./resources/saves.json", "r", encoding="utf8") as save_file:
            file_obj = json.load(save_file)
            save_list = file_obj["save data"]

    return monster_dict, gui.main(save_list), save_list


# Dumps save data to saves.json
def dump_save_data(path, data):

    with open(path, "w", encoding="utf8") as save_file:
        json_obj = json.dumps({"save data": data}, indent=4)
        save_file.write(json_obj)


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