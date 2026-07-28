---
collection: ansible
version: "6"
title: "community.digitalocean.digital_ocean_sshkey module – Manage DigitalOcean SSH keys"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/digitalocean/digital_ocean_sshkey_module.html
fetched_at: 2026-07-27T17:06:56+00:00
---
# community.digitalocean.digital_ocean_sshkey module – Manage DigitalOcean SSH keys

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
> see [Requirements](digital_ocean_sshkey_module.md#ansible-collections-community-digitalocean-digital-ocean-sshkey-module-requirements) for details.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_sshkey`.

- [Synopsis](digital_ocean_sshkey_module.md#synopsis)
- [Requirements](digital_ocean_sshkey_module.md#requirements)
- [Parameters](digital_ocean_sshkey_module.md#parameters)
- [Notes](digital_ocean_sshkey_module.md#notes)
- [Examples](digital_ocean_sshkey_module.md#examples)
- [Return Values](digital_ocean_sshkey_module.md#return-values)

## [Synopsis](digital_ocean_sshkey_module.md#id1)

- Create/delete DigitalOcean SSH keys.

## [Requirements](digital_ocean_sshkey_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](digital_ocean_sshkey_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **baseurl**  string | DigitalOcean API base url.  Default: `"https://api.digitalocean.com/v2"` |
| **fingerprint**  aliases: id  string | This is a unique identifier for the SSH key used to delete a key |
| **name**  string | The name for the SSH key |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **ssh_pub_key**  string | The Public SSH key to add. |
| **state**  string | Indicate desired state of the target.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  Default: `30` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](digital_ocean_sshkey_module.md#id4)

> **Note:**
>
> - Version 2 of DigitalOcean API is used.

## [Examples](digital_ocean_sshkey_module.md#id5)

```yaml+jinja
- name: "Create ssh key"
  community.digitalocean.digital_ocean_sshkey:
    oauth_token: "{{ oauth_token }}"
    name: "My SSH Public Key"
    ssh_pub_key: "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAQQDDHr/jh2Jy4yALcK4JyWbVkPRaWmhck3IgCoeOO3z1e2dBowLh64QAM+Qb72pxekALga2oi4GvT+TlWNhzPH4V example"
    state: present
  register: result

- name: "Delete ssh key"
  community.digitalocean.digital_ocean_sshkey:
    oauth_token: "{{ oauth_token }}"
    state: "absent"
    fingerprint: "3b:16:bf:e4:8b:00:8b:b8:59:8c:a9:d3:f0:19:45:fa"
```

## [Return Values](digital_ocean_sshkey_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | This is only present when `state=present`  Returned: when `state=present`  Sample: `{"ssh_key": {"fingerprint": "3b:16:bf:e4:8b:00:8b:b8:59:8c:a9:d3:f0:19:45:fa", "id": 512189, "name": "My SSH Public Key", "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAQQDDHr/jh2Jy4yALcK4JyWbVkPRaWmhck3IgCoeOO3z1e2dBowLh64QAM+Qb72pxekALga2oi4GvT+TlWNhzPH4V example"}}` |

### Authors

- Patrick Marques (@pmarques)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
