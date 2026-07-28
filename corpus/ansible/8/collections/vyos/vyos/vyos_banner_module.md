---
collection: ansible
version: "8"
title: "vyos.vyos.vyos_banner module – Manage multiline banners on VyOS devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vyos/vyos/vyos_banner_module.html
fetched_at: 2026-07-28T02:59:07+00:00
---
# vyos.vyos.vyos_banner module – Manage multiline banners on VyOS devices

> **Note:**
>
> This module is part of the [vyos.vyos collection](https://galaxy.ansible.com/ui/repo/published/vyos/vyos/) (version 4.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vyos.vyos`.
>
> To use it in a playbook, specify: `vyos.vyos.vyos_banner`.

New in vyos.vyos 1.0.0

- [Synopsis](vyos_banner_module.md#synopsis)
- [Parameters](vyos_banner_module.md#parameters)
- [Notes](vyos_banner_module.md#notes)
- [Examples](vyos_banner_module.md#examples)
- [Return Values](vyos_banner_module.md#return-values)

## [Synopsis](vyos_banner_module.md#id1)

- This will configure both pre-login and post-login banners on remote devices running VyOS. It allows playbooks to add or remote banner text from the active running configuration.

Aliases: banner

## [Parameters](vyos_banner_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **banner**  string / required | Specifies which banner that should be configured on the remote device.  **Choices:**   - `"pre-login"` - `"post-login"` |
| **state**  string | Specifies whether or not the configuration is present in the current devices active running configuration.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **text**  string | The banner text that should be present in the remote device running configuration. This argument accepts a multiline string, with no empty lines. Requires *state=present*. |

## [Notes](vyos_banner_module.md#id3)

> **Note:**
>
> - Tested against VyOS 1.1.8 (helium).
> - This module works with connection `ansible.netcommon.network_cli`. See [the VyOS OS Platform Options](../network/user_guide/platform_vyos.md).
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`

## [Examples](vyos_banner_module.md#id4)

```yaml+jinja
- name: configure the pre-login banner
  vyos.vyos.vyos_banner:
    banner: pre-login
    text: |
      this is my pre-login banner
      that contains a multiline
      string
    state: present
- name: remove the post-login banner
  vyos.vyos.vyos_banner:
    banner: post-login
    state: absent
```

## [Return Values](vyos_banner_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always  **Sample:** `["banner pre-login", "this is my pre-login banner", "that contains a multiline", "string"]` |

### Authors

- Trishna Guha (@trishnaguha)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
