---
collection: ansible
version: "8"
title: "community.digitalocean.digital_ocean_account_info module – Gather information about DigitalOcean User account"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/digitalocean/digital_ocean_account_info_module.html
fetched_at: 2026-07-28T01:42:50+00:00
---
# community.digitalocean.digital_ocean_account_info module – Gather information about DigitalOcean User account

> **Note:**
>
> This module is part of the [community.digitalocean collection](https://galaxy.ansible.com/ui/repo/published/community/digitalocean/) (version 1.24.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.digitalocean`.
> You need further requirements to be able to use this module,
> see [Requirements](digital_ocean_account_info_module.md#ansible-collections-community-digitalocean-digital-ocean-account-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_account_info`.

- [Synopsis](digital_ocean_account_info_module.md#synopsis)
- [Requirements](digital_ocean_account_info_module.md#requirements)
- [Parameters](digital_ocean_account_info_module.md#parameters)
- [Examples](digital_ocean_account_info_module.md#examples)
- [Return Values](digital_ocean_account_info_module.md#return-values)

## [Synopsis](digital_ocean_account_info_module.md#id1)

- This module can be used to gather information about User account.
- This module was called `digital_ocean_account_facts` before Ansible 2.9. The usage did not change.

Aliases: digital_ocean_account_facts

## [Requirements](digital_ocean_account_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](digital_ocean_account_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **baseurl**  string | DigitalOcean API base url.  **Default:** `"https://api.digitalocean.com/v2"` |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  **Default:** `30` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](digital_ocean_account_info_module.md#id4)

```yaml+jinja
- name: Gather information about user account
  community.digitalocean.digital_ocean_account_info:
    oauth_token: "{{ oauth_token }}"
```

## [Return Values](digital_ocean_account_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | DigitalOcean account information  **Returned:** success  **Sample:** `{"droplet_limit": 10, "email": "testuser1@gmail.com", "email_verified": true, "floating_ip_limit": 3, "status": "active", "status_message": "", "uuid": "aaaaaaaaaaaaaa"}` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
