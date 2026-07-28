---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_vpnsslweb_portal_bookmarkgroup module – Portal bookmark group."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_vpnsslweb_portal_bookmarkgroup_module.html
fetched_at: 2026-07-28T02:21:50+00:00
---
# fortinet.fortimanager.fmgr_vpnsslweb_portal_bookmarkgroup module – Portal bookmark group.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_vpnsslweb_portal_bookmarkgroup`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_vpnsslweb_portal_bookmarkgroup_module.md#synopsis)
- [Parameters](fmgr_vpnsslweb_portal_bookmarkgroup_module.md#parameters)
- [Notes](fmgr_vpnsslweb_portal_bookmarkgroup_module.md#notes)
- [Examples](fmgr_vpnsslweb_portal_bookmarkgroup_module.md#examples)
- [Return Values](fmgr_vpnsslweb_portal_bookmarkgroup_module.md#return-values)

## [Synopsis](fmgr_vpnsslweb_portal_bookmarkgroup_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_vpnsslweb_portal_bookmarkgroup_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **portal**  string / required | the parameter (portal) in requested url |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **vpnsslweb_portal_bookmarkgroup**  dictionary | the top level parameters set |
| **bookmarks**  list / elements=dictionary | no description |
| **additional-params**  string | Additional parameters. |
| **apptype**  string | Application type.  **Choices:**   - `"web"` - `"telnet"` - `"ssh"` - `"ftp"` - `"smb"` - `"vnc"` - `"rdp"` - `"citrix"` - `"rdpnative"` - `"portforward"` - `"sftp"` |
| **color-depth**  string | Color depth per pixel.  **Choices:**   - `"8"` - `"16"` - `"32"` |
| **description**  string | Description. |
| **domain**  string | Login domain. |
| **folder**  string | Network shared file folder parameter. |
| **form-data**  list / elements=dictionary | no description |
| **name**  string | Name. |
| **value**  string | Value. |
| **height**  integer | Screen height |
| **host**  string | Host name/IP parameter. |
| **keyboard-layout**  string | Keyboard layout.  **Choices:**   - `"ar"` - `"da"` - `"de"` - `"de-ch"` - `"en-gb"` - `"en-uk"` - `"en-us"` - `"es"` - `"fi"` - `"fr"` - `"fr-be"` - `"fr-ca"` - `"fr-ch"` - `"hr"` - `"hu"` - `"it"` - `"ja"` - `"lt"` - `"lv"` - `"mk"` - `"no"` - `"pl"` - `"pt"` - `"pt-br"` - `"ru"` - `"sl"` - `"sv"` - `"tk"` - `"tr"` - `"fr-ca-m"` - `"wg"` - `"ar-101"` - `"ar-102"` - `"ar-102-azerty"` - `"can-mul"` - `"cz"` - `"cz-qwerty"` - `"cz-pr"` - `"nl"` - `"de-ibm"` - `"en-uk-ext"` - `"en-us-dvorak"` - `"es-var"` - `"fi-sami"` - `"hu-101"` - `"it-142"` - `"ko"` - `"lt-ibm"` - `"lt-std"` - `"lav-std"` - `"lav-leg"` - `"mk-std"` - `"no-sami"` - `"pol-214"` - `"pol-pr"` - `"pt-br-abnt2"` - `"ru-mne"` - `"ru-t"` - `"sv-sami"` - `"tuk"` - `"tur-f"` - `"tur-q"` - `"zh-sym-sg-us"` - `"zh-sym-us"` - `"zh-tr-hk"` - `"zh-tr-mo"` - `"zh-tr-us"` - `"fr-apple"` - `"la-am"` |
| **listening-port**  integer | Listening port |
| **load-balancing-info**  string | The load balancing information or cookie which should be provided to the connection broker. |
| **logon-password**  any | (list) no description |
| **logon-user**  string | Logon user. |
| **name**  string | Bookmark name. |
| **port**  integer | Remote port. |
| **preconnection-blob**  string | An arbitrary string which identifies the RDP source. |
| **preconnection-id**  integer | The numeric ID of the RDP source |
| **remote-port**  integer | Remote port |
| **restricted-admin**  string | Enable/disable restricted admin mode for RDP.  **Choices:**   - `"disable"` - `"enable"` |
| **security**  string | Security mode for RDP connection.  **Choices:**   - `"rdp"` - `"nla"` - `"tls"` - `"any"` |
| **send-preconnection-id**  string | Enable/disable sending of preconnection ID.  **Choices:**   - `"disable"` - `"enable"` |
| **server-layout**  string | Server side keyboard layout.  **Choices:**   - `"en-us-qwerty"` - `"de-de-qwertz"` - `"fr-fr-azerty"` - `"it-it-qwerty"` - `"sv-se-qwerty"` - `"failsafe"` - `"en-gb-qwerty"` - `"es-es-qwerty"` - `"fr-ch-qwertz"` - `"ja-jp-qwerty"` - `"pt-br-qwerty"` - `"tr-tr-qwerty"` - `"fr-ca-qwerty"` |
| **show-status-window**  string | Enable/disable showing of status window.  **Choices:**   - `"disable"` - `"enable"` |
| **sso**  string | Single Sign-On.  **Choices:**   - `"disable"` - `"static"` - `"auto"` |
| **sso-credential**  string | Single sign-on credentials.  **Choices:**   - `"sslvpn-login"` - `"alternative"` |
| **sso-credential-sent-once**  string | Single sign-on credentials are only sent once to remote server.  **Choices:**   - `"disable"` - `"enable"` |
| **sso-password**  any | (list) no description |
| **sso-username**  string | SSO user name. |
| **url**  string | URL parameter. |
| **vnc-keyboard-layout**  string | Keyboard layout.  **Choices:**   - `"da"` - `"de"` - `"de-ch"` - `"en-uk"` - `"es"` - `"fi"` - `"fr"` - `"fr-be"` - `"it"` - `"no"` - `"pt"` - `"sv"` - `"nl"` - `"en-uk-ext"` - `"it-142"` - `"pt-br-abnt2"` - `"default"` - `"fr-ca-mul"` - `"gd"` - `"us-intl"` |
| **width**  integer | Screen width |
| **name**  string / required | Bookmark group name. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_vpnsslweb_portal_bookmarkgroup_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_vpnsslweb_portal_bookmarkgroup_module.md#id4)

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
    - name: Portal bookmark group.
      fmgr_vpnsslweb_portal_bookmarkgroup:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        portal: <your own value>
        state: <value in [present, absent]>
        vpnsslweb_portal_bookmarkgroup:
          bookmarks:
            -
              additional-params: <string>
              apptype: <value in [web, telnet, ssh, ...]>
              description: <string>
              folder: <string>
              form-data:
                -
                  name: <string>
                  value: <string>
              host: <string>
              listening-port: <integer>
              load-balancing-info: <string>
              logon-password: <list or string>
              logon-user: <string>
              name: <string>
              port: <integer>
              preconnection-blob: <string>
              preconnection-id: <integer>
              remote-port: <integer>
              security: <value in [rdp, nla, tls, ...]>
              server-layout: <value in [en-us-qwerty, de-de-qwertz, fr-fr-azerty, ...]>
              show-status-window: <value in [disable, enable]>
              sso: <value in [disable, static, auto]>
              sso-credential: <value in [sslvpn-login, alternative]>
              sso-credential-sent-once: <value in [disable, enable]>
              sso-password: <list or string>
              sso-username: <string>
              url: <string>
              domain: <string>
              color-depth: <value in [8, 16, 32]>
              height: <integer>
              keyboard-layout: <value in [ar, da, de, ...]>
              restricted-admin: <value in [disable, enable]>
              send-preconnection-id: <value in [disable, enable]>
              width: <integer>
              vnc-keyboard-layout: <value in [da, de, de-ch, ...]>
          name: <string>
```

## [Return Values](fmgr_vpnsslweb_portal_bookmarkgroup_module.md#id5)

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
