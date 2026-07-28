---
collection: ansible
version: "6"
title: "dellemc.os10.show_system_network_summary module – Operations for show_system_network output in json/yaml format."
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/os10/show_system_network_summary_module.html
fetched_at: 2026-07-27T17:26:01+00:00
---
# dellemc.os10.show_system_network_summary module – Operations for show_system_network output in json/yaml format.

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
> To use it in a playbook, specify: `dellemc.os10.show_system_network_summary`.

- [Synopsis](show_system_network_summary_module.md#synopsis)
- [Parameters](show_system_network_summary_module.md#parameters)
- [Examples](show_system_network_summary_module.md#examples)

## [Synopsis](show_system_network_summary_module.md#id1)

- Get the show system inforamtion of a Leaf-Spine.

## [Parameters](show_system_network_summary_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cli_responses**  list / elements=string / required | show system command xml output |
| **output_type**  string | json or yaml  Default value is json  Default: `"json"` |

## [Examples](show_system_network_summary_module.md#id3)

```yaml+jinja
Copy below YAML into a playbook (e.g. play.yml) and run as follows:

#$ ansible-playbook -i inv show.yml
name: show system Configuration
hosts: localhost
connection: local
gather_facts: False
vars:
  cli:
    username: admin
    password: admin
tasks:
- name: "Get Dell EMC OS10 Show system summary"
  os10_command:
    commands: ['show system | display-xml']
    provider: "{{ hostvars[item].cli }}"
  with_items: "{{ groups['all'] }}"
  register: show_system
- set_fact:
     output:  "{{ output|default([])+ [{'inv_name': item.item, 'host': item.invocation.module_args.provider.host, 'stdout_show_system': item.stdout}] }}"
  loop: "{{ show_system.results }}"
- debug: var=output
- name: "show system network call to lib "
  show_system_network_summary:
    cli_responses: "{{ output}} "
    output_type: "{{ output_method if output_method is defined else 'json' }}"
  register: show_system_network_summary
- debug: var=show_system_network_summary
```

### Authors

- Senthil Kumar Ganesan (@skg-net)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/dellemc.os10/issues)
[Repository (Sources)](https://github.com/ansible-collections/dellemc.os10)
