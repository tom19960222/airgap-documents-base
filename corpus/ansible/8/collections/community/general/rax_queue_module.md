---
collection: ansible
version: "8"
title: "community.general.rax_queue module – Create / delete a queue in Rackspace Public Cloud"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/rax_queue_module.html
fetched_at: 2026-07-28T01:49:47+00:00
---
# community.general.rax_queue module – Create / delete a queue in Rackspace Public Cloud

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
> see [Requirements](rax_queue_module.md#ansible-collections-community-general-rax-queue-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.rax_queue`.

- [DEPRECATED](rax_queue_module.md#deprecated)
- [Synopsis](rax_queue_module.md#synopsis)
- [Requirements](rax_queue_module.md#requirements)
- [Parameters](rax_queue_module.md#parameters)
- [Attributes](rax_queue_module.md#attributes)
- [Notes](rax_queue_module.md#notes)
- [Examples](rax_queue_module.md#examples)
- [Status](rax_queue_module.md#status)

## [DEPRECATED](rax_queue_module.md#id1)

Removed in:
:   version 9.0.0

Why:
:   This module relies on the deprecated package pyrax.

Alternative:
:   Use the Openstack modules instead.

## [Synopsis](rax_queue_module.md#id2)

- creates / deletes a Rackspace Public Cloud queue.

Aliases: cloud.rackspace.rax_queue

## [Requirements](rax_queue_module.md#id3)

The below requirements are needed on the host that executes this module.

- pyrax
- python >= 2.6

## [Parameters](rax_queue_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **api_key**  aliases: password  string | Rackspace API key, overrides `credentials`. |
| **auth_endpoint**  string | The URI of the authentication service.  If not specified will be set to <https://identity.api.rackspacecloud.com/v2.0/> |
| **credentials**  aliases: creds_file  path | File to find the Rackspace credentials in. Ignored if `api_key` and `username` are provided. |
| **env**  string | Environment as configured in `~/.pyrax.cfg`, see <https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration>. |
| **identity_type**  string | Authentication mechanism to use, such as rackspace or keystone.  **Default:** `"rackspace"` |
| **name**  string | Name to give the queue |
| **region**  string | Region to create an instance in. |
| **state**  string | Indicate desired state of the resource  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tenant_id**  string | The tenant ID used for authentication. |
| **tenant_name**  string | The tenant name used for authentication. |
| **username**  string | Rackspace username, overrides `credentials`. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to require SSL validation of API endpoints.  **Choices:**   - `false` - `true` |

## [Attributes](rax_queue_module.md#id5)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](rax_queue_module.md#id6)

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

## [Examples](rax_queue_module.md#id7)

```yaml+jinja
- name: Build a Queue
  gather_facts: false
  hosts: local
  connection: local
  tasks:
    - name: Queue create request
      local_action:
        module: rax_queue
        credentials: ~/.raxpub
        name: my-queue
        region: DFW
        state: present
      register: my_queue
```

## [Status](rax_queue_module.md#id8)

- This module will be removed in version 9.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](rax_queue_module.md#deprecated).

### Authors

- Christopher H. Laco (@claco)
- Matt Martz (@sivel)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
