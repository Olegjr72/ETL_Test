#!/usr/bin/bash
apt-get install mc python3-full python3-pip python3-pandas python3-psycopg2 python3-xlsxwriter python3-python-telegram-bot htop -y
python3 -m venv ./venv
./venv/bin/pip install telebot
cp ./venv/lib/python3.11/site-packages/* /usr/lib/python3/dist-packages/ -r -n

./begin.sh