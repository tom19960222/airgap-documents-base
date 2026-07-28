---
collection: ansible
version: "8"
title: "chocolatey.chocolatey.win_chocolatey_source module – Manages Chocolatey sources"
source_url: https://docs.ansible.com/projects/ansible/8/collections/chocolatey/chocolatey/win_chocolatey_source_module.html
fetched_at: 2026-07-28T01:05:36+00:00
---
# chocolatey.chocolatey.win_chocolatey_source module – Manages Chocolatey sources

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
> To use it in a playbook, specify: `chocolatey.chocolatey.win_chocolatey_source`.

New in chocolatey.chocolatey 0.2.7

- [Synopsis](win_chocolatey_source_module.md#synopsis)
- [Parameters](win_chocolatey_source_module.md#parameters)
- [See Also](win_chocolatey_source_module.md#see-also)
- [Examples](win_chocolatey_source_module.md#examples)

## [Synopsis](win_chocolatey_source_module.md#id1)

- Used to managed Chocolatey sources configured on the client.
- Requires Chocolatey to be already installed on the remote host.

## [Parameters](win_chocolatey_source_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **admin_only**  boolean | Makes the source visible to Administrators only.  Requires Chocolatey >= 0.10.8.  When creating a new source, this defaults to `false`.  **Choices:**   - `false` - `true` |
| **allow_self_service**  boolean | Allow the source to be used with self-service  Requires Chocolatey >= 0.10.4.  When creating a new source, this defaults to `false`.  **Choices:**   - `false` - `true` |
| **bypass_proxy**  boolean | Bypass the proxy when using this source.  Requires Chocolatey >= 0.10.4.  When creating a new source, this defaults to `false`.  **Choices:**   - `false` - `true` |
| **certificate**  string | The path to a .pfx file to use for X509 authenticated feeds.  Requires Chocolatey >= 0.9.10. |
| **certificate_password**  string | The password for *certificate* if required.  Requires Chocolatey >= 0.9.10. |
| **name**  string / required | The name of the source to configure. |
| **priority**  integer | The priority order of this source compared to other sources, lower is better.  All priorities above `0` will be evaluated first, then zero-based values will be evaluated in config file order.  Requires Chocolatey >= 0.9.9.9.  When creating a new source, this defaults to `0`. |
| **source**  string | The file/folder/url of the source.  Required when *state* is `present` or `disabled` and the source does not already exist. |
| **source_password**  string | The password for *source_username*.  Required if *source_username* is set. |
| **source_username**  string | The username used to access *source*. |
| **state**  string | When `absent`, will remove the source.  When `disabled`, will ensure the source exists but is disabled.  When `present`, will ensure the source exists and is enabled.  **Choices:**   - `"absent"` - `"disabled"` - `"present"` ← (default) |
| **update_password**  string | When `always`, the module will always set the password and report a change if *certificate_password* or *source_password* is set.  When `on_create`, the module will only set the password if the source is being created.  **Choices:**   - `"always"` ← (default) - `"on_create"` |

## [See Also](win_chocolatey_source_module.md#id3)

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
> [chocolatey.chocolatey.win_chocolatey_feature](win_chocolatey_feature_module.md#ansible-collections-chocolatey-chocolatey-win-chocolatey-feature-module)
> :   Manages Chocolatey features.

## [Examples](win_chocolatey_source_module.md#id4)

```yaml+jinja
- name: Remove the default public source
  win_chocolatey_source:
    name: chocolatey
    state: absent

- name: Add new internal source
  win_chocolatey_source:
    name: internal repo
    state: present
    source: http://chocolatey-server/chocolatey

- name: Create HTTP source with credentials
  win_chocolatey_source:
    name: internal repo
    state: present
    source: https://chocolatey-server/chocolatey
    source_username: username
    source_password: password

- name: Disable Chocolatey source
  win_chocolatey_source:
    name: chocolatey
    state: disabled
```

### Authors

- Jordan Borean (@jborean93)
- Rain Sallow (@vexx32)
- Josh King (@windos)

### Collection links

- [Issue Tracker](https://github.com/chocolatey/chocolatey-ansible/issues)
- [Repository (Sources)](https://github.com/chocolatey/chocolatey-ansible)
