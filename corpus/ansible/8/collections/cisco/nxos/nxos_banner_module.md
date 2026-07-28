---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_banner module – Manage multiline banners on Cisco NXOS devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_banner_module.html
fetched_at: 2026-07-28T01:38:28+00:00
---
# cisco.nxos.nxos_banner module – Manage multiline banners on Cisco NXOS devices

> **Note:**
>
> This module is part of the [cisco.nxos collection](https://galaxy.ansible.com/ui/repo/published/cisco/nxos/) (version 4.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.nxos_banner`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_banner_module.md#synopsis)
- [Parameters](nxos_banner_module.md#parameters)
- [Notes](nxos_banner_module.md#notes)
- [Examples](nxos_banner_module.md#examples)
- [Return Values](nxos_banner_module.md#return-values)

## [Synopsis](nxos_banner_module.md#id1)

- This will configure both exec and motd banners on remote devices running Cisco NXOS. It allows playbooks to add or remove banner text from the active running configuration.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: banner

## [Parameters](nxos_banner_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **banner**  string / required | Specifies which banner that should be configured on the remote device.  **Choices:**   - `"exec"` - `"motd"` |
| **multiline_delimiter**  string | Specify the delimiting character than will be used for configuration.  **Default:** `"@"` |
| **state**  string | Specifies whether or not the configuration is present in the current devices active running configuration.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **text**  string | The banner text that should be present in the remote device running configuration. This argument accepts a multiline string, with no empty lines. Requires *state=present*. |

## [Notes](nxos_banner_module.md#id3)

> **Note:**
>
> - Since responses from the device are always read with surrounding whitespaces stripped, tasks that configure banners with preceeding or trailing whitespaces will not be idempotent.
> - Limited Support for Cisco MDS
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_banner_module.md#id4)

```yaml+jinja
- name: configure the exec banner
  cisco.nxos.nxos_banner:
    banner: exec
    text: |
      this is my exec banner
      that contains a multiline
      string
    state: present
- name: remove the motd banner
  cisco.nxos.nxos_banner:
    banner: motd
    state: absent
- name: Configure banner from file
  cisco.nxos.nxos_banner:
    banner: motd
    text: "{{ lookup('file', './config_partial/raw_banner.cfg') }}"
    state: present
```

## [Return Values](nxos_banner_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always  **Sample:** `["banner exec", "this is my exec banner", "that contains a multiline", "string"]` |

### Authors

- Trishna Guha (@trishnaguha)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
