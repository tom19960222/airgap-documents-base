---
collection: ceph
version: "19.2.2"
title: "Ceph Object Gateway"
source_url: https://docs.ceph.com/en/squid/radosgw/
fetched_at: 2026-07-27T16:38:47+00:00
---
# Ceph Object Gateway

[Ceph Object Gateway](../glossary/index.md#term-Ceph-Object-Gateway) is an object storage interface built on top of
`librados`. It provides a RESTful gateway between applications and Ceph
Storage Clusters. [Ceph Object Storage](../glossary/index.md#term-Ceph-Object-Storage) supports two interfaces:

1. **S3-compatible:** Provides object storage functionality with an interface
   that is compatible with a large subset of the Amazon S3 RESTful API.
2. **Swift-compatible:** Provides object storage functionality with an interface
   that is compatible with a large subset of the OpenStack Swift API.

Ceph Object Storage uses the Ceph Object Gateway daemon (`radosgw`), an HTTP
server designed to interact with a Ceph Storage Cluster. The Ceph Object
Gateway provides interfaces that are compatible with both Amazon S3 and
OpenStack Swift, and it has its own user management. Ceph Object Gateway can
use a single Ceph Storage cluster to store data from Ceph File System and from
Ceph Block device clients. The S3 API and the Swift API share a common
namespace, which means that it is possible to write data to a Ceph Storage
Cluster with one API and then retrieve that data with the other API.

![](../_images/ditaa-c80628bafff42fe0c3c4475cdc0f216bc8ca813d.png)

> **Note:**
>
> Ceph Object Storage does **NOT** use the Ceph Metadata Server.

- [HTTP Frontends](frontends/index.md)
- [Multisite Configuration](multisite/index.md)
- [Zone Features](zone-features/index.md)
- [Pool Placement and Storage Classes](placement/index.md)
- [Multisite Sync Policy Configuration](multisite-sync-policy/index.md)
- [Configuring Pools](pools/index.md)
- [Config Reference](config-ref/index.md)
- [Admin Guide](admin/index.md)
- [User Accounts](account/index.md)
- [S3 API](s3/index.md)
- [IAM API](iam/index.md)
- [Data caching and CDN](rgw-cache/index.md)
- [Swift API](swift/index.md)
- [Admin Ops API](adminops/index.md)
- [Python binding](api/index.md)
- [Export over NFS](nfs/index.md)
- [OpenStack Keystone Integration](keystone/index.md)
- [OpenStack Barbican Integration](barbican/index.md)
- [HashiCorp Vault Integration](vault/index.md)
- [KMIP Integration](kmip/index.md)
- [Open Policy Agent Integration](opa/index.md)
- [Multi-tenancy](multitenancy/index.md)
- [Compression](compression/index.md)
- [LDAP Authentication](ldap-auth/index.md)
- [Server-Side Encryption](encryption/index.md)
- [Bucket Policy](bucketpolicy/index.md)
- [Dynamic bucket index resharding](dynamicresharding/index.md)
- [Multi factor authentication](mfa/index.md)
- [Sync Modules](sync-modules/index.md)
- [Bucket Notifications](notifications/index.md)
- [Data Layout in RADOS](layout/index.md)
- [STS](STS/index.md)
- [STS Lite](STSLite/index.md)
- [Keycloak](keycloak/index.md)
- [Session Tags](session-tags/index.md)
- [Role](role/index.md)
- [Orphan List and Associated Tooling](orphans/index.md)
- [OpenID Connect Provider](oidc/index.md)
- [Troubleshooting](troubleshooting/index.md)
- [Manpage radosgw](../man/8/radosgw/index.md)
- [Manpage radosgw-admin](../man/8/radosgw-admin/index.md)
- [QAT Acceleration for Encryption and Compression](qat-accel/index.md)
- [S3-select](s3select/index.md)
- [Lua Scripting](lua-scripting/index.md)
- [D3N Data Cache](d3n_datacache/index.md)
- [Cloud Transition](cloud-transition/index.md)
- [Metrics](metrics/index.md)

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
