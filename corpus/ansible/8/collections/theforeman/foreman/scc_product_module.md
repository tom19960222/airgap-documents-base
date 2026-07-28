---
collection: ansible
version: "8"
title: "theforeman.foreman.scc_product module – Subscribe SUSE Customer Center Account Products"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/scc_product_module.html
fetched_at: 2026-07-28T02:56:36+00:00
---
# theforeman.foreman.scc_product module – Subscribe SUSE Customer Center Account Products

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
> see [Requirements](scc_product_module.md#ansible-collections-theforeman-foreman-scc-product-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.scc_product`.

New in theforeman.foreman 1.0.0

- [Synopsis](scc_product_module.md#synopsis)
- [Requirements](scc_product_module.md#requirements)
- [Parameters](scc_product_module.md#parameters)
- [Attributes](scc_product_module.md#attributes)
- [Examples](scc_product_module.md#examples)

## [Synopsis](scc_product_module.md#id1)

- Manage SUSE Customer Center Products
- This module requires the foreman_scc_manager plugin set up in the server
- See <https://github.com/ATIX-AG/foreman_scc_manager>

Aliases: foreman_scc_product

## [Requirements](scc_product_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](scc_product_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **organization**  string / required | Organization that the entity is in |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **scc_account**  string / required | Name of the suse customer center account associated with product |
| **scc_product**  aliases: friendly_name  string / required | Full name of the product of suse customer center account.  The *friendly_name* alias is deprecated as it refers to an attribute that does not uniquely identify a product and not used for product lookups since SCC Manager 1.8.6. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](scc_product_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Examples](scc_product_module.md#id5)

```yaml+jinja
- name: "Subscribe to suse customer center product"
  theforeman.foreman.scc_product:
    scc_product: "Product1"
    scc_account: "Test"
    organization: "Test Organization"
```

### Authors

- Manisha Singhal (@manisha15) ATIX AG

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
