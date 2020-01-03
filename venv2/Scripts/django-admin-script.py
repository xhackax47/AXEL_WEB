#!C:\Users\samy_\OneDrive\Bureau\A.X.E.L\AXEL_WEB\venv2\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Django==3.0.1','console_scripts','django-admin'
__requires__ = 'Django==3.0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Django==3.0.1', 'console_scripts', 'django-admin')()
    )
