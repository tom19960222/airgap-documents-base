---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_user_local module – Configure local users in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_user_local_module.html
fetched_at: 2026-07-27T17:46:00+00:00
---
# fortinet.fortios.fortios_user_local module – Configure local users in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_user_local_module.md#ansible-collections-fortinet-fortios-fortios-user-local-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_user_local`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_user_local_module.md#synopsis)
- [Requirements](fortios_user_local_module.md#requirements)
- [Parameters](fortios_user_local_module.md#parameters)
- [Notes](fortios_user_local_module.md#notes)
- [Examples](fortios_user_local_module.md#examples)
- [Return Values](fortios_user_local_module.md#return-values)

## [Synopsis](fortios_user_local_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify user feature and local category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_user_local_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_user_local_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **user_local**  dictionary | Configure local users. |
| **auth_concurrent_override**  string | Enable/disable overriding the policy-auth-concurrent under config system global.  Choices:   - `"enable"` - `"disable"` |
| **auth_concurrent_value**  integer | Maximum number of concurrent logins permitted from the same user. |
| **authtimeout**  integer | Time in minutes before the authentication timeout for a user is reached. |
| **email_to**  string | Two-factor recipient”s email address. |
| **fortitoken**  string | Two-factor recipient”s FortiToken serial number. Source user.fortitoken.serial-number. |
| **id**  integer | User ID. |
| **ldap_server**  string | Name of LDAP server with which the user must authenticate. Source user.ldap.name. |
| **name**  string / required | User name. |
| **passwd**  string | User”s password. |
| **passwd_policy**  string | Password policy to apply to this user, as defined in config user password-policy. Source user.password-policy.name. |
| **passwd_time**  string | Time of the last password update. |
| **ppk_identity**  string | IKEv2 Postquantum Preshared Key Identity. |
| **ppk_secret**  string | IKEv2 Postquantum Preshared Key (ASCII string or hexadecimal encoded with a leading 0x). |
| **radius_server**  string | Name of RADIUS server with which the user must authenticate. Source user.radius.name. |
| **sms_custom_server**  string | Two-factor recipient”s SMS server. Source system.sms-server.name. |
| **sms_phone**  string | Two-factor recipient”s mobile phone number. |
| **sms_server**  string | Send SMS through FortiGuard or other external server.  Choices:   - `"fortiguard"` - `"custom"` |
| **status**  string | Enable/disable allowing the local user to authenticate with the FortiGate unit.  Choices:   - `"enable"` - `"disable"` |
| **tacacs_plus_server**  string | Name of TACACS+ server with which the user must authenticate. Source user.tacacs+.name. |
| **two_factor**  string | Enable/disable two-factor authentication.  Choices:   - `"disable"` - `"fortitoken"` - `"fortitoken-cloud"` - `"email"` - `"sms"` |
| **two_factor_authentication**  string | Authentication method by FortiToken Cloud.  Choices:   - `"fortitoken"` - `"email"` - `"sms"` |
| **two_factor_notification**  string | Notification method for user activation by FortiToken Cloud.  Choices:   - `"email"` - `"sms"` |
| **type**  string | Authentication method.  Choices:   - `"password"` - `"radius"` - `"tacacs+"` - `"ldap"` |
| **username_case_sensitivity**  string | Enable/disable case sensitivity when performing username matching (uppercase and lowercase letters are treated either as distinct or equivalent).  Choices:   - `"disable"` - `"enable"` |
| **username_sensitivity**  string | Enable/disable case and accent sensitivity when performing username matching (accents are stripped and case is ignored when disabled).  Choices:   - `"disable"` - `"enable"` |
| **workstation**  string | Name of the remote user workstation, if you want to limit the user to authenticate only from a particular workstation. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_user_local_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_user_local_module.md#id5)

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
  - name: Configure local users.
    fortios_user_local:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      user_local:
        auth_concurrent_override: "enable"
        auth_concurrent_value: "0"
        authtimeout: "0"
        email_to: "<your_own_value>"
        fortitoken: "<your_own_value> (source user.fortitoken.serial-number)"
        id:  "8"
        ldap_server: "<your_own_value> (source user.ldap.name)"
        name: "default_name_10"
        passwd: "<your_own_value>"
        passwd_policy: "<your_own_value> (source user.password-policy.name)"
        passwd_time: "<your_own_value>"
        ppk_identity: "<your_own_value>"
        ppk_secret: "<your_own_value>"
        radius_server: "<your_own_value> (source user.radius.name)"
        sms_custom_server: "<your_own_value> (source system.sms-server.name)"
        sms_phone: "<your_own_value>"
        sms_server: "fortiguard"
        status: "enable"
        tacacs_plus_server: "<your_own_value> (source user.tacacs+.name)"
        two_factor: "disable"
        two_factor_authentication: "fortitoken"
        two_factor_notification: "email"
        type: "password"
        username_case_sensitivity: "disable"
        username_sensitivity: "disable"
        workstation: "<your_own_value>"
```

## [Return Values](fortios_user_local_module.md#id6)

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
