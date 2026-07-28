---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_smis module – Enable or disable FlashArray SMI-S features"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_smis_module.html
fetched_at: 2026-07-28T02:51:24+00:00
---
# purestorage.flasharray.purefa_smis module – Enable or disable FlashArray SMI-S features

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
> see [Requirements](purefa_smis_module.md#ansible-collections-purestorage-flasharray-purefa-smis-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_smis`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_smis_module.md#synopsis)
- [Requirements](purefa_smis_module.md#requirements)
- [Parameters](purefa_smis_module.md#parameters)
- [Notes](purefa_smis_module.md#notes)
- [Examples](purefa_smis_module.md#examples)

## [Synopsis](purefa_smis_module.md#id1)

- Enable or disable FlashArray SMI-S Provider and/or SLP

## [Requirements](purefa_smis_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_smis_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **slp**  boolean | Enable/Disable Service Locator Protocol  Ports used are TCP 427 and UDP 427  **Choices:**   - `false` - `true` ← (default) |
| **smis**  boolean | Enable/Disable SMI-S Provider  Port used is TCP 5989  **Choices:**   - `false` - `true` ← (default) |

## [Notes](purefa_smis_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_smis_module.md#id5)

```yaml+jinja
- name: Enable SMI-S and SLP
  purestorage.flasharray.purefa_smis:
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Disable SMI-S and SLP
  purestorage.flasharray.purefa_smis:
    smis: false
    slp: false
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
- [Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
- [Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
- [Communication](index.md#communication-for-purestorage-flasharray)
