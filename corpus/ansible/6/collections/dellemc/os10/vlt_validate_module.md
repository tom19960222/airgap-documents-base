---
collection: ansible
version: "6"
title: "dellemc.os10.vlt_validate module – Validate the vlt info, raise an error if peer is not in up state"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/os10/vlt_validate_module.html
fetched_at: 2026-07-27T17:26:02+00:00
---
# dellemc.os10.vlt_validate module – Validate the vlt info, raise an error if peer is not in up state

> **Note:**
>
> This module is part of the [dellemc.os10 collection](https://galaxy.ansible.com/dellemc/os10) (version 1.1.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.os10`.
>
> To use it in a playbook, specify: `dellemc.os10.vlt_validate`.

- [Synopsis](vlt_validate_module.md#synopsis)
- [Parameters](vlt_validate_module.md#parameters)
- [Examples](vlt_validate_module.md#examples)

## [Synopsis](vlt_validate_module.md#id1)

- Troubleshoot the show vlt info and raise an error if peer is not up.

## [Parameters](vlt_validate_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **intended_vlt_pairs**  list / elements=string / required | intended vlt pair intput to verify with actual |
| **show_system_network_summary**  list / elements=string / required | show system summary output |
| **show_vlt**  list / elements=string / required | show vlt output |

## [Examples](vlt_validate_module.md#id3)

```yaml+jinja
Copy below YAML into a playbook (e.g. play.yml) and run as follows:

#$ ansible-playbook -i inv play.yml
name: show system Configuration
hosts: localhost
connection: local
gather_facts: False
tasks:
 - name: "Get Dell EMC OS10 Show run vlt"
   os10_command:
     commands:
       - command: "show running-configuration vlt | grep vlt-domain"
     provider: "{{ hostvars[item].cli }}"
   with_items: "{{ groups['all'] }}"
   register: show_run_vlt
 - set_fact:
      output_vlt:  "{{ output_vlt|default([])+ [{'host': item.invocation.module_args.provider.host, 'inv_name': item.item,
                                                 'stdout_show_vlt': item.stdout.0}] }}"
   loop: "{{ show_run_vlt.results }}"
 - debug: var=output_vlt
 - name: "Get Dell EMC OS10 Show vlt info"
   os10_command:
     commands:
       - command: "show vlt {{ item.stdout_show_vlt.split()[1] }} | display-xml"
     provider: "{{ hostvars[item.inv_name].cli }}"
   with_items: "{{ output_vlt }}"
   register: show_vlt
 - set_fact:
      vlt_out:  "{{ vlt_out|default([])+ [{'host': item.invocation.module_args.provider.host, 'inv_name': item.item, 'show_vlt_stdout': item.stdout.0}] }}"
   loop: "{{ show_vlt.results }}"
   register: vlt_output
 - name: call lib to convert vlt info from xml to dict format
   base_xml_to_dict:
      cli_responses: "{{ item.show_vlt_stdout }}"
   with_items:
     - "{{ vlt_out }}"
   register: vlt_dict_output
 - name: "Get Dell EMC OS10 Show system"
   import_role:
     name: os10_fabric_summary
   register: show_system_network_summary
 - name: call lib to process
   vlt_validate:
       show_vlt : "{{ vlt_dict_output.results }}"
       show_system_network_summary: "{{ show_system_network_summary.msg.results }}"
       intended_vlt_pairs: "{{ intended_vlt_pairs }}"
   register: show_vlt_info
```

### Authors

- Senthil Kumar Ganesan (@skg-net)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/dellemc.os10/issues)
[Repository (Sources)](https://github.com/ansible-collections/dellemc.os10)
