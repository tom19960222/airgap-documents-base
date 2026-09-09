---
collection: rook
version: "1.20.7"
title: "CephObjectRealm CRD"
source_url: https://github.com/rook/rook/blob/95a8e2a8b61cf7f8152213939f995c88a2e72ab6/Documentation/CRDs/Object-Storage/ceph-object-realm-crd.md
fetched_at: 2026-09-02T11:15:12-06:00
---
Rook allows creation of a realm in a [Ceph Object Multisite](../../Storage-Configuration/Object-Storage-RGW/ceph-object-multisite.md)
configuration through a CRD. The following settings are available for Ceph object store realms.

## Example

```yaml
apiVersion: ceph.rook.io/v1
kind: CephObjectRealm
metadata:
  name: realm-a
  namespace: rook-ceph
# This endpoint in this section needs is an endpoint from the master zone  in the master zone group of realm-a. See object-multisite.md for more details.
spec:
  pull:
    endpoint: http://10.2.105.133:80
  defaultRealm: true
```

## Settings

### Metadata

* `name`: The name of the object realm to create
* `namespace`: The namespace of the Rook cluster where the object realm is created.

### Spec

* `pull`: This optional section is for the pulling the realm for another ceph cluster.
    * `endpoint`: The endpoint in the realm from another ceph cluster you want to pull from. This endpoint must be in the master zone of the master zone group of the realm.
* `defaultRealm`: When set to true, Rook will mark the CephObjectStore's realm as the default realm in the Ceph cluster. Only one realm can be marked default. Ceph does not allow default to be unassigned after it is assigned; a different realm can be marked default instead.
