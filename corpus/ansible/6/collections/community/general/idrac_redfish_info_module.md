---
collection: ansible
version: "6"
title: "community.general.idrac_redfish_info module – Gather PowerEdge server information through iDRAC using Redfish APIs"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/idrac_redfish_info_module.html
fetched_at: 2026-07-27T17:09:40+00:00
---
# community.general.idrac_redfish_info module – Gather PowerEdge server information through iDRAC using Redfish APIs

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
> To use it in a playbook, specify: `community.general.idrac_redfish_info`.

- [Synopsis](idrac_redfish_info_module.md#synopsis)
- [Parameters](idrac_redfish_info_module.md#parameters)
- [Examples](idrac_redfish_info_module.md#examples)
- [Return Values](idrac_redfish_info_module.md#return-values)

## [Synopsis](idrac_redfish_info_module.md#id1)

- Builds Redfish URIs locally and sends them to remote iDRAC controllers to get information back.
- For use with Dell EMC iDRAC operations that require Redfish OEM extensions.
- This module was called `idrac_redfish_facts` before Ansible 2.9, returning `ansible_facts`. Note that the [community.general.idrac_redfish_info](idrac_redfish_info_module.md#ansible-collections-community-general-idrac-redfish-info-module) module no longer returns `ansible_facts`!

## [Parameters](idrac_redfish_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_token**  string  added in community.general 2.3.0 | Security token for authenticating to iDRAC. |
| **baseuri**  string / required | Base URI of iDRAC. |
| **category**  string / required | Category to execute on iDRAC. |
| **command**  list / elements=string / required | List of commands to execute on iDRAC.  `GetManagerAttributes` returns the list of dicts containing iDRAC, LifecycleController and System attributes. |
| **password**  string | Password for authenticating to iDRAC. |
| **timeout**  integer | Timeout in seconds for HTTP requests to iDRAC.  Default: `10` |
| **username**  string | Username for authenticating to iDRAC. |

## [Examples](idrac_redfish_info_module.md#id3)

```yaml+jinja
- name: Get Manager attributes with a default of 20 seconds
  community.general.idrac_redfish_info:
    category: Manager
    command: GetManagerAttributes
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    timeout: 20
  register: result

# Examples to display the value of all or a single iDRAC attribute
- name: Store iDRAC attributes as a fact variable
  ansible.builtin.set_fact:
    idrac_attributes: "{{ result.redfish_facts.entries | selectattr('Id', 'defined') | selectattr('Id', 'equalto', 'iDRACAttributes') | list | first }}"

- name: Display all iDRAC attributes
  ansible.builtin.debug:
    var: idrac_attributes

- name: Display the value of 'Syslog.1.SysLogEnable' iDRAC attribute
  ansible.builtin.debug:
    var: idrac_attributes['Syslog.1.SysLogEnable']

# Examples to display the value of all or a single LifecycleController attribute
- name: Store LifecycleController attributes as a fact variable
  ansible.builtin.set_fact:
    lc_attributes: "{{ result.redfish_facts.entries | selectattr('Id', 'defined') | selectattr('Id', 'equalto', 'LCAttributes') | list | first }}"

- name: Display LifecycleController attributes
  ansible.builtin.debug:
    var: lc_attributes

- name: Display the value of 'CollectSystemInventoryOnRestart' attribute
  ansible.builtin.debug:
    var: lc_attributes['LCAttributes.1.CollectSystemInventoryOnRestart']

# Examples to display the value of all or a single System attribute
- name: Store System attributes as a fact variable
  ansible.builtin.set_fact:
    system_attributes: "{{ result.redfish_facts.entries | selectattr('Id', 'defined') | selectattr('Id', 'equalto', 'SystemAttributes') | list | first }}"

- name: Display System attributes
  ansible.builtin.debug:
    var: system_attributes

- name: Display the value of 'PSRedPolicy'
  ansible.builtin.debug:
    var: system_attributes['ServerPwr.1.PSRedPolicy']
```

## [Return Values](idrac_redfish_info_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  dictionary | different results depending on task  Returned: always  Sample: `"List of Manager attributes"` |

### Authors

- Jose Delarosa (@jose-delarosa)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
