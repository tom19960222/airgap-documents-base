---
collection: ansible
version: "8"
title: "ansible.utils.from_xml filter – Convert given XML string to native python dictionary."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/from_xml_filter.html
fetched_at: 2026-07-28T01:09:45+00:00
---
# ansible.utils.from_xml filter – Convert given XML string to native python dictionary.

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
> To use it in a playbook, specify: `ansible.utils.from_xml`.

New in ansible.utils 2.0.2

- [Synopsis](from_xml_filter.md#synopsis)
- [Keyword parameters](from_xml_filter.md#keyword-parameters)
- [Examples](from_xml_filter.md#examples)

## [Synopsis](from_xml_filter.md#id1)

- This plugin converts the XML string to a native python dictionary.
- Using the parameters below- `data|ansible.utils.from_xml`

## [Keyword parameters](from_xml_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.utils.from_xml(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **data**  string / required | The input XML string.  This option represents the XML value that is passed to the filter plugin in pipe format.  For example `config_data|ansible.utils.from_xml`, in this case `config_data` represents this option. |
| **engine**  string | Conversion library to use within the filter plugin.  **Default:** `"xmltodict"` |

## [Examples](from_xml_filter.md#id3)

```yaml+jinja
#### Simple examples with out any engine. plugin will use default value as xmltodict

- name: convert given XML to native python dictionary
  ansible.builtin.set_fact:
    data: ' <netconf-state xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring"><schemas><schema/></schemas></netconf-state> '
- debug:
    msg: '{{ data|ansible.utils.from_xml }}'

# TASK######
# TASK [convert given XML to native python dictionary] *****************************************************************************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_utils.yaml:5
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": " <netconf-state xmlns=\"urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring\"><schemas><schema/></schemas></netconf-state> "
#     },
#     "changed": false
# }
#
# TASK [debug] *************************************************************************************************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_utils.yaml:13
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "msg": {
#         "netconf-state": {
#             "@xmlns": "urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring",
#             "schemas": {
#                 "schema": null
#             }
#         }
#     }
# }

#### example2 with engine=xmltodict

- name: convert given XML to native python dictionary
  ansible.builtin.set_fact:
    data: ' <netconf-state xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring"><schemas><schema/></schemas></netconf-state> '
- debug:
    msg: '{{ data|ansible.utils.from_xml(''xmltodict'') }}'

# TASK######
# TASK [convert given XML to native python dictionary] *****************************************************************************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_utils.yaml:5
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": " <netconf-state xmlns=\"urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring\"><schemas><schema/></schemas></netconf-state> "
#     },
#     "changed": false
# }
#
# TASK [debug] *************************************************************************************************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_utils.yaml:13
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "msg": {
#         "netconf-state": {
#             "@xmlns": "urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring",
#             "schemas": {
#                 "schema": null
#             }
#         }
#     }
# }
```

### Authors

- Ashwini Mhatre (@amhatre)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.utils/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.utils)
