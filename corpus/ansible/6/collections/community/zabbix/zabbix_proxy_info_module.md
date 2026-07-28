---
collection: ansible
version: "6"
title: "community.zabbix.zabbix_proxy_info module – Gather information about Zabbix proxy"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/zabbix/zabbix_proxy_info_module.html
fetched_at: 2026-07-27T17:24:18+00:00
---
# community.zabbix.zabbix_proxy_info module – Gather information about Zabbix proxy

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
> see [Requirements](zabbix_proxy_info_module.md#ansible-collections-community-zabbix-zabbix-proxy-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_proxy_info`.

New in community.zabbix 1.5.0

- [Synopsis](zabbix_proxy_info_module.md#synopsis)
- [Requirements](zabbix_proxy_info_module.md#requirements)
- [Parameters](zabbix_proxy_info_module.md#parameters)
- [Notes](zabbix_proxy_info_module.md#notes)
- [Examples](zabbix_proxy_info_module.md#examples)
- [Return Values](zabbix_proxy_info_module.md#return-values)

## [Synopsis](zabbix_proxy_info_module.md#id1)

- This module allows you to obtain detailed information about configured zabbix proxies.

## [Requirements](zabbix_proxy_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](zabbix_proxy_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **login_password**  string | Zabbix user password.  If not set the environment variable `ZABBIX_PASSWORD` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **login_user**  string | Zabbix user name.  If not set the environment variable `ZABBIX_USERNAME` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **proxy_hosts**  boolean | Also return list of hosts monitored by the proxy.  Choices:   - `false` ← (default) - `true` |
| **proxy_name**  string / required | Name of the Zabbix proxy. |
| **server_url**  aliases: url  string | URL of Zabbix server, with protocol (http or https). `url` is an alias for `server_url`.  If not set the environment variable `ZABBIX_SERVER` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **timeout**  integer | The timeout of API request (seconds).  This option is deprecated with the move to httpapi connection and will be removed in the next release  Default: `10` |
| **validate_certs**  boolean | If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If not set the environment variable `ZABBIX_VALIDATE_CERTS` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release  Choices:   - `false` - `true` ← (default) |

## [Notes](zabbix_proxy_info_module.md#id4)

> **Note:**
>
> - If you use *login_password=zabbix*, the word “zabbix” is replaced by “\*\*\*\*\*\*\*\*” in all module output, because *login_password* uses `no_log`. See [this FAQ](https://docs.ansible.com/ansible/latest/network/user_guide/faq.html#why-is-my-output-sometimes-replaced-with) for more information.

## [Examples](zabbix_proxy_info_module.md#id5)

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

- name: Get zabbix proxy info alongside the list of hosts monitored by the proxy
  community.zabbix.zabbix_proxy_info:
    server_url: "http://zabbix.example.com/zabbix/"
    login_user: admin
    login_password: secret
    proxy_name: zbx01.example.com
    proxy_hosts: True
```

## [Return Values](zabbix_proxy_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **zabbix_proxy**  dictionary | example  Returned: always  Sample: `{"auto_compress": "1", "custom_interfaces": "0", "description": "ExampleProxy", "discover": "0", "flags": "0", "host": "ExampleProxy", "hosts": [{"host": "ExampleHost", "hostid": "10453"}], "interface": {"available": "0", "details": [], "disable_until": "0", "dns": "ExampleProxy.local", "error": "", "errors_from": "0", "hostid": "10452", "interfaceid": "10", "ip": "10.1.1.2", "main": "1", "port": "10051", "type": "0", "useip": "1"}, "ipmi_authtype": "-1", "ipmi_password": "", "ipmi_privilege": "2", "ipmi_username": "", "lastaccess": "0", "maintenance_from": "0", "maintenance_status": "0", "maintenance_type": "0", "maintenanceid": "0", "name": "", "proxy_address": "", "proxy_hostid": "0", "proxyid": "10452", "status": "6", "templateid": "0", "tls_accept": "1", "tls_connect": "1", "tls_issuer": "", "tls_subject": "", "uuid": ""}` |

### Authors

- Dusan Matejka (@D3DeFi)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
[Homepage](https://github.com/ansible-collections/community.zabbix)
[Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
