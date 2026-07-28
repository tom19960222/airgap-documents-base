---
collection: ansible
version: "8"
title: "community.vmware.vmware_guest_customization_info module – Gather info about VM customization specifications"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_guest_customization_info_module.html
fetched_at: 2026-07-28T02:00:10+00:00
---
# community.vmware.vmware_guest_customization_info module – Gather info about VM customization specifications

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
> To use it in a playbook, specify: `community.vmware.vmware_guest_customization_info`.

- [Synopsis](vmware_guest_customization_info_module.md#synopsis)
- [Parameters](vmware_guest_customization_info_module.md#parameters)
- [Notes](vmware_guest_customization_info_module.md#notes)
- [Examples](vmware_guest_customization_info_module.md#examples)
- [Return Values](vmware_guest_customization_info_module.md#return-values)

## [Synopsis](vmware_guest_customization_info_module.md#id1)

- This module can be used to gather information about customization specifications.
- All parameters and VMware object names are case sensitive.

## [Parameters](vmware_guest_customization_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **spec_name**  string | Name of customization specification to find. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_guest_customization_info_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_guest_customization_info_module.md#id4)

```yaml+jinja
- name: Gather info about all customization specification
  community.vmware.vmware_guest_customization_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
  delegate_to: localhost
  register: all_custom_spec_info

- name: Gather info about customization specification with the given name
  community.vmware.vmware_guest_customization_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    spec_name: custom_linux_spec
  delegate_to: localhost
  register: custom_spec_info
```

## [Return Values](vmware_guest_customization_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **custom_spec_info**  dictionary | metadata about the customization specification  **Returned:** always  **Sample:** `{"assignip-eee0d684-44b7-457c-8c55-2585590b0d99": {"change_version": "1523438001", "description": "sample description", "dns_server_list": [], "dns_suffix_list": [], "domain": "None", "hostname": "sample1", "hw_clock_utc": null, "last_updated_time": "2018-04-11T09:13:21+00:00", "name": "sample", "nic_setting_map": [{"dns_domain": null, "gateway": [], "ip_address": "192.168.10.10", "net_bios": null, "nic_dns_server_list": [], "primary_wins": null, "secondry_wins": null, "subnet_mask": "255.255.255.0"}], "time_zone": null, "type": "Linux"}}` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
