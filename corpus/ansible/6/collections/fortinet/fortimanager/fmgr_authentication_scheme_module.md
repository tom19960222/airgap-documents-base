---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_authentication_scheme module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_authentication_scheme_module.html
fetched_at: 2026-07-27T17:28:35+00:00
---
# fortinet.fortimanager.fmgr_authentication_scheme module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_authentication_scheme`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_authentication_scheme_module.md#synopsis)
- [Parameters](fmgr_authentication_scheme_module.md#parameters)
- [Notes](fmgr_authentication_scheme_module.md#notes)
- [Examples](fmgr_authentication_scheme_module.md#examples)
- [Return Values](fmgr_authentication_scheme_module.md#return-values)

## [Synopsis](fmgr_authentication_scheme_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_authentication_scheme_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **authentication_scheme**  dictionary | the top level parameters set |
| **domain-controller**  string | no description |
| **ems-device-owner**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **fsso-agent-for-ntlm**  string | no description |
| **fsso-guest**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **kerberos-keytab**  string | no description |
| **method**  list / elements=string | no description  Choices:   - `"ntlm"` - `"basic"` - `"digest"` - `"form"` - `"negotiate"` - `"fsso"` - `"rsso"` - `"ssh-publickey"` - `"saml"` - `"cert"` - `"x-auth-user"` - `"saml-sp"` |
| **name**  string | no description |
| **negotiate-ntlm**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **require-tfa**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **saml-server**  string | no description |
| **saml-timeout**  integer | no description |
| **ssh-ca**  string | no description |
| **user-cert**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **user-database**  string | no description |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_authentication_scheme_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_authentication_scheme_module.md#id4)

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
     fmgr_authentication_scheme:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        authentication_scheme:
           domain-controller: <value of string>
           fsso-agent-for-ntlm: <value of string>
           fsso-guest: <value in [disable, enable]>
           kerberos-keytab: <value of string>
           method:
             - ntlm
             - basic
             - digest
             - form
             - negotiate
             - fsso
             - rsso
             - ssh-publickey
             - saml
             - cert
             - x-auth-user
             - saml-sp
           name: <value of string>
           negotiate-ntlm: <value in [disable, enable]>
           require-tfa: <value in [disable, enable]>
           ssh-ca: <value of string>
           user-database: <value of string>
           ems-device-owner: <value in [disable, enable]>
           saml-server: <value of string>
           saml-timeout: <value of integer>
           user-cert: <value in [disable, enable]>
```

## [Return Values](fmgr_authentication_scheme_module.md#id5)

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
