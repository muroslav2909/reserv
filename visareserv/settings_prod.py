import os
from visareserv.settings import BASE_DIR

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0', '54.201.234.40', 'vamiko.if.ua']

# STATIC_URL = '/static/'
DOMAIN_NAME = 'http://vamiko.if.ua/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/media/')
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
