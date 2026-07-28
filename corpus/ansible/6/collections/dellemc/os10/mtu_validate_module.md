---
collection: ansible
version: "6"
title: "dellemc.os10.mtu_validate module – Validate the MTU value for lldp neighbors"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/os10/mtu_validate_module.html
fetched_at: 2026-07-27T17:25:59+00:00
---
# dellemc.os10.mtu_validate module – Validate the MTU value for lldp neighbors

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
> To use it in a playbook, specify: `dellemc.os10.mtu_validate`.

- [Synopsis](mtu_validate_module.md#synopsis)
- [Parameters](mtu_validate_module.md#parameters)
- [Examples](mtu_validate_module.md#examples)

## [Synopsis](mtu_validate_module.md#id1)

- Get the wiring info using lldp output and show system network summary.

## [Parameters](mtu_validate_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **show_ip_intf_brief**  list / elements=string / required | show ip intf brief |
| **show_lldp_neighbors_list**  list / elements=string / required | show lldp neighbor output |
| **show_system_network_summary**  list / elements=string / required | show system network summary output |

## [Examples](mtu_validate_module.md#id3)

```yaml+jinja
Copy below YAML into a playbook (e.g. play.yml) and run follows:

#$ ansible-playbook -i inv play.yml
name: show mtu mismatch info
hosts: localhost
connection: local
gather_facts: False
tasks:
 - name: "Get Dell EMC OS10 MTU mismatch info"
   os10_command:
     commands:
       - command: "show lldp neighbors"
       - command: "show ip interface brief | display-xml"
     provider: "{{ hostvars[item].cli }}"
   with_items: "{{ groups['all'] }}"
   register: show_lldp
 - set_fact:
      output:  "{{ output|default([])+ [{'host': item.invocation.module_args.provider.host, 'inv_name': item.item,
                                         'stdout_show_lldp': item.stdout.0, 'stdout_show_ip': item.stdout.1 }] }}"
   loop: "{{ show_lldp.results }}"
 - debug: var=output
 - local_action: copy content={{ output }} dest=show1
 - name: call lib to convert ip interface info from xml to dict format
   base_xml_to_dict:
      cli_responses: "{{ item.stdout_show_ip }}"
   with_items: "{{ output }}"
   register: show_ip_intf_list
 - local_action: copy content={{ show_ip_intf_list }} dest=show_ip

 - name: "Get Dell EMC OS10 Show system"
   import_role:
     name: os10_fabric_summary
   register: show_system_network_summary
 - debug: var=show_system_network_summary
 - name: call lib to process
   mtu_validate:
     show_lldp_neighbors_list: "{{ output }}"
     show_system_network_summary: "{{ show_system_network_summary.msg.results }}"
     show_ip_intf_brief: "{{ show_ip_intf_list.results }}"
```

### Authors

- Senthil Kumar Ganesan (@skg-net)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/dellemc.os10/issues)
[Repository (Sources)](https://github.com/ansible-collections/dellemc.os10)
