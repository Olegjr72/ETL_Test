#!/usr/bin/bash
apt-get update
apt-get upgrade -y
apt-get install git -y
git clone https://github.com/Olegjr72/ETL_Test.git
chmod -R +rwx /ETL_Test
cd /ETL_Test
/ETL_Test/install.sh
