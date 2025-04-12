docker image postgres:latest

docker run --name ETL_Test --env=PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/postgresql/17/bin --env=GOSU_VERSION=1.17 --env=PG_MAJOR=17 --env=PG_VERSION=17.4-1.pgdg120+2 --env=PGDATA=/var/lib/postgresql/data --env=POSTGRES_USER=postgres --env=POSTGRES_PASSWORD=postgres --env=LANG=en_US.utf8 --volume=/var/lib/postgresql/data --network=bridge -p 5432:5432 --restart=no --runtime=runc -d postgres:latest

//////////////////////////////////////1st_time.sh/////////////////////////////////////////////////

apt-get update && apt-get upgrade -y && apt-get install git -y && git clone https://github.com/Olegjr72/ETL_Test.git && chmod -R +rwx /ETL_Test && cd /ETL_Test && /ETL_Test/install.sh

//////////////////////////////////////////////////////////////////////////////////////////////

---------------Description-----------------------

conf - configuration file

db_create.py - Create DataBase and table

etl_data.py - etl operations 

etl_bot.py - bot

begin.sh 

Ask me for bot TOKEN

The bot: https://t.me/ETL_Ant_Test_bot

