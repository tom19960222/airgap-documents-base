---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_system_admin module – Configure admin users in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_system_admin_module.html
fetched_at: 2026-07-27T17:44:04+00:00
---
# fortinet.fortios.fortios_system_admin module – Configure admin users in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_admin_module.md#ansible-collections-fortinet-fortios-fortios-system-admin-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_admin`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_admin_module.md#synopsis)
- [Requirements](fortios_system_admin_module.md#requirements)
- [Parameters](fortios_system_admin_module.md#parameters)
- [Notes](fortios_system_admin_module.md#notes)
- [Examples](fortios_system_admin_module.md#examples)
- [Return Values](fortios_system_admin_module.md#return-values)

## [Synopsis](fortios_system_admin_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and admin category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_admin_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_system_admin_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **system_admin**  dictionary | Configure admin users. |
| **accprofile**  string | Access profile for this administrator. Access profiles control administrator access to FortiGate features. Source system.accprofile.name. |
| **accprofile_override**  string | Enable to use the name of an access profile provided by the remote authentication server to control the FortiGate features that this administrator can access.  Choices:   - `"enable"` - `"disable"` |
| **allow_remove_admin_session**  string | Enable/disable allow admin session to be removed by privileged admin users.  Choices:   - `"enable"` - `"disable"` |
| **comments**  string | Comment. |
| **email_to**  string | This administrator”s email address. |
| **force_password_change**  string | Enable/disable force password change on next login.  Choices:   - `"enable"` - `"disable"` |
| **fortitoken**  string | This administrator”s FortiToken serial number. |
| **guest_auth**  string | Enable/disable guest authentication.  Choices:   - `"disable"` - `"enable"` |
| **guest_lang**  string | Guest management portal language. Source system.custom-language.name. |
| **guest_usergroups**  list / elements=dictionary | Select guest user groups. |
| **name**  string | Select guest user groups. |
| **gui_dashboard**  list / elements=dictionary | GUI dashboards. |
| **columns**  integer | Number of columns. |
| **id**  integer | Dashboard ID. |
| **layout_type**  string | Layout type.  Choices:   - `"responsive"` - `"fixed"` |
| **name**  string | Dashboard name. |
| **permanent**  string | Permanent dashboard (can”t be removed via the GUI).  Choices:   - `"disable"` - `"enable"` |
| **scope**  string | Dashboard scope.  Choices:   - `"global"` - `"vdom"` |
| **vdom**  string | Virtual domain. Source system.vdom.name. |
| **widget**  list / elements=dictionary | Dashboard widgets. |
| **fabric_device**  string | Fabric device to monitor. |
| **fabric_device_widget_name**  string | Fabric device widget name. |
| **fabric_device_widget_visualization_type**  string | Visualization type for fabric device widget. |
| **fortiview_device**  string | FortiView device. |
| **fortiview_filters**  list / elements=dictionary | FortiView filters. |
| **id**  integer | FortiView Filter ID. |
| **key**  string | Filter key. |
| **value**  string | Filter value. |
| **fortiview_sort_by**  string | FortiView sort by. |
| **fortiview_timeframe**  string | FortiView timeframe. |
| **fortiview_type**  string | FortiView type. |
| **fortiview_visualization**  string | FortiView visualization. |
| **height**  integer | Height. |
| **id**  integer | Widget ID. |
| **industry**  string | Security Audit Rating industry.  Choices:   - `"default"` - `"custom"` |
| **interface**  string | Interface to monitor. Source system.interface.name. |
| **region**  string | Security Audit Rating region.  Choices:   - `"default"` - `"custom"` |
| **title**  string | Widget title. |
| **type**  string | Widget type.  Choices:   - `"sysinfo"` - `"licinfo"` - `"forticloud"` - `"cpu-usage"` - `"memory-usage"` - `"disk-usage"` - `"log-rate"` - `"sessions"` - `"session-rate"` - `"tr-history"` - `"analytics"` - `"usb-modem"` - `"admins"` - `"security-fabric"` - `"security-fabric-ranking"` - `"sensor-info"` - `"ha-status"` - `"vulnerability-summary"` - `"host-scan-summary"` - `"fortiview"` - `"botnet-activity"` - `"fabric-device"` - `"fortimail"` |
| **width**  integer | Width. |
| **x_pos**  integer | X position. |
| **y_pos**  integer | Y position. |
| **gui_global_menu_favorites**  list / elements=dictionary | Favorite GUI menu IDs for the global VDOM. |
| **id**  string | Select menu ID. |
| **gui_new_feature_acknowledge**  list / elements=dictionary | Acknowledgement of new features. |
| **id**  string | Select menu ID. |
| **gui_vdom_menu_favorites**  list / elements=dictionary | Favorite GUI menu IDs for VDOMs. |
| **id**  string | Select menu ID. |
| **hidden**  integer | Admin user hidden attribute. |
| **history0**  string | history0 |
| **history1**  string | history1 |
| **ip6_trusthost1**  string | Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address. |
| **ip6_trusthost10**  string | Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address. |
| **ip6_trusthost2**  string | Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address. |
| **ip6_trusthost3**  string | Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address. |
| **ip6_trusthost4**  string | Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address. |
| **ip6_trusthost5**  string | Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address. |
| **ip6_trusthost6**  string | Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address. |
| **ip6_trusthost7**  string | Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address. |
| **ip6_trusthost8**  string | Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address. |
| **ip6_trusthost9**  string | Any IPv6 address from which the administrator can connect to the FortiGate unit. Default allows access from any IPv6 address. |
| **login_time**  list / elements=dictionary | Record user login time. |
| **last_failed_login**  string | Last failed login time. |
| **last_login**  string | Last successful login time. |
| **usr_name**  string | User name. |
| **name**  string / required | User name. |
| **password**  string | Admin user password. |
| **password_expire**  string | Password expire time. |
| **peer_auth**  string | Set to enable peer certificate authentication (for HTTPS admin access).  Choices:   - `"enable"` - `"disable"` |
| **peer_group**  string | Name of peer group defined under config user group which has PKI members. Used for peer certificate authentication (for HTTPS admin access). |
| **radius_vdom_override**  string | Enable to use the names of VDOMs provided by the remote authentication server to control the VDOMs that this administrator can access.  Choices:   - `"enable"` - `"disable"` |
| **remote_auth**  string | Enable/disable authentication using a remote RADIUS, LDAP, or TACACS+ server.  Choices:   - `"enable"` - `"disable"` |
| **remote_group**  string | User group name used for remote auth. |
| **schedule**  string | Firewall schedule used to restrict when the administrator can log in. No schedule means no restrictions. |
| **sms_custom_server**  string | Custom SMS server to send SMS messages to. Source system.sms-server.name. |
| **sms_phone**  string | Phone number on which the administrator receives SMS messages. |
| **sms_server**  string | Send SMS messages using the FortiGuard SMS server or a custom server.  Choices:   - `"fortiguard"` - `"custom"` |
| **ssh_certificate**  string | Select the certificate to be used by the FortiGate for authentication with an SSH client. Source certificate.remote.name. |
| **ssh_public_key1**  string | Public key of an SSH client. The client is authenticated without being asked for credentials. Create the public-private key pair in the SSH client application. |
| **ssh_public_key2**  string | Public key of an SSH client. The client is authenticated without being asked for credentials. Create the public-private key pair in the SSH client application. |
| **ssh_public_key3**  string | Public key of an SSH client. The client is authenticated without being asked for credentials. Create the public-private key pair in the SSH client application. |
| **trusthost1**  string | Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address. |
| **trusthost10**  string | Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address. |
| **trusthost2**  string | Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address. |
| **trusthost3**  string | Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address. |
| **trusthost4**  string | Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address. |
| **trusthost5**  string | Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address. |
| **trusthost6**  string | Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address. |
| **trusthost7**  string | Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address. |
| **trusthost8**  string | Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address. |
| **trusthost9**  string | Any IPv4 address or subnet address and netmask from which the administrator can connect to the FortiGate unit. Default allows access from any IPv4 address. |
| **two_factor**  string | Enable/disable two-factor authentication.  Choices:   - `"disable"` - `"fortitoken"` - `"fortitoken-cloud"` - `"email"` - `"sms"` |
| **two_factor_authentication**  string | Authentication method by FortiToken Cloud.  Choices:   - `"fortitoken"` - `"email"` - `"sms"` |
| **two_factor_notification**  string | Notification method for user activation by FortiToken Cloud.  Choices:   - `"email"` - `"sms"` |
| **vdom**  list / elements=dictionary | Virtual domain(s) that the administrator can access. |
| **name**  string | Virtual domain name. Source system.vdom.name. |
| **vdom_override**  string | Enable to use the names of VDOMs provided by the remote authentication server to control the VDOMs that this administrator can access.  Choices:   - `"enable"` - `"disable"` |
| **wildcard**  string | Enable/disable wildcard RADIUS authentication.  Choices:   - `"enable"` - `"disable"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_system_admin_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_admin_module.md#id5)

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
  - name: Configure admin users.
    fortios_system_admin:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_admin:
        accprofile: "<your_own_value> (source system.accprofile.name)"
        accprofile_override: "enable"
        allow_remove_admin_session: "enable"
        comments: "<your_own_value>"
        email_to: "<your_own_value>"
        force_password_change: "enable"
        fortitoken: "<your_own_value>"
        guest_auth: "disable"
        guest_lang: "<your_own_value> (source system.custom-language.name)"
        guest_usergroups:
         -
            name: "default_name_13"
        gui_dashboard:
         -
            columns: "10"
            id:  "16"
            layout_type: "responsive"
            name: "default_name_18"
            permanent: "disable"
            scope: "global"
            vdom: "<your_own_value> (source system.vdom.name)"
            widget:
             -
                fabric_device: "<your_own_value>"
                fabric_device_widget_name: "<your_own_value>"
                fabric_device_widget_visualization_type: "<your_own_value>"
                fortiview_device: "<your_own_value>"
                fortiview_filters:
                 -
                    id:  "28"
                    key: "<your_own_value>"
                    value: "<your_own_value>"
                fortiview_sort_by: "<your_own_value>"
                fortiview_timeframe: "<your_own_value>"
                fortiview_type: "<your_own_value>"
                fortiview_visualization: "<your_own_value>"
                height: "25"
                id:  "36"
                industry: "default"
                interface: "<your_own_value> (source system.interface.name)"
                region: "default"
                title: "<your_own_value>"
                type: "sysinfo"
                width: "25"
                x_pos: "500"
                y_pos: "500"
        gui_global_menu_favorites:
         -
            id:  "46"
        gui_new_feature_acknowledge:
         -
            id:  "48"
        gui_vdom_menu_favorites:
         -
            id:  "50"
        hidden: "127"
        history0: "<your_own_value>"
        history1: "<your_own_value>"
        ip6_trusthost1: "myhostname"
        ip6_trusthost10: "myhostname"
        ip6_trusthost2: "myhostname"
        ip6_trusthost3: "myhostname"
        ip6_trusthost4: "myhostname"
        ip6_trusthost5: "myhostname"
        ip6_trusthost6: "myhostname"
        ip6_trusthost7: "myhostname"
        ip6_trusthost8: "myhostname"
        ip6_trusthost9: "myhostname"
        login_time:
         -
            last_failed_login: "<your_own_value>"
            last_login: "<your_own_value>"
            usr_name: "<your_own_value>"
        name: "default_name_68"
        password: "<your_own_value>"
        password_expire: "<your_own_value>"
        peer_auth: "enable"
        peer_group: "<your_own_value>"
        radius_vdom_override: "enable"
        remote_auth: "enable"
        remote_group: "<your_own_value>"
        schedule: "<your_own_value>"
        sms_custom_server: "<your_own_value> (source system.sms-server.name)"
        sms_phone: "<your_own_value>"
        sms_server: "fortiguard"
        ssh_certificate: "<your_own_value> (source certificate.remote.name)"
        ssh_public_key1: "<your_own_value>"
        ssh_public_key2: "<your_own_value>"
        ssh_public_key3: "<your_own_value>"
        trusthost1: "myhostname"
        trusthost10: "myhostname"
        trusthost2: "myhostname"
        trusthost3: "myhostname"
        trusthost4: "myhostname"
        trusthost5: "myhostname"
        trusthost6: "myhostname"
        trusthost7: "myhostname"
        trusthost8: "myhostname"
        trusthost9: "myhostname"
        two_factor: "disable"
        two_factor_authentication: "fortitoken"
        two_factor_notification: "email"
        vdom:
         -
            name: "default_name_98 (source system.vdom.name)"
        vdom_override: "enable"
        wildcard: "enable"
```

## [Return Values](fortios_system_admin_module.md#id6)

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
