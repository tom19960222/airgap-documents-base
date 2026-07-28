---
collection: ansible
version: "6"
title: "community.zabbix.zabbix_proxy module – Create/delete/get/update Zabbix proxies"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/zabbix/zabbix_proxy_module.html
fetched_at: 2026-07-27T17:24:17+00:00
---
# community.zabbix.zabbix_proxy module – Create/delete/get/update Zabbix proxies

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
> see [Requirements](zabbix_proxy_module.md#ansible-collections-community-zabbix-zabbix-proxy-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_proxy`.

- [Synopsis](zabbix_proxy_module.md#synopsis)
- [Requirements](zabbix_proxy_module.md#requirements)
- [Parameters](zabbix_proxy_module.md#parameters)
- [Notes](zabbix_proxy_module.md#notes)
- [Examples](zabbix_proxy_module.md#examples)

## [Synopsis](zabbix_proxy_module.md#id1)

- This module allows you to create, modify, get and delete Zabbix proxy entries.

## [Requirements](zabbix_proxy_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](zabbix_proxy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: tls_issuer  string | Certificate issuer. |
| **description**  string | Description of the proxy. |
| **interface**  dictionary | Dictionary with params for the interface when proxy is in passive mode.  For more information, review proxy interface documentation at  <https://www.zabbix.com/documentation/4.0/manual/api/reference/proxy/object#proxy_interface>.  Default: `{}` |
| **dns**  string | DNS name of the proxy interface.  Required if *useip=0*.  Default: `""` |
| **ip**  string | IP address used by proxy interface.  Required if *useip=1*.  Default: `""` |
| **main**  integer | Whether the interface is used as default.  This suboption is currently ignored for Zabbix proxy.  This suboption is deprecated since Ansible 2.10 and will eventually be removed in 2.14.  Default: `0` |
| **port**  string | Port used by proxy interface.  Default: `"10051"` |
| **type**  integer | Interface type to add.  This suboption is currently ignored for Zabbix proxy.  This suboption is deprecated since Ansible 2.10 and will eventually be removed in 2.14.  Default: `0` |
| **useip**  integer | Connect to proxy interface with IP address instead of DNS name.  0 (don’t use ip), 1 (use ip).  Choices:   - `0` ← (default) - `1` |
| **login_password**  string | Zabbix user password.  If not set the environment variable `ZABBIX_PASSWORD` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **login_user**  string | Zabbix user name.  If not set the environment variable `ZABBIX_USERNAME` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **proxy_address**  string | Comma-delimited list of IP/CIDR addresses or DNS names to accept active proxy requests from.  Requires *status=active*.  Works only with >= Zabbix 4.0. ( remove option for <= 4.0 ) |
| **proxy_name**  string / required | Name of the proxy in Zabbix. |
| **server_url**  aliases: url  string | URL of Zabbix server, with protocol (http or https). `url` is an alias for `server_url`.  If not set the environment variable `ZABBIX_SERVER` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **state**  string | State of the proxy.  On `present`, it will create if proxy does not exist or update the proxy if the associated data is different.  On `absent` will remove a proxy if it exists.  Choices:   - `"present"` ← (default) - `"absent"` |
| **status**  string | Type of proxy. (4 - active, 5 - passive)  Choices:   - `"active"` ← (default) - `"passive"` |
| **timeout**  integer | The timeout of API request (seconds).  This option is deprecated with the move to httpapi connection and will be removed in the next release  Default: `10` |
| **tls_accept**  string | Connections from proxy.  Choices:   - `"no_encryption"` ← (default) - `"PSK"` - `"certificate"` |
| **tls_connect**  string | Connections to proxy.  Choices:   - `"no_encryption"` ← (default) - `"PSK"` - `"certificate"` |
| **tls_psk**  string | The preshared key, at least 32 hex digits. Required if either *tls_connect* or *tls_accept* has PSK enabled. |
| **tls_psk_identity**  string | PSK identity. Required if either *tls_connect* or *tls_accept* has PSK enabled. |
| **tls_subject**  string | Certificate subject. |
| **validate_certs**  boolean | If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If not set the environment variable `ZABBIX_VALIDATE_CERTS` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release  Choices:   - `false` - `true` ← (default) |

## [Notes](zabbix_proxy_module.md#id4)

> **Note:**
>
> - If you use *login_password=zabbix*, the word “zabbix” is replaced by “\*\*\*\*\*\*\*\*” in all module output, because *login_password* uses `no_log`. See [this FAQ](https://docs.ansible.com/ansible/latest/network/user_guide/faq.html#why-is-my-output-sometimes-replaced-with) for more information.

## [Examples](zabbix_proxy_module.md#id5)

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

- name: Create or update a proxy with proxy type active
  community.zabbix.zabbix_proxy:
    proxy_name: ExampleProxy
    description: ExampleProxy
    status: active
    state: present
    proxy_address: ExampleProxy.local

- name: Create a new passive proxy using only it's IP
  community.zabbix.zabbix_proxy:
    proxy_name: ExampleProxy
    description: ExampleProxy
    status: passive
    state: present
    interface:
      useip: 1
      ip: 10.1.1.2
      port: 10051

- name: Create a new passive proxy using only it's DNS
  community.zabbix.zabbix_proxy:
    proxy_name: ExampleProxy
    description: ExampleProxy
    status: passive
    state: present
    interface:
      dns: proxy.example.com
      port: 10051
```

### Authors

- Alen Komic (@akomic)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
[Homepage](https://github.com/ansible-collections/community.zabbix)
[Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
