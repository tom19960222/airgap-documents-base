---
collection: ansible
version: "8"
title: "ngine_io.cloudstack.cs_instance_nic_secondaryip module – Manages secondary IPs of an instance on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ngine_io/cloudstack/cs_instance_nic_secondaryip_module.html
fetched_at: 2026-07-28T02:45:51+00:00
---
# ngine_io.cloudstack.cs_instance_nic_secondaryip module – Manages secondary IPs of an instance on Apache CloudStack based clouds.

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
> see [Requirements](cs_instance_nic_secondaryip_module.md#ansible-collections-ngine-io-cloudstack-cs-instance-nic-secondaryip-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_instance_nic_secondaryip`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_instance_nic_secondaryip_module.md#synopsis)
- [Requirements](cs_instance_nic_secondaryip_module.md#requirements)
- [Parameters](cs_instance_nic_secondaryip_module.md#parameters)
- [Notes](cs_instance_nic_secondaryip_module.md#notes)
- [Examples](cs_instance_nic_secondaryip_module.md#examples)
- [Return Values](cs_instance_nic_secondaryip_module.md#return-values)

## [Synopsis](cs_instance_nic_secondaryip_module.md#id1)

- Add and remove secondary IPs to and from a NIC of an instance.

## [Requirements](cs_instance_nic_secondaryip_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_instance_nic_secondaryip_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string | Account the instance is related to. |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  **Choices:**   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  **Default:** `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **domain**  string | Domain the instance is related to. |
| **network**  string | Name of the network.  Required to find the NIC if instance has multiple networks assigned. |
| **poll_async**  boolean | Poll async jobs until job has finished.  **Choices:**   - `false` - `true` ← (default) |
| **project**  string | Name of the project the instance is deployed in. |
| **state**  string | State of the ipaddress.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **vm**  aliases: name  string / required | Name of instance. |
| **vm_guest_ip**  aliases: secondary_ip  string | Secondary IP address to be added to the instance nic.  If not set, the API always returns a new IP address and idempotency is not given. |
| **vpc**  string | Name of the VPC the *vm* is related to. |
| **zone**  string / required | Name of the zone in which the instance is deployed in. |

## [Notes](cs_instance_nic_secondaryip_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_instance_nic_secondaryip_module.md#id5)

```yaml+jinja
- name: Assign a specific IP to the default NIC of the VM
  ngine_io.cloudstack.cs_instance_nic_secondaryip:
    vm: customer_xy
    zone: zone01
    vm_guest_ip: 10.10.10.10

# Note: If vm_guest_ip is not set, you will get a new IP address on every run.
- name: Assign an IP to the default NIC of the VM
  ngine_io.cloudstack.cs_instance_nic_secondaryip:
    vm: customer_xy
    zone: zone01

- name: Remove a specific IP from the default NIC
  ngine_io.cloudstack.cs_instance_nic_secondaryip:
    vm: customer_xy
    zone: zone01
    vm_guest_ip: 10.10.10.10
    state: absent
```

## [Return Values](cs_instance_nic_secondaryip_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **account**  string | Account the VM is related to.  **Returned:** success  **Sample:** `"example account"` |
| **domain**  string | Domain the VM is related to.  **Returned:** success  **Sample:** `"example domain"` |
| **id**  string | UUID of the NIC.  **Returned:** success  **Sample:** `"87b1e0ce-4e01-11e4-bb66-0050569e64b8"` |
| **ip_address**  string | Primary IP of the NIC.  **Returned:** success  **Sample:** `"10.10.10.10"` |
| **mac_address**  string | MAC address of the NIC.  **Returned:** success  **Sample:** `"02:00:33:31:00:e4"` |
| **netmask**  string | Netmask of the NIC.  **Returned:** success  **Sample:** `"255.255.255.0"` |
| **network**  string | Name of the network if not default.  **Returned:** success  **Sample:** `"sync network"` |
| **project**  string | Name of project the VM is related to.  **Returned:** success  **Sample:** `"Production"` |
| **vm**  string | Name of the VM.  **Returned:** success  **Sample:** `"web-01"` |
| **vm_guest_ip**  string | Secondary IP of the NIC.  **Returned:** success  **Sample:** `"10.10.10.10"` |

### Authors

- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
- [Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
