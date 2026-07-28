---
collection: ansible
version: "8"
title: "community.vmware.vmware_host_graphics module – Manage Host Graphic Settings"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_host_graphics_module.html
fetched_at: 2026-07-28T02:00:40+00:00
---
# community.vmware.vmware_host_graphics module – Manage Host Graphic Settings

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
> To use it in a playbook, specify: `community.vmware.vmware_host_graphics`.

New in community.vmware 3.10.0

- [Synopsis](vmware_host_graphics_module.md#synopsis)
- [Parameters](vmware_host_graphics_module.md#parameters)
- [Notes](vmware_host_graphics_module.md#notes)
- [Examples](vmware_host_graphics_module.md#examples)
- [Return Values](vmware_host_graphics_module.md#return-values)

## [Synopsis](vmware_host_graphics_module.md#id1)

- This module can be used to manage Host Graphic Settings

## [Parameters](vmware_host_graphics_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **assigment_policy**  string | Shared passthrough GPU assignment policy  **Choices:**   - `"consolidation"` - `"performance"` ← (default) |
| **cluster_name**  string | Name of cluster.  All host system from given cluster used to manage Host Graphic Settings.  Required parameter, if `esxi_hostname` is not set. |
| **esxi_hostname**  list / elements=string | List of ESXi hostname to manage Host Graphic Settings.  Required parameter, if `cluster_name` is not set. |
| **graphic_type**  string | Default graphics type  **Choices:**   - `"shared"` ← (default) - `"sharedDirect"` |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **restart_xorg**  boolean | Restart X.Org Server after change any parameter ( `graphic_type` or `assigment_policy` )  **Choices:**   - `false` ← (default) - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_host_graphics_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_host_graphics_module.md#id4)

```yaml+jinja
- name: Change Host Graphics Settings
  community.vmware.vmware_host_graphics:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    graphic_type: sharedDirect
    assigment_policy: consolidation
  delegate_to: localhost
```

## [Return Values](vmware_host_graphics_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **results**  dictionary | data about host system graphics settings.  **Returned:** always  **Sample:** `{"changed": true, "esxi01": {"changed": false, "msg": "All Host Graphics Settings already configured"}, "esxi02": {"changed": true, "msg": "New host graphics settings changed to: hostDefaultGraphicsType = 'shared', sharedPassthruAssignmentPolicy = 'performance'.X.Org was restarted"}}` |

### Authors

- Alexander Nikitin (@ihumster)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
