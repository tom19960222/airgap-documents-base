---
collection: ansible
version: "6"
title: "community.general.rax_dns module – Manage domains on Rackspace Cloud DNS"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/rax_dns_module.html
fetched_at: 2026-07-27T17:12:23+00:00
---
# community.general.rax_dns module – Manage domains on Rackspace Cloud DNS

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
> see [Requirements](rax_dns_module.md#ansible-collections-community-general-rax-dns-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.rax_dns`.

- [Synopsis](rax_dns_module.md#synopsis)
- [Requirements](rax_dns_module.md#requirements)
- [Parameters](rax_dns_module.md#parameters)
- [Notes](rax_dns_module.md#notes)
- [Examples](rax_dns_module.md#examples)

## [Synopsis](rax_dns_module.md#id1)

- Manage domains on Rackspace Cloud DNS

## [Requirements](rax_dns_module.md#id2)

The below requirements are needed on the host that executes this module.

- pyrax
- python >= 2.6

## [Parameters](rax_dns_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  aliases: password  string | Rackspace API key, overrides *credentials*. |
| **auth_endpoint**  string | The URI of the authentication service.  If not specified will be set to <https://identity.api.rackspacecloud.com/v2.0/> |
| **comment**  string | Brief description of the domain. Maximum length of 160 characters |
| **credentials**  aliases: creds_file  path | File to find the Rackspace credentials in. Ignored if *api_key* and *username* are provided. |
| **email**  string | Email address of the domain administrator |
| **env**  string | Environment as configured in *~/.pyrax.cfg*, see <https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration>. |
| **identity_type**  string | Authentication mechanism to use, such as rackspace or keystone.  Default: `"rackspace"` |
| **name**  string | Domain name to create |
| **region**  string | Region to create an instance in. |
| **state**  string | Indicate desired state of the resource  Choices:   - `"present"` ← (default) - `"absent"` |
| **tenant_id**  string | The tenant ID used for authentication. |
| **tenant_name**  string | The tenant name used for authentication. |
| **ttl**  integer | Time to live of domain in seconds  Default: `3600` |
| **username**  string | Rackspace username, overrides *credentials*. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to require SSL validation of API endpoints.  Choices:   - `false` - `true` |

## [Notes](rax_dns_module.md#id4)

> **Note:**
>
> - It is recommended that plays utilizing this module be run with `serial: 1` to avoid exceeding the API request limit imposed by the Rackspace CloudDNS API
> - The following environment variables can be used, `RAX_USERNAME`, `RAX_API_KEY`, `RAX_CREDS_FILE`, `RAX_CREDENTIALS`, `RAX_REGION`.
> - `RAX_CREDENTIALS` and `RAX_CREDS_FILE` points to a credentials file appropriate for pyrax. See <https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#authenticating>
> - `RAX_USERNAME` and `RAX_API_KEY` obviate the use of a credentials file
> - `RAX_REGION` defines a Rackspace Public Cloud region (DFW, ORD, LON, …)
> - The following environment variables can be used, `RAX_USERNAME`, `RAX_API_KEY`, `RAX_CREDS_FILE`, `RAX_CREDENTIALS`, `RAX_REGION`.
> - `RAX_CREDENTIALS` and `RAX_CREDS_FILE` points to a credentials file appropriate for pyrax. See <https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#authenticating>
> - `RAX_USERNAME` and `RAX_API_KEY` obviate the use of a credentials file
> - `RAX_REGION` defines a Rackspace Public Cloud region (DFW, ORD, LON, …)

## [Examples](rax_dns_module.md#id5)

```yaml+jinja
- name: Create domain
  hosts: all
  gather_facts: false
  tasks:
    - name: Domain create request
      local_action:
        module: rax_dns
        credentials: ~/.raxpub
        name: example.org
        email: admin@example.org
      register: rax_dns
```

### Authors

- Matt Martz (@sivel)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
