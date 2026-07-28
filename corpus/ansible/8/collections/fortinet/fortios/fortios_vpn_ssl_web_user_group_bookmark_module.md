---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_vpn_ssl_web_user_group_bookmark module – Configure SSL-VPN user group bookmark in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_vpn_ssl_web_user_group_bookmark_module.html
fetched_at: 2026-07-28T02:30:31+00:00
---
# fortinet.fortios.fortios_vpn_ssl_web_user_group_bookmark module – Configure SSL-VPN user group bookmark in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/ui/repo/published/fortinet/fortios/) (version 2.3.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_vpn_ssl_web_user_group_bookmark_module.md#ansible-collections-fortinet-fortios-fortios-vpn-ssl-web-user-group-bookmark-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_vpn_ssl_web_user_group_bookmark`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_vpn_ssl_web_user_group_bookmark_module.md#synopsis)
- [Requirements](fortios_vpn_ssl_web_user_group_bookmark_module.md#requirements)
- [Parameters](fortios_vpn_ssl_web_user_group_bookmark_module.md#parameters)
- [Notes](fortios_vpn_ssl_web_user_group_bookmark_module.md#notes)
- [Examples](fortios_vpn_ssl_web_user_group_bookmark_module.md#examples)
- [Return Values](fortios_vpn_ssl_web_user_group_bookmark_module.md#return-values)

## [Synopsis](fortios_vpn_ssl_web_user_group_bookmark_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify vpn_ssl_web feature and user_group_bookmark category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_vpn_ssl_web_user_group_bookmark_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_vpn_ssl_web_user_group_bookmark_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |
| **vpn_ssl_web_user_group_bookmark**  dictionary | Configure SSL-VPN user group bookmark. |
| **bookmarks**  list / elements=dictionary | Bookmark table. |
| **additional_params**  string | Additional parameters. |
| **apptype**  string | Application type.  **Choices:**   - `"ftp"` - `"rdp"` - `"sftp"` - `"smb"` - `"ssh"` - `"telnet"` - `"vnc"` - `"web"` - `"citrix"` - `"portforward"` |
| **color_depth**  string | Color depth per pixel.  **Choices:**   - `"32"` - `"16"` - `"8"` |
| **description**  string | Description. |
| **domain**  string | Login domain. |
| **folder**  string | Network shared file folder parameter. |
| **form_data**  list / elements=dictionary | Form data. |
| **name**  string / required | Name. |
| **value**  string | Value. |
| **height**  integer | Screen height (range from 0 - 65535). |
| **host**  string | Host name/IP parameter. |
| **keyboard_layout**  string | Keyboard layout.  **Choices:**   - `"ar-101"` - `"ar-102"` - `"ar-102-azerty"` - `"can-mul"` - `"cz"` - `"cz-qwerty"` - `"cz-pr"` - `"da"` - `"nl"` - `"de"` - `"de-ch"` - `"de-ibm"` - `"en-uk"` - `"en-uk-ext"` - `"en-us"` - `"en-us-dvorak"` - `"es"` - `"es-var"` - `"fi"` - `"fi-sami"` - `"fr"` - `"fr-apple"` - `"fr-ca"` - `"fr-ch"` - `"fr-be"` - `"hr"` - `"hu"` - `"hu-101"` - `"it"` - `"it-142"` - `"ja"` - `"ko"` - `"la-am"` - `"lt"` - `"lt-ibm"` - `"lt-std"` - `"lav-std"` - `"lav-leg"` - `"mk"` - `"mk-std"` - `"no"` - `"no-sami"` - `"pol-214"` - `"pol-pr"` - `"pt"` - `"pt-br"` - `"pt-br-abnt2"` - `"ru"` - `"ru-mne"` - `"ru-t"` - `"sl"` - `"sv"` - `"sv-sami"` - `"tuk"` - `"tur-f"` - `"tur-q"` - `"zh-sym-sg-us"` - `"zh-sym-us"` - `"zh-tr-hk"` - `"zh-tr-mo"` - `"zh-tr-us"` |
| **listening_port**  integer | Listening port (0 - 65535). |
| **load_balancing_info**  string | The load balancing information or cookie which should be provided to the connection broker. |
| **logon_password**  string | Logon password. |
| **logon_user**  string | Logon user. |
| **name**  string / required | Bookmark name. |
| **port**  integer | Remote port. |
| **preconnection_blob**  string | An arbitrary string which identifies the RDP source. |
| **preconnection_id**  integer | The numeric ID of the RDP source (0-4294967295). |
| **remote_port**  integer | Remote port (0 - 65535). |
| **restricted_admin**  string | Enable/disable restricted admin mode for RDP.  **Choices:**   - `"enable"` - `"disable"` |
| **security**  string | Security mode for RDP connection .  **Choices:**   - `"any"` - `"rdp"` - `"nla"` - `"tls"` |
| **send_preconnection_id**  string | Enable/disable sending of preconnection ID.  **Choices:**   - `"enable"` - `"disable"` |
| **server_layout**  string | Server side keyboard layout.  **Choices:**   - `"de-de-qwertz"` - `"en-gb-qwerty"` - `"en-us-qwerty"` - `"es-es-qwerty"` - `"fr-ca-qwerty"` - `"fr-fr-azerty"` - `"fr-ch-qwertz"` - `"it-it-qwerty"` - `"ja-jp-qwerty"` - `"pt-br-qwerty"` - `"sv-se-qwerty"` - `"tr-tr-qwerty"` - `"failsafe"` |
| **show_status_window**  string | Enable/disable showing of status window.  **Choices:**   - `"enable"` - `"disable"` |
| **sso**  string | Single sign-on.  **Choices:**   - `"disable"` - `"static"` - `"auto"` |
| **sso_credential**  string | Single sign-on credentials.  **Choices:**   - `"sslvpn-login"` - `"alternative"` |
| **sso_credential_sent_once**  string | Single sign-on credentials are only sent once to remote server.  **Choices:**   - `"enable"` - `"disable"` |
| **sso_password**  string | SSO password. |
| **sso_username**  string | SSO user name. |
| **url**  string | URL parameter. |
| **vnc_keyboard_layout**  string | Keyboard layout.  **Choices:**   - `"default"` - `"da"` - `"nl"` - `"en-uk"` - `"en-uk-ext"` - `"fi"` - `"fr"` - `"fr-be"` - `"fr-ca-mul"` - `"de"` - `"de-ch"` - `"it"` - `"it-142"` - `"pt"` - `"pt-br-abnt2"` - `"no"` - `"gd"` - `"es"` - `"sv"` - `"us-intl"` |
| **width**  integer | Screen width (range from 0 - 65535). |
| **name**  string / required | Group name. Source user.group.name. |

## [Notes](fortios_vpn_ssl_web_user_group_bookmark_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_vpn_ssl_web_user_group_bookmark_module.md#id5)

```yaml+jinja
- hosts: fortigates
  collections:
    - fortinet.fortios
  connection: httpapi
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:
  - name: Configure SSL-VPN user group bookmark.
    fortios_vpn_ssl_web_user_group_bookmark:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      vpn_ssl_web_user_group_bookmark:
        bookmarks:
         -
            additional_params: "<your_own_value>"
            apptype: "ftp"
            color_depth: "32"
            description: "<your_own_value>"
            domain: "<your_own_value>"
            folder: "<your_own_value>"
            form_data:
             -
                name: "default_name_11"
                value: "<your_own_value>"
            height: "768"
            host: "myhostname"
            keyboard_layout: "ar-101"
            listening_port: "0"
            load_balancing_info: "<your_own_value>"
            logon_password: "<your_own_value>"
            logon_user: "<your_own_value>"
            name: "default_name_20"
            port: "0"
            preconnection_blob: "<your_own_value>"
            preconnection_id: "2147483648"
            remote_port: "0"
            restricted_admin: "enable"
            security: "any"
            send_preconnection_id: "enable"
            server_layout: "de-de-qwertz"
            show_status_window: "enable"
            sso: "disable"
            sso_credential: "sslvpn-login"
            sso_credential_sent_once: "enable"
            sso_password: "<your_own_value>"
            sso_username: "<your_own_value>"
            url: "myurl.com"
            vnc_keyboard_layout: "default"
            width: "1024"
        name: "default_name_38 (source user.group.name)"
```

## [Return Values](fortios_vpn_ssl_web_user_group_bookmark_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  **Returned:** always  **Sample:** `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  **Returned:** always  **Sample:** `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  **Returned:** always  **Sample:** `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  **Returned:** success  **Sample:** `"id"` |
| **name**  string | Name of the table used to fulfill the request  **Returned:** always  **Sample:** `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  **Returned:** always  **Sample:** `"webfilter"` |
| **revision**  string | Internal revision number  **Returned:** always  **Sample:** `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  **Returned:** always  **Sample:** `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  **Returned:** always  **Sample:** `"success"` |
| **vdom**  string | Virtual domain used  **Returned:** always  **Sample:** `"root"` |
| **version**  string | Version of the FortiGate  **Returned:** always  **Sample:** `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
- [Homepage](https://www.fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
