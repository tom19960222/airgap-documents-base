---
collection: ansible
version: "8"
title: "theforeman.foreman.redhat_manifest module – Interact with a Red Hat Satellite Subscription Manifest"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/redhat_manifest_module.html
fetched_at: 2026-07-28T02:56:25+00:00
---
# theforeman.foreman.redhat_manifest module – Interact with a Red Hat Satellite Subscription Manifest

> **Note:**
>
> This module is part of the [theforeman.foreman collection](https://galaxy.ansible.com/ui/repo/published/theforeman/foreman/) (version 3.15.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install theforeman.foreman`.
>
> To use it in a playbook, specify: `theforeman.foreman.redhat_manifest`.

New in theforeman.foreman 1.0.0

- [Synopsis](redhat_manifest_module.md#synopsis)
- [Parameters](redhat_manifest_module.md#parameters)
- [Examples](redhat_manifest_module.md#examples)
- [Return Values](redhat_manifest_module.md#return-values)

## [Synopsis](redhat_manifest_module.md#id1)

- Download and modify a Red Hat Satellite Subscription Manifest

## [Parameters](redhat_manifest_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **content_access_mode**  string | Content Access Mode of the Subscription Manifest.  Setting *content_access_mode=org_enviroment* enables Simple Content Access.  **Choices:**   - `"org_environment"` - `"entitlement"` ← (default) |
| **name**  string | Manifest Name |
| **password**  string / required | Red Hat Portal password |
| **path**  path | path to export the manifest |
| **pool_id**  string | Subscription pool_id |
| **pool_state**  string | Subscription state  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **portal**  string | Red Hat Portal subscription access address  **Default:** `"https://subscription.rhsm.redhat.com"` |
| **quantity**  integer | quantity of pool_id Subscriptions  **Default:** `1` |
| **state**  string | Manifest state  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  string / required | Red Hat Portal username |
| **uuid**  string | Manifest uuid |
| **validate_certs**  boolean | Validate Portal SSL  **Choices:**   - `false` - `true` ← (default) |

## [Examples](redhat_manifest_module.md#id3)

```yaml+jinja
- name: Create foreman.example.com Manifest and add 7 sub
  theforeman.foreman.redhat_manifest:
    name: "foreman.example.com"
    username: "john-smith"
    password: "changeme"
    pool_id: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    quantity: 7

- name: Ensure my manifest has 10 of one subs in it and export
  theforeman.foreman.redhat_manifest:
    uuid: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
    username: john-smith
    password: changeme
    pool_id: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    quantity: 10
    path: /root/manifest.zip

- name: Remove all of one subs from foreman.example.com
  theforeman.foreman.redhat_manifest:
    name: foreman.example.com
    username: john-smith
    password: changeme
    pool_id: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    pool_state: absent
```

## [Return Values](redhat_manifest_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **uuid**  string  *added in theforeman.foreman 3.8.0* | Manifest UUID  **Returned:** success  **Sample:** `"5349d1d0-5bda-480a-b7bd-ff41e2c29e03"` |

### Authors

- Sean O’Keeffe (@sean797)

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
