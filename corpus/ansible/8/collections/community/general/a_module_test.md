---
collection: ansible
version: "8"
title: "community.general.a_module test – Test whether a given string refers to an existing module or action plugin"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/a_module_test.html
fetched_at: 2026-07-28T01:53:02+00:00
---
# community.general.a_module test – Test whether a given string refers to an existing module or action plugin

> **Note:**
>
> This test plugin is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.a_module`.

New in community.general 4.0.0

- [Synopsis](a_module_test.md#synopsis)
- [Input](a_module_test.md#input)
- [Examples](a_module_test.md#examples)
- [Return Value](a_module_test.md#return-value)

## [Synopsis](a_module_test.md#id1)

- Test whether a given string refers to an existing module or action plugin.
- This can be useful in roles, which can use this to ensure that required modules are present ahead of time.

## [Input](a_module_test.md#id2)

This describes the input of the test, the value before `is community.general.a_module` or `is not community.general.a_module`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | A string denoting a fully qualified collection name (FQCN) of a module or action plugin. |

## [Examples](a_module_test.md#id3)

```yaml+jinja
- name: Make sure that community.aws.route53 is available
  ansible.builtin.assert:
    that:
      - >
        'community.aws.route53' is community.general.a_module

- name: Make sure that community.general.does_not_exist is not a module or action plugin
  ansible.builtin.assert:
    that:
      - "'community.general.does_not_exist' is not community.general.a_module"
```

## [Return Value](a_module_test.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  boolean | Whether the module or action plugin denoted by the input exists.  **Returned:** success |

### Authors

- Felix Fontein (@felixfontein)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
