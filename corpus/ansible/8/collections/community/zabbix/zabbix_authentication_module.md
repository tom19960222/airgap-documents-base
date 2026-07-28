---
collection: ansible
version: "8"
title: "community.zabbix.zabbix_authentication module – Update Zabbix authentication"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/zabbix/zabbix_authentication_module.html
fetched_at: 2026-07-28T02:02:39+00:00
---
# community.zabbix.zabbix_authentication module – Update Zabbix authentication

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
> see [Requirements](zabbix_authentication_module.md#ansible-collections-community-zabbix-zabbix-authentication-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_authentication`.

New in community.zabbix 1.6.0

- [Synopsis](zabbix_authentication_module.md#synopsis)
- [Requirements](zabbix_authentication_module.md#requirements)
- [Parameters](zabbix_authentication_module.md#parameters)
- [Examples](zabbix_authentication_module.md#examples)
- [Return Values](zabbix_authentication_module.md#return-values)

## [Synopsis](zabbix_authentication_module.md#id1)

- This module allows you to modify Zabbix authentication setting.

## [Requirements](zabbix_authentication_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.9

## [Parameters](zabbix_authentication_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **authentication_type**  string | Choose default authentication type.  **Choices:**   - `"internal"` - `"ldap"` |
| **disabled_usrgroup**  string | User group name to assign the deprovisioned user to.  The user group must be disabled and cannot be enabled or deleted when configured.  Required if `ldap_jit_status` for `saml_jit_status` enabled.  This parameter is available since Zabbix 6.4. |
| **http_auth_enabled**  boolean | HTTP authentication will be enabled if `true`.  **Choices:**   - `false` - `true` |
| **http_case_sensitive**  boolean | Case sensitive login for HTTP authentication will be enabled if `true`.  **Choices:**   - `false` - `true` |
| **http_login_form**  string | Choose default login form.  **Choices:**   - `"zabbix_login_form"` - `"http_login_form"` |
| **http_login_password**  string | Basic Auth password |
| **http_login_user**  string | Basic Auth login |
| **http_strip_domains**  list / elements=string | A list of domain names that should be removed from the username. |
| **jit_provision_interval**  string | Time interval between JIT provision requests for logged-in user.  Accepts seconds and time unit with suffix with month and year support (3600s,60m,1h,1d,1M,1y). Minimum value 1h.  Available only for LDAP provisioning.  This parameter is available since Zabbix 6.4.  **Default:** `"1h"` |
| **ldap_auth_enabled**  boolean | LDAP authentication will be enabled if `true`.  This parameter is available since Zabbix 6.4.  **Choices:**   - `false` - `true` |
| **ldap_base_dn**  string | Base DN of LDAP.  This setting is required if current value of *ldap_configured* is `false`.  Works only with Zabbix <= 6.0 and is silently ignored in higher versions. |
| **ldap_bind_dn**  string | Bind DN of LDAP.  Works only with Zabbix <= 6.0 and is silently ignored in higher versions. |
| **ldap_bind_password**  string | Bind password of LDAP.  Works only with Zabbix <= 6.0 and is silently ignored in higher versions. |
| **ldap_case_sensitive**  boolean | case sensitive login for LDAP authentication will be enabled if `true`.  **Choices:**   - `false` - `true` |
| **ldap_configured**  boolean | LDAP authentication will be enabled if `true`.  Works only with Zabbix <= 6.2 and is silently ignored in higher versions.  Removed in Zabbix 6.4  **Choices:**   - `false` - `true` |
| **ldap_host**  string | LDAP server name.  e.g. `ldap://ldap.zabbix.com`  This setting is required if current value of *ldap_configured* is `false`.  Works only with Zabbix <= 6.0 and is silently ignored in higher versions. |
| **ldap_jit_status**  boolean | Status of LDAP provisioning.  This parameter is available since Zabbix 6.4.  **Choices:**   - `false` - `true` |
| **ldap_port**  integer | A port number of LDAP server.  This setting is required if current value of *ldap_configured* is `false`.  Works only with Zabbix <= 6.0 and is silently ignored in higher versions. |
| **ldap_search_attribute**  string | Search attribute of LDAP.  This setting is required if current value of *ldap_configured* is `false`.  Works only with Zabbix <= 6.0 and is silently ignored in higher versions. |
| **ldap_userdirectory**  string | LDAP authentication default user directory name for user groups with gui_access set to LDAP or System default.  Required to be set when `ldap_configured` / `ldap_auth_enabled` is set to 1. |
| **passwd_check_rules**  list / elements=string | Checking password rules.  Select multiple from `contain_uppercase_and_lowercase_letters`, `contain_digits`. `contain_special_characters` and `avoid_easy_to_guess`.  This parameter is available since Zabbix 6.0. |
| **passwd_min_length**  integer | Minimal length of password.  Choose from 1-70.  This parameter is available since Zabbix 6.0. |
| **saml_auth_enabled**  boolean | SAML authentication will be enabled if `true`.  **Choices:**   - `false` - `true` |
| **saml_case_sensitive**  boolean | Case sensitive login for SAML authentication will be enabled if `true`.  **Choices:**   - `false` - `true` |
| **saml_encrypt_assertions**  boolean | SAML encrypt assertions will be enabled if `true`.  Works only with Zabbix <= 6.2 and is silently ignored in higher versions.  **Choices:**   - `false` - `true` |
| **saml_encrypt_nameid**  boolean | SAML encrypt name ID will be enabled if `true`.  Works only with Zabbix <= 6.2 and is silently ignored in higher versions.  **Choices:**   - `false` - `true` |
| **saml_idp_entityid**  string | SAML identify provider’s entity ID.  This setting is required if current value of *saml_auth_enabled* is `false`.  Works only with Zabbix <= 6.2 and is silently ignored in higher versions. |
| **saml_jit_status**  boolean | Status of SAML provisioning.  This parameter is available since Zabbix 6.4.  **Choices:**   - `false` - `true` |
| **saml_nameid_format**  string | Name identifier format of SAML service provider.  Works only with Zabbix <= 6.2 and is silently ignored in higher versions. |
| **saml_sign_assertions**  boolean | SAML sign assertions will be enabled if `true`.  Works only with Zabbix <= 6.2 and is silently ignored in higher versions.  **Choices:**   - `false` - `true` |
| **saml_sign_authn_requests**  boolean | SAML sign AuthN requests will be enabled if `true`.  Works only with Zabbix <= 6.2 and is silently ignored in higher versions.  **Choices:**   - `false` - `true` |
| **saml_sign_logout_requests**  boolean | SAML sign logout requests will be enabled if `true`.  Works only with Zabbix <= 6.2 and is silently ignored in higher versions.  **Choices:**   - `false` - `true` |
| **saml_sign_logout_responses**  boolean | SAML sign logout responses will be enabled if `true`.  Works only with Zabbix <= 6.2 and is silently ignored in higher versions.  **Choices:**   - `false` - `true` |
| **saml_sign_messages**  boolean | SAML sign messages will be enabled if `true`.  Works only with Zabbix <= 6.2 and is silently ignored in higher versions.  **Choices:**   - `false` - `true` |
| **saml_slo_url**  string | URL for SAML single logout service.  Works only with Zabbix <= 6.2 and is silently ignored in higher versions. |
| **saml_sp_entityid**  string | Entity ID of SAML service provider.  This setting is required if current value of *saml_auth_enabled* is `false`.  Works only with Zabbix <= 6.2 and is silently ignored in higher versions. |
| **saml_sso_url**  string | URL for single sign on service of SAML.  This setting is required if current value of *saml_auth_enabled* is `false`.  Works only with Zabbix <= 6.2 and is silently ignored in higher versions. |
| **saml_username_attribute**  string | User name attribute of SAML.  This setting is required if current value of *saml_auth_enabled* is `false`.  Works only with Zabbix <= 6.2 and is silently ignored in higher versions. |

## [Examples](zabbix_authentication_module.md#id4)

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

- name: Update all authentication setting (Zabbix <= 6.0)
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_authentication:
    authentication_type: internal
    http_auth_enabled: true
    http_login_form: zabbix_login_form
    http_strip_domains:
      - comp
      - any
    http_case_sensitive: true
    ldap_configured: true
    ldap_host: "ldap://localhost"
    ldap_port: 389
    ldap_base_dn: "ou=Users,ou=system"
    ldap_search_attribute: "uid"
    ldap_bind_dn: "uid=ldap_search,ou=system"
    ldap_case_sensitive: true
    ldap_bind_password: "password"
    saml_auth_enabled: true
    saml_idp_entityid: ""
    saml_sso_url: "https://localhost/SAML2/SSO"
    saml_slo_url: "https://localhost/SAML2/SLO"
    saml_username_attribute: "uid"
    saml_sp_entityid: "https://localhost"
    saml_nameid_format: "urn:oasis:names:tc:SAML:2.0:nameid-format:entity"
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

- name: Update all authentication setting (Zabbix = 6.2)
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_authentication:
    authentication_type: internal
    http_auth_enabled: true
    http_login_form: zabbix_login_form
    http_strip_domains:
      - comp
      - any
    http_case_sensitive: true
    ldap_configured: true
    ldap_case_sensitive: true
    saml_auth_enabled: true
    saml_idp_entityid: ""
    saml_sso_url: "https://localhost/SAML2/SSO"
    saml_slo_url: "https://localhost/SAML2/SLO"
    saml_username_attribute: "uid"
    saml_sp_entityid: "https://localhost"
    saml_nameid_format: "urn:oasis:names:tc:SAML:2.0:nameid-format:entity"
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

- name: Update all authentication setting (Zabbix >= 6.4)
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_authentication:
    authentication_type: internal
    http_auth_enabled: true
    http_login_form: zabbix_login_form
    http_strip_domains:
      - comp
      - any
    http_case_sensitive: true
    ldap_auth_enabled: true
    ldap_case_sensitive: true
    saml_auth_enabled: true
    saml_case_sensitive: true
    ldap_jit_status: true
    saml_jit_status: true
    jit_provision_interval: 1h
    disabled_usrgrp: Disabled
    passwd_min_length: 70
    passwd_check_rules:
      - contain_uppercase_and_lowercase_letters
      - contain_digits
      - contain_special_characters
      - avoid_easy_to_guess
```

## [Return Values](zabbix_authentication_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | The result of the operation  **Returned:** success  **Sample:** `"Successfully update authentication setting"` |

### Authors

- ONODERA Masaru(@masa-orca)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
- [Homepage](https://github.com/ansible-collections/community.zabbix)
- [Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
