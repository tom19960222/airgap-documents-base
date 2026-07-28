---
collection: ansible
version: "6"
title: "ansible.posix.selinux module – Change policy and state of SELinux"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/posix/selinux_module.html
fetched_at: 2026-07-27T16:44:44+00:00
---
# ansible.posix.selinux module – Change policy and state of SELinux

> **Note:**
>
> This module is part of the [ansible.posix collection](https://galaxy.ansible.com/ansible/posix) (version 1.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.posix`.
> You need further requirements to be able to use this module,
> see [Requirements](selinux_module.md#ansible-collections-ansible-posix-selinux-module-requirements) for details.
>
> To use it in a playbook, specify: `ansible.posix.selinux`.

New in ansible.posix 1.0.0

- [Synopsis](selinux_module.md#synopsis)
- [Requirements](selinux_module.md#requirements)
- [Parameters](selinux_module.md#parameters)
- [Examples](selinux_module.md#examples)
- [Return Values](selinux_module.md#return-values)

## [Synopsis](selinux_module.md#id1)

- Configures the SELinux mode and policy.
- A reboot may be required after usage.
- Ansible will not issue this reboot but will let you know when it is required.

## [Requirements](selinux_module.md#id2)

The below requirements are needed on the host that executes this module.

- libselinux-python

## [Parameters](selinux_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **configfile**  aliases: conf, file  string | The path to the SELinux configuration file, if non-standard.  Default: `"/etc/selinux/config"` |
| **policy**  string | The name of the SELinux policy to use (e.g. `targeted`) will be required if *state* is not `disabled`. |
| **state**  string / required | The SELinux mode.  Choices:   - `"disabled"` - `"enforcing"` - `"permissive"` |
| **update_kernel_param**  boolean  added in ansible.posix 1.4.0 | If set to *true*, will update also the kernel boot parameters when disabling/enabling SELinux.  The `grubby` tool must be present on the target system for this to work.  Choices:   - `false` ← (default) - `true` |

## [Examples](selinux_module.md#id4)

```yaml+jinja
- name: Enable SELinux
  ansible.posix.selinux:
    policy: targeted
    state: enforcing

- name: Put SELinux in permissive mode, logging actions that would be blocked.
  ansible.posix.selinux:
    policy: targeted
    state: permissive

- name: Disable SELinux
  ansible.posix.selinux:
    state: disabled
```

## [Return Values](selinux_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **configfile**  string | Path to SELinux configuration file.  Returned: always  Sample: `"/etc/selinux/config"` |
| **msg**  string | Messages that describe changes that were made.  Returned: always  Sample: `"Config SELinux state changed from 'disabled' to 'permissive'"` |
| **policy**  string | Name of the SELinux policy.  Returned: always  Sample: `"targeted"` |
| **reboot_required**  boolean | Whether or not an reboot is required for the changes to take effect.  Returned: always  Sample: `true` |
| **state**  string | SELinux mode.  Returned: always  Sample: `"enforcing"` |

### Authors

- Derek Carter (@goozbach)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.posix)
[Repository (Sources)](https://github.com/ansible-collections/ansible.posix)
