offmetric
=========

Send stdout and stderr to metric server(s), like PrometheusDB, InfluxDB or just syslog.


## Syntax

    echo foo | offmetric --server influxdb://influx.offscale.io --server prometheusdb://prometheus.offscale.io
