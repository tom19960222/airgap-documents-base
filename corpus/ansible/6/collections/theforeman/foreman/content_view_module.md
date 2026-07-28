---
collection: ansible
version: "6"
title: "theforeman.foreman.content_view module – Manage Content Views"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/content_view_module.html
fetched_at: 2026-07-28T00:20:37+00:00
---
# theforeman.foreman.content_view module – Manage Content Views

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
> see [Requirements](content_view_module.md#ansible-collections-theforeman-foreman-content-view-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.content_view`.

New in theforeman.foreman 1.0.0

- [Synopsis](content_view_module.md#synopsis)
- [Requirements](content_view_module.md#requirements)
- [Parameters](content_view_module.md#parameters)
- [Examples](content_view_module.md#examples)
- [Return Values](content_view_module.md#return-values)

## [Synopsis](content_view_module.md#id1)

- Create and manage content views

## [Requirements](content_view_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](content_view_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auto_publish**  boolean | Auto publish composite view when a new version of a component content view is created.  Also note auto publish will only happen when the component is marked “latest”.  Choices:   - `false` ← (default) - `true` |
| **components**  list / elements=dictionary | List of content views to includes content_view and either version or latest.  Ignored if *composite=False*. |
| **content_view**  string / required | Content View name to be added to the Composite Content View |
| **content_view_version**  aliases: version  string | Version of the Content View to add |
| **latest**  boolean | Always use the latest Content View Version  Choices:   - `false` ← (default) - `true` |
| **composite**  boolean | A composite view contains other content views.  Choices:   - `false` ← (default) - `true` |
| **description**  string | Description of the Content View |
| **label**  string | Label of the Content View. This field cannot be updated. |
| **name**  string / required | Name of the Content View |
| **organization**  string / required | Organization that the entity is in |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **repositories**  list / elements=dictionary | List of repositories that include name and product.  Cannot be combined with *composite=True*. |
| **name**  string / required | Name of the Repository to be added |
| **product**  string / required | Product of the Repository to be added |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **solve_dependencies**  boolean | Solve RPM dependencies by default on Content View publish  Choices:   - `false` - `true` |
| **state**  string | State of the entity  `present_with_defaults` will ensure the entity exists, but won’t update existing ones  Choices:   - `"present"` ← (default) - `"present_with_defaults"` - `"absent"` |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Examples](content_view_module.md#id4)

```yaml+jinja
- name: "Create or update Fedora content view"
  theforeman.foreman.content_view:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "Fedora CV"
    organization: "My Cool new Organization"
    repositories:
      - name: 'Fedora 26'
        product: 'Fedora'

- name: "Create a composite content view"
  theforeman.foreman.content_view:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "Fedora CCV"
    organization: "My Cool new Organization"
    composite: true
    auto_publish: true
    components:
      - content_view: Fedora CV
        content_view_version: 1.0
      - content_view: Internal CV
        latest: true
```

## [Return Values](content_view_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  Returned: success |
| **content_views**  list / elements=dictionary | List of content views.  Returned: success |

### Authors

- Eric D Helms (@ehelms)

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
