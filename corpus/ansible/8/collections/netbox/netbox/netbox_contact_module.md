---
collection: ansible
version: "8"
title: "netbox.netbox.netbox_contact module – Creates or removes contacts from NetBox"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netbox/netbox/netbox_contact_module.html
fetched_at: 2026-07-28T02:44:55+00:00
---
# netbox.netbox.netbox_contact module – Creates or removes contacts from NetBox

> **Note:**
>
> This module is part of the [netbox.netbox collection](https://galaxy.ansible.com/ui/repo/published/netbox/netbox/) (version 3.15.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netbox.netbox`.
> You need further requirements to be able to use this module,
> see [Requirements](netbox_contact_module.md#ansible-collections-netbox-netbox-netbox-contact-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_contact`.

New in netbox.netbox 3.5.0

- [Synopsis](netbox_contact_module.md#synopsis)
- [Requirements](netbox_contact_module.md#requirements)
- [Parameters](netbox_contact_module.md#parameters)
- [Notes](netbox_contact_module.md#notes)
- [Examples](netbox_contact_module.md#examples)
- [Return Values](netbox_contact_module.md#return-values)

## [Synopsis](netbox_contact_module.md#id1)

- Creates or removes contacts from NetBox

## [Requirements](netbox_contact_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_contact_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the contact configuration |
| **address**  string | The address of the contact |
| **comments**  string | Comments on the contact |
| **contact_group**  any | Group assignment for the contact |
| **custom_fields**  dictionary | must exist in NetBox |
| **description**  string  *added in netbox.netbox 3.10.0* | The description of the contact |
| **email**  string | The email of the contact |
| **link**  string  *added in netbox.netbox 3.7.0* | URL associated with the contact |
| **name**  string / required | Name of the contact to be created |
| **phone**  string | The phone number of the contact |
| **tags**  list / elements=any | Any tags that the contact may need to be associated with |
| **title**  string | The title of the contact |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  **Default:** `true` |

## [Notes](netbox_contact_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_contact_module.md#id5)

```yaml+jinja
- name: "Test NetBox module"
  connection: local
  hosts: localhost
  gather_facts: False
  tasks:
    - name: Create contact within NetBox with only required information
      netbox.netbox.netbox_contact:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Contact One
        state: present

    - name: Delete contact within netbox
      netbox.netbox.netbox_contact:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Contact One
        state: absent

    - name: Create contact with all parameters
      netbox.netbox.netbox_contact:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: contact ABC
          title: Mr Contact
          phone: 123456789
          email: contac@contact.com
          tags:
            - tagA
            - tagB
            - tagC
        state: present
```

## [Return Values](netbox_contact_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **contact**  dictionary | Serialized object as created or already existent within NetBox  **Returned:** on creation |
| **msg**  string | Message indicating failure or info about what has been achieved  **Returned:** always |

### Authors

- Martin Rødvand (@rodvand)

### Collection links

- [Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
- [Repository (Sources)](https://github.com/netbox-community/ansible_modules)
