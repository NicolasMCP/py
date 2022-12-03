import sys
sys.path.insert(0, '/var/www/html/teste')

activate_this = 'source /var/www/html/teste/venv/bin/activate'
with open(activate_this) as file:
    exec(file.read(), dict(__file__=activate_this))

from app import app as application
