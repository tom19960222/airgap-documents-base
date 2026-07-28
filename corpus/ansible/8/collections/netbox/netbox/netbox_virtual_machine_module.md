---
collection: ansible
version: "8"
title: "netbox.netbox.netbox_virtual_machine module – Create, update or delete virtual_machines within NetBox"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netbox/netbox/netbox_virtual_machine_module.html
fetched_at: 2026-07-28T02:45:32+00:00
---
# netbox.netbox.netbox_virtual_machine module – Create, update or delete virtual_machines within NetBox

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
> see [Requirements](netbox_virtual_machine_module.md#ansible-collections-netbox-netbox-netbox-virtual-machine-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_virtual_machine`.

New in netbox.netbox 0.1.0

- [Synopsis](netbox_virtual_machine_module.md#synopsis)
- [Requirements](netbox_virtual_machine_module.md#requirements)
- [Parameters](netbox_virtual_machine_module.md#parameters)
- [Notes](netbox_virtual_machine_module.md#notes)
- [Examples](netbox_virtual_machine_module.md#examples)
- [Return Values](netbox_virtual_machine_module.md#return-values)

## [Synopsis](netbox_virtual_machine_module.md#id1)

- Creates, updates or removes virtual_machines from NetBox

## [Requirements](netbox_virtual_machine_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_virtual_machine_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the virtual machine configuration |
| **cluster**  any | The name of the cluster attach to the virtual machine |
| **comments**  string | Comments of the virtual machine |
| **custom_fields**  dictionary | Must exist in NetBox |
| **description**  string  *added in netbox.netbox 3.10.0* | The description of the virtual machine |
| **device**  any  *added in netbox.netbox 3.9.0* | The device the virtual machine is pinned to in the cluster |
| **disk**  integer | Disk of the virtual machine (GB) |
| **local_context_data**  dictionary | configuration context of the virtual machine |
| **memory**  integer | Memory of the virtual machine (MB) |
| **name**  string / required | The name of the virtual machine |
| **platform**  any | The platform of the virtual machine |
| **primary_ip4**  any | Primary IPv4 address assigned to the virtual machine |
| **primary_ip6**  any | Primary IPv6 address assigned to the virtual machine |
| **site**  any | The name of the site attach to the virtual machine |
| **status**  any | The status of the virtual machine |
| **tags**  list / elements=any | Any tags that the virtual machine may need to be associated with |
| **tenant**  any | The tenant that the virtual machine will be assigned to |
| **vcpus**  float | Number of vcpus of the virtual machine |
| **virtual_machine_role**  any | The role of the virtual machine |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  **Default:** `true` |

## [Notes](netbox_virtual_machine_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_virtual_machine_module.md#id5)

```yaml+jinja
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False
  tasks:
    - name: Create virtual machine within NetBox with only required information
      netbox_virtual_machine:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Virtual Machine
          cluster: test cluster
        state: present

    - name: Delete virtual machine within netbox
      netbox_virtual_machine:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Virtual Machine
        state: absent

    - name: Create virtual machine with tags
      netbox_virtual_machine:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Another Test Virtual Machine
          cluster: test cluster
          site: Test Site
          tags:
            - Schnozzberry
        state: present

    - name: Update vcpus, memory and disk of an existing virtual machine
      netbox_virtual_machine:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Virtual Machine
          cluster: test cluster
          vcpus: 8
          memory: 8
          disk: 8
        state: present
```

## [Return Values](netbox_virtual_machine_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Message indicating failure or info about what has been achieved  **Returned:** always |
| **virtual machine**  dictionary | Serialized object as created or already existent within NetBox  **Returned:** success (when *state=present*) |

### Authors

- Gaelle MANGIN (@gmangin)

### Collection links

- [Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
- [Repository (Sources)](https://github.com/netbox-community/ansible_modules)
