---
collection: ansible
version: "8"
title: "community.digitalocean.digital_ocean_floating_ip module – Manage DigitalOcean Floating IPs"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/digitalocean/digital_ocean_floating_ip_module.html
fetched_at: 2026-07-28T01:43:02+00:00
---
# community.digitalocean.digital_ocean_floating_ip module – Manage DigitalOcean Floating IPs

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
> see [Requirements](digital_ocean_floating_ip_module.md#ansible-collections-community-digitalocean-digital-ocean-floating-ip-module-requirements) for details.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_floating_ip`.

- [Synopsis](digital_ocean_floating_ip_module.md#synopsis)
- [Requirements](digital_ocean_floating_ip_module.md#requirements)
- [Parameters](digital_ocean_floating_ip_module.md#parameters)
- [Notes](digital_ocean_floating_ip_module.md#notes)
- [Examples](digital_ocean_floating_ip_module.md#examples)
- [Return Values](digital_ocean_floating_ip_module.md#return-values)

## [Synopsis](digital_ocean_floating_ip_module.md#id1)

- Create/delete/assign a floating IP.

## [Requirements](digital_ocean_floating_ip_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](digital_ocean_floating_ip_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **droplet_id**  string | The Droplet that the Floating IP has been assigned to. |
| **ip**  aliases: id  string | Public IP address of the Floating IP. Used to remove an IP |
| **oauth_token**  string / required | DigitalOcean OAuth token. |
| **project_name**  aliases: project  string | Project to assign the resource to (project name, not UUID).  Defaults to the default project of the account (empty string).  Currently only supported when creating.  **Default:** `""` |
| **region**  string | The region that the Floating IP is reserved to. |
| **state**  string | Indicate desired state of the target.  If `state=present` Create (and optionally attach) floating IP  If `state=absent` Delete floating IP  If `state=attached` attach floating IP to a droplet  If `state=detached` detach floating IP from a droplet  **Choices:**   - `"present"` ← (default) - `"absent"` - `"attached"` - `"detached"` |
| **timeout**  integer | Floating IP creation timeout.  **Default:** `30` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](digital_ocean_floating_ip_module.md#id4)

> **Note:**
>
> - Version 2 of DigitalOcean API is used.

## [Examples](digital_ocean_floating_ip_module.md#id5)

```yaml+jinja
- name: "Create a Floating IP in region lon1"
  community.digitalocean.digital_ocean_floating_ip:
    state: present
    region: lon1

- name: Create a Floating IP in region lon1 (and assign to Project "test")
  community.digitalocean.digital_ocean_floating_ip:
    state: present
    region: lon1
    project: test

- name: "Create a Floating IP assigned to Droplet ID 123456"
  community.digitalocean.digital_ocean_floating_ip:
    state: present
    droplet_id: 123456

- name: "Attach an existing Floating IP of 1.2.3.4 to Droplet ID 123456"
  community.digitalocean.digital_ocean_floating_ip:
    state: attached
    ip: "1.2.3.4"
    droplet_id: 123456

- name: "Detach an existing Floating IP of 1.2.3.4 from its Droplet"
  community.digitalocean.digital_ocean_floating_ip:
    state: detached
    ip: "1.2.3.4"

- name: "Delete a Floating IP with ip 1.2.3.4"
  community.digitalocean.digital_ocean_floating_ip:
    state: absent
    ip: "1.2.3.4"
```

## [Return Values](digital_ocean_floating_ip_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **assign_status**  string | Assignment status (ok, not_found, assigned, already_assigned, service_down)  **Returned:** changed  **Sample:** `"assigned"` |
| **data**  dictionary | a DigitalOcean Floating IP resource  **Returned:** success and no resource constraint  **Sample:** `{"action": {"completed_at": null, "id": 68212728, "region": {"available": true, "features": ["private_networking", "backups", "ipv6", "metadata"], "name": "New York 3", "sizes": ["512mb,", "1gb,", "2gb,", "4gb,", "8gb,", "16gb,", "32gb,", "48gb,", "64gb"], "slug": "nyc3"}, "region_slug": "nyc3", "resource_id": 758603823, "resource_type": "floating_ip", "started_at": "2015-10-15T17:45:44Z", "status": "in-progress", "type": "assign_ip"}}` |
| **msg**  string | Informational or error message encountered during execution  **Returned:** changed  **Sample:** `"No project named test2 found"` |
| **resources**  dictionary | Resource assignment involved in project assignment  **Returned:** changed  **Sample:** `{"assigned_at": "2021-10-25T17:39:38Z", "links": {"self": "https://api.digitalocean.com/v2/floating_ips/157.230.64.107"}, "status": "assigned", "urn": "do:floatingip:157.230.64.107"}` |

### Authors

- Patrick Marques (@pmarques)
- Daniel George (@danxg87)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
