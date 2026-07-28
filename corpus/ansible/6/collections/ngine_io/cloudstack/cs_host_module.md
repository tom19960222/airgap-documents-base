---
collection: ansible
version: "6"
title: "ngine_io.cloudstack.cs_host module – Manages hosts on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ngine_io/cloudstack/cs_host_module.html
fetched_at: 2026-07-28T00:15:27+00:00
---
# ngine_io.cloudstack.cs_host module – Manages hosts on Apache CloudStack based clouds.

> **Note:**
>
> This module is part of the [ngine_io.cloudstack collection](https://galaxy.ansible.com/ngine_io/cloudstack) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.cloudstack`.
> You need further requirements to be able to use this module,
> see [Requirements](cs_host_module.md#ansible-collections-ngine-io-cloudstack-cs-host-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_host`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_host_module.md#synopsis)
- [Requirements](cs_host_module.md#requirements)
- [Parameters](cs_host_module.md#parameters)
- [Notes](cs_host_module.md#notes)
- [Examples](cs_host_module.md#examples)
- [Return Values](cs_host_module.md#return-values)

## [Synopsis](cs_host_module.md#id1)

- Create, update and remove hosts.

## [Requirements](cs_host_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_host_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allocation_state**  string | Allocation state of the host.  Choices:   - `"enabled"` - `"disabled"` - `"maintenance"` |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  Choices:   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  Default: `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **cluster**  string | Name of the cluster. |
| **host_tags**  aliases: host_tag  list / elements=string | Tags of the host. |
| **hypervisor**  string | Name of the cluster.  Required if *state=present* and host does not yet exist.  Possible values are `KVM`, `VMware`, `BareMetal`, `XenServer`, `LXC`, `HyperV`, `UCS`, `OVM`, `Simulator`. |
| **name**  aliases: ip_address  string / required | Name of the host. |
| **password**  string | Password for the host.  Required if *state=present* and host does not yet exist. |
| **pod**  string | Name of the pod.  Required if *state=present* and host does not yet exist. |
| **state**  string | State of the host.  Choices:   - `"present"` ← (default) - `"absent"` |
| **url**  string | Url of the host used to create a host.  If not provided, `http://` and param *name* is used as url.  Only considered if *state=present* and host does not yet exist. |
| **username**  string | Username for the host.  Required if *state=present* and host does not yet exist. |
| **zone**  string / required | Name of the zone in which the host should be deployed. |

## [Notes](cs_host_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_host_module.md#id5)

```yaml+jinja
- name: Ensure a host is present but disabled
  ngine_io.cloudstack.cs_host:
    name: pod01.zone01.example.com
    cluster: vcenter.example.com/zone01/cluster01
    pod: pod01
    zone: zone01
    hypervisor: VMware
    allocation_state: disabled
    host_tags:
    - perf
    - gpu

- name: Ensure an existing host is disabled
  ngine_io.cloudstack.cs_host:
    name: pod01.zone01.example.com
    zone: zone01
    allocation_state: disabled

- name: Ensure an existing host is enabled
  ngine_io.cloudstack.cs_host:
    name: pod01.zone01.example.com
    zone: zone01
    allocation_state: enabled

- name: Ensure a host is absent
  ngine_io.cloudstack.cs_host:
    name: pod01.zone01.example.com
    zone: zone01
    state: absent
```

## [Return Values](cs_host_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **allocation_state:**  string | Allocation state of the host.  Returned: success  Sample: `"enabled"` |
| **capabilities**  string | Capabilities of the host.  Returned: success  Sample: `"hvm"` |
| **cluster**  string | Cluster of the host.  Returned: success  Sample: `"vcenter.example.com/zone/cluster01"` |
| **cluster_type**  string | Type of the cluster of the host.  Returned: success  Sample: `"ExternalManaged"` |
| **cpu_allocated**  string | Amount in percent of the host’s CPU currently allocated.  Returned: success  Sample: `"166.25%"` |
| **cpu_number**  string | Number of CPUs of the host.  Returned: success  Sample: `"24"` |
| **cpu_sockets**  integer | Number of CPU sockets of the host.  Returned: success  Sample: `2` |
| **cpu_speed**  integer | CPU speed in Mhz  Returned: success  Sample: `1999` |
| **cpu_used**  string | Amount of the host’s CPU currently used.  Returned: success  Sample: `"33.6%"` |
| **cpu_with_overprovisioning**  string | Amount of the host’s CPU after applying the cpu.overprovisioning.factor.  Returned: success  Sample: `"959520.0"` |
| **created**  string | Date when the host was created.  Returned: success  Sample: `"2015-05-03T15:05:51+0200"` |
| **disconnected**  string | Date when the host was disconnected.  Returned: success  Sample: `"2015-05-03T15:05:51+0200"` |
| **disk_size_allocated**  integer | Host’s currently allocated disk size.  Returned: success  Sample: `2593` |
| **disk_size_total**  integer | Total disk size of the host  Returned: success  Sample: `259300` |
| **events**  string | Events available for the host  Returned: success  Sample: `"Ping; HostDown; AgentConnected; AgentDisconnected; PingTimeout; ShutdownRequested; Remove; StartAgentRebalance; ManagementServerDown"` |
| **gpu_group**  list / elements=string | GPU cards present in the host.  Returned: success  Sample: `[]` |
| **ha_host**  boolean | Whether the host is a HA host.  Returned: success  Sample: `false` |
| **has_enough_capacity**  boolean | Whether the host has enough CPU and RAM capacity to migrate a VM to it.  Returned: success  Sample: `true` |
| **host_tags**  string | Comma-separated list of tags for the host.  Returned: success  Sample: `"perf"` |
| **host_type**  string | Type of the host.  Returned: success  Sample: `"Routing"` |
| **host_version**  string | Version of the host.  Returned: success  Sample: `"4.5.2"` |
| **hypervisor**  string | Host’s hypervisor.  Returned: success  Sample: `"VMware"` |
| **hypervisor_version**  string | Hypervisor version.  Returned: success  Sample: `"5.1"` |
| **ip_address**  string | IP address of the host  Returned: success  Sample: `"10.10.10.1"` |
| **is_local_storage_active**  boolean | Whether the local storage is available or not.  Returned: success  Sample: `false` |
| **last_pinged**  string | Date and time the host was last pinged.  Returned: success  Sample: `"1970-01-17T17:27:32+0100"` |
| **management_server_id**  integer | Management server ID of the host.  Returned: success  Sample: `345050593418` |
| **memory_allocated**  integer | Amount of the host’s memory currently allocated.  Returned: success  Sample: `69793218560` |
| **memory_total**  integer | Total of memory of the host.  Returned: success  Sample: `206085263360` |
| **memory_used**  integer | Amount of the host’s memory currently used.  Returned: success  Sample: `65504776192` |
| **name**  string | Name of the host.  Returned: success  Sample: `"esx32.example.com"` |
| **network_kbs_read**  integer | Incoming network traffic on the host.  Returned: success  Sample: `0` |
| **network_kbs_write**  integer | Outgoing network traffic on the host.  Returned: success  Sample: `0` |
| **os_category**  string | OS category name of the host.  Returned: success  Sample: `"..."` |
| **out_of_band_management**  string | Host out-of-band management information.  Returned: success  Sample: `"..."` |
| **pod**  string | Pod name of the host.  Returned: success  Sample: `"Pod01"` |
| **removed**  string | Date and time the host was removed.  Returned: success  Sample: `"1970-01-17T17:27:32+0100"` |
| **resource_state**  string | Resource state of the host.  Returned: success  Sample: `"Enabled"` |
| **state**  string | State of the host.  Returned: success  Sample: `"Up"` |
| **suitable_for_migration**  string | Whether this host is suitable (has enough capacity and satisfies all conditions like hosttags, max guests VM limit, etc) to migrate a VM to it or not.  Returned: success  Sample: `"True"` |
| **zone**  string | Zone of the host.  Returned: success  Sample: `"zone01"` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
[Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
