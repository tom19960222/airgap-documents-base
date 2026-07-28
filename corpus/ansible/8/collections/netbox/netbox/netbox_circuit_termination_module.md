---
collection: ansible
version: "8"
title: "netbox.netbox.netbox_circuit_termination module – Create, update or delete circuit terminations within NetBox"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netbox/netbox/netbox_circuit_termination_module.html
fetched_at: 2026-07-28T02:44:48+00:00
---
# netbox.netbox.netbox_circuit_termination module – Create, update or delete circuit terminations within NetBox

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
> see [Requirements](netbox_circuit_termination_module.md#ansible-collections-netbox-netbox-netbox-circuit-termination-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_circuit_termination`.

New in netbox.netbox 0.1.0

- [Synopsis](netbox_circuit_termination_module.md#synopsis)
- [Requirements](netbox_circuit_termination_module.md#requirements)
- [Parameters](netbox_circuit_termination_module.md#parameters)
- [Notes](netbox_circuit_termination_module.md#notes)
- [Examples](netbox_circuit_termination_module.md#examples)
- [Return Values](netbox_circuit_termination_module.md#return-values)

## [Synopsis](netbox_circuit_termination_module.md#id1)

- Creates, updates or removes circuit terminations from NetBox

## [Requirements](netbox_circuit_termination_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_circuit_termination_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the circuit termination configuration |
| **circuit**  any / required | The circuit to assign to circuit termination |
| **description**  string | Description of the circuit termination |
| **mark_connected**  boolean  *added in netbox.netbox 3.5.0* | Treat as if cable is connected  **Choices:**   - `false` - `true` |
| **port_speed**  integer | The speed of the port (Kbps) |
| **pp_info**  string | Patch panel information |
| **provider_network**  any | The provider_network the circuit termination will be assigned to |
| **site**  any | The site the circuit termination will be assigned to |
| **term_side**  string / required | The side of the circuit termination  **Choices:**   - `"A"` - `"Z"` |
| **upstream_speed**  integer | The upstream speed of the circuit termination |
| **xconnect_id**  string | The cross connect ID of the circuit termination |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  **Default:** `true` |

## [Notes](netbox_circuit_termination_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_circuit_termination_module.md#id5)

```yaml+jinja
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create circuit termination within NetBox with only required information
      netbox.netbox.netbox_circuit_termination:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          circuit: Test Circuit
          term_side: A
          site: Test Site
          port_speed: 10000
        state: present

    - name: Update circuit termination with other fields
      netbox.netbox.netbox_circuit_termination:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          circuit: Test Circuit
          term_side: A
          upstream_speed: 1000
          xconnect_id: 10X100
          pp_info: PP10-24
          description: "Test description"
        state: present

    - name: Delete circuit termination within netbox
      netbox.netbox.netbox_circuit_termination:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          circuit: Test Circuit
          term_side: A
        state: absent
```

## [Return Values](netbox_circuit_termination_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **circuit_termination**  dictionary | Serialized object as created or already existent within NetBox  **Returned:** success (when *state=present*) |
| **msg**  string | Message indicating failure or info about what has been achieved  **Returned:** always |

### Authors

- Mikhail Yohman (@FragmentedPacket)

### Collection links

- [Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
- [Repository (Sources)](https://github.com/netbox-community/ansible_modules)
