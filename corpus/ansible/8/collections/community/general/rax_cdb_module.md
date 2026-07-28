---
collection: ansible
version: "8"
title: "community.general.rax_cdb module – Create/delete or resize a Rackspace Cloud Databases instance"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/rax_cdb_module.html
fetched_at: 2026-07-28T01:49:33+00:00
---
# community.general.rax_cdb module – Create/delete or resize a Rackspace Cloud Databases instance

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
> see [Requirements](rax_cdb_module.md#ansible-collections-community-general-rax-cdb-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.rax_cdb`.

- [DEPRECATED](rax_cdb_module.md#deprecated)
- [Synopsis](rax_cdb_module.md#synopsis)
- [Requirements](rax_cdb_module.md#requirements)
- [Parameters](rax_cdb_module.md#parameters)
- [Attributes](rax_cdb_module.md#attributes)
- [Notes](rax_cdb_module.md#notes)
- [Examples](rax_cdb_module.md#examples)
- [Status](rax_cdb_module.md#status)

## [DEPRECATED](rax_cdb_module.md#id1)

Removed in:
:   version 9.0.0

Why:
:   This module relies on the deprecated package pyrax.

Alternative:
:   Use the Openstack modules instead.

## [Synopsis](rax_cdb_module.md#id2)

- creates / deletes or resize a Rackspace Cloud Databases instance and optionally waits for it to be ‘running’. The name option needs to be unique since it’s used to identify the instance.

Aliases: cloud.rackspace.rax_cdb

## [Requirements](rax_cdb_module.md#id3)

The below requirements are needed on the host that executes this module.

- pyrax
- python >= 2.6

## [Parameters](rax_cdb_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **api_key**  aliases: password  string | Rackspace API key, overrides `credentials`. |
| **auth_endpoint**  string | The URI of the authentication service.  If not specified will be set to <https://identity.api.rackspacecloud.com/v2.0/> |
| **cdb_type**  aliases: type  string | type of instance (i.e. MySQL, MariaDB, Percona)  **Default:** `"MySQL"` |
| **cdb_version**  aliases: version  string | version of database (MySQL supports 5.1 and 5.6, MariaDB supports 10, Percona supports 5.6)  The available choices are: `5.1`, `5.6` and `10`.  **Default:** `"5.6"` |
| **credentials**  aliases: creds_file  path | File to find the Rackspace credentials in. Ignored if `api_key` and `username` are provided. |
| **env**  string | Environment as configured in `~/.pyrax.cfg`, see <https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration>. |
| **flavor**  integer | flavor to use for the instance 1 to 6 (i.e. 512MB to 16GB)  **Default:** `1` |
| **identity_type**  string | Authentication mechanism to use, such as rackspace or keystone.  **Default:** `"rackspace"` |
| **name**  string / required | Name of the databases server instance |
| **region**  string | Region to create an instance in. |
| **state**  string | Indicate desired state of the resource  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tenant_id**  string | The tenant ID used for authentication. |
| **tenant_name**  string | The tenant name used for authentication. |
| **username**  string | Rackspace username, overrides `credentials`. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to require SSL validation of API endpoints.  **Choices:**   - `false` - `true` |
| **volume**  integer | Volume size of the database 1-150GB  **Default:** `2` |
| **wait**  boolean | wait for the instance to be in state ‘running’ before returning  **Choices:**   - `false` ← (default) - `true` |
| **wait_timeout**  integer | how long before wait gives up, in seconds  **Default:** `300` |

## [Attributes](rax_cdb_module.md#id5)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](rax_cdb_module.md#id6)

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

## [Examples](rax_cdb_module.md#id7)

```yaml+jinja
- name: Build a Cloud Databases
  gather_facts: false
  tasks:
    - name: Server build request
      local_action:
        module: rax_cdb
        credentials: ~/.raxpub
        region: IAD
        name: db-server1
        flavor: 1
        volume: 2
        cdb_type: MySQL
        cdb_version: 5.6
        wait: true
        state: present
      register: rax_db_server
```

## [Status](rax_cdb_module.md#id8)

- This module will be removed in version 9.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](rax_cdb_module.md#deprecated).

### Authors

- Simon JAILLET (@jails)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
