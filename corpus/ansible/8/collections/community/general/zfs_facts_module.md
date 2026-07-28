---
collection: ansible
version: "8"
title: "community.general.zfs_facts module – Gather facts about ZFS datasets"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/zfs_facts_module.html
fetched_at: 2026-07-28T01:51:39+00:00
---
# community.general.zfs_facts module – Gather facts about ZFS datasets

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.zfs_facts`.

- [Synopsis](zfs_facts_module.md#synopsis)
- [Parameters](zfs_facts_module.md#parameters)
- [Attributes](zfs_facts_module.md#attributes)
- [Examples](zfs_facts_module.md#examples)
- [Return Values](zfs_facts_module.md#return-values)

## [Synopsis](zfs_facts_module.md#id1)

- Gather facts from ZFS dataset properties.

Aliases: storage.zfs.zfs_facts

## [Parameters](zfs_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **depth**  integer | Specifies recursion depth.  **Default:** `0` |
| **name**  aliases: ds, dataset  string / required | ZFS dataset name. |
| **parsable**  boolean | Specifies if property values should be displayed in machine friendly format.  **Choices:**   - `false` ← (default) - `true` |
| **properties**  string | Specifies which dataset properties should be queried in comma-separated format. For more information about dataset properties, check zfs(1M) man page.  **Default:** `"all"` |
| **recurse**  boolean | Specifies if properties for any children should be recursively displayed.  **Choices:**   - `false` ← (default) - `true` |
| **type**  string | Specifies which datasets types to display. Multiple values have to be provided in comma-separated form.  **Choices:**   - `"all"` ← (default) - `"filesystem"` - `"volume"` - `"snapshot"` - `"bookmark"` |

## [Attributes](zfs_facts_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |
| **facts** | **Support:** **full** | Action returns an `ansible_facts` dictionary that will update existing host facts. |

## [Examples](zfs_facts_module.md#id4)

```yaml+jinja
- name: Gather facts about ZFS dataset rpool/export/home
  community.general.zfs_facts:
    dataset: rpool/export/home

- name: Report space usage on ZFS filesystems under data/home
  community.general.zfs_facts:
    name: data/home
    recurse: true
    type: filesystem

- ansible.builtin.debug:
    msg: 'ZFS dataset {{ item.name }} consumes {{ item.used }} of disk space.'
  with_items: '{{ ansible_zfs_datasets }}'
```

## [Return Values](zfs_facts_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **name**  string | ZFS dataset name  **Returned:** always  **Sample:** `"rpool/var/spool"` |
| **parsable**  boolean | if parsable output should be provided in machine friendly format.  **Returned:** if ‘parsable’ is set to True  **Sample:** `true` |
| **recurse**  boolean | if we should recurse over ZFS dataset  **Returned:** if ‘recurse’ is set to True  **Sample:** `true` |
| **zfs_datasets**  string | ZFS dataset facts  **Returned:** always  **Sample:** `"{'aclinherit': 'restricted', 'aclmode': 'discard', 'atime': 'on', 'available': '43.8G', 'canmount': 'on', 'casesensitivity': 'sensitive', 'checksum': 'on', 'compression': 'off', 'compressratio': '1.00x', 'copies': '1', 'creation': 'Thu Jun 16 11:37 2016', 'dedup': 'off', 'devices': 'on', 'exec': 'on', 'filesystem_count': 'none', 'filesystem_limit': 'none', 'logbias': 'latency', 'logicalreferenced': '18.5K', 'logicalused': '3.45G', 'mlslabel': 'none', 'mounted': 'yes', 'mountpoint': '/rpool', 'name': 'rpool', 'nbmand': 'off', 'normalization': 'none', 'org.openindiana.caiman:install': 'ready', 'primarycache': 'all', 'quota': 'none', 'readonly': 'off', 'recordsize': '128K', 'redundant_metadata': 'all', 'refcompressratio': '1.00x', 'referenced': '29.5K', 'refquota': 'none', 'refreservation': 'none', 'reservation': 'none', 'secondarycache': 'all', 'setuid': 'on', 'sharenfs': 'off', 'sharesmb': 'off', 'snapdir': 'hidden', 'snapshot_count': 'none', 'snapshot_limit': 'none', 'sync': 'standard', 'type': 'filesystem', 'used': '4.41G', 'usedbychildren': '4.41G', 'usedbydataset': '29.5K', 'usedbyrefreservation': '0', 'usedbysnapshots': '0', 'utf8only': 'off', 'version': '5', 'vscan': 'off', 'written': '29.5K', 'xattr': 'on', 'zoned': 'off'}"` |

### Authors

- Adam Števko (@xen0l)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
