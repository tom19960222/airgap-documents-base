---
collection: ansible
version: "8"
title: "netapp.cloudmanager.na_cloudmanager_aws_fsx module – Cloud ONTAP file system(FSx) in AWS"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/cloudmanager/na_cloudmanager_aws_fsx_module.html
fetched_at: 2026-07-28T02:41:04+00:00
---
# netapp.cloudmanager.na_cloudmanager_aws_fsx module – Cloud ONTAP file system(FSx) in AWS

> **Note:**
>
> This module is part of the [netapp.cloudmanager collection](https://galaxy.ansible.com/ui/repo/published/netapp/cloudmanager/) (version 21.22.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.cloudmanager`.
>
> To use it in a playbook, specify: `netapp.cloudmanager.na_cloudmanager_aws_fsx`.

New in netapp.cloudmanager 21.13.0

- [Synopsis](na_cloudmanager_aws_fsx_module.md#synopsis)
- [Parameters](na_cloudmanager_aws_fsx_module.md#parameters)
- [Notes](na_cloudmanager_aws_fsx_module.md#notes)
- [Examples](na_cloudmanager_aws_fsx_module.md#examples)
- [Return Values](na_cloudmanager_aws_fsx_module.md#return-values)

## [Synopsis](na_cloudmanager_aws_fsx_module.md#id1)

- Create or delete CVO/Working Environment for AWS FSx.

## [Parameters](na_cloudmanager_aws_fsx_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aws_credentials_name**  string | The name of the AWS Credentials account name. |
| **endpoint_ip_address_range**  string | The endpoint IP address range. |
| **environment**  string  *added in netapp.cloudmanager 21.8.0* | The environment for NetApp Cloud Manager API operations.  **Choices:**   - `"prod"` ← (default) - `"stage"` |
| **feature_flags**  dictionary  *added in netapp.cloudmanager 21.11.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **file_system_id**  string  *added in netapp.cloudmanager 21.17.0* | The AWS file system ID to import to CloudManager. Required when import_file_system is ‘True’ |
| **fsx_admin_password**  string | The admin password for Cloud Volumes ONTAP fsxadmin user. |
| **import_file_system**  boolean  *added in netapp.cloudmanager 21.17.0* | bool option to existing import AWS file system to CloudManager.  **Choices:**   - `false` ← (default) - `true` |
| **kms_key_id**  string | AWS encryption parameters. It is required if using aws encryption. |
| **minimum_ssd_iops**  integer | Provisioned SSD IOPS. |
| **name**  string / required | The name of the CVO/Working Environment for AWS FSx to manage. |
| **primary_subnet_id**  string | The subnet ID of the first node. |
| **refresh_token**  string | The refresh token for NetApp Cloud Manager API operations. |
| **region**  string | The region where the working environment will be created. |
| **route_table_ids**  list / elements=string | The list of route table IDs that will be updated with the floating IPs. |
| **sa_client_id**  string | The service account secret client ID for NetApp Cloud Manager API operations. |
| **sa_secret_key**  string | The service account secret key for NetApp Cloud Manager API operations. |
| **secondary_subnet_id**  string | The subnet ID of the second node. |
| **security_group_ids**  list / elements=string | The IDs of the security groups for the working environment, multiple security groups can be provided separated by ‘,’. |
| **state**  string | Whether the specified FSx in AWS should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **storage_capacity_size**  integer | volume size for the first data aggregate.  For GB, the value can be [100 or 500].  For TB, the value can be [1,2,4,8,16]. |
| **storage_capacity_size_unit**  string | The unit for volume size.  **Choices:**   - `"GiB"` - `"TiB"` |
| **tags**  list / elements=dictionary | Additional tags for the FSx AWS working environment. |
| **tag_key**  string | The key of the tag. |
| **tag_value**  string | The tag value. |
| **tenant_id**  string / required | The NetApp account ID that the File System will be associated with. |
| **throughput_capacity**  integer | The capacity of the throughput.  **Choices:**   - `512` - `1024` - `2048` |
| **working_environment_id**  string | The ID of the AWS FSx working environment used for delete. |
| **workspace_id**  string | The ID of the Cloud Manager workspace of working environment. |

## [Notes](na_cloudmanager_aws_fsx_module.md#id3)

> **Note:**
>
> - Support check_mode.
> - The modules prefixed with na_cloudmanager are built to manage CloudManager and CVO deployments in AWS/GCP/Azure clouds.
> - If sa_client_id and sa_secret_key are provided, service account will be used in operations. refresh_token will be ignored.

## [Examples](na_cloudmanager_aws_fsx_module.md#id4)

```yaml+jinja
- name: Create NetApp AWS FSx
  netapp.cloudmanager.na_cloudmanager_aws_fsx:
    state: present
    refresh_token: "{{ xxxxxxxxxxxxxxx }}"
    name: fsxAnsible
    region: us-east-2
    workspace_id: workspace-xxxxx
    tenant_id: account-xxxxx
    storage_capacity_size: 1024
    storage_capacity_size_unit: TiB
    aws_credentials_name: xxxxxxx
    primary_subnet_id: subnet-xxxxxx
    secondary_subnet_id: subnet-xxxxx
    throughput_capacity: 512
    fsx_admin_password: xxxxxxx
    tags: [
      {tag_key: abcd,
      tag_value: ABCD}]

- name: Import AWS FSX
  na_cloudmanager_aws_fsx:
    state: present
    refresh_token: "{{ xxxxxxxxxxxxxxx }}"
    name: fsxAnsible
    region: us-west-2
    workspace_id: workspace-xxxxx
    import_file_system: True
    file_system_id: "{{ xxxxxxxxxxxxxxx }}"
    tenant_id: account-xxxxx
    aws_credentials_name: xxxxxxx

- name: Delete NetApp AWS FSx
  netapp.cloudmanager.na_cloudmanager_aws_fsx:
    state: absent
    refresh_token: "{{ xxxxxxxxxxxxxxx }}"
    working_environment_id: fs-xxxxxx
    name: fsxAnsible
    tenant_id: account-xxxxx
```

## [Return Values](na_cloudmanager_aws_fsx_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **working_environment_id**  string | Newly created AWS FSx working_environment_id.  **Returned:** success |

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.cloudmanager)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.cloudmanager)
