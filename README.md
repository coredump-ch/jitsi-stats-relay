[![Docker][docker-badge]][docker]

# Jitsi JVB InfluxDB Stats Relay

A Python 3 script to relay data from Jitsi (with enabled Colibri Stats API) to
an InfluxDB server.

## Configuration

Set the following env variables:

- `JVB_COLIBRI_HOST`: The JVB colibri host
- `JVB_COLIBRI_PORT`: The JVB colibri port (default 8080)
- `INFLUXDB_HOST`: InfluxDB hostname
- `INFLUXDB_PORT`: InfluxDB port
- `INFLUXDB_USER`: InfluxDB username
- `INFLUXDB_PASS`: InfluxDB password

You can also place those env variables in an `.env` file, they will be read
automatically.

## Docker

A docker image is built at
[coredump/jitsi-stats-relay](https://hub.docker.com/r/coredump/jitsi-stats-relay/)
for every push to master.

<!-- Badges -->
[docker]: https://hub.docker.com/r/coredump/jitsi-stats-relay/
[docker-badge]: https://img.shields.io/badge/docker%20image-coredump%2Fttn--relay-blue.svg
