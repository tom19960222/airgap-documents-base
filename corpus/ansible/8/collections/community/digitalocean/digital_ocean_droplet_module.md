---
collection: ansible
version: "8"
title: "community.digitalocean.digital_ocean_droplet module – Create and delete a DigitalOcean droplet"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/digitalocean/digital_ocean_droplet_module.html
fetched_at: 2026-07-28T01:42:59+00:00
---
# community.digitalocean.digital_ocean_droplet module – Create and delete a DigitalOcean droplet

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
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_droplet`.

- [Synopsis](digital_ocean_droplet_module.md#synopsis)
- [Parameters](digital_ocean_droplet_module.md#parameters)
- [Examples](digital_ocean_droplet_module.md#examples)
- [Return Values](digital_ocean_droplet_module.md#return-values)

## [Synopsis](digital_ocean_droplet_module.md#id1)

- Create and delete a droplet in DigitalOcean and optionally wait for it to be active.

## [Parameters](digital_ocean_droplet_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **backups**  boolean | Indicates whether automated backups should be enabled.  **Choices:**   - `false` ← (default) - `true` |
| **baseurl**  string | DigitalOcean API base url.  **Default:** `"https://api.digitalocean.com/v2"` |
| **firewall**  list / elements=string | Array of firewall names to apply to the Droplet.  Omitting a firewall name that is currently applied to a droplet will remove it. |
| **id**  aliases: droplet_id  integer | The Droplet ID you want to operate on. |
| **image**  aliases: image_id  string | This is the slug of the image you would like the Droplet created with. |
| **ipv6**  boolean | Enable IPv6 for the Droplet.  **Choices:**   - `false` ← (default) - `true` |
| **monitoring**  boolean | Indicates whether to install the DigitalOcean agent for monitoring.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string | This is the name of the Droplet.  Must be formatted by hostname rules. |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **private_networking**  boolean | Add an additional, private network interface to the Droplet (for inter-Droplet communication).  **Choices:**   - `false` ← (default) - `true` |
| **project_name**  aliases: project  string | Project to assign the resource to (project name, not UUID).  Defaults to the default project of the account (empty string).  Currently only supported when creating.  **Default:** `""` |
| **region**  aliases: region_id  string | This is the slug of the region you would like your Droplet to be created in. |
| **resize_disk**  boolean | Whether to increase disk size on resize.  Only consulted if the `unique_name` is `true`.  Droplet `size` must dictate an increase.  **Choices:**   - `false` ← (default) - `true` |
| **size**  aliases: size_id  string | This is the slug of the size you would like the Droplet created with.  Please see <https://slugs.do-api.dev/> for current slugs. |
| **sleep_interval**  integer | How long to `sleep` in between action and status checks.  Default is 10 seconds; this should be less than `wait_timeout` and nonzero.  **Default:** `10` |
| **ssh_keys**  list / elements=string | Array of SSH key fingerprints that you would like to be added to the Droplet. |
| **state**  string | Indicate desired state of the target.  `present` will create the named droplet; be mindful of the `unique_name` parameter.  `absent` will delete the named droplet, if it exists.  `active` will create the named droplet (unless it exists) and ensure that it is powered on.  `inactive` will create the named droplet (unless it exists) and ensure that it is powered off.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"active"` - `"inactive"` |
| **tags**  list / elements=string | A list of tag names as strings to apply to the Droplet after it is created.  Tag names can either be existing or new tags. |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  **Default:** `30` |
| **unique_name**  boolean | Require unique hostnames.  By default, DigitalOcean allows multiple hosts with the same name.  Setting this to `true` allows only one host per name.  Useful for idempotence.  **Choices:**   - `false` ← (default) - `true` |
| **user_data**  string | Opaque blob of data which is made available to the Droplet. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **volumes**  list / elements=string | A list including the unique string identifier for each Block Storage volume to be attached to the Droplet. |
| **vpc_uuid**  string  *added in community.digitalocean 0.1.0* | A string specifying the UUID of the VPC to which the Droplet will be assigned.  If excluded, the Droplet will be assigned to the account’s default VPC for the region. |
| **wait**  boolean | Wait for the Droplet to be active before returning.  If wait is `false` an IP address may not be returned.  **Choices:**   - `false` - `true` ← (default) |
| **wait_timeout**  integer | How long before `wait` gives up, in seconds, when creating a Droplet.  **Default:** `120` |

