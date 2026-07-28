---
collection: ansible
version: "6"
title: "ansible.builtin.fetch module – Fetch files from remote nodes"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/fetch_module.html
fetched_at: 2026-07-27T16:42:44+00:00
---
# ansible.builtin.fetch module – Fetch files from remote nodes

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `fetch` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](fetch_module.md#synopsis)
- [Parameters](fetch_module.md#parameters)
- [Attributes](fetch_module.md#attributes)
- [Notes](fetch_module.md#notes)
- [See Also](fetch_module.md#see-also)
- [Examples](fetch_module.md#examples)

## [Synopsis](fetch_module.md#id1)

- This module works like [ansible.builtin.copy](copy_module.md#ansible-collections-ansible-builtin-copy-module), but in reverse.
- It is used for fetching files from remote machines and storing them locally in a file tree, organized by hostname.
- Files that already exist at *dest* will be overwritten if they are different than the *src*.
- This module is also supported for Windows targets.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](fetch_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **dest**  string / required | A directory to save the file into.  For example, if the *dest* directory is `/backup` a *src* file named `/etc/profile` on host `host.example.com`, would be saved into `/backup/host.example.com/etc/profile`. The host name is based on the inventory name. |
| **fail_on_missing**  boolean | When set to `yes`, the task will fail if the remote file cannot be read for any reason.  Prior to Ansible 2.5, setting this would only fail if the source file was missing.  The default was changed to `yes` in Ansible 2.5.  Choices:   - `false` - `true` ← (default) |
| **flat**  boolean | Allows you to override the default behavior of appending hostname/path/to/file to the destination.  If `dest` ends with ‘/’, it will use the basename of the source file, similar to the copy module.  This can be useful if working with a single host, or if retrieving files that are uniquely named per host.  If using multiple hosts with the same filename, the file will be overwritten for each host.  Choices:   - `false` ← (default) - `true` |
| **src**  string / required | The file on the remote system to fetch.  This *must* be a file, not a directory.  Recursive fetching may be supported in a later release. |
| **validate_checksum**  boolean | Verify that the source and destination checksums match after the files are fetched.  Choices:   - `false` - `true` ← (default) |

## [Attributes](fetch_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | Support: full | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller |
| **async** | Support: none | Supports being used with the `async` keyword |
| **bypass_host_loop** | Support: none | Forces a ‘global’ task that does not execute per host, this bypasses per host templating and serial, throttle and other loop considerations  Conditionals will work as if `run_once` is being used, variables used will be from the first available host  This action will not work normally outside of lockstep strategies |
| **check_mode** | Support: full | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | Support: full | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | Platforms: posix, windows | Target OS/families that can be operated against |
| **safe_file_operations** | Support: none | Uses Ansible’s strict file operation functions to ensure proper permissions and avoid data corruption |
| **vault** | Support: none | Can automatically decrypt Ansible vaulted files |

## [Notes](fetch_module.md#id4)

> **Note:**
>
> - When running fetch with `become`, the [ansible.builtin.slurp](slurp_module.md#ansible-collections-ansible-builtin-slurp-module) module will also be used to fetch the contents of the file for determining the remote checksum. This effectively doubles the transfer size, and depending on the file size can consume all available memory on the remote or local hosts causing a `MemoryError`. Due to this it is advisable to run this module without `become` whenever possible.
> - Prior to Ansible 2.5 this module would not fail if reading the remote file was impossible unless `fail_on_missing` was set.
> - In Ansible 2.5 or later, playbook authors are encouraged to use `fail_when` or `ignore_errors` to get this ability. They may also explicitly set `fail_on_missing` to `no` to get the non-failing behaviour.

## [See Also](fetch_module.md#id5)

> **See also:**
>
> [ansible.builtin.copy](copy_module.md#ansible-collections-ansible-builtin-copy-module)
> :   Copy files to remote locations.
>
> [ansible.builtin.slurp](slurp_module.md#ansible-collections-ansible-builtin-slurp-module)
> :   Slurps a file from remote nodes.

## [Examples](fetch_module.md#id6)

```yaml+jinja
- name: Store file into /tmp/fetched/host.example.com/tmp/somefile
  ansible.builtin.fetch:
    src: /tmp/somefile
    dest: /tmp/fetched

- name: Specifying a path directly
  ansible.builtin.fetch:
    src: /tmp/somefile
    dest: /tmp/prefix-{{ inventory_hostname }}
    flat: yes

- name: Specifying a destination path
  ansible.builtin.fetch:
    src: /tmp/uniquefile
    dest: /tmp/special/
    flat: yes

- name: Storing in a path relative to the playbook
  ansible.builtin.fetch:
    src: /tmp/uniquefile
    dest: special/prefix-{{ inventory_hostname }}
    flat: yes
```

### Authors

- Ansible Core Team
- Michael DeHaan

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
