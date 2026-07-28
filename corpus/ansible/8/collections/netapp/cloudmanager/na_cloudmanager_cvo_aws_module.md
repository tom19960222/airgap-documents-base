---
collection: ansible
version: "8"
title: "netapp.cloudmanager.na_cloudmanager_cvo_aws module – NetApp Cloud Manager CVO for AWS"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/cloudmanager/na_cloudmanager_cvo_aws_module.html
fetched_at: 2026-07-28T02:41:08+00:00
---
# netapp.cloudmanager.na_cloudmanager_cvo_aws module – NetApp Cloud Manager CVO for AWS

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
> To use it in a playbook, specify: `netapp.cloudmanager.na_cloudmanager_cvo_aws`.

New in netapp.cloudmanager 21.3.0

- [Synopsis](na_cloudmanager_cvo_aws_module.md#synopsis)
- [Parameters](na_cloudmanager_cvo_aws_module.md#parameters)
- [Notes](na_cloudmanager_cvo_aws_module.md#notes)
- [Examples](na_cloudmanager_cvo_aws_module.md#examples)
- [Return Values](na_cloudmanager_cvo_aws_module.md#return-values)

## [Synopsis](na_cloudmanager_cvo_aws_module.md#id1)

- Create, delete, or manage Cloud Manager CVO for AWS.

## [Parameters](na_cloudmanager_cvo_aws_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aws_tag**  list / elements=dictionary | Additional tags for the AWS CVO working environment. |
| **tag_key**  string | The key of the tag. |
| **tag_value**  string | The tag value. |
| **backup_volumes_to_cbs**  boolean | Automatically enable back up of all volumes to S3.  **Choices:**   - `false` ← (default) - `true` |
| **capacity_package_name**  string  *added in netapp.cloudmanager 21.12.0* | Capacity package name is required when selecting a capacity based license.  Essential only available with Bring Your Own License Capacity-Based.  Professional available as an annual contract from AWS marketplace or Bring Your Own License Capacity-Based.  **Choices:**   - `"Professional"` - `"Essential"` ← (default) - `"Freemium"` |
| **capacity_tier**  string | Whether to enable data tiering for the first data aggregate.  **Choices:**   - `"S3"` ← (default) - `"NONE"` |
| **client_id**  string / required | The connector ID of the Cloud Manager Connector.  You can find the ID from the Connector tab on <https://cloudmanager.netapp.com>. |
| **cloud_provider_account**  string | The cloud provider credentials id to use when deploying the Cloud Volumes ONTAP system.  You can find the ID in Cloud Manager from the Settings > Credentials page.  If not specified, Cloud Manager uses the instance profile of the Connector. |
| **cluster_floating_ip**  string | For HA FloatingIP, the cluster management floating IP address. |
| **cluster_key_pair_name**  string  *added in netapp.cloudmanager 21.20.0* | SSH authentication key pair name |
| **data_encryption_type**  string | The type of encryption to use for the working environment.  **Choices:**   - `"AWS"` ← (default) - `"NONE"` |
| **data_floating_ip**  string | For HA FloatingIP, the data floating IP address. |
| **data_floating_ip2**  string | For HA FloatingIP, the data floating IP address. |
| **ebs_volume_size**  integer | EBS volume size for the first data aggregate.  For GB, the value can be [100 or 500].  For TB, the value can be [1,2,4,8,16].  **Default:** `1` |
| **ebs_volume_size_unit**  string | The unit for ebs volume size.  **Choices:**   - `"GB"` - `"TB"` ← (default) |
| **ebs_volume_type**  string | The EBS volume type for the first data aggregate.  **Choices:**   - `"gp3"` - `"gp2"` ← (default) - `"io1"` - `"sc1"` - `"st1"` |
| **enable_compliance**  boolean | Enable the Cloud Compliance service on the working environment.  **Choices:**   - `false` ← (default) - `true` |
| **enable_monitoring**  boolean | Enable the Monitoring service on the working environment.  **Choices:**   - `false` ← (default) - `true` |
| **environment**  string  *added in netapp.cloudmanager 21.8.0* | The environment for NetApp Cloud Manager API operations.  **Choices:**   - `"prod"` ← (default) - `"stage"` |
| **failover_mode**  string | For HA, the failover mode for the HA pair. ‘PrivateIP’ is for a single availability zone and ‘FloatingIP’ is for multiple availability zones.  **Choices:**   - `"PrivateIP"` - `"FloatingIP"` |
| **feature_flags**  dictionary  *added in netapp.cloudmanager 21.11.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **instance_profile_name**  string | The instance profile name for the working environment. If not provided, Cloud Manager creates the instance profile. |
| **instance_tenancy**  string | The EC2 instance tenancy.  **Choices:**   - `"default"` ← (default) - `"dedicated"` |
| **instance_type**  string | The instance type to use, which depends on the license type.  Explore [‘m5.xlarge’].  Standard [‘m5.2xlarge’,’r5.xlarge’].  Premium [‘m5.4xlarge’,’r5.2xlarge’,’c4.8xlarge’].  For more supported instance types, refer to Cloud Volumes ONTAP Release Notes.  **Default:** `"m5.2xlarge"` |
| **iops**  integer | Provisioned IOPS. Required only when provider_volume_type is ‘io1’ or ‘gp3’. |
| **is_ha**  boolean | Indicate whether the working environment is an HA pair or not.  **Choices:**   - `false` ← (default) - `true` |
| **kms_key_arn**  string  *added in netapp.cloudmanager 21.10.0* | AWS encryption parameters. It is required if using aws encryption. Only one of KMS key id or KMS arn should be specified. |
| **kms_key_id**  string | Aws Encryption parameters. It is required if using aws encryption. Only one of KMS key id or KMS arn should be specified. |
| **license_type**  string | The type of license to use.  For single node by Capacity [‘capacity-paygo’]  For single node by Node paygo [‘cot-explore-paygo’, ‘cot-standard-paygo’, ‘cot-premium-paygo’].  For single node by Node boyl [‘cot-premium-byol’].  For HA by Capacity [‘ha-capacity-paygo’]  For HA by Node paygo [‘ha-cot-explore-paygo’,’ha-cot-standard-paygo’,’ha-cot-premium-paygo’].  For HA by Node boyl [‘ha-cot-premium-byol’].  **Choices:**   - `"capacity-paygo"` ← (default) - `"cot-standard-paygo"` - `"cot-premium-paygo"` - `"cot-explore-paygo"` - `"cot-premium-byol"` - `"ha-cot-standard-paygo"` - `"ha-cot-premium-paygo"` - `"ha-cot-premium-byol"` - `"ha-cot-explore-paygo"` - `"ha-capacity-paygo"` |
| **mediator_assign_public_ip**  boolean | Boolean option to assign public IP.  **Choices:**   - `false` - `true` ← (default) |
| **mediator_key_pair_name**  string | For HA, the key pair name for the mediator instance. |
| **mediator_subnet_id**  string | For HA, the subnet ID of the mediator. |
| **name**  string / required | The name of the Cloud Manager CVO for AWS to manage. |
| **node1_subnet_id**  string | For HA, the subnet ID of the first node. |
| **node2_subnet_id**  string | For HA, the subnet ID of the second node. |
| **nss_account**  string | The NetApp Support Site account ID to use with this Cloud Volumes ONTAP system.  If the license type is BYOL and an NSS account is not provided, Cloud Manager tries to use the first existing NSS account. |
| **ontap_version**  string | The required ONTAP version. Ignored if ‘use_latest_version’ is set to true.  **Default:** `"latest"` |
| **optimized_network_utilization**  boolean | Use optimized network utilization.  **Choices:**   - `false` - `true` ← (default) |
| **platform_serial_number**  string | The serial number for the cluster. This is required when using ‘cot-premium-byol’. |
| **platform_serial_number_node1**  string | For HA BYOL, the serial number for the first node. This is required when using ‘ha-cot-premium-byol’. |
| **platform_serial_number_node2**  string | For HA BYOL, the serial number for the second node. This is required when using ‘ha-cot-premium-byol’. |
| **provided_license**  string | Using a NLF license file for BYOL deployment. |
| **refresh_token**  string | The refresh token for NetApp Cloud Manager API operations. |
| **region**  string / required | The region where the working environment will be created. |
| **route_table_ids**  list / elements=string | For HA FloatingIP, the list of route table IDs that will be updated with the floating IPs. |
| **sa_client_id**  string | The service account secret client ID for NetApp Cloud Manager API operations. |
| **sa_secret_key**  string | The service account secret key for NetApp Cloud Manager API operations. |
| **security_group_id**  string | The ID of the security group for the working environment. If not provided, Cloud Manager creates the security group. |
| **state**  string | Whether the specified Cloud Manager CVO for AWS should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subnet_id**  string | The subnet id where the working environment will be created. Required when single node only. |
| **svm_floating_ip**  string | For HA FloatingIP, the SVM management floating IP address. |
| **svm_name**  string  *added in netapp.cloudmanager 21.22.0* | The name of the SVM. |
| **svm_password**  string / required | The admin password for Cloud Volumes ONTAP.  It will be updated on each run. |
| **throughput**  integer | Unit is Mb/s. Valid range 125-1000.  Required only when provider_volume_type is ‘gp3’. |
| **tier_level**  string | The tiering level when ‘capacity_tier’ is set to ‘S3’.  **Choices:**   - `"normal"` ← (default) - `"ia"` - `"ia-single"` - `"intelligent"` |
| **update_svm_password**  boolean  *added in netapp.cloudmanager 21.13.0* | Indicates whether to update svm_password on the CVO.  When set to true, the module is not idempotent, as we cannot read the current password.  **Choices:**   - `false` ← (default) - `true` |
| **upgrade_ontap_version**  boolean  *added in netapp.cloudmanager 21.13.0* | Indicates whether to upgrade ONTAP image on the CVO.  If the current version already matches the desired version, no action is taken.  **Choices:**   - `false` ← (default) - `true` |
| **use_latest_version**  boolean | Indicates whether to use the latest available ONTAP version.  **Choices:**   - `false` - `true` ← (default) |
| **vpc_id**  string | The VPC ID where the working environment will be created.  If this argument is not provided, the VPC will be calculated by using the provided subnet ID. |
| **workspace_id**  string | The ID of the Cloud Manager workspace where you want to deploy Cloud Volumes ONTAP.  If not provided, Cloud Manager uses the first workspace.  You can find the ID from the Workspace tab on <https://cloudmanager.netapp.com>. |
| **writing_speed_state**  string | The write speed setting for Cloud Volumes ONTAP [‘NORMAL’,’HIGH’].  This argument is not relevant for HA pairs. |

## [Notes](na_cloudmanager_cvo_aws_module.md#id3)

> **Note:**
>
> - Support check_mode.
> - The modules prefixed with na_cloudmanager are built to manage CloudManager and CVO deployments in AWS/GCP/Azure clouds.
> - If sa_client_id and sa_secret_key are provided, service account will be used in operations. refresh_token will be ignored.

## [Examples](na_cloudmanager_cvo_aws_module.md#id4)

```yaml+jinja
- name: Create NetApp Cloud Manager CVO for AWS single
  netapp.cloudmanager.na_cloudmanager_cvo_aws:
    state: present
    refresh_token: "{{ xxxxxxxxxxxxxxx }}"
    name: AnsibleCVO
    region: us-west-1
    subnet_id: subnet-xxxxxxx
    vpc_id: vpc-xxxxxxxx
    svm_password: P@assword!
    client_id: "{{ xxxxxxxxxxxxxxx }}"
    writing_speed_state: NORMAL
    aws_tag: [
        {tag_key: abc,
        tag_value: a123}]

- name: Create NetApp Cloud Manager CVO for AWS HA
  netapp.cloudmanager.na_cloudmanager_cvo_aws:
    state: present
    refresh_token: "{{ xxxxxxxxxxxxxxx }}"
    name: AnsibleCVO
    region: us-west-1
    subnet_id: subnet-xxxxxxx
    vpc_id: vpc-xxxxxxxx
    svm_password: P@assword!
    client_id: "{{ xxxxxxxxxxxxxxx }}"
    writing_speed_state: NORMAL
    aws_tag: [
        {tag_key: abc,
        tag_value: a123}]
    is_ha: true
    failover_mode: FloatingIP
    node1_subnet_id: subnet-1
    node2_subnet_id: subnet-1
    mediator_subnet_id: subnet-1
    mediator_key_pair_name: key1
    cluster_floating_ip: 2.1.1.1
    data_floating_ip: 2.1.1.2
    data_floating_ip2: 2.1.1.3
    svm_floating_ip: 2.1.1.4
    route_table_ids: [rt-1,rt-2]

- name: Delete NetApp Cloud Manager cvo for AWS
  netapp.cloudmanager.na_cloudmanager_cvo_aws:
    state: absent
    name: ansible
    region: us-west-1
    refresh_token: "{{ xxxxxxxxxxxxxxx }}"
    subnet_id: subnet-xxxxxxx
    vpc_id: vpc-xxxxxxxx
    svm_password: P@assword!
    client_id: "{{ xxxxxxxxxxxxxxx }}"
```

## [Return Values](na_cloudmanager_cvo_aws_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **working_environment_id**  string | Newly created AWS CVO working_environment_id.  **Returned:** success |

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.cloudmanager)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.cloudmanager)
