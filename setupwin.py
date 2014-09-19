# Run the build process by running the command 'python setupwin.py build'

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': 'atexit'
    }
}

executables = [
    Executable('qAndora.py', base=base)
]

setup(name='qAndora',
      version='0.1',
      description='PySide+VLC Pandora Player',
      options=options,
      executables=executables
      )
