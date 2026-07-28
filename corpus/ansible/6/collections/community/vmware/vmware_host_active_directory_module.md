---
collection: ansible
version: "6"
title: "community.vmware.vmware_host_active_directory module – Joins an ESXi host system to an Active Directory domain or leaves it"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_host_active_directory_module.html
fetched_at: 2026-07-27T17:22:11+00:00
---
# community.vmware.vmware_host_active_directory module – Joins an ESXi host system to an Active Directory domain or leaves it

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
> To use it in a playbook, specify: `community.vmware.vmware_host_active_directory`.

- [Synopsis](vmware_host_active_directory_module.md#synopsis)
- [Parameters](vmware_host_active_directory_module.md#parameters)
- [Notes](vmware_host_active_directory_module.md#notes)
- [Examples](vmware_host_active_directory_module.md#examples)
- [Return Values](vmware_host_active_directory_module.md#return-values)

## [Synopsis](vmware_host_active_directory_module.md#id1)

- This module can be used to join or leave an ESXi host to or from an Active Directory domain.

## [Parameters](vmware_host_active_directory_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **ad_domain**  aliases: domain, domain_name  string | AD Domain to join.  Default: `""` |
| **ad_password**  string | Password for AD domain join.  Default: `""` |
| **ad_state**  aliases: state  string | Whether the ESXi host is joined to an AD domain or not.  Choices:   - `"present"` - `"absent"` ← (default) |
| **ad_user**  string | Username for AD domain join.  Default: `""` |
| **cluster_name**  string | Name of the cluster from which all host systems will be used.  This parameter is required if `esxi_hostname` is not specified. |
| **esxi_hostname**  string | Name of the host system to work with.  This parameter is required if `cluster_name` is not specified. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_host_active_directory_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_host_active_directory_module.md#id4)

```yaml+jinja
- name: Join an AD domain
  community.vmware.vmware_host_active_directory:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    ad_domain: example.local
    ad_user: adjoin
    ad_password: Password123$
    ad_state: present
  delegate_to: localhost

- name: Leave AD domain
  community.vmware.vmware_host_active_directory:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    ad_state: absent
  delegate_to: localhost
```

## [Return Values](vmware_host_active_directory_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **results**  dictionary | metadata about host system’s AD domain join state  Returned: always  Sample: `{"esxi01": {"ad_state": "present", "ad_state_current": "present", "ad_state_previous": "absent", "changed": true, "domain": "example.local", "membership_state": "ok", "msg": "Host joined to AD domain"}}` |

### Authors

- Christian Kotte (@ckotte)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
