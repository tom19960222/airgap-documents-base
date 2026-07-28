---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_snap module – Manage volume snapshots on Pure Storage FlashArrays"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_snap_module.html
fetched_at: 2026-07-28T02:51:26+00:00
---
# purestorage.flasharray.purefa_snap module – Manage volume snapshots on Pure Storage FlashArrays

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
> see [Requirements](purefa_snap_module.md#ansible-collections-purestorage-flasharray-purefa-snap-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_snap`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_snap_module.md#synopsis)
- [Requirements](purefa_snap_module.md#requirements)
- [Parameters](purefa_snap_module.md#parameters)
- [Notes](purefa_snap_module.md#notes)
- [Examples](purefa_snap_module.md#examples)

## [Synopsis](purefa_snap_module.md#id1)

- Create or delete volumes and volume snapshots on Pure Storage FlashArray.

## [Requirements](purefa_snap_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_snap_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **eradicate**  boolean | Define whether to eradicate the snapshot on delete or leave in trash.  **Choices:**   - `false` ← (default) - `true` |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **ignore_repl**  boolean | Only valid for Purity//FA 6.1 or higher  If set to true, allow destruction/eradication of snapshots in use by replication.  If set to false, allow destruction/eradication of snapshots not in use by replication  **Choices:**   - `false` ← (default) - `true` |
| **name**  string / required | The name of the source volume. |
| **offload**  string | Only valid for Purity//FA 6.1 or higher  Name of offload target for the snapshot.  Target can be either another FlashArray or an Offload Target  This is only applicable for creation, deletion and eradication of snapshots  *state* of *copy* is not supported. |
| **overwrite**  boolean | Define whether to overwrite existing volume when creating from snapshot.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | Define whether the volume snapshot should exist or not.  **Choices:**   - `"absent"` - `"copy"` - `"present"` ← (default) - `"rename"` |
| **suffix**  string | Suffix of snapshot name. |
| **target**  string | Name of target volume if creating from snapshot.  Name of new snapshot suffix if renaming a snapshot |
| **throttle**  boolean  *added in purestorage.flasharray 1.21.0* | If set to true, allows snapshot to fail if array health is not optimal.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](purefa_snap_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_snap_module.md#id5)

```yaml+jinja
- name: Create snapshot foo.ansible
  purestorage.flasharray.purefa_snap:
    name: foo
    suffix: ansible
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: present

- name: Create R/W clone foo_clone from snapshot foo.snap
  purestorage.flasharray.purefa_snap:
    name: foo
    suffix: snap
    target: foo_clone
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: copy

- name: Create R/W clone foo_clone from remote mnapshot arrayB:foo.snap
  purestorage.flasharray.purefa_snap:
    name: arrayB:foo
    suffix: snap
    target: foo_clone
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: copy

- name: Overwrite existing volume foo_clone with snapshot foo.snap
  purestorage.flasharray.purefa_snap:
    name: foo
    suffix: snap
    target: foo_clone
    overwrite: true
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: copy

- name: Delete and eradicate snapshot named foo.snap
  purestorage.flasharray.purefa_snap:
    name: foo
    suffix: snap
    eradicate: true
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: absent

- name: Rename snapshot foo.fred to foo.dave
  purestorage.flasharray.purefa_snap:
    name: foo
    suffix: fred
    target: dave
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: rename

- name: Create a remote volume snapshot on offload device arrayB
  purestorage.flasharray.purefa_snap:
    name: foo
    offload: arrayB
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Delete and eradicate a volume snapshot foo.1 on offload device arrayB
  purestorage.flasharray.purefa_snap:
    name: foo
    suffix: 1
    offload: arrayB
    eradicate: true
    state: absent
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
