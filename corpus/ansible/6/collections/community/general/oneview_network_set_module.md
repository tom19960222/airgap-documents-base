---
collection: ansible
version: "6"
title: "community.general.oneview_network_set module – Manage HPE OneView Network Set resources"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/oneview_network_set_module.html
fetched_at: 2026-07-27T17:11:29+00:00
---
# community.general.oneview_network_set module – Manage HPE OneView Network Set resources

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
> see [Requirements](oneview_network_set_module.md#ansible-collections-community-general-oneview-network-set-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.oneview_network_set`.

- [Synopsis](oneview_network_set_module.md#synopsis)
- [Requirements](oneview_network_set_module.md#requirements)
- [Parameters](oneview_network_set_module.md#parameters)
- [Notes](oneview_network_set_module.md#notes)
- [Examples](oneview_network_set_module.md#examples)
- [Return Values](oneview_network_set_module.md#return-values)

## [Synopsis](oneview_network_set_module.md#id1)

- Provides an interface to manage Network Set resources. Can create, update, or delete.

## [Requirements](oneview_network_set_module.md#id2)

The below requirements are needed on the host that executes this module.

- hpOneView >= 4.0.0
- python >= 2.7.9

## [Parameters](oneview_network_set_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_version**  integer | OneView API Version. |
| **config**  path | Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section. |
| **data**  dictionary / required | List with the Network Set properties. |
| **hostname**  string | IP address or hostname for the appliance. |
| **image_streamer_hostname**  string | IP address or hostname for the HPE Image Streamer REST API. |
| **password**  string | Password for API authentication. |
| **state**  string | Indicates the desired state for the Network Set resource. - `present` will ensure data properties are compliant with OneView. - `absent` will remove the resource from OneView, if it exists.  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  string | Username for API authentication. |
| **validate_etag**  boolean | When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  Choices:   - `false` - `true` ← (default) |

## [Notes](oneview_network_set_module.md#id4)

> **Note:**
>
> - A sample configuration file for the config parameter can be found at: <https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json>
> - Check how to use environment variables for configuration at: <https://github.com/HewlettPackard/oneview-ansible#environment-variables>
> - Additional Playbooks for the HPE OneView Ansible modules can be found at: <https://github.com/HewlettPackard/oneview-ansible/tree/master/examples>
> - The OneView API version used will directly affect returned and expected fields in resources. Information on setting the desired API version and can be found at: <https://github.com/HewlettPackard/oneview-ansible#setting-your-oneview-version>

## [Examples](oneview_network_set_module.md#id5)

```yaml+jinja
- name: Create a Network Set
  community.general.oneview_network_set:
    config: /etc/oneview/oneview_config.json
    state: present
    data:
      name: OneViewSDK Test Network Set
      networkUris:
        - Test Ethernet Network_1                                       # can be a name
        - /rest/ethernet-networks/e4360c9d-051d-4931-b2aa-7de846450dd8  # or a URI
  delegate_to: localhost

- name: Update the Network Set name to 'OneViewSDK Test Network Set - Renamed' and change the associated networks
  community.general.oneview_network_set:
    config: /etc/oneview/oneview_config.json
    state: present
    data:
      name: OneViewSDK Test Network Set
      newName: OneViewSDK Test Network Set - Renamed
      networkUris:
        - Test Ethernet Network_1
  delegate_to: localhost

- name: Delete the Network Set
  community.general.oneview_network_set:
    config: /etc/oneview/oneview_config.json
    state: absent
    data:
        name: OneViewSDK Test Network Set - Renamed
  delegate_to: localhost

- name: Update the Network set with two scopes
  community.general.oneview_network_set:
    config: /etc/oneview/oneview_config.json
    state: present
    data:
      name: OneViewSDK Test Network Set
      scopeUris:
        - /rest/scopes/01SC123456
        - /rest/scopes/02SC123456
  delegate_to: localhost
```

## [Return Values](oneview_network_set_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **network_set**  dictionary | Has the facts about the Network Set.  Returned: On state ‘present’, but can be null. |

### Authors

- Felipe Bulsoni (@fgbulsoni)
- Thiago Miotto (@tmiotto)
- Adriane Cardozo (@adriane-cardozo)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
