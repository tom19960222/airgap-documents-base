---
collection: ansible
version: "6"
title: "community.general.pkgng module – Package manager for FreeBSD >= 9.0"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/pkgng_module.html
fetched_at: 2026-07-27T17:11:56+00:00
---
# community.general.pkgng module – Package manager for FreeBSD >= 9.0

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
> To use it in a playbook, specify: `community.general.pkgng`.

- [Synopsis](pkgng_module.md#synopsis)
- [Parameters](pkgng_module.md#parameters)
- [Notes](pkgng_module.md#notes)
- [Examples](pkgng_module.md#examples)

## [Synopsis](pkgng_module.md#id1)

- Manage binary packages for FreeBSD using ‘pkgng’ which is available in versions after 9.0.

## [Parameters](pkgng_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **annotation**  list / elements=string | A list of keyvalue-pairs of the form `<+/-/:><key>[=<value>]`. A `+` denotes adding an annotation, a `-` denotes removing an annotation, and `:` denotes modifying an annotation. If setting or modifying annotations, a value must be provided. |
| **autoremove**  boolean | Remove automatically installed packages which are no longer needed.  Choices:   - `false` ← (default) - `true` |
| **cached**  boolean | Use local package base instead of fetching an updated one.  Choices:   - `false` ← (default) - `true` |
| **chroot**  path | Pkg will chroot in the specified environment.  Can not be used together with *rootdir* or *jail* options. |
| **ignore_osver**  boolean  added in community.general 1.3.0 | Ignore FreeBSD OS version check, useful on -STABLE and -CURRENT branches.  Defines the `IGNORE_OSVERSION` environment variable.  Choices:   - `false` ← (default) - `true` |
| **jail**  string | Pkg will execute in the given jail name or id.  Can not be used together with *chroot* or *rootdir* options. |
| **name**  aliases: pkg  list / elements=string / required | Name or list of names of packages to install/remove.  With *name=\**, *state=latest* will operate, but *state=present* and *state=absent* will be noops.  Warning: In Ansible 2.9 and earlier this module had a misfeature where *name=\** with *state=latest* or *state=present* would install every package from every package repository, filling up the machines disk. Avoid using them unless you are certain that your role will only be used with newer versions. |
| **pkgsite**  string | For pkgng versions before 1.1.4, specify packagesite to use for downloading packages. If not specified, use settings from `/usr/local/etc/pkg.conf`.  For newer pkgng versions, specify a the name of a repository configured in `/usr/local/etc/pkg/repos`. |
| **rootdir**  path | For pkgng versions 1.5 and later, pkg will install all packages within the specified root directory.  Can not be used together with *chroot* or *jail* options. |
| **state**  string | State of the package.  Note: `latest` added in 2.7.  Choices:   - `"present"` ← (default) - `"latest"` - `"absent"` |

## [Notes](pkgng_module.md#id3)

> **Note:**
>
> - When using pkgsite, be careful that already in cache packages won’t be downloaded again.
> - When used with a `loop:` each package will be processed individually, it is much more efficient to pass the list directly to the *name* option.

## [Examples](pkgng_module.md#id4)

```yaml+jinja
- name: Install package foo
  community.general.pkgng:
    name: foo
    state: present

- name: Annotate package foo and bar
  community.general.pkgng:
    name:
      - foo
      - bar
    annotation: '+test1=baz,-test2,:test3=foobar'

- name: Remove packages foo and bar
  community.general.pkgng:
    name:
      - foo
      - bar
    state: absent

# "latest" support added in 2.7
- name: Upgrade package baz
  community.general.pkgng:
    name: baz
    state: latest

- name: Upgrade all installed packages (see warning for the name option first!)
  community.general.pkgng:
    name: "*"
    state: latest
```

### Authors

- bleader (@bleader)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
