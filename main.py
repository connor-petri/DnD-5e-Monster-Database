import PySimpleGUI as sg

import resources.functions as functions


# Main function. Sets up and runs event loop.
def main():

    # Set up
    monster_dict, window, save_list = functions.set_up()

    #Window event loop
    while True:

        event, values = window.read()

        # Uncomment for debugging:
        # print(event, values)
    
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
                monster_dict[search_queary].make_stat_block(window)


        # Add save functionality
        if event == '-ADD-':
            save_list = functions.add_save(window, monster_dict, save_list, values['-SAVE_IN-'])


        # Delete save functionality
        if event == '-DELETE-':
            print(values['-SAVES-'])
            save_list = functions.delete_save(window, save_list, values['-SAVES-'][0])


        if event == '-SAVE_DATA-':
            functions.user_save_data(save_list)

    
    # When window is closed or event loop is broken, dump save data and close the window.
    functions.dump_save_data(save_list)
    window.close()



if __name__ == '__main__':
    main()