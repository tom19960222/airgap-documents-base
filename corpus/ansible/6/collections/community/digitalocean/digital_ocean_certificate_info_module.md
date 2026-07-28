---
collection: ansible
version: "6"
title: "community.digitalocean.digital_ocean_certificate_info module – Gather information about DigitalOcean certificates"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/digitalocean/digital_ocean_certificate_info_module.html
fetched_at: 2026-07-27T17:06:37+00:00
---
# community.digitalocean.digital_ocean_certificate_info module – Gather information about DigitalOcean certificates

> **Note:**
>
> This module is part of the [community.digitalocean collection](https://galaxy.ansible.com/community/digitalocean) (version 1.22.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.digitalocean`.
> You need further requirements to be able to use this module,
> see [Requirements](digital_ocean_certificate_info_module.md#ansible-collections-community-digitalocean-digital-ocean-certificate-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_certificate_info`.

- [Synopsis](digital_ocean_certificate_info_module.md#synopsis)
- [Requirements](digital_ocean_certificate_info_module.md#requirements)
- [Parameters](digital_ocean_certificate_info_module.md#parameters)
- [Examples](digital_ocean_certificate_info_module.md#examples)
- [Return Values](digital_ocean_certificate_info_module.md#return-values)

## [Synopsis](digital_ocean_certificate_info_module.md#id1)

- This module can be used to gather information about DigitalOcean provided certificates.
- This module was called `digital_ocean_certificate_facts` before Ansible 2.9. The usage did not change.

## [Requirements](digital_ocean_certificate_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](digital_ocean_certificate_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **baseurl**  string | DigitalOcean API base url.  Default: `"https://api.digitalocean.com/v2"` |
| **certificate_id**  string | Certificate ID that can be used to identify and reference a certificate. |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  Default: `30` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Examples](digital_ocean_certificate_info_module.md#id4)

```yaml+jinja
- name: Gather information about all certificates
  community.digitalocean.digital_ocean_certificate_info:
    oauth_token: "{{ oauth_token }}"

- name: Gather information about certificate with given id
  community.digitalocean.digital_ocean_certificate_info:
    oauth_token: "{{ oauth_token }}"
    certificate_id: "892071a0-bb95-49bc-8021-3afd67a210bf"

- name: Get not after information about certificate
  community.digitalocean.digital_ocean_certificate_info:
  register: resp_out
- set_fact:
    not_after_date: "{{ item.not_after }}"
  loop: "{{ resp_out.data | community.general.json_query(name) }}"
  vars:
    name: "[?name=='web-cert-01']"
- debug:
    var: not_after_date
```

## [Return Values](digital_ocean_certificate_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  list / elements=dictionary | DigitalOcean certificate information  Returned: success  Sample: `[{"created_at": "2017-02-08T16:02:37Z", "id": "892071a0-bb95-49bc-8021-3afd67a210bf", "name": "web-cert-01", "not_after": "2017-02-22T00:23:00Z", "sha1_fingerprint": "dfcc9f57d86bf58e321c2c6c31c7a971be244ac7"}]` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
