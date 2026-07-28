---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_user_ldap module – Configure LDAP server entries."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_user_ldap_module.html
fetched_at: 2026-07-28T02:21:02+00:00
---
# fortinet.fortimanager.fmgr_user_ldap module – Configure LDAP server entries.

> **Note:**
>
> This module is part of the [fortinet.fortimanager collection](https://galaxy.ansible.com/ui/repo/published/fortinet/fortimanager/) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortimanager`.
>
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_user_ldap`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_user_ldap_module.md#synopsis)
- [Parameters](fmgr_user_ldap_module.md#parameters)
- [Notes](fmgr_user_ldap_module.md#notes)
- [Examples](fmgr_user_ldap_module.md#examples)
- [Return Values](fmgr_user_ldap_module.md#return-values)

## [Synopsis](fmgr_user_ldap_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_user_ldap_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **user_ldap**  dictionary | the top level parameters set |
| **account-key-cert-field**  string | Define subject identity field in certificate for user access right checking.  **Choices:**   - `"othername"` - `"rfc822name"` - `"dnsname"` |
| **account-key-filter**  string | Account key filter, using the UPN as the search filter. |
| **account-key-name**  string | Account key name, using the UPN as the search filter. |
| **account-key-processing**  string | Account key processing operation, either keep or strip domain string of UPN in the token.  **Choices:**   - `"same"` - `"strip"` |
| **account-key-upn-san**  string | Define SAN in certificate for user principle name matching.  **Choices:**   - `"othername"` - `"rfc822name"` - `"dnsname"` |
| **antiphish**  string | Enable/disable AntiPhishing credential backend.  **Choices:**   - `"disable"` - `"enable"` |
| **ca-cert**  string | CA certificate name. |
| **client-cert**  string | Client certificate name. |
| **client-cert-auth**  string | Enable/disable using client certificate for TLS authentication.  **Choices:**   - `"disable"` - `"enable"` |
| **cnid**  string | Common name identifier for the LDAP server. |
| **dn**  string | Distinguished name used to look up entries on the LDAP server. |
| **dynamic_mapping**  list / elements=dictionary | Dynamic_Mapping. |
| **_scope**  list / elements=dictionary | _Scope. |
| **name**  string | Name. |
| **vdom**  string | Vdom. |
| **account-key-cert-field**  string | Define subject identity field in certificate for user access right checking.  **Choices:**   - `"othername"` - `"rfc822name"` - `"dnsname"` |
| **account-key-filter**  string | Account key filter, using the UPN as the search filter. |
| **account-key-name**  string | Account-Key-Name. |
| **account-key-processing**  string | Account key processing operation, either keep or strip domain string of UPN in the token.  **Choices:**   - `"same"` - `"strip"` |
| **account-key-upn-san**  string | Define SAN in certificate for user principle name matching.  **Choices:**   - `"othername"` - `"rfc822name"` - `"dnsname"` |
| **antiphish**  string | Enable/disable AntiPhishing credential backend.  **Choices:**   - `"disable"` - `"enable"` |
| **ca-cert**  string | CA certificate name. |
| **client-cert**  string | Client certificate name. |
| **client-cert-auth**  string | Enable/disable using client certificate for TLS authentication.  **Choices:**   - `"disable"` - `"enable"` |
| **cnid**  string | Common name identifier for the LDAP server. |
| **dn**  string | Distinguished name used to look up entries on the LDAP server. |
| **filter**  string | Filter. |
| **group**  string | Group. |
| **group-filter**  string | Filter used for group matching. |
| **group-member-check**  string | Group member checking methods.  **Choices:**   - `"user-attr"` - `"group-object"` - `"posix-group-object"` |
| **group-object-filter**  string | Filter used for group searching. |
| **group-object-search-base**  string | Group-Object-Search-Base. |
| **group-search-base**  string | Search base used for group searching. |
| **interface**  string | Specify outgoing interface to reach server. |
| **interface-select-method**  string | Specify how to select outgoing interface to reach server.  **Choices:**   - `"auto"` - `"sdwan"` - `"specify"` |
| **max-connections**  integer | no description |
| **member-attr**  string | Name of attribute from which to get group membership. |
| **obtain-user-info**  string | Enable/disable obtaining of user information.  **Choices:**   - `"disable"` - `"enable"` |
| **password**  any | (list) Password for initial binding. |
| **password-attr**  string | Name of attribute to get password hash. |
| **password-expiry-warning**  string | Enable/disable password expiry warnings.  **Choices:**   - `"disable"` - `"enable"` |
| **password-renewal**  string | Enable/disable online password renewal.  **Choices:**   - `"disable"` - `"enable"` |
| **port**  integer | Port to be used for communication with the LDAP server |
| **retrieve-protection-profile**  string | Retrieve-Protection-Profile. |
| **search-type**  list / elements=string | Search type.  **Choices:**   - `"nested"` - `"recursive"` |
| **secondary-server**  string | Secondary LDAP server CN domain name or IP. |
| **secure**  string | Port to be used for authentication.  **Choices:**   - `"disable"` - `"starttls"` - `"ldaps"` |
| **server**  string | LDAP server CN domain name or IP. |
| **server-identity-check**  string | Enable/disable LDAP server identity check  **Choices:**   - `"disable"` - `"enable"` |
| **source-ip**  string | Source IP for communications to LDAP server. |
| **source-port**  integer | Source port to be used for communication with the LDAP server. |
| **ssl-min-proto-version**  string | Minimum supported protocol version for SSL/TLS connections  **Choices:**   - `"default"` - `"TLSv1"` - `"TLSv1-1"` - `"TLSv1-2"` - `"SSLv3"` - `"TLSv1-3"` |
| **tertiary-server**  string | Tertiary LDAP server CN domain name or IP. |
| **two-factor**  string | Enable/disable two-factor authentication.  **Choices:**   - `"disable"` - `"fortitoken-cloud"` |
| **two-factor-authentication**  string | Authentication method by FortiToken Cloud.  **Choices:**   - `"fortitoken"` - `"email"` - `"sms"` |
| **two-factor-filter**  string | Filter used to synchronize users to FortiToken Cloud. |
| **two-factor-notification**  string | Notification method for user activation by FortiToken Cloud.  **Choices:**   - `"email"` - `"sms"` |
| **type**  string | Authentication type for LDAP searches.  **Choices:**   - `"simple"` - `"anonymous"` - `"regular"` |
| **user-info-exchange-server**  string | MS Exchange server from which to fetch user information. |
| **username**  string | Username |
| **group-filter**  string | Filter used for group matching. |
| **group-member-check**  string | Group member checking methods.  **Choices:**   - `"user-attr"` - `"group-object"` - `"posix-group-object"` |
| **group-object-filter**  string | Filter used for group searching. |
| **group-object-search-base**  string | Search base used for group searching. |
| **group-search-base**  string | Search base used for group searching. |
| **interface**  string | Specify outgoing interface to reach server. |
| **interface-select-method**  string | Specify how to select outgoing interface to reach server.  **Choices:**   - `"auto"` - `"sdwan"` - `"specify"` |
| **member-attr**  string | Name of attribute from which to get group membership. |
| **name**  string / required | LDAP server entry name. |
| **obtain-user-info**  string | Enable/disable obtaining of user information.  **Choices:**   - `"disable"` - `"enable"` |
| **password**  any | (list) Password for initial binding. |
| **password-attr**  string | Name of attribute to get password hash. |
| **password-expiry-warning**  string | Enable/disable password expiry warnings.  **Choices:**   - `"disable"` - `"enable"` |
| **password-renewal**  string | Enable/disable online password renewal.  **Choices:**   - `"disable"` - `"enable"` |
| **port**  integer | Port to be used for communication with the LDAP server |
| **search-type**  list / elements=string | Search type.  **Choices:**   - `"nested"` - `"recursive"` |
| **secondary-server**  string | Secondary LDAP server CN domain name or IP. |
| **secure**  string | Port to be used for authentication.  **Choices:**   - `"disable"` - `"starttls"` - `"ldaps"` |
| **server**  string | LDAP server CN domain name or IP. |
| **server-identity-check**  string | Enable/disable LDAP server identity check  **Choices:**   - `"disable"` - `"enable"` |
| **source-ip**  string | Source IP for communications to LDAP server. |
| **source-port**  integer | Source port to be used for communication with the LDAP server. |
| **ssl-min-proto-version**  string | Minimum supported protocol version for SSL/TLS connections  **Choices:**   - `"default"` - `"TLSv1"` - `"TLSv1-1"` - `"TLSv1-2"` - `"SSLv3"` - `"TLSv1-3"` |
| **tertiary-server**  string | Tertiary LDAP server CN domain name or IP. |
| **two-factor**  string | Enable/disable two-factor authentication.  **Choices:**   - `"disable"` - `"fortitoken-cloud"` |
| **two-factor-authentication**  string | Authentication method by FortiToken Cloud.  **Choices:**   - `"fortitoken"` - `"email"` - `"sms"` |
| **two-factor-filter**  string | Filter used to synchronize users to FortiToken Cloud. |
| **two-factor-notification**  string | Notification method for user activation by FortiToken Cloud.  **Choices:**   - `"email"` - `"sms"` |
| **type**  string | Authentication type for LDAP searches.  **Choices:**   - `"simple"` - `"anonymous"` - `"regular"` |
| **user-info-exchange-server**  string | MS Exchange server from which to fetch user information. |
| **username**  string | Username |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_user_ldap_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_user_ldap_module.md#id4)

```yaml+jinja
- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Configure LDAP server entries.
     fmgr_user_ldap:
        bypass_validation: False
        adom: ansible
        state: present
        user_ldap:
           dn: ansible-test
           name: ansible-test-ldap
           password: fortinet
           port: 9000
           server: ansible

- name: gathering fortimanager facts
  hosts: fortimanager00
  gather_facts: no
  connection: httpapi
  collections:
    - fortinet.fortimanager
  vars:
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_port: 443
  tasks:
   - name: retrieve all the LDAP server entries
     fmgr_fact:
       facts:
           selector: 'user_ldap'
           params:
               adom: 'ansible'
               ldap: 'your_value'
```

## [Return Values](fmgr_user_ldap_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meta**  dictionary | The result of the request.  **Returned:** always |
| **request_url**  string | The full url requested.  **Returned:** always  **Sample:** `"/sys/login/user"` |
| **response_code**  integer | The status of api request.  **Returned:** always  **Sample:** `0` |
| **response_data**  list / elements=string | The api response.  **Returned:** always |
| **response_message**  string | The descriptive message of the api response.  **Returned:** always  **Sample:** `"OK."` |
| **system_information**  dictionary | The information of the target system.  **Returned:** always |
| **rc**  integer | The status the request.  **Returned:** always  **Sample:** `0` |
| **version_check_warning**  list / elements=string | Warning if the parameters used in the playbook are not supported by the current FortiManager version.  **Returned:** complex |

### Authors

- Xinwei Du (@dux-fortinet)
- Xing Li (@lix-fortinet)
- Jie Xue (@JieX19)
- Link Zheng (@chillancezen)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/issues)
- [Homepage](https://fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection)
