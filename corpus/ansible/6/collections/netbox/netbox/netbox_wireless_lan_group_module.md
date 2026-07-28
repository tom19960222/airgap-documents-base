---
collection: ansible
version: "6"
title: "netbox.netbox.netbox_wireless_lan_group module – Creates or removes Wireless LAN Groups from NetBox"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netbox/netbox/netbox_wireless_lan_group_module.html
fetched_at: 2026-07-28T00:15:17+00:00
---
# netbox.netbox.netbox_wireless_lan_group module – Creates or removes Wireless LAN Groups from NetBox

> **Note:**
>
> This module is part of the [netbox.netbox collection](https://galaxy.ansible.com/netbox/netbox) (version 3.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netbox.netbox`.
> You need further requirements to be able to use this module,
> see [Requirements](netbox_wireless_lan_group_module.md#ansible-collections-netbox-netbox-netbox-wireless-lan-group-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_wireless_lan_group`.

New in netbox.netbox 3.5.0

- [Synopsis](netbox_wireless_lan_group_module.md#synopsis)
- [Requirements](netbox_wireless_lan_group_module.md#requirements)
- [Parameters](netbox_wireless_lan_group_module.md#parameters)
- [Notes](netbox_wireless_lan_group_module.md#notes)
- [Examples](netbox_wireless_lan_group_module.md#examples)
- [Return Values](netbox_wireless_lan_group_module.md#return-values)

## [Synopsis](netbox_wireless_lan_group_module.md#id1)

- Creates or removes Wireless LAN Groups from NetBox

## [Requirements](netbox_wireless_lan_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_wireless_lan_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the contact configuration |
| **custom_fields**  dictionary | must exist in NetBox |
| **description**  string | Description of the Wireless LAN Group |
| **name**  string / required | Name of the Wireless LAN Group to be created |
| **parent_wireless_lan_group**  any | The parent Wireless LAN group |
| **slug**  string | The slug of the Wireless LAN Group |
| **tags**  list / elements=any | Any tags that the Wireless LAN Group may need to be associated with |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  Default: `true` |

## [Notes](netbox_wireless_lan_group_module.md#id4)

> **Note:**
>
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_wireless_lan_group_module.md#id5)

```yaml+jinja
- name: "Test NetBox module"
  connection: local
  hosts: localhost
  gather_facts: False
  tasks:
    - name: Create Wireless LAN Group within NetBox with only required information
      netbox_wireless_lan_group:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Wireless LAN Group One
        state: present

    - name: Delete Wireless LAN within netbox
      netbox_wireless_lan_group:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Wireless LAN Group One
        state: absent

    - name: Create Wireless LAN Group with all parameters
      netbox_wireless_lan_group:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Wireless LAN Group One
          description: Wireless LAN Group description
          tags:
            - tagA
            - tagB
            - tagC
        state: present
```

## [Return Values](netbox_wireless_lan_group_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Message indicating failure or info about what has been achieved  Returned: always |
| **wireless_lan_group**  dictionary | Serialized object as created or already existent within NetBox  Returned: on creation |

### Authors

- Martin Rødvand (@rodvand)

### Collection links

[Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
[Repository (Sources)](https://github.com/netbox-community/ansible_modules)
