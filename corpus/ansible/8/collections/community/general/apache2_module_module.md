---
collection: ansible
version: "8"
title: "community.general.apache2_module module – Enables/disables a module of the Apache2 webserver"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/apache2_module_module.html
fetched_at: 2026-07-28T01:44:40+00:00
---
# community.general.apache2_module module – Enables/disables a module of the Apache2 webserver

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
> see [Requirements](apache2_module_module.md#ansible-collections-community-general-apache2-module-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.apache2_module`.

- [Synopsis](apache2_module_module.md#synopsis)
- [Requirements](apache2_module_module.md#requirements)
- [Parameters](apache2_module_module.md#parameters)
- [Attributes](apache2_module_module.md#attributes)
- [Notes](apache2_module_module.md#notes)
- [Examples](apache2_module_module.md#examples)
- [Return Values](apache2_module_module.md#return-values)

## [Synopsis](apache2_module_module.md#id1)

- Enables or disables a specified module of the Apache2 webserver.

Aliases: web_infrastructure.apache2_module

## [Requirements](apache2_module_module.md#id2)

The below requirements are needed on the host that executes this module.

- a2enmod
- a2dismod

## [Parameters](apache2_module_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **force**  boolean | Force disabling of default modules and override Debian warnings.  **Choices:**   - `false` ← (default) - `true` |
| **identifier**  string | Identifier of the module as listed by `apache2ctl -M`. This is optional and usually determined automatically by the common convention of appending `_module` to `name` as well as custom exception for popular modules. |
| **ignore_configcheck**  boolean | Ignore configuration checks about inconsistent module configuration. Especially for mpm_\* modules.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string / required | Name of the module to enable/disable as given to `a2enmod/a2dismod`. |
| **state**  string | Desired state of the module.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **warn_mpm_absent**  boolean  *added in community.general 6.3.0* | Control the behavior of the warning process for MPM modules.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](apache2_module_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](apache2_module_module.md#id5)

> **Note:**
>
> - This does not work on RedHat-based distributions. It does work on Debian- and SuSE-based distributions. Whether it works on others depend on whether the `a2enmod` and `a2dismod` tools are available or not.

## [Examples](apache2_module_module.md#id6)

```yaml+jinja
- name: Enable the Apache2 module wsgi
  community.general.apache2_module:
    state: present
    name: wsgi

- name: Disables the Apache2 module wsgi
  community.general.apache2_module:
    state: absent
    name: wsgi

- name: Disable default modules for Debian
  community.general.apache2_module:
    state: absent
    name: autoindex
    force: true

- name: Disable mpm_worker and ignore warnings about missing mpm module
  community.general.apache2_module:
    state: absent
    name: mpm_worker
    ignore_configcheck: true

- name: Disable mpm_event, enable mpm_prefork and ignore warnings about missing mpm module
  community.general.apache2_module:
    name: "{{ item.module }}"
    state: "{{ item.state }}"
    warn_mpm_absent: false
    ignore_configcheck: true
  loop:
  - module: mpm_event
    state: absent
  - module: mpm_prefork
    state: present

- name: Enable dump_io module, which is identified as dumpio_module inside apache2
  community.general.apache2_module:
    state: present
    name: dump_io
    identifier: dumpio_module
```

## [Return Values](apache2_module_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **rc**  integer | return code of underlying command  **Returned:** failed |
| **result**  string | message about action taken  **Returned:** always |
| **stderr**  string | stderr of underlying command  **Returned:** failed |
| **stdout**  string | stdout of underlying command  **Returned:** failed |
| **warnings**  list / elements=string | list of warning messages  **Returned:** when needed |

### Authors

- Christian Berendt (@berendt)
- Ralf Hertel (@n0trax)
- Robin Roth (@robinro)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
