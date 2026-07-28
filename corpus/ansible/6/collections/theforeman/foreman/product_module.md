---
collection: ansible
version: "6"
title: "theforeman.foreman.product module – Manage Products"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/product_module.html
fetched_at: 2026-07-28T00:20:57+00:00
---
# theforeman.foreman.product module – Manage Products

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
> see [Requirements](product_module.md#ansible-collections-theforeman-foreman-product-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.product`.

New in theforeman.foreman 1.0.0

- [Synopsis](product_module.md#synopsis)
- [Requirements](product_module.md#requirements)
- [Parameters](product_module.md#parameters)
- [Examples](product_module.md#examples)
- [Return Values](product_module.md#return-values)

## [Synopsis](product_module.md#id1)

- Create and manage products

## [Requirements](product_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](product_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string | Possibly long description to show the user in detail view |
| **gpg_key**  string | Content GPG key name attached to this product |
| **label**  string | Label to show the user |
| **name**  string / required | Name of the product |
| **organization**  string / required | Organization that the entity is in |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **ssl_ca_cert**  string | Content SSL CA certificate name attached to this product |
| **ssl_client_cert**  string | Content SSL client certificate name attached to this product |
| **ssl_client_key**  string | Content SSL client private key name attached to this product |
| **state**  string | State of the entity  `present_with_defaults` will ensure the entity exists, but won’t update existing ones  Choices:   - `"present"` ← (default) - `"present_with_defaults"` - `"absent"` |
| **sync_plan**  string | Sync plan name attached to this product |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Examples](product_module.md#id4)

```yaml+jinja
- name: "Create Fedora product with a sync plan"
  theforeman.foreman.product:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "Fedora"
    organization: "My Cool new Organization"
    sync_plan: "Fedora repos sync"
    state: present

- name: "Create CentOS 7 product with content credentials"
  theforeman.foreman.product:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "CentOS 7"
    gpg_key: "RPM-GPG-KEY-CentOS7"
    organization: "My Cool new Organization"
    state: present
```

## [Return Values](product_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  Returned: success |
| **products**  list / elements=dictionary | List of products.  Returned: success |

### Authors

- Eric D Helms (@ehelms)
- Matthias Dellweg (@mdellweg) ATIX AG

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
