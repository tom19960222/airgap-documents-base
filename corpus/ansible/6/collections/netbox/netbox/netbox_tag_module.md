---
collection: ansible
version: "6"
title: "netbox.netbox.netbox_tag module – Creates or removes tags from NetBox"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netbox/netbox/netbox_tag_module.html
fetched_at: 2026-07-28T00:15:09+00:00
---
# netbox.netbox.netbox_tag module – Creates or removes tags from NetBox

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
> see [Requirements](netbox_tag_module.md#ansible-collections-netbox-netbox-netbox-tag-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_tag`.

New in netbox.netbox 1.2.0

- [Synopsis](netbox_tag_module.md#synopsis)
- [Requirements](netbox_tag_module.md#requirements)
- [Parameters](netbox_tag_module.md#parameters)
- [Notes](netbox_tag_module.md#notes)
- [Examples](netbox_tag_module.md#examples)
- [Return Values](netbox_tag_module.md#return-values)

## [Synopsis](netbox_tag_module.md#id1)

- Creates or removes tags from NetBox

## [Requirements](netbox_tag_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_tag_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the tag configuration |
| **color**  string | Tag color |
| **description**  string | Tag description |
| **name**  string / required | Tag name |
| **slug**  string | The slugified version of the name or custom slug.  This is auto-generated following NetBox rules if not provided |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  Default: `true` |

## [Notes](netbox_tag_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_tag_module.md#id5)

```yaml+jinja
- name: "Test tags creation/deletion"
  connection: local
  hosts: localhost
  gather_facts: False
  tasks:
    - name: Create tags
      netbox_tag:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: "{{ item.name }}"
          description: "{{ item.description }}"
      loop:
        - { name: mgmt, description: "management" }
        - { name: tun, description: "tunnel" }

    - name: Delete tags
      netbox_tag:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: "{{ item }}"
        state: absent
      loop:
        - mgmt
        - tun
```

## [Return Values](netbox_tag_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Message indicating failure or info about what has been achieved  Returned: always |
| **tags**  dictionary | Serialized object as created/existent/updated/deleted within NetBox  Returned: always |

### Authors

- Pavel Korovin (@pkorovin)

### Collection links

[Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
[Repository (Sources)](https://github.com/netbox-community/ansible_modules)
