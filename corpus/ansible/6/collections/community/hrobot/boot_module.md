---
collection: ansible
version: "6"
title: "community.hrobot.boot module – Set boot configuration"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/hrobot/boot_module.html
fetched_at: 2026-07-27T17:15:50+00:00
---
# community.hrobot.boot module – Set boot configuration

> **Note:**
>
> This module is part of the [community.hrobot collection](https://galaxy.ansible.com/community/hrobot) (version 1.6.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.hrobot`.
>
> To use it in a playbook, specify: `community.hrobot.boot`.

New in community.hrobot 1.2.0

- [Synopsis](boot_module.md#synopsis)
- [Parameters](boot_module.md#parameters)
- [Attributes](boot_module.md#attributes)
- [See Also](boot_module.md#see-also)
- [Examples](boot_module.md#examples)
- [Return Values](boot_module.md#return-values)

## [Synopsis](boot_module.md#id1)

- Set the boot configuration for a dedicated server.

## [Parameters](boot_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hetzner_password**  string / required | The password for the Robot webservice user. |
| **hetzner_user**  string / required | The username for the Robot webservice user. |
| **install_cpanel**  dictionary | If this option is provided, a cPanel installation will be activated for the next boot.  Precisely one of *regular_boot*, *rescue*, *install_linux*, *install_vnc*, *install_windows*, *install_plesk*, and *install_cpanel* must be provided. |
| **arch**  integer | The architecture to use for the install.  Not all architectures are available for all distributions.  Defaults to `64`.  Choices:   - `32` - `64` |
| **dist**  string / required | The distribution to install. |
| **hostname**  string / required | The hostname. |
| **lang**  string / required | The language to use for the operating system. |
| **install_linux**  dictionary | If this option is provided, a Linux system install will be activated for the next boot.  Precisely one of *regular_boot*, *rescue*, *install_linux*, *install_vnc*, *install_windows*, *install_plesk*, and *install_cpanel* must be provided. |
| **arch**  integer | The architecture to use for the install.  Not all architectures are available for all distributions.  Defaults to `64`.  Choices:   - `32` - `64` |
| **authorized_keys**  list / elements=string | One or more SSH key fingerprints to equip the rescue system with.  Only fingerprints for SSH keys deposited in the Robot API can be used.  You can use the [community.hrobot.ssh_key_info](ssh_key_info_module.md#ansible-collections-community-hrobot-ssh-key-info-module) module to query the SSH keys you can use, and the [community.hrobot.ssh_key](ssh_key_module.md#ansible-collections-community-hrobot-ssh-key-module) module to add or update SSH keys. |
| **dist**  string / required | The distribution to install. |
| **lang**  string / required | The language to use for the operating system. |
| **install_plesk**  dictionary | If this option is provided, a Plesk installation will be activated for the next boot.  Precisely one of *regular_boot*, *rescue*, *install_linux*, *install_vnc*, *install_windows*, *install_plesk*, and *install_cpanel* must be provided. |
| **arch**  integer | The architecture to use for the install.  Not all architectures are available for all distributions.  Defaults to `64`.  Choices:   - `32` - `64` |
| **dist**  string / required | The distribution to install. |
| **hostname**  string / required | The hostname. |
| **lang**  string / required | The language to use for the operating system. |
| **install_vnc**  dictionary | If this option is provided, a VNC installation will be activated for the next boot.  Precisely one of *regular_boot*, *rescue*, *install_linux*, *install_vnc*, *install_windows*, *install_plesk*, and *install_cpanel* must be provided. |
| **arch**  integer | The architecture to use for the install.  Not all architectures are available for all distributions.  Defaults to `64`.  Choices:   - `32` - `64` |
| **dist**  string / required | The distribution to install. |
| **lang**  string / required | The language to use for the operating system. |
| **install_windows**  dictionary | If this option is provided, a Windows installation will be activated for the next boot.  Precisely one of *regular_boot*, *rescue*, *install_linux*, *install_vnc*, *install_windows*, *install_plesk*, and *install_cpanel* must be provided. |
| **lang**  string / required | The language to use for Windows. |
| **regular_boot**  boolean | If this option is provided, all special boot configurations are removed and the installed operating system will be booted up next (assuming it is bootable).  Precisely one of *regular_boot*, *rescue*, *install_linux*, *install_vnc*, *install_windows*, *install_plesk*, and *install_cpanel* must be provided.  Choices:   - `false` - `true` |
| **rescue**  dictionary | If this option is provided, the rescue system will be activated for the next boot.  Precisely one of *regular_boot*, *rescue*, *install_linux*, *install_vnc*, *install_windows*, *install_plesk*, and *install_cpanel* must be provided. |
| **arch**  integer | The architecture to use for the rescue system.  Not all architectures are available for all operating systems.  Defaults to `64`.  Choices:   - `32` - `64` |
| **authorized_keys**  list / elements=string | One or more SSH key fingerprints to equip the rescue system with.  Only fingerprints for SSH keys deposited in the Robot API can be used.  You can use the [community.hrobot.ssh_key_info](ssh_key_info_module.md#ansible-collections-community-hrobot-ssh-key-info-module) module to query the SSH keys you can use, and the [community.hrobot.ssh_key](ssh_key_module.md#ansible-collections-community-hrobot-ssh-key-module) module to add or update SSH keys. |
| **os**  string / required | The operating system to use for the rescue system. Possible choices can change over time.  Currently, `linux`, `linuxold`, `freebsd`, `freebsdold`, `freebsdax`, `freebsdbetaax`, `vkvm`, and `vkvmold` seem to be available. |
| **server_number**  integer / required | The server number of the server whose boot configuration to adjust. |

## [Attributes](boot_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | Action group: community.hrobot.robot  added in community.hrobot 1.6.0 | Use `group/community.hrobot.robot` in `module_defaults` to set defaults for this module. |
| **check_mode** | Support: full | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [See Also](boot_module.md#id4)

> **See also:**
>
> [community.hrobot.ssh_key](ssh_key_module.md#ansible-collections-community-hrobot-ssh-key-module)
> :   Add, remove or update SSH key
>
> [community.hrobot.ssh_key_info](ssh_key_info_module.md#ansible-collections-community-hrobot-ssh-key-info-module)
> :   Query information on SSH keys

## [Examples](boot_module.md#id5)

```yaml+jinja
- name: Disable all special boot configurations
  community.hrobot.boot:
    hetzner_user: foo
    hetzner_password: bar
    regular_boot: true

- name: Enable a rescue system (64bit Linux) for the next boot
  community.hrobot.boot:
    hetzner_user: foo
    hetzner_password: bar
    rescue:
      os: linux

- name: Enable a Linux install for the next boot
  community.hrobot.boot:
    hetzner_user: foo
    hetzner_password: bar
    install_linux:
      dist: CentOS 5.5 minimal
      lang: en
      authorized_keys:
        - 56:29:99:a4:5d:ed:ac:95:c1:f5:88:82:90:5d:dd:10
        - 15:28:b0:03:95:f0:77:b3:10:56:15:6b:77:22:a5:bb
```

## [Return Values](boot_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **configuration_type**  string | Describes the active boot configuration.  Returned: success  Can only return:   - `"regular_boot"` - `"rescue"` - `"install_linux"` - `"install_vnc"` - `"install_windows"` - `"install_plesk"` - `"install_cpanel"` |
| **password**  string | The root password for the active boot configuration, if available.  For non-rescue boot configurations, it is avised to change the root password as soon as possible.  Returned: success and if a boot configuration other than `regular_boot` is active |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.hrobot/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.hrobot)
[Submit a bug report](https://github.com/ansible-collections/community.hrobot/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.hrobot/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-hrobot)
