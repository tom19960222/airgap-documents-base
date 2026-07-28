---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_user_fsso module – Configure Fortinet Single Sign On (FSSO) agents in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_user_fsso_module.html
fetched_at: 2026-07-27T17:45:57+00:00
---
# fortinet.fortios.fortios_user_fsso module – Configure Fortinet Single Sign On (FSSO) agents in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_user_fsso_module.md#ansible-collections-fortinet-fortios-fortios-user-fsso-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_user_fsso`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_user_fsso_module.md#synopsis)
- [Requirements](fortios_user_fsso_module.md#requirements)
- [Parameters](fortios_user_fsso_module.md#parameters)
- [Notes](fortios_user_fsso_module.md#notes)
- [Examples](fortios_user_fsso_module.md#examples)
- [Return Values](fortios_user_fsso_module.md#return-values)

## [Synopsis](fortios_user_fsso_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify user feature and fsso category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_user_fsso_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_user_fsso_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **user_fsso**  dictionary | Configure Fortinet Single Sign On (FSSO) agents. |
| **group_poll_interval**  integer | Interval in minutes within to fetch groups from FSSO server, or unset to disable. |
| **interface**  string | Specify outgoing interface to reach server. Source system.interface.name. |
| **interface_select_method**  string | Specify how to select outgoing interface to reach server.  Choices:   - `"auto"` - `"sdwan"` - `"specify"` |
| **ldap_poll**  string | Enable/disable automatic fetching of groups from LDAP server.  Choices:   - `"enable"` - `"disable"` |
| **ldap_poll_filter**  string | Filter used to fetch groups. |
| **ldap_poll_interval**  integer | Interval in minutes within to fetch groups from LDAP server. |
| **ldap_server**  string | LDAP server to get group information. Source user.ldap.name. |
| **logon_timeout**  integer | Interval in minutes to keep logons after FSSO server down. |
| **name**  string / required | Name. |
| **password**  string | Password of the first FSSO collector agent. |
| **password2**  string | Password of the second FSSO collector agent. |
| **password3**  string | Password of the third FSSO collector agent. |
| **password4**  string | Password of the fourth FSSO collector agent. |
| **password5**  string | Password of the fifth FSSO collector agent. |
| **port**  integer | Port of the first FSSO collector agent. |
| **port2**  integer | Port of the second FSSO collector agent. |
| **port3**  integer | Port of the third FSSO collector agent. |
| **port4**  integer | Port of the fourth FSSO collector agent. |
| **port5**  integer | Port of the fifth FSSO collector agent. |
| **server**  string | Domain name or IP address of the first FSSO collector agent. |
| **server2**  string | Domain name or IP address of the second FSSO collector agent. |
| **server3**  string | Domain name or IP address of the third FSSO collector agent. |
| **server4**  string | Domain name or IP address of the fourth FSSO collector agent. |
| **server5**  string | Domain name or IP address of the fifth FSSO collector agent. |
| **sni**  string | Server Name Indication. |
| **source_ip**  string | Source IP for communications to FSSO agent. |
| **source_ip6**  string | IPv6 source for communications to FSSO agent. |
| **ssl**  string | Enable/disable use of SSL.  Choices:   - `"enable"` - `"disable"` |
| **ssl_server_host_ip_check**  string | Enable/disable server host/IP verification.  Choices:   - `"enable"` - `"disable"` |
| **ssl_trusted_cert**  string | Trusted server certificate or CA certificate. Source vpn.certificate.remote.name vpn.certificate.ca.name. |
| **type**  string | Server type.  Choices:   - `"default"` - `"fortinac"` - `"fortiems"` - `"fortiems-cloud"` |
| **user_info_server**  string | LDAP server to get user information. Source user.ldap.name. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_user_fsso_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_user_fsso_module.md#id5)

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
  - name: Configure Fortinet Single Sign On (FSSO) agents.
    fortios_user_fsso:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      user_fsso:
        group_poll_interval: "0"
        interface: "<your_own_value> (source system.interface.name)"
        interface_select_method: "auto"
        ldap_poll: "enable"
        ldap_poll_filter: "<your_own_value>"
        ldap_poll_interval: "180"
        ldap_server: "<your_own_value> (source user.ldap.name)"
        logon_timeout: "5"
        name: "default_name_11"
        password: "<your_own_value>"
        password2: "<your_own_value>"
        password3: "<your_own_value>"
        password4: "<your_own_value>"
        password5: "<your_own_value>"
        port: "8000"
        port2: "8000"
        port3: "8000"
        port4: "8000"
        port5: "8000"
        server: "192.168.100.40"
        server2: "<your_own_value>"
        server3: "<your_own_value>"
        server4: "<your_own_value>"
        server5: "<your_own_value>"
        sni: "<your_own_value>"
        source_ip: "84.230.14.43"
        source_ip6: "<your_own_value>"
        ssl: "enable"
        ssl_server_host_ip_check: "enable"
        ssl_trusted_cert: "<your_own_value> (source vpn.certificate.remote.name vpn.certificate.ca.name)"
        type: "default"
        user_info_server: "<your_own_value> (source user.ldap.name)"
```

## [Return Values](fortios_user_fsso_module.md#id6)

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
