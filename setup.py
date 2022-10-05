import subprocess
import sys
import os

def brew_install(package):
    os.system(f'brew install {package}')

def pip_install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


if __name__ == '__main__':
    brew_install('pyenv')
    brew_install('tcl-tk')
    os.system('pyenv shell 3.10.6')
    pip_install('PySimpleGUI')