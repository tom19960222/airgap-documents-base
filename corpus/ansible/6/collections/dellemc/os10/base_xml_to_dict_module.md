---
collection: ansible
version: "6"
title: "dellemc.os10.base_xml_to_dict module – Operations for show command output convertion from xml to json format."
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/os10/base_xml_to_dict_module.html
fetched_at: 2026-07-27T17:25:57+00:00
---
# dellemc.os10.base_xml_to_dict module – Operations for show command output convertion from xml to json format.

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
> To use it in a playbook, specify: `dellemc.os10.base_xml_to_dict`.

- [Synopsis](base_xml_to_dict_module.md#synopsis)
- [Parameters](base_xml_to_dict_module.md#parameters)
- [Examples](base_xml_to_dict_module.md#examples)

## [Synopsis](base_xml_to_dict_module.md#id1)

- Get the show system inforamtion of a Leaf-Spine.

## [Parameters](base_xml_to_dict_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cli_responses**  string / required | show command xml output |

## [Examples](base_xml_to_dict_module.md#id3)

```yaml+jinja
Copy below YAML into a playbook (e.g. play.yml) and run as follows:

#$ ansible-playbook -i inv play.yml
name: setup the plabook to get show command output in dict format
hosts: localhost
connection: local
gather_facts: False
vars:
  cli:
    username: admin
    password: admin
tasks:
- name: "Get Dell EMC OS10 Show output in dict format"
  os10_command:
    commands: "{{ command_list }}"
  register: show
- debug: var=show
- name: call to lib to get output in dict
  base_xml_to_dict:
    cli_responses: "{{ item }}"
  loop: "{{ show.stdout }}"
```

### Authors

- Senthil Kumar Ganesan (@skg-net)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/dellemc.os10/issues)
[Repository (Sources)](https://github.com/ansible-collections/dellemc.os10)
