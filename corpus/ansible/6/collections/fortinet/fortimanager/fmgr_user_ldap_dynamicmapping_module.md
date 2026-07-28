---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_user_ldap_dynamicmapping module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_user_ldap_dynamicmapping_module.html
fetched_at: 2026-07-27T17:37:59+00:00
---
# fortinet.fortimanager.fmgr_user_ldap_dynamicmapping module – no description

> **Note:**
>
> This module is part of the [fortinet.fortimanager collection](https://galaxy.ansible.com/fortinet/fortimanager) (version 2.1.7).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortimanager`.
>
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_user_ldap_dynamicmapping`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_user_ldap_dynamicmapping_module.md#synopsis)
- [Parameters](fmgr_user_ldap_dynamicmapping_module.md#parameters)
- [Notes](fmgr_user_ldap_dynamicmapping_module.md#notes)
- [Examples](fmgr_user_ldap_dynamicmapping_module.md#examples)
- [Return Values](fmgr_user_ldap_dynamicmapping_module.md#return-values)

## [Synopsis](fmgr_user_ldap_dynamicmapping_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_user_ldap_dynamicmapping_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **ldap**  string / required | the parameter (ldap) in requested url |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **user_ldap_dynamicmapping**  dictionary | the top level parameters set |
| **_scope**  list / elements=string | description |
| **name**  string | no description |
| **vdom**  string | no description |
| **account-key-filter**  string | no description |
| **account-key-name**  string | no description |
| **account-key-processing**  string | no description  Choices:   - `"same"` - `"strip"` |
| **antiphish**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ca-cert**  string | no description |
| **client-cert**  string | no description |
| **client-cert-auth**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **cnid**  string | no description |
| **dn**  string | no description |
| **filter**  string | no description |
| **group**  string | no description |
| **group-filter**  string | no description |
| **group-member-check**  string | no description  Choices:   - `"user-attr"` - `"group-object"` - `"posix-group-object"` |
| **group-object-filter**  string | no description |
| **group-object-search-base**  string | no description |
| **group-search-base**  string | no description |
| **interface**  string | no description |
| **interface-select-method**  string | no description  Choices:   - `"auto"` - `"sdwan"` - `"specify"` |
| **member-attr**  string | no description |
| **obtain-user-info**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **password**  string | description |
| **password-attr**  string | no description |
| **password-expiry-warning**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **password-renewal**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **port**  integer | no description |
| **retrieve-protection-profile**  string | no description |
| **search-type**  list / elements=string | description  Choices:   - `"nested"` - `"recursive"` |
| **secondary-server**  string | no description |
| **secure**  string | no description  Choices:   - `"disable"` - `"starttls"` - `"ldaps"` |
| **server**  string | no description |
| **server-identity-check**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **source-ip**  string | no description |
| **source-port**  integer | no description |
| **ssl-min-proto-version**  string | no description  Choices:   - `"default"` - `"TLSv1"` - `"TLSv1-1"` - `"TLSv1-2"` - `"SSLv3"` |
| **tertiary-server**  string | no description |
| **two-factor**  string | no description  Choices:   - `"disable"` - `"fortitoken-cloud"` |
| **two-factor-authentication**  string | no description  Choices:   - `"fortitoken"` - `"email"` - `"sms"` |
| **two-factor-notification**  string | no description  Choices:   - `"email"` - `"sms"` |
| **type**  string | no description  Choices:   - `"simple"` - `"anonymous"` - `"regular"` |
| **user-info-exchange-server**  string | no description |
| **username**  string | no description |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_user_ldap_dynamicmapping_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_user_ldap_dynamicmapping_module.md#id4)

```yaml+jinja
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
   - name: retrieve all the dynamic mappings of LDAP server
     fmgr_fact:
       facts:
           selector: 'user_ldap_dynamicmapping'
           params:
               adom: 'ansible'
               ldap: 'ansible-test-ldap' # name
               dynamic_mapping: 'your_value'

- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Configure dynamic mappings of LDAP server
     fmgr_user_ldap_dynamicmapping:
        bypass_validation: False
        adom: ansible
        ldap: ansible-test-ldap # name
        state: present
        user_ldap_dynamicmapping:
           _scope:
             -
                 name: FGT_AWS # need a valid device name
                 vdom: root # need a valid vdom name under the device
           dn: ansible-test-dn
           password: fortinet
           port: 9000
           server: ansible
           username: ansible-test-dyn
```

## [Return Values](fmgr_user_ldap_dynamicmapping_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **request_url**  string | The full url requested  Returned: always  Sample: `"/sys/login/user"` |
| **response_code**  integer | The status of api request  Returned: always  Sample: `0` |
| **response_message**  string | The descriptive message of the api response  Returned: always  Sample: `"OK."` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/issues)
[Homepage](https://fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/tree/galaxy/2.1.7)
