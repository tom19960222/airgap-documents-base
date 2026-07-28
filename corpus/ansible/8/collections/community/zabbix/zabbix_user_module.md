---
collection: ansible
version: "8"
title: "community.zabbix.zabbix_user module – Create/update/delete Zabbix users"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/zabbix/zabbix_user_module.html
fetched_at: 2026-07-28T02:02:57+00:00
---
# community.zabbix.zabbix_user module – Create/update/delete Zabbix users

> **Note:**
>
> This module is part of the [community.zabbix collection](https://galaxy.ansible.com/ui/repo/published/community/zabbix/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.zabbix`.
> You need further requirements to be able to use this module,
> see [Requirements](zabbix_user_module.md#ansible-collections-community-zabbix-zabbix-user-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_user`.

- [Synopsis](zabbix_user_module.md#synopsis)
- [Requirements](zabbix_user_module.md#requirements)
- [Parameters](zabbix_user_module.md#parameters)
- [Examples](zabbix_user_module.md#examples)
- [Return Values](zabbix_user_module.md#return-values)

## [Synopsis](zabbix_user_module.md#id1)

- This module allows you to create, modify and delete Zabbix users.

## [Requirements](zabbix_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.9

## [Parameters](zabbix_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **after_login_url**  string | URL of the page to redirect the user to after logging in. |
| **autologin**  boolean | Whether to enable auto-login.  If enable autologin, cannot enable autologout.  **Choices:**   - `false` - `true` |
| **autologout**  string | User session life time in seconds. If set to 0, the session will never expire.  If enable autologout, cannot enable autologin. |
| **current_passwd**  string | Current password for the user when overriding its password.  Required when overriding the logged in user’s password.  <https://www.zabbix.com/documentation/6.4/en/manual/api/reference/user/update> |
| **http_login_password**  string | Basic Auth password |
| **http_login_user**  string | Basic Auth login |
| **lang**  string | Language code of the user’s language.  **Choices:**   - `"en_GB"` - `"en_US"` - `"zh_CN"` - `"cs_CZ"` - `"fr_FR"` - `"he_IL"` - `"it_IT"` - `"ko_KR"` - `"ja_JP"` - `"nb_NO"` - `"pl_PL"` - `"pt_BR"` - `"pt_PT"` - `"ru_RU"` - `"sk_SK"` - `"tr_TR"` - `"uk_UA"` - `"default"` |
| **name**  string | Name of the user. |
| **override_passwd**  boolean | Override password for the user.  Password will not be updated on subsequent runs without setting this value to yes.  **Choices:**   - `false` ← (default) - `true` |
| **passwd**  string | User’s password.  Required unless all of the *usrgrps* are set to use LDAP as frontend access. |
| **refresh**  string | Automatic refresh period in seconds. |
| **role_name**  string  *added in community.zabbix 1.2.0* | User’s role.  Default is `User role` when creating a new user.  The default value will be removed at the version 2.0.0. |
| **rows_per_page**  string | Amount of object rows to show per page. |
| **state**  string | State of the user.  On `present`, it will create if user does not exist or update the user if the associated data is different.  On `absent` will remove a user if it exists.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **surname**  string | Surname of the user. |
| **theme**  string | User’s theme.  **Choices:**   - `"default"` - `"blue-theme"` - `"dark-theme"` |
| **timezone**  string  *added in community.zabbix 1.2.0* | User’s time zone.  For the full list of supported time zones please refer to <https://www.php.net/manual/en/timezones.php> |
| **user_medias**  list / elements=dictionary | Set the user’s media.  If not set, makes no changes to media. |
| **active**  boolean | Whether the media is enabled.  **Choices:**   - `false` - `true` ← (default) |
| **mediatype**  string | Media type name to set.  **Default:** `"Email"` |
| **period**  string | Time when the notifications can be sent as a time period or user macros separated by a semicolon.  Please review the documentation for more information on the supported time period.  <https://www.zabbix.com/documentation/current/en/manual/appendix/time_period>  **Default:** `"1-7,00:00-24:00"` |
| **sendto**  any / required | Address, user name or other identifier of the recipient.  If `mediatype` is Email, values are represented as array. For other types of Media types, value is represented as a string. |
| **severity**  dictionary | Trigger severities to send notifications about.  **Default:** `{"average": true, "disaster": true, "high": true, "information": true, "not_classified": true, "warning": true}` |
| **average**  boolean | severity average enable/disable.  **Choices:**   - `false` - `true` ← (default) |
| **disaster**  boolean | severity disaster enable/disable.  **Choices:**   - `false` - `true` ← (default) |
| **high**  boolean | severity high enable/disable.  **Choices:**   - `false` - `true` ← (default) |
| **information**  boolean | severity information enable/disable.  **Choices:**   - `false` - `true` ← (default) |
| **not_classified**  boolean | severity not_classified enable/disable.  **Choices:**   - `false` - `true` ← (default) |
| **warning**  boolean | severity warning enable/disable.  **Choices:**   - `false` - `true` ← (default) |
| **username**  string / required | Username.  username is the unique identifier used and cannot be updated using this module. |
| **usrgrps**  list / elements=string | User groups to add the user to.  Required when *state=present*. |

## [Examples](zabbix_user_module.md#id4)

```yaml+jinja
# If you want to use Username and Password to be authenticated by Zabbix Server
- name: Set credentials to access Zabbix Server API
  ansible.builtin.set_fact:
    ansible_user: Admin
    ansible_httpapi_pass: zabbix

# If you want to use API token to be authenticated by Zabbix Server
# https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/administration/general#api-tokens
- name: Set API token
  ansible.builtin.set_fact:
    ansible_zabbix_auth_key: 8ec0d52432c15c91fcafe9888500cf9a607f44091ab554dbee860f6b44fac895

- name: create a new zabbix user.
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_user:
    username: example
    name: user name
    surname: user surname
    usrgrps:
      - Guests
      - Disabled
    passwd: password
    lang: en_GB
    theme: blue-theme
    autologin: no
    autologout: "0"
    refresh: "30"
    rows_per_page: "200"
    after_login_url: ""
    user_medias:
      - mediatype: Email
        sendto:
          - example@example.com
          - example1@example.com
        period: 1-7,00:00-24:00
        severity:
          not_classified: no
          information: yes
          warning: yes
          average: yes
          high: yes
          disaster: yes
        active: no
    type: Zabbix super admin
    state: present

- name: delete existing zabbix user.
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_user:
    username: example
    state: absent
```

## [Return Values](zabbix_user_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **user_ids**  dictionary | User id created or changed  **Returned:** success  **Sample:** `{"userids": ["5"]}` |

### Authors

- sky-joker (@sky-joker)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
- [Homepage](https://github.com/ansible-collections/community.zabbix)
- [Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
