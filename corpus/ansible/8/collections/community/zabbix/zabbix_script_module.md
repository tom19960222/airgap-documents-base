---
collection: ansible
version: "8"
title: "community.zabbix.zabbix_script module – Create/update/delete Zabbix scripts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/zabbix/zabbix_script_module.html
fetched_at: 2026-07-28T02:02:53+00:00
---
# community.zabbix.zabbix_script module – Create/update/delete Zabbix scripts

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
> see [Requirements](zabbix_script_module.md#ansible-collections-community-zabbix-zabbix-script-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_script`.

New in community.zabbix 1.7.0

- [Synopsis](zabbix_script_module.md#synopsis)
- [Requirements](zabbix_script_module.md#requirements)
- [Parameters](zabbix_script_module.md#parameters)
- [Examples](zabbix_script_module.md#examples)

## [Synopsis](zabbix_script_module.md#id1)

- This module allows you to create, update and delete scripts.

## [Requirements](zabbix_script_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.9

## [Parameters](zabbix_script_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **authtype**  string | Authentication method used for SSH script type.  Used if type is `ssh`.  **Choices:**   - `"password"` - `"public_key"` |
| **command**  string / required | Command to run. |
| **confirmation**  string | Confirmation pop up text. The pop up will appear when trying to run the script from the Zabbix frontend.  Used if scope is `manual_host_action` or `manual_event_action`. |
| **description**  string | Description of the script. |
| **execute_on**  string | Where to run the script.  Used if type is `script`.  **Choices:**   - `"zabbix_agent"` - `"zabbix_server"` - `"zabbix_server_proxy"` ← (default) |
| **host_access**  string | Host permissions needed to run the script.  Used if scope is `manual_host_action` or `manual_event_action`.  **Choices:**   - `"read"` ← (default) - `"write"` |
| **host_group**  string | host group name that the script can be run on. If set to “all”, the script will be available on all host groups.  **Default:** `"all"` |
| **http_login_password**  string | Basic Auth password |
| **http_login_user**  string | Basic Auth login |
| **menu_path**  string | Folders separated by slash that form a menu like navigation in frontend when clicked on host or event.  Used if scope is `manual_host_action` or `manual_event_action`. |
| **name**  string / required | Name of the script. |
| **parameters**  list / elements=dictionary | Array of webhook input parameters.  Used if type is `webhook`. |
| **name**  string / required | Parameter name. |
| **value**  string | Parameter value. Supports macros.  **Default:** `""` |
| **password**  string | Password used for SSH scripts with password authentication and Telnet scripts.  Used if type is `ssh` and authtype is `password` or type is `telnet`. |
| **port**  string | Port number used for SSH and Telnet scripts.  Used if type is `ssh` or `telnet`. |
| **privatekey**  string | Name of the private key file used for SSH scripts with public key authentication.  Used if type is `ssh` and authtype is `public_key`. |
| **publickey**  string | Name of the public key file used for SSH scripts with public key authentication.  Used if type is `ssh` and authtype is `public_key`. |
| **scope**  string | Script scope.  **Choices:**   - `"action_operation"` ← (default) - `"manual_host_action"` - `"manual_event_action"` |
| **script_timeout**  string | Webhook script execution timeout in seconds. Time suffixes are supported, e.g. 30s, 1m.  Required if type is `webhook`.  Possible values: 1-60s.  **Default:** `"30s"` |
| **script_type**  string / required | Script type.  **Choices:**   - `"script"` - `"ipmi"` - `"ssh"` - `"telnet"` - `"webhook"` |
| **state**  string | State of the script.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **user_group**  string | user group name that will be allowed to run the script. If set to “all”, the script will be available for all user groups.  Used if scope is `manual_host_action` or `manual_event_action`.  **Default:** `"all"` |
| **username**  string | User name used for authentication.  Used if type is `ssh` or `telnet` |

## [Examples](zabbix_script_module.md#id4)

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

- name: test - Create new action operation script to execute webhook
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_script:
    name: Test action operation script
    scope: action_operation
    script_type: webhook
    command: "return 0"
    description: "Test action operation script"
    state: present
```

### Authors

- Evgeny Yurchenko (@BGmot)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
- [Homepage](https://github.com/ansible-collections/community.zabbix)
- [Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
