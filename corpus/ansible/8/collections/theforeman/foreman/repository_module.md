---
collection: ansible
version: "8"
title: "theforeman.foreman.repository module – Manage Repositories"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/repository_module.html
fetched_at: 2026-07-28T02:56:27+00:00
---
# theforeman.foreman.repository module – Manage Repositories

> **Note:**
>
> This module is part of the [theforeman.foreman collection](https://galaxy.ansible.com/ui/repo/published/theforeman/foreman/) (version 3.15.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install theforeman.foreman`.
> You need further requirements to be able to use this module,
> see [Requirements](repository_module.md#ansible-collections-theforeman-foreman-repository-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.repository`.

New in theforeman.foreman 1.0.0

- [Synopsis](repository_module.md#synopsis)
- [Requirements](repository_module.md#requirements)
- [Parameters](repository_module.md#parameters)
- [Attributes](repository_module.md#attributes)
- [Notes](repository_module.md#notes)
- [Examples](repository_module.md#examples)
- [Return Values](repository_module.md#return-values)

## [Synopsis](repository_module.md#id1)

- Create and manage repositories

Aliases: katello_repository

## [Requirements](repository_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](repository_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ansible_collection_requirements**  string | Contents of requirement yaml file to sync from URL |
| **arch**  string | Architecture of content in the repository  Set to `noarch` to disable the architecture restriction again. |
| **auto_enabled**  boolean | repositories will be automatically enabled on a registered host subscribed to this product  **Choices:**   - `false` - `true` |
| **checksum_type**  string | Checksum of the repository  **Choices:**   - `"sha1"` - `"sha256"` |
| **content_type**  string / required | The content type of the repository  **Choices:**   - `"deb"` - `"docker"` - `"file"` - `"ostree"` - `"puppet"` - `"yum"` - `"ansible_collection"` |
| **deb_architectures**  string | comma separated list of architectures to be synced from deb-archive  only available for *content_type=deb* |
| **deb_components**  string | comma separated list of repo components to be synced from deb-archive  only available for *content_type=deb* |
| **deb_errata_url**  string | URL to sync Debian or Ubuntu errata information from  only available on Orcharhino  only available for *content_type=deb* |
| **deb_releases**  string | comma separated list of releases to be synced from deb-archive  only available for *content_type=deb* |
| **description**  string | Description of the repository |
| **docker_tags_whitelist**  list / elements=string | list of tags to sync for Container Image repository  only available for *content_type=docker*  Deprecated since Katello 4.4 |
| **docker_upstream_name**  string | name of the upstream docker repository  only available for *content_type=docker* |
| **download_concurrency**  integer  *added in theforeman.foreman 3.0.0* | download concurrency for sync from upstream  as the API does not return this value, this will break idempotence for this module |
| **download_policy**  string | The download policy for sync from upstream.  The download policy `background` is deprecated and not available since Katello 4.3.  **Choices:**   - `"background"` - `"immediate"` - `"on_demand"` |
| **exclude_tags**  list / elements=string  *added in theforeman.foreman 3.7.0* | List of tags to exclude when syncing a container image repository. |
| **gpg_key**  string | Repository GPG key |
| **http_proxy**  string | Name of the http proxy to use for content synching  Should be combined with *http_proxy_policy=’use_selected_http_proxy’* |
| **http_proxy_policy**  string | Which proxy to use for content synching  **Choices:**   - `"global_default_http_proxy"` - `"none"` - `"use_selected_http_proxy"` |
| **ignorable_content**  list / elements=string | List of content units to ignore while syncing a yum repository.  Must be subset of rpm,drpm,srpm,distribution,erratum. |
| **ignore_global_proxy**  boolean | Whether content sync should use or ignore the global http proxy setting  This is deprecated with Katello 3.13  It has been superseeded by *http_proxy_policy*  **Choices:**   - `false` - `true` |
| **include_tags**  list / elements=string  *added in theforeman.foreman 3.7.0* | List of tags to sync for a container image repository. |
| **label**  string | label of the repository |
| **mirror_on_sync**  boolean | toggle “mirror on sync” where the state of the repository mirrors that of the upstream repository at sync time  This is deprecated with Katello 4.3  It has been superseeded by *mirroring_policy=mirror_content_only*  **Choices:**   - `false` - `true` |
| **mirroring_policy**  string | Policy to set for mirroring content  Supported since Katello 4.3  **Choices:**   - `"additive"` - `"mirror_content_only"` - `"mirror_complete"` |
| **name**  string / required | Name of the repository |
| **organization**  string / required | Organization that the entity is in |
| **os_versions**  list / elements=string | Identifies whether the repository should be disabled on a client with a non-matching OS version.  A maximum of one OS version can be selected.  Set to `[]` to disable filtering again.  **Choices:**   - `"rhel-6"` - `"rhel-7"` - `"rhel-8"` - `"rhel-9"` |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **product**  string / required | Product to which the repository lives in |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **ssl_ca_cert**  string | Repository SSL CA certificate |
| **ssl_client_cert**  string | Repository SSL client certificate |
| **ssl_client_key**  string | Repository SSL client private key |
| **state**  string | State of the entity  `present_with_defaults` will ensure the entity exists, but won’t update existing ones  **Choices:**   - `"present"` ← (default) - `"present_with_defaults"` - `"absent"` |
| **unprotected**  boolean | publish the repository via HTTP  **Choices:**   - `false` - `true` |
| **upstream_password**  string | Password to access upstream repository.  When this parameter is set, the module will not be idempotent. |
| **upstream_username**  string | username to access upstream repository |
| **url**  string | Repository URL to sync from |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |
| **verify_ssl_on_sync**  boolean | verify the upstream certifcates are signed by a trusted CA  **Choices:**   - `false` - `true` |

## [Attributes](repository_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Notes](repository_module.md#id5)

> **Note:**
>
> - You can configure certain aspects of existing Red Hat Repositories (like *download_policy*) using this module, but you can’t create (enable) or delete (disable) them.
> - If you want to enable or disable Red Hat Repositories available through your subscription, please use the [theforeman.foreman.repository_set](repository_set_module.md#ansible-collections-theforeman-foreman-repository-set-module) module instead.

## [Examples](repository_module.md#id6)

```yaml+jinja
- name: "Create repository"
  theforeman.foreman.repository:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "My repository"
    state: present
    content_type: "yum"
    product: "My Product"
    organization: "Default Organization"
    url: "http://yum.theforeman.org/plugins/latest/el7/x86_64/"
    mirror_on_sync: true
    download_policy: immediate

- name: "Create repository with content credentials"
  theforeman.foreman.repository:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "My repository 2"
    state: present
    content_type: "yum"
    product: "My Product"
    organization: "Default Organization"
    url: "http://yum.theforeman.org/releases/latest/el7/x86_64/"
    download_policy: on_demand
    mirror_on_sync: true
    gpg_key: RPM-GPG-KEY-my-product2
```

## [Return Values](repository_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  **Returned:** success |
| **repositories**  list / elements=dictionary | List of repositories.  **Returned:** success |

### Authors

- Eric D Helms (@ehelms)

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
