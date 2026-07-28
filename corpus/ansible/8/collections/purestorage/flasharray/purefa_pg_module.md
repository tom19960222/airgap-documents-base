---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_pg module – Manage protection groups on Pure Storage FlashArrays"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_pg_module.html
fetched_at: 2026-07-28T02:51:11+00:00
---
# purestorage.flasharray.purefa_pg module – Manage protection groups on Pure Storage FlashArrays

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
> see [Requirements](purefa_pg_module.md#ansible-collections-purestorage-flasharray-purefa-pg-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_pg`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_pg_module.md#synopsis)
- [Requirements](purefa_pg_module.md#requirements)
- [Parameters](purefa_pg_module.md#parameters)
- [Notes](purefa_pg_module.md#notes)
- [Examples](purefa_pg_module.md#examples)

## [Synopsis](purefa_pg_module.md#id1)

- Create, delete or modify protection groups on Pure Storage FlashArrays.
- If a protection group exists and you try to add non-valid types, eg. a host to a volume protection group the module will ignore the invalid types.
- Protection Groups on Offload targets are supported.

## [Requirements](purefa_pg_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_pg_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **enabled**  boolean | Define whether to enabled snapshots for the protection group.  **Choices:**   - `false` - `true` ← (default) |
| **eradicate**  boolean | Define whether to eradicate the protection group on delete and leave in trash.  **Choices:**   - `false` ← (default) - `true` |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **host**  list / elements=string | List of existing hosts to add to protection group.  Note that hostnames are case-sensitive however FlashArray hostnames are unique and ignore case - you cannot have *hosta* and *hostA* |
| **hostgroup**  list / elements=string | List of existing hostgroups to add to protection group.  Note that hostgroups are case-sensitive however FlashArray hostgroup names are unique and ignore case - you cannot have *groupa* and *groupA* |
| **name**  aliases: pgroup  string / required | The name of the protection group. |
| **rename**  string | Rename a protection group  If the source protection group is in a Pod or Volume Group ‘container’ you only need to provide the new protection group name in the same ‘container’ |
| **safe_mode**  boolean  *added in purestorage.flasharray 1.13.0* | Enables SafeMode restrictions on the protection group  **Once set disabling this can only be performed by Pure Technical Support**  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | Define whether the protection group should exist or not.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **target**  list / elements=string | List of remote arrays or offload target for replication protection group to connect to.  Note that all replicated protection groups are asynchronous.  Target arrays or offload targets must already be connected to the source array.  Maximum number of targets per Portection Group is 4, assuming your configuration suppors this. |
| **volume**  list / elements=string | List of existing volumes to add to protection group.  Note that volume are case-sensitive however FlashArray volume names are unique and ignore case - you cannot have *volumea* and *volumeA* |

## [Notes](purefa_pg_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_pg_module.md#id5)

```yaml+jinja
- name: Create new local protection group
  purestorage.flasharray.purefa_pg:
    name: foo
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create new protection group called bar in pod called foo
  purestorage.flasharray.purefa_pg:
    name: "foo::bar"
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create new replicated protection group
  purestorage.flasharray.purefa_pg:
    name: foo
    target:
      - arrayb
      - arrayc
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create new replicated protection group to offload target and remote array
  purestorage.flasharray.purefa_pg:
    name: foo
    target:
      - offload
      - arrayc
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create new protection group with snapshots disabled
  purestorage.flasharray.purefa_pg:
    name: foo
    enabled: false
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Delete protection group
  purestorage.flasharray.purefa_pg:
    name: foo
    eradicate: true
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: absent

- name: Eradicate protection group foo on offload target where source array is arrayA
  purestorage.flasharray.purefa_pg:
    name: "arrayA:foo"
    target: offload
    eradicate: true
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: absent

- name: Rename protection group foo in pod arrayA to bar
  purestorage.flasharray.purefa_pg:
    name: "arrayA::foo"
    rename: bar
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create protection group for hostgroups
  purestorage.flasharray.purefa_pg:
    name: bar
    hostgroup:
      - hg1
      - hg2
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create protection group for hosts
  purestorage.flasharray.purefa_pg:
    name: bar
    host:
      - host1
      - host2
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create replicated protection group for volumes
  purestorage.flasharray.purefa_pg:
    name: bar
    volume:
      - vol1
      - vol2
    target: arrayb
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
