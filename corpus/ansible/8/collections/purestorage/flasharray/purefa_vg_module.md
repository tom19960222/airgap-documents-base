---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_vg module – Manage volume groups on Pure Storage FlashArrays"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_vg_module.html
fetched_at: 2026-07-28T02:51:34+00:00
---
# purestorage.flasharray.purefa_vg module – Manage volume groups on Pure Storage FlashArrays

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
> see [Requirements](purefa_vg_module.md#ansible-collections-purestorage-flasharray-purefa-vg-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_vg`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_vg_module.md#synopsis)
- [Requirements](purefa_vg_module.md#requirements)
- [Parameters](purefa_vg_module.md#parameters)
- [Notes](purefa_vg_module.md#notes)
- [Examples](purefa_vg_module.md#examples)

## [Synopsis](purefa_vg_module.md#id1)

- Create, delete or modify volume groups on Pure Storage FlashArrays.

## [Requirements](purefa_vg_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_vg_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **bw_qos**  string | Bandwidth limit for vgroup in M or G units. M will set MB/s G will set GB/s To clear an existing QoS setting use 0 (zero) |
| **count**  integer | Number of volume groups to be created in a multiple volume group creation  Only supported from Purity//FA v6.0.0 and higher |
| **digits**  integer | Number of digits to use for multiple volume group count. This will pad the index number with zeros where necessary  Only supported from Purity//FA v6.0.0 and higher  Range is between 1 and 10  **Default:** `1` |
| **eradicate**  boolean | Define whether to eradicate the volume group on delete and leave in trash.  **Choices:**   - `false` ← (default) - `true` |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **iops_qos**  string | IOPs limit for vgroup - use value or K or M K will mean 1000 M will mean 1000000 To clear an existing IOPs setting use 0 (zero) |
| **name**  string / required | The name of the volume group.  Multi-volume-group support available from Purity//FA 6.0.0 **\*\*\*NOTE\*\*\*** Manual deletion or eradication of individual volume groups created using multi-volume-group will cause idempotency to fail  Multi-volume-group support only exists for volume group creation |
| **priority_operator**  string  *added in purestorage.flasharray 1.13.0* | DMM Priority Adjustment operator  **Choices:**   - `"+"` ← (default) - `"-"` |
| **priority_value**  integer  *added in purestorage.flasharray 1.13.0* | DMM Priority Adjustment value  **Choices:**   - `0` ← (default) - `10` |
| **rename**  string  *added in purestorage.flasharray 1.22.0* | Value to rename the specified volume group to |
| **start**  integer | Number at which to start the multiple volume group creation index  Only supported from Purity//FA v6.0.0 and higher  **Default:** `0` |
| **state**  string | Define whether the volume group should exist or not.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **suffix**  string | Suffix string, if required, for multiple volume group create  Volume group names will be formed as *<name>#I<suffix>*, where *#* is a placeholder for the volume index See associated descriptions  Only supported from Purity//FA v6.0.0 and higher |

## [Notes](purefa_vg_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_vg_module.md#id5)

```yaml+jinja
- name: Create new volune group
  purestorage.flasharray.purefa_vg:
    name: foo
    bw_qos: 50M
    iops_qos: 100
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create 10 volune groups of pattern foo#bar with QoS
  purestorage.flasharray.purefa_vg:
    name: foo
    suffix: bar
    count: 10
    start: 10
    digits: 3
    bw_qos: 50M
    iops_qos: 100
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Update volune group QoS limits
  purestorage.flasharray.purefa_vg:
    name: foo
    bw_qos: 0
    iops_qos: 5555
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Update volune group DMM Priority Adjustment (Purity//FA 6.1.2+)
  purestorage.flasharray.purefa_vg:
    name: foo
    priority_operator: '-'
    priority_value: 10
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Destroy volume group
  purestorage.flasharray.purefa_vg:
    name: foo
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: absent

- name: Recover deleted volune group - no changes are made to the volume group on recovery
  purestorage.flasharray.purefa_vg:
    name: foo
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Destroy and Eradicate volume group
  purestorage.flasharray.purefa_vg:
    name: foo
    eradicate: true
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: absent

- name: Rename volume group foo to bar
  purestorage.flasharray.purefa_vg:
    name: foo
    rename: bar
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
