---
collection: ansible
version: "8"
title: "f5networks.f5_modules.abspath filter – return absolute path of a file"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/abspath_filter.html
fetched_at: 2026-07-28T02:07:45+00:00
---
# f5networks.f5_modules.abspath filter – return absolute path of a file

> **Note:**
>
> This filter plugin is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/ui/repo/published/f5networks/f5_modules/) (version 1.27.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.abspath`.

- [Synopsis](abspath_filter.md#synopsis)
- [Input](abspath_filter.md#input)
- [Examples](abspath_filter.md#examples)
- [Return Value](abspath_filter.md#return-value)

## [Synopsis](abspath_filter.md#id1)

- A wrapper around os.path.abspath function to return absolute path of a given file path.

## [Input](abspath_filter.md#id2)

This describes the input of the filter, the value before `| f5networks.f5_modules.abspath`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | A file path |

## [Examples](abspath_filter.md#id3)

```yaml+jinja
# use filepath to install with absolute path
- name: Install AS3 package if missing
  bigip_lx_package:
    package: "files/f5-appsvcs-3.36.1-1.noarch.rpm" | abspath
```

## [Return Value](abspath_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  string | The absolute path to given file  **Returned:** success |

### Authors

- Tim Rupp

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
