---
collection: ansible
version: "6"
title: "community.sap.sap_system_facts module – Gathers SAP facts in a host"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/sap/sap_system_facts_module.html
fetched_at: 2026-07-27T17:20:59+00:00
---
# community.sap.sap_system_facts module – Gathers SAP facts in a host

> **Note:**
>
> This module is part of the [community.sap collection](https://galaxy.ansible.com/community/sap) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.sap`.
>
> To use it in a playbook, specify: `community.sap.sap_system_facts`.

New in community.sap 1.0.0

- [Synopsis](sap_system_facts_module.md#synopsis)
- [Notes](sap_system_facts_module.md#notes)
- [Examples](sap_system_facts_module.md#examples)
- [Returned Facts](sap_system_facts_module.md#returned-facts)

## [Synopsis](sap_system_facts_module.md#id1)

- This facts module gathers SAP system facts about the running instance.

## [Notes](sap_system_facts_module.md#id2)

> **Note:**
>
> - Supports `check_mode`.

## [Examples](sap_system_facts_module.md#id3)

```yaml+jinja
- name: Return SAP system ansible_facts
  community.sap.sap_system_fact:
```

## [Returned Facts](sap_system_facts_module.md#id4)

Facts returned by this module are added/updated in the `hostvars` host facts and can be referenced by name just like any other host fact. They do not need to be registered in order to use them.

| Key | Description |
| --- | --- |
| **sap**  list / elements=dictionary | Facts about the running SAP system.  Returned: When SAP system fact is present  Sample: `[{"InstanceType": "NW", "NR": "00", "SID": "ABC", "TYPE": "ASCS"}, {"InstanceType": "NW", "NR": "01", "SID": "ABC", "TYPE": "PAS"}, {"InstanceType": "HANA", "NR": "02", "SID": "HDB", "TYPE": "HDB"}, {"InstanceType": "NW", "NR": "80", "SID": "WEB", "TYPE": "WebDisp"}]` |

### Authors

- Rainer Leber (@rainerleber)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.sap/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.sap)
