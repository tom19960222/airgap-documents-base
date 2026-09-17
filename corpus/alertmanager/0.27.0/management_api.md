---
collection: alertmanager
version: "0.27.0"
title: "Management API"
source_url: https://github.com/prometheus/alertmanager/blob/0aa3c2aad14cff039931923ab16b26b7481783b5/docs/management_api.md
fetched_at: 2024-02-28T11:35:54Z
---
# Management API

Alertmanager provides a set of management API to ease automation and integrations.

### Health check

```
GET /-/healthy
HEAD /-/healthy
```

This endpoint always returns 200 and should be used to check Alertmanager health.

### Readiness check

```
GET /-/ready
HEAD /-/ready
```

This endpoint returns 200 when Alertmanager is ready to serve traffic (i.e. respond to queries).

### Reload

```
POST /-/reload
```

This endpoint triggers a reload of the Alertmanager configuration file.

An alternative way to trigger a configuration reload is by sending a `SIGHUP` to the Alertmanager process.
