---
collection: telegraf
version: "1.30.3"
title: "Nagios Parser Plugin"
source_url: https://github.com/influxdata/telegraf/blob/fd4af886672c8256ff17c888935a801d941894c4/plugins/parsers/nagios/README.md
fetched_at: 2024-05-20T10:00:01-06:00
---
# Nagios Parser Plugin

The `nagios` data format parses the output of nagios plugins.

## Configuration

```toml
[[inputs.exec]]
  ## Commands array
  commands = ["/usr/lib/nagios/plugins/check_load -w 5,6,7 -c 7,8,9"]

  ## Data format to consume.
  ## Each data format has its own unique set of configuration options, read
  ## more about them here:
  ##   https://github.com/influxdata/telegraf/blob/master/docs/DATA_FORMATS_INPUT.md
  data_format = "nagios"
```
