---
collection: ansible
version: "8"
title: "community.digitalocean.digital_ocean_balance_info module – Display DigitalOcean customer balance"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/digitalocean/digital_ocean_balance_info_module.html
fetched_at: 2026-07-28T01:42:51+00:00
---
# community.digitalocean.digital_ocean_balance_info module – Display DigitalOcean customer balance

> **Note:**
>
> This module is part of the [community.digitalocean collection](https://galaxy.ansible.com/ui/repo/published/community/digitalocean/) (version 1.24.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.digitalocean`.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_balance_info`.

New in community.digitalocean 1.2.0

- [Synopsis](digital_ocean_balance_info_module.md#synopsis)
- [Parameters](digital_ocean_balance_info_module.md#parameters)
- [Examples](digital_ocean_balance_info_module.md#examples)
- [Return Values](digital_ocean_balance_info_module.md#return-values)

## [Synopsis](digital_ocean_balance_info_module.md#id1)

- This module can be used to display the DigitalOcean customer balance.

## [Parameters](digital_ocean_balance_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **baseurl**  string | DigitalOcean API base url.  **Default:** `"https://api.digitalocean.com/v2"` |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  **Default:** `30` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](digital_ocean_balance_info_module.md#id3)

```yaml+jinja
- name: Display DigitalOcean customer balance
  community.digitalocean.digital_ocean_balance_info:
    oauth_token: "{{ oauth_token }}"
```

## [Return Values](digital_ocean_balance_info_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | DigitalOcean customer balance  **Returned:** success  **Sample:** `{"account_balance": "-27.52", "generated_at": "2021-04-11T05:08:24Z", "month_to_date_balance": "-27.40", "month_to_date_usage": "0.00"}` |

### Authors

- Mark Mercado (@mamercad)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
