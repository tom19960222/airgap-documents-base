---
collection: ansible
version: "6"
title: "community.general.manifold lookup – get credentials from Manifold.co"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/manifold_lookup.html
fetched_at: 2026-07-27T17:15:07+00:00
---
# community.general.manifold lookup – get credentials from Manifold.co

> **Note:**
>
> This lookup plugin is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.manifold`.

- [Synopsis](manifold_lookup.md#synopsis)
- [Terms](manifold_lookup.md#terms)
- [Keyword parameters](manifold_lookup.md#keyword-parameters)
- [Notes](manifold_lookup.md#notes)
- [Examples](manifold_lookup.md#examples)
- [Return Value](manifold_lookup.md#return-value)

## [Synopsis](manifold_lookup.md#id1)

- Retrieves resources’ credentials from Manifold.co

## [Terms](manifold_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  list / elements=string | Optional list of resource labels to lookup on Manifold.co. If no resources are specified, all matched resources will be returned. |

## [Keyword parameters](manifold_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.general.manifold', key1=value1, key2=value2, ...)` and `query('community.general.manifold', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **api_token**  string / required | manifold API token  Configuration:   - Environment variable: [`MANIFOLD_API_TOKEN`](../../environment_variables.md#envvar-MANIFOLD_API_TOKEN) |
| **project**  string | The project label you want to get the resource for. |
| **team**  string | The team label you want to get the resource for. |

## [Notes](manifold_lookup.md#id4)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('community.general.manifold', term1, term2, key1=value1, key2=value2)` and `query('community.general.manifold', term1, term2, key1=value1, key2=value2)`

## [Examples](manifold_lookup.md#id5)

```yaml+jinja
- name: all available resources
  ansible.builtin.debug:
    msg: "{{ lookup('community.general.manifold', api_token='SecretToken') }}"
- name: all available resources for a specific project in specific team
  ansible.builtin.debug:
    msg: "{{ lookup('community.general.manifold', api_token='SecretToken', project='poject-1', team='team-2') }}"
- name: two specific resources
  ansible.builtin.debug:
    msg: "{{ lookup('community.general.manifold', 'resource-1', 'resource-2') }}"
```

## [Return Value](manifold_lookup.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  dictionary | dictionary of credentials ready to be consumed as environment variables. If multiple resources define the same environment variable(s), the last one returned by the Manifold API will take precedence.  Returned: success |

### Authors

- Kyrylo Galanov

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
