---
collection: ansible
version: "6"
title: "community.general.rax_scaling_policy module – Manipulate Rackspace Cloud Autoscale Scaling Policy"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/rax_scaling_policy_module.html
fetched_at: 2026-07-27T17:12:34+00:00
---
# community.general.rax_scaling_policy module – Manipulate Rackspace Cloud Autoscale Scaling Policy

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](rax_scaling_policy_module.md#ansible-collections-community-general-rax-scaling-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.rax_scaling_policy`.

- [Synopsis](rax_scaling_policy_module.md#synopsis)
- [Requirements](rax_scaling_policy_module.md#requirements)
- [Parameters](rax_scaling_policy_module.md#parameters)
- [Notes](rax_scaling_policy_module.md#notes)
- [Examples](rax_scaling_policy_module.md#examples)

## [Synopsis](rax_scaling_policy_module.md#id1)

- Manipulate Rackspace Cloud Autoscale Scaling Policy

## [Requirements](rax_scaling_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- pyrax
- python >= 2.6

## [Parameters](rax_scaling_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  aliases: password  string | Rackspace API key, overrides *credentials*. |
| **at**  string | The UTC time when this policy will be executed. The time must be formatted according to `yyyy-MM-dd'T'HH:mm:ss.SSS` such as `2013-05-19T08:07:08Z` |
| **auth_endpoint**  string | The URI of the authentication service.  If not specified will be set to <https://identity.api.rackspacecloud.com/v2.0/> |
| **change**  integer | The change, either as a number of servers or as a percentage, to make in the scaling group. If this is a percentage, you must set *is_percent* to `true` also. |
| **cooldown**  integer | The period of time, in seconds, that must pass before any scaling can occur after the previous scaling. Must be an integer between 0 and 86400 (24 hrs).  Default: `300` |
| **credentials**  aliases: creds_file  path | File to find the Rackspace credentials in. Ignored if *api_key* and *username* are provided. |
| **cron**  string | The time when the policy will be executed, as a cron entry. For example, if this is parameter is set to `1 0 * * *` |
| **desired_capacity**  integer | The desired server capacity of the scaling the group; that is, how many servers should be in the scaling group. |
| **env**  string | Environment as configured in *~/.pyrax.cfg*, see <https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration>. |
| **identity_type**  string | Authentication mechanism to use, such as rackspace or keystone.  Default: `"rackspace"` |
| **is_percent**  boolean | Whether the value in *change* is a percent value  Choices:   - `false` ← (default) - `true` |
| **name**  string / required | Name to give the policy |
| **policy_type**  string / required | The type of policy that will be executed for the current release.  Choices:   - `"webhook"` - `"schedule"` |
| **region**  string | Region to create an instance in. |
| **scaling_group**  string / required | Name of the scaling group that this policy will be added to |
| **state**  string | Indicate desired state of the resource  Choices:   - `"present"` ← (default) - `"absent"` |
| **tenant_id**  string | The tenant ID used for authentication. |
| **tenant_name**  string | The tenant name used for authentication. |
| **username**  string | Rackspace username, overrides *credentials*. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to require SSL validation of API endpoints.  Choices:   - `false` - `true` |

## [Notes](rax_scaling_policy_module.md#id4)

> **Note:**
>
> - The following environment variables can be used, `RAX_USERNAME`, `RAX_API_KEY`, `RAX_CREDS_FILE`, `RAX_CREDENTIALS`, `RAX_REGION`.
> - `RAX_CREDENTIALS` and `RAX_CREDS_FILE` points to a credentials file appropriate for pyrax. See <https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#authenticating>
> - `RAX_USERNAME` and `RAX_API_KEY` obviate the use of a credentials file
> - `RAX_REGION` defines a Rackspace Public Cloud region (DFW, ORD, LON, …)
> - The following environment variables can be used, `RAX_USERNAME`, `RAX_API_KEY`, `RAX_CREDS_FILE`, `RAX_CREDENTIALS`, `RAX_REGION`.
> - `RAX_CREDENTIALS` and `RAX_CREDS_FILE` points to a credentials file appropriate for pyrax. See <https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#authenticating>
> - `RAX_USERNAME` and `RAX_API_KEY` obviate the use of a credentials file
> - `RAX_REGION` defines a Rackspace Public Cloud region (DFW, ORD, LON, …)

## [Examples](rax_scaling_policy_module.md#id5)

```yaml+jinja
---
- hosts: localhost
  gather_facts: false
  connection: local
  tasks:
    - community.general.rax_scaling_policy:
        credentials: ~/.raxpub
        region: ORD
        at: '2013-05-19T08:07:08Z'
        change: 25
        cooldown: 300
        is_percent: true
        name: ASG Test Policy - at
        policy_type: schedule
        scaling_group: ASG Test
      register: asps_at

    - community.general.rax_scaling_policy:
        credentials: ~/.raxpub
        region: ORD
        cron: '1 0 * * *'
        change: 25
        cooldown: 300
        is_percent: true
        name: ASG Test Policy - cron
        policy_type: schedule
        scaling_group: ASG Test
      register: asp_cron

    - community.general.rax_scaling_policy:
        credentials: ~/.raxpub
        region: ORD
        cooldown: 300
        desired_capacity: 5
        name: ASG Test Policy - webhook
        policy_type: webhook
        scaling_group: ASG Test
      register: asp_webhook
```

### Authors

- Matt Martz (@sivel)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
