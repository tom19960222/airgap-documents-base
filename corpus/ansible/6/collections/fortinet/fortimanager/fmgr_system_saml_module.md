---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_system_saml module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_system_saml_module.html
fetched_at: 2026-07-27T17:37:17+00:00
---
# fortinet.fortimanager.fmgr_system_saml module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_saml`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_system_saml_module.md#synopsis)
- [Parameters](fmgr_system_saml_module.md#parameters)
- [Notes](fmgr_system_saml_module.md#notes)
- [Examples](fmgr_system_saml_module.md#examples)
- [Return Values](fmgr_system_saml_module.md#return-values)

## [Synopsis](fmgr_system_saml_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_saml_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **system_saml**  dictionary | the top level parameters set |
| **acs-url**  string | no description |
| **cert**  string | no description |
| **default-profile**  string | no description  Default: `"Restricted_User"` |
| **entity-id**  string | no description |
| **fabric-idp**  list / elements=string | no description |
| **dev-id**  string | no description |
| **idp-cert**  string | no description |
| **idp-entity-id**  string | no description |
| **idp-single-logout-url**  string | no description |
| **idp-single-sign-on-url**  string | no description |
| **idp-status**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **forticloud-sso**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **idp-cert**  string | no description |
| **idp-entity-id**  string | no description |
| **idp-single-logout-url**  string | no description |
| **idp-single-sign-on-url**  string | no description |
| **login-auto-redirect**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **role**  string | no description  no description  no description  Choices:   - `"IDP"` - `"SP"` ← (default) - `"FAB-SP"` |
| **server-address**  string | no description |
| **service-providers**  list / elements=string | no description |
| **idp-entity-id**  string | no description |
| **idp-single-logout-url**  string | no description |
| **idp-single-sign-on-url**  string | no description |
| **name**  string | no description |
| **prefix**  string | no description |
| **sp-adom**  string | no description |
| **sp-cert**  string | no description |
| **sp-entity-id**  string | no description |
| **sp-profile**  string | no description |
| **sp-single-logout-url**  string | no description |
| **sp-single-sign-on-url**  string | no description |
| **sls-url**  string | no description |
| **status**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **user-auto-create**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_system_saml_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_saml_module.md#id4)

```yaml+jinja
- hosts: fortimanager-inventory
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: no description
     fmgr_system_saml:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        system_saml:
           acs-url: <value of string>
           cert: <value of string>
           entity-id: <value of string>
           idp-cert: <value of string>
           idp-entity-id: <value of string>
           idp-single-logout-url: <value of string>
           idp-single-sign-on-url: <value of string>
           login-auto-redirect: <value in [disable, enable]>
           role: <value in [IDP, SP, FAB-SP]>
           server-address: <value of string>
           service-providers:
             -
                 idp-entity-id: <value of string>
                 idp-single-logout-url: <value of string>
                 idp-single-sign-on-url: <value of string>
                 name: <value of string>
                 prefix: <value of string>
                 sp-cert: <value of string>
                 sp-entity-id: <value of string>
                 sp-single-logout-url: <value of string>
                 sp-single-sign-on-url: <value of string>
                 sp-adom: <value of string>
                 sp-profile: <value of string>
           sls-url: <value of string>
           status: <value in [disable, enable]>
           default-profile: <value of string>
           fabric-idp:
             -
                 dev-id: <value of string>
                 idp-cert: <value of string>
                 idp-entity-id: <value of string>
                 idp-single-logout-url: <value of string>
                 idp-single-sign-on-url: <value of string>
                 idp-status: <value in [disable, enable]>
           forticloud-sso: <value in [disable, enable]>
           user-auto-create: <value in [disable, enable]>
```

## [Return Values](fmgr_system_saml_module.md#id5)

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
