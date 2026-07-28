---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_user_fsso_polling module – Configure FSSO active directory servers for polling mode in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_user_fsso_polling_module.html
fetched_at: 2026-07-27T17:45:57+00:00
---
# fortinet.fortios.fortios_user_fsso_polling module – Configure FSSO active directory servers for polling mode in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_user_fsso_polling_module.md#ansible-collections-fortinet-fortios-fortios-user-fsso-polling-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_user_fsso_polling`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_user_fsso_polling_module.md#synopsis)
- [Requirements](fortios_user_fsso_polling_module.md#requirements)
- [Parameters](fortios_user_fsso_polling_module.md#parameters)
- [Notes](fortios_user_fsso_polling_module.md#notes)
- [Examples](fortios_user_fsso_polling_module.md#examples)
- [Return Values](fortios_user_fsso_polling_module.md#return-values)

## [Synopsis](fortios_user_fsso_polling_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify user feature and fsso_polling category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_user_fsso_polling_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_user_fsso_polling_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **user_fsso_polling**  dictionary | Configure FSSO active directory servers for polling mode. |
| **adgrp**  list / elements=dictionary | LDAP Group Info. |
| **name**  string | Name. |
| **default_domain**  string | Default domain managed by this Active Directory server. |
| **id**  integer / required | Active Directory server ID. |
| **ldap_server**  string | LDAP server name used in LDAP connection strings. Source user.ldap.name. |
| **logon_history**  integer | Number of hours of logon history to keep, 0 means keep all history. |
| **password**  string | Password required to log into this Active Directory server. |
| **polling_frequency**  integer | Polling frequency (every 1 to 30 seconds). |
| **port**  integer | Port to communicate with this Active Directory server. |
| **server**  string | Host name or IP address of the Active Directory server. |
| **smb_ntlmv1_auth**  string | Enable/disable support of NTLMv1 for Samba authentication.  Choices:   - `"enable"` - `"disable"` |
| **smbv1**  string | Enable/disable support of SMBv1 for Samba.  Choices:   - `"enable"` - `"disable"` |
| **status**  string | Enable/disable polling for the status of this Active Directory server.  Choices:   - `"enable"` - `"disable"` |
| **user**  string | User name required to log into this Active Directory server. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_user_fsso_polling_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_user_fsso_polling_module.md#id5)

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
  - name: Configure FSSO active directory servers for polling mode.
    fortios_user_fsso_polling:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      user_fsso_polling:
        adgrp:
         -
            name: "default_name_4"
        default_domain: "<your_own_value>"
        id:  "6"
        ldap_server: "<your_own_value> (source user.ldap.name)"
        logon_history: "8"
        password: "<your_own_value>"
        polling_frequency: "10"
        port: "0"
        server: "192.168.100.40"
        smb_ntlmv1_auth: "enable"
        smbv1: "enable"
        status: "enable"
        user: "<your_own_value>"
```

## [Return Values](fortios_user_fsso_polling_module.md#id6)

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
