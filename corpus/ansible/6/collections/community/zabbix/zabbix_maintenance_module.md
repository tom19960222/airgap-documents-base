---
collection: ansible
version: "6"
title: "community.zabbix.zabbix_maintenance module – Create Zabbix maintenance windows"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/zabbix/zabbix_maintenance_module.html
fetched_at: 2026-07-27T17:24:15+00:00
---
# community.zabbix.zabbix_maintenance module – Create Zabbix maintenance windows

> **Note:**
>
> This module is part of the [community.zabbix collection](https://galaxy.ansible.com/community/zabbix) (version 1.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.zabbix`.
> You need further requirements to be able to use this module,
> see [Requirements](zabbix_maintenance_module.md#ansible-collections-community-zabbix-zabbix-maintenance-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_maintenance`.

- [Synopsis](zabbix_maintenance_module.md#synopsis)
- [Requirements](zabbix_maintenance_module.md#requirements)
- [Parameters](zabbix_maintenance_module.md#parameters)
- [Notes](zabbix_maintenance_module.md#notes)
- [Examples](zabbix_maintenance_module.md#examples)

## [Synopsis](zabbix_maintenance_module.md#id1)

- This module will let you create Zabbix maintenance windows.

## [Requirements](zabbix_maintenance_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](zabbix_maintenance_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **collect_data**  boolean | Type of maintenance. With data collection, or without.  Choices:   - `false` - `true` ← (default) |
| **desc**  string | Short description of maintenance window.  Default: `"Created by Ansible"` |
| **host_groups**  aliases: host_group  list / elements=string | Host groups to manage maintenance window for.  **Required** option when *state=present* and *host_names* is not used. |
| **host_names**  aliases: host_name  list / elements=string | Hosts to manage maintenance window for.  **Required** option when *state=present* and *host_groups* is not used. |
| **login_password**  string | Zabbix user password.  If not set the environment variable `ZABBIX_PASSWORD` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **login_user**  string | Zabbix user name.  If not set the environment variable `ZABBIX_USERNAME` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **minutes**  integer | Length of maintenance window in minutes.  Default: `10` |
| **name**  string / required | Unique name of maintenance window. |
| **server_url**  aliases: url  string | URL of Zabbix server, with protocol (http or https). `url` is an alias for `server_url`.  If not set the environment variable `ZABBIX_SERVER` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **state**  string | Create or remove a maintenance window. Maintenance window to remove is identified by name.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=dictionary | List of tags to assign to the hosts in maintenance.  Requires *collect_data=yes*. |
| **operator**  integer | Condition operator.  Possible values is  0 - Equals  2 - Contains  Default: `2` |
| **tag**  string / required | Name of the tag. |
| **value**  string | Value of the tag.  Default: `""` |
| **timeout**  integer | The timeout of API request (seconds).  This option is deprecated with the move to httpapi connection and will be removed in the next release  Default: `10` |
| **validate_certs**  boolean | If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If not set the environment variable `ZABBIX_VALIDATE_CERTS` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release  Choices:   - `false` - `true` ← (default) |
| **visible_name**  boolean  added in community.zabbix 2.0.0 | Type of zabbix host name to use for identifying hosts to include in the maintenance.  *visible_name=yes* to search by visible name, *visible_name=no* to search by technical name.  Choices:   - `false` - `true` ← (default) |

## [Notes](zabbix_maintenance_module.md#id4)

> **Note:**
>
> - Useful for setting hosts in maintenance mode before big update, and removing maintenance window after update.
> - Module creates maintenance window from now() to now() + minutes, so if Zabbix server’s time and host’s time are not synchronized, you will get strange results.
> - If you use *login_password=zabbix*, the word “zabbix” is replaced by “\*\*\*\*\*\*\*\*” in all module output, because *login_password* uses `no_log`. See [this FAQ](https://docs.ansible.com/ansible/latest/network/user_guide/faq.html#why-is-my-output-sometimes-replaced-with) for more information.

## [Examples](zabbix_maintenance_module.md#id5)

```yaml+jinja
# Set following variables for Zabbix Server host in play or inventory
- name: Set connection specific variables
  set_fact:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 80
    ansible_httpapi_use_ssl: false
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: 'zabbixeu'  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu

# If you want to use Username and Password to be authenticated by Zabbix Server
- name: Set credentials to access Zabbix Server API
  set_fact:
    ansible_user: Admin
    ansible_httpapi_pass: zabbix

# If you want to use API token to be authenticated by Zabbix Server
# https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/administration/general#api-tokens
- name: Set API token
  set_fact:
    ansible_zabbix_auth_key: 8ec0d52432c15c91fcafe9888500cf9a607f44091ab554dbee860f6b44fac895

- name: Create a named maintenance window for host www1 for 90 minutes
  community.zabbix.zabbix_maintenance:
    name: Update of www1
    host_name: www1.example.com
    state: present
    minutes: 90

- name: Create a named maintenance window for host www1 and host groups Office and Dev
  community.zabbix.zabbix_maintenance:
    name: Update of www1
    host_name: www1.example.com
    host_groups:
      - Office
      - Dev
    state: present
    tags:
      - tag: ExampleHostsTag
      - tag: ExampleHostsTag2
        value: ExampleTagValue
      - tag: ExampleHostsTag3
        value: ExampleTagValue
        operator: 0

- name: Create a named maintenance window for hosts www1 and db1, without data collection.
  community.zabbix.zabbix_maintenance:
    name: update
    host_names:
      - www1.example.com
      - db1.example.com
    state: present
    collect_data: False

- name: Remove maintenance window by name
  community.zabbix.zabbix_maintenance:
    name: Test1
    state: absent
```

### Authors

- Alexander Bulimov (@abulimov)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
[Homepage](https://github.com/ansible-collections/community.zabbix)
[Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
