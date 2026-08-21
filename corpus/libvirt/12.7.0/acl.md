---
collection: libvirt
version: "12.7.0"
title: "Client access control"
source_url: https://libvirt.org/acl.html
fetched_at: 2026-08-21T04:10:07+00:00
---
# Client access control

Libvirt's client access control framework allows administrators to setup fine
grained permission rules across client users, managed objects and API
operations. This allows client connections to be locked down to a minimal set of
privileges.

Contents

- [Access control introduction](acl.md#access-control-introduction)
- [Access control drivers](acl.md#access-control-drivers)
- [Objects and permissions](acl.md#objects-and-permissions)

# [Access control introduction](acl.md#id1)

In a default configuration, the libvirtd daemon has three levels of access
control. All connections start off in an unauthenticated state, where the only
API operations allowed are those required to complete authentication. After
successful authentication, a connection either has full, unrestricted access to
all libvirt API calls, or is locked down to only "read only" (see 'Anonymous' in
the table below) operations, according to what socket a client connection
originated on.

The access control framework allows authenticated connections to have fine
grained permission rules to be defined by the administrator. Every API call in
libvirt has a set of permissions that will be validated against the object being
used. For example, the virDomainSetSchedulerParametersFlags method will
check whether the client user has the write permission on the domain
object instance passed in as a parameter. Further permissions will also be
checked if certain flags are set in the API call. In addition to checks on the
object passed in to an API call, some methods will filter their results. For
example the virConnectListAllDomains method will check the
search_domains on the connect object, but will also filter the returned
domain objects to only those on which the client user has the getattr
permission.

# [Access control drivers](acl.md#id2)

The access control framework is designed as a pluggable system to enable future
integration with arbitrary access control technologies. By default, the none
driver is used, which does no access control checks at all. At this time,
libvirt ships with support for using
[polkit](https://www.freedesktop.org/wiki/Software/polkit/) as a real access
control driver. To learn how to use the polkit access driver consult [the
configuration docs](aclpolkit.md).

The access driver is configured in the libvirtd.conf configuration file,
using the access_drivers parameter. This parameter accepts an array of
access control driver names. If more than one access driver is requested, then
all must succeed in order for access to be granted. To enable 'polkit' as the
driver:

```
# augtool -s set '/files/etc/libvirt/libvirtd.conf/access_drivers[1]' polkit
```

And to reset back to the default (no-op) driver

```
# augtool -s rm /files/etc/libvirt/libvirtd.conf/access_drivers
```

**Note:** changes to libvirtd.conf require that the libvirtd daemon be
restarted.

# [Objects and permissions](acl.md#id3)

Libvirt applies access control to all the main object types in its API. Each
object type, in turn, has a set of permissions defined. To determine what
permissions are checked for specific API call, consult the [API reference
manual](https://libvirt.org/html/index.html) documentation for the API in question.

### `connect` - virConnectPtr

| Permission | Description | Anonymous |
| --- | --- | --- |
| detect-storage-pools | Detect storage pools |  |
| getattr | Access connection | yes |
| interface-transaction | Interface transactions |  |
| pm-control | Use host power management |  |
| read | Read host | yes |
| search-domains | List domains | yes |
| search-interfaces | List interfaces | yes |
| search-networks | List networks | yes |
| search-node-devices | List node devices | yes |
| search-nwfilter-bindings | List network filter bindings | yes |
| search-nwfilters | List network filters | yes |
| search-secrets | List secrets | yes |
| search-storage-pools | List storage pools | yes |
| write | Write host |  |

### `domain` - virDomainPtr

| Permission | Description | Anonymous |
| --- | --- | --- |
| block-read | Read domain block |  |
| block-write | Write domain block |  |
| checkpoint | Checkpoint domain |  |
| core-dump | Dump domain |  |
| delete | Delete domain |  |
| fs-freeze | Freeze and thaw domain filesystems |  |
| fs-trim | Trim domain filesystems |  |
| getattr | Access domain | yes |
| hibernate | Hibernate domain |  |
| init-control | Domain init control |  |
| inject-nmi | Inject domain NMI |  |
| mem-read | Read domain memory |  |
| migrate | Migrate domain |  |
| open-device | Open domain device |  |
| open-graphics | Open domain graphics |  |
| open-namespace | Open domain namespace |  |
| pm-control | Use domain power management |  |
| read | Read domain | yes |
| read-secure | Read secure domain |  |
| reset | Reset domain |  |
| save | Save domain |  |
| screenshot | Take domain screenshot |  |
| send-input | Send domain input |  |
| send-signal | Send domain signal |  |
| set-password | Set password of the domain's account |  |
| set-time | Write domain time |  |
| snapshot | Snapshot domain |  |
| start | Start domain |  |
| stop | Stop domain |  |
| suspend | Suspend domain |  |
| write | Write domain |  |

### `interface` - virInterfacePtr

| Permission | Description | Anonymous |
| --- | --- | --- |
| delete | Delete interface |  |
| getattr | Access interface | yes |
| read | Read interface | yes |
| save | Save interface |  |
| start | Start interface |  |
| stop | Stop interface |  |
| write | Write interface |  |

### `network` - virNetworkPtr

| Permission | Description | Anonymous |
| --- | --- | --- |
| delete | Delete network |  |
| getattr | Access network | yes |
| read | Read network | yes |
| save | Save network |  |
| search-ports | List network ports |  |
| start | Start network |  |
| stop | Stop network |  |
| write | Write network |  |

### `network-port` - virNetworkPortPtr

| Permission | Description | Anonymous |
| --- | --- | --- |
| create | Create network port |  |
| delete | Delete network port |  |
| getattr | Access network port | yes |
| read | Read network port | yes |
| write | Read network port |  |

### `node-device` - virNodeDevicePtr

| Permission | Description | Anonymous |
| --- | --- | --- |
| delete | Delete node device |  |
| detach | Detach node device |  |
| getattr | Access node device | yes |
| read | Read node device | yes |
| save | Save node device |  |
| start | Start node device |  |
| stop | Stop node device |  |
| write | Write node device |  |

### `nwfilter` - virNWFilterPtr

| Permission | Description | Anonymous |
| --- | --- | --- |
| delete | Delete network filter |  |
| getattr | Access network filter | yes |
| read | Read network filter | yes |
| save | Save network filter |  |
| write | Write network filter |  |

### `nwfilter-binding` - virNWFilterBindingPtr

| Permission | Description | Anonymous |
| --- | --- | --- |
| create | Create network filter binding |  |
| delete | Delete network filter binding |  |
| getattr | Access network filter | yes |
| read | Read network filter binding | yes |

### `secret` - virSecretPtr

| Permission | Description | Anonymous |
| --- | --- | --- |
| delete | Delete secret |  |
| getattr | Access secret | yes |
| read | Read secret | yes |
| read-secure | Read secure secret |  |
| save | Save secret |  |
| write | Write secret |  |

### `storage-pool` - virStoragePoolPtr

| Permission | Description | Anonymous |
| --- | --- | --- |
| delete | Delete storage pool |  |
| format | Format storage pool |  |
| getattr | Access storage pool | yes |
| read | Read storage pool | yes |
| refresh | Refresh storage pool |  |
| save | Save storage pool |  |
| search-storage-vols | List storage pool volumes |  |
| start | Start storage pool |  |
| stop | Stop storage pool |  |
| write | Write storage pool |  |

### `storage-vol` - virStorageVolPtr

| Permission | Description | Anonymous |
| --- | --- | --- |
| create | Create storage volume |  |
| data-read | Read storage volume data |  |
| data-write | Write storage volume data |  |
| delete | Delete storage volume |  |
| format | Format storage volume |  |
| getattr | Access storage volume | yes |
| read | Read storage volume | yes |
| resize | Resize storage volume |  |
