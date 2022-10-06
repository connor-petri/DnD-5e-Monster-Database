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

    os.system('pyenv shell 3.10.6')
    
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