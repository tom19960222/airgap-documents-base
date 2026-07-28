---
collection: ansible
version: "8"
title: "community.windows.win_computer_description module – Set windows description, owner and organization"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_computer_description_module.html
fetched_at: 2026-07-28T02:01:39+00:00
---
# community.windows.win_computer_description module – Set windows description, owner and organization

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/ui/repo/published/community/windows/) (version 1.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_computer_description`.

- [Synopsis](win_computer_description_module.md#synopsis)
- [Parameters](win_computer_description_module.md#parameters)
- [Examples](win_computer_description_module.md#examples)

## [Synopsis](win_computer_description_module.md#id1)

- This module sets Windows description that is shown under My Computer properties. Module also sets Windows license owner and organization. License information can be viewed by running winver commad.

## [Parameters](win_computer_description_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | String value to apply to Windows descripton. Specify value of “” to clear the value. |
| **organization**  string | String value of organization that the Windows is licensed to. Specify value of “” to clear the value. |
| **owner**  string | String value of the persona that the Windows is licensed to. Specify value of “” to clear the value. |

## [Examples](win_computer_description_module.md#id3)

```yaml+jinja
- name: Set Windows description, owner and organization
  community.windows.win_computer_description:
   description: Best Box
   owner: RusoSova
   organization: MyOrg
  register: result

- name: Set Windows description only
  community.windows.win_computer_description:
   description: This is my Windows machine
  register: result

- name: Set organization and clear owner field
  community.windows.win_computer_description:
   owner: ''
   organization: Black Mesa

- name: Clear organization, description and owner
  community.windows.win_computer_description:
   organization: ""
   owner: ""
   description: ""
  register: result
```

### Authors

- RusoSova (@RusoSova)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
