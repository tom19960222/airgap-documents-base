---
collection: ansible
version: "8"
title: "community.general.rax_clb_ssl module – Manage SSL termination for a Rackspace Cloud Load Balancer"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/rax_clb_ssl_module.html
fetched_at: 2026-07-28T01:49:36+00:00
---
# community.general.rax_clb_ssl module – Manage SSL termination for a Rackspace Cloud Load Balancer

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
> see [Requirements](rax_clb_ssl_module.md#ansible-collections-community-general-rax-clb-ssl-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.rax_clb_ssl`.

- [DEPRECATED](rax_clb_ssl_module.md#deprecated)
- [Synopsis](rax_clb_ssl_module.md#synopsis)
- [Requirements](rax_clb_ssl_module.md#requirements)
- [Parameters](rax_clb_ssl_module.md#parameters)
- [Attributes](rax_clb_ssl_module.md#attributes)
- [Notes](rax_clb_ssl_module.md#notes)
- [Examples](rax_clb_ssl_module.md#examples)
- [Status](rax_clb_ssl_module.md#status)

## [DEPRECATED](rax_clb_ssl_module.md#id1)

Removed in:
:   version 9.0.0

Why:
:   This module relies on the deprecated package pyrax.

Alternative:
:   Use the Openstack modules instead.

## [Synopsis](rax_clb_ssl_module.md#id2)

- Set up, reconfigure, or remove SSL termination for an existing load balancer.

Aliases: cloud.rackspace.rax_clb_ssl

## [Requirements](rax_clb_ssl_module.md#id3)

The below requirements are needed on the host that executes this module.

- pyrax
- python >= 2.6

## [Parameters](rax_clb_ssl_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **api_key**  aliases: password  string | Rackspace API key, overrides `credentials`. |
| **auth_endpoint**  string | The URI of the authentication service.  If not specified will be set to <https://identity.api.rackspacecloud.com/v2.0/> |
| **certificate**  string | The public SSL certificates as a string in PEM format. |
| **credentials**  aliases: creds_file  path | File to find the Rackspace credentials in. Ignored if `api_key` and `username` are provided. |
| **enabled**  boolean | If set to “false”, temporarily disable SSL termination without discarding  existing credentials.  **Choices:**   - `false` - `true` ← (default) |
| **env**  string | Environment as configured in `~/.pyrax.cfg`, see <https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration>. |
| **https_redirect**  boolean | If “true”, the load balancer will redirect HTTP traffic to HTTPS.  Requires “secure_traffic_only” to be true. Incurs an implicit wait if SSL  termination is also applied or removed.  **Choices:**   - `false` - `true` |
| **identity_type**  string | Authentication mechanism to use, such as rackspace or keystone.  **Default:** `"rackspace"` |
| **intermediate_certificate**  string | One or more intermediate certificate authorities as a string in PEM  format, concatenated into a single string. |
| **loadbalancer**  string / required | Name or ID of the load balancer on which to manage SSL termination. |
| **private_key**  string | The private SSL key as a string in PEM format. |
| **region**  string | Region to create an instance in. |
| **secure_port**  integer | The port to listen for secure traffic.  **Default:** `443` |
| **secure_traffic_only**  boolean | If “true”, the load balancer will \*only\* accept secure traffic.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | If set to “present”, SSL termination will be added to this load balancer.  If “absent”, SSL termination will be removed instead.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tenant_id**  string | The tenant ID used for authentication. |
| **tenant_name**  string | The tenant name used for authentication. |
| **username**  string | Rackspace username, overrides `credentials`. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to require SSL validation of API endpoints.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Wait for the balancer to be in state “running” before turning.  **Choices:**   - `false` ← (default) - `true` |
| **wait_timeout**  integer | How long before “wait” gives up, in seconds.  **Default:** `300` |

## [Attributes](rax_clb_ssl_module.md#id5)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](rax_clb_ssl_module.md#id6)

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

## [Examples](rax_clb_ssl_module.md#id7)

```yaml+jinja
- name: Enable SSL termination on a load balancer
  community.general.rax_clb_ssl:
    loadbalancer: the_loadbalancer
    state: present
    private_key: "{{ lookup('file', 'credentials/server.key' ) }}"
    certificate: "{{ lookup('file', 'credentials/server.crt' ) }}"
    intermediate_certificate: "{{ lookup('file', 'credentials/trust-chain.crt') }}"
    secure_traffic_only: true
    wait: true

- name: Disable SSL termination
  community.general.rax_clb_ssl:
    loadbalancer: "{{ registered_lb.balancer.id }}"
    state: absent
    wait: true
```

## [Status](rax_clb_ssl_module.md#id8)

- This module will be removed in version 9.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](rax_clb_ssl_module.md#deprecated).

### Authors

- Ash Wilson (@smashwilson)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
