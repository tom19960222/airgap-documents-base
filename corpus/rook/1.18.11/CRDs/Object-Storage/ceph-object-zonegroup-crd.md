---
collection: rook
version: "1.18.11"
title: "CephObjectZoneGroup CRD"
source_url: https://github.com/rook/rook/blob/8059413c805f8ed3a0992af0113c002b0250805e/Documentation/CRDs/Object-Storage/ceph-object-zonegroup-crd.md
fetched_at: 2026-05-27T11:20:14-06:00
---
Rook allows creation of zone groups in a [Ceph Object Multisite](../../Storage-Configuration/Object-Storage-RGW/ceph-object-multisite.md)
configuration through a CRD. The following settings are available for Ceph object store zone groups.

## Example

```yaml
apiVersion: ceph.rook.io/v1
kind: CephObjectZoneGroup
metadata:
  name: zonegroup-a
  namespace: rook-ceph
spec:
  realm: realm-a
```

## Settings

### Metadata

* `name`: The name of the object zone group to create
* `namespace`: The namespace of the Rook cluster where the object zone group is created.

### Spec

* `realm`: The object realm in which the zone group will be created. This matches the name of the object realm CRD.
