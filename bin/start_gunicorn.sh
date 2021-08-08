#!/bin/bash
source /home/www/code/lesson7/venv/bin/activate
exec gunicorn -c /home/www/code/lesson7/config/gunicorn_config.py config.wsgi