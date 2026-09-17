---
collection: istio
version: "1.24"
title: "Cleanup"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/traffic-management/locality-load-balancing/cleanup/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Cleanup steps for locality load balancing."
---
Now that you've completed the locality load balancing tasks, let's
cleanup.

## Remove generated files

```bash
$ rm -f sample.yaml helloworld-region*.zone*.yaml
```

## Remove the `sample` namespace

```bash
$ for CTX in "$CTX_PRIMARY" "$CTX_R1_Z1" "$CTX_R1_Z2" "$CTX_R2_Z3" "$CTX_R3_Z4"; \
  do \
    kubectl --context="$CTX" delete ns sample --ignore-not-found=true; \
  done
```

**Congratulations!** You successfully completed the locality load balancing task!
