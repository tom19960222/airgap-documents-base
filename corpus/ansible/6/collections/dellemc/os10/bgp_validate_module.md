---
collection: ansible
version: "6"
title: "dellemc.os10.bgp_validate module – Validate the bgp neighbor state,raise error if it is not in established state"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/os10/bgp_validate_module.html
fetched_at: 2026-07-27T17:25:58+00:00
---
# dellemc.os10.bgp_validate module – Validate the bgp neighbor state,raise error if it is not in established state

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
> To use it in a playbook, specify: `dellemc.os10.bgp_validate`.

- [Synopsis](bgp_validate_module.md#synopsis)
- [Parameters](bgp_validate_module.md#parameters)
- [Examples](bgp_validate_module.md#examples)

## [Synopsis](bgp_validate_module.md#id1)

- Troubleshoot the bgp neighor state info using show ip bgp summary and show ip interface brief.

## [Parameters](bgp_validate_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bgp_neighbors**  list / elements=string / required | planned neighbours input from group_var to compare actual |
| **show_ip_bgp**  list / elements=string / required | show ip bgp summary output |
| **show_ip_intf_brief**  list / elements=string / required | show ip interface brief output |

## [Examples](bgp_validate_module.md#id3)

```yaml+jinja
Copy below YAML into a playbook (e.g. play.yml) and run as follows:

#$ ansible-playbook -i inv play.yml
name: Validate BGP configuration
hosts: localhost
connection: local
gather_facts: False
tasks:
  - name: "Get Dell EMC OS10 Show ip bgp summary"
    os10_command:
      commands:
        - command: "show ip bgp summary | display-xml"
        - command: "show ip interface brief | display-xml"
      provider: "{{ hostvars[item].cli }}"
    with_items: "{{ groups['all'] }}"
    register: show_bgp
  - set_fact:
       output_bgp:  "{{ output_bgp|default([])+ [{'host': item.invocation.module_args.provider.host, 'inv_name': item.item,
                                                  'stdout_show_bgp': item.stdout.0, 'stdout_show_ip': item.stdout.1}] }}"
    loop: "{{ show_bgp.results }}"
  - debug: var=output_bgp
  - local_action: copy content={{ output_bgp }} dest=show
  - name: call lib to convert bgp info from xml to dict format
    base_xml_to_dict:
       cli_responses: "{{ item.stdout_show_bgp }}"
    with_items:
      - "{{ output_bgp }}"
    register: show_bgp_list
  - name: call lib to convert ip interface info from xml to dict format
    base_xml_to_dict:
       cli_responses: "{{ item.stdout_show_ip }}"
    with_items:
      - "{{ output_bgp }}"
    register: show_ip_intf_list
  - name: call lib for bgp validation
    bgp_validate:
      show_ip_bgp: "{{ show_bgp_list.results  }}"
      show_ip_intf_brief: "{{ show_ip_intf_list.results  }}"
      bgp_neighbors: "{{ intended_bgp_neighbors }}"
```

### Authors

- Senthil Kumar Ganesan (@skg-net)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/dellemc.os10/issues)
[Repository (Sources)](https://github.com/ansible-collections/dellemc.os10)
