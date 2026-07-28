---
collection: ansible
version: "6"
title: "community.general.clc_blueprint_package module – Deploys a blue print package on a set of servers in CenturyLink Cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/clc_blueprint_package_module.html
fetched_at: 2026-07-27T17:08:24+00:00
---
# community.general.clc_blueprint_package module – Deploys a blue print package on a set of servers in CenturyLink Cloud

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
> see [Requirements](clc_blueprint_package_module.md#ansible-collections-community-general-clc-blueprint-package-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.clc_blueprint_package`.

- [Synopsis](clc_blueprint_package_module.md#synopsis)
- [Requirements](clc_blueprint_package_module.md#requirements)
- [Parameters](clc_blueprint_package_module.md#parameters)
- [Notes](clc_blueprint_package_module.md#notes)
- [Examples](clc_blueprint_package_module.md#examples)
- [Return Values](clc_blueprint_package_module.md#return-values)

## [Synopsis](clc_blueprint_package_module.md#id1)

- An Ansible module to deploy blue print package on a set of servers in CenturyLink Cloud.

## [Requirements](clc_blueprint_package_module.md#id2)

The below requirements are needed on the host that executes this module.

- python = 2.7
- requests >= 2.5.0
- clc-sdk

## [Parameters](clc_blueprint_package_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **package_id**  string / required | The package id of the blue print. |
| **package_params**  dictionary | The dictionary of arguments required to deploy the blue print.  Default: `{}` |
| **server_ids**  list / elements=string / required | A list of server Ids to deploy the blue print package. |
| **state**  string | Whether to install or uninstall the package. Currently it supports only “present” for install action.  Choices:   - `"present"` ← (default) |
| **wait**  string | Whether to wait for the tasks to finish before returning.  Default: `"True"` |

## [Notes](clc_blueprint_package_module.md#id4)

> **Note:**
>
> - To use this module, it is required to set the below environment variables which enables access to the Centurylink Cloud - CLC_V2_API_USERNAME, the account login id for the centurylink cloud - CLC_V2_API_PASSWORD, the account password for the centurylink cloud
> - Alternatively, the module accepts the API token and account alias. The API token can be generated using the CLC account login and password via the HTTP api call @ <https://api.ctl.io/v2/authentication/login> - CLC_V2_API_TOKEN, the API token generated from <https://api.ctl.io/v2/authentication/login> - CLC_ACCT_ALIAS, the account alias associated with the centurylink cloud
> - Users can set CLC_V2_API_URL to specify an endpoint for pointing to a different CLC environment.

## [Examples](clc_blueprint_package_module.md#id5)

```yaml+jinja
# Note - You must set the CLC_V2_API_USERNAME And CLC_V2_API_PASSWD Environment variables before running these examples

- name: Deploy package
  community.general.clc_blueprint_package:
        server_ids:
            - UC1TEST-SERVER1
            - UC1TEST-SERVER2
        package_id: 77abb844-579d-478d-3955-c69ab4a7ba1a
        package_params: {}
```

## [Return Values](clc_blueprint_package_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **server_ids**  list / elements=string | The list of server ids that are changed  Returned: success  Sample: `["UC1TEST-SERVER1", "UC1TEST-SERVER2"]` |

### Authors

- CLC Runner (@clc-runner)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
