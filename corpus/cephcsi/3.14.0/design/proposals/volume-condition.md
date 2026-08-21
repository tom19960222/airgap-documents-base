---
collection: cephcsi
version: "3.14.0"
title: "Support for CSI `VolumeCondition` aka Volume Health Checker"
source_url: https://github.com/ceph/ceph-csi/blob/v3.14.0/docs/design/proposals/volume-condition.md
fetched_at: 2025-04-10T13:22:55Z
---
# Support for CSI `VolumeCondition` aka Volume Health Checker

## health-checker API

Under `internal/health-checker`  the Manager for health-checking is
implemented. The Manager can start a checking process for a given path, return
the (un)healthy state and stop the checking process when the volume is not
needed anymore.

The Manager is responsible for creating a suitable checker for the requested
path. If the path is a block-device, the BlockChecker should be created. For a
filesystem path (directory), the FileChecker is appropriate.

## CephFS

The health-checker writes to the file `csi-volume-condition.ts` in the root of
the volume. This file contains a JSON formatted timestamp.

A new `data` directory is introduced for newly created volumes. During the
`NodeStageVolume` call the root of the volume is mounted, and the `data`
directory is bind-mounted inside the container when `NodePublishVolume` is
called.

The `data` directory makes it possible to place Ceph-CSI internal files in the
root of the volume, without that the user/application has access to it.
