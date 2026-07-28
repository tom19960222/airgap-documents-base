---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_system_saml module – Global settings for SAML authentication in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_system_saml_module.html
fetched_at: 2026-07-28T02:29:17+00:00
---
# fortinet.fortios.fortios_system_saml module – Global settings for SAML authentication in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_saml_module.md#ansible-collections-fortinet-fortios-fortios-system-saml-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_saml`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_saml_module.md#synopsis)
- [Requirements](fortios_system_saml_module.md#requirements)
- [Parameters](fortios_system_saml_module.md#parameters)
- [Notes](fortios_system_saml_module.md#notes)
- [Examples](fortios_system_saml_module.md#examples)
- [Return Values](fortios_system_saml_module.md#return-values)

## [Synopsis](fortios_system_saml_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and saml category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_saml_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_system_saml_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **system_saml**  dictionary | Global settings for SAML authentication. |
| **artifact_resolution_url**  string | SP artifact resolution URL. |
| **binding_protocol**  string | IdP Binding protocol.  **Choices:**   - `"post"` - `"redirect"` |
| **cert**  string | Certificate to sign SAML messages. Source certificate.local.name. |
| **default_login_page**  string | Choose default login page.  **Choices:**   - `"normal"` - `"sso"` |
| **default_profile**  string | Default profile for new SSO admin. Source system.accprofile.name. |
| **entity_id**  string | SP entity ID. |
| **idp_artifact_resolution_url**  string | IDP artifact resolution URL. |
| **idp_cert**  string | IDP certificate name. Source certificate.remote.name. |
| **idp_entity_id**  string | IDP entity ID. |
| **idp_single_logout_url**  string | IDP single logout URL. |
| **idp_single_sign_on_url**  string | IDP single sign-on URL. |
| **life**  integer | Length of the range of time when the assertion is valid (in minutes). |
| **portal_url**  string | SP portal URL. |
| **role**  string | SAML role.  **Choices:**   - `"identity-provider"` - `"service-provider"` |
| **server_address**  string | Server address. |
| **service_providers**  list / elements=dictionary | Authorized service providers. |
| **assertion_attributes**  list / elements=dictionary | Customized SAML attributes to send along with assertion. |
| **name**  string / required | Name. |
| **type**  string | Type.  **Choices:**   - `"username"` - `"email"` - `"profile-name"` |
| **idp_artifact_resolution_url**  string | IDP artifact resolution URL. |
| **idp_entity_id**  string | IDP entity ID. |
| **idp_single_logout_url**  string | IDP single logout URL. |
| **idp_single_sign_on_url**  string | IDP single sign-on URL. |
| **name**  string / required | Name. |
| **prefix**  string | Prefix. |
| **sp_artifact_resolution_url**  string | SP artifact resolution URL. |
| **sp_binding_protocol**  string | SP binding protocol.  **Choices:**   - `"post"` - `"redirect"` |
| **sp_cert**  string | SP certificate name. Source certificate.remote.name. |
| **sp_entity_id**  string | SP entity ID. |
| **sp_portal_url**  string | SP portal URL. |
| **sp_single_logout_url**  string | SP single logout URL. |
| **sp_single_sign_on_url**  string | SP single sign-on URL. |
| **single_logout_url**  string | SP single logout URL. |
| **single_sign_on_url**  string | SP single sign-on URL. |
| **status**  string | Enable/disable SAML authentication .  **Choices:**   - `"enable"` - `"disable"` |
| **tolerance**  integer | Tolerance to the range of time when the assertion is valid (in minutes). |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_system_saml_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_saml_module.md#id5)

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
  - name: Global settings for SAML authentication.
    fortios_system_saml:
      vdom:  "{{ vdom }}"
      system_saml:
        artifact_resolution_url: "<your_own_value>"
        binding_protocol: "post"
        cert: "<your_own_value> (source certificate.local.name)"
        default_login_page: "normal"
        default_profile: "<your_own_value> (source system.accprofile.name)"
        entity_id: "<your_own_value>"
        idp_artifact_resolution_url: "<your_own_value>"
        idp_cert: "<your_own_value> (source certificate.remote.name)"
        idp_entity_id: "<your_own_value>"
        idp_single_logout_url: "<your_own_value>"
        idp_single_sign_on_url: "<your_own_value>"
        life: "30"
        portal_url: "<your_own_value>"
        role: "identity-provider"
        server_address: "<your_own_value>"
        service_providers:
         -
            assertion_attributes:
             -
                name: "default_name_20"
                type: "username"
            idp_artifact_resolution_url: "<your_own_value>"
            idp_entity_id: "<your_own_value>"
            idp_single_logout_url: "<your_own_value>"
            idp_single_sign_on_url: "<your_own_value>"
            name: "default_name_26"
            prefix: "<your_own_value>"
            sp_artifact_resolution_url: "<your_own_value>"
            sp_binding_protocol: "post"
            sp_cert: "<your_own_value> (source certificate.remote.name)"
            sp_entity_id: "<your_own_value>"
            sp_portal_url: "<your_own_value>"
            sp_single_logout_url: "<your_own_value>"
            sp_single_sign_on_url: "<your_own_value>"
        single_logout_url: "<your_own_value>"
        single_sign_on_url: "<your_own_value>"
        status: "enable"
        tolerance: "5"
```

## [Return Values](fortios_system_saml_module.md#id6)

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
