---
collection: ansible
version: "8"
title: "community.digitalocean.digital_ocean_domain module – Create/delete a DNS domain in DigitalOcean"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/digitalocean/digital_ocean_domain_module.html
fetched_at: 2026-07-28T01:42:57+00:00
---
# community.digitalocean.digital_ocean_domain module – Create/delete a DNS domain in DigitalOcean

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
> see [Requirements](digital_ocean_domain_module.md#ansible-collections-community-digitalocean-digital-ocean-domain-module-requirements) for details.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_domain`.

- [Synopsis](digital_ocean_domain_module.md#synopsis)
- [Requirements](digital_ocean_domain_module.md#requirements)
- [Parameters](digital_ocean_domain_module.md#parameters)
- [Notes](digital_ocean_domain_module.md#notes)
- [Examples](digital_ocean_domain_module.md#examples)

## [Synopsis](digital_ocean_domain_module.md#id1)

- Create/delete a DNS domain in DigitalOcean.

## [Requirements](digital_ocean_domain_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](digital_ocean_domain_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **baseurl**  string | DigitalOcean API base url.  **Default:** `"https://api.digitalocean.com/v2"` |
| **id**  aliases: droplet_id  integer | The droplet id you want to operate on. |
| **ip**  aliases: ip4, ipv4  string | An ‘A’ record for ‘@’ ($ORIGIN) will be created with the value ‘ip’. ‘ip’ is an IP version 4 address. |
| **ip6**  aliases: ipv6  string | An ‘AAAA’ record for ‘@’ ($ORIGIN) will be created with the value ‘ip6’. ‘ip6’ is an IP version 6 address. |
| **name**  string | The name of the droplet - must be formatted by hostname rules, or the name of a SSH key, or the name of a domain. |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **project_name**  aliases: project  string | Project to assign the resource to (project name, not UUID).  Defaults to the default project of the account (empty string).  Currently only supported when creating domains.  **Default:** `""` |
| **state**  string | Indicate desired state of the target.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  **Default:** `30` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](digital_ocean_domain_module.md#id4)

> **Note:**
>
> - Environment variables DO_OAUTH_TOKEN can be used for the oauth_token.
> - As of Ansible 1.9.5 and 2.0, Version 2 of the DigitalOcean API is used, this removes `client_id` and `api_key` options in favor of `oauth_token`.
> - If you are running Ansible 1.9.4 or earlier you might not be able to use the included version of this module as the API version used has been retired.

## [Examples](digital_ocean_domain_module.md#id5)

```yaml+jinja
- name: Create a domain
  community.digitalocean.digital_ocean_domain:
    state: present
    name: my.digitalocean.domain
    ip: 127.0.0.1

- name: Create a domain (and associate to Project "test")
  community.digitalocean.digital_ocean_domain:
    state: present
    name: my.digitalocean.domain
    ip: 127.0.0.1
    project: test

# Create a droplet and corresponding domain
- name: Create a droplet
  community.digitalocean.digital_ocean:
    state: present
    name: test_droplet
    size_id: 1gb
    region_id: sgp1
    image_id: ubuntu-14-04-x64
  register: test_droplet

- name: Create a corresponding domain
  community.digitalocean.digital_ocean_domain:
    state: present
    name: "{{ test_droplet.droplet.name }}.my.domain"
    ip: "{{ test_droplet.droplet.ip_address }}"
```

### Authors

- Michael Gregson (@mgregson)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
