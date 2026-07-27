---
collection: ceph
version: "19.2.2"
title: "Ceph Object Gateway Swift API"
source_url: https://docs.ceph.com/en/squid/radosgw/swift/
fetched_at: 2026-07-27T16:40:34+00:00
---
# Ceph Object Gateway Swift API

Ceph supports a RESTful API that is compatible with the basic data access model of the [Swift API](https://developer.openstack.org/api-ref/object-store/index.html).

## API

- [Authentication](auth/index.md)
- [Service Ops](serviceops/index.md)
- [Container Ops](containerops/index.md)
- [Object Ops](objectops/index.md)
- [Temp URL Ops](tempurl/index.md)
- [Tutorial](tutorial/index.md)
- [Java](java/index.md)
- [Python](python/index.md)
- [Ruby](ruby/index.md)

## Features Support

The following table describes the support status for current Swift functional features:

| Feature | Status | Remarks |
| --- | --- | --- |
| **Authentication** | Supported |  |
| **Get Account Metadata** | Supported |  |
| **Swift ACLs** | Supported | Supports a subset of Swift ACLs |
| **List Containers** | Supported |  |
| **Delete Container** | Supported |  |
| **Create Container** | Supported |  |
| **Get Container Metadata** | Supported |  |
| **Update Container Metadata** | Supported |  |
| **Delete Container Metadata** | Supported |  |
| **List Objects** | Supported |  |
| **Static Website** | Supported |  |
| **Create Object** | Supported |  |
| **Create Large Object** | Supported |  |
| **Delete Object** | Supported |  |
| **Get Object** | Supported |  |
| **Copy Object** | Supported |  |
| **Get Object Metadata** | Supported |  |
| **Update Object Metadata** | Supported |  |
| **Expiring Objects** | Supported |  |
| **Temporary URLs** | Partial Support | No support for container-level keys |
| **Object Versioning** | Partial Support | No support for `X-History-Location` |
| **CORS** | Not Supported |  |

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
