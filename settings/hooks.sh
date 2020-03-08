#!/bin/sh
echo "push"
git checkout -t origin/deploy
git pull origin deploy
export MODE=RUN
pip3 install -r requirement.txt
fuser -k -n tcp 8000
python3 manage.py runserver
