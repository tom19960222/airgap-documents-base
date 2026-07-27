---
collection: ceph
version: "19.2.2"
title: "Service Operations"
source_url: https://docs.ceph.com/en/squid/radosgw/s3/serviceops/
fetched_at: 2026-07-27T16:42:45+00:00
---
# Service Operations

## List Buckets

`GET /` returns a list of buckets created by the user making the request. `GET /` only
returns buckets created by an authenticated user. You cannot make an anonymous request.

### Syntax

```
GET / HTTP/1.1
Host: cname.domain.com

Authorization: AWS {access-key}:{hash-of-header-and-secret}
```

### Response Entities

| Name | Type | Description |
| --- | --- | --- |
| `Buckets` | Container | Container for list of buckets. |
| `Bucket` | Container | Container for bucket information. |
| `Name` | String | Bucket name. |
| `CreationDate` | Date | UTC time when the bucket was created. |
| `ListAllMyBucketsResult` | Container | A container for the result. |
| `Owner` | Container | A container for the bucket owner’s `ID` and `DisplayName`. |
| `ID` | String | The bucket owner’s ID. |
| `DisplayName` | String | The bucket owner’s display name. |

## Get Usage Stats

Gets usage stats per user, similar to the admin command [Get User Usage Stats](../../admin/index.md#rgw-user-usage-stats).

### Syntax

```
GET /?usage HTTP/1.1
Host: cname.domain.com

Authorization: AWS {access-key}:{hash-of-header-and-secret}
```

### Response Entities

| Name | Type | Description |
| --- | --- | --- |
| `Summary` | Container | Summary of total stats by user. |
| `TotalBytes` | Integer | Bytes used by user |
| `TotalBytesRounded` | Integer | Bytes rounded to the nearest 4k boundary |
| `TotalEntries` | Integer | Total object entries |

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
