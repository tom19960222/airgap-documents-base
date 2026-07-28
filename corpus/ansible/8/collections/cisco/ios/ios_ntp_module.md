---
collection: ansible
version: "8"
title: "cisco.ios.ios_ntp module – (deprecated, removed after 2024-01-01) Manages core NTP configuration."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ios/ios_ntp_module.html
fetched_at: 2026-07-28T01:26:19+00:00
---
# cisco.ios.ios_ntp module – (deprecated, removed after 2024-01-01) Manages core NTP configuration.

> **Note:**
>
> This module is part of the [cisco.ios collection](https://galaxy.ansible.com/ui/repo/published/cisco/ios/) (version 4.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ios`.
>
> To use it in a playbook, specify: `cisco.ios.ios_ntp`.

New in cisco.ios 1.0.0

- [DEPRECATED](ios_ntp_module.md#deprecated)
- [Synopsis](ios_ntp_module.md#synopsis)
- [Parameters](ios_ntp_module.md#parameters)
- [Notes](ios_ntp_module.md#notes)
- [Examples](ios_ntp_module.md#examples)
- [Return Values](ios_ntp_module.md#return-values)
- [Status](ios_ntp_module.md#status)

## [DEPRECATED](ios_ntp_module.md#id1)

Removed in:
:   major release after 2024-01-01

Why:
:   Updated module released with more functionality.

Alternative:
:   ios_ntp_global

## [Synopsis](ios_ntp_module.md#id2)

- Manages core NTP configuration.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: ntp

## [Parameters](ios_ntp_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **acl**  string | ACL for peer/server access restricition. |
| **auth**  boolean | Enable NTP authentication. Data type boolean.  **Choices:**   - `false` ← (default) - `true` |
| **auth_key**  string | md5 NTP authentication key of tye 7. |
| **key_id**  string | auth_key id. Data type string |
| **logging**  boolean | Enable NTP logs. Data type boolean.  **Choices:**   - `false` ← (default) - `true` |
| **server**  string | Network address of NTP server. |
| **source_int**  string | Source interface for NTP packets. |
| **state**  string | Manage the state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **vrf**  string | VRF configuration for NTP servers |

## [Notes](ios_ntp_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](ios_ntp_module.md#id5)

```yaml+jinja
# Set new NTP server and source interface
- name: Example ntp play
  cisco.ios.ios_ntp:
    server: 10.0.255.10
    source_int: Loopback0
    logging: false
    state: present

# Remove NTP ACL and logging
- name: Example ntp play absent
  cisco.ios.ios_ntp:
    acl: NTP_ACL
    logging: true
    state: absent

# Set NTP authentication
- name: Example ntp play auth
  cisco.ios.ios_ntp:
    key_id: 10
    auth_key: 15435A030726242723273C21181319000A
    auth: true
    state: present

# Set new NTP configuration
- name: Example ntp play auth
  cisco.ios.ios_ntp:
    server: 10.0.255.10
    source_int: Loopback0
    acl: NTP_ACL
    logging: true
    vrf: mgmt
    key_id: 10
    auth_key: 15435A030726242723273C21181319000A
    auth: true
    state: present
```

## [Return Values](ios_ntp_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | command sent to the device  **Returned:** always  **Sample:** `["no ntp server 10.0.255.10", "no ntp source Loopback0"]` |

## [Status](ios_ntp_module.md#id7)

- This module will be removed in a major release after 2024-01-01.
  *[deprecated]*
- For more information see [DEPRECATED](ios_ntp_module.md#deprecated).

### Authors

- Federico Olivieri (@Federico87)
- Joanie Sylvain (@JoanieAda)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
