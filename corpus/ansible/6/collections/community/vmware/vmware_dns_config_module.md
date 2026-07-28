---
collection: ansible
version: "6"
title: "community.vmware.vmware_dns_config module – Manage VMware ESXi DNS Configuration"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_dns_config_module.html
fetched_at: 2026-07-27T17:21:35+00:00
---
# community.vmware.vmware_dns_config module – Manage VMware ESXi DNS Configuration

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
> To use it in a playbook, specify: `community.vmware.vmware_dns_config`.

- [DEPRECATED](vmware_dns_config_module.md#deprecated)
- [Synopsis](vmware_dns_config_module.md#synopsis)
- [Parameters](vmware_dns_config_module.md#parameters)
- [Notes](vmware_dns_config_module.md#notes)
- [Examples](vmware_dns_config_module.md#examples)
- [Status](vmware_dns_config_module.md#status)

## [DEPRECATED](vmware_dns_config_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Will be replaced with new module [community.vmware.vmware_host_dns](vmware_host_dns_module.md#ansible-collections-community-vmware-vmware-host-dns-module).

Alternative:
:   Use [community.vmware.vmware_host_dns](vmware_host_dns_module.md#ansible-collections-community-vmware-vmware-host-dns-module) instead.

## [Synopsis](vmware_dns_config_module.md#id2)

- Manage VMware ESXi DNS Configuration

## [Parameters](vmware_dns_config_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **change_hostname_to**  string / required | The hostname that an ESXi host should be changed to. |
| **dns_servers**  list / elements=string / required | The DNS servers that the host should be configured to use. |
| **domainname**  string / required | The domain the ESXi host should be apart of. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_dns_config_module.md#id4)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_dns_config_module.md#id5)

```yaml+jinja
- name: Configure ESXi hostname and DNS servers
  community.vmware.vmware_dns_config:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    change_hostname_to: esx01
    domainname: foo.org
    dns_servers:
        - 8.8.8.8
        - 8.8.4.4
  delegate_to: localhost
```

## [Status](vmware_dns_config_module.md#id6)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](vmware_dns_config_module.md#deprecated).

### Authors

- Joseph Callen (@jcpowermac)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
