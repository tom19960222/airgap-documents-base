---
collection: telegraf
version: "1.30.3"
title: "Dedup Processor Plugin"
source_url: https://github.com/influxdata/telegraf/blob/fd4af886672c8256ff17c888935a801d941894c4/plugins/processors/dedup/README.md
fetched_at: 2024-05-20T10:00:01-06:00
---
# Dedup Processor Plugin

Filter metrics whose field values are exact repetitions of the previous values.
This plugin will store its state between runs if the `statefile` option in the
agent config section is set.

## Global configuration options <!-- @/docs/includes/plugin_config.md -->

In addition to the plugin-specific configuration settings, plugins support
additional global and plugin configuration settings. These settings are used to
modify metrics, tags, and field or create aliases and configure ordering, etc.
See the [CONFIGURATION.md][CONFIGURATION.md] for more details.

[CONFIGURATION.md]: ../../../docs/CONFIGURATION.md#plugins

## Configuration

```toml @sample.conf
# Filter metrics with repeating field values
[[processors.dedup]]
  ## Maximum time to suppress output
  dedup_interval = "600s"
```

## Example

```diff
- cpu,cpu=cpu0 time_idle=42i,time_guest=1i
- cpu,cpu=cpu0 time_idle=42i,time_guest=2i
- cpu,cpu=cpu0 time_idle=42i,time_guest=2i
- cpu,cpu=cpu0 time_idle=44i,time_guest=2i
- cpu,cpu=cpu0 time_idle=44i,time_guest=2i
+ cpu,cpu=cpu0 time_idle=42i,time_guest=1i
+ cpu,cpu=cpu0 time_idle=42i,time_guest=2i
+ cpu,cpu=cpu0 time_idle=44i,time_guest=2i
```
