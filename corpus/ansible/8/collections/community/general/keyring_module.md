---
collection: ansible
version: "8"
title: "community.general.keyring module – Set or delete a passphrase using the Operating System’s native keyring"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/keyring_module.html
fetched_at: 2026-07-28T01:47:22+00:00
---
# community.general.keyring module – Set or delete a passphrase using the Operating System’s native keyring

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](keyring_module.md#ansible-collections-community-general-keyring-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.keyring`.

New in community.general 5.2.0

- [Synopsis](keyring_module.md#synopsis)
- [Requirements](keyring_module.md#requirements)
- [Parameters](keyring_module.md#parameters)
- [Attributes](keyring_module.md#attributes)
- [Examples](keyring_module.md#examples)

## [Synopsis](keyring_module.md#id1)

- This module uses the [keyring Python library](https://pypi.org/project/keyring/) to set or delete passphrases for a given service and username from the OS’ native keyring.

Aliases: system.keyring

## [Requirements](keyring_module.md#id2)

The below requirements are needed on the host that executes this module.

- keyring (Python library)
- gnome-keyring (application - required for headless Gnome keyring access)
- dbus-run-session (application - required for headless Gnome keyring access)

## [Parameters](keyring_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **keyring_password**  string / required | Password to unlock keyring. |
| **service**  string / required | The name of the service. |
| **state**  string | Whether the password should exist.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **user_password**  aliases: password  string | The password to set. |
| **username**  string / required | The user belonging to the service. |

## [Attributes](keyring_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](keyring_module.md#id5)

```yaml+jinja
- name: Set a password for test/test1
  community.general.keyring:
    service: test
    username: test1
    user_password: "{{ user_password }}"
    keyring_password: "{{ keyring_password }}"

- name: Delete the password for test/test1
  community.general.keyring:
    service: test
    username: test1
    user_password: "{{ user_password }}"
    keyring_password: "{{ keyring_password }}"
    state: absent
```

### Authors

- Alexander Hussey (@ahussey-redhat)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
