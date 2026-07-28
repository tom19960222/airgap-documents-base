---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_volume_tags module – Manage volume tags on Pure Storage FlashArrays"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_volume_tags_module.html
fetched_at: 2026-07-28T02:51:41+00:00
---
# purestorage.flasharray.purefa_volume_tags module – Manage volume tags on Pure Storage FlashArrays

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
> see [Requirements](purefa_volume_tags_module.md#ansible-collections-purestorage-flasharray-purefa-volume-tags-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_volume_tags`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_volume_tags_module.md#synopsis)
- [Requirements](purefa_volume_tags_module.md#requirements)
- [Parameters](purefa_volume_tags_module.md#parameters)
- [Notes](purefa_volume_tags_module.md#notes)
- [Examples](purefa_volume_tags_module.md#examples)

## [Synopsis](purefa_volume_tags_module.md#id1)

- Manage volume tags for volumes on Pure Storage FlashArray.
- Requires a minimum of Purity 6.0.0

## [Requirements](purefa_volume_tags_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_volume_tags_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **copyable**  boolean | Define whether the volume tags are inherited on volume copies.  **Choices:**   - `false` - `true` ← (default) |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **kvp**  list / elements=string / required | List of key value pairs to assign to the volume.  Seperate the key from the value using a colon (:) only.  All items in list will use *namespace* and *copyable* settings.  Maximum of 5 tags per volume  See examples for exact formatting requirements |
| **name**  string / required | The name of the volume. |
| **namespace**  string | The name of tag namespace  **Default:** `"default"` |
| **state**  string | Define whether the volume tag(s) should exist or not.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Notes](purefa_volume_tags_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_volume_tags_module.md#id5)

```yaml+jinja
- name: Create new tags in namespace test for volume foo
  purestorage.flasharray.purefa_volume_tags:
    name: foo
    namespace: test
    copyable: false
    kvp:
    - 'key1:value1'
    - 'key2:value2'
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Remove an existing tag in namespace test for volume foo
  purestorage.flasharray.purefa_volume_tags:
    name: foo
    namespace: test
    kvp:
    - 'key1:value1'
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: absent

- name: Update an existing tag in namespace test for volume foo
  purestorage.flasharray.purefa_volume_tags:
    name: foo
    namespace: test
    kvp:
    - 'key1:value2'
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: present
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
- [Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
- [Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
- [Communication](index.md#communication-for-purestorage-flasharray)
