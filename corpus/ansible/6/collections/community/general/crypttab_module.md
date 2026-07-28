---
collection: ansible
version: "6"
title: "community.general.crypttab module – Encrypted Linux block devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/crypttab_module.html
fetched_at: 2026-07-27T17:08:39+00:00
---
# community.general.crypttab module – Encrypted Linux block devices

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
> To use it in a playbook, specify: `community.general.crypttab`.

- [Synopsis](crypttab_module.md#synopsis)
- [Parameters](crypttab_module.md#parameters)
- [Examples](crypttab_module.md#examples)

## [Synopsis](crypttab_module.md#id1)

- Control Linux encrypted block devices that are set up during system boot in `/etc/crypttab`.

## [Parameters](crypttab_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **backing_device**  string | Path to the underlying block device or file, or the UUID of a block-device prefixed with *UUID=*. |
| **name**  string / required | Name of the encrypted block device as it appears in the `/etc/crypttab` file, or optionally prefixed with `/dev/mapper/`, as it appears in the filesystem. */dev/mapper/* will be stripped from *name*. |
| **opts**  string | A comma-delimited list of options. See `crypttab(5` ) for details. |
| **password**  path | Encryption password, the path to a file containing the password, or `-` or unset if the password should be entered at boot. |
| **path**  path | Path to file to use instead of `/etc/crypttab`.  This might be useful in a chroot environment.  Default: `"/etc/crypttab"` |
| **state**  string / required | Use *present* to add a line to `/etc/crypttab` or update its definition if already present.  Use *absent* to remove a line with matching *name*.  Use *opts_present* to add options to those already present; options with different values will be updated.  Use *opts_absent* to remove options from the existing set.  Choices:   - `"absent"` - `"opts_absent"` - `"opts_present"` - `"present"` |

## [Examples](crypttab_module.md#id3)

```yaml+jinja
- name: Set the options explicitly a device which must already exist
  community.general.crypttab:
    name: luks-home
    state: present
    opts: discard,cipher=aes-cbc-essiv:sha256

- name: Add the 'discard' option to any existing options for all devices
  community.general.crypttab:
    name: '{{ item.device }}'
    state: opts_present
    opts: discard
  loop: '{{ ansible_mounts }}'
  when: "'/dev/mapper/luks-' in {{ item.device }}"
```

### Authors

- Steve (@groks)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
