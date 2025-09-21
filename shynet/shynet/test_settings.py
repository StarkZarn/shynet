from .settings import *

# Remove debug toolbar
if "debug_toolbar" in INSTALLED_APPS:
    INSTALLED_APPS.remove("debug_toolbar")
if "debug_toolbar.middleware.DebugToolbarMiddleware" in MIDDLEWARE:
    MIDDLEWARES.remove("debug_toolbar.middleware.DebugToolbarMiddleware")
