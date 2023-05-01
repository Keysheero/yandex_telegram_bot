import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get('api_key')
CLIENT_ID = os.environ.get('client_id')
PARK_ID = os.environ.get('park_id')


BOT_TOKEN = os.environ.get('BOT_TOKEN')

DB_NAME = os.environ.get('DB_NAME')
DB_PORT = os.environ.get('DB_PORT')
DB_HOST = os.environ.get('DB_HOST')
DB_PASS = os.environ.get('DB_PASS')
DB_USER = os.environ.get('DB_USER')
