---
collection: ansible
version: "8"
title: "netbox.netbox.netbox_circuit module – Create, update or delete circuits within NetBox"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netbox/netbox/netbox_circuit_module.html
fetched_at: 2026-07-28T02:44:47+00:00
---
# netbox.netbox.netbox_circuit module – Create, update or delete circuits within NetBox

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
> see [Requirements](netbox_circuit_module.md#ansible-collections-netbox-netbox-netbox-circuit-module-requirements) for details.
>
> To use it in a playbook, specify: `netbox.netbox.netbox_circuit`.

New in netbox.netbox 0.1.0

- [Synopsis](netbox_circuit_module.md#synopsis)
- [Requirements](netbox_circuit_module.md#requirements)
- [Parameters](netbox_circuit_module.md#parameters)
- [Notes](netbox_circuit_module.md#notes)
- [Examples](netbox_circuit_module.md#examples)
- [Return Values](netbox_circuit_module.md#return-values)

## [Synopsis](netbox_circuit_module.md#id1)

- Creates, updates or removes circuits from NetBox

## [Requirements](netbox_circuit_module.md#id2)

The below requirements are needed on the host that executes this module.

- pynetbox

## [Parameters](netbox_circuit_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert**  any | Certificate path |
| **data**  dictionary / required | Defines the circuit configuration |
| **cid**  string / required | The circuit id of the circuit |
| **circuit_type**  any | The circuit type of the circuit |
| **comments**  string | Comments related to circuit |
| **commit_rate**  integer | Commit rate of the circuit (Kbps) |
| **custom_fields**  dictionary | must exist in NetBox |
| **description**  string | Description of the circuit |
| **install_date**  string | The date the circuit was installed. e.g. YYYY-MM-DD |
| **provider**  any | The provider of the circuit |
| **status**  any | The status of the circuit |
| **tags**  list / elements=any | Any tags that the device may need to be associated with |
| **tenant**  any | The tenant assigned to the circuit |
| **netbox_token**  string / required | The NetBox API token. |
| **netbox_url**  string / required | The URL of the NetBox instance.  Must be accessible by the Ansible control host. |
| **query_params**  list / elements=string | This can be used to override the specified values in ALLOWED_QUERY_PARAMS that are defined  in plugins/module_utils/netbox_utils.py and provides control to users on what may make  an object unique in their environment. |
| **state**  string | The state of the object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  any | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using a self-signed certificates.  **Default:** `true` |

## [Notes](netbox_circuit_module.md#id4)

> **Note:**
>
> - Tags should be defined as a YAML list
> - This should be ran with connection `local` and hosts `localhost`

## [Examples](netbox_circuit_module.md#id5)

```yaml+jinja
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create circuit within NetBox with only required information
      netbox.netbox.netbox_circuit:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          cid: Test Circuit
          provider: Test Provider
          circuit_type: Test Circuit Type
        state: present

    - name: Update circuit with other fields
      netbox.netbox.netbox_circuit:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          cid: Test-Circuit-1000
          provider: Test Provider
          circuit_type: Test Circuit Type
          status: Active
          tenant: Test Tenant
          install_date: "2018-12-25"
          commit_rate: 10000
          description: Test circuit
          comments: "FAST CIRCUIT"
        state: present

    - name: Delete circuit within netbox
      netbox.netbox.netbox_circuit:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          cid: Test-Circuit-1000
        state: absent
```

## [Return Values](netbox_circuit_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **circuit**  dictionary | Serialized object as created or already existent within NetBox  **Returned:** success (when *state=present*) |
| **msg**  string | Message indicating failure or info about what has been achieved  **Returned:** always |

### Authors

- Mikhail Yohman (@FragmentedPacket)

### Collection links

- [Issue Tracker](https://github.com/netbox-community/ansible_modules/issues)
- [Repository (Sources)](https://github.com/netbox-community/ansible_modules)
