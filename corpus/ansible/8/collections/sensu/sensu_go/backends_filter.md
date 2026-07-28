---
collection: ansible
version: "8"
title: "sensu.sensu_go.backends filter – Format websocket connection for backends hosts from inventory."
source_url: https://docs.ansible.com/projects/ansible/8/collections/sensu/sensu_go/backends_filter.html
fetched_at: 2026-07-28T02:53:41+00:00
---
# sensu.sensu_go.backends filter – Format websocket connection for backends hosts from inventory.

> **Note:**
>
> This filter plugin is part of the [sensu.sensu_go collection](https://galaxy.ansible.com/ui/repo/published/sensu/sensu_go/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install sensu.sensu_go`.
>
> To use it in a playbook, specify: `sensu.sensu_go.backends`.

New in sensu.sensu_go 1.13.2

- [Synopsis](backends_filter.md#synopsis)
- [Input](backends_filter.md#input)
- [Keyword parameters](backends_filter.md#keyword-parameters)
- [Examples](backends_filter.md#examples)
- [Return Value](backends_filter.md#return-value)

## [Synopsis](backends_filter.md#id1)

- Socket connection format function.
- Filter backends hosts from ansible inventory groups.
- The return value is a list of websocket connection addresses.

## [Input](backends_filter.md#id2)

This describes the input of the filter, the value before `| sensu.sensu_go.backends`.

| Parameter | Comments |
| --- | --- |
| **Input**  dictionary / required | Inventory host variables (hostvars). |

## [Keyword parameters](backends_filter.md#id3)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | sensu.sensu_go.backends(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **groups**  list / elements=string / required | List of ansible inventory groups. |

## [Examples](backends_filter.md#id4)

```yaml+jinja
- name: Filter backends from ansible inventory and format a list of websocket connection addresses
  ansible.builtin.debug:
    msg: "{{ hostvars | sensu.sensu_go.backends(groups) }}"
```

## [Return Value](backends_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | List of websocket connection addresses.  **Returned:** success |

### Authors

- Tadej Borovsak (@tadeboro)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/sensu/sensu-go-ansible/issues)
- [Repository (Sources)](https://github.com/sensu/sensu-go-ansible)
