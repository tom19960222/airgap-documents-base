---
collection: ansible
version: "8"
title: "junipernetworks.junos.junos_hostname module – Manage Hostname server configuration on Junos devices."
source_url: https://docs.ansible.com/projects/ansible/8/collections/junipernetworks/junos/junos_hostname_module.html
fetched_at: 2026-07-28T02:39:35+00:00
---
# junipernetworks.junos.junos_hostname module – Manage Hostname server configuration on Junos devices.

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
> see [Requirements](junos_hostname_module.md#ansible-collections-junipernetworks-junos-junos-hostname-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_hostname`.

New in junipernetworks.junos 2.9.0

- [Synopsis](junos_hostname_module.md#synopsis)
- [Requirements](junos_hostname_module.md#requirements)
- [Parameters](junos_hostname_module.md#parameters)
- [Notes](junos_hostname_module.md#notes)
- [Examples](junos_hostname_module.md#examples)
- [Return Values](junos_hostname_module.md#return-values)

## [Synopsis](junos_hostname_module.md#id1)

- This module manages hostname configuration on devices running Junos.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: hostname

## [Requirements](junos_hostname_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)
- xmltodict (>=0.12.0)

## [Parameters](junos_hostname_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of system Hostname configuration. |
| **hostname**  string | Specify the hostname. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the Junos device by executing the command **show system hostname**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  The states *rendered*, *gathered* and *parsed* does not perform any change on the device.  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result. For state *rendered* active connection to remote host is not required.  The states *merged*, *replaced* and *overridden* have identical behaviour for this module.  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result.  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result. The value of `running_config` option should be the same format as the output of command *show system hostname* executed on device. For state *parsed* active connection to remote host is not required.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"overridden"` - `"parsed"` - `"gathered"` - `"rendered"` |

## [Notes](junos_hostname_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the device being managed.
> - This module works with connection `netconf`.
> - See [the Junos OS Platform Options](https://docs.ansible.com/ansible/latest/network/user_guide/platform_junos.html).
> - Tested against JunOS v18.4R1

## [Examples](junos_hostname_module.md#id5)

```yaml+jinja
# Using merged
#
# Before state
# ------------
#
# vagrant@vsrx# show system hostname
#
# [edit]
- name: Merge provided HOSTNAME configuration into running configuration.
  junipernetworks.junos.junos_hostname:
    config:
      hostname: 'vsrx-18.4R1'
    state: merged
#
# -------------------------
# Module Execution Result
# -------------------------
#     "after": {
#         "hostname": "vsrx-18.4R1"
#     },
#     "before": {},
#     "changed": true,
#     "commands": [
#           "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#           "<nc:host-name>vsrx-18.4R1</nc:host-name></nc:system>"
#     ]
# After state
# -----------
#
# vagrant@vsrx-18.4R1# show system host-name
# host-name vsrx-18.4R1;
#
# Using replaced
#
# Before state
# ------------
#
# vagrant@vsrx-18.4R1# show system host-name
# host-name vsrx-18.4R1;
#
# [edit]
- name: Replaced target config with provided config.
  junipernetworks.junos.junos_hostname:
    config:
      hostname: 'vsrx-12'
    state: replaced
#
# -------------------------
# Module Execution Result
# -------------------------
#     "after": {
#         "hostname": "vsrx-12"
#     },
#     "before": {
#         "hostname": "vsrx-18.4R1"
#     },
#     "changed": true,
#     "commands": [
#           "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#           "<nc:host-name>vsrx-12</nc:host-name></nc:system>"
#     ]
# After state
# -----------
#
# vagrant@vsrx-18.4R1# show system host-name
# host-name vsrx-12;
#
# Using overridden
#
# Before state
# ------------
#
# vagrant@vsrx-18.4R1# show system host-name
# host-name vsrx-18.4R1;
#
# [edit]
- name: Replaced target config with provided config.
  junipernetworks.junos.junos_hostname:
    config:
      hostname: 'vsrx-12'
    state: overridden
#
# -------------------------
# Module Execution Result
# -------------------------
#     "after": {
#         "hostname": "vsrx-12"
#     },
#     "before": {
#         "hostname": "vsrx-18.4R1"
#     },
#     "changed": true,
#     "commands": [
#           "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#           "<nc:host-name>vsrx-12</nc:host-name></nc:system>"
#     ]
# After state
# -----------
#
# vagrant@vsrx-18.4R1# show system host-name
# host-name vsrx-12;
#
# Using deleted
#
# Before state
# ------------
#
# vagrant@vsrx-18.4R1# show system host-name
# host-name vsrx-12;
#
- name: Delete running HOSTNAME global configuration
  junipernetworks.junos.junos_hostname:
    config:
    state: deleted
#
# -------------------------
# Module Execution Result
# -------------------------
#     "after": {},
#     "before": {
#         "hostname": "vsrx-12"
#     },
#     "changed": true,
#     "commands": [
#               "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#                <nc:host-name delete="delete"/></nc:system>"
#     ]
# After state
# -----------
#
# vagrant@vsrx# show system ntp
#
# [edit]
# Using gathered
#
# Before state
# ------------
#
# vagrant@vsrx-18.4R1# show system host-name
# host-name vsrx-12;
#
- name: Gather running HOSTNAME global configuration
  junipernetworks.junos.junos_hostname:
    state: gathered
#
# -------------------------
# Module Execution Result
# -------------------------
#     "gathered": {
#         "hostname": "vsrx-12",
#     },
#     "changed": false,
# Using rendered
#
# Before state
# ------------
#
- name: Render xml for provided facts.
  junipernetworks.junos.junos_hostname:
    config:
      boot_server: '78.46.194.186'
    state: rendered
#
# -------------------------
# Module Execution Result
# -------------------------
#     "rendered": [
#           "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
#           "<nc:host-name>78.46.194.186</nc:host-name></nc:system>"
#     ]
#
# Using parsed
# parsed.cfg
# ------------
# <?xml version="1.0" encoding="UTF-8"?>
# <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
#     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
#         <version>18.4R1-S2.4</version>
#         <system xmlns="http://yang.juniper.net/junos-es/conf/system">
#            <host-name>vsrx-18.4R1</host-name>
#         </system>
#     </configuration>
# </rpc-reply>
#
- name: Parse HOSTNAME running config
  junipernetworks.junos.junos_hostname:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed":  {
#         "hostname": "vsrx-18.4R1"
#     }
#
```

## [Return Values](junos_hostname_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["\"<nc:host-name>78.46.194.186</nc:host-name></nc:system>\""]` |

### Authors

- Rohit Thakur (@rohitthakur2590)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
