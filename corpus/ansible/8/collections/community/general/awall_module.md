---
collection: ansible
version: "8"
title: "community.general.awall module – Manage awall policies"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/awall_module.html
fetched_at: 2026-07-28T01:44:46+00:00
---
# community.general.awall module – Manage awall policies

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
> To use it in a playbook, specify: `community.general.awall`.

- [Synopsis](awall_module.md#synopsis)
- [Parameters](awall_module.md#parameters)
- [Attributes](awall_module.md#attributes)
- [Notes](awall_module.md#notes)
- [Examples](awall_module.md#examples)

## [Synopsis](awall_module.md#id1)

- This modules allows for enable/disable/activate of `awall` policies.
- Alpine Wall (`awall`) generates a firewall configuration from the enabled policy files and activates the configuration on the system.

Aliases: system.awall

## [Parameters](awall_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **activate**  boolean | Activate the new firewall rules.  Can be run with other steps or on its own.  Idempotency is affected if `activate=true`, as the module will always report a changed state.  **Choices:**   - `false` ← (default) - `true` |
| **name**  list / elements=string | One or more policy names. |
| **state**  string | Whether the policies should be enabled or disabled.  **Choices:**   - `"disabled"` - `"enabled"` ← (default) |

## [Attributes](awall_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](awall_module.md#id4)

> **Note:**
>
> - At least one of `name` and `activate` is required.

## [Examples](awall_module.md#id5)

```yaml+jinja
- name: Enable "foo" and "bar" policy
  community.general.awall:
    name: [ foo bar ]
    state: enabled

- name: Disable "foo" and "bar" policy and activate new rules
  community.general.awall:
    name:
    - foo
    - bar
    state: disabled
    activate: false

- name: Activate currently enabled firewall rules
  community.general.awall:
    activate: true
```

### Authors

- Ted Trask (@tdtrask)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
