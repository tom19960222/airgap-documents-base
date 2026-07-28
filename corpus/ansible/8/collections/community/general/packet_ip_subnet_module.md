---
collection: ansible
version: "8"
title: "community.general.packet_ip_subnet module – Assign IP subnet to a bare metal server"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/packet_ip_subnet_module.html
fetched_at: 2026-07-28T01:48:49+00:00
---
# community.general.packet_ip_subnet module – Assign IP subnet to a bare metal server

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](packet_ip_subnet_module.md#ansible-collections-community-general-packet-ip-subnet-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.packet_ip_subnet`.

New in community.general 0.2.0

- [Synopsis](packet_ip_subnet_module.md#synopsis)
- [Requirements](packet_ip_subnet_module.md#requirements)
- [Parameters](packet_ip_subnet_module.md#parameters)
- [Attributes](packet_ip_subnet_module.md#attributes)
- [Examples](packet_ip_subnet_module.md#examples)
- [Return Values](packet_ip_subnet_module.md#return-values)

## [Synopsis](packet_ip_subnet_module.md#id1)

- Assign or unassign IPv4 or IPv6 subnets to or from a device in the Packet host.
- IPv4 subnets must come from already reserved block.
- IPv6 subnets must come from publicly routable /56 block from your project.
- See <https://support.packet.com/kb/articles/elastic-ips> for more info on IP block reservation.

Aliases: cloud.packet.packet_ip_subnet

## [Requirements](packet_ip_subnet_module.md#id2)

The below requirements are needed on the host that executes this module.

- packet-python >= 1.35
- python >= 2.6

## [Parameters](packet_ip_subnet_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_token**  string | Packet API token. You can also supply it in environment variable `PACKET_API_TOKEN`. |
| **cidr**  aliases: name  string / required | IPv4 or IPv6 subnet which you want to manage. It must come from a reserved block for your project in the Packet Host. |
| **device_count**  integer | The number of devices to retrieve from the project. The max allowed value is 1000.  See <https://www.packet.com/developers/api/#retrieve-all-devices-of-a-project> for more info.  **Default:** `100` |
| **device_id**  string | UUID of a device to/from which to assign/remove a subnet. |
| **hostname**  string | A hostname of a device to/from which to assign/remove a subnet. |
| **project_id**  string | UUID of a project of the device to/from which to assign/remove a subnet. |
| **state**  string | Desired state of the IP subnet on the specified device.  With `state=present`, you must specify either `hostname` or `device_id`. Subnet with given CIDR will then be assigned to the specified device.  With `state=absent`, you can specify either `hostname` or `device_id`. The subnet will be removed from specified devices.  If you leave both `hostname` and `device_id` empty, the subnet will be removed from any device it’s assigned to.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Attributes](packet_ip_subnet_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](packet_ip_subnet_module.md#id5)

```yaml+jinja
# All the examples assume that you have your Packet API token in env var PACKET_API_TOKEN.
# You can also pass it to the auth_token parameter of the module instead.

- name: Create 1 device and assign an arbitrary public IPv4 subnet to it
  hosts: localhost
  tasks:

  - packet_device:
      project_id: 89b497ee-5afc-420a-8fb5-56984898f4df
      hostnames: myserver
      operating_system: ubuntu_16_04
      plan: baremetal_0
      facility: sjc1
      state: active

# Pick an IPv4 address from a block allocated to your project.

  - community.general.packet_ip_subnet:
      project_id: 89b497ee-5afc-420a-8fb5-56984898f4df
      hostname: myserver
      cidr: "147.75.201.78/32"

# Release IP address 147.75.201.78

- name: Unassign IP address from any device in your project
  hosts: localhost
  tasks:
  - community.general.packet_ip_subnet:
      project_id: 89b497ee-5afc-420a-8fb5-56984898f4df
      cidr: "147.75.201.78/32"
      state: absent
```

## [Return Values](packet_ip_subnet_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | True if an IP address assignments were altered in any way (created or removed).  **Returned:** success  **Sample:** `true` |
| **device_id**  string | UUID of the device associated with the specified IP address.  **Returned:** success |
| **subnet**  dictionary | Dict with data about the handled IP subnet.  **Returned:** success  **Sample:** `{"address": "147.75.90.241", "address_family": 4, "assigned_to": {"href": "/devices/61f9aa5e-0530-47f5-97c2-113828e61ed0"}, "cidr": 31, "created_at": "2017-08-07T15:15:30Z", "enabled": true, "gateway": "147.75.90.240", "href": "/ips/31eda960-0a16-4c0f-b196-f3dc4928529f", "id": "1eda960-0a16-4c0f-b196-f3dc4928529f", "manageable": true, "management": true, "netmask": "255.255.255.254", "network": "147.75.90.240", "public": true}` |

### Authors

- Tomas Karasek (@t0mk)
- Nurfet Becirevic (@nurfet-becirevic)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
