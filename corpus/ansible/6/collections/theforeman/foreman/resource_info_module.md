---
collection: ansible
version: "6"
title: "theforeman.foreman.resource_info module – Gather information about resources"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/resource_info_module.html
fetched_at: 2026-07-28T00:21:04+00:00
---
# theforeman.foreman.resource_info module – Gather information about resources

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
> see [Requirements](resource_info_module.md#ansible-collections-theforeman-foreman-resource-info-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.resource_info`.

New in theforeman.foreman 1.0.0

- [Synopsis](resource_info_module.md#synopsis)
- [Requirements](resource_info_module.md#requirements)
- [Parameters](resource_info_module.md#parameters)
- [Notes](resource_info_module.md#notes)
- [Examples](resource_info_module.md#examples)
- [Return Values](resource_info_module.md#return-values)

## [Synopsis](resource_info_module.md#id1)

- Gather information about resources

## [Requirements](resource_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](resource_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **full_details**  aliases: info  boolean | If `True` all details about the found resources are returned  Choices:   - `false` ← (default) - `true` |
| **organization**  string | Scope the searched resource by organization |
| **params**  dictionary | Add parameters to the API call if necessary  If not specified, no additional parameters are passed |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **resource**  string / required | Resource to search  Set to an invalid choice like *foo* see all available options. |
| **search**  string | Search query to use  If None, all resources are returned |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Notes](resource_info_module.md#id4)

> **Note:**
>
> - Some resources don’t support scoping and will return errors when you pass *organization* or unknown data in *params*.

## [Examples](resource_info_module.md#id5)

```yaml+jinja
- name: "Read a Setting"
  theforeman.foreman.resource_info:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    resource: settings
    search: name = foreman_url
  register: result
- debug:
    var: result.resources[0].value

- name: "Read all Registries"
  theforeman.foreman.resource_info:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    resource: registries
  register: result
- debug:
    var: item.name
  with_items: "{{ result.resources }}"

- name: "Read all Organizations with full details"
  theforeman.foreman.resource_info:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    resource: organizations
    full_details: true
  register: result
- debug:
    var: result.resources

- name: Get all existing subscriptions for organization with id 1
  theforeman.foreman.resource_info:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    resource: subscriptions
    params:
      organization_id: 1
  register: result
- debug:
    var: result

- name: Get all existing activation keys for organization ACME
  theforeman.foreman.resource_info:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    resource: activation_keys
    organization: ACME
  register: result
- debug:
    var: result
```

## [Return Values](resource_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resources**  list / elements=string | Resource information  Returned: always |

### Authors

- Sean O’Keeffe (@sean797)

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
