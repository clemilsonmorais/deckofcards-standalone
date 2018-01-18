# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Django specific settings
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cardsdb.settings")
import django
django.setup()

# Import your models for use in your script
from cardsdb.models import User
# Start of application script (demo code below)