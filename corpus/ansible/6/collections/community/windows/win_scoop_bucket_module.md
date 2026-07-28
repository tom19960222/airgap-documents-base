---
collection: ansible
version: "6"
title: "community.windows.win_scoop_bucket module – Manage Scoop buckets"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_scoop_bucket_module.html
fetched_at: 2026-07-27T17:23:57+00:00
---
# community.windows.win_scoop_bucket module – Manage Scoop buckets

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/community/windows) (version 1.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
> You need further requirements to be able to use this module,
> see [Requirements](win_scoop_bucket_module.md#ansible-collections-community-windows-win-scoop-bucket-module-requirements) for details.
>
> To use it in a playbook, specify: `community.windows.win_scoop_bucket`.

New in community.windows 1.0.0

- [Synopsis](win_scoop_bucket_module.md#synopsis)
- [Requirements](win_scoop_bucket_module.md#requirements)
- [Parameters](win_scoop_bucket_module.md#parameters)
- [See Also](win_scoop_bucket_module.md#see-also)
- [Examples](win_scoop_bucket_module.md#examples)
- [Return Values](win_scoop_bucket_module.md#return-values)

## [Synopsis](win_scoop_bucket_module.md#id1)

- Manage Scoop buckets

## [Requirements](win_scoop_bucket_module.md#id2)

The below requirements are needed on the host that executes this module.

- git

## [Parameters](win_scoop_bucket_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **name**  string / required | Name of the Scoop bucket. |
| **repo**  string | Git repository that contains the scoop bucket |
| **state**  string | State of the Scoop bucket.  When `absent`, will ensure the package is not installed.  When `present`, will ensure the package is installed.  Choices:   - `"absent"` - `"present"` ← (default) |

## [See Also](win_scoop_bucket_module.md#id4)

> **See also:**
>
> [community.windows.win_scoop](win_scoop_module.md#ansible-collections-community-windows-win-scoop-module)
> :   Manage packages using Scoop.
>
> [Scoop website](https://scoop.sh)
> :   More information about Scoop
>
> [Scoop directory](https://rasa.github.io/scoop-directory/)
> :   A directory of buckets for the scoop package manager for Windows

## [Examples](win_scoop_bucket_module.md#id5)

```yaml+jinja
- name: Add the extras bucket
  community.windows.win_scoop_bucket:
    name: extras

- name: Remove the versions bucket
  community.windows.win_scoop_bucket:
    name: versions
    state: absent

- name: Add a custom bucket
  community.windows.win_scoop_bucket:
    name: my-bucket
    repo: https://github.com/example/my-bucket
```

## [Return Values](win_scoop_bucket_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **rc**  integer | The result code of the scoop action  Returned: always  Sample: `0` |
| **stdout**  string | The raw output from the scoop action  Returned: on failure or when verbosity is greater than 1  Sample: `"The test bucket was added successfully."` |

### Authors

- Jamie Magee (@JamieMagee)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
