---
collection: ansible
version: "8"
title: "community.digitalocean.digital_ocean_floating_ip_info module – DigitalOcean Floating IPs information"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/digitalocean/digital_ocean_floating_ip_info_module.html
fetched_at: 2026-07-28T01:43:03+00:00
---
# community.digitalocean.digital_ocean_floating_ip_info module – DigitalOcean Floating IPs information

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
> see [Requirements](digital_ocean_floating_ip_info_module.md#ansible-collections-community-digitalocean-digital-ocean-floating-ip-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_floating_ip_info`.

- [Synopsis](digital_ocean_floating_ip_info_module.md#synopsis)
- [Requirements](digital_ocean_floating_ip_info_module.md#requirements)
- [Parameters](digital_ocean_floating_ip_info_module.md#parameters)
- [Notes](digital_ocean_floating_ip_info_module.md#notes)
- [Examples](digital_ocean_floating_ip_info_module.md#examples)
- [Return Values](digital_ocean_floating_ip_info_module.md#return-values)

## [Synopsis](digital_ocean_floating_ip_info_module.md#id1)

- This module can be used to fetch DigitalOcean Floating IPs information.
- This module was called `digital_ocean_floating_ip_facts` before Ansible 2.9. The usage did not change.

Aliases: digital_ocean_floating_ip_facts

## [Requirements](digital_ocean_floating_ip_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](digital_ocean_floating_ip_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **baseurl**  string | DigitalOcean API base url.  **Default:** `"https://api.digitalocean.com/v2"` |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  **Default:** `30` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](digital_ocean_floating_ip_info_module.md#id4)

> **Note:**
>
> - Version 2 of DigitalOcean API is used.

## [Examples](digital_ocean_floating_ip_info_module.md#id5)

```yaml+jinja
- name: "Gather information about all Floating IPs"
  community.digitalocean.digital_ocean_floating_ip_info:
  register: result

- name: "List of current floating ips"
  debug:
    var: result.floating_ips
```

## [Return Values](digital_ocean_floating_ip_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **floating_ips**  list / elements=string | a DigitalOcean Floating IP resource  **Returned:** success and no resource constraint  **Sample:** `[{"droplet": null, "ip": "45.55.96.47", "locked": false, "region": {"available": true, "features": ["private_networking", "backups", "ipv6", "metadata"], "name": "New York 3", "sizes": ["512mb", "1gb", "2gb", "4gb", "8gb", "16gb", "32gb", "48gb", "64gb"], "slug": "nyc3"}}]` |

### Authors

- Patrick Marques (@pmarques)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
