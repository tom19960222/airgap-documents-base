---
collection: ansible
version: "8"
title: "ansible.utils.to_paths filter – Flatten a complex object into a dictionary of paths and values"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/to_paths_filter.html
fetched_at: 2026-07-28T01:10:02+00:00
---
# ansible.utils.to_paths filter – Flatten a complex object into a dictionary of paths and values

> **Note:**
>
> This filter plugin is part of the [ansible.utils collection](https://galaxy.ansible.com/ui/repo/published/ansible/utils/) (version 2.12.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.utils`.
>
> To use it in a playbook, specify: `ansible.utils.to_paths`.

New in ansible.utils 1.0.0

- [Synopsis](to_paths_filter.md#synopsis)
- [Keyword parameters](to_paths_filter.md#keyword-parameters)
- [Examples](to_paths_filter.md#examples)

## [Synopsis](to_paths_filter.md#id1)

- Flatten a complex object into a dictionary of paths and values.
- Paths are dot delimited whenever possible.
- Brackets are used for list indices and keys that contain special characters.
- **to_paths** is also available as a **lookup plugin** for convenience.
- Using the parameters below- `var|ansible.utils.to_paths(prepend, wantlist`)

## [Keyword parameters](to_paths_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.utils.to_paths(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **prepend**  string | Prepend each path entry. Useful to add the initial *var* name. |
| **var**  any / required | The value of *var* will be will be used.  This option represents the value that is passed to the filter plugin in pipe format.  For example `config_data|ansible.utils.to_paths(`), in this case `config_data` represents this option. |
| **wantlist**  boolean | If set to `True`, the return value will always be a list.  **Choices:**   - `false` - `true` |

## [Examples](to_paths_filter.md#id3)

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
    paths: "{{ a|ansible.utils.to_paths }}"

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
    paths: "{{ a|ansible.utils.to_paths(prepend='a') }}"

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
  uri:
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
    paths: "{{ result.json|ansible.utils.to_paths }}"

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

### Authors

- Bradley Thornton (@cidrblock)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.utils/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.utils)
