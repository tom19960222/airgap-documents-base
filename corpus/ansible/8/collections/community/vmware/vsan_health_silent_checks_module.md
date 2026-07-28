---
collection: ansible
version: "8"
title: "community.vmware.vsan_health_silent_checks module – Silence vSAN health checks"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vsan_health_silent_checks_module.html
fetched_at: 2026-07-28T02:01:31+00:00
---
# community.vmware.vsan_health_silent_checks module – Silence vSAN health checks

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
> see [Requirements](vsan_health_silent_checks_module.md#ansible-collections-community-vmware-vsan-health-silent-checks-module-requirements) for details.
>
> To use it in a playbook, specify: `community.vmware.vsan_health_silent_checks`.

New in community.vmware 3.6.0

- [Synopsis](vsan_health_silent_checks_module.md#synopsis)
- [Requirements](vsan_health_silent_checks_module.md#requirements)
- [Parameters](vsan_health_silent_checks_module.md#parameters)
- [Notes](vsan_health_silent_checks_module.md#notes)
- [Examples](vsan_health_silent_checks_module.md#examples)

## [Synopsis](vsan_health_silent_checks_module.md#id1)

- Take a list of vSAN health checks and silence them
- Re-enable alerts for previously silenced health checks

## [Requirements](vsan_health_silent_checks_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSAN Management SDK, which needs to be downloaded from VMware and installed manually.

## [Parameters](vsan_health_silent_checks_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **checks**  list / elements=string | The checks to silence. |
| **cluster_name**  string / required | Name of the vSAN cluster. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | The state of the health checks.  If set to `present`, all given health checks will be silenced.  If set to `absent`, all given health checks will be removed from the list of silent checks.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vsan_health_silent_checks_module.md#id4)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vsan_health_silent_checks_module.md#id5)

```yaml+jinja
- name: Disable the vSAN Support Insight health check
  community.vmware.vsan_health_silent_checks:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    checks: vsanenablesupportinsight
    cluster_name: 'vSAN01'
  delegate_to: localhost

- name: Re-enable health check alerts for release catalog and HCL DB
  community.vmware.vsan_health_silent_checks:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    checks:
      - releasecataloguptodate
      - autohclupdate
    state: absent
    cluster_name: 'vSAN01'
  delegate_to: localhost
```

### Authors

- Philipp Fruck (@p-fruck)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
