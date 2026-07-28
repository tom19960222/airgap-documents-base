---
collection: ansible
version: "6"
title: "netapp.cloudmanager.na_cloudmanager_info module – NetApp Cloud Manager info"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/cloudmanager/na_cloudmanager_info_module.html
fetched_at: 2026-07-28T00:11:39+00:00
---
# netapp.cloudmanager.na_cloudmanager_info module – NetApp Cloud Manager info

> **Note:**
>
> This module is part of the [netapp.cloudmanager collection](https://galaxy.ansible.com/netapp/cloudmanager) (version 21.21.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.cloudmanager`.
>
> To use it in a playbook, specify: `netapp.cloudmanager.na_cloudmanager_info`.

New in netapp.cloudmanager 21.4.0

- [Synopsis](na_cloudmanager_info_module.md#synopsis)
- [Parameters](na_cloudmanager_info_module.md#parameters)
- [Notes](na_cloudmanager_info_module.md#notes)
- [Examples](na_cloudmanager_info_module.md#examples)
- [Return Values](na_cloudmanager_info_module.md#return-values)

## [Synopsis](na_cloudmanager_info_module.md#id1)

- This module allows you to gather various information about cloudmanager using REST APIs.

## [Parameters](na_cloudmanager_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **client_id**  string / required | The connector ID of the Cloud Manager Connector. |
| **environment**  string  added in netapp.cloudmanager 21.8.0 | The environment for NetApp Cloud Manager API operations.  Choices:   - `"prod"` ← (default) - `"stage"` |
| **feature_flags**  dictionary  added in netapp.cloudmanager 21.11.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **gather_subsets**  list / elements=string | When supplied, this argument will restrict the information collected to a given subset.  Possible values for this argument include  working_environments_info  aggregates_info  accounts_info  account_info  agents_info  active_agents_info  Default: `["all"]` |
| **refresh_token**  string | The refresh token for NetApp Cloud Manager API operations. |
| **sa_client_id**  string | The service account secret client ID for NetApp Cloud Manager API operations. |
| **sa_secret_key**  string | The service account secret key for NetApp Cloud Manager API operations. |

## [Notes](na_cloudmanager_info_module.md#id3)

> **Note:**
>
> - Support check_mode
> - The modules prefixed with na_cloudmanager are built to manage CloudManager and CVO deployments in AWS/GCP/Azure clouds.
> - If sa_client_id and sa_secret_key are provided, service account will be used in operations. refresh_token will be ignored.

## [Examples](na_cloudmanager_info_module.md#id4)

```yaml+jinja
- name: Get all available subsets
  netapp.cloudmanager.na_cloudmanager_info:
    client_id: "{{ client_id }}"
    refresh_token: "{{ refresh_token }}"
    gather_subsets:
      - all

- name: Collect data for cloud manager with indicated subsets
  netapp.cloudmanager.na_cloudmanager_info:
    client_id: "{{ client_id }}"
    refresh_token: "{{ refresh_token }}"
    gather_subsets:
      - aggregates_info
      - working_environments_info
```

## [Return Values](na_cloudmanager_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **info**  dictionary | a dictionary of collected subsets  each subset if in JSON format  Returned: success  Sample: `{"info": {"working_environments_info": [{"azureVsaWorkingEnvironments": [], "gcpVsaWorkingEnvironments": [], "onPremWorkingEnvironments": [], "vsaWorkingEnvironments": [{"actionsRequired": null, "activeActions": null, "awsProperties": null, "capacityFeatures": null, "cbsProperties": null, "cloudProviderName": "Amazon", "cloudSyncProperties": null, "clusterProperties": null, "complianceProperties": null, "creatorUserEmail": "samlp|NetAppSAML|test_user", "cronJobSchedules": null, "encryptionProperties": null, "fpolicyProperties": null, "haProperties": null, "interClusterLifs": null, "isHA": false, "k8sProperties": null, "monitoringProperties": null, "name": "testAWS", "ontapClusterProperties": null, "publicId": "VsaWorkingEnvironment-3txYJOsX", "replicationProperties": null, "reservedSize": null, "saasProperties": null, "schedules": null, "snapshotPolicies": null, "status": null, "supportRegistrationInformation": [], "supportRegistrationProperties": null, "supportedFeatures": null, "svmName": "svm_testAWS", "svms": null, "tenantId": "Tenant-2345", "workingEnvironmentType": "VSA"}]}, null]}}` |

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.cloudmanager)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.cloudmanager)
