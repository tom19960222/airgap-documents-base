---
collection: ansible
version: "8"
title: "community.vmware.vmware_vsan_hcl_db module – Manages the vSAN Hardware Compatibility List (HCL) database"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_vsan_hcl_db_module.html
fetched_at: 2026-07-28T02:01:26+00:00
---
# community.vmware.vmware_vsan_hcl_db module – Manages the vSAN Hardware Compatibility List (HCL) database

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/ui/repo/published/community/vmware/) (version 3.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
> You need further requirements to be able to use this module,
> see [Requirements](vmware_vsan_hcl_db_module.md#ansible-collections-community-vmware-vmware-vsan-hcl-db-module-requirements) for details.
>
> To use it in a playbook, specify: `community.vmware.vmware_vsan_hcl_db`.

New in community.vmware 3.5.0

- [Synopsis](vmware_vsan_hcl_db_module.md#synopsis)
- [Requirements](vmware_vsan_hcl_db_module.md#requirements)
- [Parameters](vmware_vsan_hcl_db_module.md#parameters)
- [Notes](vmware_vsan_hcl_db_module.md#notes)
- [Examples](vmware_vsan_hcl_db_module.md#examples)

## [Synopsis](vmware_vsan_hcl_db_module.md#id1)

- Manages vSAN HCL db on vSphere
- DB file can be downloaded from <https://partnerweb.vmware.com/service/vsan/all.json>

## [Requirements](vmware_vsan_hcl_db_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSAN Management SDK, which needs to be downloaded from VMware and installed manually.

## [Parameters](vmware_vsan_hcl_db_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **source**  string / required | The path to the HCL db file |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_vsan_hcl_db_module.md#id4)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_vsan_hcl_db_module.md#id5)

```yaml+jinja
- name: Fetch HCL db file
  ansible.builtin.get_url:
    url: https://partnerweb.vmware.com/service/vsan/all.json
    dest: hcl_db.json
    force: true
  delegate_to: localhost

- name: Upload HCL db file to vCenter
  community.vmware.vmware_vsan_hcl_db:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    source: hcl_db.json
  delegate_to: localhost
```

### Authors

- Philipp Fruck (@p-fruck)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
