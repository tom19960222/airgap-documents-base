---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigiq_license lookup – Select a random license key from a pool of biqiq available licenses"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigiq_license_lookup.html
fetched_at: 2026-07-28T02:07:47+00:00
---
# f5networks.f5_modules.bigiq_license lookup – Select a random license key from a pool of biqiq available licenses

> **Note:**
>
> This lookup plugin is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/ui/repo/published/f5networks/f5_modules/) (version 1.27.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigiq_license`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigiq_license_lookup.md#synopsis)
- [Examples](bigiq_license_lookup.md#examples)
- [Return Value](bigiq_license_lookup.md#return-value)

## [Synopsis](bigiq_license_lookup.md#id1)

- Select a random license key from a pool of biqiq available licenses.
- Requires specifying BIGIQ license pool name and connection parameters.

## [Examples](bigiq_license_lookup.md#id2)

```yaml+jinja
- name: Get a regkey license from a license pool
  bigiq_regkey_license:
    key: "{{ lookup('f5networks.f5_modules.bigiq_license', pool_name='foo_pool', username=baz, password=bar, host=192.168.1.1, port=10443}}"
    state: present
    pool: foo_pool

- name: Get a regkey license from a license pool, use default credentials and port, disable SSL verification
  bigiq_regkey_license:
    key: "{{ lookup('f5networks.f5_modules.bigiq_license', pool_name='foo_pool', host=192.168.1.1, validate_certs=false}}"
    state: present
    pool: foo_pool
```

## [Return Value](bigiq_license_lookup.md#id3)

| Key | Description |
| --- | --- |
| **Return value**  string | random item  **Returned:** success |

### Authors

- Wojciech Wypior (@wojtek0806)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
