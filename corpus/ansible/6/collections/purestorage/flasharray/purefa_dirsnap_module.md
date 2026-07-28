---
collection: ansible
version: "6"
title: "purestorage.flasharray.purefa_dirsnap module – Manage FlashArray File System Directory Snapshots"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flasharray/purefa_dirsnap_module.html
fetched_at: 2026-07-28T00:18:07+00:00
---
# purestorage.flasharray.purefa_dirsnap module – Manage FlashArray File System Directory Snapshots

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
> see [Requirements](purefa_dirsnap_module.md#ansible-collections-purestorage-flasharray-purefa-dirsnap-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_dirsnap`.

New in purestorage.flasharray 1.9.0

- [Synopsis](purefa_dirsnap_module.md#synopsis)
- [Requirements](purefa_dirsnap_module.md#requirements)
- [Parameters](purefa_dirsnap_module.md#parameters)
- [Notes](purefa_dirsnap_module.md#notes)
- [Examples](purefa_dirsnap_module.md#examples)

## [Synopsis](purefa_dirsnap_module.md#id1)

- Create/Delete FlashArray File System directory snapshots
- A full snapshot name is constructed in the form of DIR.CLIENT_NAME.SUFFIX where DIR is the managed directory name, CLIENT_NAME is the client name, and SUFFIX is the suffix.
- The client visible snapshot name is CLIENT_NAME.SUFFIX.

## [Requirements](purefa_dirsnap_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_dirsnap_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **client**  string / required | The client name portion of the client visible snapshot name |
| **eradicate**  boolean | Define whether to eradicate the snapshot on delete or leave in trash  Choices:   - `false` ← (default) - `true` |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **filesystem**  string / required | Name of the filesystem the directory links to. |
| **keep_for**  integer | Retention period, after which snapshots will be eradicated  Specify in seconds. Range 300 - 31536000 (5 minutes to 1 year)  Value of 0 will set no retention period.  If not specified on create will default to 0 (no retention period) |
| **name**  string / required | Name of the directory to snapshot |
| **new_client**  string  added in purestorage.flasharray 1.12.0 | The new client name when performing a rename |
| **new_suffix**  string  added in purestorage.flasharray 1.12.0 | The new suffix when performing a rename |
| **rename**  boolean  added in purestorage.flasharray 1.12.0 | Whether to rename a directory snapshot  The snapshot client name and suffix can be changed  Required with *new_client* ans *new_suffix*  Choices:   - `false` ← (default) - `true` |
| **state**  string | Define whether the directory snapshot should exist or not.  Choices:   - `"absent"` - `"present"` ← (default) |
| **suffix**  string | Snapshot suffix to use |

## [Notes](purefa_dirsnap_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_dirsnap_module.md#id5)

```yaml+jinja
- name: Create a snapshot direcotry foo in filesysten bar for client test with suffix test
  purestorage.flasharray.purefa_dirsnap:
    name: foo
    filesystem: bar
    client: test
    suffix: test
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Update retention time for a snapshot foo:bar.client.test
  purestorage.flasharray.purefa_dirsnap:
    name: foo
    filesystem: bar
    client: client
    suffix: test
    keep_for: 300 # 5 minutes
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Delete snapshot foo:bar.client.test
  purestorage.flasharray.purefa_dirsnap:
    name: foo
    filesystem: bar
    client: client
    suffix: test
    state: absent
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Recover deleted snapshot foo:bar.client.test
  purestorage.flasharray.purefa_dirsnap:
    name: foo
    filesystem: bar
    client: client
    suffix: test
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Delete and eradicate snapshot foo:bar.client.test
  purestorage.flasharray.purefa_dirsnap:
    name: foo
    filesystem: bar
    client: client
    suffix: test
    state: absent
    eradicate: true
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Eradicate deleted snapshot foo:bar.client.test
  purestorage.flasharray.purefa_dirsnap:
    name: foo
    filesystem: bar
    client: client
    suffix: test
    eradicate: true
    state: absent
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Rename snapshot
  purestorage.flasharray.purefa_dirsnap:
    name: foo
    filesystem: bar
    client: client
    suffix: test
    rename: true
    new_client: client2
    new_suffix: test2
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
