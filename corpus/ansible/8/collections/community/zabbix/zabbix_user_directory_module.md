---
collection: ansible
version: "8"
title: "community.zabbix.zabbix_user_directory module – Create/update/delete Zabbix user directories"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/zabbix/zabbix_user_directory_module.html
fetched_at: 2026-07-28T02:02:58+00:00
---
# community.zabbix.zabbix_user_directory module – Create/update/delete Zabbix user directories

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
> see [Requirements](zabbix_user_directory_module.md#ansible-collections-community-zabbix-zabbix-user-directory-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_user_directory`.

- [Synopsis](zabbix_user_directory_module.md#synopsis)
- [Requirements](zabbix_user_directory_module.md#requirements)
- [Parameters](zabbix_user_directory_module.md#parameters)
- [Examples](zabbix_user_directory_module.md#examples)

## [Synopsis](zabbix_user_directory_module.md#id1)

- This module allows you to create, modify and delete Zabbix user directories.

## [Requirements](zabbix_user_directory_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.9

## [Parameters](zabbix_user_directory_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **base_dn**  string | LDAP base distinguished name string.  required if `idp_type` is set to *ldap*. |
| **bind_dn**  string | LDAP bind distinguished name string. Can be empty for anonymous binding.  **Default:** `""` |
| **bind_password**  string | LDAP bind password. Can be empty for anonymous binding. |
| **description**  string | User directory description.  **Default:** `""` |
| **encrypt_assertions**  boolean | SAML encrypt assertions. Encrypts if *true*.  This parameter is available since Zabbix 6.4.  **Choices:**   - `false` ← (default) - `true` |
| **encrypt_nameid**  boolean | SAML encrypt name ID. Encrypts if *true*.  This parameter is available since Zabbix 6.4.  **Choices:**   - `false` ← (default) - `true` |
| **group_basedn**  string | LDAP groups path in LDAP tree to search for groups data.  Used to configure user membership check in *openLDAP*.  Required if group_membership is not set.  This parameter is available since Zabbix 6.4. |
| **group_filter**  string | LDAP search filter to select groups when searching for specific user groups.  Used to configure user membership check in openLDAP.  Ignored when provisioning a user if group_membership is set.  This parameter is available since Zabbix 6.4. |
| **group_member**  string | LDAP tree attribute name containing group name received with `group_filter` query.  Used to configure user membership check in openLDAP.  Ignored when provisioning a user if group_membership is set.  This parameter is available since Zabbix 6.4. |
| **group_membership**  string | LDAP property containing groups of user. E.g. *memberOf*  This parameter is available since Zabbix 6.4. |
| **group_name**  string | LDAP/SAML attribute name to get group name for group mapping between Zabbix and IdP.  Used to configure user membership check in LDAP.  Ignored when provisioning a user if group_membership is set.  This parameter is available since Zabbix 6.4. |
| **host**  string | LDAP server host name, IP or URI. URI should contain schema, host and port (optional).  required if `idp_type` is set to *ldap*. |
| **http_login_password**  string | Basic Auth password |
| **http_login_user**  string | Basic Auth login |
| **idp_entityid**  string | SAML URI that identifies the IdP in SAML messages.  required if `idp_type` is set to *saml*.  This parameter is available since Zabbix 6.4. |
| **idp_type**  string | Type of IdP. Only one user directory of type SAML can exist.  This parameter is available since Zabbix 6.4.  **Choices:**   - `"ldap"` - `"saml"` |
| **name**  string / required | Unique name of the user directory. |
| **nameid_format**  string | SAML SP name ID format.  This parameter is available since Zabbix 6.4. |
| **port**  integer | LDAP server port.  required if `idp_type` is set to *ldap*. |
| **provision_groups**  list / elements=dictionary | Array of the IdP media type mappings objects.  This parameter is available since Zabbix 6.4. |
| **name**  string / required | IdP group full name.  Supports the wildcard character “\*”. Unique across all provisioning groups mappings. |
| **role**  string / required | User role name to assign to the user.  Note that if multiple provisioning groups mappings are matched, the role of the highest user type will be assigned to the user. If there are multiple roles with the same user type, the first role (sorted in alphabetical order) will be assigned to the user. |
| **user_groups**  list / elements=string / required | Array of Zabbix user group names.  Note that if multiple provisioning groups mappings are matched, Zabbix user groups of all matched mappings will be assigned to the user. |
| **provision_media**  list / elements=dictionary | Array of the IdP media type mappings objects.  This parameter is available since Zabbix 6.4. |
| **attribute**  string / required | Attribute name. Used as the value for the *sendto* field.  If present in data received from IdP and the value is not empty, will trigger media creation for the provisioned user. |
| **mediatype**  string / required | Name of media type to be created. |
| **name**  string / required | Visible name in the list of media type mappings. |
| **provision_status**  boolean | User directory provisioning status.  if *false* Provisioning of users created by this user directory is disabled  if *true* Provisioning of users created by this user directory is enabled. Additionally, the authentication status of `ldap_jit_status` or `saml_jit_status` should be enabled.  This parameter is available since Zabbix 6.4.  **Choices:**   - `false` ← (default) - `true` |
| **scim_status**  boolean | Whether the SCIM provisioning for SAML is enabled or disabled.  This parameter is available since Zabbix 6.4.  **Choices:**   - `false` ← (default) - `true` |
| **search_attribute**  string | LDAP attribute name to identify user by username in Zabbix database.  required if `idp_type` is set to *ldap*. |
| **search_filter**  string | LDAP custom filter string when authenticating user in LDAP.  Supported search_filter placeholders  *%{attr}* search attribute name (uid, sAMAccountName);  *%{user}* username value.  **Default:** `"(%{attr}=%{user})"` |
| **sign_assertions**  boolean | SAML sign assertions. Signs if *true*.  This parameter is available since Zabbix 6.4.  **Choices:**   - `false` ← (default) - `true` |
| **sign_authn_requests**  boolean | SAML sign AuthN requests. Signs if *true*.  This parameter is available since Zabbix 6.4.  **Choices:**   - `false` ← (default) - `true` |
| **sign_logout_requests**  boolean | SAML sign logout requests. Signs if *true*.  This parameter is available since Zabbix 6.4.  **Choices:**   - `false` ← (default) - `true` |
| **sign_logout_responses**  boolean | SAML sign logout responses. Signs if *true*.  This parameter is available since Zabbix 6.4.  **Choices:**   - `false` ← (default) - `true` |
| **sign_messages**  boolean | SAML sign messages. Signs if *true*.  This parameter is available since Zabbix 6.4.  **Choices:**   - `false` ← (default) - `true` |
| **slo_url**  string | SAML IdP service endpoint URL to which Zabbix will send SAML logout requests.  This parameter is available since Zabbix 6.4. |
| **sp_entityid**  string | SAML SP entity ID.  required if `idp_type` is set to *saml*.  This parameter is available since Zabbix 6.4. |
| **sso_url**  string | SAML URL of the IdP”s SAML SSO service, to which Zabbix will send SAML authentication requests.  required if `idp_type` is set to *saml*.  This parameter is available since Zabbix 6.4. |
| **start_tls**  integer | LDAP startTLS option. It cannot be used with ldaps:// protocol hosts.  **Choices:**   - `0` ← (default) - `1` |
| **state**  string | State of the user directory.  On `present`, it will create if user directory does not exist or update it if the associated data is different.  On `absent` will remove the user directory if it exists.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **user_lastname**  string | LDAP/SAML attribute name to use for users.surname field when user is provisioned  This parameter is available since Zabbix 6.4. |
| **user_ref_attr**  string | LDAP user object attribute name. Will be set instead of the placeholder *%{ref}* in c(group_filter) string.  This parameter is available since Zabbix 6.4. |
| **user_username**  string | LDAP/SAML attribute name to use for users.name field when user is provisioned  This parameter is available since Zabbix 6.4. |
| **username_attribute**  string | SAML username attribute to be used in comparison with Zabbix user.username value when authenticating.  required if `idp_type` is set to *saml*.  This parameter is available since Zabbix 6.4. |

## [Examples](zabbix_user_directory_module.md#id4)

```yaml+jinja
---
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

- name: Create new user directory or update existing info (Zabbix <= 6.2)
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_user_directory:
    state: present
    name: TestUserDirectory
    host: "test.com"
    port: 389
    base_dn: "ou=Users,dc=example,dc=org"
    search_attribute: "uid"
    bind_dn: "cn=ldap_search,dc=example,dc=org"
    description: "Test user directory"
    search_filter: "(%{attr}=test_user)"
    start_tls: 0

- name: Create new user directory with LDAP IDP or update existing info (Zabbix >= 6.4)
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_user_directory:
    state: present
    name: TestUserDirectory
    idp_type: ldap
    host: "test.ca"
    port: 389
    base_dn: "ou=Users,dc=example,dc=org"
    search_attribute: "uid"
    provision_status: true
    group_name: cn
    group_basedn: ou=Group,dc=example,dc=org
    group_member: member
    user_ref_attr: uid
    group_filter: "(member=uid=%{ref},ou=Users,dc=example,dc=com)"
    user_username: first_name
    user_lastname: last_name
    provision_media:
      - name: Media1
        mediatype: Email
        attribute: email1
    provision_groups:
      - name: idpname1
        role: Guest role
        user_groups:
          - Guests

- name: Create new user directory with SAML IDP or update existing info (Zabbix >= 6.4)
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_user_directory:
    state: present
    name: TestUserDirectory
    idp_type: saml
    idp_entityid: http://okta.com/xxxxx
    sp_entityid: zabbix
    sso_url: http://xxxx.okta.com/app/xxxxxx_123dhu8o3
    username_attribute: usrEmail
    provision_status: true
    group_name: cn
    user_username: first_name
    user_lastname: last_name
    provision_media:
      - name: Media1
        mediatype: Email
        attribute: email1
    provision_groups:
      - name: idpname1
        role: Guest role
        user_groups:
          - Guests
```

### Authors

- Evgeny Yurchenko (@BGmot)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
- [Homepage](https://github.com/ansible-collections/community.zabbix)
- [Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
