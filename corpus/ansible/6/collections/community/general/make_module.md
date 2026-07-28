---
collection: ansible
version: "6"
title: "community.general.make module – Run targets in a Makefile"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/make_module.html
fetched_at: 2026-07-27T17:10:44+00:00
---
# community.general.make module – Run targets in a Makefile

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
> see [Requirements](make_module.md#ansible-collections-community-general-make-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.make`.

- [Synopsis](make_module.md#synopsis)
- [Requirements](make_module.md#requirements)
- [Parameters](make_module.md#parameters)
- [Examples](make_module.md#examples)

## [Synopsis](make_module.md#id1)

- Run targets in a Makefile.

## [Requirements](make_module.md#id2)

The below requirements are needed on the host that executes this module.

- make

## [Parameters](make_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **chdir**  path / required | Change to this directory before running make. |
| **file**  path | Use a custom Makefile. |
| **jobs**  integer  added in community.general 2.0.0 | Set the number of make jobs to run concurrently.  Typically if set, this would be the number of processors and/or threads available to the machine.  This is not supported by all make implementations. |
| **make**  path  added in community.general 0.2.0 | Use a specific make binary. |
| **params**  dictionary | Any extra parameters to pass to make. |
| **target**  string | The target to run.  Typically this would be something like `install`,`test` or `all`.” |

## [Examples](make_module.md#id4)

```yaml+jinja
- name: Build the default target
  community.general.make:
    chdir: /home/ubuntu/cool-project

- name: Run 'install' target as root
  community.general.make:
    chdir: /home/ubuntu/cool-project
    target: install
  become: true

- name: Build 'all' target with extra arguments
  community.general.make:
    chdir: /home/ubuntu/cool-project
    target: all
    params:
      NUM_THREADS: 4
      BACKEND: lapack

- name: Build 'all' target with a custom Makefile
  community.general.make:
    chdir: /home/ubuntu/cool-project
    target: all
    file: /some-project/Makefile
```

### Authors

- Linus Unnebäck (@LinusU)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
