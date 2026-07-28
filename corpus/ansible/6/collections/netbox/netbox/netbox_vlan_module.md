---
collection: ansible
version: "6"
title: "netbox.netbox.netbox_vlan module – Create, update or delete vlans within NetBox"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netbox/netbox/netbox_vlan_module.html
fetched_at: 2026-07-28T00:15:12+00:00
---
# netbox.netbox.netbox_vlan module – Create, update or delete vlans within NetBox

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
> see [Requirements](netbox_vlan_module.md#ansible-collections-netbox-netbox-netbox-vlan-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_vlan`.

New in netbox.netbox 0.1.0

- [Synopsis](netbox_vlan_module.md#synopsis)
- [Requirements](netbox_vlan_module.md#requirements)
- [Parameters](netbox_vlan_module.md#parameters)
- [Notes](netbox_vlan_module.md#notes)
- [Examples](netbox_vlan_module.md#examples)
- [Return Values](netbox_vlan_module.md#return-values)

## [Synopsis](netbox_vlan_module.md#id1)

- Creates, updates or removes vlans from NetBox

## [Requirements](netbox_vlan_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_vlan_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the vlan configuration |
| **custom_fields**  dictionary | must exist in NetBox |
| **description**  string | The description of the vlan |
| **name**  string / required | The name of the vlan |
| **site**  any | The site the VLAN will be associated to |
| **status**  any | The status of the vlan |
| **tags**  list / elements=any | Any tags that the vlan may need to be associated with |
| **tenant**  any | The tenant that the vlan will be assigned to |
| **vid**  integer | The VLAN ID |
| **vlan_group**  any | The VLAN group the VLAN will be associated to |
| **vlan_role**  any | Required if *state=present* and the vlan does not exist yet |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  Default: `true` |

## [Notes](netbox_vlan_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_vlan_module.md#id5)

```yaml+jinja
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create vlan within NetBox with only required information
      netbox_vlan:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test VLAN
          vid: 400
        state: present

    - name: Delete vlan within netbox
      netbox_vlan:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test VLAN
          vid: 400
        state: absent

    - name: Create vlan with all information
      netbox_vlan:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test VLAN
          vid: 400
          site: Test Site
          group: Test VLAN Group
          tenant: Test Tenant
          status: Deprecated
          vlan_role: Test VLAN Role
          description: Just a test
          tags:
            - Schnozzberry
        state: present
```

## [Return Values](netbox_vlan_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Message indicating failure or info about what has been achieved  Returned: always |
| **vlan**  dictionary | Serialized object as created or already existent within NetBox  Returned: success (when *state=present*) |

### Authors

- Mikhail Yohman (@FragmentedPacket)

### Collection links

[Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
[Repository (Sources)](https://github.com/netbox-community/ansible_modules)
