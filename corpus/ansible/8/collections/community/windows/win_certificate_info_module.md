---
collection: ansible
version: "8"
title: "community.windows.win_certificate_info module – Get information on certificates from a Windows Certificate Store"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_certificate_info_module.html
fetched_at: 2026-07-28T02:01:39+00:00
---
# community.windows.win_certificate_info module – Get information on certificates from a Windows Certificate Store

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/ui/repo/published/community/windows/) (version 1.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_certificate_info`.

- [Synopsis](win_certificate_info_module.md#synopsis)
- [Parameters](win_certificate_info_module.md#parameters)
- [See Also](win_certificate_info_module.md#see-also)
- [Examples](win_certificate_info_module.md#examples)
- [Return Values](win_certificate_info_module.md#return-values)

## [Synopsis](win_certificate_info_module.md#id1)

- Returns information about certificates in a Windows Certificate Store.

## [Parameters](win_certificate_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **store_location**  string | The location of the store to search.  **Choices:**   - `"CurrentUser"` - `"LocalMachine"` ← (default) |
| **store_name**  string | The name of the store to search.  See <https://docs.microsoft.com/en-us/dotnet/api/system.security.cryptography.x509certificates.storename> for a list of built-in store names.  **Default:** `"My"` |
| **thumbprint**  string | The thumbprint as a hex string of a certificate to find.  When specified, filters the *certificates* return value to a single certificate  See the examples for how to format the thumbprint. |

## [See Also](win_certificate_info_module.md#id3)

> **See also:**
>
> [ansible.windows.win_certificate_store](../../ansible/windows/win_certificate_store_module.md#ansible-collections-ansible-windows-win-certificate-store-module)
> :   Manages the certificate store.

## [Examples](win_certificate_info_module.md#id4)

```yaml+jinja
- name: Obtain information about a particular certificate in the computer's personal store
  community.windows.win_certificate_info:
    thumbprint: BD7AF104CF1872BDB518D95C9534EA941665FD27
  register: mycert

# thumbprint can also be lower case
- name: Obtain information about a particular certificate in the computer's personal store
  community.windows.win_certificate_info:
    thumbprint: bd7af104cf1872bdb518d95c9534ea941665fd27
  register: mycert

- name: Obtain information about all certificates in the root store
  community.windows.win_certificate_info:
    store_name: Root
  register: ca

# Import a pfx and then get information on the certificates
- name: Import pfx certificate that is password protected
  ansible.windows.win_certificate_store:
    path: C:\Temp\cert.pfx
    state: present
    password: VeryStrongPasswordHere!
  become: yes
  become_method: runas
  register: mycert

- name: Obtain information on each certificate that was touched
  community.windows.win_certificate_info:
    thumbprint: "{{ item }}"
  register: mycert_stats
  loop: "{{ mycert.thumbprints }}"
```

## [Return Values](win_certificate_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **certificates**  list / elements=dictionary | A list of information about certificates found in the store, sorted by thumbprint.  **Returned:** success |
| **archived**  boolean | Indicates that the certificate is archived.  **Returned:** success  **Sample:** `false` |
| **cert_data**  string | The base64 encoded data of the entire certificate.  **Returned:** success |
| **dns_names**  list / elements=string | Lists the registered dns names for the certificate.  **Returned:** success  **Sample:** `["*.m.wikiquote.org", "*.wikipedia.org"]` |
| **extensions**  list / elements=dictionary | The collection of the certificates extensions.  **Returned:** success  **Sample:** `[{"critical": false, "field": "Subject Key Identifier", "value": "88 27 17 09 a9 b6 18 60 8b ec eb ba f6 47 59 c5 52 54 a3 b7"}, {"critical": true, "field": "Basic Constraints", "value": "Subject Type=CA, Path Length Constraint=None"}, {"critical": false, "field": "Authority Key Identifier", "value": "KeyID=2b d0 69 47 94 76 09 fe f4 6b 8d 2e 40 a6 f7 47 4d 7f 08 5e"}, {"critical": false, "field": "CRL Distribution Points", "value": "[1]CRL Distribution Point: Distribution Point Name:Full Name:URL=http://crl.apple.com/root.crl"}, {"critical": true, "field": "Key Usage", "value": "Digital Signature, Certificate Signing, Off-line CRL Signing, CRL Signing (86)"}, {"critical": false, "field": null, "value": "05 00"}]` |
| **friendly_name**  string | The associated alias for the certificate.  **Returned:** success  **Sample:** `"Microsoft Root Authority"` |
| **has_private_key**  boolean | Indicates that the certificate contains a private key.  **Returned:** success  **Sample:** `false` |
| **intended_purposes**  list / elements=string | lists the intended applications for the certificate.  **Returned:** enhanced key usages extension exists.  **Sample:** `["Server Authentication"]` |
| **is_ca**  boolean | Indicates that the certificate is a certificate authority (CA) certificate.  **Returned:** basic constraints extension exists.  **Sample:** `true` |
| **issued_by**  string | The certificate issuer’s common name.  **Returned:** success  **Sample:** `"Apple Root CA"` |
| **issued_to**  string | The certificate’s common name.  **Returned:** success  **Sample:** `"Apple Worldwide Developer Relations Certification Authority"` |
| **issuer**  string | The certificate issuer’s distinguished name.  **Returned:** success  **Sample:** `"CN=Apple Root CA, OU=Apple Certification Authority, O=Apple Inc., C=US"` |
| **key_usages**  list / elements=string | Defines how the certificate key can be used.  If this value is not defined, the key can be used for any purpose.  **Returned:** key usages extension exists.  **Sample:** `["CrlSign", "KeyCertSign", "DigitalSignature"]` |
| **path_length_constraint**  integer | The number of levels allowed in a certificates path.  If this value is 0, the certificate does not have a restriction.  **Returned:** basic constraints extension exists  **Sample:** `0` |
| **public_key**  string | The base64 encoded public key of the certificate.  **Returned:** success |
| **serial_number**  string | The serial number of the certificate represented as a hexadecimal string  **Returned:** success  **Sample:** `"01DEBCC4396DA010"` |
| **signature_algorithm**  string | The algorithm used to create the certificate’s signature  **Returned:** success  **Sample:** `"sha1RSA"` |
| **ski**  string | The certificate’s subject key identifier  **Returned:** subject key identifier extension exists.  **Sample:** `"88271709A9B618608BECEBBAF64759C55254A3B7"` |
| **subject**  string | The certificate’s distinguished name.  **Returned:** success  **Sample:** `"CN=Apple Worldwide Developer Relations Certification Authority, OU=Apple Worldwide Developer Relations, O=Apple Inc., C=US"` |
| **thumbprint**  string | The thumbprint as a hex string of the certificate.  The return format will always be upper case.  **Returned:** success  **Sample:** `"FF6797793A3CD798DC5B2ABEF56F73EDC9F83A64"` |
| **valid_from**  float | The start date of the certificate represented in seconds since epoch.  **Returned:** success  **Sample:** `1360255727.0` |
| **valid_from_iso8601**  string | The start date of the certificate represented as an iso8601 formatted date.  **Returned:** success  **Sample:** `"2017-12-15T08:39:32Z"` |
| **valid_to**  float | The expiry date of the certificate represented in seconds since epoch.  **Returned:** success  **Sample:** `1675788527.0` |
| **valid_to_iso8601**  string | The expiry date of the certificate represented as an iso8601 formatted date.  **Returned:** success  **Sample:** `"2086-01-02T08:39:32Z"` |
| **version**  integer | The x509 format version of the certificate  **Returned:** success  **Sample:** `3` |
| **exists**  boolean | Whether any certificates were found in the store.  When *thumbprint* is specified, returns true only if the certificate mathing the thumbprint exists.  **Returned:** success  **Sample:** `true` |

### Authors

- Micah Hunsberger (@mhunsber)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
