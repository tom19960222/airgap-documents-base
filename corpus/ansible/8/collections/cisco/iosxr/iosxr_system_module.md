---
collection: ansible
version: "8"
title: "cisco.iosxr.iosxr_system module – Module to manage the system attributes."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/iosxr/iosxr_system_module.html
fetched_at: 2026-07-28T01:27:00+00:00
---
# cisco.iosxr.iosxr_system module – Module to manage the system attributes.

> **Note:**
>
> This module is part of the [cisco.iosxr collection](https://galaxy.ansible.com/ui/repo/published/cisco/iosxr/) (version 5.0.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.iosxr`.
> You need further requirements to be able to use this module,
> see [Requirements](iosxr_system_module.md#ansible-collections-cisco-iosxr-iosxr-system-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.iosxr.iosxr_system`.

New in cisco.iosxr 1.0.0

- [Synopsis](iosxr_system_module.md#synopsis)
- [Requirements](iosxr_system_module.md#requirements)
- [Parameters](iosxr_system_module.md#parameters)
- [Notes](iosxr_system_module.md#notes)
- [Examples](iosxr_system_module.md#examples)
- [Return Values](iosxr_system_module.md#return-values)

## [Synopsis](iosxr_system_module.md#id1)

- This module provides declarative management of node system attributes on Cisco IOS XR devices. It provides an option to configure host system parameters or remove those parameters from the device active configuration.

Aliases: system

## [Requirements](iosxr_system_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient >= 0.5.3 when using netconf
- lxml >= 4.1.1 when using netconf

## [Parameters](iosxr_system_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **domain_name**  string | Configure the IP domain name on the remote device to the provided value. Value should be in the dotted name form and will be appended to the `hostname` to create a fully-qualified domain name. |
| **domain_search**  list / elements=string | Provides the list of domain suffixes to append to the hostname for the purpose of doing name resolution. This argument accepts a list of names and will be reconciled with the current active configuration on the running node. |
| **hostname**  string | Configure the device hostname parameter. This option takes an ASCII string value. |
| **lookup_enabled**  boolean | Provides administrative control for enabling or disabling DNS lookups. When this argument is set to True, lookups are performed and when it is set to False, lookups are not performed.  **Choices:**   - `false` - `true` ← (default) |
| **lookup_source**  string | The `lookup_source` argument provides one or more source interfaces to use for performing DNS lookups. The interface provided in `lookup_source` must be a valid interface configured on the device. |
| **name_servers**  list / elements=string | The `name_serves` argument accepts a list of DNS name servers by way of either FQDN or IP address to use to perform name resolution lookups. This argument accepts wither a list of DNS servers See examples. |
| **state**  string | State of the configuration values in the device’s current active configuration. When set to *present*, the values should be configured in the device active configuration and when set to *absent* the values should not be in the device active configuration  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **vrf**  string | VRF name for domain services  **Default:** `"default"` |

## [Notes](iosxr_system_module.md#id4)

> **Note:**
>
> - This module works with connection `network_cli` and `netconf`. See [the IOS-XR Platform Options](../network/user_guide/platform_iosxr.md).
> - name-servers *state=absent* operation with `netconf` transport is a success, but with rpc-error. This is due to XR platform issue. Recommended to use *ignore_errors* option with the task as a workaround.
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](iosxr_system_module.md#id5)

```yaml+jinja
- name: configure hostname and domain-name (default vrf=default)
  cisco.iosxr.iosxr_system:
    hostname: iosxr01
    domain_name: test.example.com
    domain_search:
    - ansible.com
    - redhat.com
    - cisco.com
- name: remove configuration
  cisco.iosxr.iosxr_system:
    hostname: iosxr01
    domain_name: test.example.com
    domain_search:
    - ansible.com
    - redhat.com
    - cisco.com
    state: absent
- name: configure hostname and domain-name with vrf
  cisco.iosxr.iosxr_system:
    hostname: iosxr01
    vrf: nondefault
    domain_name: test.example.com
    domain_search:
    - ansible.com
    - redhat.com
    - cisco.com
- name: configure DNS lookup sources
  cisco.iosxr.iosxr_system:
    lookup_source: MgmtEth0/0/CPU0/0
    lookup_enabled: true
- name: configure name servers
  cisco.iosxr.iosxr_system:
    name_servers:
    - 8.8.8.8
    - 8.8.4.4
```

## [Return Values](iosxr_system_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always  **Sample:** `["hostname iosxr01", "ip domain-name test.example.com"]` |
| **xml**  list / elements=string | NetConf rpc xml sent to device with transport `netconf`  **Returned:** always (empty list when no xml rpc to send)  **Sample:** `["<config xmlns:xc=\"urn:ietf:params:xml:ns:netconf:base:1.0\"> <ip-domain xmlns=\"http://cisco.com/ns/yang/Cisco-IOS-XR-ip-domain-cfg\"> <vrfs> <vrf> <vrf-name>default</vrf-name> <lists> <list xc:operation=\"merge\"> <order>0</order> <list-name>redhat.com</list-name> </list> </lists> </vrf> </vrfs> </ip-domain> </config>"]` |

### Authors

- Peter Sprygada (@privateip)
- Kedar Kekan (@kedarX)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
