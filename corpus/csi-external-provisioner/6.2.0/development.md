---
collection: csi-external-provisioner
version: "6.2.0"
title: "development"
source_url: https://github.com/kubernetes-csi/external-provisioner/blob/4f8ed53be40718152d081eb485fcc388e7bd77fd/doc/development.md
fetched_at: 2026-02-27T22:09:31+05:30
---
## Running on command line

For debugging, it's possible to run the external-provisioner on command line:

```sh
csi-provisioner -kubeconfig ~/.kube/config -v 5 -csi-address /run/csi/socket
```

## Vendoring

We use [dep](https://github.com/golang/dep) for management of `vendor/`.

`vendor/k8s.io` is manually copied from `staging/` directory of work-in-progress API for CSI, namely <https://github.com/kubernetes/kubernetes/pull/54463>.
