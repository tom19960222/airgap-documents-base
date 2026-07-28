---
collection: ansible
version: "6"
title: "community.general.infinity module – Manage Infinity IPAM using Rest API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/infinity_module.html
fetched_at: 2026-07-27T17:09:43+00:00
---
# community.general.infinity module – Manage Infinity IPAM using Rest API

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.infinity`.

- [Synopsis](infinity_module.md#synopsis)
- [Parameters](infinity_module.md#parameters)
- [Examples](infinity_module.md#examples)
- [Return Values](infinity_module.md#return-values)

## [Synopsis](infinity_module.md#id1)

- Manage Infinity IPAM using REST API.

## [Parameters](infinity_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **action**  string / required | Action to perform  Choices:   - `"add_network"` - `"delete_network"` - `"get_network"` - `"get_network_id"` - `"release_ip"` - `"release_network"` - `"reserve_network"` - `"reserve_next_available_ip"` |
| **ip_address**  string | IP Address for a reservation or a release. |
| **network_address**  string | Network address with CIDR format (e.g., 192.168.310.0). |
| **network_family**  string | Network family defined by Infinity, e.g. IPv4, IPv6 and Dual stack  Choices:   - `"4"` ← (default) - `"6"` - `"dual"` |
| **network_id**  string | Network ID. |
| **network_location**  integer | The parent network id for a given network.  Default: `-1` |
| **network_name**  string | The name of a network. |
| **network_size**  string | Network bitmask (e.g. 255.255.255.220) or CIDR format (e.g., /26). |
| **network_type**  string | Network type defined by Infinity  Choices:   - `"lan"` ← (default) - `"shared_lan"` - `"supernet"` |
| **password**  string / required | Infinity password. |
| **server_ip**  string / required | Infinity server_ip with IP address. |
| **username**  string / required | Username to access Infinity.  The user must have REST API privileges. |

## [Examples](infinity_module.md#id3)

```yaml+jinja
---
- hosts: localhost
  connection: local
  strategy: debug
  tasks:
    - name: Reserve network into Infinity IPAM
      community.general.infinity:
        server_ip: 80.75.107.12
        username: username
        password: password
        action: reserve_network
        network_name: reserve_new_ansible_network
        network_family: 4
        network_type: lan
        network_id: 1201
        network_size: /28
      register: infinity
```

## [Return Values](infinity_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ip_info**  string | when reserve next available ip address from a network, the ip address info ) is returned.  Returned: success  Sample: `"{\"address\": \"192.168.10.3\", \"hostname\": \"\", \"FQDN\": \"\", \"domainname\": \"\", \"id\": 3229}"` |
| **network_id**  string | id for a given network  Returned: success  Sample: `"1501"` |
| **network_info**  string | when reserving a LAN network from a Infinity supernet by providing network_size, the information about the reserved network is returned.  Returned: success  Sample: `"{'description': None, 'network_address': '192.168.10.32/28', 'network_family': '4', 'network_id': 3102, 'network_location': '3085', 'network_name': \"'reserve_new_ansible_network'\", 'network_size': None, 'network_type': 'lan', 'ranges': {'first_ip': None, 'id': 0, 'last_ip': None, 'name': None, 'type': None}}"` |

### Authors

- Meirong Liu (@MeganLiu)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
