---
collection: ansible
version: "6"
title: "community.general.oneview_fc_network module – Manage OneView Fibre Channel Network resources"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/oneview_fc_network_module.html
fetched_at: 2026-07-27T17:11:25+00:00
---
# community.general.oneview_fc_network module – Manage OneView Fibre Channel Network resources

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
> see [Requirements](oneview_fc_network_module.md#ansible-collections-community-general-oneview-fc-network-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.oneview_fc_network`.

- [Synopsis](oneview_fc_network_module.md#synopsis)
- [Requirements](oneview_fc_network_module.md#requirements)
- [Parameters](oneview_fc_network_module.md#parameters)
- [Notes](oneview_fc_network_module.md#notes)
- [Examples](oneview_fc_network_module.md#examples)
- [Return Values](oneview_fc_network_module.md#return-values)

## [Synopsis](oneview_fc_network_module.md#id1)

- Provides an interface to manage Fibre Channel Network resources. Can create, update, and delete.

## [Requirements](oneview_fc_network_module.md#id2)

The below requirements are needed on the host that executes this module.

- hpOneView >= 4.0.0
- python >= 2.7.9

## [Parameters](oneview_fc_network_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_version**  integer | OneView API Version. |
| **config**  path | Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section. |
| **data**  dictionary / required | List with the Fibre Channel Network properties. |
| **hostname**  string | IP address or hostname for the appliance. |
| **image_streamer_hostname**  string | IP address or hostname for the HPE Image Streamer REST API. |
| **password**  string | Password for API authentication. |
| **state**  string / required | Indicates the desired state for the Fibre Channel Network resource. `present` will ensure data properties are compliant with OneView. `absent` will remove the resource from OneView, if it exists.  Choices:   - `"present"` - `"absent"` |
| **username**  string | Username for API authentication. |
| **validate_etag**  boolean | When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  Choices:   - `false` - `true` ← (default) |

## [Notes](oneview_fc_network_module.md#id4)

> **Note:**
>
> - A sample configuration file for the config parameter can be found at: <https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json>
> - Check how to use environment variables for configuration at: <https://github.com/HewlettPackard/oneview-ansible#environment-variables>
> - Additional Playbooks for the HPE OneView Ansible modules can be found at: <https://github.com/HewlettPackard/oneview-ansible/tree/master/examples>
> - The OneView API version used will directly affect returned and expected fields in resources. Information on setting the desired API version and can be found at: <https://github.com/HewlettPackard/oneview-ansible#setting-your-oneview-version>

## [Examples](oneview_fc_network_module.md#id5)

```yaml+jinja
- name: Ensure that the Fibre Channel Network is present using the default configuration
  community.general.oneview_fc_network:
    config: "{{ config_file_path }}"
    state: present
    data:
      name: 'New FC Network'

- name: Ensure that the Fibre Channel Network is present with fabricType 'DirectAttach'
  community.general.oneview_fc_network:
    config: "{{ config_file_path }}"
    state: present
    data:
      name: 'New FC Network'
      fabricType: 'DirectAttach'

- name: Ensure that the Fibre Channel Network is present and is inserted in the desired scopes
  community.general.oneview_fc_network:
    config: "{{ config_file_path }}"
    state: present
    data:
      name: 'New FC Network'
      scopeUris:
        - '/rest/scopes/00SC123456'
        - '/rest/scopes/01SC123456'

- name: Ensure that the Fibre Channel Network is absent
  community.general.oneview_fc_network:
    config: "{{ config_file_path }}"
    state: absent
    data:
      name: 'New FC Network'
```

## [Return Values](oneview_fc_network_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **fc_network**  dictionary | Has the facts about the managed OneView FC Network.  Returned: On state ‘present’. Can be null. |

### Authors

- Felipe Bulsoni (@fgbulsoni)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
