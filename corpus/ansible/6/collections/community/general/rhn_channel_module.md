---
collection: ansible
version: "6"
title: "community.general.rhn_channel module – Adds or removes Red Hat software channels"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/rhn_channel_module.html
fetched_at: 2026-07-27T17:12:43+00:00
---
# community.general.rhn_channel module – Adds or removes Red Hat software channels

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
> To use it in a playbook, specify: `community.general.rhn_channel`.

- [Synopsis](rhn_channel_module.md#synopsis)
- [Parameters](rhn_channel_module.md#parameters)
- [Notes](rhn_channel_module.md#notes)
- [Examples](rhn_channel_module.md#examples)

## [Synopsis](rhn_channel_module.md#id1)

- Adds or removes Red Hat software channels.

## [Parameters](rhn_channel_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  string / required | Name of the software channel. |
| **password**  aliases: pwd  string / required | RHN/Satellite password. |
| **state**  string | Whether the channel should be present or not, taking action if the state is different from what is stated.  Choices:   - `"present"` ← (default) - `"absent"` |
| **sysname**  string / required | Name of the system as it is known in RHN/Satellite. |
| **url**  string / required | The full URL to the RHN/Satellite API. |
| **user**  string / required | RHN/Satellite login. |
| **validate_certs**  boolean  added in community.general 0.2.0 | If `False`, SSL certificates will not be validated.  This should only set to `False` when used on self controlled sites using self-signed certificates, and you are absolutely sure that nobody can modify traffic between the module and the site.  Choices:   - `false` - `true` ← (default) |

## [Notes](rhn_channel_module.md#id3)

> **Note:**
>
> - This module fetches the system id from RHN.
> - This module doesn’t support *check_mode*.

## [Examples](rhn_channel_module.md#id4)

```yaml+jinja
- name: Add a Red Hat software channel
  community.general.rhn_channel:
    name: rhel-x86_64-server-v2vwin-6
    sysname: server01
    url: https://rhn.redhat.com/rpc/api
    user: rhnuser
    password: guessme
  delegate_to: localhost
```

### Authors

- Vincent Van der Kussen (@vincentvdk)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
