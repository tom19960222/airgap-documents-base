---
collection: ansible
version: "6"
title: "netapp_eseries.santricity.na_santricity_client_certificate module – NetApp E-Series manage remote server certificates."
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp_eseries/santricity/na_santricity_client_certificate_module.html
fetched_at: 2026-07-28T00:13:54+00:00
---
# netapp_eseries.santricity.na_santricity_client_certificate module – NetApp E-Series manage remote server certificates.

> **Note:**
>
> This module is part of the [netapp_eseries.santricity collection](https://galaxy.ansible.com/netapp_eseries/santricity) (version 1.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp_eseries.santricity`.
> You need further requirements to be able to use this module,
> see [Requirements](na_santricity_client_certificate_module.md#ansible-collections-netapp-eseries-santricity-na-santricity-client-certificate-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp_eseries.santricity.na_santricity_client_certificate`.

- [Synopsis](na_santricity_client_certificate_module.md#synopsis)
- [Requirements](na_santricity_client_certificate_module.md#requirements)
- [Parameters](na_santricity_client_certificate_module.md#parameters)
- [Notes](na_santricity_client_certificate_module.md#notes)
- [Examples](na_santricity_client_certificate_module.md#examples)
- [Return Values](na_santricity_client_certificate_module.md#return-values)

## [Synopsis](na_santricity_client_certificate_module.md#id1)

- Manage NetApp E-Series storage array’s remote server certificates.

## [Requirements](na_santricity_client_certificate_module.md#id2)

The below requirements are needed on the host that executes this module.

- cryptography

## [Parameters](na_santricity_client_certificate_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API.  Example <https://prod-1.wahoo.acme.com:8443/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **certificates**  list / elements=string | List of certificate files  Each item must include the path to the file |
| **reload_certificates**  boolean | Whether to reload certificates when certificates have been added or removed.  Certificates will not be available or removed until the servers have been reloaded.  Choices:   - `false` - `true` ← (default) |
| **remove_unspecified_user_certificates**  boolean | Whether to remove user install client certificates that are not specified in *certificates*.  Choices:   - `false` ← (default) - `true` |
| **ssid**  string | The ID of the array to manage. This value must be unique for each array.  Default: `"1"` |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |

## [Notes](na_santricity_client_certificate_module.md#id4)

> **Note:**
>
> - Set *ssid==”0”* or *ssid==”proxy”* to specifically reference SANtricity Web Services Proxy.
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing M() at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](na_santricity_client_certificate_module.md#id5)

```yaml+jinja
- name: Upload certificates
  na_santricity_client_certificate:
    ssid: 1
    api_url: https://192.168.1.100:8443/devmgr/v2
    api_username: admin
    api_password: adminpass
    certificates: ["/path/to/certificates.crt", "/path/to/another_certificate.crt"]
- name: Remove all certificates
  na_santricity_client_certificate:
    ssid: 1
    api_url: https://192.168.1.100:8443/devmgr/v2
    api_username: admin
    api_password: adminpass
```

## [Return Values](na_santricity_client_certificate_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **add_certificates**  list / elements=string | Any SSL certificates that were added.  Returned: always  Sample: `["added_cerificiate.crt"]` |
| **changed**  boolean | Whether changes have been made.  Returned: always  Sample: `true` |
| **removed_certificates**  list / elements=string | Any SSL certificates that were removed.  Returned: always  Sample: `["removed_cerificiate.crt"]` |

### Authors

- Nathan Swartz (@ndswartz)

### Collection links

[Issue Tracker](https://github.com/netappeseries/santricity/issues)
[Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
