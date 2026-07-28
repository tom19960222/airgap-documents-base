---
collection: ansible
version: "6"
title: "ansible.builtin.nested lookup – composes a list with nested elements of other lists"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/nested_lookup.html
fetched_at: 2026-07-27T16:44:21+00:00
---
# ansible.builtin.nested lookup – composes a list with nested elements of other lists

> **Note:**
>
> This lookup plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `nested` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same lookup plugin name.

- [Synopsis](nested_lookup.md#synopsis)
- [Keyword parameters](nested_lookup.md#keyword-parameters)
- [Examples](nested_lookup.md#examples)
- [Return Value](nested_lookup.md#return-value)

## [Synopsis](nested_lookup.md#id1)

- Takes the input lists and returns a list with elements that are lists composed of the elements of the input lists

## [Keyword parameters](nested_lookup.md#id2)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('ansible.builtin.nested', key1=value1, key2=value2, ...)` and `query('ansible.builtin.nested', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **_raw**  string / required | a set of lists |

## [Examples](nested_lookup.md#id3)

```yaml+jinja
- name: give users access to multiple databases
  community.mysql.mysql_user:
    name: "{{ item[0] }}"
    priv: "{{ item[1] }}.*:ALL"
    append_privs: yes
    password: "foo"
  with_nested:
    - [ 'alice', 'bob' ]
    - [ 'clientdb', 'employeedb', 'providerdb' ]
# As with the case of 'with_items' above, you can use previously defined variables.:

- name: here, 'users' contains the above list of employees
  community.mysql.mysql_user:
    name: "{{ item[0] }}"
    priv: "{{ item[1] }}.*:ALL"
    append_privs: yes
    password: "foo"
  with_nested:
    - "{{ users }}"
    - [ 'clientdb', 'employeedb', 'providerdb' ]
```

## [Return Value](nested_lookup.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | A list composed of lists paring the elements of the input lists  Returned: success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
