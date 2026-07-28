---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_pkg_authentication_setting module – Configure authentication setting."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_pkg_authentication_setting_module.html
fetched_at: 2026-07-28T02:15:09+00:00
---
# fortinet.fortimanager.fmgr_pkg_authentication_setting module – Configure authentication setting.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_pkg_authentication_setting`.

New in fortinet.fortimanager 2.1.0

- [Synopsis](fmgr_pkg_authentication_setting_module.md#synopsis)
- [Parameters](fmgr_pkg_authentication_setting_module.md#parameters)
- [Notes](fmgr_pkg_authentication_setting_module.md#notes)
- [Examples](fmgr_pkg_authentication_setting_module.md#examples)
- [Return Values](fmgr_pkg_authentication_setting_module.md#return-values)

## [Synopsis](fmgr_pkg_authentication_setting_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_pkg_authentication_setting_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **pkg**  string / required | the parameter (pkg) in requested url |
| **pkg_authentication_setting**  dictionary | the top level parameters set |
| **active-auth-scheme**  string | Active authentication method |
| **auth-https**  string | Enable/disable redirecting HTTP user authentication to HTTPS.  **Choices:**   - `"disable"` - `"enable"` |
| **captive-portal**  string | Captive portal host name. |
| **captive-portal-ip**  string | Captive portal IP address. |
| **captive-portal-ip6**  string | Captive portal IPv6 address. |
| **captive-portal-port**  integer | Captive portal port number |
| **captive-portal-ssl-port**  integer | Captive portal SSL port number |
| **captive-portal-type**  string | Captive portal type.  **Choices:**   - `"fqdn"` - `"ip"` |
| **captive-portal6**  string | IPv6 captive portal host name. |
| **cert-auth**  string | Enable/disable redirecting certificate authentication to HTTPS portal.  **Choices:**   - `"disable"` - `"enable"` |
| **cert-captive-portal**  string | Certificate captive portal host name. |
| **cert-captive-portal-ip**  string | Certificate captive portal IP address. |
| **cert-captive-portal-port**  integer | Certificate captive portal port number |
| **cookie-max-age**  integer | Persistent web portal cookie maximum age in minutes |
| **cookie-refresh-div**  integer | Refresh rate divider of persistent web portal cookie |
| **dev-range**  any | (list or str) Address range for the IP based device query. |
| **ip-auth-cookie**  string | Enable/disable persistent cookie on IP based web portal authentication  **Choices:**   - `"disable"` - `"enable"` |
| **persistent-cookie**  string | Enable/disable persistent cookie on web portal authentication  **Choices:**   - `"disable"` - `"enable"` |
| **rewrite-https-port**  integer | Rewrite to HTTPS port |
| **sso-auth-scheme**  string | Single-Sign-On authentication method |
| **update-time**  string | Time of the last update. |
| **user-cert-ca**  any | (list or str) CA certificate used for client certificate verification. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_pkg_authentication_setting_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_pkg_authentication_setting_module.md#id4)

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
    - name: Configure authentication setting.
      fmgr_pkg_authentication_setting:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        pkg: <your own value>
        pkg_authentication_setting:
          active-auth-scheme: <string>
          auth-https: <value in [disable, enable]>
          captive-portal: <string>
          captive-portal-ip: <string>
          captive-portal-ip6: <string>
          captive-portal-port: <integer>
          captive-portal-ssl-port: <integer>
          captive-portal-type: <value in [fqdn, ip]>
          captive-portal6: <string>
          rewrite-https-port: <integer>
          sso-auth-scheme: <string>
          dev-range: <list or string>
          user-cert-ca: <list or string>
          cert-auth: <value in [disable, enable]>
          cert-captive-portal: <string>
          cert-captive-portal-ip: <string>
          cert-captive-portal-port: <integer>
          cookie-max-age: <integer>
          cookie-refresh-div: <integer>
          ip-auth-cookie: <value in [disable, enable]>
          persistent-cookie: <value in [disable, enable]>
          update-time: <string>
```

## [Return Values](fmgr_pkg_authentication_setting_module.md#id5)

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
