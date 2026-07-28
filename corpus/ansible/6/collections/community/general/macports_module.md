---
collection: ansible
version: "6"
title: "community.general.macports module – Package manager for MacPorts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/macports_module.html
fetched_at: 2026-07-27T17:10:43+00:00
---
# community.general.macports module – Package manager for MacPorts

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
> To use it in a playbook, specify: `community.general.macports`.

- [Synopsis](macports_module.md#synopsis)
- [Parameters](macports_module.md#parameters)
- [Examples](macports_module.md#examples)

## [Synopsis](macports_module.md#id1)

- Manages MacPorts packages (ports)

## [Parameters](macports_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  aliases: port  list / elements=string | A list of port names. |
| **selfupdate**  aliases: update_cache, update_ports  boolean | Update Macports and the ports tree, either prior to installing ports or as a separate step.  Equivalent to running `port selfupdate`.  Choices:   - `false` ← (default) - `true` |
| **state**  string | Indicates the desired state of the port.  Choices:   - `"present"` ← (default) - `"absent"` - `"active"` - `"inactive"` - `"installed"` - `"removed"` |
| **upgrade**  boolean | Upgrade all outdated ports, either prior to installing ports or as a separate step.  Equivalent to running `port upgrade outdated`.  Choices:   - `false` ← (default) - `true` |
| **variant**  aliases: variants  string | A port variant specification.  `variant` is only supported with state: *installed*/*present*. |

## [Examples](macports_module.md#id3)

```yaml+jinja
- name: Install the foo port
  community.general.macports:
    name: foo

- name: Install the universal, x11 variant of the foo port
  community.general.macports:
    name: foo
    variant: +universal+x11

- name: Install a list of ports
  community.general.macports:
    name: "{{ ports }}"
  vars:
    ports:
    - foo
    - foo-tools

- name: Update Macports and the ports tree, then upgrade all outdated ports
  community.general.macports:
    selfupdate: true
    upgrade: true

- name: Update Macports and the ports tree, then install the foo port
  community.general.macports:
    name: foo
    selfupdate: true

- name: Remove the foo port
  community.general.macports:
    name: foo
    state: absent

- name: Activate the foo port
  community.general.macports:
    name: foo
    state: active

- name: Deactivate the foo port
  community.general.macports:
    name: foo
    state: inactive
```

### Authors

- Jimmy Tang (@jcftang)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
