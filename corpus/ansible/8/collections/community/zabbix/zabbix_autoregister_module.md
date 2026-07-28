---
collection: ansible
version: "8"
title: "community.zabbix.zabbix_autoregister module – Update Zabbix autoregistration"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/zabbix/zabbix_autoregister_module.html
fetched_at: 2026-07-28T02:02:40+00:00
---
# community.zabbix.zabbix_autoregister module – Update Zabbix autoregistration

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
> see [Requirements](zabbix_autoregister_module.md#ansible-collections-community-zabbix-zabbix-autoregister-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_autoregister`.

New in community.zabbix 1.6.0

- [Synopsis](zabbix_autoregister_module.md#synopsis)
- [Requirements](zabbix_autoregister_module.md#requirements)
- [Parameters](zabbix_autoregister_module.md#parameters)
- [Notes](zabbix_autoregister_module.md#notes)
- [Examples](zabbix_autoregister_module.md#examples)
- [Return Values](zabbix_autoregister_module.md#return-values)

## [Synopsis](zabbix_autoregister_module.md#id1)

- This module allows you to modify Zabbix autoregistration.

## [Requirements](zabbix_autoregister_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.9

## [Parameters](zabbix_autoregister_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **http_login_password**  string | Basic Auth password |
| **http_login_user**  string | Basic Auth login |
| **tls_accept**  list / elements=string / required | Type of allowed incoming connections for autoregistration.  Choose from `unsecure`, `tls_with_psk` or both. |
| **tls_psk**  string | TLS connection uses this PSK value.  This setting requires *tls_accept=tls_with_psk* if current value of *tls_accept* is `unsecure`. |
| **tls_psk_identity**  string | TLS connection uses this PSK identity string.  The PSK identity string will be transmitted unencrypted over the network. Therefore, you should not put any sensitive information here.  This setting requires *tls_accept=tls_with_psk* if current value of *tls_accept* is `unsecure`. |

## [Notes](zabbix_autoregister_module.md#id4)

> **Note:**
>
> - This module returns changed=true when any value is set in *tls_psk_identity* or *tls_psk* as Zabbix API will not return any sensitive information back for module to compare.
> - Please note that this module configures **global Zabbix Server settings**. If you want to create autoregistration action so your hosts can automatically add themselves to the monitoring have a look at [community.zabbix.zabbix_action](zabbix_action_module.md#ansible-collections-community-zabbix-zabbix-action-module).

## [Examples](zabbix_autoregister_module.md#id5)

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

- name: Update autoregistration
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_autoregister:
    tls_accept:
      - unsecure
      - tls_with_psk
    tls_psk_identity: "PSK 001"
    tls_psk: "11111595725ac58dd977beef14b97461a7c1045b9a1c923453302c5473193478"

- name: Set unsecure to tls_accept
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_autoregister:
    tls_accept: unsecure
```

## [Return Values](zabbix_autoregister_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | The result of the operation  **Returned:** success  **Sample:** `"Successfully updated global autoregistration setting"` |

### Authors

- ONODERA Masaru(@masa-orca)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
- [Homepage](https://github.com/ansible-collections/community.zabbix)
- [Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
