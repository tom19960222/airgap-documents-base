---
collection: ansible
version: "6"
title: "community.general.profitbricks_volume_attachments module – Attach or detach a volume"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/profitbricks_volume_attachments_module.html
fetched_at: 2026-07-27T17:12:05+00:00
---
# community.general.profitbricks_volume_attachments module – Attach or detach a volume

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
> see [Requirements](profitbricks_volume_attachments_module.md#ansible-collections-community-general-profitbricks-volume-attachments-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.profitbricks_volume_attachments`.

- [Synopsis](profitbricks_volume_attachments_module.md#synopsis)
- [Requirements](profitbricks_volume_attachments_module.md#requirements)
- [Parameters](profitbricks_volume_attachments_module.md#parameters)
- [Examples](profitbricks_volume_attachments_module.md#examples)

## [Synopsis](profitbricks_volume_attachments_module.md#id1)

- Allows you to attach or detach a volume from a ProfitBricks server. This module has a dependency on profitbricks >= 1.0.0

## [Requirements](profitbricks_volume_attachments_module.md#id2)

The below requirements are needed on the host that executes this module.

- profitbricks

## [Parameters](profitbricks_volume_attachments_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **datacenter**  string | The datacenter in which to operate. |
| **server**  string | The name of the server you wish to detach or attach the volume. |
| **state**  string | Indicate desired state of the resource  The available choices are: `present`, `absent`.  Default: `"present"` |
| **subscription_password**  string | THe ProfitBricks password. Overrides the PB_PASSWORD environment variable. |
| **subscription_user**  string | The ProfitBricks username. Overrides the PB_SUBSCRIPTION_ID environment variable. |
| **volume**  string | The volume name or ID. |
| **wait**  boolean | wait for the operation to complete before returning  Choices:   - `false` - `true` ← (default) |
| **wait_timeout**  integer | how long before wait gives up, in seconds  Default: `600` |

## [Examples](profitbricks_volume_attachments_module.md#id4)

```yaml+jinja
- name: Attach a volume
  community.general.profitbricks_volume_attachments:
    datacenter: Tardis One
    server: node002
    volume: vol01
    wait_timeout: 500
    state: present

- name: Detach a volume
  community.general.profitbricks_volume_attachments:
    datacenter: Tardis One
    server: node002
    volume: vol01
    wait_timeout: 500
    state: absent
```

### Authors

- Matt Baldwin (@baldwinSPC)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
