#!/usr/bin/env bash
sqlite_address="$1"
python3 TableGetter.py $sqlite_address
echo "dumping db: \"$sqlite_address\"! "
sqlite3  $sqlite_address .dump > "sqlite3.sql"
echo "dump done"
python3 toMysql.py "./sqlite3.sql"
echo "tansfer done"
host="$2"
port="$3"
user="$4"
pw="$5"
db="$6"
mysql -h$host -P$port -D$db -u$user -p$pw --default-character-set=utf8mb4 -e "source ./mysql.sql" >&dumper.log
echo "write to MySQL done"
