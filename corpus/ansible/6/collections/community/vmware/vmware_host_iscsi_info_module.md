---
collection: ansible
version: "6"
title: "community.vmware.vmware_host_iscsi_info module – Gather iSCSI configuration information of ESXi host"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_host_iscsi_info_module.html
fetched_at: 2026-07-27T17:22:23+00:00
---
# community.vmware.vmware_host_iscsi_info module – Gather iSCSI configuration information of ESXi host

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
> To use it in a playbook, specify: `community.vmware.vmware_host_iscsi_info`.

- [Synopsis](vmware_host_iscsi_info_module.md#synopsis)
- [Parameters](vmware_host_iscsi_info_module.md#parameters)
- [Notes](vmware_host_iscsi_info_module.md#notes)
- [Examples](vmware_host_iscsi_info_module.md#examples)
- [Return Values](vmware_host_iscsi_info_module.md#return-values)

## [Synopsis](vmware_host_iscsi_info_module.md#id1)

- This module can be used to gather information about the iSCSI configuration of the ESXi host.

## [Parameters](vmware_host_iscsi_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **esxi_hostname**  string / required | The ESXi hostname on which to gather iSCSI settings. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_host_iscsi_info_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_host_iscsi_info_module.md#id4)

```yaml+jinja
- name: Gather iSCSI configuration information of ESXi host
  community.vmware.vmware_host_iscsi_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
  register: iscsi_info
```

## [Return Values](vmware_host_iscsi_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **detected_iscsi_drives**  list / elements=string | list of detected iSCSI drive  added from version 1.9.0  Returned: always  Sample: `["[\n    {\n        \"address\": [\n            \"192.168.0.57:3260\"\n        ]", "\n        \"canonical_name\": \"naa.60014055f198fb3d0cb4bd7ae1f802e1\"", "\n        \"iscsi_name\": \"iqn.2021-03.local.iscsi-target:iscsi-storage.target0\"\n    }\n]"]` |
| **iscsi_properties**  dictionary | dictionary of current iSCSI information  Returned: always  Sample: `{"iscsi_alias": "", "iscsi_authentication_properties": {"_vimtype": "vim.host.InternetScsiHba.AuthenticationProperties", "chapAuthEnabled": false, "chapAuthenticationType": "chapProhibited", "chapInherited": null, "chapName": "", "chapSecret": "XXXXXXXXX", "mutualChapAuthenticationType": "chapProhibited", "mutualChapInherited": null, "mutualChapName": "", "mutualChapSecret": "XXXXXXXXX"}, "iscsi_enabled": true, "iscsi_name": "iqn.1998-01.com.vmware:esxi-033f58ee", "iscsi_send_targets": [{"address": "192.168.0.1", "authenticationProperties": {"_vimtype": "vim.host.InternetScsiHba.AuthenticationProperties", "chapAuthEnabled": false, "chapAuthenticationType": "chapProhibited", "chapInherited": true, "chapName": "", "chapSecret": "XXXXXXXXX", "mutualChapAuthenticationType": "chapProhibited", "mutualChapInherited": true, "mutualChapName": "", "mutualChapSecret": "XXXXXXXXX"}, "port": 3260}], "iscsi_static_targets": [{"address": "192.168.0.1", "authenticationProperties": {"_vimtype": "vim.host.InternetScsiHba.AuthenticationProperties", "chapAuthEnabled": false, "chapAuthenticationType": "chapProhibited", "chapInherited": true, "chapName": "", "chapSecret": "XXXXXXXXX", "mutualChapAuthenticationType": "chapProhibited", "mutualChapInherited": true, "mutualChapName": "", "mutualChapSecret": "XXXXXXXXX"}, "iscsi_name": "iqn.2004-04.com.qnap:tvs-673:iscsi.vm3.2c580e", "port": 3260}], "port_bind": [], "vmhba_name": "vmhba65"}` |

### Authors

- sky-joker (@sky-joker)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
