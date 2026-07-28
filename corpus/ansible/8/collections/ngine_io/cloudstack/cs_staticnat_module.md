---
collection: ansible
version: "8"
title: "ngine_io.cloudstack.cs_staticnat module – Manages static NATs on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ngine_io/cloudstack/cs_staticnat_module.html
fetched_at: 2026-07-28T02:46:26+00:00
---
# ngine_io.cloudstack.cs_staticnat module – Manages static NATs on Apache CloudStack based clouds.

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
> see [Requirements](cs_staticnat_module.md#ansible-collections-ngine-io-cloudstack-cs-staticnat-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_staticnat`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_staticnat_module.md#synopsis)
- [Requirements](cs_staticnat_module.md#requirements)
- [Parameters](cs_staticnat_module.md#parameters)
- [Notes](cs_staticnat_module.md#notes)
- [Examples](cs_staticnat_module.md#examples)
- [Return Values](cs_staticnat_module.md#return-values)

## [Synopsis](cs_staticnat_module.md#id1)

- Create, update and remove static NATs.

## [Requirements](cs_staticnat_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_staticnat_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string | Account the static NAT is related to. |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  **Choices:**   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  **Default:** `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **domain**  string | Domain the static NAT is related to. |
| **ip_address**  string / required | Public IP address the static NAT is assigned to. |
| **network**  string | Network the IP address is related to. |
| **poll_async**  boolean | Poll async jobs until job has finished.  **Choices:**   - `false` - `true` ← (default) |
| **project**  string | Name of the project the static NAT is related to. |
| **state**  string | State of the static NAT.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **vm**  string | Name of virtual machine which we make the static NAT for.  Required if *state=present*. |
| **vm_guest_ip**  string | VM guest NIC secondary IP address for the static NAT. |
| **vpc**  string | VPC the network related to. |
| **zone**  string / required | Name of the zone in which the virtual machine is in. |

## [Notes](cs_staticnat_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_staticnat_module.md#id5)

```yaml+jinja
- name: Create a static NAT for IP 1.2.3.4 to web01
  ngine_io.cloudstack.cs_staticnat:
    ip_address: 1.2.3.4
    zone: zone01
    vm: web01

- name: Remove a static NAT
  ngine_io.cloudstack.cs_staticnat:
    ip_address: 1.2.3.4
    zone: zone01
    state: absent
```

## [Return Values](cs_staticnat_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **account**  string | Account the static NAT is related to.  **Returned:** success  **Sample:** `"example account"` |
| **domain**  string | Domain the static NAT is related to.  **Returned:** success  **Sample:** `"example domain"` |
| **id**  string | UUID of the ip_address.  **Returned:** success  **Sample:** `"a6f7a5fc-43f8-11e5-a151-feff819cdc9f"` |
| **ip_address**  string | Public IP address.  **Returned:** success  **Sample:** `"1.2.3.4"` |
| **project**  string | Name of project the static NAT is related to.  **Returned:** success  **Sample:** `"Production"` |
| **vm_display_name**  string | Display name of the virtual machine.  **Returned:** success  **Sample:** `"web-01"` |
| **vm_guest_ip**  string | IP of the virtual machine.  **Returned:** success  **Sample:** `"10.101.65.152"` |
| **vm_name**  string | Name of the virtual machine.  **Returned:** success  **Sample:** `"web-01"` |
| **zone**  string | Name of zone the static NAT is related to.  **Returned:** success  **Sample:** `"ch-gva-2"` |

### Authors

- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
- [Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
