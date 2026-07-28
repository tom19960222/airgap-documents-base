---
collection: ansible
version: "6"
title: "theforeman.foreman.external_usergroup module – Manage External User Groups"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/external_usergroup_module.html
fetched_at: 2026-07-28T00:20:42+00:00
---
# theforeman.foreman.external_usergroup module – Manage External User Groups

> **Note:**
>
> This module is part of the [theforeman.foreman collection](https://galaxy.ansible.com/theforeman/foreman) (version 3.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install theforeman.foreman`.
> You need further requirements to be able to use this module,
> see [Requirements](external_usergroup_module.md#ansible-collections-theforeman-foreman-external-usergroup-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.external_usergroup`.

New in theforeman.foreman 1.0.0

- [Synopsis](external_usergroup_module.md#synopsis)
- [Requirements](external_usergroup_module.md#requirements)
- [Parameters](external_usergroup_module.md#parameters)
- [Examples](external_usergroup_module.md#examples)
- [Return Values](external_usergroup_module.md#return-values)

## [Synopsis](external_usergroup_module.md#id1)

- Create, update, and delete external user groups

## [Requirements](external_usergroup_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](external_usergroup_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_source**  aliases: auth_source_ldap  string / required | Name of the authentication source to be used for this group |
| **name**  string / required | Name of the group |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  Choices:   - `"present"` ← (default) - `"absent"` |
| **usergroup**  string / required | Name of the linked usergroup |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Examples](external_usergroup_module.md#id4)

```yaml+jinja
- name: Create an external user group
  theforeman.foreman.external_usergroup:
    name: test
    auth_source: "My LDAP server"
    usergroup: "Internal Usergroup"
    state: present
- name: Link a group from FreeIPA
  theforeman.foreman.external_usergroup:
    name: ipa_users
    auth_source: "External"
    usergroup: "Internal Usergroup"
    state: present
```

## [Return Values](external_usergroup_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  Returned: success |
| **external_usergroups**  list / elements=dictionary | List of external usergroups.  Returned: success |

### Authors

- Kirill Shirinkin (@Fodoj)

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
