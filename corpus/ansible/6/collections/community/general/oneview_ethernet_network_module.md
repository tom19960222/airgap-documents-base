---
collection: ansible
version: "6"
title: "community.general.oneview_ethernet_network module – Manage OneView Ethernet Network resources"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/oneview_ethernet_network_module.html
fetched_at: 2026-07-27T17:11:24+00:00
---
# community.general.oneview_ethernet_network module – Manage OneView Ethernet Network resources

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
> see [Requirements](oneview_ethernet_network_module.md#ansible-collections-community-general-oneview-ethernet-network-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.oneview_ethernet_network`.

- [Synopsis](oneview_ethernet_network_module.md#synopsis)
- [Requirements](oneview_ethernet_network_module.md#requirements)
- [Parameters](oneview_ethernet_network_module.md#parameters)
- [Notes](oneview_ethernet_network_module.md#notes)
- [Examples](oneview_ethernet_network_module.md#examples)
- [Return Values](oneview_ethernet_network_module.md#return-values)

## [Synopsis](oneview_ethernet_network_module.md#id1)

- Provides an interface to manage Ethernet Network resources. Can create, update, or delete.

## [Requirements](oneview_ethernet_network_module.md#id2)

The below requirements are needed on the host that executes this module.

- hpOneView >= 3.1.0
- python >= 2.7.9

## [Parameters](oneview_ethernet_network_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_version**  integer | OneView API Version. |
| **config**  path | Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section. |
| **data**  dictionary / required | List with Ethernet Network properties. |
| **hostname**  string | IP address or hostname for the appliance. |
| **image_streamer_hostname**  string | IP address or hostname for the HPE Image Streamer REST API. |
| **password**  string | Password for API authentication. |
| **state**  string | Indicates the desired state for the Ethernet Network resource. - `present` will ensure data properties are compliant with OneView. - `absent` will remove the resource from OneView, if it exists. - `default_bandwidth_reset` will reset the network connection template to the default.  Choices:   - `"present"` ← (default) - `"absent"` - `"default_bandwidth_reset"` |
| **username**  string | Username for API authentication. |
| **validate_etag**  boolean | When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  Choices:   - `false` - `true` ← (default) |

## [Notes](oneview_ethernet_network_module.md#id4)

> **Note:**
>
> - A sample configuration file for the config parameter can be found at: <https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json>
> - Check how to use environment variables for configuration at: <https://github.com/HewlettPackard/oneview-ansible#environment-variables>
> - Additional Playbooks for the HPE OneView Ansible modules can be found at: <https://github.com/HewlettPackard/oneview-ansible/tree/master/examples>
> - The OneView API version used will directly affect returned and expected fields in resources. Information on setting the desired API version and can be found at: <https://github.com/HewlettPackard/oneview-ansible#setting-your-oneview-version>

## [Examples](oneview_ethernet_network_module.md#id5)

```yaml+jinja
- name: Ensure that the Ethernet Network is present using the default configuration
  community.general.oneview_ethernet_network:
    config: '/etc/oneview/oneview_config.json'
    state: present
    data:
      name: 'Test Ethernet Network'
      vlanId: '201'
  delegate_to: localhost

- name: Update the Ethernet Network changing bandwidth and purpose
  community.general.oneview_ethernet_network:
    config: '/etc/oneview/oneview_config.json'
    state: present
    data:
      name: 'Test Ethernet Network'
      purpose: Management
      bandwidth:
          maximumBandwidth: 3000
          typicalBandwidth: 2000
  delegate_to: localhost

- name: Ensure that the Ethernet Network is present with name 'Renamed Ethernet Network'
  community.general.oneview_ethernet_network:
    config: '/etc/oneview/oneview_config.json'
    state: present
    data:
      name: 'Test Ethernet Network'
      newName: 'Renamed Ethernet Network'
  delegate_to: localhost

- name: Ensure that the Ethernet Network is absent
  community.general.oneview_ethernet_network:
    config: '/etc/oneview/oneview_config.json'
    state: absent
    data:
      name: 'New Ethernet Network'
  delegate_to: localhost

- name: Create Ethernet networks in bulk
  community.general.oneview_ethernet_network:
    config: '/etc/oneview/oneview_config.json'
    state: present
    data:
      vlanIdRange: '1-10,15,17'
      purpose: General
      namePrefix: TestNetwork
      smartLink: false
      privateNetwork: false
      bandwidth:
        maximumBandwidth: 10000
        typicalBandwidth: 2000
  delegate_to: localhost

- name: Reset to the default network connection template
  community.general.oneview_ethernet_network:
    config: '/etc/oneview/oneview_config.json'
    state: default_bandwidth_reset
    data:
      name: 'Test Ethernet Network'
  delegate_to: localhost
```

## [Return Values](oneview_ethernet_network_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ethernet_network**  dictionary | Has the facts about the Ethernet Networks.  Returned: On state ‘present’. Can be null. |
| **ethernet_network_bulk**  dictionary | Has the facts about the Ethernet Networks affected by the bulk insert.  Returned: When ‘vlanIdRange’ attribute is in data argument. Can be null. |
| **ethernet_network_connection_template**  dictionary | Has the facts about the Ethernet Network Connection Template.  Returned: On state ‘default_bandwidth_reset’. Can be null. |

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
