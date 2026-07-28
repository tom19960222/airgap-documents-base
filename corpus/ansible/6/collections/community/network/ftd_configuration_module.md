---
collection: ansible
version: "6"
title: "community.network.ftd_configuration module – Manages configuration on Cisco FTD devices over REST API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ftd_configuration_module.html
fetched_at: 2026-07-27T17:18:36+00:00
---
# community.network.ftd_configuration module – Manages configuration on Cisco FTD devices over REST API

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.ftd_configuration`.

- [Synopsis](ftd_configuration_module.md#synopsis)
- [Parameters](ftd_configuration_module.md#parameters)
- [Examples](ftd_configuration_module.md#examples)
- [Return Values](ftd_configuration_module.md#return-values)

## [Synopsis](ftd_configuration_module.md#id1)

- Manages configuration on Cisco FTD devices including creating, updating, removing configuration objects, scheduling and staring jobs, deploying pending changes, etc. All operations are performed over REST API.

## [Parameters](ftd_configuration_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **data**  dictionary | Key-value pairs that should be sent as body parameters in a REST API call |
| **filters**  dictionary | Key-value dict that represents equality filters. Every key is a property name and value is its desired value. If multiple filters are present, they are combined with logical operator AND. |
| **operation**  string / required | The name of the operation to execute. Commonly, the operation starts with ‘add’, ‘edit’, ‘get’, ‘upsert’ or ‘delete’ verbs, but can have an arbitrary name too. |
| **path_params**  dictionary | Key-value pairs that should be sent as path parameters in a REST API call. |
| **query_params**  dictionary | Key-value pairs that should be sent as query parameters in a REST API call. |
| **register_as**  string | Specifies Ansible fact name that is used to register received response from the FTD device. |

## [Examples](ftd_configuration_module.md#id3)

```yaml+jinja
- name: Create a network object
  community.network.ftd_configuration:
    operation: "addNetworkObject"
    data:
      name: "Ansible-network-host"
      description: "From Ansible with love"
      subType: "HOST"
      value: "192.168.2.0"
      dnsResolution: "IPV4_AND_IPV6"
      type: "networkobject"
      isSystemDefined: false
    register_as: "hostNetwork"

- name: Delete the network object
  community.network.ftd_configuration:
    operation: "deleteNetworkObject"
    path_params:
      objId: "{{ hostNetwork['id'] }}"
```

## [Return Values](ftd_configuration_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **response**  dictionary | HTTP response returned from the API call.  Returned: success |

### Authors

- Cisco Systems, Inc. (@annikulin)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
