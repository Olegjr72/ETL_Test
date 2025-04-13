#!/usr/bin/bash
chmod -R +rwx /ETL_Test
cd /ETL_Test
./db_create.py
./etl_data.py
./etl_bot.py &