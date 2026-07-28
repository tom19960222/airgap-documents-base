---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_hardware module – Manage FlashArray Hardware Identification"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_hardware_module.html
fetched_at: 2026-07-28T02:50:59+00:00
---
# purestorage.flasharray.purefa_hardware module – Manage FlashArray Hardware Identification

> **Note:**
>
> This module is part of the [purestorage.flasharray collection](https://galaxy.ansible.com/ui/repo/published/purestorage/flasharray/) (version 1.24.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flasharray`.
> You need further requirements to be able to use this module,
> see [Requirements](purefa_hardware_module.md#ansible-collections-purestorage-flasharray-purefa-hardware-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_hardware`.

New in purestorage.flasharray 1.24.0

- [Synopsis](purefa_hardware_module.md#synopsis)
- [Requirements](purefa_hardware_module.md#requirements)
- [Parameters](purefa_hardware_module.md#parameters)
- [Notes](purefa_hardware_module.md#notes)
- [Examples](purefa_hardware_module.md#examples)

## [Synopsis](purefa_hardware_module.md#id1)

- Enable or disable FlashArray visual identification lights

## [Requirements](purefa_hardware_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_hardware_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **enabled**  boolean | State of the component identification LED  **Choices:**   - `false` - `true` |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **name**  string / required | Name of hardware component |

## [Notes](purefa_hardware_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_hardware_module.md#id5)

```yaml+jinja
- name: Enable identification LED
  purestorage.flasharray.purefa_hardware:
    name: "CH1.FB1"
    enabled: True
    fa_url: 10.10.10.2
    api_token: T-68618f31-0c9e-4e57-aa44-5306a2cf10e3

- name: Disable identification LED
  purestorage.flasharray.purefa_hardware:
    name: "CH1.FB1"
    enabled: False
    fa_url: 10.10.10.2
    api_token: T-68618f31-0c9e-4e57-aa44-5306a2cf10e3
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
- [Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
- [Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
- [Communication](index.md#communication-for-purestorage-flasharray)
