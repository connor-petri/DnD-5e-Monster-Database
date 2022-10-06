import subprocess
import sys


def pip_install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
    

if __name__ == '__main__':
    
    pip_install('PySimpleGUI')