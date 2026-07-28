---
collection: ansible
version: "8"
title: "netbox.netbox.netbox_prefix module – Creates or removes prefixes from NetBox"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netbox/netbox/netbox_prefix_module.html
fetched_at: 2026-07-28T02:45:19+00:00
---
# netbox.netbox.netbox_prefix module – Creates or removes prefixes from NetBox

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
> see [Requirements](netbox_prefix_module.md#ansible-collections-netbox-netbox-netbox-prefix-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_prefix`.

New in netbox.netbox 0.1.0

- [Synopsis](netbox_prefix_module.md#synopsis)
- [Requirements](netbox_prefix_module.md#requirements)
- [Parameters](netbox_prefix_module.md#parameters)
- [Notes](netbox_prefix_module.md#notes)
- [Examples](netbox_prefix_module.md#examples)
- [Return Values](netbox_prefix_module.md#return-values)

## [Synopsis](netbox_prefix_module.md#id1)

- Creates or removes prefixes from NetBox

## [Requirements](netbox_prefix_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_prefix_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the prefix configuration |
| **comments**  string  *added in netbox.netbox 3.10.0* | Comments that may include additional information in regards to the prefix |
| **custom_fields**  dictionary | Must exist in NetBox and in key/value format |
| **description**  string | The description of the prefix |
| **family**  integer | Specifies which address family the prefix prefix belongs to |
| **is_pool**  boolean | All IP Addresses within this prefix are considered usable  **Choices:**   - `false` - `true` |
| **mark_utilized**  boolean  *added in netbox.netbox 3.8.0* | Treat as 100% utilized  **Choices:**   - `false` - `true` |
| **parent**  any | Required if state is `present` and first_available is `yes`. Will get a new available prefix in this parent prefix. |
| **prefix**  any | Required if state is `present` and first_available is False. Will allocate or free this prefix. |
| **prefix_length**  integer | Required ONLY if state is `present` and first_available is `yes`.  Will get a new available prefix of the given prefix_length in this parent prefix. |
| **prefix_role**  any | The role of the prefix |
| **site**  any | Site that prefix is associated with |
| **status**  any | The status of the prefix |
| **tags**  list / elements=any | Any tags that the prefix may need to be associated with |
| **tenant**  any | The tenant that the prefix will be assigned to |
| **vlan**  any | The VLAN the prefix will be assigned to |
| **vrf**  any | VRF that prefix is associated with |
| **first_available**  boolean | If `yes` and state `present`, if an parent is given, it will get the first available prefix of the given prefix_length inside the given parent (and vrf, if given). Unused with state `absent`.  **Choices:**   - `false` ← (default) - `true` |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  **Default:** `true` |

## [Notes](netbox_prefix_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_prefix_module.md#id5)

```yaml+jinja
- name: "Test NetBox prefix module"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create prefix within NetBox with only required information
      netbox.netbox.netbox_prefix:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          prefix: 10.156.0.0/19
        state: present

    - name: Delete prefix within netbox
      netbox.netbox.netbox_prefix:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          prefix: 10.156.0.0/19
        state: absent

    - name: Create prefix with several specified options
      netbox.netbox.netbox_prefix:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          family: 4
          prefix: 10.156.32.0/19
          site: Test Site
          vrf: Test VRF
          tenant: Test Tenant
          vlan:
            name: Test VLAN
            site: Test Site
            tenant: Test Tenant
            vlan_group: Test Vlan Group
          status: Reserved
          prefix_role: Network of care
          description: Test description
          is_pool: true
          tags:
            - Schnozzberry
        state: present

    - name: Get a new /24 inside 10.156.0.0/19 within NetBox - Parent doesn't exist
      netbox.netbox.netbox_prefix:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          parent: 10.156.0.0/19
          prefix_length: 24
        state: present
        first_available: yes

    - name: Create prefix within NetBox with only required information
      netbox.netbox.netbox_prefix:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          prefix: 10.156.0.0/19
        state: present

    - name: Get a new /24 inside 10.156.0.0/19 within NetBox
      netbox.netbox.netbox_prefix:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          parent: 10.156.0.0/19
          prefix_length: 24
        state: present
        first_available: yes

    - name: Get a new /24 inside 10.157.0.0/19 within NetBox with additional values
      netbox.netbox.netbox_prefix:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          parent: 10.157.0.0/19
          prefix_length: 24
          vrf: Test VRF
          site: Test Site
        state: present
        first_available: yes
```

## [Return Values](netbox_prefix_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Message indicating failure or info about what has been achieved  **Returned:** always |
| **prefix**  dictionary | Serialized object as created or already existent within NetBox  **Returned:** on creation |

### Authors

- Mikhail Yohman (@FragmentedPacket)
- Anthony Ruhier (@Anthony25)

### Collection links

- [Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
- [Repository (Sources)](https://github.com/netbox-community/ansible_modules)
