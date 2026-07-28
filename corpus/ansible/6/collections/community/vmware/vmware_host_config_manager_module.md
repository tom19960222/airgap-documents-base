---
collection: ansible
version: "6"
title: "community.vmware.vmware_host_config_manager module – Manage advanced system settings of an ESXi host"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_host_config_manager_module.html
fetched_at: 2026-07-27T17:22:14+00:00
---
# community.vmware.vmware_host_config_manager module – Manage advanced system settings of an ESXi host

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/community/vmware) (version 2.10.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
>
> To use it in a playbook, specify: `community.vmware.vmware_host_config_manager`.

- [Synopsis](vmware_host_config_manager_module.md#synopsis)
- [Parameters](vmware_host_config_manager_module.md#parameters)
- [Notes](vmware_host_config_manager_module.md#notes)
- [Examples](vmware_host_config_manager_module.md#examples)

## [Synopsis](vmware_host_config_manager_module.md#id1)

- This module can be used to manage advanced system settings of an ESXi host when ESXi hostname or Cluster name is given.

## [Parameters](vmware_host_config_manager_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster_name**  string | Name of the cluster.  Settings are applied to every ESXi host in given cluster.  If `esxi_hostname` is not given, this parameter is required. |
| **esxi_hostname**  string | ESXi hostname.  Settings are applied to this ESXi host.  If `cluster_name` is not given, this parameter is required. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **options**  dictionary | A dictionary of advanced system settings.  Invalid options will cause module to error.  Note that the list of advanced options (with description and values) can be found by running `vim-cmd hostsvc/advopt/options`.  Default: `{}` |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_host_config_manager_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_host_config_manager_module.md#id4)

```yaml+jinja
- name: Manage Log level setting for all ESXi hosts in given Cluster
  community.vmware.vmware_host_config_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: cluster_name
    options:
        'Config.HostAgent.log.level': 'info'
  delegate_to: localhost

- name: Manage Log level setting for an ESXi host
  community.vmware.vmware_host_config_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    options:
        'Config.HostAgent.log.level': 'verbose'
  delegate_to: localhost

- name: Manage multiple settings for an ESXi host
  community.vmware.vmware_host_config_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    options:
        'Config.HostAgent.log.level': 'verbose'
        'Annotations.WelcomeMessage': 'Hello World'
        'Config.HostAgent.plugins.solo.enableMob': false
  delegate_to: localhost
```

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
