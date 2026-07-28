---
collection: ansible
version: "6"
title: "community.zabbix.zabbix_script module – Create/update/delete Zabbix scripts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/zabbix/zabbix_script_module.html
fetched_at: 2026-07-27T17:24:19+00:00
---
# community.zabbix.zabbix_script module – Create/update/delete Zabbix scripts

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
> see [Requirements](zabbix_script_module.md#ansible-collections-community-zabbix-zabbix-script-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_script`.

New in community.zabbix 1.7.0

- [Synopsis](zabbix_script_module.md#synopsis)
- [Requirements](zabbix_script_module.md#requirements)
- [Parameters](zabbix_script_module.md#parameters)
- [Notes](zabbix_script_module.md#notes)
- [Examples](zabbix_script_module.md#examples)

## [Synopsis](zabbix_script_module.md#id1)

- This module allows you to create, update and delete scripts.

## [Requirements](zabbix_script_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](zabbix_script_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **authtype**  string | Authentication method used for SSH script type.  Used if type is `ssh`.  Choices:   - `"password"` - `"public_key"` |
| **command**  string / required | Command to run. |
| **confirmation**  string | Confirmation pop up text. The pop up will appear when trying to run the script from the Zabbix frontend.  Used if scope is `manual_host_action` or `manual_event_action`. |
| **description**  string | Description of the script. |
| **execute_on**  string | Where to run the script.  Used if type is `script`.  Choices:   - `"zabbix_agent"` - `"zabbix_server"` - `"zabbix_server_proxy"` ← (default) |
| **host_access**  string | Host permissions needed to run the script.  Used if scope is `manual_host_action` or `manual_event_action`.  Choices:   - `"read"` ← (default) - `"write"` |
| **host_group**  string | host group name that the script can be run on. If set to ‘all’, the script will be available on all host groups.  Default: `"all"` |
| **login_password**  string | Zabbix user password.  If not set the environment variable `ZABBIX_PASSWORD` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **login_user**  string | Zabbix user name.  If not set the environment variable `ZABBIX_USERNAME` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **menu_path**  string | Folders separated by slash that form a menu like navigation in frontend when clicked on host or event.  Used if scope is `manual_host_action` or `manual_event_action`.  Works only with Zabbix >= 5.4. For lower versions is silently ignored. Prepend menu path to name instead. |
| **name**  string / required | Name of the script. |
| **parameters**  list / elements=dictionary | Array of webhook input parameters.  Used if type is `webhook`. |
| **name**  string / required | Parameter name. |
| **value**  string | Parameter value. Supports macros.  Default: `""` |
| **password**  string | Password used for SSH scripts with password authentication and Telnet scripts.  Used if type is `ssh` and authtype is `password` or type is `telnet`. |
| **port**  string | Port number used for SSH and Telnet scripts.  Used if type is `ssh` or `telnet`. |
| **privatekey**  string | Name of the private key file used for SSH scripts with public key authentication.  Used if type is `ssh` and authtype is `public_key`. |
| **publickey**  string | Name of the public key file used for SSH scripts with public key authentication.  Used if type is `ssh` and authtype is `public_key`. |
| **scope**  string | Script scope.  Works only with Zabbix >= 5.4. For lower versions is silently ignored which is equivalent of `manual_host_action`.  Choices:   - `"action_operation"` ← (default) - `"manual_host_action"` - `"manual_event_action"` |
| **script_timeout**  string | Webhook script execution timeout in seconds. Time suffixes are supported, e.g. 30s, 1m.  Required if type is `webhook`.  Possible values: 1-60s.  Default: `"30s"` |
| **script_type**  string / required | Script type.  Types `ssh`, `telnet` and `webhook` works only with Zabbix >= 5.4.  Choices:   - `"script"` - `"ipmi"` - `"ssh"` - `"telnet"` - `"webhook"` |
| **server_url**  aliases: url  string | URL of Zabbix server, with protocol (http or https). `url` is an alias for `server_url`.  If not set the environment variable `ZABBIX_SERVER` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **state**  string | State of the script.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | The timeout of API request (seconds).  This option is deprecated with the move to httpapi connection and will be removed in the next release  Default: `10` |
| **user_group**  string | user group name that will be allowed to run the script. If set to ‘all’, the script will be available for all user groups.  Used if scope is `manual_host_action` or `manual_event_action`.  Default: `"all"` |
| **username**  string | User name used for authentication.  Used if type is `ssh` or `telnet` |
| **validate_certs**  boolean | If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If not set the environment variable `ZABBIX_VALIDATE_CERTS` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release  Choices:   - `false` - `true` ← (default) |

## [Notes](zabbix_script_module.md#id4)

> **Note:**
>
> - If you use *login_password=zabbix*, the word “zabbix” is replaced by “\*\*\*\*\*\*\*\*” in all module output, because *login_password* uses `no_log`. See [this FAQ](https://docs.ansible.com/ansible/latest/network/user_guide/faq.html#why-is-my-output-sometimes-replaced-with) for more information.

## [Examples](zabbix_script_module.md#id5)

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

- name: test - Create new action operation script to execute webhook
  zabbix_script:
    name: Test action operation script
    scope: action_operation
    script_type: webhook
    command: 'return 0'
    description: "Test action operation script"
    state: present
```

### Authors

- Evgeny Yurchenko (@BGmot)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
[Homepage](https://github.com/ansible-collections/community.zabbix)
[Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
