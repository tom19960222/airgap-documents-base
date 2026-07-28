---
collection: ansible
version: "8"
title: "community.vmware.vcenter_domain_user_group_info module – Gather user or group information of a domain"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vcenter_domain_user_group_info_module.html
fetched_at: 2026-07-28T01:05:25+00:00
---
# community.vmware.vcenter_domain_user_group_info module – Gather user or group information of a domain

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
> To use it in a playbook, specify: `community.vmware.vcenter_domain_user_group_info`.

- [Synopsis](vcenter_domain_user_group_info_module.md#synopsis)
- [Parameters](vcenter_domain_user_group_info_module.md#parameters)
- [Notes](vcenter_domain_user_group_info_module.md#notes)
- [Examples](vcenter_domain_user_group_info_module.md#examples)
- [Return Values](vcenter_domain_user_group_info_module.md#return-values)

## [Synopsis](vcenter_domain_user_group_info_module.md#id1)

- This module can be used to gather information about user or group of a domain.

## [Parameters](vcenter_domain_user_group_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **belongs_to_group**  string | If a group existing, returned contains only users or groups that directly belong to the specified group. |
| **belongs_to_user**  string | If a user existing, returned contains only groups that directly contain the specified user. |
| **domain**  string | The *domain* to be specified searching.  **Default:** `"vsphere.local"` |
| **exact_match**  boolean | If *exact_match* is `true`, it indicates the *search_string* passed should match a user or group name exactly.  **Choices:**   - `false` ← (default) - `true` |
| **find_groups**  boolean | If *find_groups* is `true`, domain groups will be included in the result.  **Choices:**   - `false` - `true` ← (default) |
| **find_users**  boolean | If *find_users* is `true`, domain users will be included in the result.  **Choices:**   - `false` - `true` ← (default) |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **search_string**  string / required | The *search_string* is a string to be specified searching.  Specify the domain user or group name to be searched. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vcenter_domain_user_group_info_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vcenter_domain_user_group_info_module.md#id4)

```yaml+jinja
- name: Gather all domain user and group of vsphere.local
  community.vmware.vcenter_domain_user_group_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    domain: vsphere.local
    search_string: ''
  register: gather_all_domain_user_group_result

- name: Gather all domain user and group included the administrator string
  community.vmware.vcenter_domain_user_group_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    domain: vsphere.local
    search_string: administrator
  register: gather_domain_user_group_result

- name: Gather all domain user of vsphere.local
  community.vmware.vcenter_domain_user_group_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    domain: vsphere.local
    search_string: ''
    find_users: true
    find_groups: false
  register: gather_all_domain_user_result

- name: Gather administrator user by exact match condition
  community.vmware.vcenter_domain_user_group_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    domain: vsphere.local
    search_string: "vsphere.local\\administrator"
    exact_match: true
  register: gather_administrator_user_exact_match_result
```

## [Return Values](vcenter_domain_user_group_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **domain_user_groups**  list / elements=string | list of domain user and group information  **Returned:** success  **Sample:** `["[\n    {\n        \"fullName\": \"Administrator vsphere.local\"", "\n        \"group\": false", "\n        \"principal\": \"Administrator\"\n    }\n]"]` |

### Authors

- sky-joker (@sky-joker)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
