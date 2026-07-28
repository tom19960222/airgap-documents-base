---
collection: ansible
version: "6"
title: "community.general.ipmi_boot module – Management of order of boot devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/ipmi_boot_module.html
fetched_at: 2026-07-27T17:10:03+00:00
---
# community.general.ipmi_boot module – Management of order of boot devices

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
> see [Requirements](ipmi_boot_module.md#ansible-collections-community-general-ipmi-boot-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.ipmi_boot`.

- [Synopsis](ipmi_boot_module.md#synopsis)
- [Requirements](ipmi_boot_module.md#requirements)
- [Parameters](ipmi_boot_module.md#parameters)
- [Examples](ipmi_boot_module.md#examples)
- [Return Values](ipmi_boot_module.md#return-values)

## [Synopsis](ipmi_boot_module.md#id1)

- Use this module to manage order of boot devices

## [Requirements](ipmi_boot_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- pyghmi

## [Parameters](ipmi_boot_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **bootdev**  string / required | Set boot device to use on next reboot  The choices for the device are: - network – Request network boot - floppy – Boot from floppy - hd – Boot from hard drive - safe – Boot from hard drive, requesting ‘safe mode’ - optical – boot from CD/DVD/BD drive - setup – Boot into setup utility - default – remove any IPMI directed boot device request  Choices:   - `"network"` - `"floppy"` - `"hd"` - `"safe"` - `"optical"` - `"setup"` - `"default"` |
| **key**  string  added in community.general 4.1.0 | Encryption key to connect to the BMC in hex format. |
| **name**  string / required | Hostname or ip address of the BMC. |
| **password**  string / required | Password to connect to the BMC. |
| **persistent**  boolean | If set, ask that system firmware uses this device beyond next boot. Be aware many systems do not honor this.  Choices:   - `false` ← (default) - `true` |
| **port**  integer | Remote RMCP port.  Default: `623` |
| **state**  string | Whether to ensure that boot devices is desired.  The choices for the state are: - present – Request system turn on - absent – Request system turn on  Choices:   - `"present"` ← (default) - `"absent"` |
| **uefiboot**  boolean | If set, request UEFI boot explicitly. Strictly speaking, the spec suggests that if not set, the system should BIOS boot and offers no “don’t care” option. In practice, this flag not being set does not preclude UEFI boot on any system I’ve encountered.  Choices:   - `false` ← (default) - `true` |
| **user**  string / required | Username to use to connect to the BMC. |

## [Examples](ipmi_boot_module.md#id4)

```yaml+jinja
- name: Ensure bootdevice is HD
  community.general.ipmi_boot:
    name: test.testdomain.com
    user: admin
    password: password
    bootdev: hd

- name: Ensure bootdevice is not Network
  community.general.ipmi_boot:
    name: test.testdomain.com
    user: admin
    password: password
    key: 1234567890AABBCCDEFF000000EEEE12
    bootdev: network
    state: absent
```

## [Return Values](ipmi_boot_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **bootdev**  string | The boot device name which will be used beyond next boot.  Returned: success  Sample: `"default"` |
| **persistent**  boolean | If True, system firmware will use this device beyond next boot.  Returned: success  Sample: `false` |
| **uefimode**  boolean | If True, system firmware will use UEFI boot explicitly beyond next boot.  Returned: success  Sample: `false` |

### Authors

- Bulat Gaifullin (@bgaifullin)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
