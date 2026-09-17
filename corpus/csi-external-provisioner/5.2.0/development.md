---
collection: csi-external-provisioner
version: "5.2.0"
title: "development"
source_url: https://github.com/kubernetes-csi/external-provisioner/blob/12a344a40072d655cb9374a93483305f1a1be557/doc/development.md
fetched_at: 2025-01-17T04:16:07-08:00
---
## Running on command line

For debugging, it's possible to run the external-provisioner on command line:

```sh
csi-provisioner -kubeconfig ~/.kube/config -v 5 -csi-address /run/csi/socket
```

## Vendoring

We use [dep](https://github.com/golang/dep) for management of `vendor/`.

`vendor/k8s.io` is manually copied from `staging/` directory of work-in-progress API for CSI, namely <https://github.com/kubernetes/kubernetes/pull/54463>.
