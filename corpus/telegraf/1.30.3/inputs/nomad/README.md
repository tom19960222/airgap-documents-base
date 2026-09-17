---
collection: telegraf
version: "1.30.3"
title: "Hashicorp Nomad Input Plugin"
source_url: https://github.com/influxdata/telegraf/blob/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/nomad/README.md
fetched_at: 2024-05-20T10:00:01-06:00
---
# Hashicorp Nomad Input Plugin

The Nomad plugin must grab metrics from every Nomad agent of the
cluster. Telegraf may be present in every node and connect to the agent
locally. In this case should be something like `http://127.0.0.1:4646`.

> Tested on Nomad 1.1.6

## Global configuration options <!-- @/docs/includes/plugin_config.md -->

In addition to the plugin-specific configuration settings, plugins support
additional global and plugin configuration settings. These settings are used to
modify metrics, tags, and field or create aliases and configure ordering, etc.
See the [CONFIGURATION.md][CONFIGURATION.md] for more details.

[CONFIGURATION.md]: ../../../docs/CONFIGURATION.md#plugins

## Configuration

```toml @sample.conf
# Read metrics from the Nomad API
[[inputs.nomad]]
  ## URL for the Nomad agent
  # url = "http://127.0.0.1:4646"

  ## Set response_timeout (default 5 seconds)
  # response_timeout = "5s"

  ## Optional TLS Config
  # tls_ca = /path/to/cafile
  # tls_cert = /path/to/certfile
  # tls_key = /path/to/keyfile
```

## Metrics

Both Nomad servers and agents collect various metrics. For every details, please
have a look at Nomad following documentation:

- [https://www.nomadproject.io/docs/operations/metrics](https://www.nomadproject.io/docs/operations/metrics)
- [https://www.nomadproject.io/docs/operations/telemetry](https://www.nomadproject.io/docs/operations/telemetry)

## Example Output
