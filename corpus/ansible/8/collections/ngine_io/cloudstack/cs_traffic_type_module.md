---
collection: ansible
version: "8"
title: "ngine_io.cloudstack.cs_traffic_type module – Manages traffic types on CloudStack Physical Networks"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ngine_io/cloudstack/cs_traffic_type_module.html
fetched_at: 2026-07-28T02:46:31+00:00
---
# ngine_io.cloudstack.cs_traffic_type module – Manages traffic types on CloudStack Physical Networks

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
> see [Requirements](cs_traffic_type_module.md#ansible-collections-ngine-io-cloudstack-cs-traffic-type-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_traffic_type`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_traffic_type_module.md#synopsis)
- [Requirements](cs_traffic_type_module.md#requirements)
- [Parameters](cs_traffic_type_module.md#parameters)
- [Notes](cs_traffic_type_module.md#notes)
- [Examples](cs_traffic_type_module.md#examples)
- [Return Values](cs_traffic_type_module.md#return-values)

## [Synopsis](cs_traffic_type_module.md#id1)

- Add, remove, update Traffic Types associated with CloudStack Physical Networks.

## [Requirements](cs_traffic_type_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_traffic_type_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  **Choices:**   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  **Default:** `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **hyperv_networklabel**  string | The network name label of the physical device dedicated to this traffic on a HyperV host. |
| **isolation_method**  string | Use if the physical network has multiple isolation types and traffic type is public.  **Choices:**   - `"vlan"` - `"vxlan"` |
| **kvm_networklabel**  string | The network name label of the physical device dedicated to this traffic on a KVM host. |
| **ovm3_networklabel**  string | The network name of the physical device dedicated to this traffic on an OVM3 host. |
| **physical_network**  string / required | the name of the Physical Network |
| **poll_async**  boolean | Poll async jobs until job has finished.  **Choices:**   - `false` - `true` ← (default) |
| **state**  string | State of the traffic type  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **traffic_type**  string / required | the trafficType to be added to the physical network.  **Choices:**   - `"Management"` - `"Guest"` - `"Public"` - `"Storage"` |
| **vlan**  string | The VLAN id to be used for Management traffic by VMware host. |
| **vmware_networklabel**  string | The network name label of the physical device dedicated to this traffic on a VMware host. |
| **xen_networklabel**  string | The network name label of the physical device dedicated to this traffic on a XenServer host. |
| **zone**  string / required | Name of the zone with the physical network. |

## [Notes](cs_traffic_type_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_traffic_type_module.md#id5)

```yaml+jinja
- name: add a traffic type
  ngine_io.cloudstack.cs_traffic_type:
    physical_network: public-network
    traffic_type: Guest
    zone: test-zone

- name: update traffic type
  ngine_io.cloudstack.cs_traffic_type:
    physical_network: public-network
    traffic_type: Guest
    kvm_networklabel: cloudbr0
    zone: test-zone

- name: remove traffic type
  ngine_io.cloudstack.cs_traffic_type:
    physical_network: public-network
    traffic_type: Public
    state: absent
    zone: test-zone
```

## [Return Values](cs_traffic_type_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hyperv_networklabel**  string | The network name label of the physical device dedicated to this traffic on a HyperV host  **Returned:** success  **Sample:** `"HyperV Internal Switch"` |
| **id**  string | ID of the network provider  **Returned:** success  **Sample:** `"659c1840-9374-440d-a412-55ca360c9d3c"` |
| **kvm_networklabel**  string | The network name label of the physical device dedicated to this traffic on a KVM host  **Returned:** success  **Sample:** `"cloudbr0"` |
| **ovm3_networklabel**  string | The network name of the physical device dedicated to this traffic on an OVM3 host  **Returned:** success  **Sample:** `"cloudbr0"` |
| **physical_network**  string | the physical network this belongs to  **Returned:** success  **Sample:** `"28ed70b7-9a1f-41bf-94c3-53a9f22da8b6"` |
| **traffic_type**  string | the trafficType that was added to the physical network  **Returned:** success  **Sample:** `"Public"` |
| **vmware_networklabel**  string | The network name label of the physical device dedicated to this traffic on a VMware host  **Returned:** success  **Sample:** `"Management Network"` |
| **xen_networklabel**  string | The network name label of the physical device dedicated to this traffic on a XenServer host  **Returned:** success  **Sample:** `"xenbr0"` |
| **zone**  string | Name of zone the physical network is in.  **Returned:** success  **Sample:** `"ch-gva-2"` |

### Authors

- Patryk Cichy (@PatTheSilent)

### Collection links

- [Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
- [Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
