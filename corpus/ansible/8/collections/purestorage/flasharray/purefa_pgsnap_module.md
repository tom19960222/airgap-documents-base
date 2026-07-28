---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_pgsnap module – Manage protection group snapshots on Pure Storage FlashArrays"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_pgsnap_module.html
fetched_at: 2026-07-28T02:51:14+00:00
---
# purestorage.flasharray.purefa_pgsnap module – Manage protection group snapshots on Pure Storage FlashArrays

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
> see [Requirements](purefa_pgsnap_module.md#ansible-collections-purestorage-flasharray-purefa-pgsnap-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_pgsnap`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_pgsnap_module.md#synopsis)
- [Requirements](purefa_pgsnap_module.md#requirements)
- [Parameters](purefa_pgsnap_module.md#parameters)
- [Notes](purefa_pgsnap_module.md#notes)
- [Examples](purefa_pgsnap_module.md#examples)

## [Synopsis](purefa_pgsnap_module.md#id1)

- Create or delete protection group snapshots on Pure Storage FlashArray.
- Recovery of replicated snapshots on the replica target array is enabled.
- Support for ActiveCluster and Volume Group protection groups is supported.

## [Requirements](purefa_pgsnap_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_pgsnap_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **apply_retention**  boolean | Apply retention schedule settings to the snapshot  **Choices:**   - `false` ← (default) - `true` |
| **eradicate**  boolean | Define whether to eradicate the snapshot on delete or leave in trash.  **Choices:**   - `false` ← (default) - `true` |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **name**  string / required | The name of the source protection group. |
| **now**  boolean | Whether to initiate a snapshot of the protection group immeadiately  **Choices:**   - `false` ← (default) - `true` |
| **offload**  string | Name of offload target on which the snapshot exists.  This is only applicable for deletion and erasure of snapshots |
| **overwrite**  boolean | Define whether to overwrite the target volume if it already exists.  **Choices:**   - `false` ← (default) - `true` |
| **remote**  boolean | Force immeadiate snapshot to remote targets  **Choices:**   - `false` ← (default) - `true` |
| **restore**  string | Restore a specific volume from a protection group snapshot.  The protection group name is not required. Only provide the name of the volume to be restored. |
| **state**  string | Define whether the protection group snapshot should exist or not. Copy (added in 2.7) will create a full read/write clone of the snapshot.  **Choices:**   - `"absent"` - `"present"` ← (default) - `"copy"` - `"rename"` |
| **suffix**  string | Suffix of snapshot name.  Special case. If *latest* the module will select the latest snapshot created in the group |
| **target**  string | Volume to restore a specified volume to.  If not supplied this will default to the volume defined in *restore*  Name of new snapshot suffix if renaming a snapshot |
| **throttle**  boolean  *added in purestorage.flasharray 1.21.0* | If set to true, allows snapshot to fail if array health is not optimal.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](purefa_pgsnap_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_pgsnap_module.md#id5)

```yaml+jinja
- name: Create protection group snapshot foo.ansible
  purestorage.flasharray.purefa_pgsnap:
    name: foo
    suffix: ansible
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: present

- name: Delete and eradicate protection group snapshot named foo.snap
  purestorage.flasharray.purefa_pgsnap:
    name: foo
    suffix: snap
    eradicate: true
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: absent

- name: Restore volume data from local protection group snapshot named foo.snap to volume data2
  purestorage.flasharray.purefa_pgsnap:
    name: foo
    suffix: snap
    restore: data
    target: data2
    overwrite: true
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: copy

- name: Restore remote protection group snapshot arrayA:pgname.snap.data to local copy
  purestorage.flasharray.purefa_pgsnap:
    name: arrayA:pgname
    suffix: snap
    restore: data
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: copy

- name: Restore AC pod  protection group snapshot pod1::pgname.snap.data to pdo1::data2
  purestorage.flasharray.purefa_pgsnap:
    name: pod1::pgname
    suffix: snap
    restore: data
    target: pod1::data2
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: copy

- name: Create snapshot of existing pgroup foo with suffix and force immeadiate copy to remote targets
  purestorage.flasharray.purefa_pgsnap:
    name: pgname
    suffix: force
    now: true
    apply_retention: true
    remote: true
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Delete and eradicate snapshot named foo.snap on offload target bar from arrayA
  purestorage.flasharray.purefa_pgsnap:
    name: "arrayA:foo"
    suffix: snap
    offload: bar
    eradicate: true
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: absent

- name: Rename protection group snapshot foo.fred to foo.dave
  purestorage.flasharray.purefa_pgsnap:
    name: foo
    suffix: fred
    target: dave
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: rename
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
- [Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
- [Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
- [Communication](index.md#communication-for-purestorage-flasharray)
