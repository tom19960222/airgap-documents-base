---
collection: ansible
version: "6"
title: "netapp.storagegrid.na_sg_grid_client_certificate module – Manage Client Certificates on StorageGRID"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/storagegrid/na_sg_grid_client_certificate_module.html
fetched_at: 2026-07-28T00:13:37+00:00
---
# netapp.storagegrid.na_sg_grid_client_certificate module – Manage Client Certificates on StorageGRID

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
> To use it in a playbook, specify: `netapp.storagegrid.na_sg_grid_client_certificate`.

New in netapp.storagegrid 21.11.0

- [Synopsis](na_sg_grid_client_certificate_module.md#synopsis)
- [Parameters](na_sg_grid_client_certificate_module.md#parameters)
- [Notes](na_sg_grid_client_certificate_module.md#notes)
- [Examples](na_sg_grid_client_certificate_module.md#examples)
- [Return Values](na_sg_grid_client_certificate_module.md#return-values)

## [Synopsis](na_sg_grid_client_certificate_module.md#id1)

- Create, Update, Delete Client Certificates on NetApp StorageGRID.

## [Parameters](na_sg_grid_client_certificate_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **allow_prometheus**  boolean | Whether the external monitoring tool can access Prometheus metrics.  Choices:   - `false` - `true` |
| **api_url**  string / required | The url to the StorageGRID Admin Node REST API. |
| **auth_token**  string / required | The authorization token for the API request |
| **certificate_id**  string | ID of the client certificate. |
| **display_name**  string | A display name for the client certificate configuration.  This parameter can be modified if *certificate_id* is also specified. |
| **public_key**  string | X.509 client certificate in PEM-encoding. |
| **state**  string | Whether the specified certificate should exist.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |

## [Notes](na_sg_grid_client_certificate_module.md#id3)

> **Note:**
>
> - The modules prefixed with `na_sg` are built to manage NetApp StorageGRID.

## [Examples](na_sg_grid_client_certificate_module.md#id4)

```yaml+jinja
- name: create client certificate
  netapp.storagegrid.na_sg_grid_client_certificate:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    state: present
    display_name: client-cert1
    public_key: |
      -----BEGIN CERTIFICATE-----
      MIIC6DCCAdACCQC7l4WukhKD0zANBgkqhkiG9w0BAQsFADA2..swCQYDVQQGEwJB
      BAMMHnNnYW4wMS5kZXYubWljcm9icmV3Lm5ldGFwcC5hdTCC..IwDQYJKoZIhvcN
      AQEBBQADggEPADCCAQoCggEBAMvjm9I35lmKcC7ITVL8+QiZ..lvdkbfZCUQrfdy
      71inP+XmPjs0rnkhICA9ItODteRcVlO+t7nDTfm7HgG0mJFk..m0ffyEYrcx24qu
      S7gXYQjRsJmrep1awoaCa20BMGuqK2WKI3IvZ7YiT22qkBqK..+hIFffX6u3Jy+B
      77pR6YcATtpMHW/AaOx+OX9l80dIRsRZKMDxYQ==
      -----END CERTIFICATE-----
    allow_prometheus: true

- name: rename client certificate
  netapp.storagegrid.na_sg_grid_client_certificate:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    state: present
    certificate_id: 00000000-0000-0000-0000-000000000000
    display_name: client-cert1-rename
    public_key: |
      -----BEGIN CERTIFICATE-----
      MIIC6DCCAdACCQC7l4WukhKD0zANBgkqhkiG9w0BAQsFADA2..swCQYDVQQGEwJB
      BAMMHnNnYW4wMS5kZXYubWljcm9icmV3Lm5ldGFwcC5hdTCC..IwDQYJKoZIhvcN
      AQEBBQADggEPADCCAQoCggEBAMvjm9I35lmKcC7ITVL8+QiZ..lvdkbfZCUQrfdy
      71inP+XmPjs0rnkhICA9ItODteRcVlO+t7nDTfm7HgG0mJFk..m0ffyEYrcx24qu
      S7gXYQjRsJmrep1awoaCa20BMGuqK2WKI3IvZ7YiT22qkBqK..+hIFffX6u3Jy+B
      77pR6YcATtpMHW/AaOx+OX9l80dIRsRZKMDxYQ==
      -----END CERTIFICATE-----
    allow_prometheus: true

- name: delete client certificate
  netapp.storagegrid.na_sg_grid_client_certificate:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    state: absent
    display_name: client-cert1-rename
```

## [Return Values](na_sg_grid_client_certificate_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resp**  dictionary | Returns information about the StorageGRID server certificates.  Returned: success  Sample: `{"allowPrometheus": true, "displayName": "client-cert1", "expiryDate": "2024-01-01T00:00:00.000Z", "id": "abcABC_01234-0123456789abcABCabc0123456789==", "publicKey": "-----BEGIN CERTIFICATE-----MIIC6DCCAdACCQC7l4WukhKD0zANBgkqhkiG9w0BAQsFADA2MQswCQYDVQQGE...-----END CERTIFICATE-----"}` |

### Authors

- NetApp Ansible Team (@joshedmonds)

### Collection links

[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.storagegrid)
