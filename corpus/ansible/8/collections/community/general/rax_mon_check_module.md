---
collection: ansible
version: "8"
title: "community.general.rax_mon_check module – Create or delete a Rackspace Cloud Monitoring check for an existing entity."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/rax_mon_check_module.html
fetched_at: 2026-07-28T01:49:44+00:00
---
# community.general.rax_mon_check module – Create or delete a Rackspace Cloud Monitoring check for an existing entity.

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
> see [Requirements](rax_mon_check_module.md#ansible-collections-community-general-rax-mon-check-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.rax_mon_check`.

- [DEPRECATED](rax_mon_check_module.md#deprecated)
- [Synopsis](rax_mon_check_module.md#synopsis)
- [Requirements](rax_mon_check_module.md#requirements)
- [Parameters](rax_mon_check_module.md#parameters)
- [Attributes](rax_mon_check_module.md#attributes)
- [Notes](rax_mon_check_module.md#notes)
- [Examples](rax_mon_check_module.md#examples)
- [Status](rax_mon_check_module.md#status)

## [DEPRECATED](rax_mon_check_module.md#id1)

Removed in:
:   version 9.0.0

Why:
:   This module relies on the deprecated package pyrax.

Alternative:
:   Use the Openstack modules instead.

## [Synopsis](rax_mon_check_module.md#id2)

- Create or delete a Rackspace Cloud Monitoring check associated with an existing rax_mon_entity. A check is a specific test or measurement that is performed, possibly from different monitoring zones, on the systems you monitor. Rackspace monitoring module flow | rax_mon_entity -> \*rax_mon_check\* -> rax_mon_notification -> rax_mon_notification_plan -> rax_mon_alarm

Aliases: cloud.rackspace.rax_mon_check

## [Requirements](rax_mon_check_module.md#id3)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- pyrax

## [Parameters](rax_mon_check_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **api_key**  aliases: password  string | Rackspace API key, overrides `credentials`. |
| **auth_endpoint**  string | The URI of the authentication service.  If not specified will be set to <https://identity.api.rackspacecloud.com/v2.0/> |
| **check_type**  string / required | The type of check to create. `remote.` checks may be created on any rax_mon_entity. `agent.` checks may only be created on rax_mon_entities that have a non-null `agent_id`.  Choices for this option are:  - `remote.dns` - `remote.ftp-banner` - `remote.http` - `remote.imap-banner` - `remote.mssql-banner` - `remote.mysql-banner` - `remote.ping` - `remote.pop3-banner` - `remote.postgresql-banner` - `remote.smtp-banner` - `remote.smtp` - `remote.ssh` - `remote.tcp` - `remote.telnet-banner` - `agent.filesystem` - `agent.memory` - `agent.load_average` - `agent.cpu` - `agent.disk` - `agent.network` - `agent.plugin` |
| **credentials**  aliases: creds_file  path | File to find the Rackspace credentials in. Ignored if `api_key` and `username` are provided. |
| **details**  dictionary | Additional details specific to the check type. Must be a hash of strings between 1 and 255 characters long, or an array or object containing 0 to 256 items.  **Default:** `{}` |
| **disabled**  boolean | If `true`, ensure the check is created, but don’t actually use it yet.  **Choices:**   - `false` ← (default) - `true` |
| **entity_id**  string / required | ID of the rax_mon_entity to target with this check. |
| **env**  string | Environment as configured in `~/.pyrax.cfg`, see <https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration>. |
| **identity_type**  string | Authentication mechanism to use, such as rackspace or keystone.  **Default:** `"rackspace"` |
| **label**  string / required | Defines a label for this check, between 1 and 64 characters long. |
| **metadata**  dictionary | Hash of arbitrary key-value pairs to accompany this check if it fires. Keys and values must be strings between 1 and 255 characters long.  **Default:** `{}` |
| **monitoring_zones_poll**  string | Comma-separated list of the names of the monitoring zones the check should run from. Available monitoring zones include mzdfw, mzhkg, mziad, mzlon, mzord and mzsyd. Required for remote.\* checks; prohibited for agent.\* checks. |
| **period**  integer | The number of seconds between each time the check is performed. Must be greater than the minimum period set on your account. |
| **region**  string | Region to create an instance in. |
| **state**  string | Ensure that a check with this `label` exists or does not exist.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **target_alias**  string | One of `target_alias` and `target_hostname` is required for remote.\* checks, but prohibited for agent.\* checks. Use the corresponding key in the entity’s `ip_addresses` hash to resolve an IP address to target. |
| **target_hostname**  string | One of `target_hostname` and `target_alias` is required for remote.\* checks, but prohibited for agent.\* checks. The hostname this check should target. Must be a valid IPv4, IPv6, or FQDN. |
| **tenant_id**  string | The tenant ID used for authentication. |
| **tenant_name**  string | The tenant name used for authentication. |
| **timeout**  integer | The number of seconds this check will wait when attempting to collect results. Must be less than the period. |
| **username**  string | Rackspace username, overrides `credentials`. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to require SSL validation of API endpoints.  **Choices:**   - `false` - `true` |

## [Attributes](rax_mon_check_module.md#id5)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](rax_mon_check_module.md#id6)

> **Note:**
>
> - The following environment variables can be used, `RAX_USERNAME`, `RAX_API_KEY`, `RAX_CREDS_FILE`, `RAX_CREDENTIALS`, `RAX_REGION`.
> - `RAX_CREDENTIALS` and `RAX_CREDS_FILE` points to a credentials file appropriate for pyrax. See <https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#authenticating>
> - `RAX_USERNAME` and `RAX_API_KEY` obviate the use of a credentials file
> - `RAX_REGION` defines a Rackspace Public Cloud region (DFW, ORD, LON, …)

## [Examples](rax_mon_check_module.md#id7)

```yaml+jinja
- name: Create a monitoring check
  gather_facts: false
  hosts: local
  connection: local
  tasks:
  - name: Associate a check with an existing entity.
    community.general.rax_mon_check:
      credentials: ~/.rax_pub
      state: present
      entity_id: "{{ the_entity['entity']['id'] }}"
      label: the_check
      check_type: remote.ping
      monitoring_zones_poll: mziad,mzord,mzdfw
      details:
        count: 10
      meta:
        hurf: durf
    register: the_check
```

## [Status](rax_mon_check_module.md#id8)

- This module will be removed in version 9.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](rax_mon_check_module.md#deprecated).

### Authors

- Ash Wilson (@smashwilson)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
