---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_system_saml module – Global settings for SAML authentication."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_system_saml_module.html
fetched_at: 2026-07-28T02:20:08+00:00
---
# fortinet.fortimanager.fmgr_system_saml module – Global settings for SAML authentication.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_saml`.

New in fortinet.fortimanager 2.0.0

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
| **access_token**  string | The token to access FortiManager without using username and password. |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **system_saml**  dictionary | the top level parameters set |
| **acs-url**  string | SP ACS |
| **auth-request-signed**  string | Enable/Disable auth request signed.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **cert**  string | Certificate name. |
| **default-profile**  string | Default Profile Name. |
| **entity-id**  string | SP entity ID. |
| **fabric-idp**  list / elements=dictionary | Fabric-Idp. |
| **dev-id**  string | IDP Device ID. |
| **idp-cert**  string | IDP Certificate name. |
| **idp-entity-id**  string | IDP entity ID. |
| **idp-single-logout-url**  string | IDP single logout url. |
| **idp-single-sign-on-url**  string | IDP single sign-on URL. |
| **idp-status**  string | Enable/disable SAML authentication  disable - Disable SAML authentication.  enable - Enabld SAML authentication.  **Choices:**   - `"disable"` - `"enable"` |
| **forticloud-sso**  string | Enable/disable FortiCloud SSO  disable - Disable Forticloud SSO.  enable - Enabld Forticloud SSO.  **Choices:**   - `"disable"` - `"enable"` |
| **idp-cert**  string | IDP Certificate name. |
| **idp-entity-id**  string | IDP entity ID. |
| **idp-single-logout-url**  string | IDP single logout url. |
| **idp-single-sign-on-url**  string | IDP single sign-on URL. |
| **login-auto-redirect**  string | Enable/Disable auto redirect to IDP login page.  disable - Disable auto redirect to IDP Login Page.  enable - Enable auto redirect to IDP Login Page.  **Choices:**   - `"disable"` - `"enable"` |
| **role**  string | SAML role.  IDP - IDentiy Provider.  SP - Service Provider.  **Choices:**   - `"IDP"` - `"SP"` - `"FAB-SP"` |
| **server-address**  string | server address. |
| **service-providers**  list / elements=dictionary | Service-Providers. |
| **idp-entity-id**  string | IDP Entity ID. |
| **idp-single-logout-url**  string | IDP single logout url. |
| **idp-single-sign-on-url**  string | IDP single sign-on URL. |
| **name**  string | Name. |
| **prefix**  string | Prefix. |
| **sp-adom**  string | SP adom name. |
| **sp-cert**  string | SP certificate name. |
| **sp-entity-id**  string | SP Entity ID. |
| **sp-profile**  string | SP profile name. |
| **sp-single-logout-url**  string | SP single logout URL. |
| **sp-single-sign-on-url**  string | SP single sign-on URL. |
| **sls-url**  string | SP SLS |
| **status**  string | Enable/disable SAML authentication  disable - Disable SAML authentication.  enable - Enabld SAML authentication.  **Choices:**   - `"disable"` - `"enable"` |
| **user-auto-create**  string | Enable/disable user auto creation  disable - Disable auto create user.  enable - Enable auto create user.  **Choices:**   - `"disable"` - `"enable"` |
| **want-assertions-signed**  string | Enable/Disable want assertions signed.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

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
    - name: Global settings for SAML authentication.
      fmgr_system_saml:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        system_saml:
          acs-url: <string>
          cert: <string>
          entity-id: <string>
          idp-cert: <string>
          idp-entity-id: <string>
          idp-single-logout-url: <string>
          idp-single-sign-on-url: <string>
          login-auto-redirect: <value in [disable, enable]>
          role: <value in [IDP, SP, FAB-SP]>
          server-address: <string>
          service-providers:
            -
              idp-entity-id: <string>
              idp-single-logout-url: <string>
              idp-single-sign-on-url: <string>
              name: <string>
              prefix: <string>
              sp-cert: <string>
              sp-entity-id: <string>
              sp-single-logout-url: <string>
              sp-single-sign-on-url: <string>
              sp-adom: <string>
              sp-profile: <string>
          sls-url: <string>
          status: <value in [disable, enable]>
          default-profile: <string>
          fabric-idp:
            -
              dev-id: <string>
              idp-cert: <string>
              idp-entity-id: <string>
              idp-single-logout-url: <string>
              idp-single-sign-on-url: <string>
              idp-status: <value in [disable, enable]>
          forticloud-sso: <value in [disable, enable]>
          user-auto-create: <value in [disable, enable]>
          auth-request-signed: <value in [disable, enable]>
          want-assertions-signed: <value in [disable, enable]>
```

## [Return Values](fmgr_system_saml_module.md#id5)

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
