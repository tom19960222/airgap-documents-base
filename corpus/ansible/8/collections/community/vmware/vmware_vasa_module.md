---
collection: ansible
version: "8"
title: "community.vmware.vmware_vasa module – Manage VMware Virtual Volumes storage provider"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_vasa_module.html
fetched_at: 2026-07-28T02:01:13+00:00
---
# community.vmware.vmware_vasa module – Manage VMware Virtual Volumes storage provider

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
> To use it in a playbook, specify: `community.vmware.vmware_vasa`.

New in community.vmware 3.8.0

- [Synopsis](vmware_vasa_module.md#synopsis)
- [Parameters](vmware_vasa_module.md#parameters)
- [Notes](vmware_vasa_module.md#notes)
- [See Also](vmware_vasa_module.md#see-also)
- [Examples](vmware_vasa_module.md#examples)

## [Synopsis](vmware_vasa_module.md#id1)

- This module can be used to register and unregister a VASA provider

## [Parameters](vmware_vasa_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | Create `present` or remove `absent` a VASA provider.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |
| **vasa_certificate**  string | The SSL certificate of the VASA provider.  This parameter is required if *state=present* |
| **vasa_name**  string / required | The name of the VASA provider to be managed. |
| **vasa_password**  string | The password of the user account to connect to the VASA provider.  This parameter is required if *state=present* |
| **vasa_url**  string / required | The url of the VASA provider to be managed.  This parameter is required if *state=present* |
| **vasa_username**  string | The user account to connect to the VASA provider.  This parameter is required if *state=present* |

## [Notes](vmware_vasa_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [See Also](vmware_vasa_module.md#id4)

> **See also:**
>
> [community.vmware.vmware_vasa_info](vmware_vasa_info_module.md#ansible-collections-community-vmware-vmware-vasa-info-module)
> :   Gather information about vSphere VASA providers.

## [Examples](vmware_vasa_module.md#id5)

```yaml+jinja
- name: Create Cluster
  community.vmware.vmware_cluster:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    vasa_name: "{{ vasa_name }}"
    vasa_url: "{{ vasa_url }}"
    vasa_username: "{{ vasa_username }}"
    vasa_password: "{{ vasa_password }}"
    vasa_certificate: "{{ vasa_certificate }}"
    state: present
  delegate_to: localhost

- name: Unregister VASA provider
  community.vmware.vmware_vasa:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    vasa_name: "{{ vasa_name }}"
    state: absent
  delegate_to: localhost
```

### Authors

- Eugenio Grosso (@genegr)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
