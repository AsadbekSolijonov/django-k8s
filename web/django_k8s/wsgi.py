"""
WSGI config for django_k8s project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os 
import pathlib # new
import dotenv  # new
from django.core.wsgi import get_wsgi_application

# new
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
# new 
ENV_FILE_PATH = BASE_DIR / '.env'
# new
dotenv.read_dotenv(str(ENV_FILE_PATH))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_k8s.settings')

application = get_wsgi_application()
