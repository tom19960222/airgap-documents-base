---
collection: ansible
version: "8"
title: "junipernetworks.junos.junos_banner module – Manage multiline banners on Juniper JUNOS devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/junipernetworks/junos/junos_banner_module.html
fetched_at: 2026-07-28T02:39:30+00:00
---
# junipernetworks.junos.junos_banner module – Manage multiline banners on Juniper JUNOS devices

> **Note:**
>
> This module is part of the [junipernetworks.junos collection](https://galaxy.ansible.com/ui/repo/published/junipernetworks/junos/) (version 5.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install junipernetworks.junos`.
> You need further requirements to be able to use this module,
> see [Requirements](junos_banner_module.md#ansible-collections-junipernetworks-junos-junos-banner-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_banner`.

New in junipernetworks.junos 1.0.0

- [Synopsis](junos_banner_module.md#synopsis)
- [Requirements](junos_banner_module.md#requirements)
- [Parameters](junos_banner_module.md#parameters)
- [Notes](junos_banner_module.md#notes)
- [Examples](junos_banner_module.md#examples)
- [Return Values](junos_banner_module.md#return-values)

## [Synopsis](junos_banner_module.md#id1)

- This will configure both login and motd banners on network devices. It allows playbooks to add or remote banner text from the active running configuration.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: banner

## [Requirements](junos_banner_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.5.2)

## [Parameters](junos_banner_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **active**  boolean | Specifies whether or not the configuration is active or deactivated  **Choices:**   - `false` - `true` ← (default) |
| **banner**  string / required | Specifies which banner that should be configured on the remote device. Value `login` indicates system login message prior to authenticating, `motd` is login announcement after successful authentication.  **Choices:**   - `"login"` - `"motd"` |
| **state**  string | Specifies whether or not the configuration is present in the current devices active running configuration.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **text**  string | The banner text that should be present in the remote device running configuration. This argument accepts a multiline string, with no empty lines. Requires *state=present*. |

## [Notes](junos_banner_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Tested against vSRX JUNOS version 15.1X49-D15.4, vqfx-10000 JUNOS Version 15.1X53-D60.4.
> - Recommended connection is `netconf`. See [the Junos OS Platform Options](../network/user_guide/platform_junos.md).
> - This module also works with `local` connections for legacy playbooks.
> - For information on using CLI and netconf see the :ref:`Junos OS Platform Options guide <junos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Juniper network devices see <https://www.ansible.com/ansible-juniper>.

## [Examples](junos_banner_module.md#id5)

```yaml+jinja
- name: configure the login banner
  junipernetworks.junos.junos_banner:
    banner: login
    text: |
      this is my login banner
      that contains a multiline
      string
    state: present

- name: remove the motd banner
  junipernetworks.junos.junos_banner:
    banner: motd
    state: absent

- name: deactivate the motd banner
  junipernetworks.junos.junos_banner:
    banner: motd
    state: present
    active: false

- name: activate the motd banner
  junipernetworks.junos.junos_banner:
    banner: motd
    state: present
    active: true

- name: Configure banner from file
  junipernetworks.junos.junos_banner:
    banner: motd
    text: "{{ lookup('file', './config_partial/raw_banner.cfg') }}"
    state: present
```

## [Return Values](junos_banner_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **diff.prepared**  string | Configuration difference before and after applying change.  **Returned:** when configuration is changed and diff option is enabled.  **Sample:** `"[edit system login] +   message \"this is my login banner\";\n"` |

### Authors

- Ganesh Nalawade (@ganeshrn)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
