---
collection: ansible
version: "6"
title: "community.general.manageiq_group module – Management of groups in ManageIQ"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/manageiq_group_module.html
fetched_at: 2026-07-27T17:10:46+00:00
---
# community.general.manageiq_group module – Management of groups in ManageIQ

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](manageiq_group_module.md#ansible-collections-community-general-manageiq-group-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.manageiq_group`.

- [Synopsis](manageiq_group_module.md#synopsis)
- [Requirements](manageiq_group_module.md#requirements)
- [Parameters](manageiq_group_module.md#parameters)
- [Examples](manageiq_group_module.md#examples)
- [Return Values](manageiq_group_module.md#return-values)

## [Synopsis](manageiq_group_module.md#id1)

- The manageiq_group module supports adding, updating and deleting groups in ManageIQ.

## [Requirements](manageiq_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- manageiq-client
- manageiq-client <https://github.com/ManageIQ/manageiq-api-client-python/>

## [Parameters](manageiq_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **belongsto_filters**  list / elements=string | A list of strings with a reference to the allowed host, cluster or folder |
| **belongsto_filters_merge_mode**  string | In merge mode existing settings are merged with the supplied `belongsto_filters`.  In replace mode current values are replaced with the supplied `belongsto_filters`.  Choices:   - `"merge"` - `"replace"` ← (default) |
| **description**  string / required | The group description. |
| **managed_filters**  dictionary | The tag values per category |
| **managed_filters_merge_mode**  string | In merge mode existing categories are kept or updated, new categories are added.  In replace mode all categories will be replaced with the supplied `managed_filters`.  Choices:   - `"merge"` - `"replace"` ← (default) |
| **manageiq_connection**  dictionary | ManageIQ connection configuration information. |
| **ca_cert**  aliases: ca_bundle_path  string | The path to a CA bundle file or directory with certificates. defaults to None. |
| **password**  string | ManageIQ password. `MIQ_PASSWORD` env var if set. otherwise, required if no token is passed in. |
| **token**  string | ManageIQ token. `MIQ_TOKEN` env var if set. otherwise, required if no username or password is passed in. |
| **url**  string | ManageIQ environment url. `MIQ_URL` env var if set. otherwise, it is required to pass it. |
| **username**  string | ManageIQ username. `MIQ_USERNAME` env var if set. otherwise, required if no token is passed in. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether SSL certificates should be verified for HTTPS requests. defaults to True.  Choices:   - `false` - `true` ← (default) |
| **role**  string | The the group role name  The `role_id` has precedence over the `role` when supplied. |
| **role_id**  integer | The the group role id |
| **state**  string | absent - group should not exist, present - group should be.  Choices:   - `"absent"` - `"present"` ← (default) |
| **tenant**  string | The tenant for the group identified by the tenant name.  The `tenant_id` has precedence over the `tenant` when supplied.  Tenant names are case sensitive. |
| **tenant_id**  integer | The tenant for the group identified by the tenant id. |

## [Examples](manageiq_group_module.md#id4)

```yaml+jinja
- name: Create a group in ManageIQ with the role EvmRole-user and tenant 'my_tenant'
  community.general.manageiq_group:
    description: 'MyGroup-user'
    role: 'EvmRole-user'
    tenant: 'my_tenant'
    manageiq_connection:
      url: 'https://manageiq_server'
      username: 'admin'
      password: 'smartvm'
      validate_certs: false

- name: Create a group in ManageIQ with the role EvmRole-user and tenant with tenant_id 4
  community.general.manageiq_group:
    description: 'MyGroup-user'
    role: 'EvmRole-user'
    tenant_id: 4
    manageiq_connection:
      url: 'https://manageiq_server'
      username: 'admin'
      password: 'smartvm'
      validate_certs: false

- name:
  - Create or update a group in ManageIQ with the role EvmRole-user and tenant my_tenant.
  - Apply 3 prov_max_cpu and 2 department tags to the group.
  - Limit access to a cluster for the group.
  community.general.manageiq_group:
    description: 'MyGroup-user'
    role: 'EvmRole-user'
    tenant: my_tenant
    managed_filters:
      prov_max_cpu:
      - '1'
      - '2'
      - '4'
      department:
      - defense
      - engineering
    managed_filters_merge_mode: replace
    belongsto_filters:
    - "/belongsto/ExtManagementSystem|ProviderName/EmsFolder|Datacenters/EmsFolder|dc_name/EmsFolder|host/EmsCluster|Cluster name"
    belongsto_filters_merge_mode: merge
    manageiq_connection:
      url: 'https://manageiq_server'
      username: 'admin'
      password: 'smartvm'
      validate_certs: false

- name: Delete a group in ManageIQ
  community.general.manageiq_group:
    state: 'absent'
    description: 'MyGroup-user'
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'

- name: Delete a group in ManageIQ using a token
  community.general.manageiq_group:
    state: 'absent'
    description: 'MyGroup-user'
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      token: 'sometoken'
```

## [Return Values](manageiq_group_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **group**  complex | The group.  Returned: success |
| **belongsto_filters**  list / elements=string | A list of strings with a reference to the allowed host, cluster or folder  Returned: success |
| **created_on**  string | Group creation date  Returned: success  Sample: `"2018-08-12T08:37:55+00:00"` |
| **description**  string | The group description  Returned: success |
| **group_type**  string | The group type, system or user  Returned: success |
| **id**  integer | The group id  Returned: success |
| **managed_filters**  dictionary | The tag values per category  Returned: success |
| **role**  string | The group role name  Returned: success |
| **tenant**  string | The group tenant name  Returned: success |
| **updated_on**  integer | Group update date  Returned: success  Sample: `"2018-08-12T08:37:55+00:00"` |

### Authors

- Evert Mulder (@evertmulder)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
