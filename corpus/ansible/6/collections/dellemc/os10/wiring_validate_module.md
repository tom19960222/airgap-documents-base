---
collection: ansible
version: "6"
title: "dellemc.os10.wiring_validate module – Validate the wiring based on the planned wiring details"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/os10/wiring_validate_module.html
fetched_at: 2026-07-27T17:26:03+00:00
---
# dellemc.os10.wiring_validate module – Validate the wiring based on the planned wiring details

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
> To use it in a playbook, specify: `dellemc.os10.wiring_validate`.

- [Synopsis](wiring_validate_module.md#synopsis)
- [Parameters](wiring_validate_module.md#parameters)
- [Examples](wiring_validate_module.md#examples)

## [Synopsis](wiring_validate_module.md#id1)

- Get the wiring info using lldp output and show system network summary.

## [Parameters](wiring_validate_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **planned_neighbors**  list / elements=string / required | planned neighbours input from group_var to compare actual |
| **show_lldp_neighbors_list**  list / elements=string / required | show lldp neighbor output |
| **show_system_network_summary**  list / elements=string / required | show system network summary output |

## [Examples](wiring_validate_module.md#id3)

```yaml+jinja
Copy below YAML into a playbook (e.g. play.yml) and run as follows:

#$ ansible-playbook -i inv play.yml
name: show system Configuration
hosts: localhost
connection: local
gather_facts: False
tasks:
- name: "Get Dell EMC OS10 Show lldp"
  os10_command:
    commands:
      - command: "show lldp neighbors"
    provider: "{{ hostvars[item].cli }}"
  with_items: "{{ groups['all'] }}"
  register: show_lldp
- local_action: copy content={{ show_lldp }} dest=show
- set_fact:
     output_lldp:  "{{ output_lldp|default([])+ [{'host': item.invocation.module_args.provider.host, 'inv_name': item.item,
                                                  'stdout_show_lldp': item.stdout}] }}"
  loop: "{{ show_lldp.results }}"
- debug: var=output_lldp
- name: "Get Dell EMC OS10 Show system"
  import_role:
    name: os10_fabric_summary
  register: show_system_network_summary
- debug: var=show_system_network_summary
- name: call lib to process
  wiring_validate:
    show_lldp_neighbors_list: "{{ output_lldp }}"
    show_system_network_summary: "{{ show_system_network_summary.msg.results }}"
    planned_neighbors: "{{ intended_neighbors }}"
```

### Authors

- Senthil Kumar Ganesan (@skg-net)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/dellemc.os10/issues)
[Repository (Sources)](https://github.com/ansible-collections/dellemc.os10)
