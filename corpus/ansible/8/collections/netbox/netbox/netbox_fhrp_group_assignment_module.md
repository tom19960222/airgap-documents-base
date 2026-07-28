---
collection: ansible
version: "8"
title: "netbox.netbox.netbox_fhrp_group_assignment module – Create, update or delete FHRP group assignments within NetBox"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netbox/netbox/netbox_fhrp_group_assignment_module.html
fetched_at: 2026-07-28T02:45:05+00:00
---
# netbox.netbox.netbox_fhrp_group_assignment module – Create, update or delete FHRP group assignments within NetBox

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
> see [Requirements](netbox_fhrp_group_assignment_module.md#ansible-collections-netbox-netbox-netbox-fhrp-group-assignment-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_fhrp_group_assignment`.

- [Synopsis](netbox_fhrp_group_assignment_module.md#synopsis)
- [Requirements](netbox_fhrp_group_assignment_module.md#requirements)
- [Parameters](netbox_fhrp_group_assignment_module.md#parameters)
- [Notes](netbox_fhrp_group_assignment_module.md#notes)
- [See Also](netbox_fhrp_group_assignment_module.md#see-also)
- [Examples](netbox_fhrp_group_assignment_module.md#examples)
- [Return Values](netbox_fhrp_group_assignment_module.md#return-values)

## [Synopsis](netbox_fhrp_group_assignment_module.md#id1)

- Creates, updates or removes FHRP group assignments from NetBox

## [Requirements](netbox_fhrp_group_assignment_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_fhrp_group_assignment_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the FHRP group assignment configuration |
| **fhrp_group**  integer / required | FHRP Group ID |
| **interface_id**  integer / required | Interface ID |
| **interface_type**  string / required | Interface type  **Choices:**   - `"dcim.interface"` - `"virtualization.vminterface"` |
| **priority**  integer | Priority (0 .. 255) |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  **Default:** `true` |

## [Notes](netbox_fhrp_group_assignment_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [See Also](netbox_fhrp_group_assignment_module.md#id5)

> **See also:**
>
> [FHRP Group Model reference](https://docs.netbox.dev/en/stable/models/ipam/fhrpgroupassignment/)
> :   NetBox Documentation for FHRP Group Model.

## [Examples](netbox_fhrp_group_assignment_module.md#id6)

```yaml+jinja
- hosts: localhost
  connection: local
  module_defaults:
    group/netbox.netbox.netbox:
      netbox_url: "http://netbox.local"
      netbox_token: "thisIsMyToken"

  tasks:
    - name: "Create FHRP group assignment within netbox"
      netbox.netbox.netbox_fhrp_group_assignment:
        data:
          fhrp_group: 3
          interface_type: dcim.interface
          interface_id: 5
          priority: 1
        state: present

    - name: Delete FHRP group assignment within netbox
      netbox.netbox.netbox_fhrp_group_assignment:
        data:
          fhrp_group: 3
          interface_type: dcim.interface
          interface_id: 5
        state: absent
```

## [Return Values](netbox_fhrp_group_assignment_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **fhrp_group**  dictionary | Serialized object as created or already existent within NetBox  **Returned:** success (when *state=present*) |
| **msg**  string | Message indicating failure or info about what has been achieved  **Returned:** always |

### Authors

- Andrii Konts (@andrii-konts)

### Collection links

- [Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
- [Repository (Sources)](https://github.com/netbox-community/ansible_modules)
