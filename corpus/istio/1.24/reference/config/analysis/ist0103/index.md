---
collection: istio
version: "1.24"
title: "PodMissingProxy"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/config/analysis/ist0103/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
This message occurs when the sidecar is not present or not working correctly.

This most commonly occurs when you enable auto-injection but do not restart your
pods afterwards, causing the sidecar to be missing.

To resolve this problem, restart your pods and try again.

For example, to restart the pods, use this command:

```bash
$ kubectl rollout restart deployment
```
