---
collection: ansible
version: "8"
title: "ngine_io.cloudstack.cs_storage_pool module – Manages Primary Storage Pools on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ngine_io/cloudstack/cs_storage_pool_module.html
fetched_at: 2026-07-28T02:46:27+00:00
---
# ngine_io.cloudstack.cs_storage_pool module – Manages Primary Storage Pools on Apache CloudStack based clouds.

> **Note:**
>
> This module is part of the [ngine_io.cloudstack collection](https://galaxy.ansible.com/ui/repo/published/ngine_io/cloudstack/) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.cloudstack`.
> You need further requirements to be able to use this module,
> see [Requirements](cs_storage_pool_module.md#ansible-collections-ngine-io-cloudstack-cs-storage-pool-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_storage_pool`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_storage_pool_module.md#synopsis)
- [Requirements](cs_storage_pool_module.md#requirements)
- [Parameters](cs_storage_pool_module.md#parameters)
- [Notes](cs_storage_pool_module.md#notes)
- [Examples](cs_storage_pool_module.md#examples)
- [Return Values](cs_storage_pool_module.md#return-values)

## [Synopsis](cs_storage_pool_module.md#id1)

- Create, update, put into maintenance, disable, enable and remove storage pools.

## [Requirements](cs_storage_pool_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_storage_pool_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allocation_state**  string | Allocation state of the storage pool.  **Choices:**   - `"enabled"` - `"disabled"` - `"maintenance"` |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  **Choices:**   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  **Default:** `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **capacity_bytes**  integer | Bytes CloudStack can provision from this storage pool. |
| **capacity_iops**  integer | Bytes CloudStack can provision from this storage pool. |
| **cluster**  string | Name of the cluster. |
| **hypervisor**  string | Required when creating a zone scoped pool.  Possible values are `KVM`, `VMware`, `BareMetal`, `XenServer`, `LXC`, `HyperV`, `UCS`, `OVM`, `Simulator`. |
| **managed**  boolean | Whether the storage pool should be managed by CloudStack.  Only considered on creation.  **Choices:**   - `false` - `true` |
| **name**  string / required | Name of the storage pool. |
| **pod**  string | Name of the pod. |
| **provider**  string | Name of the storage provider e.g. SolidFire, SolidFireShared, DefaultPrimary, CloudByte.  **Default:** `"DefaultPrimary"` |
| **scope**  string | The scope of the storage pool.  Defaults to cluster when `cluster` is provided, otherwise zone.  **Choices:**   - `"cluster"` - `"zone"` |
| **state**  string | State of the storage pool.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **storage_tags**  aliases: storage_tag  list / elements=string | Tags associated with this storage pool. |
| **storage_url**  string | URL of the storage pool.  Required if *state=present*. |
| **zone**  string / required | Name of the zone in which the host should be deployed. |

## [Notes](cs_storage_pool_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_storage_pool_module.md#id5)

```yaml+jinja
- name: ensure a zone scoped storage_pool is present
  ngine_io.cloudstack.cs_storage_pool:
    zone: zone01
    storage_url: rbd://admin:SECRET@ceph-mons.domain/poolname
    provider: DefaultPrimary
    name: Ceph RBD
    scope: zone
    hypervisor: KVM

- name: ensure a cluster scoped storage_pool is disabled
  ngine_io.cloudstack.cs_storage_pool:
    name: Ceph RBD
    zone: zone01
    cluster: cluster01
    pod: pod01
    storage_url: rbd://admin:SECRET@ceph-the-mons.domain/poolname
    provider: DefaultPrimary
    scope: cluster
    allocation_state: disabled

- name: ensure a cluster scoped storage_pool is in maintenance
  ngine_io.cloudstack.cs_storage_pool:
    name: Ceph RBD
    zone: zone01
    cluster: cluster01
    pod: pod01
    storage_url: rbd://admin:SECRET@ceph-the-mons.domain/poolname
    provider: DefaultPrimary
    scope: cluster
    allocation_state: maintenance

- name: ensure a storage_pool is absent
  ngine_io.cloudstack.cs_storage_pool:
    name: Ceph RBD
    zone: zone01
    state: absent
```

## [Return Values](cs_storage_pool_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **allocation_state**  string | The state of the storage pool.  **Returned:** success  **Sample:** `"enabled"` |
| **capacity_iops**  integer | IOPS CloudStack can provision from this storage pool  **Returned:** when available  **Sample:** `60000` |
| **cluster**  string | The name of the cluster.  **Returned:** when scope is cluster  **Sample:** `"Cluster01"` |
| **created**  string | Date of the pool was created.  **Returned:** success  **Sample:** `"2014-12-01T14:57:57+0100"` |
| **disk_size_allocated**  integer | The pool’s currently allocated disk space.  **Returned:** success  **Sample:** `2443517624320` |
| **disk_size_total**  integer | The total size of the pool.  **Returned:** success  **Sample:** `3915055693824` |
| **disk_size_used**  integer | The pool’s currently used disk size.  **Returned:** success  **Sample:** `1040862622180` |
| **hypervisor**  string | Hypervisor related to this storage pool.  **Returned:** when available  **Sample:** `"KVM"` |
| **id**  string | UUID of the pool.  **Returned:** success  **Sample:** `"a3fca65a-7db1-4891-b97c-48806a978a96"` |
| **overprovision_factor**  string | The overprovision factor of the storage pool.  **Returned:** success  **Sample:** `"2.0"` |
| **path**  string | The storage pool path used in the storage_url.  **Returned:** success  **Sample:** `"poolname"` |
| **pod**  string | The name of the pod.  **Returned:** when scope is cluster  **Sample:** `"Cluster01"` |
| **scope**  string | The scope of the storage pool.  **Returned:** success  **Sample:** `"cluster"` |
| **state**  string | The state of the storage pool as returned by the API.  **Returned:** success  **Sample:** `"Up"` |
| **storage_capabilities**  dictionary | Capabilities of the storage pool.  **Returned:** success  **Sample:** `{"VOLUME_SNAPSHOT_QUIESCEVM": "false"}` |
| **storage_tags**  list / elements=string | the tags for the storage pool.  **Returned:** success  **Sample:** `["perf", "ssd"]` |
| **suitable_for_migration**  boolean | Whether the storage pool is suitable to migrate a volume or not.  **Returned:** success  **Sample:** `false` |
| **zone**  string | The name of the zone.  **Returned:** success  **Sample:** `"Zone01"` |

### Authors

- Netservers Ltd. (@netservers)
- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
- [Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
