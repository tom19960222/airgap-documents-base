---
collection: ansible
version: "6"
title: "community.general.grove module – Sends a notification to a grove.io channel"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/grove_module.html
fetched_at: 2026-07-27T17:09:13+00:00
---
# community.general.grove module – Sends a notification to a grove.io channel

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
> To use it in a playbook, specify: `community.general.grove`.

- [Synopsis](grove_module.md#synopsis)
- [Parameters](grove_module.md#parameters)
- [Examples](grove_module.md#examples)

## [Synopsis](grove_module.md#id1)

- The `grove` module sends a message for a service to a Grove.io channel.

## [Parameters](grove_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **channel_token**  string / required | Token of the channel to post to. |
| **icon_url**  string | Icon for the service |
| **message_content**  string / required | Message content.  The alias *message* is deprecated and will be removed in community.general 4.0.0. |
| **service**  string | Name of the service (displayed as the “user” in the message)  Default: `"ansible"` |
| **url**  string | Service URL for the web client |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Examples](grove_module.md#id3)

```yaml+jinja
- name: Sends a notification to a grove.io channel
  community.general.grove:
    channel_token: 6Ph62VBBJOccmtTPZbubiPzdrhipZXtg
    service: my-app
    message: 'deployed {{ target }}'
```

### Authors

- Jonas Pfenniger (@zimbatm)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
