---
collection: ansible
version: "6"
title: "ansible.netcommon.net_banner module – (deprecated, removed after 2022-06-01) Manage multiline banners on network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/netcommon/net_banner_module.html
fetched_at: 2026-07-27T16:44:27+00:00
---
# ansible.netcommon.net_banner module – (deprecated, removed after 2022-06-01) Manage multiline banners on network devices

> **Note:**
>
> This module is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ansible/netcommon) (version 3.1.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
>
> To use it in a playbook, specify: `ansible.netcommon.net_banner`.

New in ansible.netcommon 1.0.0

- [DEPRECATED](net_banner_module.md#deprecated)
- [Synopsis](net_banner_module.md#synopsis)
- [Parameters](net_banner_module.md#parameters)
- [Notes](net_banner_module.md#notes)
- [Examples](net_banner_module.md#examples)
- [Return Values](net_banner_module.md#return-values)
- [Status](net_banner_module.md#status)

## [DEPRECATED](net_banner_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Updated modules released with more functionality

Alternative:
:   Use platform-specific “[netos]_banner” module

## [Synopsis](net_banner_module.md#id2)

- This will configure both login and motd banners on network devices. It allows playbooks to add or remove banner text from the active running configuration.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](net_banner_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **banner**  string / required | Specifies which banner that should be configured on the remote device.  Choices:   - `"login"` - `"motd"` |
| **state**  string | Specifies whether or not the configuration is present in the current devices active running configuration.  Choices:   - `"present"` ← (default) - `"absent"` |
| **text**  string | The banner text that should be present in the remote device running configuration. This argument accepts a multiline string, with no empty lines. Requires *state=present*. |

## [Notes](net_banner_module.md#id4)

> **Note:**
>
> - This module is supported on `ansible_network_os` network platforms. See the :ref:`Network Platform Options <platform_options>` for details.

## [Examples](net_banner_module.md#id5)

```yaml+jinja
- name: configure the login banner
  ansible.netcommon.net_banner:
    banner: login
    text: |
      this is my login banner
      that contains a multiline
      string
    state: present

- name: remove the motd banner
  ansible.netcommon.net_banner:
    banner: motd
    state: absent

- name: Configure banner from file
  ansible.netcommon.net_banner:
    banner: motd
    text: "{{ lookup('file', './config_partial/raw_banner.cfg') }}"
    state: present
```

## [Return Values](net_banner_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always, except for the platforms that use Netconf transport to manage the device.  Sample: `["banner login", "this is my login banner", "that contains a multiline", "string"]` |

## [Status](net_banner_module.md#id7)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](net_banner_module.md#deprecated).

### Authors

- Ricardo Carrillo Cruz (@rcarrillocruz)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
[Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
