---
collection: csi-external-provisioner
version: "6.1.2"
title: "development"
source_url: https://github.com/kubernetes-csi/external-provisioner/blob/bc5885430bd0312da7dbea82f6e09b5cc1456251/doc/development.md
fetched_at: 2026-08-08T02:29:56Z
---
## Running on command line

For debugging, it's possible to run the external-provisioner on command line:

```sh
csi-provisioner -kubeconfig ~/.kube/config -v 5 -csi-address /run/csi/socket
```

## Vendoring

We use [dep](https://github.com/golang/dep) for management of `vendor/`.

`vendor/k8s.io` is manually copied from `staging/` directory of work-in-progress API for CSI, namely <https://github.com/kubernetes/kubernetes/pull/54463>.
