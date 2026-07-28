---
collection: ansible
version: "6"
title: "netapp.ontap.na_ontap_security_certificates module – NetApp ONTAP manage security certificates."
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/ontap/na_ontap_security_certificates_module.html
fetched_at: 2026-07-28T00:13:09+00:00
---
# netapp.ontap.na_ontap_security_certificates module – NetApp ONTAP manage security certificates.

> **Note:**
>
> This module is part of the [netapp.ontap collection](https://galaxy.ansible.com/netapp/ontap) (version 21.24.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.ontap`.
> You need further requirements to be able to use this module,
> see [Requirements](na_ontap_security_certificates_module.md#ansible-collections-netapp-ontap-na-ontap-security-certificates-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_security_certificates`.

New in netapp.ontap 20.7.0

- [Synopsis](na_ontap_security_certificates_module.md#synopsis)
- [Requirements](na_ontap_security_certificates_module.md#requirements)
- [Parameters](na_ontap_security_certificates_module.md#parameters)
- [Notes](na_ontap_security_certificates_module.md#notes)
- [Examples](na_ontap_security_certificates_module.md#examples)
- [Return Values](na_ontap_security_certificates_module.md#return-values)

## [Synopsis](na_ontap_security_certificates_module.md#id1)

- Install or delete security certificates on ONTAP. (Create and sign will come in a second iteration)

## [Requirements](na_ontap_security_certificates_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_security_certificates_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **common_name**  string | Common name of the certificate.  Required for create and install.  If name is present, ignored for sign and delete.  If name is absent or ignored, required for sign and delete. |
| **expiry_time**  string | Certificate expiration time. Specifying an expiration time is recommended when creating a certificate.  Can be provided when signing a certificate. |
| **feature_flags**  dictionary  added in netapp.ontap 20.5.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  added in netapp.ontap 21.23.0 | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hash_function**  string | Hashing function. Can be provided when creating a self-signed certificate or when signing a certificate.  Allowed values for create and sign are sha256, sha224, sha384, sha512. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  Choices:   - `false` ← (default) - `true` |
| **ignore_name_if_not_supported**  boolean  added in netapp.ontap 20.8.0 | ONTAP 9.6 and 9.7 REST API does not support *name*.  If set to true, no error is reported if *name* is present, and *name* is not used.  Choices:   - `false` - `true` ← (default) |
| **intermediate_certificates**  list / elements=string | Chain of intermediate Certificates in PEM format.  Only valid when installing a certificate. |
| **key_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client key file. |
| **key_size**  integer | Key size of the certificate in bits. Specifying a strong key size is recommended when creating a certificate.  Ignored for sign and delete. |
| **name**  string | The unique name of the security certificate per SVM.  This parameter is not supported for ONTAP 9.6 or 9.7, as the REST API does not support it.  If present with ONTAP 9.6 or 9.7, it is ignored by default, see *ignore_name_if_not_supported*.  It is strongly recommended to use name for newer releases of ONTAP. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **private_key**  string | Private key certificate in PEM format.  Required when installing a CA-signed certificate. Ignored otherwise. |
| **public_certificate**  string | Public key certificate in PEM format.  Required when installing a certificate. Ignored otherwise. |
| **signing_request**  string | If present, the certificate identified by name and svm is used to sign the request.  A signed certificate is returned. |
| **state**  string | Whether the specified security certificate should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **svm**  aliases: vserver  string | The name of the SVM (vserver).  If present, the certificate is installed in the SVM.  If absent, the certificate is installed in the cluster. |
| **type**  string | Type of certificate  Required for create and install.  If name is present, ignored for sign and delete.  If name is absent or ignored, required for sign and delete.  Choices:   - `"client"` - `"server"` - `"client_ca"` - `"server_ca"` - `"root_ca"` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  Default: `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](na_ontap_security_certificates_module.md#id4)

> **Note:**
>
> - supports check mode.
> - only supports REST. Requires ONTAP 9.6 or later, ONTAP 9.8 or later is recommended.
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_security_certificates_module.md#id5)

```yaml+jinja
- name: install certificate
  netapp.ontap.na_ontap_security_certificates:
    # <<: *cert_login
    common_name: "{{ ontap_cert_common_name }}"
    name: "{{ ontap_cert_name }}"
    public_certificate: "{{ ssl_certificate }}"
    type: client_ca
    svm: "{{ vserver }}"

- name: create certificate
  netapp.ontap.na_ontap_security_certificates:
    # <<: *cert_login
    common_name: "{{ ontap_cert_root_common_name }}"
    name: "{{ ontap_cert_name }}"
    type: root_ca
    svm: "{{ vserver }}"
    expiry_time: P365DT     # one year

- name: sign certificate using newly create certificate
  tags: sign_request
  netapp.ontap.na_ontap_security_certificates:
    # <<: *login
    name: "{{ ontap_cert_name }}"
    svm: "{{ vserver }}"
    signing_request: |
      -----BEGIN CERTIFICATE REQUEST-----
      MIIChDCCAWwCAQAwPzELMAkGA1UEBhMCVVMxCzAJBgNVBAgMAkNBMRIwEAYDVQQH
      DAlTdW5ueXZhbGUxDzANBgNVBAoMBk5ldEFwcDCCASIwDQYJKoZIhvcNAQEBBQAD
      ggEPADCCAQoCggEBALgXCj6Si/I4xLdV7wjWYTbt8jY20fQOjk/4E7yBT1vFBflE
      ks6YDc6dhC2G18cnoj9E3DiR8lIHPoAlFB/VmBNDev3GZkbFlrbV7qYmf8OEx2H2
      tAefgSP0jLmCHCN1yyhJoCG6FsAiD3tf6yoyFF6qS9ureGL0tCJJ/osx64WzUz+Q
      EN8lx7VSxriEFMSjreXZDhUFaCdIYKKRENuEWyYvdy5cbBmczhuM8EP6peOVv5Hm
      BJzPUDkq7oTtEHmttpATq2Y92qzNzETO0bXN5X/93AWri8/yEXdX+HEw1C/omtsE
      jGsCXrCrIJ+DgUdT/GHNdBWlXl/cWGtEgEQ4vrUCAwEAAaAAMA0GCSqGSIb3DQEB
      CwUAA4IBAQBjZNoQgr/JDm1T8zyRhLkl3zw4a16qKNu/MS7prqZHLVQgrptHRegU
      Hbz11XoHfVOdbyuvtzEe95QsDd6FYCZ4qzZRF3se4IjMeqwdQZ5WP0/GFiwM8Uln
      /0TCWjt759XMeUX7+wgOg5NRjJ660eWMXzu/UJf+vZO0Q2FiPIr13JvvY3TjT+9J
      UUtK4r9PaUuOPN2YL9IQqSD3goh8302Qr3nBXUgjeUGLkgfUM5S39apund2hyTX2
      JCLQsKr88pwU9iDho2tHLv/2QgLwNZLPu8V+7IGu6G4vB28lN4Uy7xbhxFOKtyWu
      fK4sEdTw3B/aDN0tB8MHFdPYycNZsEac
      -----END CERTIFICATE REQUEST-----
    expiry_time: P180DT

- name: delete certificate
  netapp.ontap.na_ontap_security_certificates:
    # <<: *cert_login
    state: absent
    name: "{{ ontap_cert_name }}"
    svm: "{{ vserver }}"

# For ONTAP 9.6 or 9.7, use common_name and type, in addition to, or in lieu of name
- name: install certificate
  netapp.ontap.na_ontap_security_certificates:
    # <<: *cert_login
    common_name: "{{ ontap_cert_common_name }}"
    public_certificate: "{{ ssl_certificate }}"
    type: client_ca
    svm: "{{ vserver }}"

- name: create certificate
  netapp.ontap.na_ontap_security_certificates:
    # <<: *cert_login
    common_name: "{{ ontap_cert_root_common_name }}"
    type: root_ca
    svm: "{{ vserver }}"
    expiry_time: P365DT     # one year

- name: sign certificate using newly create certificate
  tags: sign_request
  netapp.ontap.na_ontap_security_certificates:
    # <<: *login
    common_name: "{{ ontap_cert_root_common_name }}"
    type: root_ca
    svm: "{{ vserver }}"
    signing_request: |
      -----BEGIN CERTIFICATE REQUEST-----
      MIIChDCCAWwCAQAwPzELMAkGA1UEBhMCVVMxCzAJBgNVBAgMAkNBMRIwEAYDVQQH
      DAlTdW5ueXZhbGUxDzANBgNVBAoMBk5ldEFwcDCCASIwDQYJKoZIhvcNAQEBBQAD
      ggEPADCCAQoCggEBALgXCj6Si/I4xLdV7wjWYTbt8jY20fQOjk/4E7yBT1vFBflE
      ks6YDc6dhC2G18cnoj9E3DiR8lIHPoAlFB/VmBNDev3GZkbFlrbV7qYmf8OEx2H2
      tAefgSP0jLmCHCN1yyhJoCG6FsAiD3tf6yoyFF6qS9ureGL0tCJJ/osx64WzUz+Q
      EN8lx7VSxriEFMSjreXZDhUFaCdIYKKRENuEWyYvdy5cbBmczhuM8EP6peOVv5Hm
      BJzPUDkq7oTtEHmttpATq2Y92qzNzETO0bXN5X/93AWri8/yEXdX+HEw1C/omtsE
      jGsCXrCrIJ+DgUdT/GHNdBWlXl/cWGtEgEQ4vrUCAwEAAaAAMA0GCSqGSIb3DQEB
      CwUAA4IBAQBjZNoQgr/JDm1T8zyRhLkl3zw4a16qKNu/MS7prqZHLVQgrptHRegU
      Hbz11XoHfVOdbyuvtzEe95QsDd6FYCZ4qzZRF3se4IjMeqwdQZ5WP0/GFiwM8Uln
      /0TCWjt759XMeUX7+wgOg5NRjJ660eWMXzu/UJf+vZO0Q2FiPIr13JvvY3TjT+9J
      UUtK4r9PaUuOPN2YL9IQqSD3goh8302Qr3nBXUgjeUGLkgfUM5S39apund2hyTX2
      JCLQsKr88pwU9iDho2tHLv/2QgLwNZLPu8V+7IGu6G4vB28lN4Uy7xbhxFOKtyWu
      fK4sEdTw3B/aDN0tB8MHFdPYycNZsEac
      -----END CERTIFICATE REQUEST-----
    expiry_time: P180DT

- name: delete certificate
  netapp.ontap.na_ontap_security_certificates:
    # <<: *cert_login
    state: absent
    common_name: "{{ ontap_cert_root_common_name }}"
    type: root_ca
    name: "{{ ontap_cert_name }}"
    svm: "{{ vserver }}"
```

## [Return Values](na_ontap_security_certificates_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ontap_info**  dictionary | Returns public_certificate when signing, empty for create, install, and delete.  Returned: always  Sample: `{"ontap_info": {"public_certificate": "-----BEGIN CERTIFICATE----- ........-----END CERTIFICATE----- "}}` |

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
