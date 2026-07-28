---
collection: ansible
version: "6"
title: "netbox.netbox.netbox_l2vpn module – Create, update or delete L2VPNs within NetBox"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netbox/netbox/netbox_l2vpn_module.html
fetched_at: 2026-07-28T00:14:52+00:00
---
# netbox.netbox.netbox_l2vpn module – Create, update or delete L2VPNs within NetBox

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
> see [Requirements](netbox_l2vpn_module.md#ansible-collections-netbox-netbox-netbox-l2vpn-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_l2vpn`.

New in netbox.netbox 3.9.0

- [Synopsis](netbox_l2vpn_module.md#synopsis)
- [Requirements](netbox_l2vpn_module.md#requirements)
- [Parameters](netbox_l2vpn_module.md#parameters)
- [Notes](netbox_l2vpn_module.md#notes)
- [Examples](netbox_l2vpn_module.md#examples)
- [Return Values](netbox_l2vpn_module.md#return-values)

## [Synopsis](netbox_l2vpn_module.md#id1)

- Creates, updates or removes L2VPNs from NetBox

## [Requirements](netbox_l2vpn_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_l2vpn_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the L2VPN configuration |
| **custom_fields**  dictionary | Must exist in NetBox |
| **description**  string | The description of the L2VPN |
| **export_targets**  list / elements=any | Route targets to export |
| **identifier**  integer | The identifier of the L2VPN |
| **import_targets**  list / elements=any | Route targets to import |
| **name**  string / required | The name of the L2VPN |
| **tags**  list / elements=any | Any tags that the L2VPN may need to be associated with |
| **tenant**  any | The tenant that the L2VPN will be assigned to |
| **type**  any / required | The type of L2VPN |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  Default: `true` |

## [Notes](netbox_l2vpn_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_l2vpn_module.md#id5)

```yaml+jinja
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create L2VPN within NetBox with only required information
      netbox_l2vpn:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test L2VPN
          type: vxlan
        state: present

    - name: Delete L2VPN within netbox
      netbox_vlan:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test L2VPN
          type: vxlan
        state: absent

    - name: Create L2VPN with all required information
      netbox_vlan:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test L2VPN
          type: vpls
          identifier: 43256
          import_targets:
            - "65000:1"
          export_targets:
            - "65000:2"
          tenant: Test Tenant
          description: Just a test
          tags:
            - Schnozzberry
        state: present
```

## [Return Values](netbox_l2vpn_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **l2vpn**  dictionary | Serialized object as created or already existent within NetBox  Returned: success (when *state=present*) |
| **msg**  string | Message indicating failure or info about what has been achieved  Returned: always |

### Authors

- Martin Rødvand (@rodvand)

### Collection links

[Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
[Repository (Sources)](https://github.com/netbox-community/ansible_modules)
