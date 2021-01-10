"""
Relay stats from Jitsi JVB to InfluxDB.
"""
import os
from typing import Any, Dict

import dotenv
import influxdb
import requests


# Helper function
def require_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise RuntimeError('Missing {} env variable'.format(name))
    return value.strip()


# Helper function
def env(name: str, default: str) -> str:
    return os.environ.get(name, default).strip()


# Config from .env file
dotenv.load_dotenv(dotenv.find_dotenv())

# JVB
JVB_COLIBRI_HOST = require_env('JVB_HOST')
JVB_COLIBRI_PORT = env('JVB_PORT', '8080')

# InfluxDB
INFLUXDB_HOST = require_env('INFLUXDB_HOST')
INFLUXDB_PORT = require_env('INFLUXDB_PORT')
INFLUXDB_USER = require_env('INFLUXDB_USER')
INFLUXDB_PASS = require_env('INFLUXDB_PASS')
INFLUXDB_DB = require_env('INFLUXDB_DB')

# Create InfluxDB client
influxdb_client = influxdb.InfluxDBClient(
    INFLUXDB_HOST, INFLUXDB_PORT,
    INFLUXDB_USER, INFLUXDB_PASS,
    INFLUXDB_DB,
    ssl=True, verify_ssl=True, timeout=10,
)


def log_to_influxdb(
    client: influxdb.InfluxDBClient,
    fields: Dict[str, Any],
    tags: Dict[str, Any],
):
    """
    Log the specified data to InfluxDB.
    """
    json_body = [{
        'measurement': 'jvb_stats',
        'tags': tags,
        'fields': fields,
    }]
    client.write_points(json_body)


def main():
    # Fetch stats
    r = requests.get('{}:{}/colibri/stats'.format(JVB_COLIBRI_HOST, JVB_COLIBRI_PORT))
    r.raise_for_status()
    stats = r.json()

    # Gather data to log
    fields = {}
    for k, v in stats.items():
        if isinstance(v, (str, int, float)):
            fields[k] = v
        else:
            print('Warning: Skipping field {} (not a supported type)'.format(k))

    # Log to InfluxDB
    tags = {'jvb_host': JVB_COLIBRI_HOST}
    log_to_influxdb(influxdb_client, fields, tags)


if __name__ == '__main__':
    main()
