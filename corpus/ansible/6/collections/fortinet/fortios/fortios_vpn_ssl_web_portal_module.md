---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_vpn_ssl_web_portal module – Portal in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_vpn_ssl_web_portal_module.html
fetched_at: 2026-07-27T17:46:28+00:00
---
# fortinet.fortios.fortios_vpn_ssl_web_portal module – Portal in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/fortinet/fortios) (version 2.2.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_vpn_ssl_web_portal_module.md#ansible-collections-fortinet-fortios-fortios-vpn-ssl-web-portal-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_vpn_ssl_web_portal`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_vpn_ssl_web_portal_module.md#synopsis)
- [Requirements](fortios_vpn_ssl_web_portal_module.md#requirements)
- [Parameters](fortios_vpn_ssl_web_portal_module.md#parameters)
- [Notes](fortios_vpn_ssl_web_portal_module.md#notes)
- [Examples](fortios_vpn_ssl_web_portal_module.md#examples)
- [Return Values](fortios_vpn_ssl_web_portal_module.md#return-values)

## [Synopsis](fortios_vpn_ssl_web_portal_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify vpn_ssl_web feature and portal category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_vpn_ssl_web_portal_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_vpn_ssl_web_portal_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |
| **vpn_ssl_web_portal**  dictionary | Portal. |
| **allow_user_access**  list / elements=string | Allow user access to SSL-VPN applications.  Choices:   - `"web"` - `"ftp"` - `"smb"` - `"sftp"` - `"telnet"` - `"ssh"` - `"vnc"` - `"rdp"` - `"ping"` - `"citrix"` - `"portforward"` |
| **auto_connect**  string | Enable/disable automatic connect by client when system is up.  Choices:   - `"enable"` - `"disable"` |
| **bookmark_group**  list / elements=dictionary | Portal bookmark group. |
| **bookmarks**  list / elements=dictionary | Bookmark table. |
| **additional_params**  string | Additional parameters. |
| **apptype**  string | Application type.  Choices:   - `"ftp"` - `"rdp"` - `"sftp"` - `"smb"` - `"ssh"` - `"telnet"` - `"vnc"` - `"web"` - `"citrix"` - `"portforward"` |
| **color_depth**  string | Color depth per pixel.  Choices:   - `"32"` - `"16"` - `"8"` |
| **description**  string | Description. |
| **domain**  string | Login domain. |
| **folder**  string | Network shared file folder parameter. |
| **form_data**  list / elements=dictionary | Form data. |
| **name**  string | Name. |
| **value**  string | Value. |
| **height**  integer | Screen height (range from 0 - 65535). |
| **host**  string | Host name/IP parameter. |
| **keyboard_layout**  string | Keyboard layout.  Choices:   - `"ar-101"` - `"ar-102"` - `"ar-102-azerty"` - `"can-mul"` - `"cz"` - `"cz-qwerty"` - `"cz-pr"` - `"da"` - `"nl"` - `"de"` - `"de-ch"` - `"de-ibm"` - `"en-uk"` - `"en-uk-ext"` - `"en-us"` - `"en-us-dvorak"` - `"es"` - `"es-var"` - `"fi"` - `"fi-sami"` - `"fr"` - `"fr-apple"` - `"fr-ca"` - `"fr-ch"` - `"fr-be"` - `"hr"` - `"hu"` - `"hu-101"` - `"it"` - `"it-142"` - `"ja"` - `"ko"` - `"lt"` - `"lt-ibm"` - `"lt-std"` - `"lav-std"` - `"lav-leg"` - `"mk"` - `"mk-std"` - `"no"` - `"no-sami"` - `"pol-214"` - `"pol-pr"` - `"pt"` - `"pt-br"` - `"pt-br-abnt2"` - `"ru"` - `"ru-mne"` - `"ru-t"` - `"sl"` - `"sv"` - `"sv-sami"` - `"tuk"` - `"tur-f"` - `"tur-q"` - `"zh-sym-sg-us"` - `"zh-sym-us"` - `"zh-tr-hk"` - `"zh-tr-mo"` - `"zh-tr-us"` |
| **listening_port**  integer | Listening port (0 - 65535). |
| **load_balancing_info**  string | The load balancing information or cookie which should be provided to the connection broker. |
| **logon_password**  string | Logon password. |
| **logon_user**  string | Logon user. |
| **name**  string | Bookmark name. |
| **port**  integer | Remote port. |
| **preconnection_blob**  string | An arbitrary string which identifies the RDP source. |
| **preconnection_id**  integer | The numeric ID of the RDP source (0-4294967295). |
| **remote_port**  integer | Remote port (0 - 65535). |
| **restricted_admin**  string | Enable/disable restricted admin mode for RDP.  Choices:   - `"enable"` - `"disable"` |
| **security**  string | Security mode for RDP connection.  Choices:   - `"rdp"` - `"nla"` - `"tls"` - `"any"` |
| **send_preconnection_id**  string | Enable/disable sending of preconnection ID.  Choices:   - `"enable"` - `"disable"` |
| **server_layout**  string | Server side keyboard layout.  Choices:   - `"de-de-qwertz"` - `"en-gb-qwerty"` - `"en-us-qwerty"` - `"es-es-qwerty"` - `"fr-ca-qwerty"` - `"fr-fr-azerty"` - `"fr-ch-qwertz"` - `"it-it-qwerty"` - `"ja-jp-qwerty"` - `"pt-br-qwerty"` - `"sv-se-qwerty"` - `"tr-tr-qwerty"` - `"failsafe"` |
| **show_status_window**  string | Enable/disable showing of status window.  Choices:   - `"enable"` - `"disable"` |
| **sso**  string | Single Sign-On.  Choices:   - `"disable"` - `"static"` - `"auto"` |
| **sso_credential**  string | Single sign-on credentials.  Choices:   - `"sslvpn-login"` - `"alternative"` |
| **sso_credential_sent_once**  string | Single sign-on credentials are only sent once to remote server.  Choices:   - `"enable"` - `"disable"` |
| **sso_password**  string | SSO password. |
| **sso_username**  string | SSO user name. |
| **url**  string | URL parameter. |
| **width**  integer | Screen width (range from 0 - 65535). |
| **name**  string | Bookmark group name. |
| **clipboard**  string | Enable to support RDP/VPC clipboard functionality.  Choices:   - `"enable"` - `"disable"` |
| **custom_lang**  string | Change the web portal display language. Overrides config system global set language. You can use config system custom-language and execute system custom-language to add custom language files. Source system.custom-language.name. |
| **customize_forticlient_download_url**  string | Enable support of customized download URL for FortiClient.  Choices:   - `"enable"` - `"disable"` |
| **default_window_height**  integer | Screen height (range from 0 - 65535). |
| **default_window_width**  integer | Screen width (range from 0 - 65535). |
| **dhcp_ip_overlap**  string | Configure overlapping DHCP IP allocation assignment.  Choices:   - `"use-new"` - `"use-old"` |
| **display_bookmark**  string | Enable to display the web portal bookmark widget.  Choices:   - `"enable"` - `"disable"` |
| **display_connection_tools**  string | Enable to display the web portal connection tools widget.  Choices:   - `"enable"` - `"disable"` |
| **display_history**  string | Enable to display the web portal user login history widget.  Choices:   - `"enable"` - `"disable"` |
| **display_status**  string | Enable to display the web portal status widget.  Choices:   - `"enable"` - `"disable"` |
| **dns_server1**  string | IPv4 DNS server 1. |
| **dns_server2**  string | IPv4 DNS server 2. |
| **dns_suffix**  string | DNS suffix. |
| **exclusive_routing**  string | Enable/disable all traffic go through tunnel only.  Choices:   - `"enable"` - `"disable"` |
| **forticlient_download**  string | Enable/disable download option for FortiClient.  Choices:   - `"enable"` - `"disable"` |
| **forticlient_download_method**  string | FortiClient download method.  Choices:   - `"direct"` - `"ssl-vpn"` |
| **heading**  string | Web portal heading message. |
| **hide_sso_credential**  string | Enable to prevent SSO credential being sent to client.  Choices:   - `"enable"` - `"disable"` |
| **host_check**  string | Type of host checking performed on endpoints.  Choices:   - `"none"` - `"av"` - `"fw"` - `"av-fw"` - `"custom"` |
| **host_check_interval**  integer | Periodic host check interval. Value of 0 means disabled and host checking only happens when the endpoint connects. |
| **host_check_policy**  list / elements=dictionary | One or more policies to require the endpoint to have specific security software. |
| **name**  string | Host check software list name. Source vpn.ssl.web.host-check-software.name. |
| **ip_mode**  string | Method by which users of this SSL-VPN tunnel obtain IP addresses.  Choices:   - `"range"` - `"user-group"` - `"dhcp"` |
| **ip_pools**  list / elements=dictionary | IPv4 firewall source address objects reserved for SSL-VPN tunnel mode clients. |
| **name**  string | Address name. Source firewall.address.name firewall.addrgrp.name. |
| **ipv6_dns_server1**  string | IPv6 DNS server 1. |
| **ipv6_dns_server2**  string | IPv6 DNS server 2. |
| **ipv6_exclusive_routing**  string | Enable/disable all IPv6 traffic go through tunnel only.  Choices:   - `"enable"` - `"disable"` |
| **ipv6_pools**  list / elements=dictionary | IPv6 firewall source address objects reserved for SSL-VPN tunnel mode clients. |
| **name**  string | Address name. Source firewall.address6.name firewall.addrgrp6.name. |
| **ipv6_service_restriction**  string | Enable/disable IPv6 tunnel service restriction.  Choices:   - `"enable"` - `"disable"` |
| **ipv6_split_tunneling**  string | Enable/disable IPv6 split tunneling.  Choices:   - `"enable"` - `"disable"` |
| **ipv6_split_tunneling_routing_address**  list / elements=dictionary | IPv6 SSL-VPN tunnel mode firewall address objects that override firewall policy destination addresses to control split-tunneling access. |
| **name**  string | Address name. Source firewall.address6.name firewall.addrgrp6.name. |
| **ipv6_split_tunneling_routing_negate**  string | Enable to negate IPv6 split tunneling routing address.  Choices:   - `"enable"` - `"disable"` |
| **ipv6_tunnel_mode**  string | Enable/disable IPv6 SSL-VPN tunnel mode.  Choices:   - `"enable"` - `"disable"` |
| **ipv6_wins_server1**  string | IPv6 WINS server 1. |
| **ipv6_wins_server2**  string | IPv6 WINS server 2. |
| **keep_alive**  string | Enable/disable automatic reconnect for FortiClient connections.  Choices:   - `"enable"` - `"disable"` |
| **limit_user_logins**  string | Enable to limit each user to one SSL-VPN session at a time.  Choices:   - `"enable"` - `"disable"` |
| **mac_addr_action**  string | Client MAC address action.  Choices:   - `"allow"` - `"deny"` |
| **mac_addr_check**  string | Enable/disable MAC address host checking.  Choices:   - `"enable"` - `"disable"` |
| **mac_addr_check_rule**  list / elements=dictionary | Client MAC address check rule. |
| **mac_addr_list**  list / elements=dictionary | Client MAC address list. |
| **addr**  string | Client MAC address. |
| **mac_addr_mask**  integer | Client MAC address mask. |
| **name**  string | Client MAC address check rule name. |
| **macos_forticlient_download_url**  string | Download URL for Mac FortiClient. |
| **name**  string / required | Portal name. |
| **os_check**  string | Enable to let the FortiGate decide action based on client OS.  Choices:   - `"enable"` - `"disable"` |
| **os_check_list**  list / elements=dictionary | SSL-VPN OS checks. |
| **action**  string | OS check options.  Choices:   - `"deny"` - `"allow"` - `"check-up-to-date"` |
| **latest_patch_level**  string | Latest OS patch level. |
| **name**  string | Name. |
| **tolerance**  integer | OS patch level tolerance. |
| **prefer_ipv6_dns**  string | Prefer to query IPv6 DNS server first if enabled.  Choices:   - `"enable"` - `"disable"` |
| **redir_url**  string | Client login redirect URL. |
| **rewrite_ip_uri_ui**  string | Rewrite contents for URI contains IP and /ui/ .  Choices:   - `"enable"` - `"disable"` |
| **save_password**  string | Enable/disable FortiClient saving the user”s password.  Choices:   - `"enable"` - `"disable"` |
| **service_restriction**  string | Enable/disable tunnel service restriction.  Choices:   - `"enable"` - `"disable"` |
| **skip_check_for_browser**  string | Enable to skip host check for browser support.  Choices:   - `"enable"` - `"disable"` |
| **skip_check_for_unsupported_browser**  string | Enable to skip host check if browser does not support it.  Choices:   - `"enable"` - `"disable"` |
| **skip_check_for_unsupported_os**  string | Enable to skip host check if client OS does not support it.  Choices:   - `"enable"` - `"disable"` |
| **smb_max_version**  string | SMB maximum client protocol version.  Choices:   - `"smbv1"` - `"smbv2"` - `"smbv3"` |
| **smb_min_version**  string | SMB minimum client protocol version.  Choices:   - `"smbv1"` - `"smbv2"` - `"smbv3"` |
| **smb_ntlmv1_auth**  string | Enable support of NTLMv1 for Samba authentication.  Choices:   - `"enable"` - `"disable"` |
| **smbv1**  string | SMB version 1.  Choices:   - `"enable"` - `"disable"` |
| **split_dns**  list / elements=dictionary | Split DNS for SSL-VPN. |
| **dns_server1**  string | DNS server 1. |
| **dns_server2**  string | DNS server 2. |
| **domains**  string | Split DNS domains used for SSL-VPN clients separated by comma. |
| **id**  integer | ID. |
| **ipv6_dns_server1**  string | IPv6 DNS server 1. |
| **ipv6_dns_server2**  string | IPv6 DNS server 2. |
| **split_tunneling**  string | Enable/disable IPv4 split tunneling.  Choices:   - `"enable"` - `"disable"` |
| **split_tunneling_routing_address**  list / elements=dictionary | IPv4 SSL-VPN tunnel mode firewall address objects that override firewall policy destination addresses to control split-tunneling access. |
| **name**  string | Address name. Source firewall.address.name firewall.addrgrp.name. |
| **split_tunneling_routing_negate**  string | Enable to negate split tunneling routing address.  Choices:   - `"enable"` - `"disable"` |
| **theme**  string | Web portal color scheme.  Choices:   - `"jade"` - `"neutrino"` - `"mariner"` - `"graphite"` - `"melongene"` - `"dark-matter"` - `"onyx"` - `"eclipse"` - `"blue"` - `"green"` - `"red"` |
| **transform_backward_slashes**  string | Transform backward slashes to forward slashes in URLs.  Choices:   - `"enable"` - `"disable"` |
| **tunnel_mode**  string | Enable/disable IPv4 SSL-VPN tunnel mode.  Choices:   - `"enable"` - `"disable"` |
| **use_sdwan**  string | Use SD-WAN rules to get output interface.  Choices:   - `"enable"` - `"disable"` |
| **user_bookmark**  string | Enable to allow web portal users to create their own bookmarks.  Choices:   - `"enable"` - `"disable"` |
| **user_group_bookmark**  string | Enable to allow web portal users to create bookmarks for all users in the same user group.  Choices:   - `"enable"` - `"disable"` |
| **web_mode**  string | Enable/disable SSL-VPN web mode.  Choices:   - `"enable"` - `"disable"` |
| **windows_forticlient_download_url**  string | Download URL for Windows FortiClient. |
| **wins_server1**  string | IPv4 WINS server 1. |
| **wins_server2**  string | IPv4 WINS server 1. |

## [Notes](fortios_vpn_ssl_web_portal_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_vpn_ssl_web_portal_module.md#id5)

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
  - name: Portal.
    fortios_vpn_ssl_web_portal:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      vpn_ssl_web_portal:
        allow_user_access: "web"
        auto_connect: "enable"
        bookmark_group:
         -
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
                    name: "default_name_14"
                    value: "<your_own_value>"
                height: "768"
                host: "myhostname"
                keyboard_layout: "ar-101"
                listening_port: "0"
                load_balancing_info: "<your_own_value>"
                logon_password: "<your_own_value>"
                logon_user: "<your_own_value>"
                name: "default_name_23"
                port: "0"
                preconnection_blob: "<your_own_value>"
                preconnection_id: "2147483648"
                remote_port: "0"
                restricted_admin: "enable"
                security: "rdp"
                send_preconnection_id: "enable"
                server_layout: "de-de-qwertz"
                show_status_window: "enable"
                sso: "disable"
                sso_credential: "sslvpn-login"
                sso_credential_sent_once: "enable"
                sso_password: "<your_own_value>"
                sso_username: "<your_own_value>"
                url: "myurl.com"
                width: "1024"
            name: "default_name_40"
        clipboard: "enable"
        custom_lang: "<your_own_value> (source system.custom-language.name)"
        customize_forticlient_download_url: "enable"
        default_window_height: "768"
        default_window_width: "1024"
        dhcp_ip_overlap: "use-new"
        display_bookmark: "enable"
        display_connection_tools: "enable"
        display_history: "enable"
        display_status: "enable"
        dns_server1: "<your_own_value>"
        dns_server2: "<your_own_value>"
        dns_suffix: "<your_own_value>"
        exclusive_routing: "enable"
        forticlient_download: "enable"
        forticlient_download_method: "direct"
        heading: "<your_own_value>"
        hide_sso_credential: "enable"
        host_check: "none"
        host_check_interval: "0"
        host_check_policy:
         -
            name: "default_name_62 (source vpn.ssl.web.host-check-software.name)"
        ip_mode: "range"
        ip_pools:
         -
            name: "default_name_65 (source firewall.address.name firewall.addrgrp.name)"
        ipv6_dns_server1: "<your_own_value>"
        ipv6_dns_server2: "<your_own_value>"
        ipv6_exclusive_routing: "enable"
        ipv6_pools:
         -
            name: "default_name_70 (source firewall.address6.name firewall.addrgrp6.name)"
        ipv6_service_restriction: "enable"
        ipv6_split_tunneling: "enable"
        ipv6_split_tunneling_routing_address:
         -
            name: "default_name_74 (source firewall.address6.name firewall.addrgrp6.name)"
        ipv6_split_tunneling_routing_negate: "enable"
        ipv6_tunnel_mode: "enable"
        ipv6_wins_server1: "<your_own_value>"
        ipv6_wins_server2: "<your_own_value>"
        keep_alive: "enable"
        limit_user_logins: "enable"
        mac_addr_action: "allow"
        mac_addr_check: "enable"
        mac_addr_check_rule:
         -
            mac_addr_list:
             -
                addr: "<your_own_value>"
            mac_addr_mask: "48"
            name: "default_name_87"
        macos_forticlient_download_url: "<your_own_value>"
        name: "default_name_89"
        os_check: "enable"
        os_check_list:
         -
            action: "deny"
            latest_patch_level: "<your_own_value>"
            name: "default_name_94"
            tolerance: "0"
        prefer_ipv6_dns: "enable"
        redir_url: "<your_own_value>"
        rewrite_ip_uri_ui: "enable"
        save_password: "enable"
        service_restriction: "enable"
        skip_check_for_browser: "enable"
        skip_check_for_unsupported_browser: "enable"
        skip_check_for_unsupported_os: "enable"
        smb_max_version: "smbv1"
        smb_min_version: "smbv1"
        smb_ntlmv1_auth: "enable"
        smbv1: "enable"
        split_dns:
         -
            dns_server1: "<your_own_value>"
            dns_server2: "<your_own_value>"
            domains: "<your_own_value>"
            id:  "112"
            ipv6_dns_server1: "<your_own_value>"
            ipv6_dns_server2: "<your_own_value>"
        split_tunneling: "enable"
        split_tunneling_routing_address:
         -
            name: "default_name_117 (source firewall.address.name firewall.addrgrp.name)"
        split_tunneling_routing_negate: "enable"
        theme: "jade"
        transform_backward_slashes: "enable"
        tunnel_mode: "enable"
        use_sdwan: "enable"
        user_bookmark: "enable"
        user_group_bookmark: "enable"
        web_mode: "enable"
        windows_forticlient_download_url: "<your_own_value>"
        wins_server1: "<your_own_value>"
        wins_server2: "<your_own_value>"
```

## [Return Values](fortios_vpn_ssl_web_portal_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  Returned: always  Sample: `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  Returned: always  Sample: `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  Returned: always  Sample: `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  Returned: success  Sample: `"id"` |
| **name**  string | Name of the table used to fulfill the request  Returned: always  Sample: `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  Returned: always  Sample: `"webfilter"` |
| **revision**  string | Internal revision number  Returned: always  Sample: `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  Returned: always  Sample: `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  Returned: always  Sample: `"success"` |
| **vdom**  string | Virtual domain used  Returned: always  Sample: `"root"` |
| **version**  string | Version of the FortiGate  Returned: always  Sample: `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
[Homepage](https://www.fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
