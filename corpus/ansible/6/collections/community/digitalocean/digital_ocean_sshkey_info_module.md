---
collection: ansible
version: "6"
title: "community.digitalocean.digital_ocean_sshkey_info module – Gather information about DigitalOcean SSH keys"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/digitalocean/digital_ocean_sshkey_info_module.html
fetched_at: 2026-07-27T17:06:56+00:00
---
# community.digitalocean.digital_ocean_sshkey_info module – Gather information about DigitalOcean SSH keys

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
> see [Requirements](digital_ocean_sshkey_info_module.md#ansible-collections-community-digitalocean-digital-ocean-sshkey-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_sshkey_info`.

- [Synopsis](digital_ocean_sshkey_info_module.md#synopsis)
- [Requirements](digital_ocean_sshkey_info_module.md#requirements)
- [Parameters](digital_ocean_sshkey_info_module.md#parameters)
- [Notes](digital_ocean_sshkey_info_module.md#notes)
- [Examples](digital_ocean_sshkey_info_module.md#examples)
- [Return Values](digital_ocean_sshkey_info_module.md#return-values)

## [Synopsis](digital_ocean_sshkey_info_module.md#id1)

- This module can be used to gather information about DigitalOcean SSH keys.
- This module replaces the `digital_ocean_sshkey_facts` module.

## [Requirements](digital_ocean_sshkey_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](digital_ocean_sshkey_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **baseurl**  string | DigitalOcean API base url.  Default: `"https://api.digitalocean.com/v2"` |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  Default: `30` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](digital_ocean_sshkey_info_module.md#id4)

> **Note:**
>
> - Version 2 of DigitalOcean API is used.

## [Examples](digital_ocean_sshkey_info_module.md#id5)

```yaml+jinja
- name: Gather information about DigitalOcean SSH keys
  community.digitalocean.digital_ocean_sshkey_info:
    oauth_token: "{{ my_do_key }}"
  register: ssh_keys

- name: Set facts based on the gathered information
  set_fact:
    pubkey: "{{ item.public_key }}"
  loop: "{{ ssh_keys.data | community.general.json_query(ssh_pubkey) }}"
  vars:
    ssh_pubkey: "[?name=='ansible_ctrl']"

- name: Print SSH public key
  debug:
    msg: "{{ pubkey }}"
```

## [Return Values](digital_ocean_sshkey_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  list / elements=dictionary | List of SSH keys on DigitalOcean  Returned: success and no resource constraint  Sample: `[{"fingerprint": "3b:16:bf:e4:8b:00:8b:b8:59:8c:a9:d3:f0:19:45:fa", "id": 512189, "name": "My SSH Public Key", "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAQQDDHr/jh2Jy4yALcK4JyWbVkPRaWmhck3IgCoeOO3z1e2dBowLh64QAM+Qb72pxekALga2oi4GvT+TlWNhzPH4V example"}]` |

### Authors

- Patrick Marques (@pmarques)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
