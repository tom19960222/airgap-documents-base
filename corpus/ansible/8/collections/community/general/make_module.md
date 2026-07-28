---
collection: ansible
version: "8"
title: "community.general.make module – Run targets in a Makefile"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/make_module.html
fetched_at: 2026-07-28T01:47:45+00:00
---
# community.general.make module – Run targets in a Makefile

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
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
- [Attributes](make_module.md#attributes)
- [Examples](make_module.md#examples)
- [Return Values](make_module.md#return-values)

## [Synopsis](make_module.md#id1)

- Run targets in a Makefile.

Aliases: system.make

## [Requirements](make_module.md#id2)

The below requirements are needed on the host that executes this module.

- make

## [Parameters](make_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **chdir**  path / required | Change to this directory before running make. |
| **file**  path | Use a custom Makefile. |
| **jobs**  integer  *added in community.general 2.0.0* | Set the number of make jobs to run concurrently.  Typically if set, this would be the number of processors and/or threads available to the machine.  This is not supported by all make implementations. |
| **make**  path  *added in community.general 0.2.0* | Use a specific make binary. |
| **params**  dictionary | Any extra parameters to pass to make.  If the value is empty, only the key will be used. For example, `FOO:` will produce `FOO`, not `FOO=`. |
| **target**  string | The target to run.  Typically this would be something like `install`, `test`, or `all`.  `target` and `targets` are mutually exclusive. |
| **targets**  list / elements=string  *added in community.general 7.2.0* | The list of targets to run.  Typically this would be something like `install`, `test`, or `all`.  `target` and `targets` are mutually exclusive. |

## [Attributes](make_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](make_module.md#id5)

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

- name: build arm64 kernel on FreeBSD, with 16 parallel jobs
  community.general.make:
    chdir: /usr/src
    jobs: 16
    target: buildkernel
    params:
      # This adds -DWITH_FDT to the command line:
      -DWITH_FDT:
      # The following adds TARGET=arm64 TARGET_ARCH=aarch64 to the command line:
      TARGET: arm64
      TARGET_ARCH: aarch64
```

## [Return Values](make_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **chdir**  string | The value of the module parameter `chdir`.  **Returned:** success |
| **command**  string  *added in community.general 6.5.0* | The command built and executed by the module.  **Returned:** success |
| **file**  string | The value of the module parameter `file`.  **Returned:** success |
| **jobs**  integer | The value of the module parameter `jobs`.  **Returned:** success |
| **params**  dictionary | The value of the module parameter `params`.  **Returned:** success |
| **target**  string | The value of the module parameter `target`.  **Returned:** success |
| **targets**  string  *added in community.general 7.2.0* | The value of the module parameter `targets`.  **Returned:** success |

### Authors

- Linus Unnebäck (@LinusU)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
