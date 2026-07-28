---
collection: ansible
version: "8"
title: "community.general.xenserver_facts module – Get facts reported on xenserver"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/xenserver_facts_module.html
fetched_at: 2026-07-28T01:51:29+00:00
---
# community.general.xenserver_facts module – Get facts reported on xenserver

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.xenserver_facts`.

- [Synopsis](xenserver_facts_module.md#synopsis)
- [Attributes](xenserver_facts_module.md#attributes)
- [Examples](xenserver_facts_module.md#examples)

## [Synopsis](xenserver_facts_module.md#id1)

- Reads data out of XenAPI, can be used instead of multiple xe commands.

Aliases: cloud.misc.xenserver_facts

## [Attributes](xenserver_facts_module.md#id2)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  *added in community.general 3.3.0*  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |
| **facts** | **Support:** **full** | Action returns an `ansible_facts` dictionary that will update existing host facts. |

## [Examples](xenserver_facts_module.md#id3)

```yaml+jinja
- name: Gather facts from xenserver
  community.general.xenserver_facts:

- name: Print running VMs
  ansible.builtin.debug:
    msg: "{{ item }}"
  with_items: "{{ xs_vms.keys() }}"
  when: xs_vms[item]['power_state'] == "Running"

# Which will print:
#
# TASK: [Print running VMs] ***********************************************************
# skipping: [10.13.0.22] => (item=CentOS 4.7 (32-bit))
# ok: [10.13.0.22] => (item=Control domain on host: 10.0.13.22) => {
#     "item": "Control domain on host: 10.0.13.22",
#     "msg": "Control domain on host: 10.0.13.22"
# }
```

### Authors

- Andy Hill (@andyhky)
- Tim Rupp (@caphrim007)
- Robin Lee (@cheese)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
