from .settings import *

# Override DEBUG settings
DEBUG = False

# Remove debug toolbar
if 'debug_toolbar' in INSTALLED_APPS:
    INSTALLED_APPS.remove('debug_toolbar')
