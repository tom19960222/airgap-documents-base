---
collection: ansible
version: "8"
title: "community.general.udm_user module – Manage posix users on a univention corporate server"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/udm_user_module.html
fetched_at: 2026-07-28T01:51:03+00:00
---
# community.general.udm_user module – Manage posix users on a univention corporate server

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.udm_user`.

- [Synopsis](udm_user_module.md#synopsis)
- [Parameters](udm_user_module.md#parameters)
- [Attributes](udm_user_module.md#attributes)
- [Examples](udm_user_module.md#examples)

## [Synopsis](udm_user_module.md#id1)

- This module allows to manage posix users on a univention corporate server (UCS). It uses the python API of the UCS to create a new object or edit it.

Aliases: cloud.univention.udm_user

## [Parameters](udm_user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **birthday**  string | Birthday |
| **city**  string | City of users business address. |
| **country**  string | Country of users business address. |
| **department_number**  aliases: departmentNumber  string | Department number of users business address. |
| **description**  string | Description (not gecos) |
| **display_name**  aliases: displayName  string | Display name (not gecos) |
| **email**  list / elements=string | A list of e-mail addresses.  **Default:** `[""]` |
| **employee_number**  aliases: employeeNumber  string | Employee number |
| **employee_type**  aliases: employeeType  string | Employee type |
| **firstname**  string | First name. Required if `state=present`. |
| **gecos**  string | GECOS |
| **groups**  list / elements=string | POSIX groups, the LDAP DNs of the groups will be found with the LDAP filter for each group as $GROUP: `(&(objectClass=posixGroup)(cn=$GROUP))`.  **Default:** `[]` |
| **home_share**  aliases: homeShare  string | Home NFS share. Must be a LDAP DN, e.g. `cn=home,cn=shares,ou=school,dc=example,dc=com`. |
| **home_share_path**  aliases: homeSharePath  string | Path to home NFS share, inside the homeShare. |
| **home_telephone_number**  aliases: homeTelephoneNumber  list / elements=string | List of private telephone numbers.  **Default:** `[]` |
| **homedrive**  string | Windows home drive, for example `"H:"`. |
| **lastname**  string | Last name. Required if `state=present`. |
| **mail_alternative_address**  aliases: mailAlternativeAddress  list / elements=string | List of alternative e-mail addresses.  **Default:** `[]` |
| **mail_home_server**  aliases: mailHomeServer  string | FQDN of mail server |
| **mail_primary_address**  aliases: mailPrimaryAddress  string | Primary e-mail address |
| **mobile_telephone_number**  aliases: mobileTelephoneNumber  list / elements=string | Mobile phone number  **Default:** `[]` |
| **organisation**  aliases: organization  string | Organisation |
| **ou**  string | Organizational Unit inside the LDAP Base DN, for example `school` for LDAP OU `ou=school,dc=example,dc=com`.  **Default:** `""` |
| **overridePWHistory**  aliases: override_pw_history  boolean | Override password history  **Choices:**   - `false` ← (default) - `true` |
| **overridePWLength**  aliases: override_pw_length  boolean | Override password check  **Choices:**   - `false` ← (default) - `true` |
| **pager_telephonenumber**  aliases: pagerTelephonenumber  list / elements=string | List of pager telephone numbers.  **Default:** `[]` |
| **password**  string | Password. Required if `state=present`. |
| **phone**  list / elements=string | List of telephone numbers.  **Default:** `[]` |
| **position**  string | Define the whole position of users object inside the LDAP tree, for example `cn=employee,cn=users,ou=school,dc=example,dc=com`.  **Default:** `""` |
| **postcode**  string | Postal code of users business address. |
| **primary_group**  aliases: primaryGroup  string | Primary group. This must be the group LDAP DN.  If not specified, it defaults to `cn=Domain Users,cn=groups,$LDAP_BASE_DN`. |
| **profilepath**  string | Windows profile directory |
| **pwd_change_next_login**  aliases: pwdChangeNextLogin  string | Change password on next login.  **Choices:**   - `"0"` - `"1"` |
| **room_number**  aliases: roomNumber  string | Room number of users business address. |
| **samba_privileges**  aliases: sambaPrivileges  list / elements=string | Samba privilege, like allow printer administration, do domain join.  **Default:** `[]` |
| **samba_user_workstations**  aliases: sambaUserWorkstations  list / elements=string | Allow the authentication only on this Microsoft Windows host.  **Default:** `[]` |
| **sambahome**  string | Windows home path, for example `'\\$FQDN\$USERNAME'`. |
| **scriptpath**  string | Windows logon script. |
| **secretary**  list / elements=string | A list of superiors as LDAP DNs.  **Default:** `[]` |
| **serviceprovider**  list / elements=string | Enable user for the following service providers.  **Default:** `[""]` |
| **shell**  string | Login shell  **Default:** `"/bin/bash"` |
| **state**  string | Whether the user is present or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **street**  string | Street of users business address. |
| **subpath**  string | LDAP subpath inside the organizational unit, for example `cn=teachers,cn=users` for LDAP container `cn=teachers,cn=users,dc=example,dc=com`.  **Default:** `"cn=users"` |
| **title**  string | Title, for example `Prof.`. |
| **unixhome**  string | Unix home directory  If not specified, it defaults to `/home/$USERNAME`. |
| **update_password**  string | `always` will update passwords if they differ. `on_create` will only set the password for newly created users.  **Choices:**   - `"always"` ← (default) - `"on_create"` |
| **userexpiry**  string | Account expiry date, for example `1999-12-31`.  If not specified, it defaults to the current day plus one year. |
| **username**  aliases: name  string / required | User name |

## [Attributes](udm_user_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **partial** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](udm_user_module.md#id4)

```yaml+jinja
- name: Create a user on a UCS
  community.general.udm_user:
    name: FooBar
    password: secure_password
    firstname: Foo
    lastname: Bar

- name: Create a user with the DN uid=foo,cn=teachers,cn=users,ou=school,dc=school,dc=example,dc=com
  community.general.udm_user:
    name: foo
    password: secure_password
    firstname: Foo
    lastname: Bar
    ou: school
    subpath: 'cn=teachers,cn=users'

# or define the position
- name: Create a user with the DN uid=foo,cn=teachers,cn=users,ou=school,dc=school,dc=example,dc=com
  community.general.udm_user:
    name: foo
    password: secure_password
    firstname: Foo
    lastname: Bar
    position: 'cn=teachers,cn=users,ou=school,dc=school,dc=example,dc=com'
```

### Authors

- Tobias Rüetschi (@keachi)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
