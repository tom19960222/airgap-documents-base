---
collection: ansible
version: "6"
title: "community.general.alternatives module – Manages alternative programs for common commands"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/alternatives_module.html
fetched_at: 2026-07-27T17:08:05+00:00
---
# community.general.alternatives module – Manages alternative programs for common commands

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](alternatives_module.md#ansible-collections-community-general-alternatives-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.alternatives`.

- [Synopsis](alternatives_module.md#synopsis)
- [Requirements](alternatives_module.md#requirements)
- [Parameters](alternatives_module.md#parameters)
- [Examples](alternatives_module.md#examples)

## [Synopsis](alternatives_module.md#id1)

- Manages symbolic links using the ‘update-alternatives’ tool.
- Useful when multiple programs are installed but provide similar functionality (e.g. different editors).

## [Requirements](alternatives_module.md#id2)

The below requirements are needed on the host that executes this module.

- update-alternatives

## [Parameters](alternatives_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **link**  path | The path to the symbolic link that should point to the real executable.  This option is always required on RHEL-based distributions. On Debian-based distributions this option is required when the alternative *name* is unknown to the system. |
| **name**  string / required | The generic name of the link. |
| **path**  path / required | The path to the real executable that the link should point to. |
| **priority**  integer | The priority of the alternative. If no priority is given for creation `50` is used as a fallback. |
| **state**  string  added in community.general 4.8.0 | `present` - install the alternative (if not already installed), but do not set it as the currently selected alternative for the group.  `selected` - install the alternative (if not already installed), and set it as the currently selected alternative for the group.  `auto` - install the alternative (if not already installed), and set the group to auto mode. Added in community.general 5.1.0.  `absent` - removes the alternative. Added in community.general 5.1.0.  Choices:   - `"present"` - `"selected"` ← (default) - `"auto"` - `"absent"` |
| **subcommands**  aliases: slaves  list / elements=dictionary  added in community.general 5.1.0 | A list of subcommands.  Each subcommand needs a name, a link and a path parameter. |
| **link**  path / required | The path to the symbolic link that should point to the real subcommand executable. |
| **name**  string / required | The generic name of the subcommand. |
| **path**  path / required | The path to the real executable that the subcommand should point to. |

## [Examples](alternatives_module.md#id4)

```yaml+jinja
- name: Correct java version selected
  community.general.alternatives:
    name: java
    path: /usr/lib/jvm/java-7-openjdk-amd64/jre/bin/java

- name: Alternatives link created
  community.general.alternatives:
    name: hadoop-conf
    link: /etc/hadoop/conf
    path: /etc/hadoop/conf.ansible

- name: Make java 32 bit an alternative with low priority
  community.general.alternatives:
    name: java
    path: /usr/lib/jvm/java-7-openjdk-i386/jre/bin/java
    priority: -10

- name: Install Python 3.5 but do not select it
  community.general.alternatives:
    name: python
    path: /usr/bin/python3.5
    link: /usr/bin/python
    state: present

- name: Install Python 3.5 and reset selection to auto
  community.general.alternatives:
    name: python
    path: /usr/bin/python3.5
    link: /usr/bin/python
    state: auto

- name: keytool is a subcommand of java
  community.general.alternatives:
    name: java
    link: /usr/bin/java
    path: /usr/lib/jvm/java-7-openjdk-amd64/jre/bin/java
    subcommands:
      - name: keytool
        link: /usr/bin/keytool
        path: /usr/lib/jvm/java-7-openjdk-amd64/jre/bin/keytool
```

### Authors

- Marius Rieder (@jiuka)
- David Wittman (@DavidWittman)
- Gabe Mulley (@mulby)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
