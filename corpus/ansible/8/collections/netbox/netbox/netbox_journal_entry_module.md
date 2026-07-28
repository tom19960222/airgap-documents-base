---
collection: ansible
version: "8"
title: "netbox.netbox.netbox_journal_entry module – Creates a journal entry"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netbox/netbox/netbox_journal_entry_module.html
fetched_at: 2026-07-28T02:45:10+00:00
---
# netbox.netbox.netbox_journal_entry module – Creates a journal entry

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
> see [Requirements](netbox_journal_entry_module.md#ansible-collections-netbox-netbox-netbox-journal-entry-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_journal_entry`.

New in netbox.netbox 3.12.0

- [Synopsis](netbox_journal_entry_module.md#synopsis)
- [Requirements](netbox_journal_entry_module.md#requirements)
- [Parameters](netbox_journal_entry_module.md#parameters)
- [Notes](netbox_journal_entry_module.md#notes)
- [Examples](netbox_journal_entry_module.md#examples)
- [Return Values](netbox_journal_entry_module.md#return-values)

## [Synopsis](netbox_journal_entry_module.md#id1)

- Creates a journal entry in NetBox

## [Requirements](netbox_journal_entry_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_journal_entry_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the journal entry |
| **assigned_object_id**  integer / required | ID of the object to create the journal entry on |
| **assigned_object_type**  string / required | The object type of the model |
| **comments**  string / required | The comment associated with the journal entry |
| **created_by**  integer | The user ID of the user creating the journal entry. Omit to use the API token user |
| **custom_fields**  dictionary | Must exist in NetBox |
| **kind**  string | The kind of journal entry |
| **tags**  list / elements=any | Any tags that the journal entry may need to be associated with |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | Use `new` for adding a journal entry.  **Choices:**   - `"new"` ← (default) |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  **Default:** `true` |

## [Notes](netbox_journal_entry_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_journal_entry_module.md#id5)

```yaml+jinja
- name: "Test NetBox Module"
  hosts: localhost
  connection: local
  gather_facts: false
  module_defaults:
    group/netbox.netbox.netbox:
      netbox_url: MYURL
      netbox_token: MYTOKEN
  tasks:
    - name: Create an IP Address
      netbox.netbox.netbox_ip_address:
        data:
          address: 192.168.8.14/24
      register: ip

    - name: Create a journal entry
      netbox.netbox.netbox_journal_entry:
        data:
          assigned_object_type: ipam.ipaddress
          assigned_object_id: "{{ ip.ip_address.id }}"
          kind: success
          comments: |
            This is a journal entry
      when: ip.changed
```

## [Return Values](netbox_journal_entry_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **journal_entry**  dictionary | Serialized object as created or already existent within NetBox  **Returned:** on creation |
| **msg**  string | Message indicating failure or info about what has been achieved  **Returned:** always |

### Authors

- Martin Rødvand (@rodvand)

### Collection links

- [Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
- [Repository (Sources)](https://github.com/netbox-community/ansible_modules)
