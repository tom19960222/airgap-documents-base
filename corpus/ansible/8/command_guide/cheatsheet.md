---
collection: ansible
version: "8"
title: "Ansible CLI cheatsheet"
source_url: https://docs.ansible.com/projects/ansible/8/command_guide/cheatsheet.html
fetched_at: 2026-07-28T00:58:31+00:00
---
# Ansible CLI cheatsheet

This page shows one or more examples of each Ansible command line utility with some common flags added and a link to the full documentation for the command.
This page offers a quick reminder of some common use cases only - it may be out of date or incomplete or both.
For canonical documentation, follow the links to the CLI pages.

- [ansible-playbook](cheatsheet.md#ansible-playbook)
- [ansible-galaxy](cheatsheet.md#ansible-galaxy)

## [ansible-playbook](cheatsheet.md#id1)

```bash
ansible-playbook -i /path/to/my_inventory_file -u my_connection_user -k -f 3 -T 30 -t my_tag -M /path/to/my_modules -b -K my_playbook.yml
```

Loads `my_playbook.yml` from the current working directory and:
:   - `-i` - uses `my_inventory_file` in the path provided for [inventory](../inventory_guide/intro_inventory.md#intro-inventory) to match the [pattern](../inventory_guide/intro_patterns.md#intro-patterns).
    - `-u` - connects [over SSH](../inventory_guide/connection_details.md#connections) as `my_connection_user`.
    - `-k` - asks for password which is then provided to SSH authentication.
    - `-f` - allocates 3 [forks](../playbook_guide/playbooks_strategies.md#playbooks-strategies).
    - `-T` - sets a 30-second timeout.
    - `-t` - runs only tasks marked with the [tag](../playbook_guide/playbooks_tags.md#tags) `my_tag`.
    - `-M` - loads [local modules](../dev_guide/developing_locally.md#developing-locally) from `/path/to/my/modules`.
    - `-b` - executes with elevated privileges (uses [become](../playbook_guide/playbooks_privilege_escalation.md#become)).
    - `-K` - prompts the user for the become password.

See [ansible-playbook](../cli/ansible-playbook.md#ansible-playbook) for detailed documentation.

## [ansible-galaxy](cheatsheet.md#id2)

Installing a collection:

```bash
ansible-galaxy collection install mynamespace.mycollection
```

Downloads `mynamespace.mycollection` from the configured Galaxy server ([galaxy.ansible.com](galaxy.ansible.com.md) by default).

Listing all installed collections:

```bash
ansible-galaxy collection list
```

See [ansible-galaxy](../cli/ansible-galaxy.md#ansible-galaxy) for detailed documentation.
