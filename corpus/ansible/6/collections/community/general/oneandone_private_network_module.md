---
collection: ansible
version: "6"
title: "community.general.oneandone_private_network module – Configure 1&1 private networking"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/oneandone_private_network_module.html
fetched_at: 2026-07-27T17:11:20+00:00
---
# community.general.oneandone_private_network module – Configure 1&1 private networking

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](oneandone_private_network_module.md#ansible-collections-community-general-oneandone-private-network-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.oneandone_private_network`.

- [Synopsis](oneandone_private_network_module.md#synopsis)
- [Requirements](oneandone_private_network_module.md#requirements)
- [Parameters](oneandone_private_network_module.md#parameters)
- [Examples](oneandone_private_network_module.md#examples)
- [Return Values](oneandone_private_network_module.md#return-values)

## [Synopsis](oneandone_private_network_module.md#id1)

- Create, remove, reconfigure, update a private network. This module has a dependency on 1and1 >= 1.0

## [Requirements](oneandone_private_network_module.md#id2)

The below requirements are needed on the host that executes this module.

- 1and1
- python >= 2.6

## [Parameters](oneandone_private_network_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **add_members**  list / elements=string | List of server identifiers (name or id) to be added to the private network.  Default: `[]` |
| **api_url**  string | Custom API URL. Overrides the ONEANDONE_API_URL environment variable. |
| **auth_token**  string | Authenticating API token provided by 1&1. |
| **datacenter**  string | The identifier of the datacenter where the private network will be created  Choices:   - `"US"` - `"ES"` - `"DE"` - `"GB"` |
| **description**  string | Set a description for the network. |
| **name**  string | Private network name used with present state. Used as identifier (id or name) when used with absent state. |
| **network_address**  string | Set a private network space, i.e. 192.168.1.0 |
| **private_network**  string | The identifier (id or name) of the network used with update state. |
| **remove_members**  list / elements=string | List of server identifiers (name or id) to be removed from the private network.  Default: `[]` |
| **state**  string | Define a network’s state to create, remove, or update.  Choices:   - `"present"` ← (default) - `"absent"` - `"update"` |
| **subnet_mask**  string | Set the netmask for the private network, i.e. 255.255.255.0 |
| **wait**  boolean | wait for the instance to be in state ‘running’ before returning  Choices:   - `false` - `true` ← (default) |
| **wait_interval**  integer | Defines the number of seconds to wait when using the _wait_for methods  Default: `5` |
| **wait_timeout**  integer | how long before wait gives up, in seconds  Default: `600` |

## [Examples](oneandone_private_network_module.md#id4)

```yaml+jinja
- name: Create a private network
  community.general.oneandone_private_network:
    auth_token: oneandone_private_api_key
    name: backup_network
    description: Testing creation of a private network with ansible
    network_address: 70.35.193.100
    subnet_mask: 255.0.0.0
    datacenter: US

- name: Destroy a private network
  community.general.oneandone_private_network:
    auth_token: oneandone_private_api_key
    state: absent
    name: backup_network

- name: Modify the private network
  community.general.oneandone_private_network:
    auth_token: oneandone_private_api_key
    state: update
    private_network: backup_network
    network_address: 192.168.2.0
    subnet_mask: 255.255.255.0

- name: Add members to the private network
  community.general.oneandone_private_network:
    auth_token: oneandone_private_api_key
    state: update
    private_network: backup_network
    add_members:
     - server identifier (id or name)

- name: Remove members from the private network
  community.general.oneandone_private_network:
    auth_token: oneandone_private_api_key
    state: update
    private_network: backup_network
    remove_members:
     - server identifier (id or name)
```

## [Return Values](oneandone_private_network_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **private_network**  dictionary | Information about the private network.  Returned: always  Sample: `{"id": "55726DEDA20C99CF6F2AF8F18CAC9963", "name": "backup_network"}` |

### Authors

- Amel Ajdinovic (@aajdinov)
- Ethan Devenport (@edevenport)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
