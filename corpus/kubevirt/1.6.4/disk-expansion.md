---
collection: kubevirt
version: "1.6.4"
title: "Disk expansion"
source_url: https://github.com/kubevirt/kubevirt/blob/ac5324e8f6e7cda1cfe92542df3ceb0cd0d8e68f/docs/disk-expansion.md
fetched_at: 2026-03-16T09:25:18Z
---
# Disk expansion

For some storage methods, Kubernetes may support expanding storage in-use (allowVolumeExpansion feature).
KubeVirt can respond to it by making the additional storage available for the virtual machines.
This feature is currently off by default, and requires enabling a feature gate.
To enable it, add the ExpandDisks feature gate in the kubevirt object:

kubectl edit kubevirt -n kubevirt kubevirt
```yaml
spec:
  configuration:
    developerConfiguration:
      featureGates:
      - ExpandDisks
```

Enabling this feature does two things:
- Notify the virtual machine about size changes
- If the disk is a Filesystem PVC, the matching file is expanded to the remaining size (while reserving some space for file system overhead).
