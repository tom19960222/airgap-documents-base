---
collection: csi-external-provisioner
version: "6.0.2"
title: "development"
source_url: https://github.com/kubernetes-csi/external-provisioner/blob/753b615576935c6abdd9eb770708abb5845f2ee6/doc/development.md
fetched_at: 2026-08-07T02:24:53Z
---
## Running on command line

For debugging, it's possible to run the external-provisioner on command line:

```sh
csi-provisioner -kubeconfig ~/.kube/config -v 5 -csi-address /run/csi/socket
```

## Vendoring

We use [dep](https://github.com/golang/dep) for management of `vendor/`.

`vendor/k8s.io` is manually copied from `staging/` directory of work-in-progress API for CSI, namely <https://github.com/kubernetes/kubernetes/pull/54463>.
