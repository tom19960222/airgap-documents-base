---
collection: ansible
version: "6"
title: "community.vmware.vcenter_license module – Manage VMware vCenter license keys"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vcenter_license_module.html
fetched_at: 2026-07-27T17:21:19+00:00
---
# community.vmware.vcenter_license module – Manage VMware vCenter license keys

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
> To use it in a playbook, specify: `community.vmware.vcenter_license`.

- [Synopsis](vcenter_license_module.md#synopsis)
- [Parameters](vcenter_license_module.md#parameters)
- [Notes](vcenter_license_module.md#notes)
- [Examples](vcenter_license_module.md#examples)
- [Return Values](vcenter_license_module.md#return-values)

## [Synopsis](vcenter_license_module.md#id1)

- Add and delete vCenter, ESXi server license keys.

## [Parameters](vcenter_license_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster_name**  string | Name of the cluster to apply vSAN license. |
| **datacenter**  string | The datacenter name to use for the operation. |
| **esxi_hostname**  string | The hostname of the ESXi server to which the specified license will be assigned.  This parameter is optional. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable supported added in Ansible 2.6. |
| **labels**  dictionary | The optional labels of the license key to manage in vSphere vCenter.  This is dictionary with key/value pair.  Default: `{"source": "ansible"}` |
| **license**  string / required | The license key to manage in vSphere vCenter. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable supported added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable supported added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead. |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | Whether to add (`present`) or remove (`absent`) the license key.  Choices:   - `"absent"` - `"present"` ← (default) |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable supported added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable supported added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vcenter_license_module.md#id3)

> **Note:**
>
> - This module will also auto-assign the current vCenter to the license key if the product matches the license key, and vCenter us currently assigned an evaluation license only.
> - The evaluation license (00000-00000-00000-00000-00000) is not listed when unused.
> - If `esxi_hostname` is specified, then will assign the `license` key to the ESXi host.
> - If `esxi_hostname` is not specified, then will just register the `license` key to vCenter inventory without assigning it to an ESXi host.
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vcenter_license_module.md#id4)

```yaml+jinja
- name: Add a new vCenter license
  community.vmware.vcenter_license:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    license: f600d-21ae3-5592b-249e0-cc341
    state: present
  delegate_to: localhost

- name: Remove an (unused) vCenter license
  community.vmware.vcenter_license:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    license: f600d-21ae3-5592b-249e0-cc341
    state: absent
  delegate_to: localhost

- name: Add ESXi license and assign to the ESXi host
  community.vmware.vcenter_license:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    license: f600d-21ae3-5592b-249e0-dd502
    state: present
  delegate_to: localhost

- name: Add vSAN license and assign to the given cluster
  community.vmware.vcenter_license:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: '{{ datacenter_name }}'
    cluster_name: '{{ cluster_name }}'
    license: f600d-21ae3-5592b-249e0-dd502
    state: present
  delegate_to: localhost
```

## [Return Values](vcenter_license_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **licenses**  list / elements=string | list of license keys after module executed  Returned: always  Sample: `["f600d-21ae3-5592b-249e0-cc341", "143cc-0e942-b2955-3ea12-d006f"]` |

### Authors

- Dag Wieers (@dagwieers)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
