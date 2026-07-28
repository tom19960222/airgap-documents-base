---
collection: ansible
version: "8"
title: "ansible.utils.get_path lookup – Retrieve the value in a variable using a path"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/get_path_lookup.html
fetched_at: 2026-07-28T01:10:05+00:00
---
# ansible.utils.get_path lookup – Retrieve the value in a variable using a path

> **Note:**
>
> This lookup plugin is part of the [ansible.utils collection](https://galaxy.ansible.com/ui/repo/published/ansible/utils/) (version 2.12.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.utils`.
>
> To use it in a playbook, specify: `ansible.utils.get_path`.

New in ansible.utils 1.0.0

- [Synopsis](get_path_lookup.md#synopsis)
- [Keyword parameters](get_path_lookup.md#keyword-parameters)
- [Examples](get_path_lookup.md#examples)
- [Return Value](get_path_lookup.md#return-value)

## [Synopsis](get_path_lookup.md#id1)

- Use a *path* to retrieve a nested value from a *var*
- **get_path** is also available as a **filter plugin** for convenience
- Using the parameters below- `lookup('ansible.utils.get_path', var, path, wantlist`)

## [Keyword parameters](get_path_lookup.md#id2)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('ansible.utils.get_path', key1=value1, key2=value2, ...)` and `query('ansible.utils.get_path', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **path**  string / required | The *path* in the *var* to retrieve the value of.  The *path* needs to a be a valid jinja path. |
| **var**  any / required | The variable from which the value should be extracted. |
| **wantlist**  boolean | If set to `True`, the return value will always be a list.  This can also be accomplished using `query` or `q` instead of `lookup`.  <https://docs.ansible.com/ansible/latest/plugins/lookup.html>.  **Choices:**   - `false` - `true` |

## [Examples](get_path_lookup.md#id3)

```yaml+jinja
- ansible.builtin.set_fact:
    a:
      b:
        c:
          d:
            - 0
            - 1
          e:
            - true
            - false

- name: Retrieve a value deep inside a using a path
  ansible.builtin.set_fact:
    value: "{{ lookup('ansible.utils.get_path', a, path) }}"
  vars:
    path: b.c.d[0]

# TASK [Retrieve a value deep inside a using a path] ******************
# ok: [localhost] => changed=false
#   ansible_facts:
#     value: '0'

#### Working with hostvars

- name: Retrieve a value deep inside all of the host's vars
  ansible.builtin.set_fact:
    value: "{{ lookup('ansible.utils.get_path', look_in, look_for) }}"
  vars:
    look_in: "{{ hostvars[inventory_hostname] }}"
    look_for: a.b.c.d[0]

# TASK [Retrieve a value deep inside all of the host's vars] ********
# ok: [nxos101] => changed=false
#   ansible_facts:
#     as_filter: '0'
#     as_lookup: '0'

#### Used alongside ansible.utils.to_paths

- name: Get the paths for the object
  ansible.builtin.set_fact:
    paths: "{{ lookup('ansible.utils.to_paths', a, prepend='a') }}"

- name: Retrieve the value of each path from vars
  ansible.builtin.debug:
    msg: "The value of path {{ path }} in vars is {{ value }}"
  loop: "{{ paths.keys()|list }}"
  loop_control:
    label: "{{ item }}"
  vars:
    path: "{{ item }}"
    value: "{{ lookup('ansible.utils.get_path', hostvars[inventory_hostname], item) }}"

# TASK [Get the paths for the object] *******************************
# ok: [nxos101] => changed=false
#   ansible_facts:
#     paths:
#       a.b.c.d[0]: 0
#       a.b.c.d[1]: 1
#       a.b.c.e[0]: True
#       a.b.c.e[1]: False

# TASK [Retrieve the value of each path from vars] ******************
# ok: [nxos101] => (item=a.b.c.d[0]) =>
#   msg: The value of path a.b.c.d[0] in vars is 0
# ok: [nxos101] => (item=a.b.c.d[1]) =>
#   msg: The value of path a.b.c.d[1] in vars is 1
# ok: [nxos101] => (item=a.b.c.e[0]) =>
#   msg: The value of path a.b.c.e[0] in vars is True
# ok: [nxos101] => (item=a.b.c.e[1]) =>
#   msg: The value of path a.b.c.e[1] in vars is False

#### Working with complex structures and transforming results

- name: Retrieve the current interface config
  cisco.nxos.nxos_interfaces:
    state: gathered
  register: interfaces

- name: Get the description of several interfaces
  ansible.builtin.debug:
    msg: "{{ lookup('ansible.utils.get_path', rekeyed, item) }}"
  vars:
    rekeyed:
      by_name: "{{ interfaces.gathered|ansible.builtin.rekey_on_member('name') }}"
  loop:
    - by_name['Ethernet1/1'].description
    - by_name['Ethernet1/2'].description|upper
    - by_name['Ethernet1/3'].description|default('')

# TASK [Get the description of several interfaces] ******************
# ok: [nxos101] => (item=by_name['Ethernet1/1'].description) => changed=false
#   msg: Configured by ansible
# ok: [nxos101] => (item=by_name['Ethernet1/2'].description|upper) => changed=false
#   msg: CONFIGURED BY ANSIBLE
# ok: [nxos101] => (item=by_name['Ethernet1/3'].description|default('')) => changed=false
#   msg: ''
```

## [Return Value](get_path_lookup.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  string | One or more zero-based indices of the matching list items.  See `wantlist` if a list is always required.  **Returned:** success |

### Authors

- Bradley Thornton (@cidrblock)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.utils/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.utils)
