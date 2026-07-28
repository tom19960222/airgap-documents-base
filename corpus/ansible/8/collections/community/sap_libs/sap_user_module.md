---
collection: ansible
version: "8"
title: "community.sap_libs.sap_user module – This module will manage a user entities in a SAP S4/HANA environment"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/sap_libs/sap_user_module.html
fetched_at: 2026-07-28T01:59:18+00:00
---
# community.sap_libs.sap_user module – This module will manage a user entities in a SAP S4/HANA environment

> **Note:**
>
> This module is part of the [community.sap_libs collection](https://galaxy.ansible.com/ui/repo/published/community/sap_libs/) (version 1.4.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.sap_libs`.
> You need further requirements to be able to use this module,
> see [Requirements](sap_user_module.md#ansible-collections-community-sap-libs-sap-user-module-requirements) for details.
>
> To use it in a playbook, specify: `community.sap_libs.sap_user`.

New in community.sap_libs 1.0.0

- [Synopsis](sap_user_module.md#synopsis)
- [Requirements](sap_user_module.md#requirements)
- [Parameters](sap_user_module.md#parameters)
- [Notes](sap_user_module.md#notes)
- [Examples](sap_user_module.md#examples)
- [Return Values](sap_user_module.md#return-values)

## [Synopsis](sap_user_module.md#id1)

- The [community.sap_libs.sap_user](sap_user_module.md#ansible-collections-community-sap-libs-sap-user-module) module depends on `pyrfc` Python library (version 2.4.0 and upwards). Depending on distribution you are using, you may need to install additional packages to have these available.
- This module will use the following user BAPIs to manage user entities. - `BAPI_USER_GET_DETAIL` - `BAPI_USER_DELETE` - `BAPI_USER_CREATE1` - `BAPI_USER_CHANGE` - `BAPI_USER_ACTGROUPS_ASSIGN` - `BAPI_USER_PROFILES_ASSIGN` - `BAPI_USER_UNLOCK` - `BAPI_USER_LOCK`

## [Requirements](sap_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- pyrfc >= 2.4.0

## [Parameters](sap_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **client**  string | The client number to connect to.  You must quote the value to ensure retaining the leading zeros.  **Default:** `"000"` |
| **company**  string | The specific company the user belongs to.  The company name must be available in the SAP system. |
| **conn_password**  string / required | The required password for the SAP system. |
| **conn_username**  string / required | The required username for the SAP system. |
| **email**  string | The email address of the user in the SAP system. |
| **firstname**  string | The Firstname of the user in the SAP system. |
| **force**  boolean | Must be `'True'` if the password or type should be overwritten.  **Choices:**   - `false` ← (default) - `true` |
| **host**  string / required | The required host for the SAP system. Can be either an FQDN or IP Address. |
| **lastname**  string | The lastname of the user in the SAP system. |
| **password**  string | The password for the user in the SAP system. |
| **profiles**  list / elements=string | Assign profiles to the user.  Should be in uppercase, for example `'SAP_NEW'` or `'SAP_ALL'`.  **Default:** `[""]` |
| **roles**  list / elements=string | Assign roles to the user.  **Default:** `[""]` |
| **state**  string | The decision what to do with the user.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"lock"` - `"unlock"` |
| **sysnr**  string | The system number of the SAP system.  You must quote the value to ensure retaining the leading zeros.  **Default:** `"00"` |
| **user_type**  string | The type for the user in the SAP system.  `'A'` Dialog user, `'B'` System User, `'C'` Communication User, `'S'` Service User, `'L'` Reference User.  Must be in uppercase.  **Choices:**   - `"A"` ← (default) - `"B"` - `"C"` - `"S"` - `"L"` |
| **useralias**  string | The alias for the user in the SAP system. |
| **username**  string / required | The username. |

## [Notes](sap_user_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`.

## [Examples](sap_user_module.md#id5)

```yaml+jinja
- name: Create SAP User
  community.sap_libs.sap_user:
    conn_username: 'DDIC'
    conn_password: 'Test123'
    host: 192.168.1.150
    sysnr: '01'
    client: '000'
    state: present
    username: ADMIN
    firstname: first_admin
    lastname: last_admin
    email: admin@test.de
    password: Test123456
    useralias: ADMIN
    company: DEFAULT_COMPANY
    roles:
      - "SAP_ALL"

- name: Force change SAP User
  community.sap_libs.sap_user:
    conn_username: 'DDIC'
    conn_password: 'Test123'
    host: 192.168.1.150
    sysnr: '01'
    client: '000'
    state: present
    force: true
    username: ADMIN
    firstname: first_admin
    lastname: last_admin
    email: admin@test.de
    password: Test123456
    useralias: ADMIN
    company: DEFAULT_COMPANY
    roles:
      - "SAP_ALL"

- name: Delete SAP User
  community.sap_libs.sap_user:
    conn_username: 'DDIC'
    conn_password: 'Test123'
    host: 192.168.1.150
    sysnr: '01'
    client: '000'
    state: absent
    force: true
    username: ADMIN

- name: Unlock SAP User
  community.sap_libs.sap_user:
    conn_username: 'DDIC'
    conn_password: 'Test123'
    host: 192.168.1.150
    sysnr: '01'
    client: '000'
    state: unlock
    force: true
    username: ADMIN
```

## [Return Values](sap_user_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | A small execution description about the user action.  **Returned:** always  **Sample:** `"User ADMIN created"` |
| **out**  list / elements=dictionary | A detailed description about the user action.  **Returned:** on success  **Sample:** `["...", {"RETURN": [{"FIELD": "BNAME", "ID": "01", "LOG_MSG_NO": "000000", "LOG_NO": "", "MESSAGE": "User ADMIN created", "MESSAGE_V1": "ADMIN", "MESSAGE_V2": "", "MESSAGE_V3": "", "MESSAGE_V4": "", "NUMBER": "102", "PARAMETER": "", "ROW": 0, "SYSTEM": "", "TYPE": "S"}], "SAPUSER_UUID_HIST": []}]` |

### Authors

- Rainer Leber (@rainerleber)

### Collection links

- [Issue Tracker](https://github.com/sap-linuxlab/community.sap_libs)
- [Repository (Sources)](https://github.com/sap-linuxlab/community.sap_libs)
