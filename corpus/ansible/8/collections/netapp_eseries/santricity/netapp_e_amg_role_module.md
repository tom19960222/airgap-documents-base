---
collection: ansible
version: "8"
title: "netapp_eseries.santricity.netapp_e_amg_role module – NetApp E-Series update the role of a storage array within an Asynchronous Mirror Group (AMG)."
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp_eseries/santricity/netapp_e_amg_role_module.html
fetched_at: 2026-07-28T02:44:24+00:00
---
# netapp_eseries.santricity.netapp_e_amg_role module – NetApp E-Series update the role of a storage array within an Asynchronous Mirror Group (AMG).

> **Note:**
>
> This module is part of the [netapp_eseries.santricity collection](https://galaxy.ansible.com/ui/repo/published/netapp_eseries/santricity/) (version 1.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp_eseries.santricity`.
>
> To use it in a playbook, specify: `netapp_eseries.santricity.netapp_e_amg_role`.

New in netapp_eseries.santricity 2.2

- [Synopsis](netapp_e_amg_role_module.md#synopsis)
- [Parameters](netapp_e_amg_role_module.md#parameters)
- [Examples](netapp_e_amg_role_module.md#examples)
- [Return Values](netapp_e_amg_role_module.md#return-values)

## [Synopsis](netapp_e_amg_role_module.md#id1)

- Update a storage array to become the primary or secondary instance in an asynchronous mirror group

## [Parameters](netapp_e_amg_role_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity WebServices Proxy or embedded REST API. |
| **api_url**  string / required | The url to the SANtricity WebServices Proxy or embedded REST API. |
| **api_username**  string / required | The username to authenticate with the SANtricity WebServices Proxy or embedded REST API. |
| **force**  boolean | Whether to force the role reversal regardless of the online-state of the primary  **Choices:**   - `false` ← (default) - `true` |
| **name**  string / required | Name of the role |
| **noSync**  boolean | Whether to avoid synchronization prior to role reversal  **Choices:**   - `false` ← (default) - `true` |
| **role**  string / required | Whether the array should be the primary or secondary array for the AMG  **Choices:**   - `"primary"` - `"secondary"` |
| **ssid**  string / required | The ID of the primary storage array for the async mirror action |
| **validate_certs**  boolean | Should https certificates be validated?  **Choices:**   - `false` - `true` ← (default) |

## [Examples](netapp_e_amg_role_module.md#id3)

```yaml+jinja
- name: Update the role of a storage array
  netapp_e_amg_role:
    name: updating amg role
    role: primary
    ssid: "{{ ssid }}"
    api_url: "{{ netapp_api_url }}"
    api_username: "{{ netapp_api_username }}"
    api_password: "{{ netapp_api_password }}"
    validate_certs: "{{ netapp_api_validate_certs }}"
```

## [Return Values](netapp_e_amg_role_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Failure message  **Returned:** failure  **Sample:** `"No Async Mirror Group with the name."` |

### Authors

- Kevin Hulquest (@hulquest)

### Collection links

- [Issue Tracker](https://github.com/netappeseries/santricity/issues)
- [Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
