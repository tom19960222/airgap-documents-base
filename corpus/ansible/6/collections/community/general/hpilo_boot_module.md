---
collection: ansible
version: "6"
title: "community.general.hpilo_boot module – Boot system using specific media through HP iLO interface"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/hpilo_boot_module.html
fetched_at: 2026-07-27T17:09:21+00:00
---
# community.general.hpilo_boot module – Boot system using specific media through HP iLO interface

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](hpilo_boot_module.md#ansible-collections-community-general-hpilo-boot-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.hpilo_boot`.

- [Synopsis](hpilo_boot_module.md#synopsis)
- [Requirements](hpilo_boot_module.md#requirements)
- [Parameters](hpilo_boot_module.md#parameters)
- [Notes](hpilo_boot_module.md#notes)
- [Examples](hpilo_boot_module.md#examples)

## [Synopsis](hpilo_boot_module.md#id1)

- This module boots a system through its HP iLO interface. The boot media can be one of: cdrom, floppy, hdd, network or usb.
- This module requires the hpilo python module.

## [Requirements](hpilo_boot_module.md#id2)

The below requirements are needed on the host that executes this module.

- python-hpilo

## [Parameters](hpilo_boot_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **force**  boolean | Whether to force a reboot (even when the system is already booted).  As a safeguard, without force, hpilo_boot will refuse to reboot a server that is already running.  Choices:   - `false` ← (default) - `true` |
| **host**  string / required | The HP iLO hostname/address that is linked to the physical system. |
| **image**  string | The URL of a cdrom, floppy or usb boot media image. protocol://username:password@hostname:port/filename  protocol is either ‘http’ or ‘https’  username:password is optional  port is optional |
| **login**  string | The login name to authenticate to the HP iLO interface.  Default: `"Administrator"` |
| **media**  string | The boot media to boot the system from  Choices:   - `"cdrom"` - `"floppy"` - `"rbsu"` - `"hdd"` - `"network"` - `"normal"` - `"usb"` |
| **password**  string | The password to authenticate to the HP iLO interface.  Default: `"admin"` |
| **ssl_version**  string | Change the ssl_version used.  Choices:   - `"SSLv3"` - `"SSLv23"` - `"TLSv1"` ← (default) - `"TLSv1_1"` - `"TLSv1_2"` |
| **state**  string | The state of the boot media.  no_boot: Do not boot from the device  boot_once: Boot from the device once and then notthereafter  boot_always: Boot from the device each time the server is rebooted  connect: Connect the virtual media device and set to boot_always  disconnect: Disconnects the virtual media device and set to no_boot  poweroff: Power off the server  Choices:   - `"boot_always"` - `"boot_once"` ← (default) - `"connect"` - `"disconnect"` - `"no_boot"` - `"poweroff"` |

## [Notes](hpilo_boot_module.md#id4)

> **Note:**
>
> - To use a USB key image you need to specify floppy as boot media.
> - This module ought to be run from a system that can access the HP iLO interface directly, either by using `local_action` or using `delegate_to`.

## [Examples](hpilo_boot_module.md#id5)

```yaml+jinja
- name: Task to boot a system using an ISO from an HP iLO interface only if the system is an HP server
  community.general.hpilo_boot:
    host: YOUR_ILO_ADDRESS
    login: YOUR_ILO_LOGIN
    password: YOUR_ILO_PASSWORD
    media: cdrom
    image: http://some-web-server/iso/boot.iso
  when: cmdb_hwmodel.startswith('HP ')
  delegate_to: localhost

- name: Power off a server
  community.general.hpilo_boot:
    host: YOUR_ILO_HOST
    login: YOUR_ILO_LOGIN
    password: YOUR_ILO_PASSWORD
    state: poweroff
  delegate_to: localhost
```

### Authors

- Dag Wieers (@dagwieers)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
