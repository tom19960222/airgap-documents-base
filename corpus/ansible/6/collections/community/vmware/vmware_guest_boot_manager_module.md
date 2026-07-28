---
collection: ansible
version: "6"
title: "community.vmware.vmware_guest_boot_manager module – Manage boot options for the given virtual machine"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_guest_boot_manager_module.html
fetched_at: 2026-07-27T17:21:50+00:00
---
# community.vmware.vmware_guest_boot_manager module – Manage boot options for the given virtual machine

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
> To use it in a playbook, specify: `community.vmware.vmware_guest_boot_manager`.

- [Synopsis](vmware_guest_boot_manager_module.md#synopsis)
- [Parameters](vmware_guest_boot_manager_module.md#parameters)
- [Notes](vmware_guest_boot_manager_module.md#notes)
- [Examples](vmware_guest_boot_manager_module.md#examples)
- [Return Values](vmware_guest_boot_manager_module.md#return-values)

## [Synopsis](vmware_guest_boot_manager_module.md#id1)

- This module can be used to manage boot options for the given virtual machine.

## [Parameters](vmware_guest_boot_manager_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **boot_delay**  integer | Delay in milliseconds before starting the boot sequence.  Default: `0` |
| **boot_firmware**  string | Choose which firmware should be used to boot the virtual machine.  Choices:   - `"bios"` - `"efi"` |
| **boot_order**  list / elements=string | List of the boot devices.  Default: `[]` |
| **boot_retry_delay**  integer | Specify the time in milliseconds between virtual machine boot failure and subsequent attempt to boot again.  If set, will automatically set `boot_retry_enabled` to `True` as this parameter is required.  Default: `0` |
| **boot_retry_enabled**  boolean | If set to `True`, the virtual machine that fails to boot, will try to boot again after `boot_retry_delay` is expired.  If set to `False`, the virtual machine waits indefinitely for user intervention.  Choices:   - `false` ← (default) - `true` |
| **enter_bios_setup**  boolean | If set to `True`, the virtual machine automatically enters BIOS setup the next time it boots.  The virtual machine resets this flag, so that the machine boots proceeds normally.  Choices:   - `false` ← (default) - `true` |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **moid**  string | Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.  This is required if `name` or `uuid` is not supplied. |
| **name**  string | Name of the VM to work with.  This is required if `uuid` or `moid` parameter is not supplied. |
| **name_match**  string | If multiple virtual machines matching the name, use the first or last found.  Choices:   - `"first"` ← (default) - `"last"` |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **secure_boot_enabled**  boolean | Choose if EFI secure boot should be enabled. EFI secure boot can only be enabled with boot_firmware = efi  Choices:   - `false` ← (default) - `true` |
| **use_instance_uuid**  boolean | Whether to use the VMware instance UUID rather than the BIOS UUID.  Choices:   - `false` ← (default) - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **uuid**  string | UUID of the instance to manage if known, this is VMware’s BIOS UUID by default.  This is required if `name` or `moid` parameter is not supplied. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_guest_boot_manager_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_guest_boot_manager_module.md#id4)

```yaml+jinja
- name: Change virtual machine's boot order and related parameters
  community.vmware.vmware_guest_boot_manager:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    name: testvm
    boot_delay: 2000
    enter_bios_setup: True
    boot_retry_enabled: True
    boot_retry_delay: 22300
    boot_firmware: bios
    secure_boot_enabled: False
    boot_order:
      - floppy
      - cdrom
      - ethernet
      - disk
  delegate_to: localhost
  register: vm_boot_order

- name: Change virtual machine's boot order using Virtual Machine MoID
  community.vmware.vmware_guest_boot_manager:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    moid: vm-42
    boot_delay: 2000
    enter_bios_setup: True
    boot_retry_enabled: True
    boot_retry_delay: 22300
    boot_firmware: bios
    secure_boot_enabled: False
    boot_order:
      - floppy
      - cdrom
      - ethernet
      - disk
  delegate_to: localhost
  register: vm_boot_order
```

## [Return Values](vmware_guest_boot_manager_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vm_boot_status**  dictionary | metadata about boot order of virtual machine  Returned: always  Sample: `{"current_boot_delay": 2000, "current_boot_firmware": "bios", "current_boot_order": ["floppy", "disk", "ethernet", "cdrom"], "current_boot_retry_delay": 22300, "current_boot_retry_enabled": true, "current_enter_bios_setup": true, "current_secure_boot_enabled": false, "previous_boot_delay": 10, "previous_boot_firmware": "efi", "previous_boot_order": ["ethernet", "cdrom", "floppy", "disk"], "previous_boot_retry_delay": 10000, "previous_boot_retry_enabled": true, "previous_enter_bios_setup": false, "previous_secure_boot_enabled": true}` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
