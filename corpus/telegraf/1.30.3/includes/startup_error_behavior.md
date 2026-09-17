---
collection: telegraf
version: "1.30.3"
title: "startup_error_behavior"
source_url: https://github.com/influxdata/telegraf/blob/fd4af886672c8256ff17c888935a801d941894c4/docs/includes/startup_error_behavior.md
fetched_at: 2024-05-20T10:00:01-06:00
---
In addition to the plugin-specific and global configuration settings the plugin
supports options for specifying the behavior when experiencing startup errors
using the `startup_error_behavior` setting. Available values are:

- `error`:  Telegraf with stop and exit in case of startup errors. This is the
            default behavior.
- `ignore`: Telegraf will ignore startup errors for this plugin and disables it
            but continues processing for all other plugins.
- `retry`:  Telegraf will try to startup the plugin in every gather or write
            cycle in case of startup errors. The plugin is disabled until
            the startup succeeds.
