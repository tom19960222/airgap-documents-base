---
collection: ansible
version: "8"
title: "community.general.oneview_enclosure_info module – Retrieve information about one or more Enclosures"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/oneview_enclosure_info_module.html
fetched_at: 2026-07-28T01:48:29+00:00
---
# community.general.oneview_enclosure_info module – Retrieve information about one or more Enclosures

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
> see [Requirements](oneview_enclosure_info_module.md#ansible-collections-community-general-oneview-enclosure-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.oneview_enclosure_info`.

- [Synopsis](oneview_enclosure_info_module.md#synopsis)
- [Requirements](oneview_enclosure_info_module.md#requirements)
- [Parameters](oneview_enclosure_info_module.md#parameters)
- [Attributes](oneview_enclosure_info_module.md#attributes)
- [Notes](oneview_enclosure_info_module.md#notes)
- [Examples](oneview_enclosure_info_module.md#examples)
- [Return Values](oneview_enclosure_info_module.md#return-values)

## [Synopsis](oneview_enclosure_info_module.md#id1)

- Retrieve information about one or more of the Enclosures from OneView.
- This module was called `oneview_enclosure_facts` before Ansible 2.9, returning `ansible_facts`. Note that the [community.general.oneview_enclosure_info](oneview_enclosure_info_module.md#ansible-collections-community-general-oneview-enclosure-info-module) module no longer returns `ansible_facts`!

Aliases: remote_management.oneview.oneview_enclosure_info

## [Requirements](oneview_enclosure_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- hpOneView >= 2.0.1
- python >= 2.7.9

## [Parameters](oneview_enclosure_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_version**  integer | OneView API Version. |
| **config**  path | Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section. |
| **hostname**  string | IP address or hostname for the appliance. |
| **image_streamer_hostname**  string | IP address or hostname for the HPE Image Streamer REST API. |
| **name**  string | Enclosure name. |
| **options**  list / elements=any | List with options to gather additional information about an Enclosure and related resources. Options allowed: `script`, `environmentalConfiguration`, and `utilization`. For the option `utilization`, you can provide specific parameters. |
| **params**  dictionary | List of params to delimit, filter and sort the list of resources.  params allowed: - `start`: The first item to return, using 0-based indexing. - `count`: The number of resources to return. - `filter`: A general filter/query string to narrow the list of items returned. - `sort`: The sort order of the returned data set. |
| **password**  string | Password for API authentication. |
| **username**  string | Username for API authentication. |

## [Attributes](oneview_enclosure_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  *added in community.general 3.3.0*  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](oneview_enclosure_info_module.md#id5)

> **Note:**
>
> - A sample configuration file for the config parameter can be found at: <https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json>
> - Check how to use environment variables for configuration at: <https://github.com/HewlettPackard/oneview-ansible#environment-variables>
> - Additional Playbooks for the HPE OneView Ansible modules can be found at: <https://github.com/HewlettPackard/oneview-ansible/tree/master/examples>
> - The OneView API version used will directly affect returned and expected fields in resources. Information on setting the desired API version and can be found at: <https://github.com/HewlettPackard/oneview-ansible#setting-your-oneview-version>

## [Examples](oneview_enclosure_info_module.md#id6)

```yaml+jinja
- name: Gather information about all Enclosures
  community.general.oneview_enclosure_info:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 500
  no_log: true
  delegate_to: localhost
  register: result

- name: Print fetched information about Enclosures
  ansible.builtin.debug:
    msg: "{{ result.enclosures }}"

- name: Gather paginated, filtered and sorted information about Enclosures
  community.general.oneview_enclosure_info:
    params:
      start: 0
      count: 3
      sort: name:descending
      filter: status=OK
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 500
  no_log: true
  delegate_to: localhost
  register: result

- name: Print fetched information about paginated, filtered and sorted list of Enclosures
  ansible.builtin.debug:
    msg: "{{ result.enclosures }}"

- name: Gather information about an Enclosure by name
  community.general.oneview_enclosure_info:
    name: Enclosure-Name
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 500
  no_log: true
  delegate_to: localhost
  register: result

- name: Print fetched information about Enclosure found by name
  ansible.builtin.debug:
    msg: "{{ result.enclosures }}"

- name: Gather information about an Enclosure by name with options
  community.general.oneview_enclosure_info:
    name: Test-Enclosure
    options:
      - script                       # optional
      - environmentalConfiguration   # optional
      - utilization                  # optional
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 500
  no_log: true
  delegate_to: localhost
  register: result

- name: Print fetched information about Enclosure found by name
  ansible.builtin.debug:
    msg: "{{ result.enclosures }}"

- name: Print fetched information about Enclosure Script
  ansible.builtin.debug:
    msg: "{{ result.enclosure_script }}"

- name: Print fetched information about Enclosure Environmental Configuration
  ansible.builtin.debug:
    msg: "{{ result.enclosure_environmental_configuration }}"

- name: Print fetched information about Enclosure Utilization
  ansible.builtin.debug:
    msg: "{{ result.enclosure_utilization }}"

- name: "Gather information about an Enclosure with temperature data at a resolution of one sample per day, between two
         specified dates"
  community.general.oneview_enclosure_info:
    name: Test-Enclosure
    options:
      - utilization:                   # optional
          fields: AmbientTemperature
          filter:
            - startDate=2016-07-01T14:29:42.000Z
            - endDate=2017-07-01T03:29:42.000Z
          view: day
          refresh: false
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 500
  no_log: true
  delegate_to: localhost
  register: result

- name: Print fetched information about Enclosure found by name
  ansible.builtin.debug:
    msg: "{{ result.enclosures }}"

- name: Print fetched information about Enclosure Utilization
  ansible.builtin.debug:
    msg: "{{ result.enclosure_utilization }}"
```

## [Return Values](oneview_enclosure_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **enclosure_environmental_configuration**  dictionary | Has all the OneView information about the environmental configuration of an Enclosure.  **Returned:** When requested, but can be null. |
| **enclosure_script**  string | Has all the OneView information about the script of an Enclosure.  **Returned:** When requested, but can be null. |
| **enclosure_utilization**  dictionary | Has all the OneView information about the utilization of an Enclosure.  **Returned:** When requested, but can be null. |
| **enclosures**  dictionary | Has all the OneView information about the Enclosures.  **Returned:** Always, but can be null. |

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
