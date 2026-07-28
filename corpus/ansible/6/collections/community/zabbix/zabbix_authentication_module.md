---
collection: ansible
version: "6"
title: "community.zabbix.zabbix_authentication module – Update Zabbix authentication"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/zabbix/zabbix_authentication_module.html
fetched_at: 2026-07-27T17:24:07+00:00
---
# community.zabbix.zabbix_authentication module – Update Zabbix authentication

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
> see [Requirements](zabbix_authentication_module.md#ansible-collections-community-zabbix-zabbix-authentication-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_authentication`.

New in community.zabbix 1.6.0

- [Synopsis](zabbix_authentication_module.md#synopsis)
- [Requirements](zabbix_authentication_module.md#requirements)
- [Parameters](zabbix_authentication_module.md#parameters)
- [Notes](zabbix_authentication_module.md#notes)
- [Examples](zabbix_authentication_module.md#examples)
- [Return Values](zabbix_authentication_module.md#return-values)

## [Synopsis](zabbix_authentication_module.md#id1)

- This module allows you to modify Zabbix authentication setting.

## [Requirements](zabbix_authentication_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](zabbix_authentication_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **authentication_type**  string | Choose default authentication type.  Choices:   - `"internal"` - `"ldap"` |
| **http_auth_enabled**  boolean | HTTP authentication will be enabled if `true`.  Choices:   - `false` - `true` |
| **http_case_sensitive**  boolean | Case sensitive login for HTTP authentication will be enabled if `true`.  Choices:   - `false` - `true` |
| **http_login_form**  string | Choose default login form.  Choices:   - `"zabbix_login_form"` - `"http_login_form"` |
| **http_strip_domains**  list / elements=string | A list of domain names that should be removed from the username. |
| **ldap_base_dn**  string | Base DN of LDAP.  This setting is required if current value of *ldap_configured* is `false`.  Works only with Zabbix <= 6.0 and is silently ignored in higher versions. |
| **ldap_bind_dn**  string | Bind DN of LDAP.  Works only with Zabbix <= 6.0 and is silently ignored in higher versions. |
| **ldap_bind_password**  string | Bind password of LDAP.  Works only with Zabbix <= 6.0 and is silently ignored in higher versions. |
| **ldap_case_sensitive**  boolean | case sensitive login for LDAP authentication will be enabled if `true`.  Choices:   - `false` - `true` |
| **ldap_configured**  boolean | LDAP authentication will be enabled if `true`.  Choices:   - `false` - `true` |
| **ldap_host**  string | LDAP server name.  e.g. `ldap://ldap.zabbix.com`  This setting is required if current value of *ldap_configured* is `false`.  Works only with Zabbix <= 6.0 and is silently ignored in higher versions. |
| **ldap_port**  integer | A port number of LDAP server.  This setting is required if current value of *ldap_configured* is `false`.  Works only with Zabbix <= 6.0 and is silently ignored in higher versions. |
| **ldap_search_attribute**  string | Search attribute of LDAP.  This setting is required if current value of *ldap_configured* is `false`.  Works only with Zabbix <= 6.0 and is silently ignored in higher versions. |
| **ldap_userdirectory**  string | LDAP authentication default user directory name for user groups with gui_access set to LDAP or System default.  Required to be set when `ldap_configured` is set to 1. |
| **login_password**  string | Zabbix user password.  If not set the environment variable `ZABBIX_PASSWORD` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **login_user**  string | Zabbix user name.  If not set the environment variable `ZABBIX_USERNAME` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **passwd_check_rules**  list / elements=string | Checking password rules.  Select multiple from `contain_uppercase_and_lowercase_letters`, `contain_digits`. `contain_special_characters` and `avoid_easy_to_guess`.  This parameter is available since Zabbix 6.0. |
| **passwd_min_length**  integer | Minimal length of password.  Choose from 1-70.  This parameter is available since Zabbix 6.0. |
| **saml_auth_enabled**  boolean | SAML authentication will be enabled if `true`.  Choices:   - `false` - `true` |
| **saml_case_sensitive**  boolean | Case sensitive login for SAML authentication will be enabled if `true`.  Choices:   - `false` - `true` |
| **saml_encrypt_assertions**  boolean | SAML encrypt assertions will be enabled if `true`.  Choices:   - `false` - `true` |
| **saml_encrypt_nameid**  boolean | SAML encrypt name ID will be enabled if `true`.  Choices:   - `false` - `true` |
| **saml_idp_entityid**  string | SAML identify provider’s entity ID.  This setting is required if current value of *saml_auth_enabled* is `false`. |
| **saml_nameid_format**  string | Name identifier format of SAML service provider. |
| **saml_sign_assertions**  boolean | SAML sign assertions will be enabled if `true`.  Choices:   - `false` - `true` |
| **saml_sign_authn_requests**  boolean | SAML sign AuthN requests will be enabled if `true`.  Choices:   - `false` - `true` |
| **saml_sign_logout_requests**  boolean | SAML sign logout requests will be enabled if `true`.  Choices:   - `false` - `true` |
| **saml_sign_logout_responses**  boolean | SAML sign logout responses will be enabled if `true`.  Choices:   - `false` - `true` |
| **saml_sign_messages**  boolean | SAML sign messages will be enabled if `true`.  Choices:   - `false` - `true` |
| **saml_slo_url**  string | URL for SAML single logout service. |
| **saml_sp_entityid**  string | Entity ID of SAML service provider.  This setting is required if current value of *saml_auth_enabled* is `false`. |
| **saml_sso_url**  string | URL for single sign on service of SAML.  This setting is required if current value of *saml_auth_enabled* is `false`. |
| **saml_username_attribute**  string | User name attribute of SAML.  This setting is required if current value of *saml_auth_enabled* is `false`. |
| **server_url**  aliases: url  string | URL of Zabbix server, with protocol (http or https). `url` is an alias for `server_url`.  If not set the environment variable `ZABBIX_SERVER` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **timeout**  integer | The timeout of API request (seconds).  This option is deprecated with the move to httpapi connection and will be removed in the next release  Default: `10` |
| **validate_certs**  boolean | If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If not set the environment variable `ZABBIX_VALIDATE_CERTS` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release  Choices:   - `false` - `true` ← (default) |

## [Notes](zabbix_authentication_module.md#id4)

> **Note:**
>
> - Zabbix 5.4 version and higher are supported.
> - If you use *login_password=zabbix*, the word “zabbix” is replaced by “\*\*\*\*\*\*\*\*” in all module output, because *login_password* uses `no_log`. See [this FAQ](https://docs.ansible.com/ansible/latest/network/user_guide/faq.html#why-is-my-output-sometimes-replaced-with) for more information.

## [Examples](zabbix_authentication_module.md#id5)

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

- name: Update all authentication setting
  zabbix_authentication:
    authentication_type: internal
    http_auth_enabled: true
    http_login_form: zabbix_login_form
    http_strip_domains:
      - comp
      - any
    http_case_sensitive: true
    ldap_configured: true
    ldap_host: 'ldap://localhost'
    ldap_port: 389
    ldap_base_dn: 'ou=Users,ou=system'
    ldap_search_attribute: 'uid'
    ldap_bind_dn: 'uid=ldap_search,ou=system'
    ldap_case_sensitive: true
    ldap_bind_password: 'password'
    saml_auth_enabled: true
    saml_idp_entityid: ''
    saml_sso_url: 'https://localhost/SAML2/SSO'
    saml_slo_url: 'https://localhost/SAML2/SLO'
    saml_username_attribute: 'uid'
    saml_sp_entityid: 'https://localhost'
    saml_nameid_format: 'urn:oasis:names:tc:SAML:2.0:nameid-format:entity'
    saml_sign_messages: true
    saml_sign_assertions: true
    saml_sign_authn_requests: true
    saml_sign_logout_requests: true
    saml_sign_logout_responses: true
    saml_encrypt_nameid: true
    saml_encrypt_assertions: true
    saml_case_sensitive: true
    passwd_min_length: 70
    passwd_check_rules:
      - contain_uppercase_and_lowercase_letters
      - contain_digits
      - contain_special_characters
      - avoid_easy_to_guess
```

## [Return Values](zabbix_authentication_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | The result of the operation  Returned: success  Sample: `"Successfully update authentication setting"` |

### Authors

- ONODERA Masaru(@masa-orca)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
[Homepage](https://github.com/ansible-collections/community.zabbix)
[Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
