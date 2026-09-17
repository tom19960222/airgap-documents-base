---
collection: telegraf
version: "1.30.3"
title: "Input Data Formats"
source_url: https://github.com/influxdata/telegraf/blob/fd4af886672c8256ff17c888935a801d941894c4/docs/DATA_FORMATS_INPUT.md
fetched_at: 2024-05-20T10:00:01-06:00
---
# Input Data Formats

Telegraf contains many general purpose plugins that support parsing input data
using a configurable parser into [metrics][].  This allows, for example, the
`kafka_consumer` input plugin to process messages in any of InfluxDB Line
Protocol, JSON format, or Apache Avro format.

- [Avro](/plugins/parsers/avro)
- [Binary](/plugins/parsers/binary)
- [Collectd](/plugins/parsers/collectd)
- [CSV](/plugins/parsers/csv)
- [Dropwizard](/plugins/parsers/dropwizard)
- [Form URL Encoded](/plugins/parsers/form_urlencoded)
- [Graphite](/plugins/parsers/graphite)
- [Grok](/plugins/parsers/grok)
- [InfluxDB Line Protocol](/plugins/parsers/influx)
- [JSON](/plugins/parsers/json)
- [JSON v2](/plugins/parsers/json_v2)
- [Logfmt](/plugins/parsers/logfmt)
- [Nagios](/plugins/parsers/nagios)
- [OpenTSDB](/plugins/parsers/opentsdb)
- [Prometheus](/plugins/parsers/prometheus)
- [PrometheusRemoteWrite](/plugins/parsers/prometheusremotewrite)
- [Value](/plugins/parsers/value), ie: 45 or "booyah"
- [Wavefront](/plugins/parsers/wavefront)
- [XPath](/plugins/parsers/xpath) (supports XML, JSON, MessagePack, Protocol Buffers)

Any input plugin containing the `data_format` option can use it to select the
desired parser:

```toml
[[inputs.exec]]
  ## Commands array
  commands = ["/tmp/test.sh", "/usr/bin/mycollector --foo=bar"]

  ## measurement name suffix (for separating different commands)
  name_suffix = "_mycollector"

  ## Data format to consume.
  data_format = "json"
```

[metrics]: /docs/METRICS.md
