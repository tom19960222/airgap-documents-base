---
collection: telegraf
version: "1.30.3"
title: "Wavefront Parser Plugin"
source_url: https://github.com/influxdata/telegraf/blob/fd4af886672c8256ff17c888935a801d941894c4/plugins/parsers/wavefront/README.md
fetched_at: 2024-05-20T10:00:01-06:00
---
# Wavefront Parser Plugin

Wavefront Data Format is metrics are parsed directly into Telegraf metrics.
For more information about the Wavefront Data Format see
[here](https://docs.wavefront.com/wavefront_data_format.html).

## Configuration

```toml
[[inputs.file]]
  files = ["example"]

  ## Data format to consume.
  ## Each data format has its own unique set of configuration options, read
  ## more about them here:
  ##   https://github.com/influxdata/telegraf/blob/master/docs/DATA_FORMATS_INPUT.md
  data_format = "wavefront"
```

There are no additional configuration options for Wavefront Data Format
line-protocol.
