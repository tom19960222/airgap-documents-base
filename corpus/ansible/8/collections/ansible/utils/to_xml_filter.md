---
collection: ansible
version: "8"
title: "ansible.utils.to_xml filter – Convert given JSON string to XML"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/to_xml_filter.html
fetched_at: 2026-07-28T01:10:03+00:00
---
# ansible.utils.to_xml filter – Convert given JSON string to XML

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
> To use it in a playbook, specify: `ansible.utils.to_xml`.

New in ansible.utils 2.0.2

- [Synopsis](to_xml_filter.md#synopsis)
- [Keyword parameters](to_xml_filter.md#keyword-parameters)
- [Examples](to_xml_filter.md#examples)

## [Synopsis](to_xml_filter.md#id1)

- This plugin converts the JSON string to XML.
- Using the parameters below- `data|ansible.utils.to_xml`

## [Keyword parameters](to_xml_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.utils.to_xml(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **data**  dictionary / required | The input JSON string .  This option represents the JSON value that is passed to the filter plugin in pipe format.  For example `config_data|ansible.utils.to_xml`, in this case `config_data` represents this option. |
| **engine**  string | Conversion library to use within the filter plugin.  **Default:** `"xmltodict"` |
| **full_document**  boolean | The option to disable xml declaration(defaults to True).  **Choices:**   - `false` - `true` ← (default) |
| **indent**  string | The character used for indentation (defaults to tabs).  **Choices:**   - `"tabs"` ← (default) - `"spaces"` |
| **indent_width**  integer | The number of spaces to use to indent output data.  This option is only used when indent=”spaces”, otherwise it is ignored.  When indent=”tabs”, a single tab is always used for indentation.  **Default:** `4` |

## [Examples](to_xml_filter.md#id3)

```yaml+jinja
#### Simple examples with out any engine. plugin will use default value as xmltodict

- name: Define JSON data
  ansible.builtin.set_fact:
      data:
          "interface-configurations":
              "@xmlns": "http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg"
              "interface-configuration":
- debug:
      msg: "{{ data | ansible.utils.to_xml }}"

# TASK [Define JSON data ] *************************************************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_utils_json_to_xml.yaml:5
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": {
#             "interface-configurations": {
#                 "@xmlns": "http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg",
#                 "interface-configuration": null
#             }
#         }
#     },
#     "changed": false
# }
#
# TASK [debug] ***********************************************************************************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_utils_json_to_xml.yaml:13
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "msg": "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<interface-configurations xmlns=\"http://cisco.com/ns/yang/
#     Cisco-IOS-XR-ifmgr-cfg\">\n\t<interface-configuration></interface-configuration>\n</interface-configurations>"
# }

#### example2 with engine=xmltodict

- name: Define JSON data
  ansible.builtin.set_fact:
      data:
          "interface-configurations":
              "@xmlns": "http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg"
              "interface-configuration":
- debug:
      msg: "{{ data | ansible.utils.to_xml('xmltodict') }}"

# TASK [Define JSON data ] *************************************************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_utils_json_to_xml.yaml:5
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": {
#             "interface-configurations": {
#                 "@xmlns": "http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg",
#                 "interface-configuration": null
#             }
#         }
#     },
#     "changed": false
# }
# TASK [debug] ***********************************************************************************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_utils_json_to_xml.yaml:13
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "msg": "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<interface-configurations xmlns=\"http://cisco.com/ns/yang/
#     Cisco-IOS-XR-ifmgr-cfg\">\n\t<interface-configuration></interface-configuration>\n</interface-configurations>"
# }

#### example3 with indent='spaces' and indent_width=2

- name: Define JSON data
  ansible.builtin.set_fact:
      data:
          "interface-configurations":
              "@xmlns": "http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg"
              "interface-configuration":
- debug:
      msg: "{{ data | ansible.utils.to_xml(indent='spaces', indent_width=2) }}"

# TASK [Define JSON data ] *************************************************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_utils_json_to_xml.yaml:5
# ok: [localhost] => {
#     "ansible_facts": {
#         "data": {
#             "interface-configurations": {
#                 "@xmlns": "http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg",
#                 "interface-configuration": null
#             }
#         }
#     },
#     "changed": false
# }
# TASK [debug] ***********************************************************************************************************
# task path: /Users/amhatre/ansible-collections/playbooks/test_utils_json_to_xml.yaml:13
# Loading collection ansible.utils from /Users/amhatre/ansible-collections/collections/ansible_collections/ansible/utils
# ok: [localhost] => {
#     "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<interface-configurations xmlns=\"http://cisco.com/ns/yang/
#     Cisco-IOS-XR-ifmgr-cfg\">\n  <interface-configuration></interface-configuration>\n</interface-configurations>"
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
