---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_user_radius module – Configure RADIUS server entries in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_user_radius_module.html
fetched_at: 2026-07-27T17:46:05+00:00
---
# fortinet.fortios.fortios_user_radius module – Configure RADIUS server entries in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_user_radius_module.md#ansible-collections-fortinet-fortios-fortios-user-radius-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_user_radius`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_user_radius_module.md#synopsis)
- [Requirements](fortios_user_radius_module.md#requirements)
- [Parameters](fortios_user_radius_module.md#parameters)
- [Notes](fortios_user_radius_module.md#notes)
- [Examples](fortios_user_radius_module.md#examples)
- [Return Values](fortios_user_radius_module.md#return-values)

## [Synopsis](fortios_user_radius_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify user feature and radius category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_user_radius_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_user_radius_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **user_radius**  dictionary | Configure RADIUS server entries. |
| **accounting_server**  list / elements=dictionary | Additional accounting servers. |
| **id**  integer | ID (0 - 4294967295). |
| **interface**  string | Specify outgoing interface to reach server. Source system.interface.name. |
| **interface_select_method**  string | Specify how to select outgoing interface to reach server.  Choices:   - `"auto"` - `"sdwan"` - `"specify"` |
| **port**  integer | RADIUS accounting port number. |
| **secret**  string | Secret key. |
| **server**  string | Server CN domain name or IP address. |
| **source_ip**  string | Source IP address for communications to the RADIUS server. |
| **status**  string | Status.  Choices:   - `"enable"` - `"disable"` |
| **acct_all_servers**  string | Enable/disable sending of accounting messages to all configured servers .  Choices:   - `"enable"` - `"disable"` |
| **acct_interim_interval**  integer | Time in seconds between each accounting interim update message. |
| **all_usergroup**  string | Enable/disable automatically including this RADIUS server in all user groups.  Choices:   - `"disable"` - `"enable"` |
| **auth_type**  string | Authentication methods/protocols permitted for this RADIUS server.  Choices:   - `"auto"` - `"ms_chap_v2"` - `"ms_chap"` - `"chap"` - `"pap"` |
| **class**  list / elements=dictionary | Class attribute name(s). |
| **name**  string | Class name. |
| **delimiter**  string | Configure delimiter to be used for separating profile group names in the SSO attribute .  Choices:   - `"plus"` - `"comma"` |
| **group_override_attr_type**  string | RADIUS attribute type to override user group information.  Choices:   - `"filter-Id"` - `"class"` |
| **h3c_compatibility**  string | Enable/disable compatibility with the H3C, a mechanism that performs security checking for authentication.  Choices:   - `"enable"` - `"disable"` |
| **interface**  string | Specify outgoing interface to reach server. Source system.interface.name. |
| **interface_select_method**  string | Specify how to select outgoing interface to reach server.  Choices:   - `"auto"` - `"sdwan"` - `"specify"` |
| **mac_case**  string | MAC authentication case .  Choices:   - `"uppercase"` - `"lowercase"` |
| **mac_password_delimiter**  string | MAC authentication password delimiter .  Choices:   - `"hyphen"` - `"single-hyphen"` - `"colon"` - `"none"` |
| **mac_username_delimiter**  string | MAC authentication username delimiter .  Choices:   - `"hyphen"` - `"single-hyphen"` - `"colon"` - `"none"` |
| **name**  string / required | RADIUS server entry name. |
| **nas_ip**  string | IP address used to communicate with the RADIUS server and used as NAS-IP-Address and Called-Station-ID attributes. |
| **password_encoding**  string | Password encoding.  Choices:   - `"auto"` - `"ISO-8859-1"` |
| **password_renewal**  string | Enable/disable password renewal.  Choices:   - `"enable"` - `"disable"` |
| **radius_coa**  string | Enable to allow a mechanism to change the attributes of an authentication, authorization, and accounting session after it is authenticated.  Choices:   - `"enable"` - `"disable"` |
| **radius_port**  integer | RADIUS service port number. |
| **rsso**  string | Enable/disable RADIUS based single sign on feature.  Choices:   - `"enable"` - `"disable"` |
| **rsso_context_timeout**  integer | Time in seconds before the logged out user is removed from the “user context list” of logged on users. |
| **rsso_endpoint_attribute**  string | RADIUS attributes used to extract the user end point identifier from the RADIUS Start record.  Choices:   - `"User-Name"` - `"NAS-IP-Address"` - `"Framed-IP-Address"` - `"Framed-IP-Netmask"` - `"Filter-Id"` - `"Login-IP-Host"` - `"Reply-Message"` - `"Callback-Number"` - `"Callback-Id"` - `"Framed-Route"` - `"Framed-IPX-Network"` - `"Class"` - `"Called-Station-Id"` - `"Calling-Station-Id"` - `"NAS-Identifier"` - `"Proxy-State"` - `"Login-LAT-Service"` - `"Login-LAT-Node"` - `"Login-LAT-Group"` - `"Framed-AppleTalk-Zone"` - `"Acct-Session-Id"` - `"Acct-Multi-Session-Id"` |
| **rsso_endpoint_block_attribute**  string | RADIUS attributes used to block a user.  Choices:   - `"User-Name"` - `"NAS-IP-Address"` - `"Framed-IP-Address"` - `"Framed-IP-Netmask"` - `"Filter-Id"` - `"Login-IP-Host"` - `"Reply-Message"` - `"Callback-Number"` - `"Callback-Id"` - `"Framed-Route"` - `"Framed-IPX-Network"` - `"Class"` - `"Called-Station-Id"` - `"Calling-Station-Id"` - `"NAS-Identifier"` - `"Proxy-State"` - `"Login-LAT-Service"` - `"Login-LAT-Node"` - `"Login-LAT-Group"` - `"Framed-AppleTalk-Zone"` - `"Acct-Session-Id"` - `"Acct-Multi-Session-Id"` |
| **rsso_ep_one_ip_only**  string | Enable/disable the replacement of old IP addresses with new ones for the same endpoint on RADIUS accounting Start messages.  Choices:   - `"enable"` - `"disable"` |
| **rsso_flush_ip_session**  string | Enable/disable flushing user IP sessions on RADIUS accounting Stop messages.  Choices:   - `"enable"` - `"disable"` |
| **rsso_log_flags**  list / elements=string | Events to log.  Choices:   - `"protocol-error"` - `"profile-missing"` - `"accounting-stop-missed"` - `"accounting-event"` - `"endpoint-block"` - `"radiusd-other"` - `"none"` |
| **rsso_log_period**  integer | Time interval in seconds that group event log messages will be generated for dynamic profile events. |
| **rsso_radius_response**  string | Enable/disable sending RADIUS response packets after receiving Start and Stop records.  Choices:   - `"enable"` - `"disable"` |
| **rsso_radius_server_port**  integer | UDP port to listen on for RADIUS Start and Stop records. |
| **rsso_secret**  string | RADIUS secret used by the RADIUS accounting server. |
| **rsso_validate_request_secret**  string | Enable/disable validating the RADIUS request shared secret in the Start or End record.  Choices:   - `"enable"` - `"disable"` |
| **secondary_secret**  string | Secret key to access the secondary server. |
| **secondary_server**  string | Secondary RADIUS CN domain name or IP address. |
| **secret**  string | Pre-shared secret key used to access the primary RADIUS server. |
| **server**  string | Primary RADIUS server CN domain name or IP address. |
| **source_ip**  string | Source IP address for communications to the RADIUS server. |
| **sso_attribute**  string | RADIUS attribute that contains the profile group name to be extracted from the RADIUS Start record.  Choices:   - `"User-Name"` - `"NAS-IP-Address"` - `"Framed-IP-Address"` - `"Framed-IP-Netmask"` - `"Filter-Id"` - `"Login-IP-Host"` - `"Reply-Message"` - `"Callback-Number"` - `"Callback-Id"` - `"Framed-Route"` - `"Framed-IPX-Network"` - `"Class"` - `"Called-Station-Id"` - `"Calling-Station-Id"` - `"NAS-Identifier"` - `"Proxy-State"` - `"Login-LAT-Service"` - `"Login-LAT-Node"` - `"Login-LAT-Group"` - `"Framed-AppleTalk-Zone"` - `"Acct-Session-Id"` - `"Acct-Multi-Session-Id"` |
| **sso_attribute_key**  string | Key prefix for SSO group value in the SSO attribute. |
| **sso_attribute_value_override**  string | Enable/disable override old attribute value with new value for the same endpoint.  Choices:   - `"enable"` - `"disable"` |
| **switch_controller_acct_fast_framedip_detect**  integer | Switch controller accounting message Framed-IP detection from DHCP snooping (seconds). |
| **switch_controller_service_type**  list / elements=string | RADIUS service type.  Choices:   - `"login"` - `"framed"` - `"callback-login"` - `"callback-framed"` - `"outbound"` - `"administrative"` - `"nas-prompt"` - `"authenticate-only"` - `"callback-nas-prompt"` - `"call-check"` - `"callback-administrative"` |
| **tertiary_secret**  string | Secret key to access the tertiary server. |
| **tertiary_server**  string | Tertiary RADIUS CN domain name or IP address. |
| **timeout**  integer | Time in seconds between re-sending authentication requests. |
| **use_management_vdom**  string | Enable/disable using management VDOM to send requests.  Choices:   - `"enable"` - `"disable"` |
| **username_case_sensitive**  string | Enable/disable case sensitive user names.  Choices:   - `"enable"` - `"disable"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_user_radius_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_user_radius_module.md#id5)

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
  - name: Configure RADIUS server entries.
    fortios_user_radius:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      user_radius:
        accounting_server:
         -
            id:  "4"
            interface: "<your_own_value> (source system.interface.name)"
            interface_select_method: "auto"
            port: "0"
            secret: "<your_own_value>"
            server: "192.168.100.40"
            source_ip: "84.230.14.43"
            status: "enable"
        acct_all_servers: "enable"
        acct_interim_interval: "0"
        all_usergroup: "disable"
        auth_type: "auto"
        class:
         -
            name: "default_name_17"
        delimiter: "plus"
        group_override_attr_type: "filter-Id"
        h3c_compatibility: "enable"
        interface: "<your_own_value> (source system.interface.name)"
        interface_select_method: "auto"
        mac_case: "uppercase"
        mac_password_delimiter: "hyphen"
        mac_username_delimiter: "hyphen"
        name: "default_name_26"
        nas_ip: "<your_own_value>"
        password_encoding: "auto"
        password_renewal: "enable"
        radius_coa: "enable"
        radius_port: "0"
        rsso: "enable"
        rsso_context_timeout: "28800"
        rsso_endpoint_attribute: "User-Name"
        rsso_endpoint_block_attribute: "User-Name"
        rsso_ep_one_ip_only: "enable"
        rsso_flush_ip_session: "enable"
        rsso_log_flags: "protocol-error"
        rsso_log_period: "0"
        rsso_radius_response: "enable"
        rsso_radius_server_port: "1813"
        rsso_secret: "<your_own_value>"
        rsso_validate_request_secret: "enable"
        secondary_secret: "<your_own_value>"
        secondary_server: "<your_own_value>"
        secret: "<your_own_value>"
        server: "192.168.100.40"
        source_ip: "84.230.14.43"
        sso_attribute: "User-Name"
        sso_attribute_key: "<your_own_value>"
        sso_attribute_value_override: "enable"
        switch_controller_acct_fast_framedip_detect: "2"
        switch_controller_service_type: "login"
        tertiary_secret: "<your_own_value>"
        tertiary_server: "<your_own_value>"
        timeout: "5"
        use_management_vdom: "enable"
        username_case_sensitive: "enable"
```

## [Return Values](fortios_user_radius_module.md#id6)

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
