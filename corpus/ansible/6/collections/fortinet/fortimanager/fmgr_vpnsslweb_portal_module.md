---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_vpnsslweb_portal module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_vpnsslweb_portal_module.html
fetched_at: 2026-07-27T17:38:37+00:00
---
# fortinet.fortimanager.fmgr_vpnsslweb_portal module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_vpnsslweb_portal`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_vpnsslweb_portal_module.md#synopsis)
- [Parameters](fmgr_vpnsslweb_portal_module.md#parameters)
- [Notes](fmgr_vpnsslweb_portal_module.md#notes)
- [Examples](fmgr_vpnsslweb_portal_module.md#examples)
- [Return Values](fmgr_vpnsslweb_portal_module.md#return-values)

## [Synopsis](fmgr_vpnsslweb_portal_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_vpnsslweb_portal_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **vpnsslweb_portal**  dictionary | the top level parameters set |
| **allow-user-access**  list / elements=string | no description  Choices:   - `"web"` - `"ftp"` - `"telnet"` - `"smb"` - `"vnc"` - `"rdp"` - `"ssh"` - `"ping"` - `"citrix"` - `"portforward"` - `"sftp"` |
| **auto-connect**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **bookmark-group**  list / elements=string | no description |
| **bookmarks**  list / elements=string | no description |
| **additional-params**  string | no description |
| **apptype**  string | no description  Choices:   - `"web"` - `"telnet"` - `"ssh"` - `"ftp"` - `"smb"` - `"vnc"` - `"rdp"` - `"citrix"` - `"rdpnative"` - `"portforward"` - `"sftp"` |
| **color-depth**  string | no description  Choices:   - `"8"` - `"16"` - `"32"` |
| **description**  string | no description |
| **domain**  string | no description |
| **folder**  string | no description |
| **form-data**  list / elements=string | no description |
| **name**  string | no description |
| **value**  string | no description |
| **height**  integer | no description |
| **host**  string | no description |
| **keyboard-layout**  string | no description  Choices:   - `"ar"` - `"da"` - `"de"` - `"de-ch"` - `"en-gb"` - `"en-uk"` - `"en-us"` - `"es"` - `"fi"` - `"fr"` - `"fr-be"` - `"fr-ca"` - `"fr-ch"` - `"hr"` - `"hu"` - `"it"` - `"ja"` - `"lt"` - `"lv"` - `"mk"` - `"no"` - `"pl"` - `"pt"` - `"pt-br"` - `"ru"` - `"sl"` - `"sv"` - `"tk"` - `"tr"` - `"fr-ca-m"` - `"wg"` - `"ar-101"` - `"ar-102"` - `"ar-102-azerty"` - `"can-mul"` - `"cz"` - `"cz-qwerty"` - `"cz-pr"` - `"nl"` - `"de-ibm"` - `"en-uk-ext"` - `"en-us-dvorak"` - `"es-var"` - `"fi-sami"` - `"hu-101"` - `"it-142"` - `"ko"` - `"lt-ibm"` - `"lt-std"` - `"lav-std"` - `"lav-leg"` - `"mk-std"` - `"no-sami"` - `"pol-214"` - `"pol-pr"` - `"pt-br-abnt2"` - `"ru-mne"` - `"ru-t"` - `"sv-sami"` - `"tuk"` - `"tur-f"` - `"tur-q"` - `"zh-sym-sg-us"` - `"zh-sym-us"` - `"zh-tr-hk"` - `"zh-tr-mo"` - `"zh-tr-us"` - `"fr-apple"` |
| **listening-port**  integer | no description |
| **load-balancing-info**  string | no description |
| **logon-password**  string | no description |
| **logon-user**  string | no description |
| **name**  string | no description |
| **port**  integer | no description |
| **preconnection-blob**  string | no description |
| **preconnection-id**  integer | no description |
| **remote-port**  integer | no description |
| **restricted-admin**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **security**  string | no description  Choices:   - `"rdp"` - `"nla"` - `"tls"` - `"any"` |
| **send-preconnection-id**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **server-layout**  string | no description  Choices:   - `"en-us-qwerty"` - `"de-de-qwertz"` - `"fr-fr-azerty"` - `"it-it-qwerty"` - `"sv-se-qwerty"` - `"failsafe"` - `"en-gb-qwerty"` - `"es-es-qwerty"` - `"fr-ch-qwertz"` - `"ja-jp-qwerty"` - `"pt-br-qwerty"` - `"tr-tr-qwerty"` - `"fr-ca-qwerty"` |
| **show-status-window**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sso**  string | no description  Choices:   - `"disable"` - `"static"` - `"auto"` |
| **sso-credential**  string | no description  Choices:   - `"sslvpn-login"` - `"alternative"` |
| **sso-credential-sent-once**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sso-password**  string | no description |
| **sso-username**  string | no description |
| **url**  string | no description |
| **width**  integer | no description |
| **name**  string | no description |
| **clipboard**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **custom-lang**  string | no description |
| **customize-forticlient-download-url**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **default-window-height**  integer | no description |
| **default-window-width**  integer | no description |
| **display-bookmark**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **display-connection-tools**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **display-history**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **display-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dns-server1**  string | no description |
| **dns-server2**  string | no description |
| **dns-suffix**  string | no description |
| **exclusive-routing**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **forticlient-download**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **forticlient-download-method**  string | no description  Choices:   - `"direct"` - `"ssl-vpn"` |
| **heading**  string | no description |
| **hide-sso-credential**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **host-check**  string | no description  Choices:   - `"none"` - `"av"` - `"fw"` - `"av-fw"` - `"custom"` |
| **host-check-interval**  integer | no description |
| **host-check-policy**  string | no description |
| **ip-mode**  string | no description  Choices:   - `"range"` - `"user-group"` |
| **ip-pools**  string | no description |
| **ipv6-dns-server1**  string | no description |
| **ipv6-dns-server2**  string | no description |
| **ipv6-exclusive-routing**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ipv6-pools**  string | no description |
| **ipv6-service-restriction**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ipv6-split-tunneling**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ipv6-split-tunneling-routing-address**  string | no description |
| **ipv6-split-tunneling-routing-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ipv6-tunnel-mode**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ipv6-wins-server1**  string | no description |
| **ipv6-wins-server2**  string | no description |
| **keep-alive**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **limit-user-logins**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mac-addr-action**  string | no description  Choices:   - `"deny"` - `"allow"` |
| **mac-addr-check**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mac-addr-check-rule**  list / elements=string | no description |
| **mac-addr-list**  string | no description |
| **mac-addr-mask**  integer | no description |
| **name**  string | no description |
| **macos-forticlient-download-url**  string | no description |
| **name**  string | no description |
| **os-check**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **os-check-list**  dictionary | no description |
| **action**  string | no description  Choices:   - `"allow"` - `"check-up-to-date"` - `"deny"` |
| **latest-patch-level**  string | no description |
| **name**  string | no description |
| **tolerance**  integer | no description |
| **prefer-ipv6-dns**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **redir-url**  string | no description |
| **rewrite-ip-uri-ui**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **save-password**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **service-restriction**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **skip-check-for-browser**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **skip-check-for-unsupported-browser**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **skip-check-for-unsupported-os**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **smb-max-version**  string | no description  Choices:   - `"smbv1"` - `"smbv2"` - `"smbv3"` |
| **smb-min-version**  string | no description  Choices:   - `"smbv1"` - `"smbv2"` - `"smbv3"` |
| **smb-ntlmv1-auth**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **smbv1**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **split-dns**  list / elements=string | no description |
| **dns-server1**  string | no description |
| **dns-server2**  string | no description |
| **domains**  string | no description |
| **id**  integer | no description |
| **ipv6-dns-server1**  string | no description |
| **ipv6-dns-server2**  string | no description |
| **split-tunneling**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **split-tunneling-routing-address**  string | no description |
| **split-tunneling-routing-negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **theme**  string | no description  Choices:   - `"gray"` - `"blue"` - `"orange"` - `"crimson"` - `"steelblue"` - `"darkgrey"` - `"green"` - `"melongene"` - `"red"` - `"mariner"` - `"neutrino"` - `"jade"` - `"graphite"` - `"dark-matter"` - `"onyx"` - `"eclipse"` |
| **transform-backward-slashes**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **tunnel-mode**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **use-sdwan**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **user-bookmark**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **user-group-bookmark**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **web-mode**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **windows-forticlient-download-url**  string | no description |
| **wins-server1**  string | no description |
| **wins-server2**  string | no description |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_vpnsslweb_portal_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_vpnsslweb_portal_module.md#id4)

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
     fmgr_vpnsslweb_portal:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        vpnsslweb_portal:
           allow-user-access:
             - web
             - ftp
             - telnet
             - smb
             - vnc
             - rdp
             - ssh
             - ping
             - citrix
             - portforward
             - sftp
           auto-connect: <value in [disable, enable]>
           bookmark-group:
             -
                 bookmarks:
                   -
                       additional-params: <value of string>
                       apptype: <value in [web, telnet, ssh, ...]>
                       description: <value of string>
                       folder: <value of string>
                       form-data:
                         -
                             name: <value of string>
                             value: <value of string>
                       host: <value of string>
                       listening-port: <value of integer>
                       load-balancing-info: <value of string>
                       logon-password: <value of string>
                       logon-user: <value of string>
                       name: <value of string>
                       port: <value of integer>
                       preconnection-blob: <value of string>
                       preconnection-id: <value of integer>
                       remote-port: <value of integer>
                       security: <value in [rdp, nla, tls, ...]>
                       server-layout: <value in [en-us-qwerty, de-de-qwertz, fr-fr-azerty, ...]>
                       show-status-window: <value in [disable, enable]>
                       sso: <value in [disable, static, auto]>
                       sso-credential: <value in [sslvpn-login, alternative]>
                       sso-credential-sent-once: <value in [disable, enable]>
                       sso-password: <value of string>
                       sso-username: <value of string>
                       url: <value of string>
                       domain: <value of string>
                       color-depth: <value in [8, 16, 32]>
                       height: <value of integer>
                       keyboard-layout: <value in [ar, da, de, ...]>
                       restricted-admin: <value in [disable, enable]>
                       send-preconnection-id: <value in [disable, enable]>
                       width: <value of integer>
                 name: <value of string>
           custom-lang: <value of string>
           customize-forticlient-download-url: <value in [disable, enable]>
           display-bookmark: <value in [disable, enable]>
           display-connection-tools: <value in [disable, enable]>
           display-history: <value in [disable, enable]>
           display-status: <value in [disable, enable]>
           dns-server1: <value of string>
           dns-server2: <value of string>
           dns-suffix: <value of string>
           exclusive-routing: <value in [disable, enable]>
           forticlient-download: <value in [disable, enable]>
           forticlient-download-method: <value in [direct, ssl-vpn]>
           heading: <value of string>
           hide-sso-credential: <value in [disable, enable]>
           host-check: <value in [none, av, fw, ...]>
           host-check-interval: <value of integer>
           host-check-policy: <value of string>
           ip-mode: <value in [range, user-group]>
           ip-pools: <value of string>
           ipv6-dns-server1: <value of string>
           ipv6-dns-server2: <value of string>
           ipv6-exclusive-routing: <value in [disable, enable]>
           ipv6-pools: <value of string>
           ipv6-service-restriction: <value in [disable, enable]>
           ipv6-split-tunneling: <value in [disable, enable]>
           ipv6-split-tunneling-routing-address: <value of string>
           ipv6-tunnel-mode: <value in [disable, enable]>
           ipv6-wins-server1: <value of string>
           ipv6-wins-server2: <value of string>
           keep-alive: <value in [disable, enable]>
           limit-user-logins: <value in [disable, enable]>
           mac-addr-action: <value in [deny, allow]>
           mac-addr-check: <value in [disable, enable]>
           mac-addr-check-rule:
             -
                 mac-addr-list: <value of string>
                 mac-addr-mask: <value of integer>
                 name: <value of string>
           macos-forticlient-download-url: <value of string>
           name: <value of string>
           os-check: <value in [disable, enable]>
           redir-url: <value of string>
           save-password: <value in [disable, enable]>
           service-restriction: <value in [disable, enable]>
           skip-check-for-unsupported-browser: <value in [disable, enable]>
           skip-check-for-unsupported-os: <value in [disable, enable]>
           smb-ntlmv1-auth: <value in [disable, enable]>
           smbv1: <value in [disable, enable]>
           split-dns:
             -
                 dns-server1: <value of string>
                 dns-server2: <value of string>
                 domains: <value of string>
                 id: <value of integer>
                 ipv6-dns-server1: <value of string>
                 ipv6-dns-server2: <value of string>
           split-tunneling: <value in [disable, enable]>
           split-tunneling-routing-address: <value of string>
           theme: <value in [gray, blue, orange, ...]>
           tunnel-mode: <value in [disable, enable]>
           user-bookmark: <value in [disable, enable]>
           user-group-bookmark: <value in [disable, enable]>
           web-mode: <value in [disable, enable]>
           windows-forticlient-download-url: <value of string>
           wins-server1: <value of string>
           wins-server2: <value of string>
           skip-check-for-browser: <value in [disable, enable]>
           smb-max-version: <value in [smbv1, smbv2, smbv3]>
           smb-min-version: <value in [smbv1, smbv2, smbv3]>
           transform-backward-slashes: <value in [disable, enable]>
           ipv6-split-tunneling-routing-negate: <value in [disable, enable]>
           split-tunneling-routing-negate: <value in [disable, enable]>
           os-check-list:
              action: <value in [allow, check-up-to-date, deny]>
              latest-patch-level: <value of string>
              name: <value of string>
              tolerance: <value of integer>
           use-sdwan: <value in [disable, enable]>
           prefer-ipv6-dns: <value in [disable, enable]>
           rewrite-ip-uri-ui: <value in [disable, enable]>
           clipboard: <value in [disable, enable]>
           default-window-height: <value of integer>
           default-window-width: <value of integer>
```

## [Return Values](fmgr_vpnsslweb_portal_module.md#id5)

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
