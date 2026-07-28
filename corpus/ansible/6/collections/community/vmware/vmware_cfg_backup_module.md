---
collection: ansible
version: "6"
title: "community.vmware.vmware_cfg_backup module – Backup / Restore / Reset ESXi host configuration"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_cfg_backup_module.html
fetched_at: 2026-07-27T17:21:22+00:00
---
# community.vmware.vmware_cfg_backup module – Backup / Restore / Reset ESXi host configuration

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
> To use it in a playbook, specify: `community.vmware.vmware_cfg_backup`.

- [Synopsis](vmware_cfg_backup_module.md#synopsis)
- [Parameters](vmware_cfg_backup_module.md#parameters)
- [Notes](vmware_cfg_backup_module.md#notes)
- [Examples](vmware_cfg_backup_module.md#examples)
- [Return Values](vmware_cfg_backup_module.md#return-values)

## [Synopsis](vmware_cfg_backup_module.md#id1)

- This module can be used to perform various operations related to backup, restore and reset of ESXi host configuration.

## [Parameters](vmware_cfg_backup_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **dest**  path | The destination where the ESXi configuration bundle will be saved. The *dest* can be a folder or a file.  If *dest* is a folder, the backup file will be saved in the folder with the default filename generated from the ESXi server.  If *dest* is a file, the backup file will be saved with that filename. The file extension will always be .tgz. |
| **esxi_hostname**  string | Name of ESXi server. This is required only if authentication against a vCenter is done. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **src**  path | The file containing the ESXi configuration that will be restored. |
| **state**  string / required | If `saved`, the .tgz backup bundle will be saved in *dest*.  If `absent`, the host configuration will be reset to default values.  If `loaded`, the backup file in *src* will be loaded to the ESXi host rewriting the hosts settings.  Choices:   - `"saved"` - `"absent"` - `"loaded"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_cfg_backup_module.md#id3)

> **Note:**
>
> - Works only for ESXi hosts
> - For configuration load or reset, the host will be switched automatically to maintenance mode.
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_cfg_backup_module.md#id4)

```yaml+jinja
- name: Save the ESXi configuration locally by authenticating directly against the ESXi host
  community.vmware.vmware_cfg_backup:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    state: saved
    dest: /tmp/
  delegate_to: localhost

- name: Save the ESXi configuration locally by authenticating against the vCenter and selecting the ESXi host
  community.vmware.vmware_cfg_backup:
    hostname: '{{ vcenter_hostname }}'
    esxi_hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    state: saved
    dest: /tmp/
  delegate_to: localhost
```

## [Return Values](vmware_cfg_backup_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dest_file**  string | The full path of where the file holding the ESXi configurations was stored  Returned: changed  Sample: `"/tmp/configBundle-esxi.host.domain.tgz"` |

### Authors

- Andreas Nafpliotis (@nafpliot-ibm)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
