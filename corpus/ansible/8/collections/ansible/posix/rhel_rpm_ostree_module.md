---
collection: ansible
version: "8"
title: "ansible.posix.rhel_rpm_ostree module – Ensure packages exist in a RHEL for Edge rpm-ostree based system"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/posix/rhel_rpm_ostree_module.html
fetched_at: 2026-07-28T01:09:30+00:00
---
# ansible.posix.rhel_rpm_ostree module – Ensure packages exist in a RHEL for Edge rpm-ostree based system

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
> see [Requirements](rhel_rpm_ostree_module.md#ansible-collections-ansible-posix-rhel-rpm-ostree-module-requirements) for details.
>
> To use it in a playbook, specify: `ansible.posix.rhel_rpm_ostree`.

New in ansible.posix 1.5.0

- [Synopsis](rhel_rpm_ostree_module.md#synopsis)
- [Requirements](rhel_rpm_ostree_module.md#requirements)
- [Parameters](rhel_rpm_ostree_module.md#parameters)
- [Notes](rhel_rpm_ostree_module.md#notes)
- [Examples](rhel_rpm_ostree_module.md#examples)
- [Return Values](rhel_rpm_ostree_module.md#return-values)

## [Synopsis](rhel_rpm_ostree_module.md#id1)

- Compatibility layer for using the “package” module for RHEL for Edge systems utilizing the RHEL System Roles.

## [Requirements](rhel_rpm_ostree_module.md#id2)

The below requirements are needed on the host that executes this module.

- rpm-ostree

## [Parameters](rhel_rpm_ostree_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **name**  aliases: pkg  list / elements=string | A package name or package specifier with version, like `name-1.0`.  Comparison operators for package version are valid here `>`, `<`, `>=`, `<=`. Example - `name>=1.0`  If a previous version is specified, the task also needs to turn `allow_downgrade` on. See the `allow_downgrade` documentation for caveats with downgrading packages.  When using state=latest, this can be `'*'` which means run `yum -y update`.  You can also pass a url or a local path to a rpm file (using state=present). To operate on several packages this can accept a comma separated string of packages or (as of 2.0) a list of packages.  **Default:** `[]` |
| **state**  string | Whether to install (`present` or `installed`, `latest`), or remove (`absent` or `removed`) a package.  `present` and `installed` will simply ensure that a desired package is installed.  `latest` will update the specified package if it’s not of the latest available version.  `absent` and `removed` will remove the specified package.  Default is `None`, however in effect the default action is `present` unless the `autoremove` option is enabled for this module, then `absent` is inferred.  **Choices:**   - `"absent"` - `"installed"` - `"latest"` - `"present"` - `"removed"` |

## [Notes](rhel_rpm_ostree_module.md#id4)

> **Note:**
>
> - This module does not support installing or removing packages to/from an overlay as this is not supported by RHEL for Edge, packages needed should be defined in the osbuild Blueprint and provided to Image Builder at build time. This module exists only for `package` module compatibility.

## [Examples](rhel_rpm_ostree_module.md#id5)

```yaml+jinja
- name: Ensure htop and ansible are installed on rpm-ostree based RHEL
  ansible.posix.rhel_rpm_ostree:
    name:
      - htop
      - ansible
    state: present
```

## [Return Values](rhel_rpm_ostree_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | status of rpm transaction  **Returned:** always  **Sample:** `"No changes made."` |

### Authors

- Adam Miller (@maxamillion)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.posix)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.posix)
