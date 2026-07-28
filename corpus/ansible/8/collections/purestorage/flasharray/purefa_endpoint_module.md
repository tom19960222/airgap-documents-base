---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_endpoint module – Manage VMware protocol-endpoints on Pure Storage FlashArrays"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_endpoint_module.html
fetched_at: 2026-07-28T02:50:52+00:00
---
# purestorage.flasharray.purefa_endpoint module – Manage VMware protocol-endpoints on Pure Storage FlashArrays

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
> see [Requirements](purefa_endpoint_module.md#ansible-collections-purestorage-flasharray-purefa-endpoint-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_endpoint`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_endpoint_module.md#synopsis)
- [Requirements](purefa_endpoint_module.md#requirements)
- [Parameters](purefa_endpoint_module.md#parameters)
- [Notes](purefa_endpoint_module.md#notes)
- [Examples](purefa_endpoint_module.md#examples)
- [Return Values](purefa_endpoint_module.md#return-values)

## [Synopsis](purefa_endpoint_module.md#id1)

- Create, delete or eradicate the an endpoint on a Pure Storage FlashArray.

## [Requirements](purefa_endpoint_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_endpoint_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **eradicate**  boolean | Define whether to eradicate the endpoint on delete or leave in trash.  **Choices:**   - `false` ← (default) - `true` |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **hgroup**  string | name of hostgroup to attach endpoint to |
| **host**  string | name of host to attach endpoint to |
| **name**  string / required | The name of the endpoint. |
| **rename**  string | Value to rename the specified endpoint to.  Rename only applies to the container the current endpoint is in. |
| **state**  string | Define whether the endpoint should exist or not.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Notes](purefa_endpoint_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_endpoint_module.md#id5)

```yaml+jinja
- name: Create new endpoint named foo
  purestorage.flasharray.purefa_endpoint:
    name: test-endpoint
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: present

- name: Delete and eradicate endpoint named foo
  purestorage.flasharray.purefa_endpoint:
    name: foo
    eradicate: true
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: absent

- name: Rename endpoint foor to bar
  purestorage.flasharray.purefa_endpoint:
    name: foo
    rename: bar
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
```

## [Return Values](purefa_endpoint_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **volume**  dictionary | A dictionary describing the changed volume. Only some attributes below will be returned with various actions.  **Returned:** success |
| **created**  string | Volume creation time  **Returned:** success  **Sample:** `"2019-03-13T22:49:24Z"` |
| **name**  string | Volume name  **Returned:** success |
| **serial**  string | Volume serial number  **Returned:** success  **Sample:** `"361019ECACE43D83000120A4"` |
| **source**  string | Volume name of source volume used for volume copy  **Returned:** success |

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
- [Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
- [Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
- [Communication](index.md#communication-for-purestorage-flasharray)
