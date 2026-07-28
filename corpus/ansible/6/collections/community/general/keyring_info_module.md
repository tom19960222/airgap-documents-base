---
collection: ansible
version: "6"
title: "community.general.keyring_info module – Get a passphrase using the Operating System’s native keyring"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/keyring_info_module.html
fetched_at: 2026-07-27T17:10:25+00:00
---
# community.general.keyring_info module – Get a passphrase using the Operating System’s native keyring

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](keyring_info_module.md#ansible-collections-community-general-keyring-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.keyring_info`.

New in community.general 5.2.0

- [Synopsis](keyring_info_module.md#synopsis)
- [Requirements](keyring_info_module.md#requirements)
- [Parameters](keyring_info_module.md#parameters)
- [Examples](keyring_info_module.md#examples)
- [Return Values](keyring_info_module.md#return-values)

## [Synopsis](keyring_info_module.md#id1)

- This module uses the [keyring Python library](https://pypi.org/project/keyring/) to retrieve passphrases for a given service and username from the OS’ native keyring.

## [Requirements](keyring_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- keyring (Python library)
- gnome-keyring (application - required for headless Linux keyring access)
- dbus-run-session (application - required for headless Linux keyring access)

## [Parameters](keyring_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **keyring_password**  string / required | Password to unlock keyring. |
| **service**  string / required | The name of the service. |
| **username**  string / required | The user belonging to the service. |

## [Examples](keyring_info_module.md#id4)

```yaml+jinja
- name: Retrieve password for service_name/user_name
  community.general.keyring_info:
    service: test
    username: test1
    keyring_password: "{{ keyring_password }}"
  register: test_password

- name: Display password
  ansible.builtin.debug:
    msg: "{{ test_password.passphrase }}"
```

## [Return Values](keyring_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **passphrase**  string | A string containing the password.  Returned: success and the password exists  Sample: `"Password123"` |

### Authors

- Alexander Hussey (@ahussey-redhat)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
