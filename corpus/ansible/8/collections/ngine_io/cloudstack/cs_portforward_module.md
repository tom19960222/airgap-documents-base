---
collection: ansible
version: "8"
title: "ngine_io.cloudstack.cs_portforward module – Manages port forwarding rules on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ngine_io/cloudstack/cs_portforward_module.html
fetched_at: 2026-07-28T02:46:13+00:00
---
# ngine_io.cloudstack.cs_portforward module – Manages port forwarding rules on Apache CloudStack based clouds.

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
> see [Requirements](cs_portforward_module.md#ansible-collections-ngine-io-cloudstack-cs-portforward-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_portforward`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_portforward_module.md#synopsis)
- [Requirements](cs_portforward_module.md#requirements)
- [Parameters](cs_portforward_module.md#parameters)
- [Notes](cs_portforward_module.md#notes)
- [Examples](cs_portforward_module.md#examples)
- [Return Values](cs_portforward_module.md#return-values)

## [Synopsis](cs_portforward_module.md#id1)

- Create, update and remove port forwarding rules.

## [Requirements](cs_portforward_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_portforward_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string | Account the *vm* is related to. |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  **Choices:**   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  **Default:** `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **domain**  string | Domain the *vm* is related to. |
| **ip_address**  string / required | Public IP address the rule is assigned to. |
| **network**  string | Name of the network. Required when forwarding ports in a VPC. |
| **open_firewall**  boolean | Whether the firewall rule for public port should be created, while creating the new rule.  Not supported when forwarding ports in a VPC.  Use [ngine_io.cloudstack.cs_firewall](cs_firewall_module.md#ansible-collections-ngine-io-cloudstack-cs-firewall-module) for managing firewall rules.  **Choices:**   - `false` ← (default) - `true` |
| **poll_async**  boolean | Poll async jobs until job has finished.  **Choices:**   - `false` - `true` ← (default) |
| **private_end_port**  integer | End private port for this rule.  If not specified equal *private_port*. |
| **private_port**  integer / required | Start private port for this rule. |
| **project**  string | Name of the project the *vm* is located in. |
| **protocol**  string | Protocol of the port forwarding rule.  **Choices:**   - `"tcp"` ← (default) - `"udp"` |
| **public_end_port**  integer | End public port for this rule.  If not specified equal *public_port*. |
| **public_port**  integer / required | Start public port for this rule. |
| **state**  string | State of the port forwarding rule.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: tag  list / elements=dictionary | List of tags. Tags are a list of dictionaries having keys *key* and *value*.  To delete all tags, set a empty list e.g. *tags: []*. |
| **vm**  string | Name of virtual machine which we make the port forwarding rule for.  Required if *state=present*. |
| **vm_guest_ip**  string | VM guest NIC secondary IP address for the port forwarding rule. |
| **vpc**  string | Name of the VPC. |
| **zone**  string / required | Name of the zone in which the virtual machine is in. |

## [Notes](cs_portforward_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_portforward_module.md#id5)

```yaml+jinja
- name: 1.2.3.4:80 -> web01:8080
  ngine_io.cloudstack.cs_portforward:
    ip_address: 1.2.3.4
    zone: zone01
    vm: web01
    public_port: 80
    private_port: 8080

- name: forward SSH and open firewall
  ngine_io.cloudstack.cs_portforward:
    ip_address: '{{ public_ip }}'
    zone: zone01
    vm: '{{ inventory_hostname }}'
    public_port: '{{ ansible_ssh_port }}'
    private_port: 22
    open_firewall: true

- name: forward DNS traffic, but do not open firewall
  ngine_io.cloudstack.cs_portforward:
    ip_address: 1.2.3.4
    zone: zone01
    vm: '{{ inventory_hostname }}'
    public_port: 53
    private_port: 53
    protocol: udp

- name: remove ssh port forwarding
  ngine_io.cloudstack.cs_portforward:
    ip_address: 1.2.3.4
    zone: zone01
    public_port: 22
    private_port: 22
    state: absent

- name: forward SSH in backend tier of VPC
  ngine_io.cloudstack.cs_portforward:
    ip_address: '{{ public_ip }}'
    zone: zone01
    vm: '{{ inventory_hostname }}'
    public_port: '{{ ansible_ssh_port }}'
    private_port: 22
    vpc: myVPC
    network: backend
```

## [Return Values](cs_portforward_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | UUID of the public IP address.  **Returned:** success  **Sample:** `"a6f7a5fc-43f8-11e5-a151-feff819cdc9f"` |
| **ip_address**  string | Public IP address.  **Returned:** success  **Sample:** `"1.2.3.4"` |
| **network**  string | Name of the network.  **Returned:** success  **Sample:** `"dmz"` |
| **private_end_port**  integer | End port on the virtual machine’s IP address.  **Returned:** success  **Sample:** `80` |
| **private_port**  integer | Start port on the virtual machine’s IP address.  **Returned:** success  **Sample:** `80` |
| **protocol**  string | Protocol.  **Returned:** success  **Sample:** `"tcp"` |
| **public_end_port**  integer | End port on the public IP address.  **Returned:** success  **Sample:** `80` |
| **public_port**  integer | Start port on the public IP address.  **Returned:** success  **Sample:** `80` |
| **tags**  list / elements=string | Tags related to the port forwarding.  **Returned:** success  **Sample:** `[]` |
| **vm_display_name**  string | Display name of the virtual machine.  **Returned:** success  **Sample:** `"web-01"` |
| **vm_guest_ip**  string | IP of the virtual machine.  **Returned:** success  **Sample:** `"10.101.65.152"` |
| **vm_name**  string | Name of the virtual machine.  **Returned:** success  **Sample:** `"web-01"` |
| **vpc**  string | Name of the VPC.  **Returned:** success  **Sample:** `"my_vpc"` |

### Authors

- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
- [Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
