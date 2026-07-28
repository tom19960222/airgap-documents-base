---
collection: ansible
version: "8"
title: "ansible.utils.index_of lookup – Find the indices of items in a list matching some criteria"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/index_of_lookup.html
fetched_at: 2026-07-28T01:10:06+00:00
---
# ansible.utils.index_of lookup – Find the indices of items in a list matching some criteria

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
> To use it in a playbook, specify: `ansible.utils.index_of`.

New in ansible.utils 1.0.0

- [Synopsis](index_of_lookup.md#synopsis)
- [Keyword parameters](index_of_lookup.md#keyword-parameters)
- [Examples](index_of_lookup.md#examples)
- [Return Value](index_of_lookup.md#return-value)

## [Synopsis](index_of_lookup.md#id1)

- This plugin returns the indices of items matching some criteria in a list.
- When working with a list of dictionaries, the key to evaluate can be specified.
- **index_of** is also available as a **filter plugin** for convenience.
- Using the parameters below- `lookup('ansible.utils.index_of', data, test, value, key, fail_on_missing, wantlist`).

## [Keyword parameters](index_of_lookup.md#id2)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('ansible.utils.index_of', key1=value1, key2=value2, ...)` and `query('ansible.utils.index_of', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **data**  list / elements=any / required | A list of items to enumerate and test against. |
| **fail_on_missing**  boolean | When provided a list of dictionaries, fail if the key is missing from one or more of the dictionaries.  **Choices:**   - `false` - `true` |
| **key**  string | When the data provided is a list of dictionaries, run the test against this dictionary key.  When using a *key*, the *data* must only contain dictionaries.  See *fail_on_missing* below to determine the behaviour when the *key* is missing from a dictionary in the *data*. |
| **test**  string / required | The name of the test to run against the list, a valid jinja2 test or ansible test plugin.  Jinja2 includes the following tests <http://jinja.palletsprojects.com/templates/#builtin-tests>.  An overview of tests included in ansible <https://docs.ansible.com/ansible/latest/user_guide/playbooks_tests.html>. |
| **value**  any | The value used to test each list item against.  Not required for simple tests (e.g. `true`, `false`, `even`, `odd`)  May be a `string`, `boolean`, `number`, `regular expression` `dict` and so on, depending on the **test** used. |
| **wantlist**  boolean | When only a single entry in the *data* is matched, the index of that entry is returned as an integer.  If set to `True`, the return value will always be a list, even if only a single entry is matched.  This can also be accomplished using `query` or `q` instead of `lookup`.  <https://docs.ansible.com/ansible/latest/plugins/lookup.html>  **Choices:**   - `false` - `true` |

## [Examples](index_of_lookup.md#id3)

```yaml+jinja
#### Simple examples

- ansible.builtin.set_fact:
    data:
      - 1
      - 2
      - 3

- name: Find the index of 2
  ansible.builtin.set_fact:
    indices: "{{ lookup('ansible.utils.index_of', data, 'eq', 2) }}"

# TASK [Find the index of 2] *************************************************
# ok: [nxos101] => changed=false
#   ansible_facts:
#     indices: '1'

- name: Find the index of 2, ensure list is returned
  ansible.builtin.set_fact:
    indices: "{{ lookup('ansible.utils.index_of', data, 'eq', 2, wantlist=True) }}"

# TASK [Find the index of 2, ensure list is returned] ************************
# ok: [nxos101] => changed=false
#   ansible_facts:
#     indices:
#     - 1

- name: Find the index of 3 using the long format
  ansible.builtin.set_fact:
    indices: "{{ lookup('ansible.utils.index_of', data=data, test='eq', value=value, wantlist=True) }}"
  vars:
    value: 3

# TASK [Find the index of 3 using the long format] ***************************
# ok: [nxos101] => changed=false
#   ansible_facts:
#     indices:
#     - 2

- name: Find numbers greater than 1, using loop
  debug:
    msg: "{{ data[item] }} is {{ test }} than {{ value }}"
  loop: "{{ lookup('ansible.utils.index_of', data, test, value) }}"
  vars:
    test: '>'
    value: 1

# TASK [Find numbers great than 1, using loop] *******************************
# ok: [sw01] => (item=1) =>
#   msg: 2 is > than 1
# ok: [sw01] => (item=2) =>
#   msg: 3 is > than 1

- name: Find numbers greater than 1, using with
  debug:
    msg: "{{ data[item] }} is {{ params.test }} than {{ params.value }}"
  with_ansible.utils.index_of: "{{ params }}"
  vars:
    params:
      data: "{{ data }}"
      test: '>'
      value: 1

# TASK [Find numbers greater than 1, using with] *****************************
# ok: [nxos101] => (item=1) =>
#   msg: 2 is > than 1
# ok: [nxos101] => (item=2) =>
#   msg: 3 is > than 1

#### Working with lists of dictionaries

- ansible.builtin.set_fact:
    data:
      - name: sw01.example.lan
        type: switch
      - name: rtr01.example.lan
        type: router
      - name: fw01.example.corp
        type: firewall
      - name: fw02.example.corp
        type: firewall

- name: Find the index of all firewalls using the type key
  ansible.builtin.set_fact:
    firewalls: "{{ lookup('ansible.utils.index_of', data, 'eq', 'firewall', 'type') }}"

# TASK [Find the index of all firewalls using the type key] ******************
# ok: [nxos101] => changed=false
#   ansible_facts:
#     firewalls:
#     - 2
#     - 3

- name: Find the index of all firewalls, use in a loop
  debug:
    msg: "The type of {{ device_type }} at index {{ item }} has name {{ data[item].name }}."
  loop: "{{ lookup('ansible.utils.index_of', data, 'eq', device_type, 'type') }}"
  vars:
    device_type: firewall

# TASK [Find the index of all firewalls, use in a loop, as a filter] *********
# ok: [nxos101] => (item=2) =>
#   msg: The type of firewall at index 2 has name fw01.example.corp.
# ok: [nxos101] => (item=3) =>
#   msg: The type of firewall at index 3 has name fw02.example.corp.

- name: Find the index of all devices with a .corp name
  debug:
    msg: "The device named {{ data[item].name }} is a {{ data[item].type }}"
  loop: "{{ lookup('ansible.utils.index_of', data, 'regex', expression, 'name') }}"
  vars:
    expression: '\.corp$'

# TASK [Find the index of all devices with a .corp name] *********************
# ok: [nxos101] => (item=2) =>
#   msg: The device named fw01.example.corp is a firewall
# ok: [nxos101] => (item=3) =>
#   msg: The device named fw02.example.corp is a firewall

#### Working with complex structures from resource modules

- name: Retrieve the current L3 interface configuration
  cisco.nxos.nxos_l3_interfaces:
    state: gathered
  register: current_l3

# TASK [Retrieve the current L3 interface configuration] *********************
# ok: [sw01] => changed=false
#   gathered:
#   - name: Ethernet1/1
#   - name: Ethernet1/2
#   <...>
#   - name: Ethernet1/128
#   - ipv4:
#     - address: 192.168.101.14/24
#     name: mgmt0

- name: Find the indices interfaces with a 192.168.101.xx ip address
  ansible.builtin.set_fact:
    found: "{{ found + entry }}"
  with_indexed_items: "{{ current_l3.gathered }}"
  vars:
    found: []
    ip: '192.168.101.'
    address: "{{ lookup('ansible.utils.index_of', item.1.ipv4 | d([]), 'search', ip, 'address', wantlist=True) }}"
    entry:
      - interface_idx: "{{ item.0 }}"
        address_idxs: "{{ address }}"
  when: address

# TASK [debug] ***************************************************************
# ok: [sw01] =>
#   found:
#   - address_idxs:
#     - 0
#     interface_idx: '128'

- name: Show all interfaces and their address
  debug:
    msg: "{{ interface.name }} has ip {{ address }}"
  loop: "{{ found|subelements('address_idxs') }}"
  vars:
    interface: "{{ current_l3.gathered[item.0.interface_idx|int] }}"
    address: "{{ interface.ipv4[item.1].address }}"

# TASK [Show all interfaces and their address] *******************************
# ok: [nxos101] => (item=[{'interface_idx': '128', 'address_idxs': [0]}, 0]) =>
#   msg: mgmt0 has ip 192.168.101.14/24

#### Working with deeply nested data

- ansible.builtin.set_fact:
    data:
      interfaces:
        interface:
          - config:
              description: configured by Ansible - 1
              enabled: true
              loopback-mode: false
              mtu: 1024
              name: loopback0000
              type: eth
            name: loopback0000
            subinterfaces:
              subinterface:
                - config:
                    description: subinterface configured by Ansible - 1
                    enabled: true
                    index: 5
                  index: 5
                - config:
                    description: subinterface configured by Ansible - 2
                    enabled: false
                    index: 2
                  index: 2
          - config:
              description: configured by Ansible - 2
              enabled: false
              loopback-mode: false
              mtu: 2048
              name: loopback1111
              type: virt
            name: loopback1111
            subinterfaces:
              subinterface:
                - config:
                    description: subinterface configured by Ansible - 3
                    enabled: true
                    index: 10
                  index: 10
                - config:
                    description: subinterface configured by Ansible - 4
                    enabled: false
                    index: 3
                  index: 3

- name: Find the description of loopback111, subinterface index 10
  debug:
    msg: |-
      {{ data.interfaces.interface[int_idx|int]
          .subinterfaces.subinterface[subint_idx|int]
            .config.description }}
  vars:
    # the values to search for
    int_name: loopback1111
    sub_index: 10
    # retrieve the index in each nested list
    int_idx: |
      {{ lookup('ansible.utils.index_of',
             data.interfaces.interface,
                 'eq', int_name, 'name') }}
    subint_idx: |
      {{ lookup('ansible.utils.index_of',
             data.interfaces.interface[int_idx|int].subinterfaces.subinterface,
                 'eq', sub_index, 'index') }}

# TASK [Find the description of loopback111, subinterface index 10] ************
# ok: [sw01] =>
#   msg: subinterface configured by Ansible - 3
```

## [Return Value](index_of_lookup.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  string | One or more zero-based indicies of the matching list items.  See `wantlist` if a list is always required.  **Returned:** success |

### Authors

- Bradley Thornton (@cidrblock)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.utils/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.utils)
