---
collection: ansible
version: "6"
title: "ibm.qradar.offense_note module – Create or update a QRadar Offense Note"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ibm/qradar/offense_note_module.html
fetched_at: 2026-07-27T17:50:15+00:00
---
# ibm.qradar.offense_note module – Create or update a QRadar Offense Note

> **Note:**
>
> This module is part of the [ibm.qradar collection](https://galaxy.ansible.com/ibm/qradar) (version 2.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ibm.qradar`.
>
> To use it in a playbook, specify: `ibm.qradar.offense_note`.

New in ibm.qradar 1.0.0

- [Synopsis](offense_note_module.md#synopsis)
- [Parameters](offense_note_module.md#parameters)
- [Examples](offense_note_module.md#examples)

## [Synopsis](offense_note_module.md#id1)

- This module allows to create a QRadar Offense note

## [Parameters](offense_note_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **id**  integer / required | Offense ID to operate on |
| **note_text**  string / required | The note’s text contents |

## [Examples](offense_note_module.md#id3)

```yaml+jinja
- name: Add a note to QRadar Offense ID 1
  ibm.qradar.offense_note:
    id: 1
    note_text: This an example note entry that should be made on offense id 1
```

### Authors

- Ansible Security Automation Team (@maxamillion) <<https://github.com/ansible-security>>

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ibm.qradar/issues)
[Repository (Sources)](https://github.com/ansible-collections/ibm.qradar)
