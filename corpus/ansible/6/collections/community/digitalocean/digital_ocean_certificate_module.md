---
collection: ansible
version: "6"
title: "community.digitalocean.digital_ocean_certificate module – Manage certificates in DigitalOcean"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/digitalocean/digital_ocean_certificate_module.html
fetched_at: 2026-07-27T17:06:36+00:00
---
# community.digitalocean.digital_ocean_certificate module – Manage certificates in DigitalOcean

> **Note:**
>
> This module is part of the [community.digitalocean collection](https://galaxy.ansible.com/community/digitalocean) (version 1.22.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.digitalocean`.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_certificate`.

- [Synopsis](digital_ocean_certificate_module.md#synopsis)
- [Parameters](digital_ocean_certificate_module.md#parameters)
- [Notes](digital_ocean_certificate_module.md#notes)
- [Examples](digital_ocean_certificate_module.md#examples)

## [Synopsis](digital_ocean_certificate_module.md#id1)

- Create, Retrieve and remove certificates DigitalOcean.

## [Parameters](digital_ocean_certificate_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **baseurl**  string | DigitalOcean API base url.  Default: `"https://api.digitalocean.com/v2"` |
| **certificate_chain**  string | The full PEM-formatted trust chain between the certificate authority’s certificate and your domain’s SSL certificate. |
| **leaf_certificate**  string | A PEM-formatted public SSL Certificate. |
| **name**  string / required | The name of the certificate. |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **private_key**  string | A PEM-formatted private key content of SSL Certificate. |
| **state**  string | Whether the certificate should be present or absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  Default: `30` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](digital_ocean_certificate_module.md#id3)

> **Note:**
>
> - Two environment variables can be used, DO_API_KEY, DO_OAUTH_TOKEN and DO_API_TOKEN. They both refer to the v2 token.

## [Examples](digital_ocean_certificate_module.md#id4)

```yaml+jinja
- name: Create a certificate
  community.digitalocean.digital_ocean_certificate:
    name: production
    state: present
    private_key: "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkM8OI7pRpgyj1I\n-----END PRIVATE KEY-----"
    leaf_certificate: "-----BEGIN CERTIFICATE-----\nMIIFDmg2Iaw==\n-----END CERTIFICATE-----"
    oauth_token: b7d03a6947b217efb6f3ec3bd365652

- name: Create a certificate using file lookup plugin
  community.digitalocean.digital_ocean_certificate:
    name: production
    state: present
    private_key: "{{ lookup('file', 'test.key') }}"
    leaf_certificate: "{{ lookup('file', 'test.cert') }}"
    oauth_token: "{{ oauth_token }}"

- name: Create a certificate with trust chain
  community.digitalocean.digital_ocean_certificate:
    name: production
    state: present
    private_key: "{{ lookup('file', 'test.key') }}"
    leaf_certificate: "{{ lookup('file', 'test.cert') }}"
    certificate_chain: "{{ lookup('file', 'chain.cert') }}"
    oauth_token: "{{ oauth_token }}"

- name: Remove a certificate
  community.digitalocean.digital_ocean_certificate:
    name: production
    state: absent
    oauth_token: "{{ oauth_token }}"
```

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
