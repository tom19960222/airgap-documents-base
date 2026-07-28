---
collection: ansible
version: "8"
title: "community.general.rax module – Create / delete an instance in Rackspace Public Cloud"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/rax_module.html
fetched_at: 2026-07-28T01:49:30+00:00
---
# community.general.rax module – Create / delete an instance in Rackspace Public Cloud

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](rax_module.md#ansible-collections-community-general-rax-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.rax`.

- [DEPRECATED](rax_module.md#deprecated)
- [Synopsis](rax_module.md#synopsis)
- [Requirements](rax_module.md#requirements)
- [Parameters](rax_module.md#parameters)
- [Attributes](rax_module.md#attributes)
- [Notes](rax_module.md#notes)
- [Examples](rax_module.md#examples)
- [Status](rax_module.md#status)

## [DEPRECATED](rax_module.md#id1)

Removed in:
:   version 9.0.0

Why:
:   This module relies on the deprecated package pyrax.

Alternative:
:   Use the Openstack modules instead.

## [Synopsis](rax_module.md#id2)

- creates / deletes a Rackspace Public Cloud instance and optionally waits for it to be ‘running’.

Aliases: cloud.rackspace.rax

## [Requirements](rax_module.md#id3)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- pyrax

## [Parameters](rax_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **api_key**  aliases: password  string | Rackspace API key, overrides `credentials`. |
| **auth_endpoint**  string | The URI of the authentication service.  If not specified will be set to <https://identity.api.rackspacecloud.com/v2.0/> |
| **auto_increment**  boolean | Whether or not to increment a single number with the name of the created servers. Only applicable when used with the `group` attribute or meta key.  **Choices:**   - `false` - `true` ← (default) |
| **boot_from_volume**  boolean | Whether or not to boot the instance from a Cloud Block Storage volume. If `true` and `image` is specified a new volume will be created at boot time. `boot_volume_size` is required with `image` to create a new volume at boot time.  **Choices:**   - `false` ← (default) - `true` |
| **boot_volume**  string | Cloud Block Storage ID or Name to use as the boot volume of the instance |
| **boot_volume_size**  integer | Size of the volume to create in Gigabytes. This is only required with `image` and `boot_from_volume`.  **Default:** `100` |
| **boot_volume_terminate**  boolean | Whether the `boot_volume` or newly created volume from `image` will be terminated when the server is terminated  **Choices:**   - `false` ← (default) - `true` |
| **config_drive**  boolean | Attach read-only configuration drive to server as label config-2  **Choices:**   - `false` ← (default) - `true` |
| **count**  integer | number of instances to launch  **Default:** `1` |
| **count_offset**  integer | number count to start at  **Default:** `1` |
| **credentials**  aliases: creds_file  path | File to find the Rackspace credentials in. Ignored if `api_key` and `username` are provided. |
| **disk_config**  string | Disk partitioning strategy  If not specified it will assume the value `auto`.  **Choices:**   - `"auto"` - `"manual"` |
| **env**  string | Environment as configured in `~/.pyrax.cfg`, see <https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration>. |
| **exact_count**  boolean | Explicitly ensure an exact count of instances, used with state=active/present. If specified as `true` and `count` is less than the servers matched, servers will be deleted to match the count. If the number of matched servers is fewer than specified in `count` additional servers will be added.  **Choices:**   - `false` ← (default) - `true` |
| **extra_client_args**  dictionary | A hash of key/value pairs to be used when creating the cloudservers client. This is considered an advanced option, use it wisely and with caution.  **Default:** `{}` |
| **extra_create_args**  dictionary | A hash of key/value pairs to be used when creating a new server. This is considered an advanced option, use it wisely and with caution.  **Default:** `{}` |
| **files**  dictionary | Files to insert into the instance. remotefilename:localcontent  **Default:** `{}` |
| **flavor**  string | flavor to use for the instance |
| **group**  string | host group to assign to server, is also used for idempotent operations to ensure a specific number of instances |
| **identity_type**  string | Authentication mechanism to use, such as rackspace or keystone.  **Default:** `"rackspace"` |
| **image**  string | image to use for the instance. Can be an `id`, `human_id` or `name`. With `boot_from_volume`, a Cloud Block Storage volume will be created with this image |
| **instance_ids**  list / elements=string | list of instance ids, currently only used when state=’absent’ to remove instances |
| **key_name**  aliases: keypair  string | key pair to use on the instance |
| **meta**  dictionary | A hash of metadata to associate with the instance  **Default:** `{}` |
| **name**  string | Name to give the instance |
| **networks**  list / elements=string | The network to attach to the instances. If specified, you must include ALL networks including the public and private interfaces. Can be `id` or `label`.  **Default:** `["public", "private"]` |
| **region**  string | Region to create an instance in. |
| **state**  string | Indicate desired state of the resource  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tenant_id**  string | The tenant ID used for authentication. |
| **tenant_name**  string | The tenant name used for authentication. |
| **user_data**  string | Data to be uploaded to the servers config drive. This option implies `config_drive`. Can be a file path or a string |
| **username**  string | Rackspace username, overrides `credentials`. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to require SSL validation of API endpoints.  **Choices:**   - `false` - `true` |
| **wait**  boolean | wait for the instance to be in state ‘running’ before returning  **Choices:**   - `false` ← (default) - `true` |
| **wait_timeout**  integer | how long before wait gives up, in seconds  **Default:** `300` |

## [Attributes](rax_module.md#id5)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](rax_module.md#id6)

> **Note:**
>
> - `exact_count` can be “destructive” if the number of running servers in the `group` is larger than that specified in `count`. In such a case, the `state` is effectively set to `absent` and the extra servers are deleted. In the case of deletion, the returned data structure will have `action` set to `delete`, and the oldest servers in the group will be deleted.
> - The following environment variables can be used, `RAX_USERNAME`, `RAX_API_KEY`, `RAX_CREDS_FILE`, `RAX_CREDENTIALS`, `RAX_REGION`.
> - `RAX_CREDENTIALS` and `RAX_CREDS_FILE` points to a credentials file appropriate for pyrax. See <https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#authenticating>
> - `RAX_USERNAME` and `RAX_API_KEY` obviate the use of a credentials file
> - `RAX_REGION` defines a Rackspace Public Cloud region (DFW, ORD, LON, …)

## [Examples](rax_module.md#id7)

```yaml+jinja
- name: Build a Cloud Server
  gather_facts: false
  tasks:
    - name: Server build request
      local_action:
        module: rax
        credentials: ~/.raxpub
        name: rax-test1
        flavor: 5
        image: b11d9567-e412-4255-96b9-bd63ab23bcfe
        key_name: my_rackspace_key
        files:
          /root/test.txt: /home/localuser/test.txt
        wait: true
        state: present
        networks:
          - private
          - public
      register: rax

- name: Build an exact count of cloud servers with incremented names
  hosts: local
  gather_facts: false
  tasks:
    - name: Server build requests
      local_action:
        module: rax
        credentials: ~/.raxpub
        name: test%03d.example.org
        flavor: performance1-1
        image: ubuntu-1204-lts-precise-pangolin
        state: present
        count: 10
        count_offset: 10
        exact_count: true
        group: test
        wait: true
      register: rax
```

## [Status](rax_module.md#id8)

- This module will be removed in version 9.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](rax_module.md#deprecated).

### Authors

- Jesse Keating (@omgjlk)
- Matt Martz (@sivel)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
