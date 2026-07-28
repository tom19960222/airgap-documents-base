---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_user_saml module – SAML server entry configuration in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_user_saml_module.html
fetched_at: 2026-07-28T02:30:04+00:00
---
# fortinet.fortios.fortios_user_saml module – SAML server entry configuration in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_user_saml_module.md#ansible-collections-fortinet-fortios-fortios-user-saml-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_user_saml`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_user_saml_module.md#synopsis)
- [Requirements](fortios_user_saml_module.md#requirements)
- [Parameters](fortios_user_saml_module.md#parameters)
- [Notes](fortios_user_saml_module.md#notes)
- [Examples](fortios_user_saml_module.md#examples)
- [Return Values](fortios_user_saml_module.md#return-values)

## [Synopsis](fortios_user_saml_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify user feature and saml category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_user_saml_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_user_saml_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **user_saml**  dictionary | SAML server entry configuration. |
| **adfs_claim**  string | Enable/disable ADFS Claim for user/group attribute in assertion statement .  **Choices:**   - `"enable"` - `"disable"` |
| **auth_url**  string | URL to verify authentication. |
| **cert**  string | Certificate to sign SAML messages. Source vpn.certificate.local.name. |
| **clock_tolerance**  integer | Clock skew tolerance in seconds (0 - 300). |
| **digest_method**  string | Digest method algorithm .  **Choices:**   - `"sha1"` - `"sha256"` |
| **entity_id**  string | SP entity ID. |
| **group_claim_type**  string | Group claim in assertion statement.  **Choices:**   - `"email"` - `"given-name"` - `"name"` - `"upn"` - `"common-name"` - `"email-adfs-1x"` - `"group"` - `"upn-adfs-1x"` - `"role"` - `"sur-name"` - `"ppid"` - `"name-identifier"` - `"authentication-method"` - `"deny-only-group-sid"` - `"deny-only-primary-sid"` - `"deny-only-primary-group-sid"` - `"group-sid"` - `"primary-group-sid"` - `"primary-sid"` - `"windows-account-name"` |
| **group_name**  string | Group name in assertion statement. |
| **idp_cert**  string | IDP Certificate name. Source vpn.certificate.remote.name. |
| **idp_entity_id**  string | IDP entity ID. |
| **idp_single_logout_url**  string | IDP single logout url. |
| **idp_single_sign_on_url**  string | IDP single sign-on URL. |
| **limit_relaystate**  string | Enable/disable limiting of relay-state parameter when it exceeds SAML 2.0 specification limits (80 bytes).  **Choices:**   - `"enable"` - `"disable"` |
| **name**  string / required | SAML server entry name. |
| **reauth**  string | Enable/disable signalling of IDP to force user re-authentication .  **Choices:**   - `"enable"` - `"disable"` |
| **single_logout_url**  string | SP single logout URL. |
| **single_sign_on_url**  string | SP single sign-on URL. |
| **user_claim_type**  string | User name claim in assertion statement.  **Choices:**   - `"email"` - `"given-name"` - `"name"` - `"upn"` - `"common-name"` - `"email-adfs-1x"` - `"group"` - `"upn-adfs-1x"` - `"role"` - `"sur-name"` - `"ppid"` - `"name-identifier"` - `"authentication-method"` - `"deny-only-group-sid"` - `"deny-only-primary-sid"` - `"deny-only-primary-group-sid"` - `"group-sid"` - `"primary-group-sid"` - `"primary-sid"` - `"windows-account-name"` |
| **user_name**  string | User name in assertion statement. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_user_saml_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_user_saml_module.md#id5)

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
  - name: SAML server entry configuration.
    fortios_user_saml:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      user_saml:
        adfs_claim: "enable"
        auth_url: "<your_own_value>"
        cert: "<your_own_value> (source vpn.certificate.local.name)"
        clock_tolerance: "15"
        digest_method: "sha1"
        entity_id: "<your_own_value>"
        group_claim_type: "email"
        group_name: "<your_own_value>"
        idp_cert: "<your_own_value> (source vpn.certificate.remote.name)"
        idp_entity_id: "<your_own_value>"
        idp_single_logout_url: "<your_own_value>"
        idp_single_sign_on_url: "<your_own_value>"
        limit_relaystate: "enable"
        name: "default_name_16"
        reauth: "enable"
        single_logout_url: "<your_own_value>"
        single_sign_on_url: "<your_own_value>"
        user_claim_type: "email"
        user_name: "<your_own_value>"
```

## [Return Values](fortios_user_saml_module.md#id6)

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
