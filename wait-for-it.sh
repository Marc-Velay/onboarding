#!/bin/bash
# wait-for-postgres.sh

set -e

host="$1"
shift
cmd="$@"
echo '$host'
until mysql -h "$host" -U "mysql" -c '\l'; do
  >&2 echo "MySQL is unavailable - sleeping"
  sleep 1
done

>&2 echo "MySQL is up - executing command"
exec $cmd