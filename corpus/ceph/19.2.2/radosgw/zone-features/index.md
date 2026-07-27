---
collection: ceph
version: "19.2.2"
title: "Zone Features"
source_url: https://docs.ceph.com/en/squid/radosgw/zone-features/
fetched_at: 2026-07-27T16:40:30+00:00
---
# Zone Features

Some features require support from all cooperating radosgws before they can be enabled. Each zone lists its `supported_features`, and each zonegroup lists its `enabled_features`. Before a feature can be enabled in the zonegroup, it must be supported by all of its zones.

On creation of new zones and zonegroups, all known features are supported and some features (see table below) are enabled by default. After upgrading an existing zone, however, new features must be enabled manually.

## Supported Features

| Feature | Release | Default |
| --- | --- | --- |
| [resharding](index.md#feature-resharding) | Reef | Enabled |
| [compress-encrypted](index.md#feature-compress-encrypted) | Reef | Disabled |
| [notification_v2](index.md#feature-notification-v2) | Squid | Enabled |

### resharding

This feature allows buckets to be resharded in a multisite configuration
without interrupting the replication of their objects. When
`rgw_dynamic_resharding` is enabled, it runs on each zone independently, and
zones may choose different shard counts for the same bucket. When buckets are
resharded manually with `radosgw-admin bucket reshard`, only that zone’s
bucket is modified. A zone feature should only be marked as supported after all
of its RGWs and OSDs have upgraded.

> **Note:**
>
> Dynamic resharding is not supported in multisite deployments prior to
> the Reef release.

### compress-encrypted

This feature enables support for combining [Server-Side Encryption](../encryption.md) and
[Compression](../compression.md) on the same object. Object data gets compressed before encryption.
Prior to Reef, multisite would not replicate such objects correctly, so all zones
must upgrade to Reef or later before enabling.

> **Warning:**
>
> The compression ratio may leak information about the encrypted data,
> and allow attackers to distinguish whether two same-sized objects might contain
> the same data. Due to these security considerations, this feature is disabled
> by default.

### notification_v2

This feature opts in to a new “v2” metadata format for bucket notifications and
topics. Unlike “v1”, this format is supported by multisite replication and can
scale to many topics.

Once this feature is enabled on all zonegroups in the realm, a background process
will convert existing v1 topics and bucket notifications into their v2 format.

## Commands

### Add support for a zone feature

On the cluster that contains the given zone:

```
radosgw-admin zone modify --rgw-zone={zone-name} --enable-feature={feature-name}
radosgw-admin period update --commit
```

> **Note:**
>
> The `period update` command only works if the zone belongs to a realm.
> Otherwise, all radosgws will need to restart before they notice the change.

### Remove support for a zone feature

On the cluster that contains the given zone:

```
radosgw-admin zone modify --rgw-zone={zone-name} --disable-feature={feature-name}
radosgw-admin period update --commit
```

### Enable a zonegroup feature

On any cluster in the realm:

```
radosgw-admin zonegroup modify --rgw-zonegroup={zonegroup-name} --enable-feature={feature-name}
radosgw-admin period update --commit
```

### Disable a zonegroup feature

On any cluster in the realm:

```
radosgw-admin zonegroup modify --rgw-zonegroup={zonegroup-name} --disable-feature={feature-name}
radosgw-admin period update --commit
```

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
