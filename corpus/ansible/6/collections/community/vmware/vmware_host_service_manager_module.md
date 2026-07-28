---
collection: ansible
version: "6"
title: "community.vmware.vmware_host_service_manager module – Manage services on a given ESXi host"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_host_service_manager_module.html
fetched_at: 2026-07-27T17:22:32+00:00
---
# community.vmware.vmware_host_service_manager module – Manage services on a given ESXi host

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
> To use it in a playbook, specify: `community.vmware.vmware_host_service_manager`.

- [Synopsis](vmware_host_service_manager_module.md#synopsis)
- [Parameters](vmware_host_service_manager_module.md#parameters)
- [Notes](vmware_host_service_manager_module.md#notes)
- [Examples](vmware_host_service_manager_module.md#examples)

## [Synopsis](vmware_host_service_manager_module.md#id1)

- This module can be used to manage (start, stop, restart) services on a given ESXi host.
- If cluster_name is provided, specified service will be managed on all ESXi host belonging to that cluster.
- If specific esxi_hostname is provided, then specified service will be managed on given ESXi host only.

## [Parameters](vmware_host_service_manager_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster_name**  string | Name of the cluster.  Service settings are applied to every ESXi host system/s in given cluster.  If `esxi_hostname` is not given, this parameter is required. |
| **esxi_hostname**  string | ESXi hostname.  Service settings are applied to this ESXi host system.  If `cluster_name` is not given, this parameter is required. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **service_name**  string / required | Name of Service to be managed. This is a brief identifier for the service, for example, ntpd, vxsyslogd etc.  This value should be a valid ESXi service name. |
| **service_policy**  string | Set of valid service policy strings.  If set `on`, then service should be started when the host starts up.  If set `automatic`, then service should run if and only if it has open firewall ports.  If set `off`, then Service should not be started when the host starts up.  Choices:   - `"automatic"` - `"off"` - `"on"` |
| **state**  string | Desired state of service.  State value ‘start’ and ‘present’ has same effect.  State value ‘stop’ and ‘absent’ has same effect.  State value `unchanged` is added in version 1.14.0 to allow defining startup policy without defining or changing service state.  Choices:   - `"absent"` - `"present"` - `"restart"` - `"start"` ← (default) - `"stop"` - `"unchanged"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_host_service_manager_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_host_service_manager_module.md#id4)

```yaml+jinja
- name: Start ntpd service setting for all ESXi Host in given Cluster
  community.vmware.vmware_host_service_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
    service_name: ntpd
    state: present
  delegate_to: localhost

- name: Start ntpd setting for an ESXi Host
  community.vmware.vmware_host_service_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    service_name: ntpd
    state: present
  delegate_to: localhost

- name: Start ntpd setting for an ESXi Host with Service policy
  community.vmware.vmware_host_service_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    service_name: ntpd
    service_policy: on
    state: present
  delegate_to: localhost

- name: Stop ntpd setting for an ESXi Host
  community.vmware.vmware_host_service_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    service_name: ntpd
    state: absent
  delegate_to: localhost
```

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
