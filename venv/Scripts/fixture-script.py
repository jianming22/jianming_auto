#!C:\Users\ljm\PycharmProjects\jianming\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'fixture==1.5.11','console_scripts','fixture'
__requires__ = 'fixture==1.5.11'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('fixture==1.5.11', 'console_scripts', 'fixture')()
    )
