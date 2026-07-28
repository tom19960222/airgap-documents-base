---
collection: ansible
version: "6"
title: "purestorage.flasharray.purefa_timeout module – Configure Pure Storage FlashArray GUI idle timeout"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flasharray/purefa_timeout_module.html
fetched_at: 2026-07-28T00:18:32+00:00
---
# purestorage.flasharray.purefa_timeout module – Configure Pure Storage FlashArray GUI idle timeout

> **Note:**
>
> This module is part of the [purestorage.flasharray collection](https://galaxy.ansible.com/purestorage/flasharray) (version 1.15.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flasharray`.
> You need further requirements to be able to use this module,
> see [Requirements](purefa_timeout_module.md#ansible-collections-purestorage-flasharray-purefa-timeout-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_timeout`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_timeout_module.md#synopsis)
- [Requirements](purefa_timeout_module.md#requirements)
- [Parameters](purefa_timeout_module.md#parameters)
- [Notes](purefa_timeout_module.md#notes)
- [Examples](purefa_timeout_module.md#examples)

## [Synopsis](purefa_timeout_module.md#id1)

- Configure GUI idle timeout for Pure Storage FlashArrays.
- This does not affect existing GUI sessions.

## [Requirements](purefa_timeout_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_timeout_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **state**  string | Set or disable the GUI idle timeout  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | Minutes for idle timeout.  Default: `30` |

## [Notes](purefa_timeout_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_timeout_module.md#id5)

```yaml+jinja
- name: Set GUI idle timeout to 25 minutes
  purestorage.flasharray.purefa_timeout:
    timeout: 25
    state: present
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Disable idle timeout
  purestorage.flasharray.purefa_timeout:
    state: absent
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
[Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
[Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
[Communication](index.md#communication-for-purestorage-flasharray)
