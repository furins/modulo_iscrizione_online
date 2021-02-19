#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER cirf;
    CREATE DATABASE cirf;
    GRANT ALL PRIVILEGES ON DATABASE cirf TO cirf;
EOSQL