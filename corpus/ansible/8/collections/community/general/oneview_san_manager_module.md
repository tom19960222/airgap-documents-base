---
collection: ansible
version: "8"
title: "community.general.oneview_san_manager module – Manage OneView SAN Manager resources"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/oneview_san_manager_module.html
fetched_at: 2026-07-28T01:48:38+00:00
---
# community.general.oneview_san_manager module – Manage OneView SAN Manager resources

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
> see [Requirements](oneview_san_manager_module.md#ansible-collections-community-general-oneview-san-manager-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.oneview_san_manager`.

- [Synopsis](oneview_san_manager_module.md#synopsis)
- [Requirements](oneview_san_manager_module.md#requirements)
- [Parameters](oneview_san_manager_module.md#parameters)
- [Attributes](oneview_san_manager_module.md#attributes)
- [Notes](oneview_san_manager_module.md#notes)
- [Examples](oneview_san_manager_module.md#examples)
- [Return Values](oneview_san_manager_module.md#return-values)

## [Synopsis](oneview_san_manager_module.md#id1)

- Provides an interface to manage SAN Manager resources. Can create, update, or delete.

Aliases: remote_management.oneview.oneview_san_manager

## [Requirements](oneview_san_manager_module.md#id2)

The below requirements are needed on the host that executes this module.

- hpOneView >= 3.1.1
- python >= 2.7.9

## [Parameters](oneview_san_manager_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_version**  integer | OneView API Version. |
| **config**  path | Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section. |
| **data**  dictionary / required | List with SAN Manager properties. |
| **hostname**  string | IP address or hostname for the appliance. |
| **image_streamer_hostname**  string | IP address or hostname for the HPE Image Streamer REST API. |
| **password**  string | Password for API authentication. |
| **state**  string | Indicates the desired state for the Uplink Set resource. - `present` ensures data properties are compliant with OneView. - `absent` removes the resource from OneView, if it exists. - `connection_information_set` updates the connection information for the SAN Manager. This operation is non-idempotent.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"connection_information_set"` |
| **username**  string | Username for API authentication. |
| **validate_etag**  boolean | When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](oneview_san_manager_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](oneview_san_manager_module.md#id5)

> **Note:**
>
> - A sample configuration file for the config parameter can be found at: <https://github.com/HewlettPackard/oneview-ansible/blob/master/examples/oneview_config-rename.json>
> - Check how to use environment variables for configuration at: <https://github.com/HewlettPackard/oneview-ansible#environment-variables>
> - Additional Playbooks for the HPE OneView Ansible modules can be found at: <https://github.com/HewlettPackard/oneview-ansible/tree/master/examples>
> - The OneView API version used will directly affect returned and expected fields in resources. Information on setting the desired API version and can be found at: <https://github.com/HewlettPackard/oneview-ansible#setting-your-oneview-version>

## [Examples](oneview_san_manager_module.md#id6)

```yaml+jinja
- name: Creates a Device Manager for the Brocade SAN provider with the given hostname and credentials
  community.general.oneview_san_manager:
    config: /etc/oneview/oneview_config.json
    state: present
    data:
      providerDisplayName: Brocade Network Advisor
      connectionInfo:
        - name: Host
          value: 172.18.15.1
        - name: Port
          value: 5989
        - name: Username
          value: username
        - name: Password
          value: password
        - name: UseSsl
          value: true
  delegate_to: localhost

- name: Ensure a Device Manager for the Cisco SAN Provider is present
  community.general.oneview_san_manager:
    config: /etc/oneview/oneview_config.json
    state: present
    data:
      name: 172.18.20.1
      providerDisplayName: Cisco
      connectionInfo:
        - name: Host
          value: 172.18.20.1
        - name: SnmpPort
          value: 161
        - name: SnmpUserName
          value: admin
        - name: SnmpAuthLevel
          value: authnopriv
        - name: SnmpAuthProtocol
          value: sha
        - name: SnmpAuthString
          value: password
  delegate_to: localhost

- name: Sets the SAN Manager connection information
  community.general.oneview_san_manager:
    config: /etc/oneview/oneview_config.json
    state: connection_information_set
    data:
      connectionInfo:
        - name: Host
          value: '172.18.15.1'
        - name: Port
          value: '5989'
        - name: Username
          value: 'username'
        - name: Password
          value: 'password'
        - name: UseSsl
          value: true
  delegate_to: localhost

- name: Refreshes the SAN Manager
  community.general.oneview_san_manager:
    config: /etc/oneview/oneview_config.json
    state: present
    data:
      name: 172.18.15.1
      refreshState: RefreshPending
  delegate_to: localhost

- name: Delete the SAN Manager recently created
  community.general.oneview_san_manager:
    config: /etc/oneview/oneview_config.json
    state: absent
    data:
      name: '172.18.15.1'
  delegate_to: localhost
```

## [Return Values](oneview_san_manager_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **san_manager**  dictionary | Has the OneView facts about the SAN Manager.  **Returned:** On state ‘present’. Can be null. |

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
