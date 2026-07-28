---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_certs module – Manage FlashArray SSL Certificates"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_certs_module.html
fetched_at: 2026-07-28T02:50:41+00:00
---
# purestorage.flasharray.purefa_certs module – Manage FlashArray SSL Certificates

> **Note:**
>
> This module is part of the [purestorage.flasharray collection](https://galaxy.ansible.com/ui/repo/published/purestorage/flasharray/) (version 1.24.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flasharray`.
> You need further requirements to be able to use this module,
> see [Requirements](purefa_certs_module.md#ansible-collections-purestorage-flasharray-purefa-certs-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_certs`.

New in purestorage.flasharray 1.8.0

- [Synopsis](purefa_certs_module.md#synopsis)
- [Requirements](purefa_certs_module.md#requirements)
- [Parameters](purefa_certs_module.md#parameters)
- [Notes](purefa_certs_module.md#notes)
- [Examples](purefa_certs_module.md#examples)

## [Synopsis](purefa_certs_module.md#id1)

- Create, delete, import and export FlashArray SSL Certificates

## [Requirements](purefa_certs_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_certs_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **certificate**  string | Required for *import*  A valid signed certicate in PEM format (Base64 encoded)  Includes the “—–BEGIN CERTIFICATE—–” and “—–END CERTIFICATE—–” lines  Does not exceed 3000 characters in length |
| **common_name**  string | The fully qualified domain name (FQDN) of the current array  For example, the common name for <https://purearray.example.com> is purearray.example.com, or \*.example.com for a wildcard certificate  This can also be the management IP address of the array or the shortname of the current array.  Maximum of 64 characters  If not provided this will default to the shortname of the array |
| **country**  string | The two-letter ISO code for the country where your organization is located |
| **days**  integer | The number of valid days for the self-signed certificate being generated  If not specified, the self-signed certificate expires after 3650 days.  **Default:** `3650` |
| **email**  string | The email address used to contact your organization |
| **export_file**  string | Name of file to contain Certificate Signing Request when `status sign`  Name of file to export the current SSL Certificate when `status export`  File will be overwritten if it already exists |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **generate**  boolean | Generate a new private key.  If not selected, the certificate will use the existing key  **Choices:**   - `false` ← (default) - `true` |
| **intermeadiate_cert**  string | Intermeadiate certificate provided by the CA |
| **key**  string | If the Certificate Signed Request (CSR) was not constructed on the array or the private key has changed since construction the CSR, provide a new private key here |
| **key_size**  integer | The key size in bits if you generate a new private key  **Choices:**   - `1024` - `2048` ← (default) - `4096` |
| **locality**  string | The full name of the city where your organization is located |
| **name**  string | Name of the SSL Certificate  **Default:** `"management"` |
| **org_unit**  string | The department within your organization that is managing the certificate |
| **organization**  string | The full and exact legal name of your organization.  The organization name should not be abbreviated and should include suffixes such as Inc, Corp, or LLC. |
| **passphrase**  string | Passphrase if the private key is encrypted |
| **province**  string | The full name of the state or province where your organization is located |
| **state**  string | Action for the module to perform  *present* will create or re-create an SSL certificate  *absent* will delete an existing SSL certificate  *sign* will construct a Certificate Signing request (CSR)  *export* will export the exisitng SSL certificate  *import* will import a CA provided certificate.  **Choices:**   - `"absent"` - `"present"` ← (default) - `"import"` - `"export"` - `"sign"` |

## [Notes](purefa_certs_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_certs_module.md#id5)

```yaml+jinja
- name: Create SSL certifcate foo
  purestorage.flasharray.purefa_certs:
    name: foo
    key_size: 4096
    country: US
    province: FL
    locality: Miami
    organization: "Acme Inc"
    org_unit: "DevOps"
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Delete SSL certificate foo
  purestorage.flasharray.purefa_certs:
    name: foo
    state: absent
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Request CSR
  purestorage.flasharray.purefa_certs:
    state: sign
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Request CSR with updated fields
  purestorage.flasharray.purefa_certs:
    state: sign
    org_unit: Development
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Regenerate key for SSL foo
  purestorage.flasharray.purefa_certs:
    generate: true
    name: foo
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Import SSL Cert foo and Private Key
  purestorage.flasharray.purefa_certs:
    state: import
    name: foo
    certificate: "{{lookup('file', 'example.crt') }}"
    key: "{{lookup('file', 'example.key') }}"
    passphrase: password
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
- [Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
- [Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
- [Communication](index.md#communication-for-purestorage-flasharray)
