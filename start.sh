#!/bin/bash

# init SQLite DB
python create_sqlite_db.py

gunicorn -c gunicorn_config.py smart_spreadsheet_app:app 
