---
collection: ansible
version: "6"
title: "community.digitalocean.digital_ocean_droplet_info module – Gather information about DigitalOcean Droplets"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/digitalocean/digital_ocean_droplet_info_module.html
fetched_at: 2026-07-27T17:06:42+00:00
---
# community.digitalocean.digital_ocean_droplet_info module – Gather information about DigitalOcean Droplets

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
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_droplet_info`.

New in community.digitalocean 1.4.0

- [Synopsis](digital_ocean_droplet_info_module.md#synopsis)
- [Parameters](digital_ocean_droplet_info_module.md#parameters)
- [Examples](digital_ocean_droplet_info_module.md#examples)
- [Return Values](digital_ocean_droplet_info_module.md#return-values)

## [Synopsis](digital_ocean_droplet_info_module.md#id1)

- This module can be used to gather information about Droplets.

## [Parameters](digital_ocean_droplet_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **baseurl**  string | DigitalOcean API base url.  Default: `"https://api.digitalocean.com/v2"` |
| **id**  string | Droplet ID that can be used to identify and reference a droplet. |
| **name**  string | Droplet name that can be used to identify and reference a droplet. |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  Default: `30` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Examples](digital_ocean_droplet_info_module.md#id3)

```yaml+jinja
- name: Gather information about all droplets
  community.digitalocean.digital_ocean_droplet_info:
    oauth_token: "{{ oauth_token }}"

- name: Gather information about a specific droplet by name
  community.digitalocean.digital_ocean_droplet_info:
    oauth_token: "{{ oauth_token }}"
    name: my-droplet-name

- name: Gather information about a specific droplet by id
  community.digitalocean.digital_ocean_droplet_info:
    oauth_token: "{{ oauth_token }}"
    id: abc-123-d45

- name: Get information about all droplets to loop through
  community.digitalocean.digital_ocean_droplet_info:
    oauth_token: "{{ oauth_token }}"
  register: droplets

- name: Get number of droplets
  set_fact:
    droplet_count: "{{ droplets.data | length }}"
```

## [Return Values](digital_ocean_droplet_info_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  list / elements=dictionary | DigitalOcean droplet information  Returned: success  Sample: `[{"backup_ids": [], "created_at": "2021-04-07T00:44:53Z", "disk": 25, "features": ["private_networking"], "id": 123456789, "image": {"created_at": "2020-10-20T08:49:55Z", "description": "Ubuntu 18.04 x86 image", "distribution": "Ubuntu", "id": 987654321, "min_disk_size": 15, "name": "18.04 (LTS) x64", "public": false, "regions": [], "size_gigabytes": 0.34, "slug": null, "status": "retired", "tags": [], "type": "base"}, "kernel": null, "locked": false, "memory": 1024, "name": "my-droplet-01", "networks": {"v4": [{"gateway": "", "ip_address": "1.2.3.4", "netmask": "255.255.240.0", "type": "private"}, {"gateway": "5.6.7.8", "ip_address": "4.3.2.1", "netmask": "255.255.240.0", "type": "public"}], "v6": []}, "next_backup_window": null, "region": {"available": true, "features": ["backups", "ipv6", "metadata", "install_agent", "storage", "image_transfer"], "name": "New York 1", "sizes": ["s-1vcpu-1gb", "s-1vcpu-1gb-intel", "s-1vcpu-2gb", "s-1vcpu-2gb-intel", "s-2vcpu-2gb", "s-2vcpu-2gb-intel", "s-2vcpu-4gb", "s-2vcpu-4gb-intel", "s-4vcpu-8gb", "c-2", "c2-2vcpu-4gb", "s-4vcpu-8gb-intel", "g-2vcpu-8gb", "gd-2vcpu-8gb", "s-8vcpu-16gb", "m-2vcpu-16gb", "c-4", "c2-4vcpu-8gb", "s-8vcpu-16gb-intel", "m3-2vcpu-16gb", "g-4vcpu-16gb", "so-2vcpu-16gb", "m6-2vcpu-16gb", "gd-4vcpu-16gb", "so1_5-2vcpu-16gb", "m-4vcpu-32gb", "c-8", "c2-8vcpu-16gb", "m3-4vcpu-32gb", "g-8vcpu-32gb", "so-4vcpu-32gb", "m6-4vcpu-32gb", "gd-8vcpu-32gb", "so1_5-4vcpu-32gb", "m-8vcpu-64gb", "c-16", "c2-16vcpu-32gb", "m3-8vcpu-64gb", "g-16vcpu-64gb", "so-8vcpu-64gb", "m6-8vcpu-64gb", "gd-16vcpu-64gb", "so1_5-8vcpu-64gb", "m-16vcpu-128gb", "c-32", "c2-32vcpu-64gb", "m3-16vcpu-128gb", "m-24vcpu-192gb", "g-32vcpu-128gb", "so-16vcpu-128gb", "m6-16vcpu-128gb", "gd-32vcpu-128gb", "m3-24vcpu-192gb", "g-40vcpu-160gb", "so1_5-16vcpu-128gb", "m-32vcpu-256gb", "gd-40vcpu-160gb", "so-24vcpu-192gb", "m6-24vcpu-192gb", "m3-32vcpu-256gb", "so1_5-24vcpu-192gb", "so-32vcpu-256gb", "m6-32vcpu-256gb", "so1_5-32vcpu-256gb"], "slug": "nyc1"}, "size": {"available": true, "description": "Basic", "disk": 25, "memory": 1024, "price_hourly": 0.00744, "price_monthly": 5.0, "regions": ["ams2", "ams3", "blr1", "fra1", "lon1", "nyc1", "nyc2", "nyc3", "sfo1", "sfo3", "sgp1", "tor1"], "slug": "s-1vcpu-1gb", "transfer": 1.0, "vcpus": 1}, "size_slug": "s-1vcpu-1gb", "snapshot_ids": [], "status": "active", "tags": ["tag1"], "vcpus": 1, "volume_ids": [], "vpc_uuid": "123-abc-567a"}]` |

### Authors

- Tyler Auerbeck (@tylerauerbeck)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