## [Examples](digital_ocean_droplet_module.md#id3)

```yaml+jinja
- name: Create a new Droplet
  community.digitalocean.digital_ocean_droplet:
    state: present
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
    name: mydroplet
    size: s-1vcpu-1gb
    region: sfo3
    image: ubuntu-20-04-x64
    wait_timeout: 500
    ssh_keys: [ .... ]
  register: my_droplet

- name: Show Droplet info
  ansible.builtin.debug:
    msg: |
      Droplet ID is {{ my_droplet.data.droplet.id }}
      First Public IPv4 is {{ (my_droplet.data.droplet.networks.v4 | selectattr('type', 'equalto', 'public')).0.ip_address | default('<none>', true) }}
      First Private IPv4 is {{ (my_droplet.data.droplet.networks.v4 | selectattr('type', 'equalto', 'private')).0.ip_address | default('<none>', true) }}

- name: Create a new Droplet (and assign to Project "test")
  community.digitalocean.digital_ocean_droplet:
    state: present
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
    name: mydroplet
    size: s-1vcpu-1gb
    region: sfo3
    image: ubuntu-20-04-x64
    wait_timeout: 500
    ssh_keys: [ .... ]
    project: test
  register: my_droplet

- name: Ensure a Droplet is present
  community.digitalocean.digital_ocean_droplet:
    state: present
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
    id: 123
    name: mydroplet
    size: s-1vcpu-1gb
    region: sfo3
    image: ubuntu-20-04-x64
    wait_timeout: 500

- name: Ensure a Droplet is present and has firewall rules applied
  community.digitalocean.digital_ocean_droplet:
    state: present
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
    id: 123
    name: mydroplet
    size: s-1vcpu-1gb
    region: sfo3
    image: ubuntu-20-04-x64
    firewall: ['myfirewall', 'anotherfirewall']
    wait_timeout: 500

- name: Ensure a Droplet is present with SSH keys installed
  community.digitalocean.digital_ocean_droplet:
    state: present
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
    id: 123
    name: mydroplet
    size: s-1vcpu-1gb
    region: sfo3
    ssh_keys: ['1534404', '1784768']
    image: ubuntu-20-04-x64
    wait_timeout: 500
```

## [Return Values](digital_ocean_droplet_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **assign_status**  string | Assignment status (ok, not_found, assigned, already_assigned, service_down)  **Returned:** changed  **Sample:** `"assigned"` |
| **data**  dictionary | a DigitalOcean Droplet  **Returned:** changed  **Sample:** `{"droplet": {"backup_ids": [], "created_at": "2014-11-14T16:36:31Z", "disk": 20, "features": ["virtio"], "id": 3164494, "image": {}, "kernel": {"id": 2233, "name": "Ubuntu 14.04 x64 vmlinuz-3.13.0-37-generic", "version": "3.13.0-37-generic"}, "locked": true, "memory": 512, "name": "example.com", "networks": {}, "region": {}, "size": {}, "size_slug": "512mb", "snapshot_ids": [], "status": "new", "tags": ["web"], "vcpus": 1, "volume_ids": []}, "ip_address": "104.248.118.172", "ipv6_address": "2604:a880:400:d1::90a:6001", "private_ipv4_address": "10.136.122.141"}` |
| **msg**  string | Informational or error message encountered during execution  **Returned:** changed  **Sample:** `"No project named test2 found"` |
| **resources**  dictionary | Resource assignment involved in project assignment  **Returned:** changed  **Sample:** `{"assigned_at": "2021-10-25T17:39:38Z", "links": {"self": "https://api.digitalocean.com/v2/droplets/3164494"}, "status": "assigned", "urn": "do:droplet:3164494"}` |

### Authors

- Gurchet Rai (@gurch101)
- Mark Mercado (@mamercad)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
