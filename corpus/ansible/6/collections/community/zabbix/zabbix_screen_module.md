---
collection: ansible
version: "6"
title: "community.zabbix.zabbix_screen module – Create/update/delete Zabbix screens"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/zabbix/zabbix_screen_module.html
fetched_at: 2026-07-27T17:24:19+00:00
---
# community.zabbix.zabbix_screen module – Create/update/delete Zabbix screens

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
> see [Requirements](zabbix_screen_module.md#ansible-collections-community-zabbix-zabbix-screen-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_screen`.

- [Synopsis](zabbix_screen_module.md#synopsis)
- [Requirements](zabbix_screen_module.md#requirements)
- [Parameters](zabbix_screen_module.md#parameters)
- [Notes](zabbix_screen_module.md#notes)
- [Examples](zabbix_screen_module.md#examples)

## [Synopsis](zabbix_screen_module.md#id1)

- This module allows you to create, modify and delete Zabbix screens and associated graph data.

## [Requirements](zabbix_screen_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- Zabbix <= 5.2

## [Parameters](zabbix_screen_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **login_password**  string | Zabbix user password.  If not set the environment variable `ZABBIX_PASSWORD` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **login_user**  string | Zabbix user name.  If not set the environment variable `ZABBIX_USERNAME` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **screens**  list / elements=dictionary / required | List of screens to be created/updated/deleted (see example). |
| **graph_height**  integer | Graph height will be set in graph settings. |
| **graph_names**  list / elements=string | Graph names will be added to a screen. Case insensitive.  Required if *state=present*. |
| **graph_width**  integer | Graph width will be set in graph settings. |
| **graphs_in_row**  integer | Limit columns of a screen and make multiple rows.  Default: `3` |
| **host_group**  aliases: host_groups  list / elements=string | Host group(s) will be used for searching hosts.  Required if *state=present*. |
| **screen_name**  string / required | Screen name will be used.  If a screen has already been added, the screen name won’t be updated. |
| **sort**  boolean | Sort hosts alphabetically.  If there are numbers in hostnames, leading zero should be used.  Choices:   - `false` ← (default) - `true` |
| **state**  string | *present* - Create a screen if it doesn’t exist. If the screen already exists, the screen will be updated as needed.  *absent* - If a screen exists, the screen will be deleted.  Choices:   - `"absent"` - `"present"` ← (default) |
| **server_url**  aliases: url  string | URL of Zabbix server, with protocol (http or https). `url` is an alias for `server_url`.  If not set the environment variable `ZABBIX_SERVER` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **timeout**  integer | The timeout of API request (seconds).  This option is deprecated with the move to httpapi connection and will be removed in the next release  Default: `10` |
| **validate_certs**  boolean | If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If not set the environment variable `ZABBIX_VALIDATE_CERTS` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release  Choices:   - `false` - `true` ← (default) |

## [Notes](zabbix_screen_module.md#id4)

> **Note:**
>
> - Too many concurrent updates to the same screen may cause Zabbix to return errors, see examples for a workaround if needed.
> - Screens where removed from Zabbix with Version 5.4
> - If you use *login_password=zabbix*, the word “zabbix” is replaced by “\*\*\*\*\*\*\*\*” in all module output, because *login_password* uses `no_log`. See [this FAQ](https://docs.ansible.com/ansible/latest/network/user_guide/faq.html#why-is-my-output-sometimes-replaced-with) for more information.

## [Examples](zabbix_screen_module.md#id5)

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

# Screens where removed from Zabbix with Version 5.4

# Create/update a screen.
- name: Create a new screen or update an existing screen's items 5 in a row
  community.zabbix.zabbix_screen:
    screens:
      - screen_name: ExampleScreen1
        host_group: Example group1
        state: present
        graph_names:
          - Example graph1
          - Example graph2
        graph_width: 200
        graph_height: 100
        graphs_in_row: 5

# Create/update multi-screen
- name: Create two of new screens or update the existing screens' items
  community.zabbix.zabbix_screen:
    screens:
      - screen_name: ExampleScreen1
        host_group: Example group1
        state: present
        graph_names:
          - Example graph1
          - Example graph2
        graph_width: 200
        graph_height: 100
      - screen_name: ExampleScreen2
        host_group: Example group2
        state: present
        graph_names:
          - Example graph1
          - Example graph2
        graph_width: 200
        graph_height: 100

# Limit the Zabbix screen creations to one host since Zabbix can return an error when doing concurrent updates
- name: Create a new screen or update an existing screen's items
  community.zabbix.zabbix_screen:
    state: present
    screens:
      - screen_name: ExampleScreen
        host_group: Example group
        state: present
        graph_names:
          - Example graph1
          - Example graph2
        graph_width: 200
        graph_height: 100
  when: inventory_hostname==groups['group_name'][0]

# Create/update using multiple hosts_groups. Hosts NOT present in all listed host_groups will be skipped.
- name: Create new screen or update the existing screen's items for hosts in both given groups
  community.zabbix.zabbix_screen:
    screens:
      - screen_name: ExampleScreen1
        host_group:
          - Example group1
          - Example group2
        state: present
        graph_names:
          - Example graph1
          - Example graph2
        graph_width: 200
        graph_height: 100
```

### Authors

- Cove (@cove)
- Tony Minfei Ding
- Harrison Gu (@harrisongu)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
[Homepage](https://github.com/ansible-collections/community.zabbix)
[Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
