---
collection: ansible
version: "8"
title: "community.zabbix.zabbix_usergroup module – Create/delete/update Zabbix user groups"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/zabbix/zabbix_usergroup_module.html
fetched_at: 2026-07-28T02:03:00+00:00
---
# community.zabbix.zabbix_usergroup module – Create/delete/update Zabbix user groups

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
> see [Requirements](zabbix_usergroup_module.md#ansible-collections-community-zabbix-zabbix-usergroup-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_usergroup`.

- [Synopsis](zabbix_usergroup_module.md#synopsis)
- [Requirements](zabbix_usergroup_module.md#requirements)
- [Parameters](zabbix_usergroup_module.md#parameters)
- [Examples](zabbix_usergroup_module.md#examples)
- [Return Values](zabbix_usergroup_module.md#return-values)

## [Synopsis](zabbix_usergroup_module.md#id1)

- Create user groups if they do not exist.
- Delete existing user groups if they exist and are empty.
- Update existing user groups.

## [Requirements](zabbix_usergroup_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.9

## [Parameters](zabbix_usergroup_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **debug_mode**  string | Whether debug mode is enabled or disabled.  **Choices:**   - `"disabled"` ← (default) - `"enabled"` |
| **gui_access**  string | Frontend authentication method of the users in the group.  Possible values:  default - use the system default authentication method;  internal - use internal authentication;  LDAP - use LDAP authentication;  disable - disable access to the frontend.  **Choices:**   - `"default"` ← (default) - `"internal"` - `"LDAP"` - `"disable"` |
| **hostgroup_rights**  list / elements=dictionary | Host group permissions to assign to the user group  For => Zabbix 6.2 |
| **host_group**  string / required | Name of the host group to add permission to. |
| **permission**  string / required | Access level to the host group.  **Choices:**   - `"denied"` - `"read-only"` - `"read-write"` |
| **http_login_password**  string | Basic Auth password |
| **http_login_user**  string | Basic Auth login |
| **name**  aliases: user_group  string / required | Name of the user group to create, update or delete. |
| **rights**  list / elements=dictionary | Permissions to assign to the group  For <= Zabbix 6.0 |
| **host_group**  string / required | Name of the host group to add permission to. |
| **permission**  string / required | Access level to the host group.  **Choices:**   - `"denied"` - `"read-only"` - `"read-write"` |
| **state**  string | State of the user group.  On `present`, it will create if user group does not exist or update the user group if the associated data is different.  On `absent` will remove a user group if it exists.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **status**  string | Whether the user group is enabled or disabled.  **Choices:**   - `"enabled"` ← (default) - `"disabled"` |
| **tag_filters**  list / elements=dictionary | Tag based permissions to assign to the group |
| **host_group**  string / required | Name of the host group to add permission to. |
| **tag**  string | Tag name.  **Default:** `""` |
| **value**  string | Tag value.  **Default:** `""` |
| **templategroup_rights**  list / elements=dictionary | Template group permissions to assign to the user group  For => Zabbix 6.2 |
| **permission**  string / required | Access level to the templategroup.  **Choices:**   - `"denied"` - `"read-only"` - `"read-write"` |
| **template_group**  string / required | Name of the template group to add permission to. |
| **userdirectory**  string | Authentication user directory when gui_access set to LDAP or System default.  For => Zabbix 6.2 |

## [Examples](zabbix_usergroup_module.md#id4)

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

# Base create user group example
- name: Create user group
    # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_usergroup:
    name: ACME
    userdirectory: LDAP infra 1
    state: present

# Base create user group with selected user directory for LDAP authentication
- name: Create user group
    # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_usergroup:
    name: ACME
    userdirectory: LDAP infra 1
    state: present

# Base create user group with disabled gui access
- name: Create user group with disabled gui access
    # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_usergroup:
    name: ACME
    gui_access: disable

# Base create user group with permissions for Zabbix <= 6.0
- name: Create user group with permissions
    # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_usergroup:
    name: ACME
    rights:
        - host_group: Webserver
          permission: read-write
        - host_group: Databaseserver
          permission: read-only
    state: present

# Base create user group with permissions for Zabbix => 6.2
- name: Create user group with permissions
    # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_usergroup:
    name: ACME
    hostgroup_rights:
        - host_group: Webserver
          permission: read-write
        - host_group: Databaseserver
          permission: read-only
    templategroup_rights:
        - template_group: Linux Templates
          permission: read-write
        - template_group: Templates
          permission: read-only
    state: present

# Base create user group with tag permissions
- name: Create user group with tag permissions
    # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_usergroup:
    name: ACME
    tag_filters:
        - host_group: Webserver
          tag: Application
          value: Java
        - host_group: Discovered hosts
          tag: Service
          value: JIRA
    state: present

# Base delete user groups example
- name: Delete user groups
    # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_usergroup:
    name: ACME
    state: absent
```

## [Return Values](zabbix_usergroup_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | The result of the operation  **Returned:** always  **Sample:** `"User group created: ACME, ID: 42"` |
| **state**  string | User group state at the end of execution.  **Returned:** on success  **Sample:** `"present"` |
| **usergroup**  string | User group name.  **Returned:** on success  **Sample:** `"ACME"` |
| **usrgrpid**  string | User group id, if created, changed or deleted.  **Returned:** on success  **Sample:** `"42"` |

### Authors

- Tobias Birkefeld (@tcraxs)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
- [Homepage](https://github.com/ansible-collections/community.zabbix)
- [Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
