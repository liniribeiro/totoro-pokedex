import os

from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEST = config('TEST', None)
HOST = config('HOST', '0.0.0.0')
PORT = config('PORT', '5000')
DATABASE_URL = config('DATABASE_URL', 'sqlite:///pokedex.sqlite3')

