---
collection: ansible
version: "8"
title: "netbox.netbox.netbox_vm_interface module – Creates or removes interfaces from virtual machines in NetBox"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netbox/netbox/netbox_vm_interface_module.html
fetched_at: 2026-07-28T02:45:35+00:00
---
# netbox.netbox.netbox_vm_interface module – Creates or removes interfaces from virtual machines in NetBox

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
> see [Requirements](netbox_vm_interface_module.md#ansible-collections-netbox-netbox-netbox-vm-interface-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_vm_interface`.

New in netbox.netbox 0.1.0

- [Synopsis](netbox_vm_interface_module.md#synopsis)
- [Requirements](netbox_vm_interface_module.md#requirements)
- [Parameters](netbox_vm_interface_module.md#parameters)
- [Notes](netbox_vm_interface_module.md#notes)
- [Examples](netbox_vm_interface_module.md#examples)
- [Return Values](netbox_vm_interface_module.md#return-values)

## [Synopsis](netbox_vm_interface_module.md#id1)

- Creates or removes interfaces from virtual machines in NetBox

## [Requirements](netbox_vm_interface_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_vm_interface_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the vm interface configuration |
| **custom_fields**  dictionary  *added in netbox.netbox 3.4.0* | Must exist in NetBox |
| **description**  string | The description of the interface |
| **enabled**  boolean | Sets whether interface shows enabled or disabled  **Choices:**   - `false` - `true` |
| **mac_address**  string | The MAC address of the interface |
| **mode**  any | The mode of the interface |
| **mtu**  integer | The MTU of the interface |
| **name**  string / required | Name of the interface to be created |
| **parent_vm_interface**  any  *added in netbox.netbox 3.2.0* | The virtual machine interface’s parent interface. |
| **tagged_vlans**  any | A list of tagged VLANS to be assigned to interface. Mode must be set to either `Tagged` or `Tagged All` |
| **tags**  list / elements=any | Any tags that the prefix may need to be associated with |
| **untagged_vlan**  any | The untagged VLAN to be assigned to interface |
| **virtual_machine**  any | Name of the virtual machine the interface will be associated with (case-sensitive) |
| **vm_bridge**  any  *added in netbox.netbox 3.6.0* | The bridge the interface is connected to |
| **vrf**  any  *added in netbox.netbox 3.7.0* | VRF the interface is associated with |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  **Default:** `true` |

## [Notes](netbox_vm_interface_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_vm_interface_module.md#id5)

```yaml+jinja
- name: "Test NetBox interface module"
  connection: local
  hosts: localhost
  gather_facts: False
  tasks:
    - name: Create interface within NetBox with only required information
      netbox_vm_interface:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          virtual_machine: test100
          name: GigabitEthernet1
        state: present

    - name: Delete interface within netbox
      netbox_vm_interface:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          virtual_machine: test100
          name: GigabitEthernet1
        state: absent

    - name: Create interface as a trunk port
      netbox_vm_interface:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          virtual_machine: test100
          name: GigabitEthernet25
          enabled: false
          untagged_vlan:
            name: Wireless
            site: Test Site
          tagged_vlans:
            - name: Data
              site: Test Site
            - name: VoIP
              site: Test Site
          mtu: 1600
          mode: Tagged
        state: present

    - name: Create bridge interface within NetBox
      netbox_vm_interface:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          virtual_machine: test100
          name: br1000
        state: present

    - name: Connect bridge interface within NetBox
      netbox_vm_interface:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          virtual_machine: test100
          name: br1001
          vm_bridge: br1000
        state: present
```

## [Return Values](netbox_vm_interface_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **interface**  dictionary | Serialized object as created or already existent within NetBox  **Returned:** on creation |
| **msg**  string | Message indicating failure or info about what has been achieved  **Returned:** always |

### Authors

- Benjamin Vergnaud (@bvergnaud)

### Collection links

- [Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
- [Repository (Sources)](https://github.com/netbox-community/ansible_modules)
