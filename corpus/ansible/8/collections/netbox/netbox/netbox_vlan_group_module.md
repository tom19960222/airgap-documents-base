---
collection: ansible
version: "8"
title: "netbox.netbox.netbox_vlan_group module – Create, update or delete vlans groups within NetBox"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netbox/netbox/netbox_vlan_group_module.html
fetched_at: 2026-07-28T02:45:34+00:00
---
# netbox.netbox.netbox_vlan_group module – Create, update or delete vlans groups within NetBox

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
> see [Requirements](netbox_vlan_group_module.md#ansible-collections-netbox-netbox-netbox-vlan-group-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_vlan_group`.

New in netbox.netbox 0.1.0

- [Synopsis](netbox_vlan_group_module.md#synopsis)
- [Requirements](netbox_vlan_group_module.md#requirements)
- [Parameters](netbox_vlan_group_module.md#parameters)
- [Notes](netbox_vlan_group_module.md#notes)
- [Examples](netbox_vlan_group_module.md#examples)
- [Return Values](netbox_vlan_group_module.md#return-values)

## [Synopsis](netbox_vlan_group_module.md#id1)

- Creates, updates or removes vlans groups from NetBox

## [Requirements](netbox_vlan_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_vlan_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the vlan group configuration |
| **custom_fields**  dictionary  *added in netbox.netbox 3.1.0* | must exist in NetBox |
| **description**  string  *added in netbox.netbox 3.1.0* | Description for VLAN group |
| **max_vid**  integer  *added in netbox.netbox 3.7.0* | Highest permissible ID of a child VLAN |
| **min_vid**  integer  *added in netbox.netbox 3.7.0* | Lowest permissible ID of a child VLAN |
| **name**  string / required | The name of the vlan group |
| **scope**  any  *added in netbox.netbox 3.1.0* | Object related to scope type (NetBox 2.11+) |
| **scope_type**  string  *added in netbox.netbox 3.1.0* | Type of scope to be applied (NetBox 2.11+)  **Choices:**   - `"dcim.location"` - `"dcim.rack"` - `"dcim.region"` - `"dcim.site"` - `"dcim.sitegroup"` - `"virtualization.cluster"` - `"virtualization.clustergroup"` |
| **site**  any | The site the vlan will be assigned to (NetBox < 2.11)  Will be removed in version 5.0.0 |
| **slug**  string | The slugified version of the name or custom slug.  This is auto-generated following NetBox rules if not provided |
| **tags**  list / elements=any  *added in netbox.netbox 3.6.0* | The tags to add/update |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  **Default:** `true` |

## [Notes](netbox_vlan_group_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_vlan_group_module.md#id5)

```yaml+jinja
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create vlan group within NetBox with only required information - Pre 2.11
      netbox_vlan_group:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test vlan group
          site: Test Site
        state: present

    - name: Create vlan group within NetBox with only required information - Post 2.11
      netbox_vlan_group:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test vlan group
          scope_type: "dcim.site"
          scope: Test Site
        state: present

    - name: Delete vlan group within netbox
      netbox_vlan_group:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test vlan group
        state: absent
```

## [Return Values](netbox_vlan_group_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Message indicating failure or info about what has been achieved  **Returned:** always |
| **vlan_group**  dictionary | Serialized object as created or already existent within NetBox  **Returned:** success (when *state=present*) |

### Authors

- Mikhail Yohman (@FragmentedPacket)

### Collection links

- [Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
- [Repository (Sources)](https://github.com/netbox-community/ansible_modules)
