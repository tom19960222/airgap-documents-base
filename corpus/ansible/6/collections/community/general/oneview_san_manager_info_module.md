---
collection: ansible
version: "6"
title: "community.general.oneview_san_manager_info module – Retrieve information about one or more of the OneView SAN Managers"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/oneview_san_manager_info_module.html
fetched_at: 2026-07-27T17:11:31+00:00
---
# community.general.oneview_san_manager_info module – Retrieve information about one or more of the OneView SAN Managers

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
> see [Requirements](oneview_san_manager_info_module.md#ansible-collections-community-general-oneview-san-manager-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.oneview_san_manager_info`.

- [Synopsis](oneview_san_manager_info_module.md#synopsis)
- [Requirements](oneview_san_manager_info_module.md#requirements)
- [Parameters](oneview_san_manager_info_module.md#parameters)
- [Notes](oneview_san_manager_info_module.md#notes)
- [Examples](oneview_san_manager_info_module.md#examples)
- [Return Values](oneview_san_manager_info_module.md#return-values)

## [Synopsis](oneview_san_manager_info_module.md#id1)

- Retrieve information about one or more of the SAN Managers from OneView
- This module was called `oneview_san_manager_facts` before Ansible 2.9, returning `ansible_facts`. Note that the [community.general.oneview_san_manager_info](oneview_san_manager_info_module.md#ansible-collections-community-general-oneview-san-manager-info-module) module no longer returns `ansible_facts`!

## [Requirements](oneview_san_manager_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- hpOneView >= 2.0.1
- python >= 2.7.9

## [Parameters](oneview_san_manager_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_version**  integer | OneView API Version. |
| **config**  path | Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section. |
| **hostname**  string | IP address or hostname for the appliance. |
| **image_streamer_hostname**  string | IP address or hostname for the HPE Image Streamer REST API. |
| **params**  dictionary | List of params to delimit, filter and sort the list of resources.  params allowed: - `start`: The first item to return, using 0-based indexing. - `count`: The number of resources to return. - `query`: A general query string to narrow the list of resources returned. - `sort`: The sort order of the returned data set. |
| **password**  string | Password for API authentication. |
| **provider_display_name**  string | Provider Display Name. |
| **username**  string | Username for API authentication. |

## [Notes](oneview_san_manager_info_module.md#id4)

> **Note:**
>
> - A sample configuration file for the config parameter can be found at: <https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json>
> - Check how to use environment variables for configuration at: <https://github.com/HewlettPackard/oneview-ansible#environment-variables>
> - Additional Playbooks for the HPE OneView Ansible modules can be found at: <https://github.com/HewlettPackard/oneview-ansible/tree/master/examples>
> - The OneView API version used will directly affect returned and expected fields in resources. Information on setting the desired API version and can be found at: <https://github.com/HewlettPackard/oneview-ansible#setting-your-oneview-version>

## [Examples](oneview_san_manager_info_module.md#id5)

```yaml+jinja
- name: Gather information about all SAN Managers
  community.general.oneview_san_manager_info:
    config: /etc/oneview/oneview_config.json
  delegate_to: localhost
  register: result

- name: Print fetched information about SAN Managers
  ansible.builtin.debug:
    msg: "{{ result.san_managers }}"

- name: Gather paginated, filtered and sorted information about SAN Managers
  community.general.oneview_san_manager_info:
    config: /etc/oneview/oneview_config.json
    params:
      start: 0
      count: 3
      sort: name:ascending
      query: isInternal eq false
  delegate_to: localhost
  register: result

- name: Print fetched information about paginated, filtered and sorted list of SAN Managers
  ansible.builtin.debug:
    msg: "{{ result.san_managers }}"

- name: Gather information about a SAN Manager by provider display name
  community.general.oneview_san_manager_info:
    config: /etc/oneview/oneview_config.json
    provider_display_name: Brocade Network Advisor
  delegate_to: localhost
  register: result

- name: Print fetched information about SAN Manager found by provider display name
  ansible.builtin.debug:
    msg: "{{ result.san_managers }}"
```

## [Return Values](oneview_san_manager_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **san_managers**  dictionary | Has all the OneView information about the SAN Managers.  Returned: Always, but can be null. |

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
