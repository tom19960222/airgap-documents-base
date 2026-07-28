---
collection: ansible
version: "6"
title: "community.vmware.vmware_dvs_host module – Add or remove a host from distributed virtual switch"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_dvs_host_module.html
fetched_at: 2026-07-27T17:21:39+00:00
---
# community.vmware.vmware_dvs_host module – Add or remove a host from distributed virtual switch

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
> To use it in a playbook, specify: `community.vmware.vmware_dvs_host`.

- [Synopsis](vmware_dvs_host_module.md#synopsis)
- [Parameters](vmware_dvs_host_module.md#parameters)
- [Notes](vmware_dvs_host_module.md#notes)
- [Examples](vmware_dvs_host_module.md#examples)

## [Synopsis](vmware_dvs_host_module.md#id1)

- Manage a host system from distributed virtual switch.

## [Parameters](vmware_dvs_host_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **esxi_hostname**  string / required | The ESXi hostname. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **lag_uplinks**  list / elements=dictionary  added in community.vmware 1.12.0 | The ESXi hosts vmnics to use with specific LAGs.  Default: `[]` |
| **lag**  string / required | Name of the LAG. |
| **vmnics**  list / elements=string | The ESXi hosts vmnics to use with the LAG.  Default: `[]` |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | If the host should be present or absent attached to the vSwitch.  Choices:   - `"present"` ← (default) - `"absent"` |
| **switch_name**  string / required | The name of the Distributed vSwitch. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |
| **vendor_specific_config**  list / elements=dictionary | List of key, value dictionaries for the Vendor Specific Configuration. |
| **key**  string / required | Key of setting. |
| **value**  string / required | Value of setting. |
| **vmnics**  list / elements=string | The ESXi hosts vmnics to use with the Distributed vSwitch.  Default: `[]` |

## [Notes](vmware_dvs_host_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_dvs_host_module.md#id4)

```yaml+jinja
- name: Add Host to dVS
  community.vmware.vmware_dvs_host:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    switch_name: dvSwitch
    vmnics:
        - vmnic0
        - vmnic1
    state: present
  delegate_to: localhost

- name: Add vmnics to LAGs
  community.vmware.vmware_dvs_host:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    switch_name: dvSwitch
    lag_uplinks:
        - lag: lag1
          vmnics:
              - vmnic0
              - vmnic1
        - lag: lag2
          vmnics:
              - vmnic2
              - vmnic3
    state: present
  delegate_to: localhost

- name: Add Host to dVS/enable learnswitch (https://labs.vmware.com/flings/learnswitch)
  community.vmware.vmware_dvs_host:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    switch_name: dvSwitch
    vendor_specific_config:
        - key: com.vmware.netoverlay.layer1
          value: learnswitch
    vmnics:
        - vmnic0
        - vmnic1
    state: present
  delegate_to: localhost
```

### Authors

- Joseph Callen (@jcpowermac)
- Abhijeet Kasurde (@Akasurde)
- Joseph Andreatta (@vmwjoseph)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
