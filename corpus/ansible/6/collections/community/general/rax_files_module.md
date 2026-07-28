---
collection: ansible
version: "6"
title: "community.general.rax_files module – Manipulate Rackspace Cloud Files Containers"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/rax_files_module.html
fetched_at: 2026-07-27T17:12:25+00:00
---
# community.general.rax_files module – Manipulate Rackspace Cloud Files Containers

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
> see [Requirements](rax_files_module.md#ansible-collections-community-general-rax-files-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.rax_files`.

- [Synopsis](rax_files_module.md#synopsis)
- [Requirements](rax_files_module.md#requirements)
- [Parameters](rax_files_module.md#parameters)
- [Notes](rax_files_module.md#notes)
- [Examples](rax_files_module.md#examples)

## [Synopsis](rax_files_module.md#id1)

- Manipulate Rackspace Cloud Files Containers

## [Requirements](rax_files_module.md#id2)

The below requirements are needed on the host that executes this module.

- pyrax
- python >= 2.6

## [Parameters](rax_files_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  aliases: password  string | Rackspace API key, overrides *credentials*. |
| **auth_endpoint**  string | The URI of the authentication service.  If not specified will be set to <https://identity.api.rackspacecloud.com/v2.0/> |
| **clear_meta**  boolean | Optionally clear existing metadata when applying metadata to existing containers. Selecting this option is only appropriate when setting type=meta  Choices:   - `false` ← (default) - `true` |
| **container**  string | The container to use for container or metadata operations. |
| **credentials**  aliases: creds_file  path | File to find the Rackspace credentials in. Ignored if *api_key* and *username* are provided. |
| **env**  string | Environment as configured in *~/.pyrax.cfg*, see <https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration>. |
| **identity_type**  string | Authentication mechanism to use, such as rackspace or keystone.  Default: `"rackspace"` |
| **meta**  dictionary | A hash of items to set as metadata values on a container  Default: `{}` |
| **private**  boolean | Used to set a container as private, removing it from the CDN. **Warning!** Private containers, if previously made public, can have live objects available until the TTL on cached objects expires  Choices:   - `false` ← (default) - `true` |
| **public**  boolean | Used to set a container as public, available via the Cloud Files CDN  Choices:   - `false` ← (default) - `true` |
| **region**  string | Region to create an instance in |
| **state**  string | Indicate desired state of the resource  Choices:   - `"present"` ← (default) - `"absent"` - `"list"` |
| **tenant_id**  string | The tenant ID used for authentication. |
| **tenant_name**  string | The tenant name used for authentication. |
| **ttl**  integer | In seconds, set a container-wide TTL for all objects cached on CDN edge nodes. Setting a TTL is only appropriate for containers that are public |
| **type**  string | Type of object to do work on, i.e. metadata object or a container object  Choices:   - `"container"` ← (default) - `"meta"` |
| **username**  string | Rackspace username, overrides *credentials*. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to require SSL validation of API endpoints.  Choices:   - `false` - `true` |
| **web_error**  string | Sets an object to be presented as the HTTP error page when accessed by the CDN URL |
| **web_index**  string | Sets an object to be presented as the HTTP index page when accessed by the CDN URL |

## [Notes](rax_files_module.md#id4)

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

## [Examples](rax_files_module.md#id5)

```yaml+jinja
- name: "Test Cloud Files Containers"
  hosts: local
  gather_facts: false
  tasks:
    - name: "List all containers"
      community.general.rax_files:
        state: list

    - name: "Create container called 'mycontainer'"
      community.general.rax_files:
        container: mycontainer

    - name: "Create container 'mycontainer2' with metadata"
      community.general.rax_files:
        container: mycontainer2
        meta:
          key: value
          file_for: someuser@example.com

    - name: "Set a container's web index page"
      community.general.rax_files:
        container: mycontainer
        web_index: index.html

    - name: "Set a container's web error page"
      community.general.rax_files:
        container: mycontainer
        web_error: error.html

    - name: "Make container public"
      community.general.rax_files:
        container: mycontainer
        public: true

    - name: "Make container public with a 24 hour TTL"
      community.general.rax_files:
        container: mycontainer
        public: true
        ttl: 86400

    - name: "Make container private"
      community.general.rax_files:
        container: mycontainer
        private: true

- name: "Test Cloud Files Containers Metadata Storage"
  hosts: local
  gather_facts: false
  tasks:
    - name: "Get mycontainer2 metadata"
      community.general.rax_files:
        container: mycontainer2
        type: meta

    - name: "Set mycontainer2 metadata"
      community.general.rax_files:
        container: mycontainer2
        type: meta
        meta:
          uploaded_by: someuser@example.com

    - name: "Remove mycontainer2 metadata"
      community.general.rax_files:
        container: "mycontainer2"
        type: meta
        state: absent
        meta:
          key: ""
          file_for: ""
```

### Authors

- Paul Durivage (@angstwad)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
