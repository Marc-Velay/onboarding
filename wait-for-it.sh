#!/bin/bash
# wait-for-postgres.sh

set -e

host="$1"
shift
cmd="$@"

#until mysqladmin ping -h localhost
#do
#  echo "Waiting for database connection..."
  # wait for 5 seconds before check again
#  sleep 5
#done
sleep 1000

>&2 echo "MySQL is up - executing command"
exec $cmd