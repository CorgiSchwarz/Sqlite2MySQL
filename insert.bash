#!/usr/bin/env bash
host="$1"
port="$2"
user="$3"
pw="$4"
db="$5"
file_name='./mysql.sql'
mysql -h $host -p $port -u $user -p $pw --default-character-set=utf8mb4 -e "source ~/Desktop/code/SqliteConverter/mysql.sql" >& error.log
#mysql -h $host -p $port -u $user -p $pw <<EOF
#use ${db};
#source ${file_name};
#EOF