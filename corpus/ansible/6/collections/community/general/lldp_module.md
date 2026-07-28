---
collection: ansible
version: "6"
title: "community.general.lldp module – Get details reported by lldp"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/lldp_module.html
fetched_at: 2026-07-27T17:10:33+00:00
---
# community.general.lldp module – Get details reported by lldp

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](lldp_module.md#ansible-collections-community-general-lldp-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.lldp`.

- [Synopsis](lldp_module.md#synopsis)
- [Requirements](lldp_module.md#requirements)
- [Notes](lldp_module.md#notes)
- [Examples](lldp_module.md#examples)

## [Synopsis](lldp_module.md#id1)

- Reads data out of lldpctl

## [Requirements](lldp_module.md#id2)

The below requirements are needed on the host that executes this module.

- lldpctl

## [Notes](lldp_module.md#id3)

> **Note:**
>
> - Requires lldpd running and lldp enabled on switches

## [Examples](lldp_module.md#id4)

```yaml+jinja
# Retrieve switch/port information
 - name: Gather information from lldp
   community.general.lldp:

 - name: Print each switch/port
   ansible.builtin.debug:
    msg: "{{ lldp[item]['chassis']['name'] }} / {{ lldp[item]['port']['ifname'] }}"
   with_items: "{{ lldp.keys() }}"

# TASK: [Print each switch/port] ***********************************************************
# ok: [10.13.0.22] => (item=eth2) => {"item": "eth2", "msg": "switch1.example.com / Gi0/24"}
# ok: [10.13.0.22] => (item=eth1) => {"item": "eth1", "msg": "switch2.example.com / Gi0/3"}
# ok: [10.13.0.22] => (item=eth0) => {"item": "eth0", "msg": "switch3.example.com / Gi0/3"}
```

### Authors

- Andy Hill (@andyhky)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
