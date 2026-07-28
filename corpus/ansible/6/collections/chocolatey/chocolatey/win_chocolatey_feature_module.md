---
collection: ansible
version: "6"
title: "chocolatey.chocolatey.win_chocolatey_feature module – Manages Chocolatey features"
source_url: https://docs.ansible.com/projects/ansible/6/collections/chocolatey/chocolatey/win_chocolatey_feature_module.html
fetched_at: 2026-07-27T16:49:01+00:00
---
# chocolatey.chocolatey.win_chocolatey_feature module – Manages Chocolatey features

> **Note:**
>
> This module is part of the [chocolatey.chocolatey collection](https://galaxy.ansible.com/chocolatey/chocolatey) (version 1.3.1).
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
| **state**  string | When `disabled` then the feature will be disabled.  When `enabled` then the feature will be enabled.  Choices:   - `"disabled"` - `"enabled"` ← (default) |

## [See Also](win_chocolatey_feature_module.md#id3)

> **See also:**
>
> win_chocolatey
> :   The official documentation on the **win_chocolatey** module.
>
> win_chocolatey_config
> :   The official documentation on the **win_chocolatey_config** module.
>
> win_chocolatey_facts
> :   The official documentation on the **win_chocolatey_facts** module.
>
> win_chocolatey_source
> :   The official documentation on the **win_chocolatey_source** module.

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

### Collection links

[Issue Tracker](https://github.com/chocolatey/chocolatey-ansible/issues)
[Repository (Sources)](https://github.com/chocolatey/chocolatey-ansible)
