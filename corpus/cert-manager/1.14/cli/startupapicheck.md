---
collection: cert-manager
version: "1.14"
title: "startupapicheck CLI reference"
source_url: https://github.com/cert-manager/website/blob/d2e1bdfbbe23fcf24dcb68ab54353a65a4131c20/content/v1.14-docs/cli/startupapicheck.md
fetched_at: 2026-09-15T21:21:15Z
app_version: "1.14.7"
---
```
Check that cert-manager started successfully

Usage:
  startupapicheck [command]

Available Commands:
  check       Check cert-manager components
  help        Help about any command

Flags:
  -h, --help                           help for startupapicheck
      --log-flush-frequency duration   Maximum number of seconds between log flushes (default 5s)
      --logging-format string          Sets the log format. Permitted formats: "json" (gated by LoggingBetaOptions), "text". (default "text")
  -v, --v Level[=2]                    number for the log level verbosity
      --vmodule pattern=N,...          comma-separated list of pattern=N settings for file-filtered logging (only works for text log format)

Use "startupapicheck [command] --help" for more information about a command.
```
