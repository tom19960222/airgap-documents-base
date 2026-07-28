---
collection: ansible
version: "8"
title: "community.windows.win_firewall module – Enable or disable the Windows Firewall"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_firewall_module.html
fetched_at: 2026-07-28T02:01:55+00:00
---
# community.windows.win_firewall module – Enable or disable the Windows Firewall

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/ui/repo/published/community/windows/) (version 1.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
> You need further requirements to be able to use this module,
> see [Requirements](win_firewall_module.md#ansible-collections-community-windows-win-firewall-module-requirements) for details.
>
> To use it in a playbook, specify: `community.windows.win_firewall`.

- [Synopsis](win_firewall_module.md#synopsis)
- [Requirements](win_firewall_module.md#requirements)
- [Parameters](win_firewall_module.md#parameters)
- [See Also](win_firewall_module.md#see-also)
- [Examples](win_firewall_module.md#examples)
- [Return Values](win_firewall_module.md#return-values)

## [Synopsis](win_firewall_module.md#id1)

- Enable or Disable Windows Firewall profiles.

## [Requirements](win_firewall_module.md#id2)

The below requirements are needed on the host that executes this module.

- This module requires Windows Management Framework 5 or later.

## [Parameters](win_firewall_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **inbound_action**  string  *added in community.windows 1.1.0* | Set to `allow` or `block` inbound network traffic in the profile.  `not_configured` is valid when configuring a GPO.  **Choices:**   - `"allow"` - `"block"` - `"not_configured"` |
| **outbound_action**  string  *added in community.windows 1.1.0* | Set to `allow` or `block` inbound network traffic in the profile.  `not_configured` is valid when configuring a GPO.  **Choices:**   - `"allow"` - `"block"` - `"not_configured"` |
| **profiles**  list / elements=string | Specify one or more profiles to change.  **Choices:**   - `"Domain"` ← (default) - `"Private"` ← (default) - `"Public"` ← (default)   **Default:** `["Domain", "Private", "Public"]` |
| **state**  string | Set state of firewall for given profile.  **Choices:**   - `"disabled"` - `"enabled"` |

## [See Also](win_firewall_module.md#id4)

> **See also:**
>
> [community.windows.win_firewall_rule](win_firewall_rule_module.md#ansible-collections-community-windows-win-firewall-rule-module)
> :   Windows firewall automation.

## [Examples](win_firewall_module.md#id5)

```yaml+jinja
- name: Enable firewall for Domain, Public and Private profiles
  community.windows.win_firewall:
    state: enabled
    profiles:
    - Domain
    - Private
    - Public
  tags: enable_firewall

- name: Disable Domain firewall
  community.windows.win_firewall:
    state: disabled
    profiles:
    - Domain
  tags: disable_firewall

- name: Enable firewall for Domain profile and block outbound connections
  community.windows.win_firewall:
    profiles: Domain
    state: enabled
    outbound_action: block
  tags: block_connection
```

## [Return Values](win_firewall_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **enabled**  boolean | Current firewall status for chosen profile (after any potential change).  **Returned:** always  **Sample:** `true` |
| **profiles**  string | Chosen profile.  **Returned:** always  **Sample:** `"Domain"` |
| **state**  list / elements=string | Desired state of the given firewall profile(s).  **Returned:** always  **Sample:** `["enabled"]` |

### Authors

- Michael Eaton (@michaeldeaton)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
