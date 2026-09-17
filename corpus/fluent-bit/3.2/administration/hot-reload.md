---
collection: fluent-bit
version: "3.2"
title: "Hot reload"
source_url: https://github.com/fluent/fluent-bit-docs/blob/36106a0740d3f62f05d0e9e69b2c0e21dfa9de21/administration/hot-reload.md
fetched_at: 2025-03-27T12:50:23+02:00
app_version: "3.2.10"
---
# Hot reload

Fluent Bit supports the reloading feature when enabled in the configuration file
or on the command line with `-Y` or `--enable-hot-reload` option.

Hot reloading is supported on Linux, macOS, and Windows operating systems.

## Update the configuration

To get started with reloading over HTTP, enable the HTTP Server
in the configuration file:

**Tab: fluent-bit.conf**

```text
[SERVICE]
    HTTP_Server  On
    HTTP_Listen  0.0.0.0
    HTTP_PORT    2020
    Hot_Reload   On
...
```

**Tab: fluent-bit.yaml**

```yaml
service:
    http_server: on
    http_listen: 0.0.0.0
    http_port: 2020
    hot_reload: on
```

## How to reload

After updating the configuration, use one of the following methods to perform a
hot reload:

### HTTP

Use the following HTTP endpoints to perform a hot reload:

- `PUT /api/v2/reload`
- `POST /api/v2/reload`

For using curl to reload Fluent Bit, users must specify an empty request body as:

```text
curl -X POST -d '{}' localhost:2020/api/v2/reload
```

### Signal

Hot reloading can be used with `SIGHUP`.

`SIGHUP` signal isn't supported on Windows.

## Confirm a reload

Use one of the following methods to confirm the reload occurred.

### HTTP

Obtain a count of hot reload using the HTTP endpoint:

- `GET /api/v2/reload`

The endpoint returns `hot_reload_count` as follows:

```json
{"hot_reload_count":3}
```

The default value of the counter is `0`.
