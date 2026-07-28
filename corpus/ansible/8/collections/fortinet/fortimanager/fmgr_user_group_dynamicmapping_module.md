---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_user_group_dynamicmapping module – Configure user groups."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_user_group_dynamicmapping_module.html
fetched_at: 2026-07-28T02:20:54+00:00
---
# fortinet.fortimanager.fmgr_user_group_dynamicmapping module – Configure user groups.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_user_group_dynamicmapping`.

New in fortinet.fortimanager 2.1.0

- [Synopsis](fmgr_user_group_dynamicmapping_module.md#synopsis)
- [Parameters](fmgr_user_group_dynamicmapping_module.md#parameters)
- [Notes](fmgr_user_group_dynamicmapping_module.md#notes)
- [Examples](fmgr_user_group_dynamicmapping_module.md#examples)
- [Return Values](fmgr_user_group_dynamicmapping_module.md#return-values)

## [Synopsis](fmgr_user_group_dynamicmapping_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_user_group_dynamicmapping_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **group**  string / required | the parameter (group) in requested url |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **user_group_dynamicmapping**  dictionary | the top level parameters set |
| **_scope**  list / elements=dictionary | no description |
| **name**  string | no description |
| **vdom**  string | no description |
| **auth-concurrent-override**  string | Enable/disable overriding the global number of concurrent authentication sessions for this user group.  **Choices:**   - `"disable"` - `"enable"` |
| **auth-concurrent-value**  integer | Maximum number of concurrent authenticated connections per user |
| **authtimeout**  integer | Authentication timeout in minutes for this user group. |
| **company**  string | Set the action for the company guest user field.  **Choices:**   - `"optional"` - `"mandatory"` - `"disabled"` |
| **email**  string | Enable/disable the guest user email address field.  **Choices:**   - `"disable"` - `"enable"` |
| **expire**  integer | Time in seconds before guest user accounts expire |
| **expire-type**  string | Determine when the expiration countdown begins.  **Choices:**   - `"immediately"` - `"first-successful-login"` |
| **group-type**  string | Set the group to be for firewall authentication, FSSO, RSSO, or guest users.  **Choices:**   - `"firewall"` - `"directory-service"` - `"fsso-service"` - `"guest"` - `"rsso"` |
| **guest**  list / elements=dictionary | no description |
| **comment**  string | Comment. |
| **company**  string | Set the action for the company guest user field. |
| **email**  string | Email. |
| **expiration**  string | Expire time. |
| **group**  string | no description |
| **id**  integer | Guest ID. |
| **mobile-phone**  string | Mobile phone. |
| **name**  string | Guest name. |
| **password**  any | (list) no description |
| **sponsor**  string | Set the action for the sponsor guest user field. |
| **user-id**  string | Guest ID. |
| **http-digest-realm**  string | Realm attribute for MD5-digest authentication. |
| **id**  integer / required | Group ID. |
| **ldap-memberof**  string | no description |
| **logic-type**  string | no description  **Choices:**   - `"or"` - `"and"` |
| **match**  list / elements=dictionary | no description |
| **_gui_meta**  string | no description |
| **group-name**  string | Name of matching user or group on remote authentication server. |
| **id**  integer | ID. |
| **server-name**  string | Name of remote auth server. |
| **max-accounts**  integer | Maximum number of guest accounts that can be created for this group |
| **member**  any | (list or str) no description |
| **mobile-phone**  string | Enable/disable the guest user mobile phone number field.  **Choices:**   - `"disable"` - `"enable"` |
| **multiple-guest-add**  string | Enable/disable addition of multiple guests.  **Choices:**   - `"disable"` - `"enable"` |
| **password**  string | Guest user password type.  **Choices:**   - `"auto-generate"` - `"specify"` - `"disable"` |
| **redir-url**  string | no description |
| **sms-custom-server**  string | SMS server. |
| **sms-server**  string | Send SMS through FortiGuard or other external server.  **Choices:**   - `"fortiguard"` - `"custom"` |
| **sponsor**  string | Set the action for the sponsor guest user field.  **Choices:**   - `"optional"` - `"mandatory"` - `"disabled"` |
| **sslvpn-bookmarks-group**  any | (list or str) no description |
| **sslvpn-cache-cleaner**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **sslvpn-client-check**  list / elements=string | no description  **Choices:**   - `"forticlient"` - `"forticlient-av"` - `"forticlient-fw"` - `"3rdAV"` - `"3rdFW"` |
| **sslvpn-ftp**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **sslvpn-http**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **sslvpn-os-check**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **sslvpn-os-check-list**  dictionary | no description |
| **action**  string | no description  **Choices:**   - `"allow"` - `"check-up-to-date"` - `"deny"` |
| **latest-patch-level**  string | no description |
| **name**  string | no description |
| **tolerance**  integer | no description |
| **sslvpn-portal**  any | (list or str) no description |
| **sslvpn-portal-heading**  string | no description |
| **sslvpn-rdp**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **sslvpn-samba**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **sslvpn-split-tunneling**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **sslvpn-ssh**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **sslvpn-telnet**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **sslvpn-tunnel**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **sslvpn-tunnel-endip**  string | no description |
| **sslvpn-tunnel-ip-mode**  string | no description  **Choices:**   - `"range"` - `"usrgrp"` |
| **sslvpn-tunnel-startip**  string | no description |
| **sslvpn-virtual-desktop**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **sslvpn-vnc**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **sslvpn-webapp**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **sso-attribute-value**  string | Name of the RADIUS user group that this local user group represents. |
| **user-id**  string | Guest user ID type.  **Choices:**   - `"email"` - `"auto-generate"` - `"specify"` |
| **user-name**  string | Enable/disable the guest user name entry.  **Choices:**   - `"disable"` - `"enable"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_user_group_dynamicmapping_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_user_group_dynamicmapping_module.md#id4)

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
    - name: Configure user groups.
      fmgr_user_group_dynamicmapping:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        group: <your own value>
        state: <value in [present, absent]>
        user_group_dynamicmapping:
          _scope:
            -
              name: <string>
              vdom: <string>
          auth-concurrent-override: <value in [disable, enable]>
          auth-concurrent-value: <integer>
          authtimeout: <integer>
          company: <value in [optional, mandatory, disabled]>
          email: <value in [disable, enable]>
          expire: <integer>
          expire-type: <value in [immediately, first-successful-login]>
          group-type: <value in [firewall, directory-service, fsso-service, ...]>
          guest:
            -
              comment: <string>
              company: <string>
              email: <string>
              expiration: <string>
              group: <string>
              id: <integer>
              mobile-phone: <string>
              name: <string>
              password: <list or string>
              sponsor: <string>
              user-id: <string>
          http-digest-realm: <string>
          id: <integer>
          ldap-memberof: <string>
          logic-type: <value in [or, and]>
          match:
            -
              _gui_meta: <string>
              group-name: <string>
              id: <integer>
              server-name: <string>
          max-accounts: <integer>
          member: <list or string>
          mobile-phone: <value in [disable, enable]>
          multiple-guest-add: <value in [disable, enable]>
          password: <value in [auto-generate, specify, disable]>
          redir-url: <string>
          sms-custom-server: <string>
          sms-server: <value in [fortiguard, custom]>
          sponsor: <value in [optional, mandatory, disabled]>
          sslvpn-bookmarks-group: <list or string>
          sslvpn-cache-cleaner: <value in [disable, enable]>
          sslvpn-client-check:
            - forticlient
            - forticlient-av
            - forticlient-fw
            - 3rdAV
            - 3rdFW
          sslvpn-ftp: <value in [disable, enable]>
          sslvpn-http: <value in [disable, enable]>
          sslvpn-os-check: <value in [disable, enable]>
          sslvpn-os-check-list:
            action: <value in [allow, check-up-to-date, deny]>
            latest-patch-level: <string>
            name: <string>
            tolerance: <integer>
          sslvpn-portal: <list or string>
          sslvpn-portal-heading: <string>
          sslvpn-rdp: <value in [disable, enable]>
          sslvpn-samba: <value in [disable, enable]>
          sslvpn-split-tunneling: <value in [disable, enable]>
          sslvpn-ssh: <value in [disable, enable]>
          sslvpn-telnet: <value in [disable, enable]>
          sslvpn-tunnel: <value in [disable, enable]>
          sslvpn-tunnel-endip: <string>
          sslvpn-tunnel-ip-mode: <value in [range, usrgrp]>
          sslvpn-tunnel-startip: <string>
          sslvpn-virtual-desktop: <value in [disable, enable]>
          sslvpn-vnc: <value in [disable, enable]>
          sslvpn-webapp: <value in [disable, enable]>
          sso-attribute-value: <string>
          user-id: <value in [email, auto-generate, specify]>
          user-name: <value in [disable, enable]>
```

## [Return Values](fmgr_user_group_dynamicmapping_module.md#id5)

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
