---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_user_peer module – Configure peer users in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_user_peer_module.html
fetched_at: 2026-07-27T17:46:02+00:00
---
# fortinet.fortios.fortios_user_peer module – Configure peer users in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_user_peer_module.md#ansible-collections-fortinet-fortios-fortios-user-peer-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_user_peer`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_user_peer_module.md#synopsis)
- [Requirements](fortios_user_peer_module.md#requirements)
- [Parameters](fortios_user_peer_module.md#parameters)
- [Notes](fortios_user_peer_module.md#notes)
- [Examples](fortios_user_peer_module.md#examples)
- [Return Values](fortios_user_peer_module.md#return-values)

## [Synopsis](fortios_user_peer_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify user feature and peer category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_user_peer_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_user_peer_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **user_peer**  dictionary | Configure peer users. |
| **ca**  string | Name of the CA certificate. Source vpn.certificate.ca.name. |
| **cn**  string | Peer certificate common name. |
| **cn_type**  string | Peer certificate common name type.  Choices:   - `"string"` - `"email"` - `"FQDN"` - `"ipv4"` - `"ipv6"` |
| **ldap_mode**  string | Mode for LDAP peer authentication.  Choices:   - `"password"` - `"principal-name"` |
| **ldap_password**  string | Password for LDAP server bind. |
| **ldap_server**  string | Name of an LDAP server defined under the user ldap command. Performs client access rights check. Source user.ldap.name. |
| **ldap_username**  string | Username for LDAP server bind. |
| **mandatory_ca_verify**  string | Determine what happens to the peer if the CA certificate is not installed. Disable to automatically consider the peer certificate as valid.  Choices:   - `"enable"` - `"disable"` |
| **name**  string / required | Peer name. |
| **ocsp_override_server**  string | Online Certificate Status Protocol (OCSP) server for certificate retrieval. Source vpn.certificate.ocsp-server.name. |
| **passwd**  string | Peer”s password used for two-factor authentication. |
| **subject**  string | Peer certificate name constraints. |
| **two_factor**  string | Enable/disable two-factor authentication, applying certificate and password-based authentication.  Choices:   - `"enable"` - `"disable"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_user_peer_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_user_peer_module.md#id5)

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
  - name: Configure peer users.
    fortios_user_peer:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      user_peer:
        ca: "<your_own_value> (source vpn.certificate.ca.name)"
        cn: "<your_own_value>"
        cn_type: "string"
        ldap_mode: "password"
        ldap_password: "<your_own_value>"
        ldap_server: "<your_own_value> (source user.ldap.name)"
        ldap_username: "<your_own_value>"
        mandatory_ca_verify: "enable"
        name: "default_name_11"
        ocsp_override_server: "<your_own_value> (source vpn.certificate.ocsp-server.name)"
        passwd: "<your_own_value>"
        subject: "<your_own_value>"
        two_factor: "enable"
```

## [Return Values](fortios_user_peer_module.md#id6)

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
