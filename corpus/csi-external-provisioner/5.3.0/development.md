---
collection: csi-external-provisioner
version: "5.3.0"
title: "development"
source_url: https://github.com/kubernetes-csi/external-provisioner/blob/1a7e9381439295969ad0336f1e21791f7dc3abe8/doc/development.md
fetched_at: 2025-05-30T10:04:18-07:00
---
## Running on command line

For debugging, it's possible to run the external-provisioner on command line:

```sh
csi-provisioner -kubeconfig ~/.kube/config -v 5 -csi-address /run/csi/socket
```

## Vendoring

We use [dep](https://github.com/golang/dep) for management of `vendor/`.

`vendor/k8s.io` is manually copied from `staging/` directory of work-in-progress API for CSI, namely <https://github.com/kubernetes/kubernetes/pull/54463>.
