---
collection: ansible
version: "8"
title: "community.general.rax_clb_nodes module – Add, modify and remove nodes from a Rackspace Cloud Load Balancer"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/rax_clb_nodes_module.html
fetched_at: 2026-07-28T01:49:35+00:00
---
# community.general.rax_clb_nodes module – Add, modify and remove nodes from a Rackspace Cloud Load Balancer

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
> see [Requirements](rax_clb_nodes_module.md#ansible-collections-community-general-rax-clb-nodes-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.rax_clb_nodes`.

- [DEPRECATED](rax_clb_nodes_module.md#deprecated)
- [Synopsis](rax_clb_nodes_module.md#synopsis)
- [Requirements](rax_clb_nodes_module.md#requirements)
- [Parameters](rax_clb_nodes_module.md#parameters)
- [Attributes](rax_clb_nodes_module.md#attributes)
- [Notes](rax_clb_nodes_module.md#notes)
- [Examples](rax_clb_nodes_module.md#examples)
- [Status](rax_clb_nodes_module.md#status)

## [DEPRECATED](rax_clb_nodes_module.md#id1)

Removed in:
:   version 9.0.0

Why:
:   This module relies on the deprecated package pyrax.

Alternative:
:   Use the Openstack modules instead.

## [Synopsis](rax_clb_nodes_module.md#id2)

- Adds, modifies and removes nodes from a Rackspace Cloud Load Balancer

Aliases: cloud.rackspace.rax_clb_nodes

## [Requirements](rax_clb_nodes_module.md#id3)

The below requirements are needed on the host that executes this module.

- pyrax
- python >= 2.6

## [Parameters](rax_clb_nodes_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **address**  string | IP address or domain name of the node |
| **api_key**  aliases: password  string | Rackspace API key, overrides `credentials`. |
| **auth_endpoint**  string | The URI of the authentication service.  If not specified will be set to <https://identity.api.rackspacecloud.com/v2.0/> |
| **condition**  string | Condition for the node, which determines its role within the load balancer  **Choices:**   - `"enabled"` - `"disabled"` - `"draining"` |
| **credentials**  aliases: creds_file  path | File to find the Rackspace credentials in. Ignored if `api_key` and `username` are provided. |
| **env**  string | Environment as configured in `~/.pyrax.cfg`, see <https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration>. |
| **identity_type**  string | Authentication mechanism to use, such as rackspace or keystone.  **Default:** `"rackspace"` |
| **load_balancer_id**  integer / required | Load balancer id |
| **node_id**  integer | Node id |
| **port**  integer | Port number of the load balanced service on the node |
| **region**  string | Region to create an instance in. |
| **state**  string | Indicate desired state of the node  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tenant_id**  string | The tenant ID used for authentication. |
| **tenant_name**  string | The tenant name used for authentication. |
| **type**  string | Type of node  **Choices:**   - `"primary"` - `"secondary"` |
| **username**  string | Rackspace username, overrides `credentials`. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to require SSL validation of API endpoints.  **Choices:**   - `false` - `true` |
| **virtualenv**  path | Virtualenv to execute this module in |
| **wait**  boolean | Wait for the load balancer to become active before returning  **Choices:**   - `false` ← (default) - `true` |
| **wait_timeout**  integer | How long to wait before giving up and returning an error  **Default:** `30` |
| **weight**  integer | Weight of node |

## [Attributes](rax_clb_nodes_module.md#id5)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](rax_clb_nodes_module.md#id6)

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

## [Examples](rax_clb_nodes_module.md#id7)

```yaml+jinja
- name: Add a new node to the load balancer
  local_action:
    module: rax_clb_nodes
    load_balancer_id: 71
    address: 10.2.2.3
    port: 80
    condition: enabled
    type: primary
    wait: true
    credentials: /path/to/credentials

- name: Drain connections from a node
  local_action:
    module: rax_clb_nodes
    load_balancer_id: 71
    node_id: 410
    condition: draining
    wait: true
    credentials: /path/to/credentials

- name: Remove a node from the load balancer
  local_action:
    module: rax_clb_nodes
    load_balancer_id: 71
    node_id: 410
    state: absent
    wait: true
    credentials: /path/to/credentials
```

## [Status](rax_clb_nodes_module.md#id8)

- This module will be removed in version 9.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](rax_clb_nodes_module.md#deprecated).

### Authors

- Lukasz Kawczynski (@neuroid)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
