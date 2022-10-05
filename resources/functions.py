import PySimpleGUI as sg
import json


def dump_save_data(path, data):

    with open(path, "w", encoding="utf8") as save_file:
        json_obj = json.dumps({"save data": data}, indent=4)
        save_file.write(json_obj)


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


def delete_save(window, save_list, value):

    if value in save_list:
        save_list.remove(value)
        window['-SAVES-'].update(values=save_list)

    else:
        sg.popup(f'Error: {value} is not a saved monster.')

    return save_list