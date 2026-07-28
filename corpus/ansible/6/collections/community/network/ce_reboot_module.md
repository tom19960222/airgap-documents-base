---
collection: ansible
version: "6"
title: "community.network.ce_reboot module – Reboot a HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_reboot_module.html
fetched_at: 2026-07-27T17:17:47+00:00
---
# community.network.ce_reboot module – Reboot a HUAWEI CloudEngine switches.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
> You need further requirements to be able to use this module,
> see [Requirements](ce_reboot_module.md#ansible-collections-community-network-ce-reboot-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.ce_reboot`.

- [Synopsis](ce_reboot_module.md#synopsis)
- [Requirements](ce_reboot_module.md#requirements)
- [Parameters](ce_reboot_module.md#parameters)
- [Notes](ce_reboot_module.md#notes)
- [Examples](ce_reboot_module.md#examples)
- [Return Values](ce_reboot_module.md#return-values)

## [Synopsis](ce_reboot_module.md#id1)

- Reboot a HUAWEI CloudEngine switches.

## [Requirements](ce_reboot_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient

## [Parameters](ce_reboot_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **confirm**  boolean / required | Safeguard boolean. Set to true if you’re sure you want to reboot.  Choices:   - `false` - `true` |
| **save_config**  boolean | Flag indicating whether to save the configuration.  Choices:   - `false` ← (default) - `true` |

## [Notes](ce_reboot_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_reboot_module.md#id5)

```yaml+jinja
- name: Reboot module test
  hosts: cloudengine
  connection: local
  gather_facts: no
  vars:
    cli:
      host: "{{ inventory_hostname }}"
      port: "{{ ansible_ssh_port }}"
      username: "{{ username }}"
      password: "{{ password }}"
      transport: cli

  tasks:
  - name: Reboot the device
    community.network.ce_reboot:
      confirm: true
      save_config: true
      provider: "{{ cli }}"
```

## [Return Values](ce_reboot_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **rebooted**  boolean | Whether the device was instructed to reboot.  Returned: success  Sample: `true` |

### Authors

- Gong Jianjun (@QijunPan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
