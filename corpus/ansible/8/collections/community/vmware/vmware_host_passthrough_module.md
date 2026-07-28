---
collection: ansible
version: "8"
title: "community.vmware.vmware_host_passthrough module – Manage PCI device passthrough settings on host"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_host_passthrough_module.html
fetched_at: 2026-07-28T02:00:50+00:00
---
# community.vmware.vmware_host_passthrough module – Manage PCI device passthrough settings on host

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
> To use it in a playbook, specify: `community.vmware.vmware_host_passthrough`.

- [Synopsis](vmware_host_passthrough_module.md#synopsis)
- [Parameters](vmware_host_passthrough_module.md#parameters)
- [Notes](vmware_host_passthrough_module.md#notes)
- [Examples](vmware_host_passthrough_module.md#examples)
- [Return Values](vmware_host_passthrough_module.md#return-values)

## [Synopsis](vmware_host_passthrough_module.md#id1)

- This module can be managed PCI device passthrough settings on host.

## [Parameters](vmware_host_passthrough_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster**  aliases: cluster_name  string | Name of the cluster from which all host systems will be used.  This parameter is required if `esxi_hostname` is not specified. |
| **devices**  list / elements=dictionary / required | List of PCI device name or id. |
| **device**  aliases: name, device_name  string | Name of PCI device to enable passthrough. |
| **esxi_hostname**  string | Name of the host system to work with.  This parameter is required if `cluster_name` is not specified.  User can specify specific host from the cluster. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | If *state=present*, passthrough of PCI device will be enabled.  If *state=absent*, passthrough of PCI device will be disabled.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_host_passthrough_module.md#id3)

> **Note:**
>
> - Supports `check_mode`.
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_host_passthrough_module.md#id4)

```yaml+jinja
- name: Enable PCI device passthrough against the whole ESXi in a cluster
  community.vmware.vmware_host_passthrough:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    cluster: "{{ ccr1 }}"
    devices:
      - device_name: "Dual Band Wireless AC 3165"
    state: present

- name: Enable PCI device passthrough against one ESXi
  community.vmware.vmware_host_passthrough:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    esxi_hostname: "{{ esxi1 }}"
    devices:
      - device_name: "Dual Band Wireless AC 3165"
    state: present

- name: Enable PCI device passthrough with PCI ids
  community.vmware.vmware_host_passthrough:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    esxi_hostname: "{{ esxi1 }}"
    devices:
      - device: '0000:03:00.0'
      - device: '0000:00:02.0'
    state: present

- name: Disable PCI device passthrough against the whole ESXi in a cluster
  community.vmware.vmware_host_passthrough:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    cluster: "{{ ccr1 }}"
    devices:
      - device_name: "Dual Band Wireless AC 3165"
    state: absent
```

## [Return Values](vmware_host_passthrough_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **passthrough_configs**  list / elements=dictionary | list of that PCI devices have been enabled passthrough for each host system.  **Returned:** changed  **Sample:** `"[\n    {\n        \"esxi-01.example.com\": [\n            {\n                \"device_id\": \"0000:03:00.0\",\n                \"device_name\": \"Dual Band Wireless AC 3165\",\n                \"passthruEnabled\": true\n            }\n        ]\n    },\n    {\n        \"esxi-02.example.com\": [\n            {\n                \"device_id\": \"0000:03:00.0\",\n                \"device_name\": \"Dual Band Wireless AC 3165\",\n                \"passthruEnabled\": true\n            }\n        ]\n    }\n]"` |

### Authors

- sky-joker (@sky-joker)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
