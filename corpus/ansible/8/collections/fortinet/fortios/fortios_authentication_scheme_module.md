---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_authentication_scheme module – Configure Authentication Schemes in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_authentication_scheme_module.html
fetched_at: 2026-07-28T02:23:25+00:00
---
# fortinet.fortios.fortios_authentication_scheme module – Configure Authentication Schemes in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_authentication_scheme_module.md#ansible-collections-fortinet-fortios-fortios-authentication-scheme-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_authentication_scheme`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_authentication_scheme_module.md#synopsis)
- [Requirements](fortios_authentication_scheme_module.md#requirements)
- [Parameters](fortios_authentication_scheme_module.md#parameters)
- [Notes](fortios_authentication_scheme_module.md#notes)
- [Examples](fortios_authentication_scheme_module.md#examples)
- [Return Values](fortios_authentication_scheme_module.md#return-values)

## [Synopsis](fortios_authentication_scheme_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify authentication feature and scheme category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_authentication_scheme_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_authentication_scheme_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **authentication_scheme**  dictionary | Configure Authentication Schemes. |
| **domain_controller**  string | Domain controller setting. Source user.domain-controller.name. |
| **ems_device_owner**  string | Enable/disable SSH public-key authentication with device owner .  **Choices:**   - `"enable"` - `"disable"` |
| **fsso_agent_for_ntlm**  string | FSSO agent to use for NTLM authentication. Source user.fsso.name. |
| **fsso_guest**  string | Enable/disable user fsso-guest authentication .  **Choices:**   - `"enable"` - `"disable"` |
| **kerberos_keytab**  string | Kerberos keytab setting. Source user.krb-keytab.name. |
| **method**  list / elements=string | Authentication methods .  **Choices:**   - `"ntlm"` - `"basic"` - `"digest"` - `"form"` - `"negotiate"` - `"fsso"` - `"rsso"` - `"ssh-publickey"` - `"cert"` - `"saml"` |
| **name**  string / required | Authentication scheme name. |
| **negotiate_ntlm**  string | Enable/disable negotiate authentication for NTLM .  **Choices:**   - `"enable"` - `"disable"` |
| **require_tfa**  string | Enable/disable two-factor authentication .  **Choices:**   - `"enable"` - `"disable"` |
| **saml_server**  string | SAML configuration. Source user.saml.name. |
| **saml_timeout**  integer | SAML authentication timeout in seconds. |
| **ssh_ca**  string | SSH CA name. Source firewall.ssh.local-ca.name. |
| **user_cert**  string | Enable/disable authentication with user certificate .  **Choices:**   - `"enable"` - `"disable"` |
| **user_database**  list / elements=dictionary | Authentication server to contain user information; “local” (default) or “123” (for LDAP). |
| **name**  string / required | Authentication server name. Source system.datasource.name user.radius.name user.tacacs+.name user.ldap.name user.group.name. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_authentication_scheme_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_authentication_scheme_module.md#id5)

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
  - name: Configure Authentication Schemes.
    fortios_authentication_scheme:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      authentication_scheme:
        domain_controller: "<your_own_value> (source user.domain-controller.name)"
        ems_device_owner: "enable"
        fsso_agent_for_ntlm: "<your_own_value> (source user.fsso.name)"
        fsso_guest: "enable"
        kerberos_keytab: "<your_own_value> (source user.krb-keytab.name)"
        method: "ntlm"
        name: "default_name_9"
        negotiate_ntlm: "enable"
        require_tfa: "enable"
        saml_server: "<your_own_value> (source user.saml.name)"
        saml_timeout: "120"
        ssh_ca: "<your_own_value> (source firewall.ssh.local-ca.name)"
        user_cert: "enable"
        user_database:
         -
            name: "default_name_17 (source system.datasource.name user.radius.name user.tacacs+.name user.ldap.name user.group.name)"
```

## [Return Values](fortios_authentication_scheme_module.md#id6)

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
