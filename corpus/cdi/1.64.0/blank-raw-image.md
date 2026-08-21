---
collection: cdi
version: "1.64.0"
title: "How to create Blank Raw Image User Guide"
source_url: https://github.com/kubevirt/containerized-data-importer/blob/v1.64.0/doc/blank-raw-image.md
fetched_at: 2025-12-11T21:02:45+02:00
---
# How to create Blank Raw Image User Guide
The purpose of this document is to show how to create a data volume containing a new blank raw image.

## Prerequesites
You have a Kubernetes cluster up and running with CDI installed and at least one PersistentVolume is available or can be created dynamically.

## Create Blank Raw Image with DataVolume manifest

Create the following [DataVolume manifest](../manifests/example/blank-image-datavolume.yaml):

```bash
apiVersion: cdi.kubevirt.io/v1beta1
kind: DataVolume
metadata:
  name: blank-image-datavolume
spec:
  source:
      blank: {}
  storage:
    resources:
      requests:
        storage: 500Mi
```

Deploy the DataVolume manifest:

```bash
kubectl create -f blank-image-datavolume.yaml
```

An importer pod will be spawned and the new image will be created on your PV.
