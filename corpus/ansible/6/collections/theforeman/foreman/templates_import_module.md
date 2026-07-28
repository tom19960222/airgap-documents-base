---
collection: ansible
version: "6"
title: "theforeman.foreman.templates_import module – Sync Templates from a repository"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/templates_import_module.html
fetched_at: 2026-07-28T00:21:16+00:00
---
# theforeman.foreman.templates_import module – Sync Templates from a repository

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
> see [Requirements](templates_import_module.md#ansible-collections-theforeman-foreman-templates-import-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.templates_import`.

New in theforeman.foreman 1.0.0

- [Synopsis](templates_import_module.md#synopsis)
- [Requirements](templates_import_module.md#requirements)
- [Parameters](templates_import_module.md#parameters)
- [Notes](templates_import_module.md#notes)
- [Examples](templates_import_module.md#examples)
- [Return Values](templates_import_module.md#return-values)

## [Synopsis](templates_import_module.md#id1)

- Sync provisioning templates, report_templates, partition tables and job templates from external git repository or file system.
- Based on foreman_templates plugin <https://github.com/theforeman/foreman_templates>.

## [Requirements](templates_import_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](templates_import_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **associate**  string | Associate to Operatingsystems, Locations and Organizations based on metadata.  Choices:   - `"always"` - `"new"` - `"never"` |
| **branch**  string | Branch of the *repo*. Only for git-based repositories. |
| **dirname**  string | The directory within Git repo containing the templates. |
| **filter**  string | Sync only templates with name matching this regular expression, after *prefix* was applied.  Case-insensitive, snippets are not filtered. |
| **force**  boolean | Update templates that are locked.  Choices:   - `false` - `true` |
| **locations**  list / elements=string | List of locations the entity should be assigned to |
| **lock**  boolean | Lock imported templates.  Choices:   - `false` - `true` |
| **negate**  boolean | Negate the filter condition.  Choices:   - `false` - `true` |
| **organizations**  list / elements=string | List of organizations the entity should be assigned to |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **prefix**  string | Adds specified string to beginning of all imported templates that do not yet have that prefix. |
| **repo**  string | Filesystem path or repo (with protocol), for example /tmp/dir or git://example.com/repo.git or https://example.com/repo.git. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |
| **verbose**  boolean | Add template reports to the output.  Choices:   - `false` - `true` |

## [Notes](templates_import_module.md#id4)

> **Note:**
>
> - Due to a bug in the foreman_templates plugin, this module won’t report `changed=true` when the only change is the Organization/Location association of the imported templates. Please see <https://projects.theforeman.org/issues/29534> for details.
> - Default values for all module options can be set using [theforeman.foreman.setting](setting_module.md#ansible-collections-theforeman-foreman-setting-module) for TemplateSync category or on the settings page in WebUI.

## [Examples](templates_import_module.md#id5)

```yaml+jinja
- name: Sync templates from git repo
  theforeman.foreman.templates_import:
    repo: https://github.com/theforeman/community-templates.git
    branch: 1.24-stable
    associate: new
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
```

## [Return Values](templates_import_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **message**  dictionary | Information about the import.  Returned: success |
| **branch**  string | Branch used in the repository.  Returned: success |
| **repo**  string | Repository, the templates were imported from.  Returned: success |
| **report**  dictionary | Report of the import.  Returned: success |
| **changed**  list / elements=string | List of templates that have been updated.  Returned: success |
| **new**  list / elements=string | List of templates that have been created.  Returned: success |
| **templates**  dictionary | Final state of the templates.  Returned: success |

### Authors

- Anton Nesterov (@nesanton)

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
