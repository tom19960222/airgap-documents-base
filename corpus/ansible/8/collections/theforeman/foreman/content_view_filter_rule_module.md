---
collection: ansible
version: "8"
title: "theforeman.foreman.content_view_filter_rule module – Manage content view filter rules"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/content_view_filter_rule_module.html
fetched_at: 2026-07-28T02:55:48+00:00
---
# theforeman.foreman.content_view_filter_rule module – Manage content view filter rules

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
> see [Requirements](content_view_filter_rule_module.md#ansible-collections-theforeman-foreman-content-view-filter-rule-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.content_view_filter_rule`.

New in theforeman.foreman 3.9.0

- [Synopsis](content_view_filter_rule_module.md#synopsis)
- [Requirements](content_view_filter_rule_module.md#requirements)
- [Parameters](content_view_filter_rule_module.md#parameters)
- [Attributes](content_view_filter_rule_module.md#attributes)
- [Examples](content_view_filter_rule_module.md#examples)
- [Return Values](content_view_filter_rule_module.md#return-values)

## [Synopsis](content_view_filter_rule_module.md#id1)

- Create, manage and remove content view filter rules

## [Requirements](content_view_filter_rule_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](content_view_filter_rule_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **architecture**  aliases: arch  string | set package, module_stream, etc. architecture that the rule applies to |
| **content_view**  string / required | the name of the content view that the filter applies to |
| **content_view_filter**  string / required | the name of the content view filter that the rule applies to |
| **context**  string | the context for a module  only valid in filter *type=modulemd* |
| **date_type**  string | set whether rule applied to erratum using the ‘Issued On’ or ‘Updated On’ date  only valid on filter *type=erratum*.  **Choices:**   - `"issued"` - `"updated"` ← (default) |
| **end_date**  string | the rule limit for erratum end date (YYYY-MM-DD)  see date_type for the date the rule applies to  Only valid on *filter_type=erratum_by_date*. |
| **errata_id**  string | erratum id |
| **max_version**  string | package maximum version |
| **min_version**  string | package minimum version |
| **name**  aliases: rule_name, module_name, package_name, package_group, tag  string | Content view filter rule name, package name, package_group name, module stream or docker tag  If omitted, the value of *name* will be used if necessary  for module stream filters, this is the name of the module stream to search for |
| **organization**  string / required | Organization that the entity is in |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **start_date**  string | the rule limit for erratum start date (YYYY-MM-DD)  see date_type for the date the rule applies to  Only valid on *filter_type=erratum*. |
| **state**  string | State of the entity  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **stream**  string | the context for a module  only valid in filter *type=modulemd* |
| **types**  list / elements=string | errata types the ruel applies to (enhancement, bugfix, security)  Only valid on *filter_type=erratum*  **Default:** `["bugfix", "enhancement", "security"]` |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |
| **version**  string | package or module version |

## [Attributes](content_view_filter_rule_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Examples](content_view_filter_rule_module.md#id5)

```yaml+jinja
- name: "Include errata by date"
  theforeman.foreman.content_view_filter_rule:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    organization: "Default Organization"
    content_view: "Standard Operating Environment"
    content_view_filter: "errata_by_date"
    state: present
    inclusion: true
    date_type: updated
    types:
      - bugfix
      - security
      - enhancement
    end_date: "2022-05-25"

- name: "Exclude csh versions 6.20 and older"
  theforeman.foreman.content_view_filter:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    organization: "Default Organization"
    content_view: "Standard Operating Environment"
    content_view_filter: "package filter 1"
    name: "tcsh"
    max_version: "6.20.00"

- name: "Exclude csh version 6.23 due to example policy"
  theforeman.foreman.content_view_filter:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    organization: "Default Organization"
    content_view: "Standard Operating Environment"
    content_view_filter: "package filter 1"
    name: "tcsh"
    version: "6.23.00"

- name: "Content View Filter Rule for 389"
  content_view_filter_rule:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    validate_certs: "true"
    organization: "Default Organization"
    content_view: "Standard Operating Environment"
    content_view_filter: "modulemd filter"
    name: "389-directory-server"
    stream: "next"
    version: "820220325123957"
    context: "9edba152"
    state: present
```

## [Return Values](content_view_filter_rule_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  **Returned:** success |
| **content_view_filters_rules**  list / elements=dictionary | List of content view filter rule(s).  **Returned:** success |

### Authors

- Paul Armstrong (@parmstro)

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
