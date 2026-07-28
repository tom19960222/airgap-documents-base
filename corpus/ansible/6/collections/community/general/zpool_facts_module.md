---
collection: ansible
version: "6"
title: "community.general.zpool_facts module – Gather facts about ZFS pools"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/zpool_facts_module.html
fetched_at: 2026-07-27T17:14:13+00:00
---
# community.general.zpool_facts module – Gather facts about ZFS pools

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
> To use it in a playbook, specify: `community.general.zpool_facts`.

- [Synopsis](zpool_facts_module.md#synopsis)
- [Parameters](zpool_facts_module.md#parameters)
- [Examples](zpool_facts_module.md#examples)
- [Returned Facts](zpool_facts_module.md#returned-facts)
- [Return Values](zpool_facts_module.md#return-values)

## [Synopsis](zpool_facts_module.md#id1)

- Gather facts from ZFS pool properties.

## [Parameters](zpool_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  aliases: pool, zpool  string | ZFS pool name. |
| **parsable**  boolean | Specifies if property values should be displayed in machine friendly format.  Choices:   - `false` ← (default) - `true` |
| **properties**  string | Specifies which dataset properties should be queried in comma-separated format. For more information about dataset properties, check zpool(1M) man page.  Default: `"all"` |

## [Examples](zpool_facts_module.md#id3)

```yaml+jinja
- name: Gather facts about ZFS pool rpool
  community.general.zpool_facts: pool=rpool

- name: Gather space usage about all imported ZFS pools
  community.general.zpool_facts: properties='free,size'

- name: Print gathered information
  ansible.builtin.debug:
    msg: 'ZFS pool {{ item.name }} has {{ item.free }} free space out of {{ item.size }}.'
  with_items: '{{ ansible_zfs_pools }}'
```

## [Returned Facts](zpool_facts_module.md#id4)

Facts returned by this module are added/updated in the `hostvars` host facts and can be referenced by name just like any other host fact. They do not need to be registered in order to use them.

| Key | Description |
| --- | --- |
| **ansible_zfs_pools**  string | ZFS pool facts  Returned: always  Sample: `"{'allocated': '3.46G', 'altroot': '-', 'autoexpand': 'off', 'autoreplace': 'off', 'bootfs': 'rpool/ROOT/openindiana', 'cachefile': '-', 'capacity': '6%', 'comment': '-', 'dedupditto': '0', 'dedupratio': '1.00x', 'delegation': 'on', 'expandsize': '-', 'failmode': 'wait', 'feature@async_destroy': 'enabled', 'feature@bookmarks': 'enabled', 'feature@edonr': 'enabled', 'feature@embedded_data': 'active', 'feature@empty_bpobj': 'active', 'feature@enabled_txg': 'active', 'feature@extensible_dataset': 'enabled', 'feature@filesystem_limits': 'enabled', 'feature@hole_birth': 'active', 'feature@large_blocks': 'enabled', 'feature@lz4_compress': 'active', 'feature@multi_vdev_crash_dump': 'enabled', 'feature@sha512': 'enabled', 'feature@skein': 'enabled', 'feature@spacemap_histogram': 'active', 'fragmentation': '3%', 'free': '46.3G', 'freeing': '0', 'guid': '15729052870819522408', 'health': 'ONLINE', 'leaked': '0', 'listsnapshots': 'off', 'name': 'rpool', 'readonly': 'off', 'size': '49.8G', 'version': '-'}"` |

## [Return Values](zpool_facts_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **name**  string | ZFS pool name  Returned: always  Sample: `"rpool"` |
| **parsable**  boolean | if parsable output should be provided in machine friendly format.  Returned: if ‘parsable’ is set to True  Sample: `true` |

### Authors

- Adam Števko (@xen0l)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
