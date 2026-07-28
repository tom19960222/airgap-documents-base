---
collection: ansible
version: "8"
title: "theforeman.foreman.content_view_filter_rule_info module – Fetch information about a Content View Filter Rule"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/content_view_filter_rule_info_module.html
fetched_at: 2026-07-28T02:55:49+00:00
---
# theforeman.foreman.content_view_filter_rule_info module – Fetch information about a Content View Filter Rule

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
> see [Requirements](content_view_filter_rule_info_module.md#ansible-collections-theforeman-foreman-content-view-filter-rule-info-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.content_view_filter_rule_info`.

New in theforeman.foreman 3.9.0

- [Synopsis](content_view_filter_rule_info_module.md#synopsis)
- [Requirements](content_view_filter_rule_info_module.md#requirements)
- [Parameters](content_view_filter_rule_info_module.md#parameters)
- [Attributes](content_view_filter_rule_info_module.md#attributes)
- [Examples](content_view_filter_rule_info_module.md#examples)
- [Return Values](content_view_filter_rule_info_module.md#return-values)

## [Synopsis](content_view_filter_rule_info_module.md#id1)

- Fetch information about a Content View Filter Rule

## [Requirements](content_view_filter_rule_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](content_view_filter_rule_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **content_view**  string / required | the name of the content view that the filter applies to |
| **content_view_filter**  string / required | the name of the content view filter that the rule applies to |
| **errata_id**  string | for erratum fitlers using errata_by_id, the errata id to search for |
| **location**  string | Label of the Location to scope the search for. |
| **name**  string | Name of the resource to fetch information for.  Mutually exclusive with *search*. |
| **organization**  string / required | Name of the Organization to scope the search for. |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **search**  string | Search query to use  If None, and *name* is not set, all resources are returned.  Mutually exclusive with *name*. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](content_view_filter_rule_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Examples](content_view_filter_rule_info_module.md#id5)

```yaml+jinja
- name: "Show a content_view_filter_rule"
  theforeman.foreman.content_view_filter_info:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    content_view: "SOE_RHEL9"
    content_view_filter: "NoFireFox"
    name: firefox
```

## [Return Values](content_view_filter_rule_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **content_view_filter_rule**  dictionary | Details about the found content_view_filter_rule  **Returned:** success and *name* was passed |
| **content_view_filter_rules**  dictionary | Details about the found content_view_filter_rules  **Returned:** success and the filter type is erratum or modulemd |

### Authors

- Paul Armstrong (@parmstro)

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
