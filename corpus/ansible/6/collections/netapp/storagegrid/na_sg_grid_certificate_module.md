---
collection: ansible
version: "6"
title: "netapp.storagegrid.na_sg_grid_certificate module – Manage the Storage API and Grid Management certificates on StorageGRID."
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/storagegrid/na_sg_grid_certificate_module.html
fetched_at: 2026-07-28T00:13:36+00:00
---
# netapp.storagegrid.na_sg_grid_certificate module – Manage the Storage API and Grid Management certificates on StorageGRID.

> **Note:**
>
> This module is part of the [netapp.storagegrid collection](https://galaxy.ansible.com/netapp/storagegrid) (version 21.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.storagegrid`.
>
> To use it in a playbook, specify: `netapp.storagegrid.na_sg_grid_certificate`.

New in netapp.storagegrid 21.6.0

- [Synopsis](na_sg_grid_certificate_module.md#synopsis)
- [Parameters](na_sg_grid_certificate_module.md#parameters)
- [Notes](na_sg_grid_certificate_module.md#notes)
- [Examples](na_sg_grid_certificate_module.md#examples)
- [Return Values](na_sg_grid_certificate_module.md#return-values)

## [Synopsis](na_sg_grid_certificate_module.md#id1)

- Set and update the Storage API and Grid Management certificates on NetApp StorageGRID.

## [Parameters](na_sg_grid_certificate_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_url**  string / required | The url to the StorageGRID Admin Node REST API. |
| **auth_token**  string / required | The authorization token for the API request |
| **ca_bundle**  string | Intermediate CA certificate bundle in concatenated PEM-encoding.  Omit if there is no intermediate CA. |
| **private_key**  string | Certificate private key in PEM-encoding.  Required if *server_certificate* is specified. |
| **server_certificate**  string | X.509 server certificate in PEM-encoding. |
| **state**  string | Whether the specified certificate should be set.  Choices:   - `"present"` ← (default) - `"absent"` |
| **type**  string / required | Which certificate to update.  Choices:   - `"storage-api"` - `"management"` |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |

## [Notes](na_sg_grid_certificate_module.md#id3)

> **Note:**
>
> - The modules prefixed with `na_sg` are built to manage NetApp StorageGRID.

## [Examples](na_sg_grid_certificate_module.md#id4)

```yaml+jinja
- name: set storage API certificate
  netapp.storagegrid.na_sg_grid_certificate:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    state: present
    type: storage-api
    server_certificate: |
      -----BEGIN CERTIFICATE-----
      MIIC6DCCAdACCQC7l4WukhKD0zANBgkqhkiG9w0BAQsFADA2MQswCQYDVQQGEwJB
      BAMMHnNnYW4wMS5kZXYubWljcm9icmV3Lm5ldGFwcC5hdTCCASIwDQYJKoZIhvcN
      AQEBBQADggEPADCCAQoCggEBAMvjm9I35lmKcC7ITVL8+QiZ/klvdkbfZCUQrfdy
      71inP+XmPjs0rnkhICA9ItODteRcVlO+t7nDTfm7HgG0mJFkcJm0ffyEYrcx24qu
      S7gXYQjRsJmrep1awoaCa20BMGuqK2WKI3IvZ7YiT22qkBqKJD+hIFffX6u3Jy+B
      77pR6YcATtpMHW/AaOx+OX9l80dIRsRZKMDxYQ==
      -----END CERTIFICATE-----
    private_key: |
      -----BEGIN PRIVATE KEY-----
      MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDL45vSN+ZZinAu
      L25W0+cz1Oi69AKkI7d9nbFics2ay5+7o+4rKqf3en2R4MSxiJvy+iDlOmATib5O
      x8TN5pJ9AgMBAAECggEADDLM8tHXXUoUFihzv+BUwff8p8YcbHcXFcSes+xTd5li
      po8lNsx/v2pQx4ByBkuaYLZGIEXOWS6gkp44xhIXgQKBgQD4Hq7862u5HLbmhrV3
      vs8nC69b3QKBgQDacCD8d8JpwPbg8t2VjXM3UvdmgAaLUfU7O1DWV+W3jqzmDOoN
      zWVgPbPNj0UmzvLDbgxLoxe77wjn2BHsAJVAfJ9VeQKBgGqFAegYO+wHR8lJUoa5
      ZEe8Upy2oBtvND/0dnwO2ym2FGsBJN0Gr4NKdG5vkzLsthKkcwRm0ikwEUOUZQKE
      K8J5yEVeo9K2v3wggtq8fYn6
      -----END PRIVATE KEY-----
```

## [Return Values](na_sg_grid_certificate_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resp**  dictionary | Returns information about the StorageGRID server certificates.  Returned: success  Sample: `{"caBundleEncoded": "-----BEGIN CERTIFICATE-----MIIDdTCCAl2gAwIBAgILBAAAAAABFUtaw5QwDQYJKoZIhvcNAQEFBQAwVzELM...-----END CERTIFICATE-----", "serverCertificateEncoded": "-----BEGIN CERTIFICATE-----MIIC6DCCAdACCQC7l4WukhKD0zANBgkqhkiG9w0BAQsFADA2MQswCQYDVQQGE...-----END CERTIFICATE-----"}` |

### Authors

- NetApp Ansible Team (@joshedmonds)

### Collection links

[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.storagegrid)
