---
collection: ansible
version: "6"
title: "Compile Tests"
source_url: https://docs.ansible.com/projects/ansible/6/dev_guide/testing_compile.html
fetched_at: 2026-07-27T16:42:51+00:00
---
# [Compile Tests](testing_compile.md#id1)

Topics

- [Compile Tests](testing_compile.md#compile-tests)

  - [Overview](testing_compile.md#overview)
  - [Running compile tests locally](testing_compile.md#running-compile-tests-locally)
  - [Installing dependencies](testing_compile.md#installing-dependencies)
  - [Extending compile tests](testing_compile.md#extending-compile-tests)

## [Overview](testing_compile.md#id2)

Compile tests check source files for valid syntax on all supported python versions:

- 2.4 (Ansible 2.3 only)
- 2.6
- 2.7
- 3.5
- 3.6
- 3.7
- 3.8
- 3.9

NOTE: In Ansible 2.4 and earlier the compile test was provided by a dedicated sub-command `ansible-test compile` instead of a sanity test using `ansible-test sanity --test compile`.

## [Running compile tests locally](testing_compile.md#id3)

Compile tests can be run across the whole code base by doing:

```shell
cd /path/to/ansible/source
source hacking/env-setup
ansible-test sanity --test compile
```

Against a single file by doing:

```shell
ansible-test sanity --test compile lineinfile
```

Or against a specific Python version by doing:

```shell
ansible-test sanity --test compile --python 2.7 lineinfile
```

For advanced usage see the help:

```shell
ansible-test sanity --help
```

## [Installing dependencies](testing_compile.md#id4)

`ansible-test` has a number of dependencies , for `compile` tests we suggest running the tests with `--local`, which is the default

The dependencies can be installed using the `--requirements` argument. For example:

```shell
ansible-test sanity --test compile --requirements lineinfile
```

The full list of requirements can be found at [test/lib/ansible_test/_data/requirements](https://github.com/ansible/ansible/tree/devel/test/lib/ansible_test/_data/requirements). Requirements files are named after their respective commands. See also the [constraints](https://github.com/ansible/ansible/blob/devel/test/lib/ansible_test/_data/requirements/constraints.txt) applicable to all commands.

## [Extending compile tests](testing_compile.md#id5)

If you believe changes are needed to the compile tests please add a comment on the [Testing Working Group Agenda](https://github.com/ansible/community/blob/master/meetings/README.md) so it can be discussed.
