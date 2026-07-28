---
collection: ansible
version: "6"
title: "theforeman.foreman.repository_set module – Enable/disable Red Hat Repositories available through subscriptions"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/repository_set_module.html
fetched_at: 2026-07-28T00:21:02+00:00
---
# theforeman.foreman.repository_set module – Enable/disable Red Hat Repositories available through subscriptions

> **Note:**
>
> This module is part of the [theforeman.foreman collection](https://galaxy.ansible.com/theforeman/foreman) (version 3.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install theforeman.foreman`.
> You need further requirements to be able to use this module,
> see [Requirements](repository_set_module.md#ansible-collections-theforeman-foreman-repository-set-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.repository_set`.

New in theforeman.foreman 1.0.0

- [Synopsis](repository_set_module.md#synopsis)
- [Requirements](repository_set_module.md#requirements)
- [Parameters](repository_set_module.md#parameters)
- [Examples](repository_set_module.md#examples)
- [Return Values](repository_set_module.md#return-values)

## [Synopsis](repository_set_module.md#id1)

- Enable/disable Red Hat Repositories that are available through subscriptions

## [Requirements](repository_set_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](repository_set_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **all_repositories**  boolean | Affect all available repositories in the repository set instead of listing them in *repositories*.  Required when *repositories* is unset or an empty list.  Choices:   - `false` - `true` |
| **label**  string | Label of the repository set, can be used in place of *name* & *product* |
| **name**  string | Name of the repository set |
| **organization**  string / required | Organization that the entity is in |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **product**  string | Name of the parent product |
| **repositories**  list / elements=dictionary | Release version and base architecture of the repositories to enable.  Some reposotory sets require only *basearch* or only *releasever* to be set.  See the examples how you can obtain this information using [theforeman.foreman.resource_info](resource_info_module.md#ansible-collections-theforeman-foreman-resource-info-module).  Required when *all_repositories* is unset or `false`. |
| **basearch**  string | Basearch of the repository to enable. |
| **releasever**  string | Releasever of the repository to enable. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | Whether the repositories are enabled or not  Choices:   - `"enabled"` ← (default) - `"disabled"` |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Examples](repository_set_module.md#id4)

```yaml+jinja
- name: "Enable RHEL 7 RPMs repositories"
  theforeman.foreman.repository_set:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "Red Hat Enterprise Linux 7 Server (RPMs)"
    organization: "Default Organization"
    product: "Red Hat Enterprise Linux Server"
    repositories:
    - releasever: "7.0"
      basearch: "x86_64"
    - releasever: "7.1"
      basearch: "x86_64"
    - releasever: "7.2"
      basearch: "x86_64"
    - releasever: "7.3"
      basearch: "x86_64"
    state: enabled

- name: "Enable RHEL 7 RPMs repositories with label"
  theforeman.foreman.repository_set:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    organization: "Default Organization"
    label: rhel-7-server-rpms
    repositories:
    - releasever: "7.0"
      basearch: "x86_64"
    - releasever: "7.1"
      basearch: "x86_64"
    - releasever: "7.2"
      basearch: "x86_64"
    - releasever: "7.3"
      basearch: "x86_64"
    state: enabled

- name: "Disable RHEL 7 Extras RPMs repository"
  theforeman.foreman.repository_set:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: Red Hat Enterprise Linux 7 Server - Extras (RPMs)
    organization: "Default Organization"
    product: Red Hat Enterprise Linux Server
    state: disabled
    repositories:
      - basearch: x86_64

- name: "Enable RHEL 8 BaseOS RPMs repository with label"
  theforeman.foreman.repository_set:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    organization: "Default Organization"
    label: rhel-8-for-x86_64-baseos-rpms
    repositories:
      - releasever: "8"

- name: "Enable Red Hat Virtualization Manager RPMs repository with label"
  theforeman.foreman.repository_set:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    organization: "Default Organization"
    label: "rhel-7-server-rhv-4.2-manager-rpms"
    repositories:
      - basearch: x86_64
    state: enabled

- name: "Enable Red Hat Virtualization Manager RPMs repository without specifying basearch"
  theforeman.foreman.repository_set:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    organization: "Default Organization"
    label: "rhel-7-server-rhv-4.2-manager-rpms"
    all_repositories: true
    state: enabled

- name: "Search for possible repository sets of a product"
  theforeman.foreman.resource_info:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    organization: "Default Organization"
    resource: repository_sets
    search: product_name="Red Hat Virtualization Manager"
  register: data
- name: "Output found repository sets, see the contentUrl section for possible repository substitutions"
  debug:
    var: data

- name: "Search for possible repository sets by label"
  theforeman.foreman.resource_info:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    organization: "Default Organization"
    resource: repository_sets
    search: label=rhel-7-server-rhv-4.2-manager-rpms
  register: data
- name: "Output found repository sets, see the contentUrl section for possible repository substitutions"
  debug:
    var: data

- name: Enable set with and without all_repositories at the same time
  theforeman.foreman.repository_set:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    organization: "Default Organization"
    label: "{{ item.label }}"
    repositories: "{{ item.repositories | default(omit) }}"
    all_repositories: "{{ item.repositories is not defined }}"
    state: enabled
  loop:
    - label: rhel-7-server-rpms
      repositories:
        - releasever: "7Server"
          basearch: "x86_64"
    - label: rhel-7-server-rhv-4.2-manager-rpms
```

## [Return Values](repository_set_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  Returned: success |
| **repository_sets**  list / elements=dictionary | List of repository sets.  Returned: success |

### Authors

- Andrew Kofink (@akofink)

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
