---
collection: ansible
version: "8"
title: "ngine_io.cloudstack.cs_physical_network module – Manages physical networks on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ngine_io/cloudstack/cs_physical_network_module.html
fetched_at: 2026-07-28T02:46:09+00:00
---
# ngine_io.cloudstack.cs_physical_network module – Manages physical networks on Apache CloudStack based clouds.

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
> see [Requirements](cs_physical_network_module.md#ansible-collections-ngine-io-cloudstack-cs-physical-network-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_physical_network`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_physical_network_module.md#synopsis)
- [Requirements](cs_physical_network_module.md#requirements)
- [Parameters](cs_physical_network_module.md#parameters)
- [Notes](cs_physical_network_module.md#notes)
- [Examples](cs_physical_network_module.md#examples)
- [Return Values](cs_physical_network_module.md#return-values)

## [Synopsis](cs_physical_network_module.md#id1)

- Create, update and remove networks.
- Enabled and disabled Network Service Providers
- Enables Internal LoadBalancer and VPC/VirtualRouter elements as required

## [Requirements](cs_physical_network_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_physical_network_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  **Choices:**   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  **Default:** `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **broadcast_domain_range**  string | broadcast domain range for the physical network[Pod or Zone].  **Choices:**   - `"POD"` - `"ZONE"` |
| **domain**  string | Domain the network is owned by. |
| **isolation_method**  string | Isolation method for the physical network.  **Choices:**   - `"VLAN"` - `"VXLAN"` - `"GRE"` - `"L3"` |
| **name**  aliases: physical_network  string / required | Name of the physical network. |
| **network_speed**  string | The speed for the physical network.  **Choices:**   - `"1G"` - `"10G"` |
| **nsps_disabled**  list / elements=string | List of Network Service Providers to disable. |
| **nsps_enabled**  list / elements=string | List of Network Service Providers to enable. |
| **poll_async**  boolean | Poll async jobs until job has finished.  **Choices:**   - `false` - `true` ← (default) |
| **state**  string | State of the physical network.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"disabled"` - `"enabled"` |
| **tags**  aliases: tag  string | A tag to identify this network.  Physical networks support only one tag.  To remove an existing tag pass an empty string. |
| **vlan**  string | The VLAN/VNI Ranges of the physical network. |
| **zone**  string / required | Name of the zone in which the network belongs. |

## [Notes](cs_physical_network_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_physical_network_module.md#id5)

```yaml+jinja
- name: Ensure a network is present
  ngine_io.cloudstack.cs_physical_network:
    name: net01
    zone: zone01
    isolation_method: VLAN
    broadcast_domain_range: ZONE

- name: Set a tag on a network
  ngine_io.cloudstack.cs_physical_network:
    name: net01
    zone: zone01
    tag: overlay

- name: Remove tag on a network
  ngine_io.cloudstack.cs_physical_network:
    name: net01
    zone: zone01
    tag: ""

- name: Ensure a network is enabled with specific nsps enabled
  ngine_io.cloudstack.cs_physical_network:
    name: net01
    zone: zone01
    isolation_method: VLAN
    vlan: 100-200,300-400
    broadcast_domain_range: ZONE
    state: enabled
    nsps_enabled:
      - virtualrouter
      - internallbvm
      - vpcvirtualrouter

- name: Ensure a network is enabled with VXLAN isolation
  ngine_io.cloudstack.cs_physical_network:
    name: net01
    zone: zone01
    isolation_method: VXLAN
    vlan: 42-8192
    broadcast_domain_range: ZONE
    state: enabled

- name: Ensure a network is disabled
  ngine_io.cloudstack.cs_physical_network:
    name: net01
    zone: zone01
    state: disabled

- name: Ensure a network is enabled
  ngine_io.cloudstack.cs_physical_network:
    name: net01
    zone: zone01
    state: enabled

- name: Ensure a network is absent
  ngine_io.cloudstack.cs_physical_network:
    name: net01
    zone: zone01
    state: absent
```

## [Return Values](cs_physical_network_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **broadcast_domain_range**  string | broadcastdomainrange of the network [POD / ZONE].  **Returned:** success  **Sample:** `"ZONE"` |
| **domain**  string | Name of domain the network is in.  **Returned:** success  **Sample:** `"domain1"` |
| **id**  string | UUID of the network.  **Returned:** success  **Sample:** `"3f8f25cd-c498-443f-9058-438cfbcbff50"` |
| **isolation_method**  string | isolationmethod of the network [VLAN/VXLAN/GRE/L3].  **Returned:** success  **Sample:** `"VLAN"` |
| **name**  string | Name of the network.  **Returned:** success  **Sample:** `"net01"` |
| **network_speed**  string | networkspeed of the network [1G/10G].  **Returned:** success  **Sample:** `"1G"` |
| **nsps**  complex | list of enabled or disabled Network Service Providers  **Returned:** on enabling/disabling of Network Service Providers |
| **disabled**  list / elements=string | list of Network Service Providers that were disabled  **Returned:** on Network Service Provider disabling  **Sample:** `["internallbvm"]` |
| **enabled**  list / elements=string | list of Network Service Providers that were enabled  **Returned:** on Network Service Provider enabling  **Sample:** `["virtualrouter"]` |
| **state**  string | State of the network [Enabled/Disabled].  **Returned:** success  **Sample:** `"Enabled"` |
| **zone**  string | Name of zone the physical network is in.  **Returned:** success  **Sample:** `"ch-gva-2"` |

### Authors

- Netservers Ltd. (@netservers)
- Patryk Cichy (@PatTheSilent)

### Collection links

- [Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
- [Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
