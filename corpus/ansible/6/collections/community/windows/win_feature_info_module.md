---
collection: ansible
version: "6"
title: "community.windows.win_feature_info module – Gather information about Windows features"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_feature_info_module.html
fetched_at: 2026-07-27T17:23:24+00:00
---
# community.windows.win_feature_info module – Gather information about Windows features

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/community/windows) (version 1.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_feature_info`.

New in community.windows 1.4.0

- [Synopsis](win_feature_info_module.md#synopsis)
- [Parameters](win_feature_info_module.md#parameters)
- [See Also](win_feature_info_module.md#see-also)
- [Examples](win_feature_info_module.md#examples)
- [Return Values](win_feature_info_module.md#return-values)

## [Synopsis](win_feature_info_module.md#id1)

- Gather information about all or a specific installed Windows feature(s).

## [Parameters](win_feature_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  string | If specified, this is used to match the `name` of the Windows feature to get the info for.  Can be a wildcard to match multiple features but the wildcard will only be matched on the `name` of the feature.  If omitted then all features will returned.  Default: `"*"` |

## [See Also](win_feature_info_module.md#id3)

> **See also:**
>
> [ansible.windows.win_feature](../../ansible/windows/win_feature_module.md#ansible-collections-ansible-windows-win-feature-module)
> :   Installs and uninstalls Windows Features on Windows Server.

## [Examples](win_feature_info_module.md#id4)

```yaml+jinja
- name: Get info for all installed features
  community.windows.win_feature_info:
  register: feature_info
- name: Get info for a single feature
  community.windows.win_feature_info:
    name: DNS
  register: feature_info
- name: Find all features that start with 'FS'
  ansible.windows.win_feature_info:
    name: FS*
```

## [Return Values](win_feature_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **exists**  boolean | Whether any features were found based on the criteria specified.  Returned: always  Sample: `true` |
| **features**  list / elements=dictionary | A list of feature(s) that were found based on the criteria.  Will be an empty list if no features were found.  Returned: always |
| **additional_info**  dictionary | A list of privileges that the feature requires and will run with  Returned: success |
| **install_name**  string | The action to perform once triggered, can be `start_feature` or `stop_feature`.  Returned: success  Sample: `"ADCertificateServicesRole"` |
| **major_version**  integer | Major Version of feature `name`.  Returned: success  Sample: `8` |
| **minor_version**  integer | Minor Version of feature `name`.  Returned: success  Sample: `0` |
| **number_id_version**  integer | Numberic Id of feature `name`.  Returned: success  Sample: `16` |
| **best_practices_model_id**  string | BestPracticesModelId for feature `name`.  Returned: success  Sample: `"Microsoft/Windows/UpdateServices"` |
| **depends_on**  list / elements=string | The command line that will be run when a `run_command` failure action is fired.  Returned: success  Sample: `["Web-Static-Content", "Web-Default-Doc"]` |
| **depth**  integer | Depth of `name` feature.  Returned: success  Sample: `1` |
| **description**  string | The description of the feature.  Returned: success  Sample: `"Example description of the Windows feature."` |
| **display_name**  string | The Display name of feature found.  Returned: success  Sample: `"Active Directory Certificate Services"` |
| **event_query**  string | The EventQuery for feature `name`.  This will be `null` if None Present  Returned: success  Sample: `"IPAMServer.Events.xml"` |
| **feature_type**  string | The Feature Type of `name`.  Values will be one of `Role`, `Role Service`, `Feature`.  Returned: success  Sample: `"Feature"` |
| **install_state**  string | The Install State of `name`.  Values will be one of `Available`, `Removed`, `Installed`.  Returned: success  Sample: `"Installed"` |
| **installed**  boolean | Whether the feature by `name` is installed.  Returned: success  Sample: `false` |
| **name**  string | Name of feature found.  Returned: success  Sample: `"AD-Certificate"` |
| **parent**  string | The parent of feature `name` if present.  Returned: success  Sample: `"PowerShellRoot"` |
| **path**  string | The Path of `name` feature.  Returned: success  Sample: `"WoW64 Support"` |
| **post_configuration_needed**  boolean | Tells if Post Configuration is needed for feature `name`.  Returned: success  Sample: `false` |
| **server_component_descriptor**  string | Descriptor of `name` feature.  Returned: success  Sample: `"ServerComponent_AD_Certificate"` |
| **sub_features**  list / elements=string | List of sub features names of feature `name`.  Returned: success  Sample: `["WAS-Process-Model", "WAS-NET-Environment", "WAS-Config-APIs"]` |
| **system_service**  list / elements=string | The name of the service installed by feature `name`.  Returned: success  Sample: `["iisadmin", "w3svc"]` |

### Authors

- Larry Lane (@gamethis)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
