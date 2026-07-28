---
collection: ansible
version: "8"
title: "ansible.utils.to_paths lookup – Flatten a complex object into a dictionary of paths and values"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/to_paths_lookup.html
fetched_at: 2026-07-28T01:10:06+00:00
---
# ansible.utils.to_paths lookup – Flatten a complex object into a dictionary of paths and values

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
> To use it in a playbook, specify: `ansible.utils.to_paths`.

New in ansible.utils 1.0.0

- [Synopsis](to_paths_lookup.md#synopsis)
- [Keyword parameters](to_paths_lookup.md#keyword-parameters)
- [Examples](to_paths_lookup.md#examples)
- [Return Value](to_paths_lookup.md#return-value)

## [Synopsis](to_paths_lookup.md#id1)

- Flatten a complex object into a dictionary of paths and values.
- Paths are dot delimited whenever possible.
- Brackets are used for list indices and keys that contain special characters.
- **to_paths** is also available as a filter plugin.
- Using the parameters below- `lookup('ansible.utils.to_paths', var, prepend, wantlist`)

## [Keyword parameters](to_paths_lookup.md#id2)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('ansible.utils.to_paths', key1=value1, key2=value2, ...)` and `query('ansible.utils.to_paths', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **prepend**  string | Prepend each path entry. Useful to add the initial *var* name. |
| **var**  any / required | The value of *var* will be used. |
| **wantlist**  boolean | If set to *True*, the return value will always be a list.  This can also be accomplished using `query` or **q** instead of `lookup`.  <https://docs.ansible.com/ansible/latest/plugins/lookup.html>  **Choices:**   - `false` - `true` |

## [Examples](to_paths_lookup.md#id3)

```yaml+jinja
#### Simple examples

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

- ansible.builtin.set_fact:
    paths: "{{ lookup('ansible.utils.to_paths', a) }}"

# TASK [ansible.builtin.set_fact] ********************************************
# ok: [nxos101] => changed=false
#   ansible_facts:
#     paths:
#       b.c.d[0]: 0
#       b.c.d[1]: 1
#       b.c.e[0]: True
#       b.c.e[1]: False

- name: Use prepend to add the initial variable name
  ansible.builtin.set_fact:
    paths: "{{ lookup('ansible.utils.to_paths', a, prepend='a') }}"

# TASK [Use prepend to add the initial variable name] **************************
# ok: [nxos101] => changed=false
#   ansible_facts:
#     paths:
#       a.b.c.d[0]: 0
#       a.b.c.d[1]: 1
#       a.b.c.e[0]: True
#       a.b.c.e[1]: False

#### Using a complex object

- name: Make an API call
  ansible.builtin.uri:
    url: "https://nxos101/restconf/data/openconfig-interfaces:interfaces"
    headers:
      accept: "application/yang.data+json"
    url_password: password
    url_username: admin
    validate_certs: false
  register: result
  delegate_to: localhost

- name: Flatten the complex object
  ansible.builtin.set_fact:
    paths: "{{ lookup('ansible.utils.to_paths', result.json) }}"

# TASK [Flatten the complex object] ******************************************
# ok: [nxos101] => changed=false
#   ansible_facts:
#     paths:
#       interfaces.interface[0].config.enabled: 'true'
#       interfaces.interface[0].config.mtu: '1500'
#       interfaces.interface[0].config.name: eth1/71
#       interfaces.interface[0].config.type: ethernetCsmacd
#       interfaces.interface[0].ethernet.config['auto-negotiate']: 'true'
#       interfaces.interface[0].ethernet.state.counters['in-crc-errors']: '0'
#       interfaces.interface[0].ethernet.state.counters['in-fragment-frames']: '0'
#       interfaces.interface[0].ethernet.state.counters['in-jabber-frames']: '0'
#       interfaces.interface[0].ethernet.state.counters['in-mac-control-frames']: '0'
#       <...>
```

## [Return Value](to_paths_lookup.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  string | A dictionary of key value pairs.  The key is the path.  The value is the value.  **Returned:** success |

### Authors

- Bradley Thornton (@cidrblock)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.utils/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.utils)
