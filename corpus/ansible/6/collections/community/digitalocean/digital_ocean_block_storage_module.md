---
collection: ansible
version: "6"
title: "community.digitalocean.digital_ocean_block_storage module – Create/destroy or attach/detach Block Storage volumes in DigitalOcean"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/digitalocean/digital_ocean_block_storage_module.html
fetched_at: 2026-07-27T17:06:34+00:00
---
# community.digitalocean.digital_ocean_block_storage module – Create/destroy or attach/detach Block Storage volumes in DigitalOcean

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
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_block_storage`.

- [Synopsis](digital_ocean_block_storage_module.md#synopsis)
- [Parameters](digital_ocean_block_storage_module.md#parameters)
- [Notes](digital_ocean_block_storage_module.md#notes)
- [Examples](digital_ocean_block_storage_module.md#examples)
- [Return Values](digital_ocean_block_storage_module.md#return-values)

## [Synopsis](digital_ocean_block_storage_module.md#id1)

- Create/destroy Block Storage volume in DigitalOcean, or attach/detach Block Storage volume to a droplet.

## [Parameters](digital_ocean_block_storage_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **baseurl**  string | DigitalOcean API base url.  Default: `"https://api.digitalocean.com/v2"` |
| **block_size**  integer | The size of the Block Storage volume in gigabytes.  Required when *command=create* and *state=present*.  If snapshot_id is included, this will be ignored.  If block_size > current size of the volume, the volume is resized. |
| **command**  string / required | Which operation do you want to perform.  Choices:   - `"create"` - `"attach"` |
| **description**  string | Description of the Block Storage volume. |
| **droplet_id**  integer | The droplet id you want to operate on.  Required when *command=attach*. |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **project_name**  aliases: project  string | Project to assign the resource to (project name, not UUID).  Defaults to the default project of the account (empty string).  Currently only supported when `command=create`.  Default: `""` |
| **region**  string | The slug of the region where your Block Storage volume should be located in.  If *snapshot_id* is included, this will be ignored. |
| **snapshot_id**  string | The snapshot id you would like the Block Storage volume created with.  If included, *region* and *block_size* will be ignored and changed to `null`. |
| **state**  string / required | Indicate desired state of the target.  Choices:   - `"present"` - `"absent"` |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  Default: `30` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **volume_name**  string / required | The name of the Block Storage volume. |

## [Notes](digital_ocean_block_storage_module.md#id3)

> **Note:**
>
> - Two environment variables can be used, DO_API_KEY and DO_API_TOKEN. They both refer to the v2 token.
> - If snapshot_id is used, region and block_size will be ignored and changed to null.

## [Examples](digital_ocean_block_storage_module.md#id4)

```yaml+jinja
- name: Create new Block Storage
  community.digitalocean.digital_ocean_block_storage:
    state: present
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
    command: create
    region: nyc1
    block_size: 10
    volume_name: nyc1-block-storage

- name: Create new Block Storage (and assign to Project "test")
  community.digitalocean.digital_ocean_block_storage:
    state: present
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
    command: create
    region: nyc1
    block_size: 10
    volume_name: nyc1-block-storage
    project_name: test

- name: Resize an existing Block Storage
  community.digitalocean.digital_ocean_block_storage:
    state: present
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
    command: create
    region: nyc1
    block_size: 20
    volume_name: nyc1-block-storage

- name: Delete Block Storage
  community.digitalocean.digital_ocean_block_storage:
    state: absent
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
    command: create
    region: nyc1
    volume_name: nyc1-block-storage

- name: Attach Block Storage to a Droplet
  community.digitalocean.digital_ocean_block_storage:
    state: present
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
    command: attach
    volume_name: nyc1-block-storage
    region: nyc1
    droplet_id: <ID>

- name: Detach Block Storage from a Droplet
  community.digitalocean.digital_ocean_block_storage:
    state: absent
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
    command: attach
    volume_name: nyc1-block-storage
    region: nyc1
    droplet_id: <ID>
```

## [Return Values](digital_ocean_block_storage_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **assign_status**  string | Assignment status (ok, not_found, assigned, already_assigned, service_down)  Returned: changed  Sample: `"assigned"` |
| **id**  string | Unique identifier of a Block Storage volume returned during creation.  Returned: changed  Sample: `"69b25d9a-494c-12e6-a5af-001f53126b44"` |
| **msg**  string | Informational or error message encountered during execution  Returned: changed  Sample: `"No project named test2 found"` |
| **resources**  dictionary | Resource assignment involved in project assignment  Returned: changed  Sample: `{"assigned_at": "2021-10-25T17:39:38Z", "links": {"self": "https://api.digitalocean.com/v2/volumes/8691c49e-35ba-11ec-9406-0a58ac1472b9"}, "status": "assigned", "urn": "do:volume:8691c49e-35ba-11ec-9406-0a58ac1472b9"}` |

### Authors

- Harnek Sidhu (@harneksidhu)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
