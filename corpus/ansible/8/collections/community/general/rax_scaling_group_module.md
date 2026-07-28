---
collection: ansible
version: "8"
title: "community.general.rax_scaling_group module – Manipulate Rackspace Cloud Autoscale Groups"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/rax_scaling_group_module.html
fetched_at: 2026-07-28T01:49:48+00:00
---
# community.general.rax_scaling_group module – Manipulate Rackspace Cloud Autoscale Groups

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
> see [Requirements](rax_scaling_group_module.md#ansible-collections-community-general-rax-scaling-group-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.rax_scaling_group`.

- [DEPRECATED](rax_scaling_group_module.md#deprecated)
- [Synopsis](rax_scaling_group_module.md#synopsis)
- [Requirements](rax_scaling_group_module.md#requirements)
- [Parameters](rax_scaling_group_module.md#parameters)
- [Attributes](rax_scaling_group_module.md#attributes)
- [Notes](rax_scaling_group_module.md#notes)
- [Examples](rax_scaling_group_module.md#examples)
- [Status](rax_scaling_group_module.md#status)

## [DEPRECATED](rax_scaling_group_module.md#id1)

Removed in:
:   version 9.0.0

Why:
:   This module relies on the deprecated package pyrax.

Alternative:
:   Use the Openstack modules instead.

## [Synopsis](rax_scaling_group_module.md#id2)

- Manipulate Rackspace Cloud Autoscale Groups

Aliases: cloud.rackspace.rax_scaling_group

## [Requirements](rax_scaling_group_module.md#id3)

The below requirements are needed on the host that executes this module.

- pyrax
- python >= 2.6

## [Parameters](rax_scaling_group_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **api_key**  aliases: password  string | Rackspace API key, overrides `credentials`. |
| **auth_endpoint**  string | The URI of the authentication service.  If not specified will be set to <https://identity.api.rackspacecloud.com/v2.0/> |
| **config_drive**  boolean | Attach read-only configuration drive to server as label config-2  **Choices:**   - `false` ← (default) - `true` |
| **cooldown**  integer | The period of time, in seconds, that must pass before any scaling can occur after the previous scaling. Must be an integer between 0 and 86400 (24 hrs).  **Default:** `300` |
| **credentials**  aliases: creds_file  path | File to find the Rackspace credentials in. Ignored if `api_key` and `username` are provided. |
| **disk_config**  string | Disk partitioning strategy  If not specified, it will fallback to `auto`.  **Choices:**   - `"auto"` - `"manual"` |
| **env**  string | Environment as configured in `~/.pyrax.cfg`, see <https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration>. |
| **files**  dictionary | Files to insert into the instance. Hash of `remotepath: localpath`  **Default:** `{}` |
| **flavor**  string / required | flavor to use for the instance |
| **identity_type**  string | Authentication mechanism to use, such as rackspace or keystone.  **Default:** `"rackspace"` |
| **image**  string / required | image to use for the instance. Can be an `id`, `human_id` or `name`. |
| **key_name**  string | key pair to use on the instance |
| **loadbalancers**  list / elements=dictionary | List of load balancer `id` and `port` hashes |
| **max_entities**  integer / required | The maximum number of entities that are allowed in the scaling group. Must be an integer between 0 and 1000. |
| **meta**  dictionary | A hash of metadata to associate with the instance  **Default:** `{}` |
| **min_entities**  integer / required | The minimum number of entities that are allowed in the scaling group. Must be an integer between 0 and 1000. |
| **name**  string / required | Name to give the scaling group |
| **networks**  list / elements=string | The network to attach to the instances. If specified, you must include ALL networks including the public and private interfaces. Can be `id` or `label`.  **Default:** `["public", "private"]` |
| **region**  string | Region to create an instance in. |
| **server_name**  string / required | The base name for servers created by Autoscale |
| **state**  string | Indicate desired state of the resource  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tenant_id**  string | The tenant ID used for authentication. |
| **tenant_name**  string | The tenant name used for authentication. |
| **user_data**  string | Data to be uploaded to the servers config drive. This option implies `config_drive`. Can be a file path or a string |
| **username**  string | Rackspace username, overrides `credentials`. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to require SSL validation of API endpoints.  **Choices:**   - `false` - `true` |
| **wait**  boolean | wait for the scaling group to finish provisioning the minimum amount of servers  **Choices:**   - `false` ← (default) - `true` |
| **wait_timeout**  integer | how long before wait gives up, in seconds  **Default:** `300` |

## [Attributes](rax_scaling_group_module.md#id5)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](rax_scaling_group_module.md#id6)

> **Note:**
>
> - The following environment variables can be used, `RAX_USERNAME`, `RAX_API_KEY`, `RAX_CREDS_FILE`, `RAX_CREDENTIALS`, `RAX_REGION`.
> - `RAX_CREDENTIALS` and `RAX_CREDS_FILE` point to a credentials file appropriate for pyrax. See <https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#authenticating>
> - `RAX_USERNAME` and `RAX_API_KEY` obviate the use of a credentials file
> - `RAX_REGION` defines a Rackspace Public Cloud region (DFW, ORD, LON, …)
> - The following environment variables can be used, `RAX_USERNAME`, `RAX_API_KEY`, `RAX_CREDS_FILE`, `RAX_CREDENTIALS`, `RAX_REGION`.
> - `RAX_CREDENTIALS` and `RAX_CREDS_FILE` points to a credentials file appropriate for pyrax. See <https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#authenticating>
> - `RAX_USERNAME` and `RAX_API_KEY` obviate the use of a credentials file
> - `RAX_REGION` defines a Rackspace Public Cloud region (DFW, ORD, LON, …)

## [Examples](rax_scaling_group_module.md#id7)

```yaml+jinja
---
- hosts: localhost
  gather_facts: false
  connection: local
  tasks:
    - community.general.rax_scaling_group:
        credentials: ~/.raxpub
        region: ORD
        cooldown: 300
        flavor: performance1-1
        image: bb02b1a3-bc77-4d17-ab5b-421d89850fca
        min_entities: 5
        max_entities: 10
        name: ASG Test
        server_name: asgtest
        loadbalancers:
            - id: 228385
              port: 80
      register: asg
```

## [Status](rax_scaling_group_module.md#id8)

- This module will be removed in version 9.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](rax_scaling_group_module.md#deprecated).

### Authors

- Matt Martz (@sivel)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
