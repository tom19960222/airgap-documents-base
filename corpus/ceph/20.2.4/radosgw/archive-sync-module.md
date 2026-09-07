---
collection: ceph
version: "20.2.4"
title: "Archive Sync Module"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/radosgw/archive-sync-module.rst
fetched_at: 2026-08-18T01:32:45Z
---
# Archive Sync Module

.. versionadded:: Nautilus

The Archive Sync module uses the RGW versioning feature of S3 objects to
maintain an archive zone that captures successive versions of objects
as they are updated in other zones.  Archive zone objects can
be removed only through gateways associated with the archive zone.

This enables a deployment where several
non-versioned zones replicate their data and metadata through their zone
gateways (mirror configuration) providing high availability to the end users,
while the archive zone captures data and metadata updates.

Deploying an archive zone in a multizone configuration enables the
flexibility of S3 object history in a single zone while saving the space
that replicas of versioned S3 objects would consume in the rest of the
zones.

## Archive Sync Tier Type Configuration

### How to Configure

See [Multisite Configuration](multisite.md) for multisite configuration instructions. The
archive sync module requires the creation of a new zone. The zone tier type needs
to be defined as ``archive``:

```bash
radosgw-admin zone create --rgw-zonegroup={zone-group-name} \
                            --rgw-zone={zone-name} \
                            --endpoints={http://fqdn}[,{http://fqdn}] \
                            --tier-type=archive
```
