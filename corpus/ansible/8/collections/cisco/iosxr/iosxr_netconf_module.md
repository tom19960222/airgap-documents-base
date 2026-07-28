---
collection: ansible
version: "8"
title: "cisco.iosxr.iosxr_netconf module – Configures NetConf sub-system service on Cisco IOS-XR devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/iosxr/iosxr_netconf_module.html
fetched_at: 2026-07-28T01:26:52+00:00
---
# cisco.iosxr.iosxr_netconf module – Configures NetConf sub-system service on Cisco IOS-XR devices

> **Note:**
>
> This module is part of the [cisco.iosxr collection](https://galaxy.ansible.com/ui/repo/published/cisco/iosxr/) (version 5.0.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.iosxr`.
>
> To use it in a playbook, specify: `cisco.iosxr.iosxr_netconf`.

New in cisco.iosxr 1.0.0

- [Synopsis](iosxr_netconf_module.md#synopsis)
- [Parameters](iosxr_netconf_module.md#parameters)
- [Notes](iosxr_netconf_module.md#notes)
- [Examples](iosxr_netconf_module.md#examples)
- [Return Values](iosxr_netconf_module.md#return-values)

## [Synopsis](iosxr_netconf_module.md#id1)

- This module provides an abstraction that enables and configures the netconf system service running on Cisco IOS-XR Software. This module can be used to easily enable the Netconf API. Netconf provides a programmatic interface for working with configuration and state resources as defined in RFC 6242.

Aliases: netconf

## [Parameters](iosxr_netconf_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **netconf_port**  aliases: listens_on  integer | This argument specifies the port the netconf service should listen on for SSH connections. The default port as defined in RFC 6242 is 830.  **Default:** `830` |
| **netconf_vrf**  aliases: vrf  string | netconf vrf name  **Default:** `"default"` |
| **state**  string | Specifies the state of the `iosxr_netconf` resource on the remote device. If the *state* argument is set to *present* the netconf service will be configured. If the *state* argument is set to *absent* the netconf service will be removed from the configuration.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](iosxr_netconf_module.md#id3)

> **Note:**
>
> - This module works with connection `network_cli`. See [the IOS-XR Platform Options](../network/user_guide/platform_iosxr.md).
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](iosxr_netconf_module.md#id4)

```yaml+jinja
- name: enable netconf service on port 830
  cisco.iosxr.iosxr_netconf:
    listens_on: 830
    state: present

- name: disable netconf service
  cisco.iosxr.iosxr_netconf:
    state: absent
```

## [Return Values](iosxr_netconf_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  string | Returns the command sent to the remote device  **Returned:** when changed is True  **Sample:** `"ssh server netconf port 830"` |

### Authors

- Kedar Kekan (@kedarX)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
