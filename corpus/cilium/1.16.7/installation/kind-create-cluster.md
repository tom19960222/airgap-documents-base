---
collection: cilium
version: "1.16.7"
title: "kind-create-cluster"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/installation/kind-create-cluster.rst
fetched_at: 2025-02-13T12:04:31Z
---
To create a cluster with the configuration defined above, pass the
``kind-config.yaml`` you created with the ``--config`` flag of kind.

```shell-session
kind create cluster --config=kind-config.yaml
```

After a couple of seconds or minutes, a 4 nodes cluster should be created.

A new ``kubectl`` context (``kind-kind``) should be added to ``KUBECONFIG`` or, if unset,
to ``${HOME}/.kube/config``:

```shell-session
kubectl cluster-info --context kind-kind
```

> **Note:**
> The cluster nodes will remain in state ``NotReady`` until Cilium is deployed.
> This behavior is expected.
