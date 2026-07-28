---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_vpnsslweb_portal module – Portal."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_vpnsslweb_portal_module.html
fetched_at: 2026-07-28T02:21:49+00:00
---
# fortinet.fortimanager.fmgr_vpnsslweb_portal module – Portal.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_vpnsslweb_portal`.

New in fortinet.fortimanager 2.0.0

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
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **vpnsslweb_portal**  dictionary | the top level parameters set |
| **allow-user-access**  list / elements=string | Allow user access to SSL-VPN applications.  **Choices:**   - `"web"` - `"ftp"` - `"telnet"` - `"smb"` - `"vnc"` - `"rdp"` - `"ssh"` - `"ping"` - `"citrix"` - `"portforward"` - `"sftp"` |
| **auto-connect**  string | Enable/disable automatic connect by client when system is up.  **Choices:**   - `"disable"` - `"enable"` |
| **bookmark-group**  list / elements=dictionary | Bookmark-Group. |
| **bookmarks**  list / elements=dictionary | Bookmarks. |
| **additional-params**  string | Additional parameters. |
| **apptype**  string | Application type.  **Choices:**   - `"web"` - `"telnet"` - `"ssh"` - `"ftp"` - `"smb"` - `"vnc"` - `"rdp"` - `"citrix"` - `"rdpnative"` - `"portforward"` - `"sftp"` |
| **color-depth**  string | Color depth per pixel.  **Choices:**   - `"8"` - `"16"` - `"32"` |
| **description**  string | Description. |
| **domain**  string | Login domain. |
| **folder**  string | Network shared file folder parameter. |
| **form-data**  list / elements=dictionary | Form-Data. |
| **name**  string | Name. |
| **value**  string | Value. |
| **height**  integer | Screen height |
| **host**  string | Host name/IP parameter. |
| **keyboard-layout**  string | Keyboard layout.  **Choices:**   - `"ar"` - `"da"` - `"de"` - `"de-ch"` - `"en-gb"` - `"en-uk"` - `"en-us"` - `"es"` - `"fi"` - `"fr"` - `"fr-be"` - `"fr-ca"` - `"fr-ch"` - `"hr"` - `"hu"` - `"it"` - `"ja"` - `"lt"` - `"lv"` - `"mk"` - `"no"` - `"pl"` - `"pt"` - `"pt-br"` - `"ru"` - `"sl"` - `"sv"` - `"tk"` - `"tr"` - `"fr-ca-m"` - `"wg"` - `"ar-101"` - `"ar-102"` - `"ar-102-azerty"` - `"can-mul"` - `"cz"` - `"cz-qwerty"` - `"cz-pr"` - `"nl"` - `"de-ibm"` - `"en-uk-ext"` - `"en-us-dvorak"` - `"es-var"` - `"fi-sami"` - `"hu-101"` - `"it-142"` - `"ko"` - `"lt-ibm"` - `"lt-std"` - `"lav-std"` - `"lav-leg"` - `"mk-std"` - `"no-sami"` - `"pol-214"` - `"pol-pr"` - `"pt-br-abnt2"` - `"ru-mne"` - `"ru-t"` - `"sv-sami"` - `"tuk"` - `"tur-f"` - `"tur-q"` - `"zh-sym-sg-us"` - `"zh-sym-us"` - `"zh-tr-hk"` - `"zh-tr-mo"` - `"zh-tr-us"` - `"fr-apple"` - `"la-am"` |
| **listening-port**  integer | Listening port |
| **load-balancing-info**  string | The load balancing information or cookie which should be provided to the connection broker. |
| **logon-password**  any | (list) Logon password. |
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
| **sso-password**  any | (list) SSO password. |
| **sso-username**  string | SSO user name. |
| **url**  string | URL parameter. |
| **vnc-keyboard-layout**  string | Keyboard layout.  **Choices:**   - `"da"` - `"de"` - `"de-ch"` - `"en-uk"` - `"es"` - `"fi"` - `"fr"` - `"fr-be"` - `"it"` - `"no"` - `"pt"` - `"sv"` - `"nl"` - `"en-uk-ext"` - `"it-142"` - `"pt-br-abnt2"` - `"default"` - `"fr-ca-mul"` - `"gd"` - `"us-intl"` |
| **width**  integer | Screen width |
| **name**  string | Bookmark group name. |
| **client-src-range**  string | Allow client to add source range for the tunnel traffic.  **Choices:**   - `"disable"` - `"enable"` |
| **clipboard**  string | Enable to support RDP/VPC clipboard functionality.  **Choices:**   - `"disable"` - `"enable"` |
| **custom-lang**  string | Change the web portal display language. |
| **customize-forticlient-download-url**  string | Enable support of customized download URL for FortiClient.  **Choices:**   - `"disable"` - `"enable"` |
| **default-protocol**  string | Application type that is set by default.  **Choices:**   - `"web"` - `"ftp"` - `"telnet"` - `"smb"` - `"vnc"` - `"rdp"` - `"ssh"` - `"sftp"` |
| **default-window-height**  integer | Screen height |
| **default-window-width**  integer | Screen width |
| **dhcp-ip-overlap**  string | Configure overlapping DHCP IP allocation assignment.  **Choices:**   - `"use-old"` - `"use-new"` |
| **dhcp-ra-giaddr**  string | Relay agent gateway IP address to use in the giaddr field of DHCP requests. |
| **dhcp6-ra-linkaddr**  string | Relay agent IPv6 link address to use in DHCP6 requests. |
| **display-bookmark**  string | Enable to display the web portal bookmark widget.  **Choices:**   - `"disable"` - `"enable"` |
| **display-connection-tools**  string | Enable to display the web portal connection tools widget.  **Choices:**   - `"disable"` - `"enable"` |
| **display-history**  string | Enable to display the web portal user login history widget.  **Choices:**   - `"disable"` - `"enable"` |
| **display-status**  string | Enable to display the web portal status widget.  **Choices:**   - `"disable"` - `"enable"` |
| **dns-server1**  string | IPv4 DNS server 1. |
| **dns-server2**  string | IPv4 DNS server 2. |
| **dns-suffix**  string | DNS suffix. |
| **exclusive-routing**  string | Enable/disable all traffic go through tunnel only.  **Choices:**   - `"disable"` - `"enable"` |
| **focus-bookmark**  string | Enable to prioritize the placement of the bookmark section over the quick-connection section in the SSL-VPN application.  **Choices:**   - `"disable"` - `"enable"` |
| **forticlient-download**  string | Enable/disable download option for FortiClient.  **Choices:**   - `"disable"` - `"enable"` |
| **forticlient-download-method**  string | FortiClient download method.  **Choices:**   - `"direct"` - `"ssl-vpn"` |
| **heading**  string | Web portal heading message. |
| **hide-sso-credential**  string | Enable to prevent SSO credential being sent to client.  **Choices:**   - `"disable"` - `"enable"` |
| **host-check**  string | Type of host checking performed on endpoints.  **Choices:**   - `"none"` - `"av"` - `"fw"` - `"av-fw"` - `"custom"` |
| **host-check-interval**  integer | Periodic host check interval. |
| **host-check-policy**  any | (list or str) One or more policies to require the endpoint to have specific security software. |
| **ip-mode**  string | Method by which users of this SSL-VPN tunnel obtain IP addresses.  **Choices:**   - `"range"` - `"user-group"` - `"dhcp"` - `"no-ip"` |
| **ip-pools**  any | (list or str) IPv4 firewall source address objects reserved for SSL-VPN tunnel mode clients. |
| **ipv6-dns-server1**  string | IPv6 DNS server 1. |
| **ipv6-dns-server2**  string | IPv6 DNS server 2. |
| **ipv6-exclusive-routing**  string | Enable/disable all IPv6 traffic go through tunnel only.  **Choices:**   - `"disable"` - `"enable"` |
| **ipv6-pools**  any | (list or str) IPv4 firewall source address objects reserved for SSL-VPN tunnel mode clients. |
| **ipv6-service-restriction**  string | Enable/disable IPv6 tunnel service restriction.  **Choices:**   - `"disable"` - `"enable"` |
| **ipv6-split-tunneling**  string | Enable/disable IPv6 split tunneling.  **Choices:**   - `"disable"` - `"enable"` |
| **ipv6-split-tunneling-routing-address**  any | (list or str) IPv6 SSL-VPN tunnel mode firewall address objects that override firewall policy destination addresses to control … |
| **ipv6-split-tunneling-routing-negate**  string | Enable to negate IPv6 split tunneling routing address.  **Choices:**   - `"disable"` - `"enable"` |
| **ipv6-tunnel-mode**  string | Enable/disable IPv6 SSL-VPN tunnel mode.  **Choices:**   - `"disable"` - `"enable"` |
| **ipv6-wins-server1**  string | IPv6 WINS server 1. |
| **ipv6-wins-server2**  string | IPv6 WINS server 2. |
| **keep-alive**  string | Enable/disable automatic reconnect for FortiClient connections.  **Choices:**   - `"disable"` - `"enable"` |
| **landing-page**  dictionary | no description |
| **form-data**  list / elements=dictionary | no description |
| **name**  string | Name. |
| **value**  string | Value. |
| **logout-url**  string | Landing page log out URL. |
| **sso**  string | Single sign-on.  **Choices:**   - `"disable"` - `"static"` - `"auto"` |
| **sso-credential**  string | Single sign-on credentials.  **Choices:**   - `"sslvpn-login"` - `"alternative"` |
| **sso-password**  any | (list) no description |
| **sso-username**  string | SSO user name. |
| **url**  string | Landing page URL. |
| **landing-page-mode**  string | Enable/disable SSL-VPN landing page mode.  **Choices:**   - `"disable"` - `"enable"` |
| **limit-user-logins**  string | Enable to limit each user to one SSL-VPN session at a time.  **Choices:**   - `"disable"` - `"enable"` |
| **mac-addr-action**  string | Client MAC address action.  **Choices:**   - `"deny"` - `"allow"` |
| **mac-addr-check**  string | Enable/disable MAC address host checking.  **Choices:**   - `"disable"` - `"enable"` |
| **mac-addr-check-rule**  list / elements=dictionary | Mac-Addr-Check-Rule. |
| **mac-addr-list**  any | (list) Client MAC address list. |
| **mac-addr-mask**  integer | Client MAC address mask. |
| **name**  string | Client MAC address check rule name. |
| **macos-forticlient-download-url**  string | Download URL for Mac FortiClient. |
| **name**  string / required | Portal name. |
| **os-check**  string | Enable to let the FortiGate decide action based on client OS.  **Choices:**   - `"disable"` - `"enable"` |
| **os-check-list**  dictionary | no description |
| **action**  string | OS check options.  **Choices:**   - `"allow"` - `"check-up-to-date"` - `"deny"` |
| **latest-patch-level**  string | Latest OS patch level. |
| **name**  string | Name. |
| **tolerance**  integer | OS patch level tolerance. |
| **prefer-ipv6-dns**  string | prefer to query IPv6 dns first if enabled.  **Choices:**   - `"disable"` - `"enable"` |
| **redir-url**  string | Client login redirect URL. |
| **rewrite-ip-uri-ui**  string | Rewrite contents for URI contains IP and /ui/.  **Choices:**   - `"disable"` - `"enable"` |
| **save-password**  string | Enable/disable FortiClient saving the users password.  **Choices:**   - `"disable"` - `"enable"` |
| **service-restriction**  string | Enable/disable tunnel service restriction.  **Choices:**   - `"disable"` - `"enable"` |
| **skip-check-for-browser**  string | Enable to skip host check for browser support.  **Choices:**   - `"disable"` - `"enable"` |
| **skip-check-for-unsupported-browser**  string | Enable to skip host check if browser does not support it.  **Choices:**   - `"disable"` - `"enable"` |
| **skip-check-for-unsupported-os**  string | Enable to skip host check if client OS does not support it.  **Choices:**   - `"disable"` - `"enable"` |
| **smb-max-version**  string | SMB maximum client protocol version.  **Choices:**   - `"smbv1"` - `"smbv2"` - `"smbv3"` |
| **smb-min-version**  string | SMB minimum client protocol version.  **Choices:**   - `"smbv1"` - `"smbv2"` - `"smbv3"` |
| **smb-ntlmv1-auth**  string | Enable support of NTLMv1 for Samba authentication.  **Choices:**   - `"disable"` - `"enable"` |
| **smbv1**  string | Enable/disable support of SMBv1 for Samba.  **Choices:**   - `"disable"` - `"enable"` |
| **split-dns**  list / elements=dictionary | Split-Dns. |
| **dns-server1**  string | DNS server 1. |
| **dns-server2**  string | DNS server 2. |
| **domains**  string | Split DNS domains used for SSL-VPN clients separated by comma |
| **id**  integer | ID. |
| **ipv6-dns-server1**  string | IPv6 DNS server 1. |
| **ipv6-dns-server2**  string | IPv6 DNS server 2. |
| **split-tunneling**  string | Enable/disable IPv4 split tunneling.  **Choices:**   - `"disable"` - `"enable"` |
| **split-tunneling-routing-address**  any | (list or str) IPv4 SSL-VPN tunnel mode firewall address objects that override firewall policy destination addresses to control … |
| **split-tunneling-routing-negate**  string | Enable to negate split tunneling routing address.  **Choices:**   - `"disable"` - `"enable"` |
| **theme**  string | Web portal color scheme.  **Choices:**   - `"gray"` - `"blue"` - `"orange"` - `"crimson"` - `"steelblue"` - `"darkgrey"` - `"green"` - `"melongene"` - `"red"` - `"mariner"` - `"neutrino"` - `"jade"` - `"graphite"` - `"dark-matter"` - `"onyx"` - `"eclipse"` - `"jet-stream"` - `"security-fabric"` |
| **transform-backward-slashes**  string | Transform backward slashes to forward slashes in URLs.  **Choices:**   - `"disable"` - `"enable"` |
| **tunnel-mode**  string | Enable/disable IPv4 SSL-VPN tunnel mode.  **Choices:**   - `"disable"` - `"enable"` |
| **use-sdwan**  string | Use SD-WAN rules to get output interface.  **Choices:**   - `"disable"` - `"enable"` |
| **user-bookmark**  string | Enable to allow web portal users to create their own bookmarks.  **Choices:**   - `"disable"` - `"enable"` |
| **user-group-bookmark**  string | Enable to allow web portal users to create bookmarks for all users in the same user group.  **Choices:**   - `"disable"` - `"enable"` |
| **virtual-desktop**  string | Enable/disable SSL VPN virtual desktop.  **Choices:**   - `"disable"` - `"enable"` |
| **virtual-desktop-app-list**  string | Virtual desktop application list. |
| **virtual-desktop-clipboard-share**  string | Enable/disable sharing of clipboard in virtual desktop.  **Choices:**   - `"disable"` - `"enable"` |
| **virtual-desktop-desktop-switch**  string | Enable/disable switch to virtual desktop.  **Choices:**   - `"disable"` - `"enable"` |
| **virtual-desktop-logout-when-browser-close**  string | Enable/disable logout when browser is close in virtual desktop.  **Choices:**   - `"disable"` - `"enable"` |
| **virtual-desktop-network-share-access**  string | Enable/disable network share access in virtual desktop.  **Choices:**   - `"disable"` - `"enable"` |
| **virtual-desktop-printing**  string | Enable/disable printing in virtual desktop.  **Choices:**   - `"disable"` - `"enable"` |
| **virtual-desktop-removable-media-access**  string | Enable/disable access to removable media in virtual desktop.  **Choices:**   - `"disable"` - `"enable"` |
| **web-mode**  string | Enable/disable SSL VPN web mode.  **Choices:**   - `"disable"` - `"enable"` |
| **windows-forticlient-download-url**  string | Download URL for Windows FortiClient. |
| **wins-server1**  string | IPv4 WINS server 1. |
| **wins-server2**  string | IPv4 WINS server 1. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

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
    - name: Portal.
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
          custom-lang: <string>
          customize-forticlient-download-url: <value in [disable, enable]>
          display-bookmark: <value in [disable, enable]>
          display-connection-tools: <value in [disable, enable]>
          display-history: <value in [disable, enable]>
          display-status: <value in [disable, enable]>
          dns-server1: <string>
          dns-server2: <string>
          dns-suffix: <string>
          exclusive-routing: <value in [disable, enable]>
          forticlient-download: <value in [disable, enable]>
          forticlient-download-method: <value in [direct, ssl-vpn]>
          heading: <string>
          hide-sso-credential: <value in [disable, enable]>
          host-check: <value in [none, av, fw, ...]>
          host-check-interval: <integer>
          host-check-policy: <list or string>
          ip-mode: <value in [range, user-group, dhcp, ...]>
          ip-pools: <list or string>
          ipv6-dns-server1: <string>
          ipv6-dns-server2: <string>
          ipv6-exclusive-routing: <value in [disable, enable]>
          ipv6-pools: <list or string>
          ipv6-service-restriction: <value in [disable, enable]>
          ipv6-split-tunneling: <value in [disable, enable]>
          ipv6-split-tunneling-routing-address: <list or string>
          ipv6-tunnel-mode: <value in [disable, enable]>
          ipv6-wins-server1: <string>
          ipv6-wins-server2: <string>
          keep-alive: <value in [disable, enable]>
          limit-user-logins: <value in [disable, enable]>
          mac-addr-action: <value in [deny, allow]>
          mac-addr-check: <value in [disable, enable]>
          mac-addr-check-rule:
            -
              mac-addr-list: <list or string>
              mac-addr-mask: <integer>
              name: <string>
          macos-forticlient-download-url: <string>
          name: <string>
          os-check: <value in [disable, enable]>
          redir-url: <string>
          save-password: <value in [disable, enable]>
          service-restriction: <value in [disable, enable]>
          skip-check-for-unsupported-browser: <value in [disable, enable]>
          skip-check-for-unsupported-os: <value in [disable, enable]>
          smb-ntlmv1-auth: <value in [disable, enable]>
          smbv1: <value in [disable, enable]>
          split-dns:
            -
              dns-server1: <string>
              dns-server2: <string>
              domains: <string>
              id: <integer>
              ipv6-dns-server1: <string>
              ipv6-dns-server2: <string>
          split-tunneling: <value in [disable, enable]>
          split-tunneling-routing-address: <list or string>
          theme: <value in [gray, blue, orange, ...]>
          tunnel-mode: <value in [disable, enable]>
          user-bookmark: <value in [disable, enable]>
          user-group-bookmark: <value in [disable, enable]>
          web-mode: <value in [disable, enable]>
          windows-forticlient-download-url: <string>
          wins-server1: <string>
          wins-server2: <string>
          skip-check-for-browser: <value in [disable, enable]>
          smb-max-version: <value in [smbv1, smbv2, smbv3]>
          smb-min-version: <value in [smbv1, smbv2, smbv3]>
          virtual-desktop-logout-when-browser-close: <value in [disable, enable]>
          virtual-desktop-clipboard-share: <value in [disable, enable]>
          virtual-desktop-desktop-switch: <value in [disable, enable]>
          virtual-desktop: <value in [disable, enable]>
          virtual-desktop-network-share-access: <value in [disable, enable]>
          virtual-desktop-printing: <value in [disable, enable]>
          virtual-desktop-app-list: <string>
          virtual-desktop-removable-media-access: <value in [disable, enable]>
          transform-backward-slashes: <value in [disable, enable]>
          ipv6-split-tunneling-routing-negate: <value in [disable, enable]>
          split-tunneling-routing-negate: <value in [disable, enable]>
          os-check-list:
            action: <value in [allow, check-up-to-date, deny]>
            latest-patch-level: <string>
            name: <string>
            tolerance: <integer>
          use-sdwan: <value in [disable, enable]>
          prefer-ipv6-dns: <value in [disable, enable]>
          rewrite-ip-uri-ui: <value in [disable, enable]>
          clipboard: <value in [disable, enable]>
          default-window-height: <integer>
          default-window-width: <integer>
          dhcp-ip-overlap: <value in [use-old, use-new]>
          client-src-range: <value in [disable, enable]>
          dhcp-ra-giaddr: <string>
          dhcp6-ra-linkaddr: <string>
          landing-page:
            form-data:
              -
                name: <string>
                value: <string>
            logout-url: <string>
            sso: <value in [disable, static, auto]>
            sso-credential: <value in [sslvpn-login, alternative]>
            sso-password: <list or string>
            sso-username: <string>
            url: <string>
          landing-page-mode: <value in [disable, enable]>
          default-protocol: <value in [web, ftp, telnet, ...]>
          focus-bookmark: <value in [disable, enable]>
```

## [Return Values](fmgr_vpnsslweb_portal_module.md#id5)

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
