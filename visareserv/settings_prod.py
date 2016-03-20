import os

DOMAIN_NAME = 'http://54.201.234.40'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DEBUG = False
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

