---
collection: ansible
version: "6"
title: "community.digitalocean.digital_ocean module – Create/delete a droplet/SSH_key in DigitalOcean"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/digitalocean/digital_ocean_module.html
fetched_at: 2026-07-27T17:06:32+00:00
---
# community.digitalocean.digital_ocean module – Create/delete a droplet/SSH_key in DigitalOcean

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
> see [Requirements](digital_ocean_module.md#ansible-collections-community-digitalocean-digital-ocean-module-requirements) for details.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean`.

- [DEPRECATED](digital_ocean_module.md#deprecated)
- [Synopsis](digital_ocean_module.md#synopsis)
- [Requirements](digital_ocean_module.md#requirements)
- [Parameters](digital_ocean_module.md#parameters)
- [Notes](digital_ocean_module.md#notes)
- [Examples](digital_ocean_module.md#examples)
- [Status](digital_ocean_module.md#status)

## [DEPRECATED](digital_ocean_module.md#id1)

Removed in:
:   version 2.0.0

Why:
:   Updated module to remove external dependency with increased functionality.

Alternative:
:   Use [community.digitalocean.digital_ocean_droplet](digital_ocean_droplet_module.md#ansible-collections-community-digitalocean-digital-ocean-droplet-module) instead.

## [Synopsis](digital_ocean_module.md#id2)

- Create/delete a droplet in DigitalOcean and optionally wait for it to be ‘running’, or deploy an SSH key.

## [Requirements](digital_ocean_module.md#id3)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- dopy

## [Parameters](digital_ocean_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **api_token**  aliases: API_TOKEN  string | DigitalOcean api token. |
| **backups_enabled**  boolean | Optional, Boolean, enables backups for your droplet.  Choices:   - `false` ← (default) - `true` |
| **command**  string | Which target you want to operate on.  Choices:   - `"droplet"` ← (default) - `"ssh"` |
| **id**  aliases: droplet_id  integer | Numeric, the droplet id you want to operate on. |
| **image_id**  string | This is the slug of the image you would like the droplet created with. |
| **ipv6**  boolean | Optional, Boolean, enable IPv6 for your droplet.  Choices:   - `false` ← (default) - `true` |
| **name**  string | String, this is the name of the droplet - must be formatted by hostname rules, or the name of a SSH key. |
| **private_networking**  boolean | Bool, add an additional, private network interface to droplet for inter-droplet communication.  Choices:   - `false` ← (default) - `true` |
| **region_id**  string | This is the slug of the region you would like your server to be created in. |
| **size_id**  string | This is the slug of the size you would like the droplet created with. |
| **ssh_key_ids**  list / elements=string | Optional, array of SSH key (numeric) ID that you would like to be added to the server. |
| **ssh_pub_key**  string | The public SSH key you want to add to your account. |
| **state**  string | Indicate desired state of the target.  Choices:   - `"present"` ← (default) - `"active"` - `"absent"` - `"deleted"` |
| **unique_name**  boolean | Bool, require unique hostnames. By default, DigitalOcean allows multiple hosts with the same name. Setting this to “yes” allows only one host per name. Useful for idempotence.  Choices:   - `false` ← (default) - `true` |
| **user_data**  string | opaque blob of data which is made available to the droplet |
| **virtio**  boolean | Bool, turn on virtio driver in droplet for improved network and storage I/O.  Choices:   - `false` - `true` ← (default) |
| **wait**  boolean | Wait for the droplet to be in state ‘running’ before returning. If wait is “no” an ip_address may not be returned.  Choices:   - `false` - `true` ← (default) |
| **wait_timeout**  integer | How long before wait gives up, in seconds.  Default: `300` |

## [Notes](digital_ocean_module.md#id5)

> **Note:**
>
> - Two environment variables can be used, DO_API_KEY and DO_API_TOKEN. They both refer to the v2 token.
> - As of Ansible 1.9.5 and 2.0, Version 2 of the DigitalOcean API is used, this removes `client_id` and `api_key` options in favor of `api_token`.
> - If you are running Ansible 1.9.4 or earlier you might not be able to use the included version of this module as the API version used has been retired. Upgrade Ansible or, if unable to, try downloading the latest version of this module from github and putting it into a ‘library’ directory.

## [Examples](digital_ocean_module.md#id6)

```yaml+jinja
# Ensure a SSH key is present
# If a key matches this name, will return the ssh key id and changed = False
# If no existing key matches this name, a new key is created, the ssh key id is returned and changed = False

- name: Ensure a SSH key is present
  community.digitalocean.digital_ocean:
    state: present
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
    command: ssh
    name: my_ssh_key
    ssh_pub_key: 'ssh-rsa AAAA...'

# Will return the droplet details including the droplet id (used for idempotence)
- name: Create a new Droplet
  community.digitalocean.digital_ocean:
    state: present
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
    command: droplet
    name: mydroplet
    size_id: 2gb
    region_id: ams2
    image_id: fedora-19-x64
    wait_timeout: 500
  register: my_droplet

- debug:
    msg: "ID is {{ my_droplet.droplet.id }}"

- debug:
    msg: "IP is {{ my_droplet.droplet.ip_address }}"

# Ensure a droplet is present
# If droplet id already exist, will return the droplet details and changed = False
# If no droplet matches the id, a new droplet will be created and the droplet details (including the new id) are returned, changed = True.

- name: Ensure a droplet is present
  community.digitalocean.digital_ocean:
    state: present
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
    command: droplet
    id: 123
    name: mydroplet
    size_id: 2gb
    region_id: ams2
    image_id: fedora-19-x64
    wait_timeout: 500

# Create a droplet with ssh key
# The ssh key id can be passed as argument at the creation of a droplet (see ssh_key_ids).
# Several keys can be added to ssh_key_ids as id1,id2,id3
# The keys are used to connect as root to the droplet.

- name: Create a droplet with ssh key
  community.digitalocean.digital_ocean:
    state: present
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
    ssh_key_ids: 123,456
    name: mydroplet
    size_id: 2gb
    region_id: ams2
    image_id: fedora-19-x64
```

## [Status](digital_ocean_module.md#id7)

- This module will be removed in version 2.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](digital_ocean_module.md#deprecated).

### Authors

- Vincent Viallet (@zbal)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
