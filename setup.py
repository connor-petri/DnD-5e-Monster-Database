import subprocess
import sys
import os
import platform


def brew_install(package):
    os.system(f'brew install {package}')

def pip_install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def mac_install():
    brew_install('pyenv')
    brew_install('tcl-tk')

    while True:
        user_input = input('shell or virtualenv?').lower()

        if user_input=='shell':
            os.system('pyenv shell 3.10.6')
            break

        elif user_input == 'virtualenv':
            os.system('pyenv virtualenv 3.10.6 5e_monster_database')
            os.system('pyenv activate 5e_monster_database')
            break
    
    pip_install('PySimpleGUI')



def windows_install():

    pip_install('PySimpleGui')


def main():

    if platform.system() == "Windows":
        windows_install()

    if platform.system() in ('Darwin', 'macOS'):
        mac_install()
    
    

if __name__ == '__main__':
    
    main()