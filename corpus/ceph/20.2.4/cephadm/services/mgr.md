---
collection: ceph
version: "20.2.4"
title: "MGR Service"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/cephadm/services/mgr.rst
fetched_at: 2026-08-18T01:32:45Z
---
<a id="mgr-cephadm-mgr"></a>

# MGR Service

The cephadm MGR service hosts multiple modules. These include the
[mgr-dashboard](../../mgr/dashboard.md#mgr-dashboard) and the cephadm manager module.

<a id="cephadm-mgr-networks"></a>

## Specifying Networks

The MGR service supports binding only to a specific IP within a network.

example spec file (leveraging a default placement):

```yaml
service_type: mgr
networks:
- 192.169.142.0/24
```

<a id="cephadm-mgr-co-location"></a>

# Allow co-location of MGR daemons

In deployment scenarios with just a single host, cephadm still needs
to deploy at least two MGR daemons in order to allow an automated
upgrade of the cluster. See ``mgr_standby_modules`` in
the [mgr-administrator-guide](../../mgr/administrator.md#mgr-administrator-guide) for further details.

See also: [cephadm_co_location](index.md#cephadm-co-location).

# Further Reading

* [ceph-manager-daemon](../../mgr/index.md#ceph-manager-daemon)
* [cephadm-manually-deploy-mgr](../troubleshooting.md#cephadm-manually-deploy-mgr)
