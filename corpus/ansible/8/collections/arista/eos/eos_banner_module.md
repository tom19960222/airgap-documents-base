---
collection: ansible
version: "8"
title: "arista.eos.eos_banner module – Manage multiline banners on Arista EOS devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/arista/eos/eos_banner_module.html
fetched_at: 2026-07-28T01:10:58+00:00
---
# arista.eos.eos_banner module – Manage multiline banners on Arista EOS devices

> **Note:**
>
> This module is part of the [arista.eos collection](https://galaxy.ansible.com/ui/repo/published/arista/eos/) (version 6.2.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install arista.eos`.
>
> To use it in a playbook, specify: `arista.eos.eos_banner`.

New in arista.eos 1.0.0

- [Synopsis](eos_banner_module.md#synopsis)
- [Parameters](eos_banner_module.md#parameters)
- [Notes](eos_banner_module.md#notes)
- [Examples](eos_banner_module.md#examples)
- [Return Values](eos_banner_module.md#return-values)

## [Synopsis](eos_banner_module.md#id1)

- This will configure both login and motd banners on remote devices running Arista EOS. It allows playbooks to add or remote banner text from the active running configuration.

Aliases: banner

## [Parameters](eos_banner_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **banner**  string / required | Specifies which banner that should be configured on the remote device.  **Choices:**   - `"login"` - `"motd"` |
| **state**  string | Specifies whether or not the configuration is present in the current devices active running configuration.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **text**  string | The banner text that should be present in the remote device running configuration. This argument accepts a multiline string. Requires *state=present*. |

## [Notes](eos_banner_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F

## [Examples](eos_banner_module.md#id4)

```yaml+jinja
- name: configure the login banner
  arista.eos.eos_banner:
    banner: login
    text: |
      this is my login banner
      that contains a multiline
      string
    state: present

- name: remove the motd banner
  arista.eos.eos_banner:
    banner: motd
    state: absent
```

## [Return Values](eos_banner_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always  **Sample:** `["banner login", "this is my login banner", "that contains a multiline", "string", "EOF"]` |
| **session_name**  string | The EOS config session name used to load the configuration  **Returned:** if changes  **Sample:** `"ansible_1479315771"` |

### Authors

- Peter Sprygada (@privateip)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/arista.eos)
