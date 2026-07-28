---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_user_ldap module – Configure LDAP server entries in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_user_ldap_module.html
fetched_at: 2026-07-27T17:46:00+00:00
---
# fortinet.fortios.fortios_user_ldap module – Configure LDAP server entries in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_user_ldap_module.md#ansible-collections-fortinet-fortios-fortios-user-ldap-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_user_ldap`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_user_ldap_module.md#synopsis)
- [Requirements](fortios_user_ldap_module.md#requirements)
- [Parameters](fortios_user_ldap_module.md#parameters)
- [Notes](fortios_user_ldap_module.md#notes)
- [Examples](fortios_user_ldap_module.md#examples)
- [Return Values](fortios_user_ldap_module.md#return-values)

## [Synopsis](fortios_user_ldap_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify user feature and ldap category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_user_ldap_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_user_ldap_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **user_ldap**  dictionary | Configure LDAP server entries. |
| **account_key_filter**  string | Account key filter, using the UPN as the search filter. |
| **account_key_processing**  string | Account key processing operation, either keep or strip domain string of UPN in the token.  Choices:   - `"same"` - `"strip"` |
| **antiphish**  string | Enable/disable AntiPhishing credential backend.  Choices:   - `"enable"` - `"disable"` |
| **ca_cert**  string | CA certificate name. Source vpn.certificate.ca.name. |
| **client_cert**  string | Client certificate name. Source vpn.certificate.local.name. |
| **client_cert_auth**  string | Enable/disable using client certificate for TLS authentication.  Choices:   - `"enable"` - `"disable"` |
| **cnid**  string | Common name identifier for the LDAP server. The common name identifier for most LDAP servers is “cn”. |
| **dn**  string | Distinguished name used to look up entries on the LDAP server. |
| **group_filter**  string | Filter used for group matching. |
| **group_member_check**  string | Group member checking methods.  Choices:   - `"user-attr"` - `"group-object"` - `"posix-group-object"` |
| **group_object_filter**  string | Filter used for group searching. |
| **group_search_base**  string | Search base used for group searching. |
| **interface**  string | Specify outgoing interface to reach server. Source system.interface.name. |
| **interface_select_method**  string | Specify how to select outgoing interface to reach server.  Choices:   - `"auto"` - `"sdwan"` - `"specify"` |
| **member_attr**  string | Name of attribute from which to get group membership. |
| **name**  string / required | LDAP server entry name. |
| **obtain_user_info**  string | Enable/disable obtaining of user information.  Choices:   - `"enable"` - `"disable"` |
| **password**  string | Password for initial binding. |
| **password_attr**  string | Name of attribute to get password hash. |
| **password_expiry_warning**  string | Enable/disable password expiry warnings.  Choices:   - `"enable"` - `"disable"` |
| **password_renewal**  string | Enable/disable online password renewal.  Choices:   - `"enable"` - `"disable"` |
| **port**  integer | Port to be used for communication with the LDAP server . |
| **search_type**  list / elements=string | Search type.  Choices:   - `"recursive"` |
| **secondary_server**  string | Secondary LDAP server CN domain name or IP. |
| **secure**  string | Port to be used for authentication.  Choices:   - `"disable"` - `"starttls"` - `"ldaps"` |
| **server**  string | LDAP server CN domain name or IP. |
| **server_identity_check**  string | Enable/disable LDAP server identity check (verify server domain name/IP address against the server certificate).  Choices:   - `"enable"` - `"disable"` |
| **source_ip**  string | FortiGate IP address to be used for communication with the LDAP server. |
| **source_port**  integer | Source port to be used for communication with the LDAP server. |
| **ssl_min_proto_version**  string | Minimum supported protocol version for SSL/TLS connections .  Choices:   - `"default"` - `"SSLv3"` - `"TLSv1"` - `"TLSv1-1"` - `"TLSv1-2"` |
| **tertiary_server**  string | Tertiary LDAP server CN domain name or IP. |
| **two_factor**  string | Enable/disable two-factor authentication.  Choices:   - `"disable"` - `"fortitoken-cloud"` |
| **two_factor_authentication**  string | Authentication method by FortiToken Cloud.  Choices:   - `"fortitoken"` - `"email"` - `"sms"` |
| **two_factor_filter**  string | Filter used to synchronize users to FortiToken Cloud. |
| **two_factor_notification**  string | Notification method for user activation by FortiToken Cloud.  Choices:   - `"email"` - `"sms"` |
| **type**  string | Authentication type for LDAP searches.  Choices:   - `"simple"` - `"anonymous"` - `"regular"` |
| **user_info_exchange_server**  string | MS Exchange server from which to fetch user information. Source user.exchange.name. |
| **username**  string | Username (full DN) for initial binding. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_user_ldap_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_user_ldap_module.md#id5)

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
  - name: Configure LDAP server entries.
    fortios_user_ldap:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      user_ldap:
        account_key_filter: "<your_own_value>"
        account_key_processing: "same"
        antiphish: "enable"
        ca_cert: "<your_own_value> (source vpn.certificate.ca.name)"
        client_cert: "<your_own_value> (source vpn.certificate.local.name)"
        client_cert_auth: "enable"
        cnid: "<your_own_value>"
        dn: "<your_own_value>"
        group_filter: "<your_own_value>"
        group_member_check: "user-attr"
        group_object_filter: "<your_own_value>"
        group_search_base: "<your_own_value>"
        interface: "<your_own_value> (source system.interface.name)"
        interface_select_method: "auto"
        member_attr: "<your_own_value>"
        name: "default_name_18"
        obtain_user_info: "enable"
        password: "<your_own_value>"
        password_attr: "<your_own_value>"
        password_expiry_warning: "enable"
        password_renewal: "enable"
        port: "389"
        search_type: "recursive"
        secondary_server: "<your_own_value>"
        secure: "disable"
        server: "192.168.100.40"
        server_identity_check: "enable"
        source_ip: "84.230.14.43"
        source_port: "0"
        ssl_min_proto_version: "default"
        tertiary_server: "<your_own_value>"
        two_factor: "disable"
        two_factor_authentication: "fortitoken"
        two_factor_filter: "<your_own_value>"
        two_factor_notification: "email"
        type: "simple"
        user_info_exchange_server: "<your_own_value> (source user.exchange.name)"
        username: "<your_own_value>"
```

## [Return Values](fortios_user_ldap_module.md#id6)

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
