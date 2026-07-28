---
collection: ansible
version: "6"
title: "chocolatey.chocolatey.win_chocolatey_source module – Manages Chocolatey sources"
source_url: https://docs.ansible.com/projects/ansible/6/collections/chocolatey/chocolatey/win_chocolatey_source_module.html
fetched_at: 2026-07-27T16:43:23+00:00
---
# chocolatey.chocolatey.win_chocolatey_source module – Manages Chocolatey sources

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
| **admin_only**  boolean | Makes the source visible to Administrators only.  Requires Chocolatey >= 0.10.8.  When creating a new source, this defaults to `no`.  Choices:   - `false` - `true` |
| **allow_self_service**  boolean | Allow the source to be used with self-service  Requires Chocolatey >= 0.10.4.  When creating a new source, this defaults to `no`.  Choices:   - `false` - `true` |
| **bypass_proxy**  boolean | Bypass the proxy when using this source.  Requires Chocolatey >= 0.10.4.  When creating a new source, this defaults to `no`.  Choices:   - `false` - `true` |
| **certificate**  string | The path to a .pfx file to use for X509 authenticated feeds.  Requires Chocolatey >= 0.9.10. |
| **certificate_password**  string | The password for *certificate* if required.  Requires Chocolatey >= 0.9.10. |
| **name**  string / required | The name of the source to configure. |
| **priority**  integer | The priority order of this source compared to other sources, lower is better.  All priorities above `0` will be evaluated first, then zero-based values will be evaluated in config file order.  Requires Chocolatey >= 0.9.9.9.  When creating a new source, this defaults to `0`. |
| **source**  string | The file/folder/url of the source.  Required when *state* is `present` or `disabled` and the source does not already exist. |
| **source_password**  string | The password for *source_username*.  Required if *source_username* is set. |
| **source_username**  string | The username used to access *source*. |
| **state**  string | When `absent`, will remove the source.  When `disabled`, will ensure the source exists but is disabled.  When `present`, will ensure the source exists and is enabled.  Choices:   - `"absent"` - `"disabled"` - `"present"` ← (default) |
| **update_password**  string | When `always`, the module will always set the password and report a change if *certificate_password* or *source_password* is set.  When `on_create`, the module will only set the password if the source is being created.  Choices:   - `"always"` ← (default) - `"on_create"` |

## [See Also](win_chocolatey_source_module.md#id3)

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
> win_chocolatey_feature
> :   The official documentation on the **win_chocolatey_feature** module.

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

### Collection links

[Issue Tracker](https://github.com/chocolatey/chocolatey-ansible/issues)
[Repository (Sources)](https://github.com/chocolatey/chocolatey-ansible)
