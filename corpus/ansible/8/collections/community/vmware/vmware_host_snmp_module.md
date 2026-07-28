---
collection: ansible
version: "8"
title: "community.vmware.vmware_host_snmp module – Configures SNMP on an ESXi host system"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_host_snmp_module.html
fetched_at: 2026-07-28T02:00:54+00:00
---
# community.vmware.vmware_host_snmp module – Configures SNMP on an ESXi host system

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/ui/repo/published/community/vmware/) (version 3.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
>
> To use it in a playbook, specify: `community.vmware.vmware_host_snmp`.

- [Synopsis](vmware_host_snmp_module.md#synopsis)
- [Parameters](vmware_host_snmp_module.md#parameters)
- [Notes](vmware_host_snmp_module.md#notes)
- [Examples](vmware_host_snmp_module.md#examples)
- [Return Values](vmware_host_snmp_module.md#return-values)

## [Synopsis](vmware_host_snmp_module.md#id1)

- This module can be used to configure the embedded SNMP agent on an ESXi host.

## [Parameters](vmware_host_snmp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster_name**  string  *added in community.vmware 3.11.0* | Name of cluster.  All host system from given cluster used to manage SNMP agent.  Required parameter, if `esxi_hostname` is not set. |
| **community**  list / elements=string | List of SNMP community strings.  **Default:** `[]` |
| **esxi_hostname**  list / elements=string  *added in community.vmware 3.11.0* | List of ESXi hostname to manage SNMP agent.  Required parameter, if `cluster_name` is not set. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **hw_source**  string | Source hardware events from IPMI sensors or CIM Indications.  The embedded SNMP agent receives hardware events either from IPMI sensors `sensors` or CIM indications `indications`.  **Choices:**   - `"indications"` ← (default) - `"sensors"` |
| **log_level**  string | Syslog logging level.  **Choices:**   - `"debug"` - `"info"` ← (default) - `"warning"` - `"error"` |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **send_trap**  boolean | Send a test trap to validate the configuration.  **Choices:**   - `false` ← (default) - `true` |
| **snmp_port**  integer | Port used by the SNMP agent.  **Default:** `161` |
| **state**  string | Enable, disable, or reset the SNMP agent.  **Choices:**   - `"disabled"` ← (default) - `"enabled"` - `"reset"` |
| **sys_contact**  string | System contact who manages the system. |
| **sys_location**  string | System location. |
| **trap_filter**  list / elements=string | A list of trap oids for traps not to be sent by agent, e.g. [ 1.3.6.1.4.1.6876.4.1.1.0, 1.3.6.1.4.1.6876.4.1.1.1 ]  Use value `reset` to clear settings. |
| **trap_targets**  list / elements=dictionary | A list of trap targets.  You need to use `hostname`, `port`, and `community` for each trap target.  **Default:** `[]` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_host_snmp_module.md#id3)

> **Note:**
>
> - You need to reset the agent (to factory defaults) if you want to clear all community strings, trap targets, or filters
> - SNMP v3 configuration isn’t implemented yet
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_host_snmp_module.md#id4)

```yaml+jinja
- name: Enable and configure SNMP community on standalone ESXi host
  community.vmware.vmware_host_snmp:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    community: [ test ]
    state: enabled
  delegate_to: localhost

- name: Configure SNMP traps and filters on cluster
  community.vmware.vmware_host_snmp:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
    community: [ test ]
    trap_targets:
      - hostname: 192.168.1.100
        port: 162
        community: test123
      - hostname: 192.168.1.101
        port: 162
        community: test1234
    trap_filter:
      - 1.3.6.1.4.1.6876.4.1.1.0
      - 1.3.6.1.4.1.6876.4.1.1.1
    state: enabled
  delegate_to: localhost

- name: Enable and configure SNMP system contact and location on simple ESXi host in vCenter
  community.vmware.vmware_host_snmp:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    sys_contact: "admin@testemail.com"
    sys_location: "Austin, USA"
    state: enabled
  delegate_to: localhost

- name: Disable SNMP on standalone ESXi host
  community.vmware.vmware_host_snmp:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    state: disabled
  delegate_to: localhost
```

## [Return Values](vmware_host_snmp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **results**  dictionary | metadata about host system’s SNMP configuration  **Returned:** always  **Sample:** `{"changed": true, "esx01.example.local": {"changed": true, "community": ["test"], "community_previous": [], "hw_source": "indications", "log_level": "info", "log_level_previous": "warning", "msg": "SNMP state, community list, log level, sys contact, and sys location changed", "port": 161, "state": "enabled", "state_previous": "disabled", "sys_contact_previous": "", "sys_location_previous": "", "trap_filter": null, "trap_targets": []}, "failed": false}` |

### Authors

- Christian Kotte (@ckotte)
- Alexander Nikitin (@ihumster)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
