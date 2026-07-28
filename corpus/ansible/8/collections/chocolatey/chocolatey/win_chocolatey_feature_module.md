---
collection: ansible
version: "8"
title: "chocolatey.chocolatey.win_chocolatey_feature module – Manages Chocolatey features"
source_url: https://docs.ansible.com/projects/ansible/8/collections/chocolatey/chocolatey/win_chocolatey_feature_module.html
fetched_at: 2026-07-28T01:18:37+00:00
---
# chocolatey.chocolatey.win_chocolatey_feature module – Manages Chocolatey features

> **Note:**
>
> This module is part of the [chocolatey.chocolatey collection](https://galaxy.ansible.com/ui/repo/published/chocolatey/chocolatey/) (version 1.5.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install chocolatey.chocolatey`.
>
> To use it in a playbook, specify: `chocolatey.chocolatey.win_chocolatey_feature`.

New in chocolatey.chocolatey 0.2.7

- [Synopsis](win_chocolatey_feature_module.md#synopsis)
- [Parameters](win_chocolatey_feature_module.md#parameters)
- [See Also](win_chocolatey_feature_module.md#see-also)
- [Examples](win_chocolatey_feature_module.md#examples)

## [Synopsis](win_chocolatey_feature_module.md#id1)

- Used to enable or disable features in Chocolatey.

## [Parameters](win_chocolatey_feature_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  string / required | The name of the feature to manage.  Run `choco.exe feature list` to get a list of features that can be managed.  For a list of options see [Chocolatey feature docs](https://chocolatey.org/docs/chocolatey-configuration#features) |
| **state**  string | When `disabled` then the feature will be disabled.  When `enabled` then the feature will be enabled.  **Choices:**   - `"disabled"` - `"enabled"` ← (default) |

## [See Also](win_chocolatey_feature_module.md#id3)

> **See also:**
>
> [chocolatey.chocolatey.win_chocolatey](win_chocolatey_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-module)
> :   Manage packages using chocolatey.
>
> [chocolatey.chocolatey.win_chocolatey_config](win_chocolatey_config_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-config-module)
> :   Manages Chocolatey config settings.
>
> [chocolatey.chocolatey.win_chocolatey_facts](win_chocolatey_facts_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-facts-module)
> :   Create a facts collection for Chocolatey.
>
> [chocolatey.chocolatey.win_chocolatey_source](win_chocolatey_source_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-source-module)
> :   Manages Chocolatey sources.

## [Examples](win_chocolatey_feature_module.md#id4)

```yaml+jinja
- name: Disable file checksum matching
  win_chocolatey_feature:
    name: checksumFiles
    state: disabled

- name: Stop Chocolatey on the first package failure
  win_chocolatey_feature:
    name: stopOnFirstPackageFailure
    state: enabled
```

### Authors

- Jordan Borean (@jborean93)
- Rain Sallow (@vexx32)
- Josh King (@windos)

### Collection links

- [Issue Tracker](https://github.com/chocolatey/chocolatey-ansible/issues)
- [Repository (Sources)](https://github.com/chocolatey/chocolatey-ansible)
