---
collection: ansible
version: "6"
title: "community.general.redfish_info module – Manages Out-Of-Band controllers using Redfish APIs"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/redfish_info_module.html
fetched_at: 2026-07-27T17:12:37+00:00
---
# community.general.redfish_info module – Manages Out-Of-Band controllers using Redfish APIs

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.redfish_info`.

- [Synopsis](redfish_info_module.md#synopsis)
- [Parameters](redfish_info_module.md#parameters)
- [Examples](redfish_info_module.md#examples)
- [Return Values](redfish_info_module.md#return-values)

## [Synopsis](redfish_info_module.md#id1)

- Builds Redfish URIs locally and sends them to remote OOB controllers to get information back.
- Information retrieved is placed in a location specified by the user.
- This module was called `redfish_facts` before Ansible 2.9, returning `ansible_facts`. Note that the [community.general.redfish_info](redfish_info_module.md#ansible-collections-community-general-redfish-info-module) module no longer returns `ansible_facts`!

## [Parameters](redfish_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_token**  string  added in community.general 2.3.0 | Security token for authenticating to OOB controller. |
| **baseuri**  string / required | Base URI of OOB controller. |
| **category**  list / elements=string | List of categories to execute on OOB controller.  Default: `["Systems"]` |
| **command**  list / elements=string | List of commands to execute on OOB controller. |
| **password**  string | Password for authenticating to OOB controller. |
| **timeout**  integer | Timeout in seconds for HTTP requests to OOB controller.  Default: `10` |
| **username**  string | Username for authenticating to OOB controller. |

## [Examples](redfish_info_module.md#id3)

```yaml+jinja
- name: Get CPU inventory
  community.general.redfish_info:
    category: Systems
    command: GetCpuInventory
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
  register: result

- name: Print fetched information
  ansible.builtin.debug:
    msg: "{{ result.redfish_facts.cpu.entries | to_nice_json }}"

- name: Get CPU model
  community.general.redfish_info:
    category: Systems
    command: GetCpuInventory
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
  register: result

- name: Print fetched information
  ansible.builtin.debug:
    msg: "{{ result.redfish_facts.cpu.entries.0.Model }}"

- name: Get memory inventory
  community.general.redfish_info:
    category: Systems
    command: GetMemoryInventory
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
  register: result

- name: Get fan inventory with a timeout of 20 seconds
  community.general.redfish_info:
    category: Chassis
    command: GetFanInventory
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    timeout: 20
  register: result

- name: Get Virtual Media information
  community.general.redfish_info:
    category: Manager
    command: GetVirtualMedia
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
  register: result

- name: Print fetched information
  ansible.builtin.debug:
    msg: "{{ result.redfish_facts.virtual_media.entries | to_nice_json }}"

- name: Get Virtual Media information from Systems
  community.general.redfish_info:
    category: Systems
    command: GetVirtualMedia
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
  register: result

- name: Print fetched information
  ansible.builtin.debug:
    msg: "{{ result.redfish_facts.virtual_media.entries | to_nice_json }}"

- name: Get Volume Inventory
  community.general.redfish_info:
    category: Systems
    command: GetVolumeInventory
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
  register: result
- name: Print fetched information
  ansible.builtin.debug:
    msg: "{{ result.redfish_facts.volume.entries | to_nice_json }}"

- name: Get Session information
  community.general.redfish_info:
    category: Sessions
    command: GetSessions
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
  register: result

- name: Print fetched information
  ansible.builtin.debug:
    msg: "{{ result.redfish_facts.session.entries | to_nice_json }}"

- name: Get default inventory information
  community.general.redfish_info:
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
  register: result
- name: Print fetched information
  ansible.builtin.debug:
    msg: "{{ result.redfish_facts | to_nice_json }}"

- name: Get several inventories
  community.general.redfish_info:
    category: Systems
    command: GetNicInventory,GetBiosAttributes
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Get default system inventory and user information
  community.general.redfish_info:
    category: Systems,Accounts
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Get default system, user and firmware information
  community.general.redfish_info:
    category: ["Systems", "Accounts", "Update"]
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Get Manager NIC inventory information
  community.general.redfish_info:
    category: Manager
    command: GetManagerNicInventory
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Get boot override information
  community.general.redfish_info:
    category: Systems
    command: GetBootOverride
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Get chassis inventory
  community.general.redfish_info:
    category: Chassis
    command: GetChassisInventory
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Get all information available in the Manager category
  community.general.redfish_info:
    category: Manager
    command: all
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Get firmware update capability information
  community.general.redfish_info:
    category: Update
    command: GetFirmwareUpdateCapabilities
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Get firmware inventory
  community.general.redfish_info:
    category: Update
    command: GetFirmwareInventory
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Get software inventory
  community.general.redfish_info:
    category: Update
    command: GetSoftwareInventory
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Get Manager Services
  community.general.redfish_info:
    category: Manager
    command: GetNetworkProtocols
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Get all information available in all categories
  community.general.redfish_info:
    category: all
    command: all
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Get system health report
  community.general.redfish_info:
    category: Systems
    command: GetHealthReport
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Get chassis health report
  community.general.redfish_info:
    category: Chassis
    command: GetHealthReport
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Get manager health report
  community.general.redfish_info:
    category: Manager
    command: GetHealthReport
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Get manager Redfish Host Interface inventory
  community.general.redfish_info:
    category: Manager
    command: GetHostInterfaces
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Get Manager Inventory
  community.general.redfish_info:
    category: Manager
    command: GetManagerInventory
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
```

## [Return Values](redfish_info_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  dictionary | different results depending on task  Returned: always  Sample: `"List of CPUs on system"` |

### Authors

- Jose Delarosa (@jose-delarosa)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
