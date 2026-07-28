---
collection: ansible
version: "8"
title: "ansible.netcommon.parse_xml filter – The parse_xml filter plugin."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/netcommon/parse_xml_filter.html
fetched_at: 2026-07-28T01:04:55+00:00
---
# ansible.netcommon.parse_xml filter – The parse_xml filter plugin.

> **Note:**
>
> This filter plugin is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ui/repo/published/ansible/netcommon/) (version 5.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
>
> To use it in a playbook, specify: `ansible.netcommon.parse_xml`.

New in ansible.netcommon 1.0.0

- [Synopsis](parse_xml_filter.md#synopsis)
- [Keyword parameters](parse_xml_filter.md#keyword-parameters)
- [Notes](parse_xml_filter.md#notes)
- [Examples](parse_xml_filter.md#examples)

## [Synopsis](parse_xml_filter.md#id1)

- This filter will load the spec file and pass the command output through it, returning JSON output.
- The YAML spec file defines how to parse the CLI output.

## [Keyword parameters](parse_xml_filter.md#id2)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.netcommon.parse_xml(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **output**  any / required | This source xml on which parse_xml invokes. |
| **tmpl**  string | The spec file should be valid formatted YAML. It defines how to parse the XML output and return JSON data.  For example `xml_data | ansible.netcommon.parse_xml(template.yml`), in this case `xml_data` represents xml data option. |

## [Notes](parse_xml_filter.md#id3)

> **Note:**
>
> - To convert the XML output of a network device command into structured JSON output.

## [Examples](parse_xml_filter.md#id4)

```yaml+jinja
# Using parse_xml

# example_output.xml

# <?xml version="1.0" encoding="UTF-8"?>
# <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
#   <data>
#           <ntp>
#                   <nodes>
#                           <node>
#                                   <node>0/0/CPU0</node>
#                                   <associations>
#                                           <is-ntp-enabled>true</is-ntp-enabled>
#                                           <sys-leap>ntp-leap-no-warning</sys-leap>
#                                           <peer-summary-info>
#                                                   <peer-info-common>
#                                                           <host-mode>ntp-mode-client</host-mode>
#                                                           <is-configured>true</is-configured>
#                                                           <address>10.1.1.1</address>
#                                                           <reachability>0</reachability>
#                                                   </peer-info-common>
#                                                   <time-since>-1</time-since>
#                                           </peer-summary-info>
#                                           <peer-summary-info>
#                                                   <peer-info-common>
#                                                           <host-mode>ntp-mode-client</host-mode>
#                                                           <is-configured>true</is-configured>
#                                                           <address>172.16.252.29</address>
#                                                           <reachability>255</reachability>
#                                                   </peer-info-common>
#                                                   <time-since>991</time-since>
#                                           </peer-summary-info>
#                                   </associations>
#                           </node>
#                   </nodes>
#           </ntp>
#   </data>
# </rpc-reply>

# parse_xml.yml

# ---
# vars:
#   ntp_peers:
#     address: "{{ item.address }}"
#     reachability: "{{ item.reachability}}"
# keys:
#   result:
#     value: "{{ ntp_peers }}"
#     top: data/ntp/nodes/node/associations
#     items:
#       address: peer-summary-info/peer-info-common/address
#       reachability: peer-summary-info/peer-info-common/reachability

- name: Facts setup
  ansible.builtin.set_fact:
    xml: "{{ lookup('file', 'example_output.xml') }}"

- name: Parse xml invocation
  ansible.builtin.debug:
    msg: "{{ xml | ansible.netcommon.parse_xml('parse_xml.yml') }}"

# Task Output
# -----------
#
# TASK [set xml Data]
# ok: [host] => changed=false
#   ansible_facts:
#     xml: |-
#       <?xml version="1.0" encoding="UTF-8"?>
#       <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
#               <data>
#                       <ntp>
#                               <nodes>
#                                       <node>
#                                               <node>0/0/CPU0</node>
#                                               <associations>
#                                                       <is-ntp-enabled>true</is-ntp-enabled>
#                                                       <sys-leap>ntp-leap-no-warning</sys-leap>
#                                                       <peer-summary-info>
#                                                               <peer-info-common>
#                                                                       <host-mode>ntp-mode-client</host-mode>
#                                                                       <is-configured>true</is-configured>
#                                                                       <address>10.1.1.1</address>
#                                                                       <reachability>0</reachability>
#                                                               </peer-info-common>
#                                                               <time-since>-1</time-since>
#                                                       </peer-summary-info>
#                                                       <peer-summary-info>
#                                                               <peer-info-common>
#                                                                       <host-mode>ntp-mode-client</host-mode>
#                                                                       <is-configured>true</is-configured>
#                                                                       <address>172.16.252.29</address>
#                                                                       <reachability>255</reachability>
#                                                               </peer-info-common>
#                                                               <time-since>991</time-since>
#                                                       </peer-summary-info>
#                                               </associations>
#                                       </node>
#                               </nodes>
#                       </ntp>
#               </data>
#       </rpc-reply>

# TASK [Parse Data]
# ok: [host] => changed=false
#   ansible_facts:
#     output:
#       result:
#       - address:
#         - 10.1.1.1
#         - 172.16.252.29
#         reachability:
#         - '0'
#         - '255'
```

### Authors

- Ganesh Nalawade (@ganeshrn)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
