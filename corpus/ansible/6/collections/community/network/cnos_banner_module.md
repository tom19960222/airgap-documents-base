---
collection: ansible
version: "6"
title: "community.network.cnos_banner module – Manage multiline banners on Lenovo CNOS devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/cnos_banner_module.html
fetched_at: 2026-07-27T17:18:03+00:00
---
# community.network.cnos_banner module – Manage multiline banners on Lenovo CNOS devices

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
> To use it in a playbook, specify: `community.network.cnos_banner`.

- [Synopsis](cnos_banner_module.md#synopsis)
- [Parameters](cnos_banner_module.md#parameters)
- [Notes](cnos_banner_module.md#notes)
- [Examples](cnos_banner_module.md#examples)
- [Return Values](cnos_banner_module.md#return-values)

## [Synopsis](cnos_banner_module.md#id1)

- This will configure both login and motd banners on remote devices running Lenovo CNOS. It allows playbooks to add or remote banner text from the active running configuration.

## [Parameters](cnos_banner_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **banner**  string / required | Specifies which banner should be configured on the remote device. In Ansible 2.8 and earlier only *login* and *motd* were supported.  Choices:   - `"login"` - `"motd"` |
| **state**  string | Specifies whether or not the configuration is present in the current devices active running configuration.  Choices:   - `"present"` ← (default) - `"absent"` |
| **text**  string | The banner text that should be present in the remote device running configuration. This argument accepts a multiline string, with no empty lines. Requires *state=present*. |

## [Notes](cnos_banner_module.md#id3)

> **Note:**
>
> - Tested against CNOS 10.8.1

## [Examples](cnos_banner_module.md#id4)

```yaml+jinja
- name: Configure the login banner
  community.network.cnos_banner:
    banner: login
    text: |
      this is my login banner
      that contains a multiline
      string
    state: present

- name: Remove the motd banner
  community.network.cnos_banner:
    banner: motd
    state: absent

- name: Configure banner from file
  community.network.cnos_banner:
    banner:  motd
    text: "{{ lookup('file', './config_partial/raw_banner.cfg') }}"
    state: present
```

## [Return Values](cnos_banner_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always  Sample: `["banner login", "this is my login banner", "that contains a multiline", "string"]` |

### Authors

- Anil Kumar Muraleedharan (@amuraleedhar)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
