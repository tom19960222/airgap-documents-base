---
collection: ansible
version: "6"
title: "hetzner.hcloud.hcloud_certificate module – Create and manage certificates on the Hetzner Cloud."
source_url: https://docs.ansible.com/projects/ansible/6/collections/hetzner/hcloud/hcloud_certificate_module.html
fetched_at: 2026-07-27T17:49:36+00:00
---
# hetzner.hcloud.hcloud_certificate module – Create and manage certificates on the Hetzner Cloud.

> **Note:**
>
> This module is part of the [hetzner.hcloud collection](https://galaxy.ansible.com/hetzner/hcloud) (version 1.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install hetzner.hcloud`.
> You need further requirements to be able to use this module,
> see [Requirements](hcloud_certificate_module.md#ansible-collections-hetzner-hcloud-hcloud-certificate-module-requirements) for details.
>
> To use it in a playbook, specify: `hetzner.hcloud.hcloud_certificate`.

- [Synopsis](hcloud_certificate_module.md#synopsis)
- [Requirements](hcloud_certificate_module.md#requirements)
- [Parameters](hcloud_certificate_module.md#parameters)
- [See Also](hcloud_certificate_module.md#see-also)
- [Examples](hcloud_certificate_module.md#examples)
- [Return Values](hcloud_certificate_module.md#return-values)

## [Synopsis](hcloud_certificate_module.md#id1)

- Create, update and manage certificates on the Hetzner Cloud.

## [Requirements](hcloud_certificate_module.md#id2)

The below requirements are needed on the host that executes this module.

- hcloud-python >= 1.0.0

## [Parameters](hcloud_certificate_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string / required | This is the API Token for the Hetzner Cloud.  You can also set this option by using the environment variable HCLOUD_TOKEN |
| **certificate**  string | Certificate and chain in PEM format, in order so that each record directly certifies the one preceding.  Required if certificate does not exist. |
| **domain_names**  list / elements=string | Certificate key in PEM format.  Required if certificate does not exist.  Default: `[]` |
| **endpoint**  string | This is the API Endpoint for the Hetzner Cloud.  Default: `"https://api.hetzner.cloud/v1"` |
| **id**  integer | The ID of the Hetzner Cloud certificate to manage.  Only required if no certificate *name* is given |
| **labels**  dictionary | User-defined labels (key-value pairs) |
| **name**  string | The Name of the Hetzner Cloud certificate to manage.  Only required if no certificate *id* is given or a certificate does not exist. |
| **private_key**  string | Certificate key in PEM format.  Required if certificate does not exist. |
| **state**  string | State of the certificate.  Choices:   - `"absent"` - `"present"` ← (default) |
| **type**  string | Choose between uploading a Certificate in PEM format or requesting a managed Let’s Encrypt Certificate.  Choices:   - `"uploaded"` ← (default) - `"managed"` |

## [See Also](hcloud_certificate_module.md#id4)

> **See also:**
>
> [Documentation for Hetzner Cloud API](https://docs.hetzner.cloud/)
> :   Complete reference for the Hetzner Cloud API.

## [Examples](hcloud_certificate_module.md#id5)

```yaml+jinja
- name: Create a basic certificate
  hcloud_certificate:
    name: my-certificate
    certificate: "ssh-rsa AAAjjk76kgf...Xt"
    private_key: "ssh-rsa AAAjjk76kgf...Xt"
    state: present

- name: Create a certificate with labels
  hcloud_certificate:
    name: my-certificate
    certificate: "ssh-rsa AAAjjk76kgf...Xt"
    private_key: "ssh-rsa AAAjjk76kgf...Xt"
    labels:
        key: value
        mylabel: 123
    state: present

- name: Ensure the certificate is absent (remove if needed)
  hcloud_certificate:
    name: my-certificate
    state: absent
```

## [Return Values](hcloud_certificate_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hcloud_certificate**  complex | The certificate instance  Returned: Always |
| **certificate**  string | Certificate and chain in PEM format  Returned: always  Sample: `"-----BEGIN CERTIFICATE-----..."` |
| **domain_names**  dictionary | List of Domains and Subdomains covered by the Certificate  Returned: always |
| **fingerprint**  string | Fingerprint of the certificate  Returned: always  Sample: `"03:c7:55:9b:2a:d1:04:17:09:f6:d0:7f:18:34:63:d4:3e:5f"` |
| **id**  integer | Numeric identifier of the certificate  Returned: always  Sample: `1937415` |
| **labels**  dictionary | User-defined labels (key-value pairs)  Returned: always |
| **name**  string | Name of the certificate  Returned: always  Sample: `"my website cert"` |
| **not_valid_after**  string | Point in time when the Certificate stops being valid (in ISO-8601 format)  Returned: always |
| **not_valid_before**  string | Point in time when the Certificate becomes valid (in ISO-8601 format)  Returned: always |

### Authors

- Lukas Kaemmerling (@lkaemmerling)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
[Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)
