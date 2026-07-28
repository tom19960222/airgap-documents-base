---
collection: ansible
version: "6"
title: "community.general.xenserver_facts module – Get facts reported on xenserver"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/xenserver_facts_module.html
fetched_at: 2026-07-27T17:14:04+00:00
---
# community.general.xenserver_facts module – Get facts reported on xenserver

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.xenserver_facts`.

- [Synopsis](xenserver_facts_module.md#synopsis)
- [Examples](xenserver_facts_module.md#examples)

## [Synopsis](xenserver_facts_module.md#id1)

- Reads data out of XenAPI, can be used instead of multiple xe commands.

## [Examples](xenserver_facts_module.md#id2)

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

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
