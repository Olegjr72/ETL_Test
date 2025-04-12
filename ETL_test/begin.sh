#!/usr/bin/bash
./db_create.py
./etl_data.py
./etl_bot.py &