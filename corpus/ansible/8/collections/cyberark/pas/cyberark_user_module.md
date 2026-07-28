---
collection: ansible
version: "8"
title: "cyberark.pas.cyberark_user module – CyberArk User Management using PAS Web Services SDK."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cyberark/pas/cyberark_user_module.html
fetched_at: 2026-07-28T01:05:40+00:00
---
# cyberark.pas.cyberark_user module – CyberArk User Management using PAS Web Services SDK.

> **Note:**
>
> This module is part of the [cyberark.pas collection](https://galaxy.ansible.com/ui/repo/published/cyberark/pas/) (version 1.0.23).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cyberark.pas`.
>
> To use it in a playbook, specify: `cyberark.pas.cyberark_user`.

New in cyberark.pas 1.0.0

- [Synopsis](cyberark_user_module.md#synopsis)
- [Parameters](cyberark_user_module.md#parameters)
- [Examples](cyberark_user_module.md#examples)
- [Return Values](cyberark_user_module.md#return-values)

## [Synopsis](cyberark_user_module.md#id1)

- CyberArk User Management using PAS Web Services SDK, It currently supports the following actions Get User Details, Add User, Update User, Delete User.

## [Parameters](cyberark_user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **authorization**  list / elements=string | A list of authorization options for this user.  Options can include AddSafes and AuditUsers  The default provides backwards compatability with older versions of the collection  **Default:** `["AddSafes", "AuditUsers"]` |
| **change_password_on_the_next_logon**  boolean | Whether or not the user must change their password in their next logon.  **Choices:**   - `false` ← (default) - `true` |
| **cyberark_session**  dictionary / required | Dictionary set by a CyberArk authentication containing the different values to perform actions on a logged-on CyberArk session, please see [cyberark.pas.cyberark_authentication](cyberark_authentication_module.md#ansible-collections-cyberark-pas-cyberark-authentication-module) module for an example of cyberark_session. |
| **disabled**  boolean | Whether or not the user will be disabled.  **Choices:**   - `false` ← (default) - `true` |
| **domain_name**  string | The name of the user domain. |
| **email**  string | The user email address. |
| **expiry_date**  string | The date and time when the user account will expire and become disabled. |
| **first_name**  string | The user first name. |
| **group_name**  string | The name of the group the user will be added to.  Causes an additional lookup in cyberark  Will be ignored if vault_id is used  Will cause a failure if group is missing or more than one group with that name exists |
| **initial_password**  string | The password that the new user will use to log on the first time.  This password must meet the password policy requirements.  This parameter is required when state is present – Add User. |
| **last_name**  string | The user last name. |
| **location**  string | The Vault Location for the user. |
| **logging_file**  string | Setting the log file name and location for troubleshooting logs.  **Default:** `"/tmp/ansible_cyberark.log"` |
| **logging_level**  string | Parameter used to define the level of troubleshooting output to the `logging_file` value.  **Choices:**   - `"NOTSET"` ← (default) - `"DEBUG"` - `"INFO"` |
| **member_type**  string | The type of member. |
| **new_password**  string | The user updated password. Make sure that this password meets the password policy requirements. |
| **state**  string | Specifies the state needed for the user present for create user, absent for delete user.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **timeout**  float | How long to wait for the server to send data before giving up  **Default:** `10.0` |
| **user_type_name**  string | The type of user.  The parameter defaults to `EPVUser`. |
| **username**  string / required | The name of the user who will be queried (for details), added, updated or deleted. |
| **vault_id**  integer | The ID of the user group to add the user to  Prefered over group_name |

## [Examples](cyberark_user_module.md#id3)

```yaml+jinja
- name: Logon to CyberArk Vault using PAS Web Services SDK
  cyberark_authentication:
    api_base_url: https://components.cyberark.local
    use_shared_logon_authentication: true

- name: Create user & immediately add it to a group
  cyberark_user:
    username: username
    initial_password: password
    user_type_name: EPVUser
    change_password_on_the_next_logon: false
    group_name: GroupOfUser
    state: present
    cyberark_session: '{{ cyberark_session }}'

- name: Make sure user is present and reset user credential if present
  cyberark_user:
    username: Username
    new_password: password
    disabled: false
    state: present
    cyberark_session: '{{ cyberark_session }}'

- name: Logoff from CyberArk Vault
  cyberark_authentication:
    state: absent
    cyberark_session: '{{ cyberark_session }}'
```

## [Return Values](cyberark_user_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether there was a change done.  **Returned:** always |
| **cyberark_user**  complex | Dictionary containing result properties.  **Returned:** always |
| **result**  dictionary | user properties when state is present  **Returned:** success |
| **status_code**  integer | Result HTTP Status code  **Returned:** success  **Sample:** `200` |

### Authors

- Edward Nunez (@enunez-cyberark)
- Cyberark Bizdev (@cyberark-bizdev)
- Erasmo Acosta (@erasmix)
- James Stutes (@jimmyjamcabd)

### Collection links

- [Issue Tracker](https://github.com/cyberark/ansible-security-automation-collection/issues)
- [Repository (Sources)](https://github.com/cyberark/ansible-security-automation-collection)
