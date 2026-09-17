---
collection: telegraf
version: "1.30.3"
title: "Prometheus Text-Based Format Parser Plugin"
source_url: https://github.com/influxdata/telegraf/blob/fd4af886672c8256ff17c888935a801d941894c4/plugins/parsers/prometheus/README.md
fetched_at: 2024-05-20T10:00:01-06:00
---
# Prometheus Text-Based Format Parser Plugin

There are no additional configuration options for [Prometheus Text-Based
Format][]. The metrics are parsed directly into Telegraf metrics. It is used
internally in [prometheus input](/plugins/inputs/prometheus) or can be used in
[http_listener_v2](/plugins/inputs/http_listener_v2) to simulate Pushgateway.

[Prometheus Text-Based Format]: https://prometheus.io/docs/instrumenting/exposition_formats/#text-based-format

## Configuration

```toml
[[inputs.file]]
  files = ["example"]

  ## Data format to consume.
  ## Each data format has its own unique set of configuration options, read
  ## more about them here:
  ##   https://github.com/influxdata/telegraf/blob/master/docs/DATA_FORMATS_INPUT.md
  data_format = "prometheus"

```
