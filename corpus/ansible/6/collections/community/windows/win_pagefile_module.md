---
collection: ansible
version: "6"
title: "community.windows.win_pagefile module – Query or change pagefile configuration"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_pagefile_module.html
fetched_at: 2026-07-27T17:23:39+00:00
---
# community.windows.win_pagefile module – Query or change pagefile configuration

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/community/windows) (version 1.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_pagefile`.

- [Synopsis](win_pagefile_module.md#synopsis)
- [Parameters](win_pagefile_module.md#parameters)
- [Notes](win_pagefile_module.md#notes)
- [Examples](win_pagefile_module.md#examples)
- [Return Values](win_pagefile_module.md#return-values)

## [Synopsis](win_pagefile_module.md#id1)

- Query current pagefile configuration.
- Enable/Disable AutomaticManagedPagefile.
- Create new or override pagefile configuration.

## [Parameters](win_pagefile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **automatic**  boolean | Configures AutomaticManagedPagefile for the entire system.  Choices:   - `false` - `true` |
| **drive**  string | The drive of the pagefile. |
| **initial_size**  integer | The initial size of the pagefile in megabytes. |
| **maximum_size**  integer | The maximum size of the pagefile in megabytes. |
| **override**  boolean | Override the current pagefile on the drive.  Choices:   - `false` - `true` ← (default) |
| **remove_all**  boolean | Remove all pagefiles in the system, not including automatic managed.  Choices:   - `false` ← (default) - `true` |
| **state**  string | State of the pagefile.  Choices:   - `"absent"` - `"present"` - `"query"` ← (default) |
| **system_managed**  boolean | Configures current pagefile to be managed by the system.  Choices:   - `false` ← (default) - `true` |
| **test_path**  boolean | Use Test-Path on the drive to make sure the drive is accessible before creating the pagefile.  Choices:   - `false` - `true` ← (default) |

## [Notes](win_pagefile_module.md#id3)

> **Note:**
>
> - There is difference between automatic managed pagefiles that configured once for the entire system and system managed pagefile that configured per pagefile.
> - InitialSize 0 and MaximumSize 0 means the pagefile is managed by the system.
> - Value out of range exception may be caused by several different issues, two common problems - No such drive, Pagefile size is too small.
> - Setting a pagefile when AutomaticManagedPagefile is on will disable the AutomaticManagedPagefile.

## [Examples](win_pagefile_module.md#id4)

```yaml+jinja
- name: Query pagefiles configuration
  community.windows.win_pagefile:

- name: Query C pagefile
  community.windows.win_pagefile:
    drive: C

- name: Set C pagefile, don't override if exists
  community.windows.win_pagefile:
    drive: C
    initial_size: 1024
    maximum_size: 1024
    override: no
    state: present

- name: Set C pagefile, override if exists
  community.windows.win_pagefile:
    drive: C
    initial_size: 1024
    maximum_size: 1024
    state: present

- name: Remove C pagefile
  community.windows.win_pagefile:
    drive: C
    state: absent

- name: Remove all current pagefiles, enable AutomaticManagedPagefile and query at the end
  community.windows.win_pagefile:
    remove_all: yes
    automatic: yes

- name: Remove all pagefiles disable AutomaticManagedPagefile and set C pagefile
  community.windows.win_pagefile:
    drive: C
    initial_size: 2048
    maximum_size: 2048
    remove_all: yes
    automatic: no
    state: present

- name: Set D pagefile, override if exists
  community.windows.win_pagefile:
    drive: d
    initial_size: 1024
    maximum_size: 1024
    state: present
```

## [Return Values](win_pagefile_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **automatic_managed_pagefiles**  boolean | Whether the pagefiles is automatically managed.  Returned: When state is query.  Sample: `true` |
| **pagefiles**  list / elements=string | Contains caption, description, initial_size, maximum_size and name for each pagefile in the system.  Returned: When state is query.  Sample: `[{"caption": "c:\\ 'pagefile.sys'", "description": "'pagefile.sys' @ c:\\", "initial_size": 2048, "maximum_size": 2048, "name": "c:\\pagefile.sys"}, {"caption": "d:\\ 'pagefile.sys'", "description": "'pagefile.sys' @ d:\\", "initial_size": 1024, "maximum_size": 1024, "name": "d:\\pagefile.sys"}]` |

### Authors

- Liran Nisanov (@LiranNis)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
