---
collection: ceph
version: "19.2.2"
title: "Compression"
source_url: https://docs.ceph.com/en/squid/radosgw/compression/
fetched_at: 2026-07-27T16:40:38+00:00
---
# Compression

New in version Kraken.

The Ceph Object Gateway supports server-side compression of uploaded objects.
using any of the existing compression plugins.

> **Note:**
>
> The Reef release added a [compress-encrypted](../zone-features/index.md#feature-compress-encrypted) zonegroup
> feature to enable compression with [Server-Side Encryption](../encryption.md).

Supported compression plugins include the following:

- lz4
- snappy
- zlib
- zstd

## Configuration

Compression can be enabled on a storage class in the Zone’s placement target
by providing the `--compression=<type>` option to the command
`radosgw-admin zone placement modify`.

The compression `type` refers to the name of the compression plugin that will
be used when writing new object data. Each compressed object remembers which
plugin was used, so any change to this setting will neither affect Ceph’s
ability to decompress existing objects nor require existing objects to be
recompressed.

Compression settings apply to all new objects uploaded to buckets using this
placement target. Compression can be disabled by setting the `type` to an
empty string or `none`.

For example:

```
$ radosgw-admin zone placement modify \
      --rgw-zone default \
      --placement-id default-placement \
      --storage-class STANDARD \
      --compression zlib
{
...
    "placement_pools": [
        {
            "key": "default-placement",
            "val": {
                "index_pool": "default.rgw.buckets.index",
                "storage_classes": {
                    "STANDARD": {
                        "data_pool": "default.rgw.buckets.data",
                        "compression_type": "zlib"
                    }
                },
                "data_extra_pool": "default.rgw.buckets.non-ec",
                "index_type": 0,
            }
        }
    ],
...
}
```

> **Note:**
>
> A `default` zone is created for you if you have not done any
> previous [Multisite Configuration](../multisite.md).

## Statistics

Run the `radosgw-admin bucket stats` command to see compression statistics
for a given bucket:

```
radosgw-admin bucket stats --bucket=<name>
```

```
{
...
    "usage": {
        "rgw.main": {
            "size": 1075028,
            "size_actual": 1331200,
            "size_utilized": 592035,
            "size_kb": 1050,
            "size_kb_actual": 1300,
            "size_kb_utilized": 579,
            "num_objects": 104
        }
    },
...
}
```

Other commands and APIs will report object and bucket sizes based on their
uncompressed data.

The `size_utilized` and `size_kb_utilized` fields represent the total
size of compressed data, in bytes and kilobytes respectively.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
