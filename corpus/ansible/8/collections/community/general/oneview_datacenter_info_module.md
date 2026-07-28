---
collection: ansible
version: "8"
title: "community.general.oneview_datacenter_info module – Retrieve information about the OneView Data Centers"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/oneview_datacenter_info_module.html
fetched_at: 2026-07-28T01:48:29+00:00
---
# community.general.oneview_datacenter_info module – Retrieve information about the OneView Data Centers

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
> see [Requirements](oneview_datacenter_info_module.md#ansible-collections-community-general-oneview-datacenter-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.oneview_datacenter_info`.

- [Synopsis](oneview_datacenter_info_module.md#synopsis)
- [Requirements](oneview_datacenter_info_module.md#requirements)
- [Parameters](oneview_datacenter_info_module.md#parameters)
- [Attributes](oneview_datacenter_info_module.md#attributes)
- [Notes](oneview_datacenter_info_module.md#notes)
- [Examples](oneview_datacenter_info_module.md#examples)
- [Return Values](oneview_datacenter_info_module.md#return-values)

## [Synopsis](oneview_datacenter_info_module.md#id1)

- Retrieve information about the OneView Data Centers.
- This module was called `oneview_datacenter_facts` before Ansible 2.9, returning `ansible_facts`. Note that the [community.general.oneview_datacenter_info](oneview_datacenter_info_module.md#ansible-collections-community-general-oneview-datacenter-info-module) module no longer returns `ansible_facts`!

Aliases: remote_management.oneview.oneview_datacenter_info

## [Requirements](oneview_datacenter_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- hpOneView >= 2.0.1
- python >= 2.7.9

## [Parameters](oneview_datacenter_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_version**  integer | OneView API Version. |
| **config**  path | Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section. |
| **hostname**  string | IP address or hostname for the appliance. |
| **image_streamer_hostname**  string | IP address or hostname for the HPE Image Streamer REST API. |
| **name**  string | Data Center name. |
| **options**  list / elements=string | Retrieve additional information. Options available: ‘visualContent’. |
| **params**  dictionary | List of params to delimit, filter and sort the list of resources.  params allowed: - `start`: The first item to return, using 0-based indexing. - `count`: The number of resources to return. - `filter`: A general filter/query string to narrow the list of items returned. - `sort`: The sort order of the returned data set. |
| **password**  string | Password for API authentication. |
| **username**  string | Username for API authentication. |

## [Attributes](oneview_datacenter_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  *added in community.general 3.3.0*  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](oneview_datacenter_info_module.md#id5)

> **Note:**
>
> - A sample configuration file for the config parameter can be found at: <https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json>
> - Check how to use environment variables for configuration at: <https://github.com/HewlettPackard/oneview-ansible#environment-variables>
> - Additional Playbooks for the HPE OneView Ansible modules can be found at: <https://github.com/HewlettPackard/oneview-ansible/tree/master/examples>
> - The OneView API version used will directly affect returned and expected fields in resources. Information on setting the desired API version and can be found at: <https://github.com/HewlettPackard/oneview-ansible#setting-your-oneview-version>

## [Examples](oneview_datacenter_info_module.md#id6)

```yaml+jinja
- name: Gather information about all Data Centers
  community.general.oneview_datacenter_info:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 500
  delegate_to: localhost
  register: result

- name: Print fetched information about Data Centers
  ansible.builtin.debug:
    msg: "{{ result.datacenters }}"

- name: Gather paginated, filtered and sorted information about Data Centers
  community.general.oneview_datacenter_info:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 500
    params:
      start: 0
      count: 3
      sort: 'name:descending'
      filter: 'state=Unmanaged'
  register: result

- name: Print fetched information about paginated, filtered and sorted list of Data Centers
  ansible.builtin.debug:
    msg: "{{ result.datacenters }}"

- name: Gather information about a Data Center by name
  community.general.oneview_datacenter_info:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 500
    name: "My Data Center"
  delegate_to: localhost
  register: result

- name: Print fetched information about Data Center found by name
  ansible.builtin.debug:
    msg: "{{ result.datacenters }}"

- name: Gather information about the Data Center Visual Content
  community.general.oneview_datacenter_info:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 500
    name: "My Data Center"
    options:
      - visualContent
  delegate_to: localhost
  register: result

- name: Print fetched information about Data Center found by name
  ansible.builtin.debug:
    msg: "{{ result.datacenters }}"

- name: Print fetched information about Data Center Visual Content
  ansible.builtin.debug:
    msg: "{{ result.datacenter_visual_content }}"
```

## [Return Values](oneview_datacenter_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **datacenter_visual_content**  dictionary | Has information about the Data Center Visual Content.  **Returned:** When requested, but can be null. |
| **datacenters**  dictionary | Has all the OneView information about the Data Centers.  **Returned:** Always, but can be null. |

### Authors

- Alex Monteiro (@aalexmonteiro)
- Madhav Bharadwaj (@madhav-bharadwaj)
- Priyanka Sood (@soodpr)
- Ricardo Galeno (@ricardogpsf)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
