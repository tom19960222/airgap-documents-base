---
collection: ansible
version: "6"
title: "community.general.awall module – Manage awall policies"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/awall_module.html
fetched_at: 2026-07-27T17:08:12+00:00
---
# community.general.awall module – Manage awall policies

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
> To use it in a playbook, specify: `community.general.awall`.

- [Synopsis](awall_module.md#synopsis)
- [Parameters](awall_module.md#parameters)
- [Examples](awall_module.md#examples)

## [Synopsis](awall_module.md#id1)

- This modules allows for enable/disable/activate of *awall* policies.
- Alpine Wall (*awall*) generates a firewall configuration from the enabled policy files and activates the configuration on the system.

## [Parameters](awall_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **activate**  boolean | Activate the new firewall rules.  Can be run with other steps or on its own.  Choices:   - `false` ← (default) - `true` |
| **name**  list / elements=string | One or more policy names. |
| **state**  string | Whether the policies should be enabled or disabled.  Choices:   - `"disabled"` - `"enabled"` ← (default) |

## [Examples](awall_module.md#id3)

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

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
