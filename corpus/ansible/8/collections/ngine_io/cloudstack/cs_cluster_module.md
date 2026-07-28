---
collection: ansible
version: "8"
title: "ngine_io.cloudstack.cs_cluster module – Manages host clusters on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ngine_io/cloudstack/cs_cluster_module.html
fetched_at: 2026-07-28T02:45:42+00:00
---
# ngine_io.cloudstack.cs_cluster module – Manages host clusters on Apache CloudStack based clouds.

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
> see [Requirements](cs_cluster_module.md#ansible-collections-ngine-io-cloudstack-cs-cluster-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_cluster`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_cluster_module.md#synopsis)
- [Requirements](cs_cluster_module.md#requirements)
- [Parameters](cs_cluster_module.md#parameters)
- [Notes](cs_cluster_module.md#notes)
- [Examples](cs_cluster_module.md#examples)
- [Return Values](cs_cluster_module.md#return-values)

## [Synopsis](cs_cluster_module.md#id1)

- Create, update and remove clusters.

## [Requirements](cs_cluster_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_cluster_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  **Choices:**   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  **Default:** `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **cluster_type**  string | Type of the cluster.  Required if *state=present*  **Choices:**   - `"CloudManaged"` - `"ExternalManaged"` |
| **guest_vswitch_name**  string | Name of virtual switch used for guest traffic in the cluster.  This would override zone wide traffic label setting. |
| **guest_vswitch_type**  string | Type of virtual switch used for guest traffic in the cluster.  Allowed values are, vmwaresvs (for VMware standard vSwitch) and vmwaredvs (for VMware distributed vSwitch)  **Choices:**   - `"vmwaresvs"` - `"vmwaredvs"` |
| **hypervisor**  string | Name the hypervisor to be used.  Required if *state=present*.  Possible values are `KVM`, `VMware`, `BareMetal`, `XenServer`, `LXC`, `HyperV`, `UCS`, `OVM`, `Simulator`. |
| **name**  string / required | name of the cluster. |
| **ovm3_cluster**  string | Ovm3 native OCFS2 clustering enabled for cluster. |
| **ovm3_pool**  string | Ovm3 native pooling enabled for cluster. |
| **ovm3_vip**  string | Ovm3 vip to use for pool (and cluster). |
| **password**  string | Password for the cluster. |
| **pod**  string | Name of the pod in which the cluster belongs to. |
| **public_vswitch_name**  string | Name of virtual switch used for public traffic in the cluster.  This would override zone wide traffic label setting. |
| **public_vswitch_type**  string | Type of virtual switch used for public traffic in the cluster.  Allowed values are, vmwaresvs (for VMware standard vSwitch) and vmwaredvs (for VMware distributed vSwitch)  **Choices:**   - `"vmwaresvs"` - `"vmwaredvs"` |
| **state**  string | State of the cluster.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"disabled"` - `"enabled"` |
| **url**  string | URL for the cluster |
| **username**  string | Username for the cluster. |
| **vms_ip_address**  string | IP address of the VSM associated with this cluster. |
| **vms_password**  string | Password for the VSM associated with this cluster. |
| **vms_username**  string | Username for the VSM associated with this cluster. |
| **zone**  string / required | Name of the zone in which the cluster belongs to. |

## [Notes](cs_cluster_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_cluster_module.md#id5)

```yaml+jinja
- name: Ensure a cluster is present
  ngine_io.cloudstack.cs_cluster:
    name: kvm-cluster-01
    zone: ch-zrh-ix-01
    hypervisor: KVM
    cluster_type: CloudManaged

- name: Ensure a cluster is disabled
  ngine_io.cloudstack.cs_cluster:
    name: kvm-cluster-01
    zone: ch-zrh-ix-01
    state: disabled

- name: Ensure a cluster is enabled
  ngine_io.cloudstack.cs_cluster:
    name: kvm-cluster-01
    zone: ch-zrh-ix-01
    state: enabled

- name: Ensure a cluster is absent
  ngine_io.cloudstack.cs_cluster:
    name: kvm-cluster-01
    zone: ch-zrh-ix-01
    state: absent
```

## [Return Values](cs_cluster_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **allocation_state**  string | State of the cluster.  **Returned:** success  **Sample:** `"Enabled"` |
| **cluster_type**  string | Type of the cluster.  **Returned:** success  **Sample:** `"ExternalManaged"` |
| **cpu_overcommit_ratio**  string | The CPU overcommit ratio of the cluster.  **Returned:** success  **Sample:** `"1.0"` |
| **hypervisor**  string | Hypervisor of the cluster  **Returned:** success  **Sample:** `"VMware"` |
| **id**  string | UUID of the cluster.  **Returned:** success  **Sample:** `"04589590-ac63-4ffc-93f5-b698b8ac38b6"` |
| **managed_state**  string | Whether this cluster is managed by CloudStack.  **Returned:** success  **Sample:** `"Managed"` |
| **memory_overcommit_ratio**  string | The memory overcommit ratio of the cluster.  **Returned:** success  **Sample:** `"1.0"` |
| **name**  string | Name of the cluster.  **Returned:** success  **Sample:** `"cluster01"` |
| **ovm3_vip**  string | Ovm3 VIP to use for pooling and/or clustering  **Returned:** success  **Sample:** `"10.10.10.101"` |
| **pod**  string | Name of pod the cluster is in.  **Returned:** success  **Sample:** `"pod01"` |
| **zone**  string | Name of zone the cluster is in.  **Returned:** success  **Sample:** `"ch-gva-2"` |

### Authors

- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
- [Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
