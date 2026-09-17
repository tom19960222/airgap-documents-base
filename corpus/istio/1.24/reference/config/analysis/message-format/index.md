---
collection: istio
version: "1.24"
title: "Analyzer Message Format"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/config/analysis/message-format/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
The `istioctl analyze` command provides messages in the format:

```plain
<level> [<code>] (<affected-resource>) <message-details>
```

The `<affected-resource>` field expands to:

```plain
<resource-kind> <resource-name>.<resource-namespace>
```

For example:

```plain
Error [IST0101] (VirtualService httpbin.default) Referenced gateway not found: "httpbin-gateway-bogus"
```

The `<message-details>` field contains a detailed description that may contain further information to help resolve the problem. The namespace suffix is omitted for cluster-scoped resources, for example `namespace`.
