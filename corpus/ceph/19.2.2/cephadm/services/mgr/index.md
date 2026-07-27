---
collection: ceph
version: "19.2.2"
title: "MGR Service"
source_url: https://docs.ceph.com/en/squid/cephadm/services/mgr/
fetched_at: 2026-07-27T16:39:21+00:00
---
# MGR Service

The cephadm MGR service hosts multiple modules. These include the
[Ceph Dashboard](../../../mgr/dashboard/index.md#mgr-dashboard) and the cephadm manager module.

## Specifying Networks

The MGR service supports binding only to a specific IP within a network.

example spec file (leveraging a default placement):

```yaml
service_type: mgr
networks:
- 192.169.142.0/24
```

### Allow co-location of MGR daemons

In deployment scenarios with just a single host, cephadm still needs
to deploy at least two MGR daemons in order to allow an automated
upgrade of the cluster. See `mgr_standby_modules` in
the [ceph-mgr administrator’s guide](../../../mgr/administrator/index.md#mgr-administrator-guide) for further details.

See also: [Co-location of daemons](../index.md#cephadm-co-location).

### Further Reading

- [Ceph Manager Daemon](../../../mgr/index.md#ceph-manager-daemon)
- [Manually Deploying a Manager Daemon](../../troubleshooting/index.md#cephadm-manually-deploy-mgr)

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
