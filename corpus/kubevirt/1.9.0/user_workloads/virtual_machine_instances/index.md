---
collection: kubevirt
version: "1.9.0"
title: "Virtual Machines Instances"
source_url: https://kubevirt.io/user-guide/user_workloads/virtual_machine_instances/
fetched_at: 2026-08-21T02:37:25+00:00
---
# Virtual Machines Instances

The `VirtualMachineInstance` type conceptionally has two parts:

- Information for making scheduling decisions
- Information about the virtual machine API

Every `VirtualMachineInstance` object represents a single running
virtual machine instance.

## API Overview

With the installation of KubeVirt, new types are added to the Kubernetes
API to manage Virtual Machines.

You can interact with the new resources (via `kubectl`) as you would
with any other API resource.

## VirtualMachineInstance API

> Note: A full API reference is available at
> <https://kubevirt.io/api-reference/>.

Here is an example of a VirtualMachineInstance object:

```
apiVersion: kubevirt.io/v1
kind: VirtualMachineInstance
metadata:
  name: testvmi-nocloud
spec:
  terminationGracePeriodSeconds: 30
  domain:
    resources:
      requests:
        memory: 1024M
    devices:
      disks:
      - name: containerdisk
        disk:
          bus: virtio
      - name: emptydisk
        disk:
          bus: virtio
      - disk:
          bus: virtio
        name: cloudinitdisk
  volumes:
  - name: containerdisk
    containerDisk:
      image: kubevirt/fedora-cloud-container-disk-demo:latest
  - name: emptydisk
    emptyDisk:
      capacity: "2Gi"
  - name: cloudinitdisk
    cloudInitNoCloud:
      userData: |-
        #cloud-config
        password: fedora
        chpasswd: { expire: False }
```

This example uses a fedora cloud image in combination with cloud-init
and an ephemeral empty disk with a capacity of `2Gi`. For the sake of
simplicity, the volume sources in this example are ephemeral and don't
require a provisioner in your cluster.

## Additional Information

- Using instancetypes and preferences with a VirtualMachine:
  [Instancetypes and preferences](../instancetypes/index.md)
- More information about persistent and ephemeral volumes:
  [Disks and Volumes](../../storage/disks_and_volumes/index.md)
- How to access a VirtualMachineInstance via `console` or `vnc`:
  [Console Access](../accessing_virtual_machines/index.md)
- How to customize VirtualMachineInstances with `cloud-init`:
  [Cloud Init](../startup_scripts/index.md#cloud-init)
