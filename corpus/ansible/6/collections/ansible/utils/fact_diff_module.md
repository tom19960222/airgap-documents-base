---
collection: ansible
version: "6"
title: "ansible.utils.fact_diff module – Find the difference between currently set facts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/utils/fact_diff_module.html
fetched_at: 2026-07-27T16:44:49+00:00
---
# ansible.utils.fact_diff module – Find the difference between currently set facts

> **Note:**
>
> This module is part of the [ansible.utils collection](https://galaxy.ansible.com/ansible/utils) (version 2.8.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.utils`.
>
> To use it in a playbook, specify: `ansible.utils.fact_diff`.

New in ansible.utils 1.0.0

- [Synopsis](fact_diff_module.md#synopsis)
- [Parameters](fact_diff_module.md#parameters)
- [Examples](fact_diff_module.md#examples)
- [Return Values](fact_diff_module.md#return-values)

## [Synopsis](fact_diff_module.md#id1)

- Compare two facts or variables and get a diff.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](fact_diff_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **after**  any / required | The second fact to be used in the comparison. |
| **before**  any / required | The first fact to be used in the comparison. |
| **plugin**  dictionary | Configure and specify the diff plugin to use  Default: `{}` |
| **name**  string | The diff plugin to use, in fully qualified collection name format.  Default: `"ansible.utils.native"` |
| **vars**  dictionary | Parameters passed to the diff plugin.  Default: `{}` |
| **skip_lines**  list / elements=string | Skip lines matching these regular expressions.  Matches will be removed prior to the diff.  If the provided *before* and *after* are a string, they will be split.  Each entry in each list will be cast to a string for the comparison |

## [Examples](fact_diff_module.md#id3)

```yaml+jinja
- ansible.builtin.set_fact:
    before:
      a:
        b:
          c:
            d:
            - 0
            - 1
    after:
      a:
        b:
          c:
            d:
            - 2
            - 3

- name: Show the difference in json format
  ansible.utils.fact_diff:
    before: "{{ before }}"
    after: "{{ after }}"

# TASK [ansible.utils.fact_diff] **************************************
# --- before
# +++ after
# @@ -3,8 +3,8 @@
#          "b": {
#              "c": {
#                  "d": [
# -                    0,
# -                    1
# +                    2,
# +                    3
#                  ]
#              }
#          }
#
# changed: [localhost]

- name: Show the difference in path format
  ansible.utils.fact_diff:
    before: "{{ before|ansible.utils.to_paths }}"
    after: "{{ after|ansible.utils.to_paths }}"

# TASK [ansible.utils.fact_diff] **************************************
# --- before
# +++ after
# @@ -1,4 +1,4 @@
#  {
# -    "a.b.c.d[0]": 0,
# -    "a.b.c.d[1]": 1
# +    "a.b.c.d[0]": 2,
# +    "a.b.c.d[1]": 3
#  }
#
# changed: [localhost]

- name: Show the difference in yaml format
  ansible.utils.fact_diff:
    before: "{{ before|to_nice_yaml }}"
    after: "{{ after|to_nice_yaml }}"

# TASK [ansible.utils.fact_diff] **************************************
# --- before
# +++ after
# @@ -2,5 +2,5 @@
#      b:
#          c:
#              d:
# -            - 0
# -            - 1
# +            - 2
# +            - 3

# changed: [localhost]

#### Show the difference between complex object using restconf
#  ansible_connection: ansible.netcommon.httpapi
#  ansible_httpapi_use_ssl: True
#  ansible_httpapi_validate_certs: False
#  ansible_network_os: ansible.netcommon.restconf

- name: Get the current interface config prior to changes
  ansible.netcommon.restconf_get:
    content: config
    path: /data/Cisco-NX-OS-device:System/intf-items/phys-items
  register: pre

- name: Update the description of eth1/100
  ansible.utils.update_fact:
    updates:
    - path: "pre['response']['phys-items']['PhysIf-list'][{{ index }}]['descr']"
      value: "Configured by ansible {{ 100 | random }}"
  vars:
    index: "{{ pre['response']['phys-items']['PhysIf-list']|ansible.utils.index_of('eq', 'eth1/100', 'id') }}"
  register: updated

- name: Apply the configuration
  ansible.netcommon.restconf_config:
    path: 'data/Cisco-NX-OS-device:System/intf-items/'
    content: "{{ updated.pre.response}}"
    method: patch

- name: Get the current interface config after changes
  ansible.netcommon.restconf_get:
    content: config
    path: /data/Cisco-NX-OS-device:System/intf-items/phys-items
  register: post

- name: Show the difference
  ansible.utils.fact_diff:
    before: "{{ pre.response|ansible.utils.to_paths }}"
    after: "{{ post.response|ansible.utils.to_paths }}"

# TASK [ansible.utils.fact_diff] *********************************************
# --- before
# +++ after
# @@ -3604,7 +3604,7 @@
#      "phys-items['PhysIf-list'][37].bw": "0",
#      "phys-items['PhysIf-list'][37].controllerId": "",
#      "phys-items['PhysIf-list'][37].delay": "1",
# -    "phys-items['PhysIf-list'][37].descr": "Configured by ansible 95",
# +    "phys-items['PhysIf-list'][37].descr": "Configured by ansible 20",
#      "phys-items['PhysIf-list'][37].dot1qEtherType": "0x8100",
#      "phys-items['PhysIf-list'][37].duplex": "auto",
#      "phys-items['PhysIf-list'][37].id": "eth1/100",

# changed: [nxos101]
```

## [Return Values](fact_diff_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **diff_lines**  list / elements=string | The *diff_text* split into lines.  Returned: always |
| **diff_text**  string | The diff in text format.  Returned: always |

### Authors

- Bradley Thornton (@cidrblock)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.utils/issues)
[Repository (Sources)](https://github.com/ansible-collections/ansible.utils)
