---
collection: ansible
version: "8"
title: "netapp_eseries.santricity.na_santricity_server_certificate module – NetApp E-Series manage the storage system’s server SSL certificates."
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp_eseries/santricity/na_santricity_server_certificate_module.html
fetched_at: 2026-07-28T02:44:18+00:00
---
# netapp_eseries.santricity.na_santricity_server_certificate module – NetApp E-Series manage the storage system’s server SSL certificates.

> **Note:**
>
> This module is part of the [netapp_eseries.santricity collection](https://galaxy.ansible.com/ui/repo/published/netapp_eseries/santricity/) (version 1.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp_eseries.santricity`.
> You need further requirements to be able to use this module,
> see [Requirements](na_santricity_server_certificate_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-server-certificate-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp_eseries.santricity.na_santricity_server_certificate`.

- [Synopsis](na_santricity_server_certificate_module.md#synopsis)
- [Requirements](na_santricity_server_certificate_module.md#requirements)
- [Parameters](na_santricity_server_certificate_module.md#parameters)
- [Notes](na_santricity_server_certificate_module.md#notes)
- [Examples](na_santricity_server_certificate_module.md#examples)
- [Return Values](na_santricity_server_certificate_module.md#return-values)

## [Synopsis](na_santricity_server_certificate_module.md#id1)

- Manage NetApp E-Series storage system’s server SSL certificates.

## [Requirements](na_santricity_server_certificate_module.md#id2)

The below requirements are needed on the host that executes this module.

- cryptography

## [Parameters](na_santricity_server_certificate_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API.  Example <https://prod-1.wahoo.acme.com:8443/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **certificates**  list / elements=string | Unordered list of all server certificate files which include PEM and DER encoded certificates as well as private keys.  When *certificates* is not defined then a self-signed certificate will be expected. |
| **controller**  string | The controller that owns the port you want to configure.  Controller names are represented alphabetically, with the first controller as A, the second as B, and so on.  Current hardware models have either 1 or 2 available controllers, but that is not a guaranteed hard limitation and could change in the future.  *controller* must be specified unless managing SANtricity Web Services Proxy (ie *ssid=”proxy”*)  **Choices:**   - `"A"` - `"B"` |
| **passphrase**  string | Passphrase for PEM encoded private key encryption.  If *passphrase* is not supplied then Ansible will prompt for private key certificate. |
| **ssid**  string | The ID of the array to manage. This value must be unique for each array.  **Default:** `"1"` |
| **validate_certs**  boolean | Should https certificates be validated?  **Choices:**   - `false` - `true` ← (default) |

## [Notes](na_santricity_server_certificate_module.md#id4)

> **Note:**
>
> - Set *ssid==’0’* or *ssid==’proxy’* to specifically reference SANtricity Web Services Proxy.
> - Certificates can be the following filetypes - PEM (.pem, .crt, .cer, or .key) or DER (.der or .cer)
> - When *certificates* is not defined then a self-signed certificate will be expected.
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing “M(netapp_e_storage_system)” at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](na_santricity_server_certificate_module.md#id5)

```yaml+jinja
- name: Ensure signed certificate is installed.
  na_santricity_server_certificate:
    ssid: 1
    api_url: https://192.168.1.100:8443/devmgr/v2
    api_username: admin
    api_password: adminpass
    controller: A
    certificates:
      - 'root_auth_cert.pem'
      - 'intermediate_auth1_cert.pem'
      - 'intermediate_auth2_cert.pem'
      - 'public_cert.pem'
      - 'private_key.pem'
    passphrase: keypass
- name: Ensure signed certificate bundle is installed.
  na_santricity_server_certificate:
    ssid: 1
    api_url: https://192.168.1.100:8443/devmgr/v2
    api_username: admin
    api_password: adminpass
    controller: B
    certificates:
      - 'cert_bundle.pem'
    passphrase: keypass
- name: Ensure storage system generated self-signed certificate is installed.
  na_santricity_server_certificate:
    ssid: 1
    api_url: https://192.168.1.100:8443/devmgr/v2
    api_username: admin
    api_password: adminpass
    controller: A
```

## [Return Values](na_santricity_server_certificate_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **added_certificates**  list / elements=string | Any SSL certificates that were added.  **Returned:** always  **Sample:** `["added_certificiate.crt"]` |
| **changed**  boolean | Whether changes have been made.  **Returned:** always  **Sample:** `true` |
| **removed_certificates**  list / elements=string | Any SSL certificates that were removed.  **Returned:** always  **Sample:** `["removed_certificiate.crt"]` |
| **signed_server_certificate**  boolean | Whether the public server certificate is signed.  **Returned:** always  **Sample:** `true` |

### Authors

- Nathan Swartz (@ndswartz)

### Collection links

- [Issue Tracker](https://github.com/netappeseries/santricity/issues)
- [Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
