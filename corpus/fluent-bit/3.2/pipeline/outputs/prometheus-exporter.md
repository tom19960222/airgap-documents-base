---
collection: fluent-bit
version: "3.2"
title: "Prometheus Exporter"
source_url: https://github.com/fluent/fluent-bit-docs/blob/36106a0740d3f62f05d0e9e69b2c0e21dfa9de21/pipeline/outputs/prometheus-exporter.md
fetched_at: 2025-03-27T12:50:23+02:00
app_version: "3.2.10"
---
# Prometheus Exporter

The prometheus exporter allows you to take metrics from Fluent Bit and expose them such that a Prometheus instance can scrape them.

Important Note: The prometheus exporter only works with metric  plugins, such as Node Exporter Metrics

| Key | Description | Default |
| :--- | :--- | :--- |
| host | This is address Fluent Bit will bind to when hosting prometheus metrics. Note: `listen` parameter is deprecated from v1.9.0. | 0.0.0.0 |
| port | This is the port Fluent Bit will bind to when hosting prometheus metrics | 2021 |
| add\_label | This allows you to add custom labels to all metrics exposed through the prometheus exporter. You may have multiple of these fields |  |
| workers | The number of [workers](../../administration/multithreading.md#outputs) to perform flush operations for this output. | `1` |

## Getting Started

The Prometheus exporter only works with metrics captured from metric plugins. In the following example, host metrics are captured by the node exporter metrics plugin and then are routed to prometheus exporter. Within the output plugin two labels are added `app="fluent-bit"`and `color="blue"`

**Tab: fluent-bit.conf**

```text
# Node Exporter Metrics + Prometheus Exporter
# -------------------------------------------
# The following example collect host metrics on Linux and expose
# them through a Prometheus HTTP end-point.
#
# After starting the service try it with:
#
# $ curl http://127.0.0.1:2021/metrics
#
[SERVICE]
    flush           1
    log_level       info

[INPUT]
    name            node_exporter_metrics
    tag             node_metrics
    scrape_interval 2

[OUTPUT]
    name            prometheus_exporter
    match           node_metrics
    host            0.0.0.0
    port            2021
    # add user-defined labels
    add_label       app fluent-bit
    add_label       color blue
```

**Tab: fluent-bit.yaml**

```yaml
# Node Exporter Metrics + Prometheus Exporter
# -------------------------------------------
# The following example collect host metrics on Linux and expose
# them through a Prometheus HTTP end-point.
#
# After starting the service try it with:
#
# $ curl http://127.0.0.1:2021/metrics
#
service:
    flush: 1
    log_level: info
pipeline:
    inputs:
        - name: node_exporter_metrics
          tag:  node_metrics
          scrape_interval: 2
    outputs:
        - name: prometheus_exporter
          match: node_metrics
          host: 0.0.0.0
          port: 2021
          # add user-defined labels
          add_label:
            - app fluent-bit
            - color blue
```
