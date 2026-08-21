---
collection: kubevirt
version: "1.9.0"
title: "Basic use"
source_url: https://kubevirt.io/user-guide/user_workloads/basic_use/
fetched_at: 2026-08-21T02:37:11+00:00
---
# Basic use

Using KubeVirt should be fairly natural if you are used to working with
Kubernetes.

The primary way of using KubeVirt is by working with the KubeVirt kinds
in the Kubernetes API:

```
$ kubectl create -f vmi.yaml
$ kubectl wait --for=condition=Ready vmis/my-vmi
$ kubectl get vmis
$ kubectl delete vmis testvmi
```

The following pages describe how to use and discover the API, manage,
and access virtual machines.

## User Interface

KubeVirt does not come with a UI, it is only extending the Kubernetes
API with virtualization functionality.
