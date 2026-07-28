---
collection: ansible
version: "6"
title: "community.network.pn_snmp_vacm module – CLI command to create/modify/delete snmp-vacm"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/pn_snmp_vacm_module.html
fetched_at: 2026-07-27T17:19:30+00:00
---
# community.network.pn_snmp_vacm module – CLI command to create/modify/delete snmp-vacm

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.pn_snmp_vacm`.

- [Synopsis](pn_snmp_vacm_module.md#synopsis)
- [Parameters](pn_snmp_vacm_module.md#parameters)
- [Examples](pn_snmp_vacm_module.md#examples)
- [Return Values](pn_snmp_vacm_module.md#return-values)

## [Synopsis](pn_snmp_vacm_module.md#id1)

- This module can be used to create View Access Control Models (VACM), modify VACM and delete VACM.

## [Parameters](pn_snmp_vacm_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_auth**  boolean | authentication required.  Choices:   - `false` - `true` |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_oid_restrict**  string | restrict OID. |
| **pn_priv**  boolean | privileges.  Choices:   - `false` - `true` |
| **pn_user_name**  string | SNMP administrator name. |
| **pn_user_type**  string | SNMP user type.  Choices:   - `"rouser"` - `"rwuser"` |
| **state**  string / required | State the action to perform. Use `present` to create snmp-vacm and `absent` to delete snmp-vacm and `update` to modify snmp-vacm.  Choices:   - `"present"` - `"absent"` - `"update"` |

## [Examples](pn_snmp_vacm_module.md#id3)

```yaml+jinja
- name: Create snmp vacm
  community.network.pn_snmp_vacm:
    pn_cliswitch: "sw01"
    state: "present"
    pn_user_name: "foo"
    pn_user_type: "rouser"

- name: Update snmp vacm
  community.network.pn_snmp_vacm:
    pn_cliswitch: "sw01"
    state: "update"
    pn_user_name: "foo"
    pn_user_type: "rwuser"

- name: Delete snmp vacm
  community.network.pn_snmp_vacm:
    pn_cliswitch: "sw01"
    state: "absent"
    pn_user_name: "foo"
```

## [Return Values](pn_snmp_vacm_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  Returned: always |
| **command**  string | the CLI command run on the target node.  Returned: always |
| **stderr**  list / elements=string | set of error responses from the snmp-vacm command.  Returned: on error |
| **stdout**  list / elements=string | set of responses from the snmp-vacm command.  Returned: always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
