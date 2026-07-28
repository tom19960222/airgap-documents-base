---
collection: ansible
version: "8"
title: "cisco.ucs.ucs_query module – Queries UCS Manager objects by class or distinguished name"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ucs/ucs_query_module.html
fetched_at: 2026-07-28T01:39:37+00:00
---
# cisco.ucs.ucs_query module – Queries UCS Manager objects by class or distinguished name

> **Note:**
>
> This module is part of the [cisco.ucs collection](https://galaxy.ansible.com/ui/repo/published/cisco/ucs/) (version 1.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ucs`.
> You need further requirements to be able to use this module,
> see [Requirements](ucs_query_module.md#ansible-collections-cisco-ucs-ucs-query-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ucs.ucs_query`.

New in cisco.ucs 2.8

- [Synopsis](ucs_query_module.md#synopsis)
- [Requirements](ucs_query_module.md#requirements)
- [Parameters](ucs_query_module.md#parameters)
- [Examples](ucs_query_module.md#examples)
- [Return Values](ucs_query_module.md#return-values)

## [Synopsis](ucs_query_module.md#id1)

- -Queries UCS Manager objects by class or distinguished name.

## [Requirements](ucs_query_module.md#id2)

The below requirements are needed on the host that executes this module.

- ucsmsdk

## [Parameters](ucs_query_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **class_ids**  string | One or more UCS Manager Class IDs to query.  As a comma separated list |
| **delegate_to**  string | Where the module will be run  **Default:** `"localhost"` |
| **distinguished_names**  string | One or more UCS Manager Distinguished Names to query.  As a comma separated list |
| **hostname**  string / required | IP address or hostname of Cisco UCS Manager.  Modules can be used with the UCS Platform Emulator <https://cs.co/ucspe> |
| **password**  string / required | Password for Cisco UCS Manager authentication. |
| **port**  integer | Port number to be used during connection (by default uses 443 for https and 80 for http connection). |
| **proxy**  string | If use_proxy is no, specfies proxy to be used for connection. e.g. ‘<http://proxy.xy.z:8080>’ |
| **use_proxy**  boolean | If `no`, will not use the proxy as defined by system environment variable.  **Choices:**   - `false` - `true` ← (default) |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  **Choices:**   - `false` - `true` ← (default) |
| **username**  string | Username for Cisco UCS Manager authentication.  **Default:** `"admin"` |

## [Examples](ucs_query_module.md#id4)

```yaml+jinja
- name: Query UCS Class ID
  cisco.ucs.ucs_query:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    class_ids: computeBlade
    delegate_to: localhost

- name: Query UCS Class IDs
  cisco.ucs.ucs_query:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    class_ids: computeBlade, fabricVlan
    delegate_to: localhost

- name: Query UCS Distinguished Name
  cisco.ucs.ucs_query:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    distinguished_names: org-root
    delegate_to: localhost

- name: Query UCS Distinguished Names
  cisco.ucs.ucs_query:
    hostname: "{{ ucs_hostname }}"
    username: "{{ ucs_username }}"
    password: "{{ ucs_password }}"
    distinguished_names: org-root, sys/rack-unit-1, sys/chassis-1/blade-2
    delegate_to: localhost
```

## [Return Values](ucs_query_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **objects**  dictionary | results JSON encodded  **Returned:** success |

### Authors

- John McDonough (@movinalot)
- CiscoUcs (@CiscoUcs)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-ucs)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-ucs)
