---
collection: ansible
version: "8"
title: "vmware.vmware_rest.appliance_networking_interfaces_ipv4 module – Set IPv4 network configuration for specific network interface."
source_url: https://docs.ansible.com/projects/ansible/8/collections/vmware/vmware_rest/appliance_networking_interfaces_ipv4_module.html
fetched_at: 2026-07-28T02:57:20+00:00
---
# vmware.vmware_rest.appliance_networking_interfaces_ipv4 module – Set IPv4 network configuration for specific network interface.

> **Note:**
>
> This module is part of the [vmware.vmware_rest collection](https://galaxy.ansible.com/ui/repo/published/vmware/vmware_rest/) (version 2.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vmware.vmware_rest`.
> You need further requirements to be able to use this module,
> see [Requirements](appliance_networking_interfaces_ipv4_module.md#ansible-collections-vmware-vmware-rest-appliance-networking-interfaces-ipv4-module-requirements) for details.
>
> To use it in a playbook, specify: `vmware.vmware_rest.appliance_networking_interfaces_ipv4`.

New in vmware.vmware_rest 2.0.0

- [Synopsis](appliance_networking_interfaces_ipv4_module.md#synopsis)
- [Requirements](appliance_networking_interfaces_ipv4_module.md#requirements)
- [Parameters](appliance_networking_interfaces_ipv4_module.md#parameters)
- [Notes](appliance_networking_interfaces_ipv4_module.md#notes)
- [Examples](appliance_networking_interfaces_ipv4_module.md#examples)
- [Return Values](appliance_networking_interfaces_ipv4_module.md#return-values)

## [Synopsis](appliance_networking_interfaces_ipv4_module.md#id1)

- Set IPv4 network configuration for specific network interface.

## [Requirements](appliance_networking_interfaces_ipv4_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp

## [Parameters](appliance_networking_interfaces_ipv4_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **address**  string | The IPv4 address, for example, “10.20.80.191”. |
| **default_gateway**  string | The IPv4 address of the default gateway. This configures the global default gateway on the appliance with the specified gateway address and interface. This gateway replaces the existing default gateway configured on the appliance. However, if the gateway address is link-local, then it is added for that interface. This does not support configuration of multiple global default gateways through different interfaces. |
| **interface_name**  string / required | Network interface to update, for example, “nic0”. This parameter is mandatory. |
| **mode**  string / required | The `mode` defines different IPv4 address assignment modes. This parameter is mandatory.  **Choices:**   - `"DHCP"` - `"STATIC"` - `"UNCONFIGURED"` |
| **prefix**  integer | The IPv4 CIDR prefix, for example, 24. See <http://www.oav.net/mirrors/cidr.html> for netmask-to-prefix conversion. |
| **session_timeout**  float  *added in vmware.vmware_rest 2.1.0* | Timeout settings for client session.  The maximal number of seconds for the whole operation including connection establishment, request sending and response.  The default value is 300s. |
| **state**  string | **Choices:**   - `"set"` ← (default) |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of  environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](appliance_networking_interfaces_ipv4_module.md#id4)

> **Note:**
>
> - Tested on vSphere 7.0.2

## [Examples](appliance_networking_interfaces_ipv4_module.md#id5)

```yaml+jinja
- name: Set the IPv4 network information of nic99 (which does not exist)
  vmware.vmware_rest.appliance_networking_interfaces_ipv4:
    interface_name: nic99
    config:
      address: 10.20.80.191
      prefix: '32'
      mode: STATIC
  failed_when:
  - not(result.failed)
  - result.value.messages[0].default_message msg == "The interface is unknown."
  register: result
```

## [Return Values](appliance_networking_interfaces_ipv4_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **failed_when_result**  integer | Set the IPv4 network information of nic99 (which does not exist)  **Returned:** On success  **Sample:** `0` |
| **msg**  string | Set the IPv4 network information of nic99 (which does not exist)  **Returned:** On success  **Sample:** `"missing required arguments: mode"` |

### Authors

- Ansible Cloud Team (@ansible-collections)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
- [Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
