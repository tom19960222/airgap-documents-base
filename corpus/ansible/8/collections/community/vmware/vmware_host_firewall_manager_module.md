---
collection: ansible
version: "8"
title: "community.vmware.vmware_host_firewall_manager module – Manage firewall configurations about an ESXi host"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_host_firewall_manager_module.html
fetched_at: 2026-07-28T02:00:40+00:00
---
# community.vmware.vmware_host_firewall_manager module – Manage firewall configurations about an ESXi host

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
> To use it in a playbook, specify: `community.vmware.vmware_host_firewall_manager`.

- [Synopsis](vmware_host_firewall_manager_module.md#synopsis)
- [Parameters](vmware_host_firewall_manager_module.md#parameters)
- [Notes](vmware_host_firewall_manager_module.md#notes)
- [Examples](vmware_host_firewall_manager_module.md#examples)
- [Return Values](vmware_host_firewall_manager_module.md#return-values)

## [Synopsis](vmware_host_firewall_manager_module.md#id1)

- This module can be used to manage firewall configurations about an ESXi host when ESXi hostname or Cluster name is given.

## [Parameters](vmware_host_firewall_manager_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster_name**  string | Name of the cluster.  Firewall settings are applied to every ESXi host system in given cluster.  If `esxi_hostname` is not given, this parameter is required. |
| **esxi_hostname**  string | ESXi hostname.  Firewall settings are applied to this ESXi host system.  If `cluster_name` is not given, this parameter is required. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **rules**  list / elements=dictionary | A list of Rule set which needs to be managed.  Each member of list is rule set name and state to be set the rule.  Both rule name and rule state are required parameters.  Additional IPs and networks can also be specified  Please see examples for more information.  **Default:** `[]` |
| **allowed_hosts**  dictionary | Define the allowed hosts for this rule set. |
| **all_ip**  boolean / required | Whether all hosts should be allowed or not.  **Choices:**   - `false` - `true` |
| **ip_address**  list / elements=string | List of allowed IP addresses.  **Default:** `[]` |
| **ip_network**  list / elements=string | List of allowed IP networks.  **Default:** `[]` |
| **enabled**  boolean / required | Whether the rule set is enabled or not.  **Choices:**   - `false` - `true` |
| **name**  string / required | Rule set name. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_host_firewall_manager_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_host_firewall_manager_module.md#id4)

```yaml+jinja
- name: Enable vvold rule set for all ESXi Host in given Cluster
  community.vmware.vmware_host_firewall_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: cluster_name
    rules:
        - name: vvold
          enabled: true
          allowed_hosts:
            all_ip: true
  delegate_to: localhost

- name: Enable vvold rule set for an ESXi Host
  community.vmware.vmware_host_firewall_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    rules:
        - name: vvold
          enabled: true
          allowed_hosts:
            all_ip: true
  delegate_to: localhost

- name: Manage multiple rule set for an ESXi Host
  community.vmware.vmware_host_firewall_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    rules:
        - name: vvold
          enabled: true
          allowed_hosts:
            all_ip: true
        - name: CIMHttpServer
          enabled: false
  delegate_to: localhost

- name: Manage IP and network based firewall permissions for ESXi
  community.vmware.vmware_host_firewall_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    rules:
        - name: gdbserver
          enabled: true
          allowed_hosts:
            all_ip: false
            ip_address:
              - 192.168.20.10
              - 192.168.20.11
        - name: CIMHttpServer
          enabled: true
          allowed_hosts:
            all_ip: false
            ip_network:
              - 192.168.100.0/24
        - name: remoteSerialPort
          enabled: true
          allowed_hosts:
            all_ip: false
            ip_address:
              - 192.168.100.11
            ip_network:
              - 192.168.200.0/24
  delegate_to: localhost
```

## [Return Values](vmware_host_firewall_manager_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **rule_set_state**  dictionary | dict with hostname as key and dict with firewall rule set facts as value  **Returned:** success  **Sample:** `{"rule_set_state": {"localhost.localdomain": {"CIMHttpServer": {"allowed_hosts": {"current_allowed_all": true, "current_allowed_ip": [], "current_allowed_networks": [], "desired_allowed_all": true, "desired_allowed_ip": [], "desired_allowed_networks": [], "previous_allowed_all": true, "previous_allowed_ip": [], "previous_allowed_networks": []}, "current_state": false, "desired_state": false, "previous_state": true}, "remoteSerialPort": {"allowed_hosts": {"current_allowed_all": false, "current_allowed_ip": ["192.168.100.11"], "current_allowed_networks": ["192.168.200.0/24"], "desired_allowed_all": false, "desired_allowed_ip": ["192.168.100.11"], "desired_allowed_networks": ["192.168.200.0/24"], "previous_allowed_all": true, "previous_allowed_ip": [], "previous_allowed_networks": []}, "current_state": true, "desired_state": true, "previous_state": true}}}}` |

### Authors

- Abhijeet Kasurde (@Akasurde)
- Aaron Longchamps (@alongchamps)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
