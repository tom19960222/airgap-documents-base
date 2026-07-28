---
collection: ansible
version: "6"
title: "community.general.memset_memstore_info module – Retrieve Memstore product usage information"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/memset_memstore_info_module.html
fetched_at: 2026-07-27T17:10:55+00:00
---
# community.general.memset_memstore_info module – Retrieve Memstore product usage information

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.memset_memstore_info`.

- [Synopsis](memset_memstore_info_module.md#synopsis)
- [Parameters](memset_memstore_info_module.md#parameters)
- [Notes](memset_memstore_info_module.md#notes)
- [Examples](memset_memstore_info_module.md#examples)
- [Return Values](memset_memstore_info_module.md#return-values)

## [Synopsis](memset_memstore_info_module.md#id1)

- Retrieve Memstore product usage information.
- This module was called `memset_memstore_facts` before Ansible 2.9. The usage did not change.

## [Parameters](memset_memstore_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_key**  string / required | The API key obtained from the Memset control panel. |
| **name**  string / required | The Memstore product name (i.e. `mstestyaa1`). |

## [Notes](memset_memstore_info_module.md#id3)

> **Note:**
>
> - An API key generated via the Memset customer control panel is needed with the following minimum scope - *memstore.usage*.

## [Examples](memset_memstore_info_module.md#id4)

```yaml+jinja
- name: Get usage for mstestyaa1
  community.general.memset_memstore_info:
    name: mstestyaa1
    api_key: 5eb86c9896ab03919abcf03857163741
  delegate_to: localhost
```

## [Return Values](memset_memstore_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **memset_api**  complex | Info from the Memset API  Returned: always |
| **bandwidth**  complex | Dictionary of CDN bandwidth facts  Returned: always |
| **bytes_in**  integer | Inbound bandwidth for the last 24 hours in bytes  Returned: always  Sample: `1000` |
| **bytes_out**  integer | Outbound bandwidth for the last 24 hours in bytes  Returned: always  Sample: `1000` |
| **requests**  integer | Number of requests in the last 24 hours  Returned: always  Sample: `10` |
| **bytes**  integer | Space used in bytes  Returned: always  Sample: `3860997965` |
| **cdn_bandwidth**  complex | Dictionary of CDN bandwidth facts  Returned: always |
| **bytes_in**  integer | Inbound CDN bandwidth for the last 24 hours in bytes  Returned: always  Sample: `1000` |
| **bytes_out**  integer | Outbound CDN bandwidth for the last 24 hours in bytes  Returned: always  Sample: `1000` |
| **requests**  integer | Number of requests in the last 24 hours  Returned: always  Sample: `10` |
| **containers**  integer | Number of containers  Returned: always  Sample: `10` |
| **objs**  integer | Number of objects  Returned: always  Sample: `1000` |

### Authors

- Simon Weald (@glitchcrab)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
