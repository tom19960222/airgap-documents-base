---
collection: ansible
version: "6"
title: "Sanity Tests"
source_url: https://docs.ansible.com/projects/ansible/6/dev_guide/testing_sanity.html
fetched_at: 2026-07-27T16:42:39+00:00
---
# [Sanity Tests](testing_sanity.md#id1)

Topics

- [Sanity Tests](testing_sanity.md#sanity-tests)

  - [How to run](testing_sanity.md#how-to-run)
  - [Available Tests](testing_sanity.md#available-tests)

Sanity tests are made up of scripts and tools used to perform static code analysis.
The primary purpose of these tests is to enforce Ansible coding standards and requirements.

Tests are run with `ansible-test sanity`.
All available tests are run unless the `--test` option is used.

## [How to run](testing_sanity.md#id2)

> **Note:**
>
> To run sanity tests using docker, always use the default docker image
> by passing the `--docker` or `--docker default` argument.

```shell
source hacking/env-setup

# Run all sanity tests
ansible-test sanity

# Run all sanity tests including disabled ones
ansible-test sanity --allow-disabled

# Run all sanity tests against certain file(s)
ansible-test sanity lib/ansible/modules/files/template.py

# Run all sanity tests against certain folder(s)
ansible-test sanity lib/ansible/modules/files/

# Run all tests inside docker (good if you don't have dependencies installed)
ansible-test sanity --docker default

# Run validate-modules against a specific file
ansible-test sanity --test validate-modules lib/ansible/modules/files/template.py
```

## [Available Tests](testing_sanity.md#id3)

Tests can be listed with `ansible-test sanity --list-tests`.

See the full list of [sanity tests](testing/sanity/index.md#all-sanity-tests), which details the various tests and details how to fix identified issues.
