#!/bin/bash
/bin/su -c "/usr/pgsql-9.6/bin/pg_ctl -D /var/lib/pgsql/9.6/data start" - postgres
sleep 5
echo "CREATE EXTENSION postgis;" | /usr/bin/psql -U postgres -d postgres
/usr/bin/shp2pgsql -s 4326 /resources/cb_2018_us_state_500k/cb_2018_us_state_500k.shp | /usr/bin/psql -U postgres -d postgres
python /main.py
