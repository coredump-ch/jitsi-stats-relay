[![Build status](https://img.shields.io/github/actions/workflow/status/coredump-ch/jitsi-stats-relay/ci.yml?branch=main)](https://github.com/coredump-ch/jitsi-stats-relay/actions?query=workflow%3ACI)
[![Docker][docker-badge]][docker]

# Jitsi JVB InfluxDB Stats Relay

A Python 3 script to relay data from Jitsi (with enabled Colibri Stats API) to
an InfluxDB server.

## Configuration

Set the following env variables:

- `JVB_HOST`: The JVB colibri host
- `JVB_PORT`: The JVB colibri port (default 8080)
- `JVB_PROTO`: The JVB colibri protocol (default http)
- `INFLUXDB_HOST`: InfluxDB hostname
- `INFLUXDB_PORT`: InfluxDB port
- `INFLUXDB_USER`: InfluxDB username
- `INFLUXDB_PASS`: InfluxDB password
- `INTERVAL_SECONDS`: Check interval in seconds, defaults to 10

You can also place those env variables in an `.env` file, they will be read
automatically.

## Docker

A docker image is built at
[coredump/jitsi-stats-relay](https://hub.docker.com/r/coredump/jitsi-stats-relay/)
for every push to main.

<!-- Badges -->
[docker]: https://hub.docker.com/r/coredump/jitsi-stats-relay/
[docker-badge]: https://img.shields.io/badge/docker%20image-coredump%2Fjitsi--stats--relay-blue.svg
