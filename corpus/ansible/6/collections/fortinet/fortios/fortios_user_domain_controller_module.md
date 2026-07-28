---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_user_domain_controller module – Configure domain controller entries in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_user_domain_controller_module.html
fetched_at: 2026-07-27T17:45:55+00:00
---
# fortinet.fortios.fortios_user_domain_controller module – Configure domain controller entries in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_user_domain_controller_module.md#ansible-collections-fortinet-fortios-fortios-user-domain-controller-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_user_domain_controller`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_user_domain_controller_module.md#synopsis)
- [Requirements](fortios_user_domain_controller_module.md#requirements)
- [Parameters](fortios_user_domain_controller_module.md#parameters)
- [Notes](fortios_user_domain_controller_module.md#notes)
- [Examples](fortios_user_domain_controller_module.md#examples)
- [Return Values](fortios_user_domain_controller_module.md#return-values)

## [Synopsis](fortios_user_domain_controller_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify user feature and domain_controller category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_user_domain_controller_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_user_domain_controller_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **user_domain_controller**  dictionary | Configure domain controller entries. |
| **ad_mode**  string | Set Active Directory mode.  Choices:   - `"none"` - `"ds"` - `"lds"` |
| **adlds_dn**  string | AD LDS distinguished name. |
| **adlds_ip6**  string | AD LDS IPv6 address. |
| **adlds_ip_address**  string | AD LDS IPv4 address. |
| **adlds_port**  integer | Port number of AD LDS service . |
| **dns_srv_lookup**  string | Enable/disable DNS service lookup.  Choices:   - `"enable"` - `"disable"` |
| **domain_name**  string | Domain DNS name. |
| **extra_server**  list / elements=dictionary | Extra servers. |
| **id**  integer | Server ID. |
| **ip_address**  string | Domain controller IP address. |
| **port**  integer | Port to be used for communication with the domain controller . |
| **source_ip_address**  string | FortiGate IPv4 address to be used for communication with the domain controller. |
| **source_port**  integer | Source port to be used for communication with the domain controller. |
| **hostname**  string | Hostname of the server to connect to. |
| **interface**  string | Specify outgoing interface to reach server. Source system.interface.name. |
| **interface_select_method**  string | Specify how to select outgoing interface to reach server.  Choices:   - `"auto"` - `"sdwan"` - `"specify"` |
| **ip6**  string | Domain controller IPv6 address. |
| **ip_address**  string | Domain controller IPv4 address. |
| **ldap_server**  list / elements=dictionary | LDAP server name(s). Source user.ldap.name. |
| **name**  string | LDAP server name. Source user.ldap.name. |
| **name**  string / required | Domain controller entry name. |
| **password**  string | Password for specified username. |
| **port**  integer | Port to be used for communication with the domain controller . |
| **replication_port**  integer | Port to be used for communication with the domain controller for replication service. Port number 0 indicates automatic discovery. |
| **source_ip6**  string | FortiGate IPv6 address to be used for communication with the domain controller. |
| **source_ip_address**  string | FortiGate IPv4 address to be used for communication with the domain controller. |
| **source_port**  integer | Source port to be used for communication with the domain controller. |
| **username**  string | User name to sign in with. Must have proper permissions for service. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_user_domain_controller_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_user_domain_controller_module.md#id5)

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
  - name: Configure domain controller entries.
    fortios_user_domain_controller:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      user_domain_controller:
        ad_mode: "none"
        adlds_dn: "<your_own_value>"
        adlds_ip_address: "<your_own_value>"
        adlds_ip6: "<your_own_value>"
        adlds_port: "389"
        dns_srv_lookup: "enable"
        domain_name: "<your_own_value>"
        extra_server:
         -
            id:  "11"
            ip_address: "<your_own_value>"
            port: "445"
            source_ip_address: "<your_own_value>"
            source_port: "0"
        hostname: "myhostname"
        interface: "<your_own_value> (source system.interface.name)"
        interface_select_method: "auto"
        ip_address: "<your_own_value>"
        ip6: "<your_own_value>"
        ldap_server:
         -
            name: "default_name_22 (source user.ldap.name)"
        name: "default_name_23"
        password: "<your_own_value>"
        port: "445"
        replication_port: "0"
        source_ip_address: "<your_own_value>"
        source_ip6: "<your_own_value>"
        source_port: "0"
        username: "<your_own_value>"
```

## [Return Values](fortios_user_domain_controller_module.md#id6)

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
