---
collection: ansible
version: "6"
title: "netapp_eseries.santricity.netapp_e_storage_system module – NetApp E-Series Web Services Proxy manage storage arrays"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp_eseries/santricity/netapp_e_storage_system_module.html
fetched_at: 2026-07-28T00:14:25+00:00
---
# netapp_eseries.santricity.netapp_e_storage_system module – NetApp E-Series Web Services Proxy manage storage arrays

> **Note:**
>
> This module is part of the [netapp_eseries.santricity collection](https://galaxy.ansible.com/netapp_eseries/santricity) (version 1.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp_eseries.santricity`.
>
> To use it in a playbook, specify: `netapp_eseries.santricity.netapp_e_storage_system`.

New in netapp_eseries.santricity 2.2

- [Synopsis](netapp_e_storage_system_module.md#synopsis)
- [Parameters](netapp_e_storage_system_module.md#parameters)
- [Examples](netapp_e_storage_system_module.md#examples)
- [Return Values](netapp_e_storage_system_module.md#return-values)

## [Synopsis](netapp_e_storage_system_module.md#id1)

- Manage the arrays accessible via a NetApp Web Services Proxy for NetApp E-series storage arrays.

## [Parameters](netapp_e_storage_system_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity WebServices Proxy or embedded REST API. |
| **api_url**  string / required | The url to the SANtricity WebServices Proxy or embedded REST API. |
| **api_username**  string / required | The username to authenticate with the SANtricity WebServices Proxy or embedded REST API. |
| **array_password**  string | The management password of the array to manage, if set. |
| **array_status_timeout_sec**  integer | Array status timeout measured in seconds  Default: `60` |
| **array_wwn**  string | The WWN of the array to manage. Only necessary if in-band managing multiple arrays on the same agent host. Mutually exclusive of controller_addresses parameter. |
| **controller_addresses**  list / elements=string / required | The list addresses for the out-of-band management adapter or the agent host. Mutually exclusive of array_wwn parameter. |
| **enable_trace**  boolean | Enable trace logging for SYMbol calls to the storage system.  Choices:   - `false` ← (default) - `true` |
| **meta_tags**  list / elements=string | Optional meta tags to associate to this storage system |
| **ssid**  string / required | The ID of the array to manage. This value must be unique for each array. |
| **state**  string / required | Whether the specified array should be configured on the Web Services Proxy or not.  Choices:   - `"present"` - `"absent"` |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |

## [Examples](netapp_e_storage_system_module.md#id3)

```yaml+jinja
---
    - name:  Presence of storage system
      netapp_e_storage_system:
        ssid: "{{ item.key }}"
        state: present
        api_url: "{{ netapp_api_url }}"
        api_username: "{{ netapp_api_username }}"
        api_password: "{{ netapp_api_password }}"
        validate_certs: "{{ netapp_api_validate_certs }}"
        controller_addresses:
          - "{{ item.value.address1 }}"
          - "{{ item.value.address2 }}"
      with_dict: "{{ storage_systems }}"
      when: check_storage_system
```

## [Return Values](netapp_e_storage_system_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | State of request  Returned: always  Sample: `"Storage system removed."` |

### Authors

- Kevin Hulquest (@hulquest)

### Collection links

[Issue Tracker](https://github.com/netappeseries/santricity/issues)
[Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
