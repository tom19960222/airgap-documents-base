---
collection: ansible
version: "6"
title: "purestorage.flasharray.purefa_default_protection module – Manage SafeMode default protection for a Pure Storage FlashArray"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flasharray/purefa_default_protection_module.html
fetched_at: 2026-07-28T00:18:06+00:00
---
# purestorage.flasharray.purefa_default_protection module – Manage SafeMode default protection for a Pure Storage FlashArray

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
> see [Requirements](purefa_default_protection_module.md#ansible-collections-purestorage-flasharray-purefa-default-protection-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_default_protection`.

New in purestorage.flasharray 1.14.0

- [Synopsis](purefa_default_protection_module.md#synopsis)
- [Requirements](purefa_default_protection_module.md#requirements)
- [Parameters](purefa_default_protection_module.md#parameters)
- [Notes](purefa_default_protection_module.md#notes)
- [Examples](purefa_default_protection_module.md#examples)

## [Synopsis](purefa_default_protection_module.md#id1)

- Configure automatic protection group membership for new volumes and copied volumes array wide, or at the pod level.
- Requires a minimum of Purity 6.3.4

## [Requirements](purefa_default_protection_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_default_protection_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **name**  list / elements=string / required | The name of the protection group to assign or remove as default for the scope.  If *scope* is *pod* only the short-name for the pod protection group is needed. See examples |
| **pod**  string | name of the pod to apply the default protection to.  Only required for *scope* is *pod* |
| **scope**  string | The scope of the default protection group  Choices:   - `"array"` ← (default) - `"pod"` |
| **state**  string | Define whether to add or delete the protection group to the default list  Choices:   - `"absent"` - `"present"` ← (default) |

## [Notes](purefa_default_protection_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_default_protection_module.md#id5)

```yaml+jinja
- name: Add protection group foo::bar as default for pod foo
  purestorage.flasharray.purefa_default_protection:
    name: bar
    pod: foo
    scope: pod
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Add protection group foo as default for array
  purestorage.flasharray.purefa_default_protection:
    name: foo
    scope: array
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Remove protection group foo from array default protection
  purestorage.flasharray.purefa_default_protection:
    name: foo
    scope: array
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: absent

- name: Clear default protection for the array
  purestorage.flasharray.purefa_volume_tags:
    name: ''
    scope: array
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: absent
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
[Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
[Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
[Communication](index.md#communication-for-purestorage-flasharray)
