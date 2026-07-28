---
collection: ansible
version: "6"
title: "community.general.cobbler_system module – Manage system objects in Cobbler"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/cobbler_system_module.html
fetched_at: 2026-07-27T17:08:32+00:00
---
# community.general.cobbler_system module – Manage system objects in Cobbler

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.cobbler_system`.

- [Synopsis](cobbler_system_module.md#synopsis)
- [Parameters](cobbler_system_module.md#parameters)
- [Notes](cobbler_system_module.md#notes)
- [Examples](cobbler_system_module.md#examples)
- [Return Values](cobbler_system_module.md#return-values)

## [Synopsis](cobbler_system_module.md#id1)

- Add, modify or remove systems in Cobbler

## [Parameters](cobbler_system_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **host**  string | The name or IP address of the Cobbler system.  Default: `"127.0.0.1"` |
| **interfaces**  dictionary | A list of dictionaries containing interface options. |
| **name**  string | The system name to manage. |
| **password**  string | The password to log in to Cobbler. |
| **port**  integer | Port number to be used for REST connection.  The default value depends on parameter `use_ssl`. |
| **properties**  dictionary | A dictionary with system properties. |
| **state**  string | Whether the system should be present, absent or a query is made.  Choices:   - `"absent"` - `"present"` ← (default) - `"query"` |
| **sync**  boolean | Sync on changes.  Concurrently syncing Cobbler is bound to fail.  Choices:   - `false` ← (default) - `true` |
| **use_ssl**  boolean | If `false`, an HTTP connection will be used instead of the default HTTPS connection.  Choices:   - `false` - `true` ← (default) |
| **username**  string | The username to log in to Cobbler.  Default: `"cobbler"` |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only set to `false` when used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](cobbler_system_module.md#id3)

> **Note:**
>
> - Concurrently syncing Cobbler is bound to fail with weird errors.
> - On python 2.7.8 and older (i.e. on RHEL7) you may need to tweak the python behaviour to disable certificate validation. More information at [Certificate verification in Python standard library HTTP clients](https://access.redhat.com/articles/2039753).

## [Examples](cobbler_system_module.md#id4)

```yaml+jinja
- name: Ensure the system exists in Cobbler
  community.general.cobbler_system:
    host: cobbler01
    username: cobbler
    password: MySuperSecureP4sswOrd
    name: myhost
    properties:
      profile: CentOS6-x86_64
      name_servers: [ 2.3.4.5, 3.4.5.6 ]
      name_servers_search: foo.com, bar.com
    interfaces:
      eth0:
        macaddress: 00:01:02:03:04:05
        ipaddress: 1.2.3.4
  delegate_to: localhost

- name: Enable network boot in Cobbler
  community.general.cobbler_system:
    host: bdsol-aci-cobbler-01
    username: cobbler
    password: ins3965!
    name: bdsol-aci51-apic1.cisco.com
    properties:
      netboot_enabled: true
    state: present
  delegate_to: localhost

- name: Query all systems in Cobbler
  community.general.cobbler_system:
    host: cobbler01
    username: cobbler
    password: MySuperSecureP4sswOrd
    state: query
  register: cobbler_systems
  delegate_to: localhost

- name: Query a specific system in Cobbler
  community.general.cobbler_system:
    host: cobbler01
    username: cobbler
    password: MySuperSecureP4sswOrd
    name: '{{ inventory_hostname }}'
    state: query
  register: cobbler_properties
  delegate_to: localhost

- name: Ensure the system does not exist in Cobbler
  community.general.cobbler_system:
    host: cobbler01
    username: cobbler
    password: MySuperSecureP4sswOrd
    name: myhost
    state: absent
  delegate_to: localhost
```

## [Return Values](cobbler_system_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **system**  dictionary | (Resulting) information about the system we are working with  Returned: when *name* is provided |
| **systems**  list / elements=string | List of systems  Returned: *state=query* and *name* is not provided |

### Authors

- Dag Wieers (@dagwieers)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
