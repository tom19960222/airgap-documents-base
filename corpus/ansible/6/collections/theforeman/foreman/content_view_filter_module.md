---
collection: ansible
version: "6"
title: "theforeman.foreman.content_view_filter module – Manage Content View Filters"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/content_view_filter_module.html
fetched_at: 2026-07-28T00:20:38+00:00
---
# theforeman.foreman.content_view_filter module – Manage Content View Filters

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
> see [Requirements](content_view_filter_module.md#ansible-collections-theforeman-foreman-content-view-filter-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.content_view_filter`.

New in theforeman.foreman 1.0.0

- [Synopsis](content_view_filter_module.md#synopsis)
- [Requirements](content_view_filter_module.md#requirements)
- [Parameters](content_view_filter_module.md#parameters)
- [Examples](content_view_filter_module.md#examples)
- [Return Values](content_view_filter_module.md#return-values)

## [Synopsis](content_view_filter_module.md#id1)

- Create and manage content View filters

## [Requirements](content_view_filter_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](content_view_filter_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **architecture**  string | package architecture |
| **content_view**  string / required | Name of the content view |
| **date_type**  string | Search using the ‘Issued On’ or ‘Updated On’  Only valid on *filter_type=erratum*.  Choices:   - `"issued"` - `"updated"` ← (default) |
| **description**  string | Description of the Content View Filter |
| **end_date**  string | erratum end date (YYYY-MM-DD) |
| **errata_id**  string | erratum id |
| **filter_state**  string | State of the content view filter  Choices:   - `"present"` ← (default) - `"absent"` |
| **filter_type**  string / required | Content view filter type  Choices:   - `"rpm"` - `"package_group"` - `"erratum"` - `"docker"` |
| **inclusion**  boolean | Create an include filter  Choices:   - `false` ← (default) - `true` |
| **max_version**  string | package maximum version |
| **min_version**  string | package minimum version |
| **name**  string / required | Name of the Content View Filter |
| **organization**  string / required | Organization that the entity is in |
| **original_packages**  boolean | Include all RPMs with no errata  Choices:   - `false` - `true` |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **repositories**  list / elements=dictionary | List of repositories that include name and product  An empty Array means all current and future repositories  Default: `[]` |
| **rule_name**  aliases: package_name, package_group, tag  string | Content view filter rule name or package name  If omitted, the value of *name* will be used if necessary |
| **rule_state**  string | State of the content view filter rule  Choices:   - `"present"` ← (default) - `"absent"` |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **start_date**  string | erratum start date (YYYY-MM-DD) |
| **types**  list / elements=string | erratum types (enhancement, bugfix, security)  Default: `["bugfix", "enhancement", "security"]` |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |
| **version**  string | package version |

## [Examples](content_view_filter_module.md#id4)

```yaml+jinja
- name: Exclude csh
  theforeman.foreman.content_view_filter:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "package filter 1"
    organization: "Default Organization"
    content_view: Web Servers
    filter_type: "rpm"
    package_name: tcsh

- name: Include newer csh versions
  theforeman.foreman.content_view_filter:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "package filter 1"
    organization: "Default Organization"
    content_view: Web Servers
    filter_type: "rpm"
    package_name: tcsh
    min_version: 6.20.00
    inclusion: True
```

## [Return Values](content_view_filter_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  Returned: success |
| **content_view_filters**  list / elements=dictionary | List of content view filters.  Returned: success |

### Authors

- Sean O’Keeffe (@sean797)

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
