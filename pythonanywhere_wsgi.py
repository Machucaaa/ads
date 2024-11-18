

# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

## assuming your django settings file is at '/home/alma4anywhere/mysite/mysite/settings.py'
## and your manage.py is is at '/home/alma4anywhere/mysite/manage.py'
path = '/home/alma4anywhere/ads/'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'ads.settings'

##then:
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())
