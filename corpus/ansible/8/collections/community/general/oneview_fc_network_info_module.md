---
collection: ansible
version: "8"
title: "community.general.oneview_fc_network_info module – Retrieve the information about one or more of the OneView Fibre Channel Networks"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/oneview_fc_network_info_module.html
fetched_at: 2026-07-28T01:48:32+00:00
---
# community.general.oneview_fc_network_info module – Retrieve the information about one or more of the OneView Fibre Channel Networks

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
> see [Requirements](oneview_fc_network_info_module.md#ansible-collections-community-general-oneview-fc-network-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.oneview_fc_network_info`.

- [Synopsis](oneview_fc_network_info_module.md#synopsis)
- [Requirements](oneview_fc_network_info_module.md#requirements)
- [Parameters](oneview_fc_network_info_module.md#parameters)
- [Attributes](oneview_fc_network_info_module.md#attributes)
- [Notes](oneview_fc_network_info_module.md#notes)
- [Examples](oneview_fc_network_info_module.md#examples)
- [Return Values](oneview_fc_network_info_module.md#return-values)

## [Synopsis](oneview_fc_network_info_module.md#id1)

- Retrieve the information about one or more of the Fibre Channel Networks from OneView.
- This module was called `oneview_fc_network_facts` before Ansible 2.9, returning `ansible_facts`. Note that the [community.general.oneview_fc_network_info](oneview_fc_network_info_module.md#ansible-collections-community-general-oneview-fc-network-info-module) module no longer returns `ansible_facts`!

Aliases: remote_management.oneview.oneview_fc_network_info

## [Requirements](oneview_fc_network_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- hpOneView >= 2.0.1
- python >= 2.7.9

## [Parameters](oneview_fc_network_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_version**  integer | OneView API Version. |
| **config**  path | Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section. |
| **hostname**  string | IP address or hostname for the appliance. |
| **image_streamer_hostname**  string | IP address or hostname for the HPE Image Streamer REST API. |
| **name**  string | Fibre Channel Network name. |
| **params**  dictionary | List of params to delimit, filter and sort the list of resources.  params allowed: - `start`: The first item to return, using 0-based indexing. - `count`: The number of resources to return. - `filter`: A general filter/query string to narrow the list of items returned. - `sort`: The sort order of the returned data set. |
| **password**  string | Password for API authentication. |
| **username**  string | Username for API authentication. |

## [Attributes](oneview_fc_network_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  *added in community.general 3.3.0*  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](oneview_fc_network_info_module.md#id5)

> **Note:**
>
> - A sample configuration file for the config parameter can be found at: <https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json>
> - Check how to use environment variables for configuration at: <https://github.com/HewlettPackard/oneview-ansible#environment-variables>
> - Additional Playbooks for the HPE OneView Ansible modules can be found at: <https://github.com/HewlettPackard/oneview-ansible/tree/master/examples>
> - The OneView API version used will directly affect returned and expected fields in resources. Information on setting the desired API version and can be found at: <https://github.com/HewlettPackard/oneview-ansible#setting-your-oneview-version>

## [Examples](oneview_fc_network_info_module.md#id6)

```yaml+jinja
- name: Gather information about all Fibre Channel Networks
  community.general.oneview_fc_network_info:
    config: /etc/oneview/oneview_config.json
  delegate_to: localhost
  register: result

- name: Print fetched information about Fibre Channel Networks
  ansible.builtin.debug:
    msg: "{{ result.fc_networks }}"

- name: Gather paginated, filtered and sorted information about Fibre Channel Networks
  community.general.oneview_fc_network_info:
    config: /etc/oneview/oneview_config.json
    params:
      start: 1
      count: 3
      sort: 'name:descending'
      filter: 'fabricType=FabricAttach'
  delegate_to: localhost
  register: result

- name: Print fetched information about paginated, filtered and sorted list of Fibre Channel Networks
  ansible.builtin.debug:
    msg: "{{ result.fc_networks }}"

- name: Gather information about a Fibre Channel Network by name
  community.general.oneview_fc_network_info:
    config: /etc/oneview/oneview_config.json
    name: network name
  delegate_to: localhost
  register: result

- name: Print fetched information about Fibre Channel Network found by name
  ansible.builtin.debug:
    msg: "{{ result.fc_networks }}"
```

## [Return Values](oneview_fc_network_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **fc_networks**  dictionary | Has all the OneView information about the Fibre Channel Networks.  **Returned:** Always, but can be null. |

### Authors

- Felipe Bulsoni (@fgbulsoni)
- Thiago Miotto (@tmiotto)
- Adriane Cardozo (@adriane-cardozo)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
