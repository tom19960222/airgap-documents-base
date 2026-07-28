---
collection: ansible
version: "8"
title: "community.network.icx_banner module – Manage multiline banners on Ruckus ICX 7000 series switches"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/icx_banner_module.html
fetched_at: 2026-07-28T01:56:44+00:00
---
# community.network.icx_banner module – Manage multiline banners on Ruckus ICX 7000 series switches

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.icx_banner`.

- [Synopsis](icx_banner_module.md#synopsis)
- [Parameters](icx_banner_module.md#parameters)
- [Notes](icx_banner_module.md#notes)
- [Examples](icx_banner_module.md#examples)
- [Return Values](icx_banner_module.md#return-values)

## [Synopsis](icx_banner_module.md#id1)

- This will configure both login and motd banners on remote ruckus ICX 7000 series switches. It allows playbooks to add or remove banner text from the active running configuration.

Aliases: network.icx.icx_banner

## [Parameters](icx_banner_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **banner**  string / required | Specifies which banner should be configured on the remote device.  **Choices:**   - `"motd"` - `"exec"` - `"incoming"` |
| **check_running_config**  boolean | Check running configuration. This can be set as environment variable. Module will use environment variable value(default:True), unless it is overridden, by specifying it as module parameter.  **Choices:**   - `false` - `true` ← (default) |
| **enterkey**  boolean | Specifies whether or not the motd configuration should accept the require-enter-key  Default is false.  **Choices:**   - `false` - `true` |
| **state**  string | Specifies whether or not the configuration is present in the current devices active running configuration.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **text**  string | The banner text that should be present in the remote device running configuration. This argument accepts a multiline string, with no empty lines. |

## [Notes](icx_banner_module.md#id3)

> **Note:**
>
> - Tested against ICX 10.1

## [Examples](icx_banner_module.md#id4)

```yaml+jinja
- name: Configure the motd banner
  community.network.icx_banner:
    banner: motd
    text: |
        this is my motd banner
        that contains a multiline
        string
    state: present

- name: Remove the motd banner
  community.network.icx_banner:
    banner: motd
    state: absent

- name: Configure require-enter-key for motd
  community.network.icx_banner:
    banner: motd
    enterkey: true

- name: Remove require-enter-key for motd
  community.network.icx_banner:
    banner: motd
    enterkey: false
```

## [Return Values](icx_banner_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always  **Sample:** `["banner motd", "this is my motd banner", "that contains a multiline", "string"]` |

### Authors

- Ruckus Wireless (@Commscope)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
