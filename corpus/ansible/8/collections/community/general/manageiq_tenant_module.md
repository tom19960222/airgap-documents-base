---
collection: ansible
version: "8"
title: "community.general.manageiq_tenant module – Management of tenants in ManageIQ"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/manageiq_tenant_module.html
fetched_at: 2026-07-28T01:47:51+00:00
---
# community.general.manageiq_tenant module – Management of tenants in ManageIQ

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
> see [Requirements](manageiq_tenant_module.md#ansible-collections-community-general-manageiq-tenant-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.manageiq_tenant`.

- [Synopsis](manageiq_tenant_module.md#synopsis)
- [Requirements](manageiq_tenant_module.md#requirements)
- [Parameters](manageiq_tenant_module.md#parameters)
- [Attributes](manageiq_tenant_module.md#attributes)
- [Examples](manageiq_tenant_module.md#examples)
- [Return Values](manageiq_tenant_module.md#return-values)

## [Synopsis](manageiq_tenant_module.md#id1)

- The manageiq_tenant module supports adding, updating and deleting tenants in ManageIQ.

Aliases: remote_management.manageiq.manageiq_tenant

## [Requirements](manageiq_tenant_module.md#id2)

The below requirements are needed on the host that executes this module.

- manageiq-client
- manageiq-client <https://github.com/ManageIQ/manageiq-api-client-python/>

## [Parameters](manageiq_tenant_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string / required | The tenant description. |
| **manageiq_connection**  dictionary | ManageIQ connection configuration information. |
| **ca_cert**  aliases: ca_bundle_path  string | The path to a CA bundle file or directory with certificates. |
| **password**  string | ManageIQ password. `MIQ_PASSWORD` environment variable if set. Otherwise, required if no token is passed in. |
| **token**  string | ManageIQ token. `MIQ_TOKEN` environment variable if set. Otherwise, required if no username or password is passed in. |
| **url**  string | ManageIQ environment URL. `MIQ_URL` environment variable if set. Otherwise, it is required to pass it. |
| **username**  string | ManageIQ username. `MIQ_USERNAME` environment variable if set. Otherwise, required if no token is passed in. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether SSL certificates should be verified for HTTPS requests.  **Choices:**   - `false` - `true` ← (default) |
| **name**  string / required | The tenant name. |
| **parent**  string | The name of the parent tenant. If not supplied and no `parent_id` is supplied the root tenant is used. |
| **parent_id**  integer | The id of the parent tenant. If not supplied the root tenant is used.  The `parent_id` takes president over `parent` when supplied |
| **quotas**  dictionary | The tenant quotas.  All parameters case sensitive.  Valid attributes are:  - `cpu_allocated` (int): use null to remove the quota. - `mem_allocated` (GB): use null to remove the quota. - `storage_allocated` (GB): use null to remove the quota. - `vms_allocated` (int): use null to remove the quota. - `templates_allocated` (int): use null to remove the quota.  **Default:** `{}` |
| **state**  string | absent - tenant should not exist, present - tenant should be.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Attributes](manageiq_tenant_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](manageiq_tenant_module.md#id5)

```yaml+jinja
- name: Update the root tenant in ManageIQ
  community.general.manageiq_tenant:
    name: 'My Company'
    description: 'My company name'
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      validate_certs: false

- name: Create a tenant in ManageIQ
  community.general.manageiq_tenant:
    name: 'Dep1'
    description: 'Manufacturing department'
    parent_id: 1
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      validate_certs: false

- name: Delete a tenant in ManageIQ
  community.general.manageiq_tenant:
    state: 'absent'
    name: 'Dep1'
    parent_id: 1
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      validate_certs: false

- name: Set tenant quota for cpu_allocated, mem_allocated, remove quota for vms_allocated
  community.general.manageiq_tenant:
    name: 'Dep1'
    parent_id: 1
    quotas:
      - cpu_allocated: 100
      - mem_allocated: 50
      - vms_allocated: null
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      validate_certs: false

- name: Delete a tenant in ManageIQ using a token
  community.general.manageiq_tenant:
    state: 'absent'
    name: 'Dep1'
    parent_id: 1
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      token: 'sometoken'
      validate_certs: false
```

## [Return Values](manageiq_tenant_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **tenant**  complex | The tenant.  **Returned:** success |
| **description**  string | The tenant description  **Returned:** success |
| **id**  integer | The tenant id  **Returned:** success |
| **name**  string | The tenant name  **Returned:** success |
| **parent_id**  integer | The id of the parent tenant  **Returned:** success |
| **quotas**  list / elements=string | List of tenant quotas  **Returned:** success  **Sample:** `{"cpu_allocated": 100, "mem_allocated": 50}` |

### Authors

- Evert Mulder (@evertmulder)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
