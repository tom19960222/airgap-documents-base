---
collection: ansible
version: "8"
title: "theforeman.foreman.location module – Manage Locations"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/location_module.html
fetched_at: 2026-07-28T02:56:13+00:00
---
# theforeman.foreman.location module – Manage Locations

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
> see [Requirements](location_module.md#ansible-collections-theforeman-foreman-location-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.location`.

New in theforeman.foreman 1.0.0

- [Synopsis](location_module.md#synopsis)
- [Requirements](location_module.md#requirements)
- [Parameters](location_module.md#parameters)
- [Attributes](location_module.md#attributes)
- [Examples](location_module.md#examples)
- [Return Values](location_module.md#return-values)

## [Synopsis](location_module.md#id1)

- Manage Locations

Aliases: foreman_location

## [Requirements](location_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](location_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ignore_types**  aliases: select_all_types  list / elements=string  *added in theforeman.foreman 3.8.0* | List of resources types that will be automatically associated |
| **name**  string / required | Name of the Location |
| **organizations**  list / elements=string | List of organizations the location should be assigned to |
| **parameters**  list / elements=dictionary | Entity domain specific host parameters |
| **name**  string / required | Name of the parameter |
| **parameter_type**  string | Type of the parameter  **Choices:**   - `"string"` ← (default) - `"boolean"` - `"integer"` - `"real"` - `"array"` - `"hash"` - `"yaml"` - `"json"` |
| **value**  any / required | Value of the parameter |
| **parent**  string | Title of a parent Location for nesting |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](location_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Examples](location_module.md#id5)

```yaml+jinja
# Create a simple location
- name: "Create CI Location"
  theforeman.foreman.location:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "My Cool New Location"
    organizations:
      - "Default Organization"
    state: present

# Create a nested location
- name: "Create Nested CI Location"
  theforeman.foreman.location:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "My Nested location"
    parent: "My Cool New Location"
    state: present

# Create a new nested location with parent included in name
- name: "Create New Nested Location"
  theforeman.foreman.location:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "My Cool New Location/New nested location"
    state: present

# Move a nested location to another parent
- name: "Create Nested CI Location"
  theforeman.foreman.location:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "My Cool New Location/New nested location"
    parent: "My Cool New Location/My Nested location"
    state: present
```

## [Return Values](location_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  **Returned:** success |
| **locations**  list / elements=dictionary | List of locations.  **Returned:** success |

### Authors

- Matthias M Dellweg (@mdellweg) ATIX AG

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
