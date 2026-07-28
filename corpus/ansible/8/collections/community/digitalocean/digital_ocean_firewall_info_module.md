---
collection: ansible
version: "8"
title: "community.digitalocean.digital_ocean_firewall_info module – Gather information about DigitalOcean firewalls"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/digitalocean/digital_ocean_firewall_info_module.html
fetched_at: 2026-07-28T01:43:02+00:00
---
# community.digitalocean.digital_ocean_firewall_info module – Gather information about DigitalOcean firewalls

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
> see [Requirements](digital_ocean_firewall_info_module.md#ansible-collections-community-digitalocean-digital-ocean-firewall-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_firewall_info`.

- [Synopsis](digital_ocean_firewall_info_module.md#synopsis)
- [Requirements](digital_ocean_firewall_info_module.md#requirements)
- [Parameters](digital_ocean_firewall_info_module.md#parameters)
- [Examples](digital_ocean_firewall_info_module.md#examples)
- [Return Values](digital_ocean_firewall_info_module.md#return-values)

## [Synopsis](digital_ocean_firewall_info_module.md#id1)

- This module can be used to gather information about DigitalOcean firewalls.
- This module was called `digital_ocean_firewall_facts` before Ansible 2.9. The usage did not change.

Aliases: digital_ocean_firewall_facts

## [Requirements](digital_ocean_firewall_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](digital_ocean_firewall_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **baseurl**  string | DigitalOcean API base url.  **Default:** `"https://api.digitalocean.com/v2"` |
| **name**  string | Firewall rule name that can be used to identify and reference a specific firewall rule. |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  **Default:** `30` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](digital_ocean_firewall_info_module.md#id4)

```yaml+jinja
- name: Gather information about all firewalls
  community.digitalocean.digital_ocean_firewall_info:
    oauth_token: "{{ oauth_token }}"

- name: Gather information about a specific firewall by name
  community.digitalocean.digital_ocean_firewall_info:
    oauth_token: "{{ oauth_token }}"
    name: "firewall_name"

- name: Gather information from a firewall rule
  community.digitalocean.digital_ocean_firewall_info:
    name: SSH
  register: resp_out

- set_fact:
    firewall_id: "{{ resp_out.data.id }}"

- debug:
    msg: "{{ firewall_id }}"
```

## [Return Values](digital_ocean_firewall_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  list / elements=dictionary | DigitalOcean firewall information  **Returned:** success  **Sample:** `[{"created_at": "2018-01-15T07:04:25Z", "droplet_ids": [87426985], "id": "435tbg678-1db53-32b6-t543-28322569t252", "inbound_rules": [{"ports": "9100", "protocol": "tcp", "sources": {"addresses": ["1.1.1.1"]}}], "name": "metrics", "outbound_rules": [], "pending_changes": [], "status": "succeeded", "tags": []}]` |

### Authors

- Anthony Bond (@BondAnthony)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
