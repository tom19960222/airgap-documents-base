---
collection: ansible
version: "6"
title: "f5networks.f5_modules.license_hopper lookup – Return random license from list"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/license_hopper_lookup.html
fetched_at: 2026-07-27T16:43:26+00:00
---
# f5networks.f5_modules.license_hopper lookup – Return random license from list

> **Note:**
>
> This lookup plugin is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/f5networks/f5_modules) (version 1.21.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.license_hopper`.

New in f5networks.f5_modules 1.0

- [Synopsis](license_hopper_lookup.md#synopsis)
- [Examples](license_hopper_lookup.md#examples)
- [Return Value](license_hopper_lookup.md#return-value)

## [Synopsis](license_hopper_lookup.md#id1)

- Select a random license key from a file and remove it from future lookups
- Can optionally remove the key if `remove=True` is specified

## [Examples](license_hopper_lookup.md#id2)

```yaml+jinja
- name: Get a regkey license from a stash without deleting it
  bigiq_regkey_license:
    key: "{{ lookup('license_hopper', 'filename=/path/to/licenses.txt') }}"
    state: present
    pool: regkey1

- name: Get a regkey license from a stash and delete the key from the file
  bigiq_regkey_license:
    key: "{{ lookup('license_hopper', 'filename=/path/to/licenses.txt', remove=True) }}"
    state: present
    pool: regkey1
```

## [Return Value](license_hopper_lookup.md#id3)

| Key | Description |
| --- | --- |
| **Return value**  string | random item  Returned: success |

### Authors

- Tim Rupp

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
