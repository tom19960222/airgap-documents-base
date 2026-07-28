---
collection: ansible
version: "6"
title: "community.general.clc_server_snapshot module – Create, Delete and Restore server snapshots in CenturyLink Cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/clc_server_snapshot_module.html
fetched_at: 2026-07-27T17:08:29+00:00
---
# community.general.clc_server_snapshot module – Create, Delete and Restore server snapshots in CenturyLink Cloud

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
> see [Requirements](clc_server_snapshot_module.md#ansible-collections-community-general-clc-server-snapshot-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.clc_server_snapshot`.

- [Synopsis](clc_server_snapshot_module.md#synopsis)
- [Requirements](clc_server_snapshot_module.md#requirements)
- [Parameters](clc_server_snapshot_module.md#parameters)
- [Notes](clc_server_snapshot_module.md#notes)
- [Examples](clc_server_snapshot_module.md#examples)
- [Return Values](clc_server_snapshot_module.md#return-values)

## [Synopsis](clc_server_snapshot_module.md#id1)

- An Ansible module to Create, Delete and Restore server snapshots in CenturyLink Cloud.

## [Requirements](clc_server_snapshot_module.md#id2)

The below requirements are needed on the host that executes this module.

- python = 2.7
- requests >= 2.5.0
- clc-sdk

## [Parameters](clc_server_snapshot_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **expiration_days**  integer | The number of days to keep the server snapshot before it expires.  Default: `7` |
| **server_ids**  list / elements=string / required | The list of CLC server Ids. |
| **state**  string | The state to insure that the provided resources are in.  Choices:   - `"present"` ← (default) - `"absent"` - `"restore"` |
| **wait**  string | Whether to wait for the provisioning tasks to finish before returning.  Default: `"True"` |

## [Notes](clc_server_snapshot_module.md#id4)

> **Note:**
>
> - To use this module, it is required to set the below environment variables which enables access to the Centurylink Cloud - CLC_V2_API_USERNAME, the account login id for the centurylink cloud - CLC_V2_API_PASSWORD, the account password for the centurylink cloud
> - Alternatively, the module accepts the API token and account alias. The API token can be generated using the CLC account login and password via the HTTP api call @ <https://api.ctl.io/v2/authentication/login> - CLC_V2_API_TOKEN, the API token generated from <https://api.ctl.io/v2/authentication/login> - CLC_ACCT_ALIAS, the account alias associated with the centurylink cloud
> - Users can set CLC_V2_API_URL to specify an endpoint for pointing to a different CLC environment.

## [Examples](clc_server_snapshot_module.md#id5)

```yaml+jinja
# Note - You must set the CLC_V2_API_USERNAME And CLC_V2_API_PASSWD Environment variables before running these examples

- name: Create server snapshot
  community.general.clc_server_snapshot:
    server_ids:
        - UC1TEST-SVR01
        - UC1TEST-SVR02
    expiration_days: 10
    wait: true
    state: present

- name: Restore server snapshot
  community.general.clc_server_snapshot:
    server_ids:
        - UC1TEST-SVR01
        - UC1TEST-SVR02
    wait: true
    state: restore

- name: Delete server snapshot
  community.general.clc_server_snapshot:
    server_ids:
        - UC1TEST-SVR01
        - UC1TEST-SVR02
    wait: true
    state: absent
```

## [Return Values](clc_server_snapshot_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **server_ids**  list / elements=string | The list of server ids that are changed  Returned: success  Sample: `["UC1TEST-SVR01", "UC1TEST-SVR02"]` |

### Authors

- CLC Runner (@clc-runner)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
