---
collection: ansible
version: "6"
title: "community.general.oneview_logical_interconnect_group module – Manage OneView Logical Interconnect Group resources"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/oneview_logical_interconnect_group_module.html
fetched_at: 2026-07-27T17:11:28+00:00
---
# community.general.oneview_logical_interconnect_group module – Manage OneView Logical Interconnect Group resources

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
> see [Requirements](oneview_logical_interconnect_group_module.md#ansible-collections-community-general-oneview-logical-interconnect-group-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.oneview_logical_interconnect_group`.

- [Synopsis](oneview_logical_interconnect_group_module.md#synopsis)
- [Requirements](oneview_logical_interconnect_group_module.md#requirements)
- [Parameters](oneview_logical_interconnect_group_module.md#parameters)
- [Notes](oneview_logical_interconnect_group_module.md#notes)
- [Examples](oneview_logical_interconnect_group_module.md#examples)
- [Return Values](oneview_logical_interconnect_group_module.md#return-values)

## [Synopsis](oneview_logical_interconnect_group_module.md#id1)

- Provides an interface to manage Logical Interconnect Group resources. Can create, update, or delete.

## [Requirements](oneview_logical_interconnect_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- hpOneView >= 4.0.0
- python >= 2.7.9

## [Parameters](oneview_logical_interconnect_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_version**  integer | OneView API Version. |
| **config**  path | Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section. |
| **data**  dictionary / required | List with the Logical Interconnect Group properties. |
| **hostname**  string | IP address or hostname for the appliance. |
| **image_streamer_hostname**  string | IP address or hostname for the HPE Image Streamer REST API. |
| **password**  string | Password for API authentication. |
| **state**  string | Indicates the desired state for the Logical Interconnect Group resource. `absent` will remove the resource from OneView, if it exists. `present` will ensure data properties are compliant with OneView.  Choices:   - `"absent"` - `"present"` ← (default) |
| **username**  string | Username for API authentication. |
| **validate_etag**  boolean | When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  Choices:   - `false` - `true` ← (default) |

## [Notes](oneview_logical_interconnect_group_module.md#id4)

> **Note:**
>
> - A sample configuration file for the config parameter can be found at: <https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json>
> - Check how to use environment variables for configuration at: <https://github.com/HewlettPackard/oneview-ansible#environment-variables>
> - Additional Playbooks for the HPE OneView Ansible modules can be found at: <https://github.com/HewlettPackard/oneview-ansible/tree/master/examples>
> - The OneView API version used will directly affect returned and expected fields in resources. Information on setting the desired API version and can be found at: <https://github.com/HewlettPackard/oneview-ansible#setting-your-oneview-version>

## [Examples](oneview_logical_interconnect_group_module.md#id5)

```yaml+jinja
- name: Ensure that the Logical Interconnect Group is present
  community.general.oneview_logical_interconnect_group:
    config: /etc/oneview/oneview_config.json
    state: present
    data:
      name: Test Logical Interconnect Group
      uplinkSets: []
      enclosureType: C7000
      interconnectMapTemplate:
        interconnectMapEntryTemplates:
          - logicalDownlinkUri: ~
            logicalLocation:
                locationEntries:
                    - relativeValue: 1
                      type: Bay
                    - relativeValue: 1
                      type: Enclosure
            permittedInterconnectTypeName: HP VC Flex-10/10D Module
            # Alternatively you can inform permittedInterconnectTypeUri
  delegate_to: localhost

- name: Ensure that the Logical Interconnect Group has the specified scopes
  community.general.oneview_logical_interconnect_group:
    config: /etc/oneview/oneview_config.json
    state: present
    data:
      name: Test Logical Interconnect Group
      scopeUris:
        - /rest/scopes/00SC123456
        - /rest/scopes/01SC123456
  delegate_to: localhost

- name: Ensure that the Logical Interconnect Group is present with name 'Test'
  community.general.oneview_logical_interconnect_group:
    config: /etc/oneview/oneview_config.json
    state: present
    data:
      name: New Logical Interconnect Group
      newName: Test
  delegate_to: localhost

- name: Ensure that the Logical Interconnect Group is absent
  community.general.oneview_logical_interconnect_group:
    config: /etc/oneview/oneview_config.json
    state: absent
    data:
      name: New Logical Interconnect Group
  delegate_to: localhost
```

## [Return Values](oneview_logical_interconnect_group_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **logical_interconnect_group**  dictionary | Has the facts about the OneView Logical Interconnect Group.  Returned: On state ‘present’. Can be null. |

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
