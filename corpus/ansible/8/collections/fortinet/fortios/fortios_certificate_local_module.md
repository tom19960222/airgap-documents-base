---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_certificate_local module – Local keys and certificates in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_certificate_local_module.html
fetched_at: 2026-07-28T02:23:31+00:00
---
# fortinet.fortios.fortios_certificate_local module – Local keys and certificates in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_certificate_local_module.md#ansible-collections-fortinet-fortios-fortios-certificate-local-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_certificate_local`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_certificate_local_module.md#synopsis)
- [Requirements](fortios_certificate_local_module.md#requirements)
- [Parameters](fortios_certificate_local_module.md#parameters)
- [Notes](fortios_certificate_local_module.md#notes)
- [Examples](fortios_certificate_local_module.md#examples)
- [Return Values](fortios_certificate_local_module.md#return-values)

## [Synopsis](fortios_certificate_local_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify certificate feature and local category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_certificate_local_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_certificate_local_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **certificate_local**  dictionary | Local keys and certificates. |
| **acme_ca_url**  string | The URL for the ACME CA server (Let”s Encrypt is the ). |
| **acme_domain**  string | A valid domain that resolves to this FortiGate unit. |
| **acme_email**  string | Contact email address that is required by some CAs like LetsEncrypt. |
| **acme_renew_window**  integer | Beginning of the renewal window (in days before certificate expiration, 30 by default). |
| **acme_rsa_key_size**  integer | Length of the RSA private key of the generated cert (Minimum 2048 bits). |
| **auto_regenerate_days**  integer | Number of days to wait before expiry of an updated local certificate is requested (0 = disabled). |
| **auto_regenerate_days_warning**  integer | Number of days to wait before an expiry warning message is generated (0 = disabled). |
| **ca_identifier**  string | CA identifier of the CA server for signing via SCEP. |
| **certificate**  string | PEM format certificate. |
| **cmp_path**  string | Path location inside CMP server. |
| **cmp_regeneration_method**  string | CMP auto-regeneration method.  **Choices:**   - `"keyupate"` - `"renewal"` |
| **cmp_server**  string | Address and port for CMP server (format = address:port). |
| **cmp_server_cert**  string | CMP server certificate. Source certificate.ca.name certificate.remote.name. |
| **comments**  string | Comment. |
| **csr**  string | Certificate Signing Request. |
| **enroll_protocol**  string | Certificate enrollment protocol.  **Choices:**   - `"none"` - `"scep"` - `"cmpv2"` - `"acme2"` - `"est"` |
| **est_ca_id**  string | CA identifier of the CA server for signing via EST. |
| **est_client_cert**  string | Certificate used to authenticate this FortiGate to EST server. Source certificate.local.name. |
| **est_http_password**  string | HTTP Authentication password for signing via EST. |
| **est_http_username**  string | HTTP Authentication username for signing via EST. |
| **est_server**  string | Address and port for EST server (e.g. <https://example.com:1234>). |
| **est_server_cert**  string | EST server”s certificate must be verifiable by this certificate to be authenticated. Source certificate.ca.name certificate.remote.name. |
| **est_srp_password**  string | EST SRP authentication password. |
| **est_srp_username**  string | EST SRP authentication username. |
| **ike_localid**  string | Local ID the FortiGate uses for authentication as a VPN client. |
| **ike_localid_type**  string | IKE local ID type.  **Choices:**   - `"asn1dn"` - `"fqdn"` |
| **last_updated**  integer | Time at which certificate was last updated. |
| **name**  string / required | Name. |
| **name_encoding**  string | Name encoding method for auto-regeneration.  **Choices:**   - `"printable"` - `"utf8"` |
| **password**  string | Password as a PEM file. |
| **private_key**  string | PEM format key encrypted with a password. |
| **private_key_retain**  string | Enable/disable retention of private key during SCEP renewal .  **Choices:**   - `"enable"` - `"disable"` |
| **range**  string | Either a global or VDOM IP address range for the certificate.  **Choices:**   - `"global"` - `"vdom"` |
| **scep_password**  string | SCEP server challenge password for auto-regeneration. |
| **scep_url**  string | SCEP server URL. |
| **source**  string | Certificate source type.  **Choices:**   - `"factory"` - `"user"` - `"bundle"` |
| **source_ip**  string | Source IP address for communications to the SCEP server. |
| **state**  string | Certificate Signing Request State. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_certificate_local_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_certificate_local_module.md#id5)

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
  - name: Local keys and certificates.
    fortios_certificate_local:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      certificate_local:
        acme_ca_url: "<your_own_value>"
        acme_domain: "<your_own_value>"
        acme_email: "<your_own_value>"
        acme_renew_window: "30"
        acme_rsa_key_size: "2048"
        auto_regenerate_days: "0"
        auto_regenerate_days_warning: "0"
        ca_identifier:  "myId_10"
        certificate: "<your_own_value>"
        cmp_path: "<your_own_value>"
        cmp_regeneration_method: "keyupate"
        cmp_server: "<your_own_value>"
        cmp_server_cert: "<your_own_value> (source certificate.ca.name certificate.remote.name)"
        comments: "<your_own_value>"
        csr: "<your_own_value>"
        enroll_protocol: "none"
        est_ca_id: "<your_own_value>"
        est_client_cert: "<your_own_value> (source certificate.local.name)"
        est_http_password: "<your_own_value>"
        est_http_username: "<your_own_value>"
        est_server: "<your_own_value>"
        est_server_cert: "<your_own_value> (source certificate.ca.name certificate.remote.name)"
        est_srp_password: "<your_own_value>"
        est_srp_username: "<your_own_value>"
        ike_localid: "<your_own_value>"
        ike_localid_type: "asn1dn"
        last_updated: "2147483647"
        name: "default_name_30"
        name_encoding: "printable"
        password: "<your_own_value>"
        private_key: "<your_own_value>"
        private_key_retain: "enable"
        range: "global"
        scep_password: "<your_own_value>"
        scep_url: "<your_own_value>"
        source: "factory"
        source_ip: "84.230.14.43"
        state: "<your_own_value>"
```

## [Return Values](fortios_certificate_local_module.md#id6)

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
