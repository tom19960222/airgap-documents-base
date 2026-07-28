---
collection: ansible
version: "8"
title: "compile"
source_url: https://docs.ansible.com/projects/ansible/8/dev_guide/testing/sanity/compile.html
fetched_at: 2026-07-28T01:03:26+00:00
---
# compile

All Python source files must successfully compile using all supported Python versions.

> **Note:**
>
> The list of supported Python versions is dependent on the version of `ansible-core` that you are using.
> Make sure you consult the version of the documentation which matches your `ansible-core` version.

Controller code, including plugins in Ansible Collections, must support the following Python versions:

- 3.11
- 3.10
- 3.9

Code which runs on targets (`modules` and `module_utils`) must support all controller supported Python versions,
as well as the additional Python versions supported only on targets:

- 3.8
- 3.7
- 3.6
- 3.5
- 2.7

> **Note:**
>
> Ansible Collections can be
> [configured](https://github.com/ansible/ansible/blob/devel/test/lib/ansible_test/config/config.yml)
> to support a subset of the target-only Python versions.
