#!/bin/bash
# wait-for-postgres.sh

set -e

host="$1"
shift
cmd="$@"
echo '$host'
until -xaqW%h:30 $CFG_MYSQL_HOST 3306
do
  echo "Waiting for database connection..."
  # wait for 5 seconds before check again
  sleep 5
done

>&2 echo "MySQL is up - executing command"
exec $cmd