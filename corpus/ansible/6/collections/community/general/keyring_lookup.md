---
collection: ansible
version: "6"
title: "community.general.keyring lookup – grab secrets from the OS keyring"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/keyring_lookup.html
fetched_at: 2026-07-27T17:15:05+00:00
---
# community.general.keyring lookup – grab secrets from the OS keyring

> **Note:**
>
> This lookup plugin is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](keyring_lookup.md#ansible-collections-community-general-keyring-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.general.keyring`.

- [Synopsis](keyring_lookup.md#synopsis)
- [Requirements](keyring_lookup.md#requirements)
- [Examples](keyring_lookup.md#examples)
- [Return Value](keyring_lookup.md#return-value)

## [Synopsis](keyring_lookup.md#id1)

- Allows you to access data stored in the OS provided keyring/keychain.

## [Requirements](keyring_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- keyring (python library)

## [Examples](keyring_lookup.md#id3)

```yaml+jinja
- name: output secrets to screen (BAD IDEA)
  ansible.builtin.debug:
    msg: "Password: {{item}}"
  with_community.general.keyring:
    - 'servicename username'

- name: access mysql with password from keyring
  mysql_db: login_password={{lookup('community.general.keyring','mysql joe')}} login_user=joe
```

## [Return Value](keyring_lookup.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | Secrets stored.  Returned: success |

### Authors

- Samuel Boucher

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
