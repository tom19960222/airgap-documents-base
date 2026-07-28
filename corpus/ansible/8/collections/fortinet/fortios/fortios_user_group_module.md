---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_user_group module – Configure user groups in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_user_group_module.html
fetched_at: 2026-07-28T02:29:55+00:00
---
# fortinet.fortios.fortios_user_group module – Configure user groups in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_user_group_module.md#ansible-collections-fortinet-fortios-fortios-user-group-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_user_group`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_user_group_module.md#synopsis)
- [Requirements](fortios_user_group_module.md#requirements)
- [Parameters](fortios_user_group_module.md#parameters)
- [Notes](fortios_user_group_module.md#notes)
- [Examples](fortios_user_group_module.md#examples)
- [Return Values](fortios_user_group_module.md#return-values)

## [Synopsis](fortios_user_group_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify user feature and group category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_user_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_user_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **user_group**  dictionary | Configure user groups. |
| **auth_concurrent_override**  string | Enable/disable overriding the global number of concurrent authentication sessions for this user group.  **Choices:**   - `"enable"` - `"disable"` |
| **auth_concurrent_value**  integer | Maximum number of concurrent authenticated connections per user (0 - 100). |
| **authtimeout**  integer | Authentication timeout in minutes for this user group. 0 to use the global user setting auth-timeout. |
| **company**  string | Set the action for the company guest user field.  **Choices:**   - `"optional"` - `"mandatory"` - `"disabled"` |
| **email**  string | Enable/disable the guest user email address field.  **Choices:**   - `"disable"` - `"enable"` |
| **expire**  integer | Time in seconds before guest user accounts expire (1 - 31536000). |
| **expire_type**  string | Determine when the expiration countdown begins.  **Choices:**   - `"immediately"` - `"first-successful-login"` |
| **group_type**  string | Set the group to be for firewall authentication, FSSO, RSSO, or guest users.  **Choices:**   - `"firewall"` - `"fsso-service"` - `"rsso"` - `"guest"` |
| **guest**  list / elements=dictionary | Guest User. |
| **comment**  string | Comment. |
| **company**  string | Set the action for the company guest user field. |
| **email**  string | Email. |
| **expiration**  string | Expire time. |
| **id**  integer / required | Guest ID. see <a href=’#notes’>Notes</a>. |
| **mobile_phone**  string | Mobile phone. |
| **name**  string | Guest name. |
| **password**  string | Guest password. |
| **sponsor**  string | Set the action for the sponsor guest user field. |
| **user_id**  string | Guest ID. |
| **http_digest_realm**  string | Realm attribute for MD5-digest authentication. |
| **id**  integer | Group ID. |
| **match**  list / elements=dictionary | Group matches. |
| **group_name**  string | Name of matching user or group on remote authentication server. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **server_name**  string | Name of remote auth server. Source user.radius.name user.ldap.name user.tacacs+.name user.saml.name. |
| **max_accounts**  integer | Maximum number of guest accounts that can be created for this group (0 means unlimited). |
| **member**  list / elements=dictionary | Names of users, peers, LDAP severs, or RADIUS servers to add to the user group. |
| **name**  string / required | Group member name. Source user.peer.name user.local.name user.radius.name user.tacacs+.name user.ldap.name user.saml.name user .adgrp.name user.pop3.name user.certificate.name. |
| **mobile_phone**  string | Enable/disable the guest user mobile phone number field.  **Choices:**   - `"disable"` - `"enable"` |
| **multiple_guest_add**  string | Enable/disable addition of multiple guests.  **Choices:**   - `"disable"` - `"enable"` |
| **name**  string / required | Group name. |
| **password**  string | Guest user password type.  **Choices:**   - `"auto-generate"` - `"specify"` - `"disable"` |
| **sms_custom_server**  string | SMS server. Source system.sms-server.name. |
| **sms_server**  string | Send SMS through FortiGuard or other external server.  **Choices:**   - `"fortiguard"` - `"custom"` |
| **sponsor**  string | Set the action for the sponsor guest user field.  **Choices:**   - `"optional"` - `"mandatory"` - `"disabled"` |
| **sso_attribute_value**  string | Name of the RADIUS user group that this local user group represents. |
| **user_id**  string | Guest user ID type.  **Choices:**   - `"email"` - `"auto-generate"` - `"specify"` |
| **user_name**  string | Enable/disable the guest user name entry.  **Choices:**   - `"disable"` - `"enable"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_user_group_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_user_group_module.md#id5)

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
  - name: Configure user groups.
    fortios_user_group:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      user_group:
        auth_concurrent_override: "enable"
        auth_concurrent_value: "0"
        authtimeout: "0"
        company: "optional"
        email: "disable"
        expire: "14400"
        expire_type: "immediately"
        group_type: "firewall"
        guest:
         -
            comment: "Comment."
            company: "<your_own_value>"
            email: "<your_own_value>"
            expiration: "<your_own_value>"
            id:  "16"
            mobile_phone: "<your_own_value>"
            name: "default_name_18"
            password: "<your_own_value>"
            sponsor: "<your_own_value>"
            user_id: "<your_own_value>"
        http_digest_realm: "<your_own_value>"
        id:  "23"
        match:
         -
            group_name: "<your_own_value>"
            id:  "26"
            server_name: "<your_own_value> (source user.radius.name user.ldap.name user.tacacs+.name user.saml.name)"
        max_accounts: "0"
        member:
         -
            name: "default_name_30 (source user.peer.name user.local.name user.radius.name user.tacacs+.name user.ldap.name user.saml.name user.adgrp.name
               user.pop3.name user.certificate.name)"
        mobile_phone: "disable"
        multiple_guest_add: "disable"
        name: "default_name_33"
        password: "auto-generate"
        sms_custom_server: "<your_own_value> (source system.sms-server.name)"
        sms_server: "fortiguard"
        sponsor: "optional"
        sso_attribute_value: "<your_own_value>"
        user_id: "email"
        user_name: "disable"
```

## [Return Values](fortios_user_group_module.md#id6)

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
