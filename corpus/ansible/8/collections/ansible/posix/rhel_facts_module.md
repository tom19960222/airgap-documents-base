---
collection: ansible
version: "8"
title: "ansible.posix.rhel_facts module – Facts module to set or override RHEL specific facts."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/posix/rhel_facts_module.html
fetched_at: 2026-07-28T01:09:29+00:00
---
# ansible.posix.rhel_facts module – Facts module to set or override RHEL specific facts.

> **Note:**
>
> This module is part of the [ansible.posix collection](https://galaxy.ansible.com/ui/repo/published/ansible/posix/) (version 1.5.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.posix`.
> You need further requirements to be able to use this module,
> see [Requirements](rhel_facts_module.md#ansible-collections-ansible-posix-rhel-facts-module-requirements) for details.
>
> To use it in a playbook, specify: `ansible.posix.rhel_facts`.

New in ansible.posix 1.5.0

- [Synopsis](rhel_facts_module.md#synopsis)
- [Requirements](rhel_facts_module.md#requirements)
- [See Also](rhel_facts_module.md#see-also)
- [Examples](rhel_facts_module.md#examples)
- [Returned Facts](rhel_facts_module.md#returned-facts)

## [Synopsis](rhel_facts_module.md#id1)

- Compatibility layer for using the “package” module for rpm-ostree based systems via setting the “pkg_mgr” fact correctly.

## [Requirements](rhel_facts_module.md#id2)

The below requirements are needed on the host that executes this module.

- rpm-ostree

## [See Also](rhel_facts_module.md#id3)

> **See also:**
>
> [ansible.builtin.package](../builtin/package_module.md#ansible-collections-ansible-builtin-package-module)
> :   Generic OS package manager.

## [Examples](rhel_facts_module.md#id4)

```yaml+jinja
- name: Playbook to use the package module on all RHEL footprints
  vars:
    ansible_facts_modules:
      - setup # REQUIRED to be run before all custom fact modules
      - ansible.posix.rhel_facts
  tasks:
    - name: Ensure packages are installed
      ansible.builtin.package:
        name:
          - htop
          - ansible
        state: present
```

## [Returned Facts](rhel_facts_module.md#id5)

Facts returned by this module are added/updated in the `hostvars` host facts and can be referenced by name just like any other host fact. They do not need to be registered in order to use them.

| Key | Description |
| --- | --- |
| **pkg_mgr**  string | System-level package manager override  **Returned:** when needed  **Sample:** `"{'pkg_mgr': 'ansible.posix.rhel_facts'}"` |

### Authors

- Adam Miller (@maxamillion)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.posix)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.posix)
