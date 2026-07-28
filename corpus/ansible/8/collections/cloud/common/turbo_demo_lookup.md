---
collection: ansible
version: "8"
title: "cloud.common.turbo_demo lookup – A demo for lookup plugins on cloud.common"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cloud/common/turbo_demo_lookup.html
fetched_at: 2026-07-28T01:05:37+00:00
---
# cloud.common.turbo_demo lookup – A demo for lookup plugins on cloud.common

> **Note:**
>
> This lookup plugin is part of the [cloud.common collection](https://galaxy.ansible.com/ui/repo/published/cloud/common/) (version 2.1.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cloud.common`.
>
> To use it in a playbook, specify: `cloud.common.turbo_demo`.

- [Synopsis](turbo_demo_lookup.md#synopsis)
- [Keyword parameters](turbo_demo_lookup.md#keyword-parameters)
- [Examples](turbo_demo_lookup.md#examples)

## [Synopsis](turbo_demo_lookup.md#id1)

- return the parent process of the running process

## [Keyword parameters](turbo_demo_lookup.md#id2)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('cloud.common.turbo_demo', key1=value1, key2=value2, ...)` and `query('cloud.common.turbo_demo', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **playbook_vars**  list / elements=string | list of playbook variables to add in the output. |

## [Examples](turbo_demo_lookup.md#id3)

```yaml+jinja

```

### Authors

- Aubin Bikouo (@abikouo)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cloud.common/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cloud.common)
