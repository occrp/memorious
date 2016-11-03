import os

DEBUG = True

APP_NAME = os.environ.get('MEMORIOUS_APP_NAME', 'memorious')
APP_TITLE = os.environ.get('MEMORIOUS_APP_TITLE', APP_NAME)
SECRET_KEY = os.environ.get('MEMORIOUS_SECRET_KEY')

DATABASE_URL = os.environ.get('DATABASE_URI')
ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL', 'http://localhost:9200/')

MODEL_YAML = os.environ.get('MEMORIOUS_MODEL', 'model.yaml')