---
collection: ansible
version: "6"
title: "community.general.sensu_silence module – Manage Sensu silence entries"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/sensu_silence_module.html
fetched_at: 2026-07-27T17:13:11+00:00
---
# community.general.sensu_silence module – Manage Sensu silence entries

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
> To use it in a playbook, specify: `community.general.sensu_silence`.

- [Synopsis](sensu_silence_module.md#synopsis)
- [Parameters](sensu_silence_module.md#parameters)
- [Examples](sensu_silence_module.md#examples)

## [Synopsis](sensu_silence_module.md#id1)

- Create and clear (delete) a silence entries via the Sensu API for subscriptions and checks.

## [Parameters](sensu_silence_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **check**  string | Specifies the check which the silence entry applies to. |
| **creator**  string | Specifies the entity responsible for this entry. |
| **expire**  integer | If specified, the silence entry will be automatically cleared after this number of seconds. |
| **expire_on_resolve**  boolean | If specified as true, the silence entry will be automatically cleared once the condition it is silencing is resolved.  Choices:   - `false` - `true` |
| **reason**  string | If specified, this free-form string is used to provide context or rationale for the reason this silence entry was created. |
| **state**  string | Specifies to create or clear (delete) a silence entry via the Sensu API  Choices:   - `"present"` ← (default) - `"absent"` |
| **subscription**  string / required | Specifies the subscription which the silence entry applies to.  To create a silence entry for a client prepend `client:` to client name. Example - `client:server1.example.dev` |
| **url**  string | Specifies the URL of the Sensu monitoring host server.  Default: `"http://127.0.01:4567"` |

## [Examples](sensu_silence_module.md#id3)

```yaml+jinja
# Silence ALL checks for a given client
- name: Silence server1.example.dev
  community.general.sensu_silence:
    subscription: client:server1.example.dev
    creator: "{{ ansible_user_id }}"
    reason: Performing maintenance

# Silence specific check for a client
- name: Silence CPU_Usage check for server1.example.dev
  community.general.sensu_silence:
    subscription: client:server1.example.dev
    check: CPU_Usage
    creator: "{{ ansible_user_id }}"
    reason: Investigation alert issue

# Silence multiple clients from a dict
  silence:
    server1.example.dev:
      reason: 'Deployment in progress'
    server2.example.dev:
      reason: 'Deployment in progress'

- name: Silence several clients from a dict
  community.general.sensu_silence:
    subscription: "client:{{ item.key }}"
    reason: "{{ item.value.reason }}"
    creator: "{{ ansible_user_id }}"
  with_dict: "{{ silence }}"
```

### Authors

- Steven Bambling (@smbambling)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
