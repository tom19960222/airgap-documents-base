---
collection: telegraf
version: "1.30.3"
title: "Code Style"
source_url: https://github.com/influxdata/telegraf/blob/fd4af886672c8256ff17c888935a801d941894c4/docs/developers/CODE_STYLE.md
fetched_at: 2024-05-20T10:00:01-06:00
---
# Code Style

Code is required to be formatted using `gofmt`, this covers most code style
requirements.  It is also highly recommended to use `goimports` to
automatically order imports.

Please try to keep lines length under 80 characters, the exact number of
characters is not strict but it generally helps with readability.
