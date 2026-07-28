---
collection: ansible
version: "6"
title: "purestorage.flasharray.purefa_hg module – Manage hostgroups on Pure Storage FlashArrays"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flasharray/purefa_hg_module.html
fetched_at: 2026-07-28T00:18:13+00:00
---
# purestorage.flasharray.purefa_hg module – Manage hostgroups on Pure Storage FlashArrays

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
> see [Requirements](purefa_hg_module.md#ansible-collections-purestorage-flasharray-purefa-hg-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_hg`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_hg_module.md#synopsis)
- [Requirements](purefa_hg_module.md#requirements)
- [Parameters](purefa_hg_module.md#parameters)
- [Notes](purefa_hg_module.md#notes)
- [Examples](purefa_hg_module.md#examples)

## [Synopsis](purefa_hg_module.md#id1)

- Create, delete or modifiy hostgroups on Pure Storage FlashArrays.

## [Requirements](purefa_hg_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_hg_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **host**  list / elements=string | List of existing hosts to add to hostgroup.  Note that hostnames are case-sensitive however FlashArray hostnames are unique and ignore case - you cannot have *hosta* and *hostA* |
| **hostgroup**  string / required | The name of the hostgroup. |
| **lun**  integer | LUN ID to assign to volume for hostgroup. Must be unique.  Only applicable when only one volume is specified for connection.  If not provided the ID will be automatically assigned.  Range for LUN ID is 1 to 4095. |
| **rename**  string  added in purestorage.flasharray 1.10.0 | New name of hostgroup |
| **state**  string | Define whether the hostgroup should exist or not.  Choices:   - `"absent"` - `"present"` ← (default) |
| **volume**  list / elements=string | List of existing volumes to add to hostgroup.  Note that volumes are case-sensitive however FlashArray volume names are unique and ignore case - you cannot have *volumea* and *volumeA* |

## [Notes](purefa_hg_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_hg_module.md#id5)

```yaml+jinja
- name: Create empty hostgroup
  purestorage.flasharray.purefa_hg:
    hostgroup: foo
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Add hosts and volumes to existing or new hostgroup
  purestorage.flasharray.purefa_hg:
    hostgroup: foo
    host:
      - host1
      - host2
    volume:
      - vol1
      - vol2
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Delete hosts and volumes from hostgroup
  purestorage.flasharray.purefa_hg:
    hostgroup: foo
    host:
      - host1
      - host2
    volume:
      - vol1
      - vol2
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: absent

# This will disconnect all hosts and volumes in the hostgroup
- name: Delete hostgroup
  purestorage.flasharray.purefa_hg:
    hostgroup: foo
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: absent

- name: Rename hostgroup
  purestorage.flasharray.purefa_hg:
    hostgroup: foo
    rename: bar
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create host group with hosts and volumes
  purestorage.flasharray.purefa_hg:
    hostgroup: bar
    host:
      - host1
      - host2
    volume:
      - vol1
      - vol2
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
```

### Authors

- Pure Storage ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
[Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
[Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
[Communication](index.md#communication-for-purestorage-flasharray)
