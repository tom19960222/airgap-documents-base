---
collection: ansible
version: "6"
title: "netapp.cloudmanager.na_cloudmanager_cvo_azure module – NetApp Cloud Manager CVO/working environment in single or HA mode for Azure."
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/cloudmanager/na_cloudmanager_cvo_azure_module.html
fetched_at: 2026-07-28T00:11:37+00:00
---
# netapp.cloudmanager.na_cloudmanager_cvo_azure module – NetApp Cloud Manager CVO/working environment in single or HA mode for Azure.

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
> To use it in a playbook, specify: `netapp.cloudmanager.na_cloudmanager_cvo_azure`.

New in netapp.cloudmanager 21.4.0

- [Synopsis](na_cloudmanager_cvo_azure_module.md#synopsis)
- [Parameters](na_cloudmanager_cvo_azure_module.md#parameters)
- [Notes](na_cloudmanager_cvo_azure_module.md#notes)
- [Examples](na_cloudmanager_cvo_azure_module.md#examples)
- [Return Values](na_cloudmanager_cvo_azure_module.md#return-values)

## [Synopsis](na_cloudmanager_cvo_azure_module.md#id1)

- Create, delete, or manage Cloud Manager CVO/working environment in single or HA mode for Azure.

## [Parameters](na_cloudmanager_cvo_azure_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **allow_deploy_in_existing_rg**  boolean | Indicates if to allow creation in existing resource group.  Choices:   - `false` ← (default) - `true` |
| **availability_zone**  integer  added in netapp.cloudmanager 21.20.0 | The availability zone on the location configuration. |
| **availability_zone_node1**  integer  added in netapp.cloudmanager 21.21.0 | The node1 availability zone on the location configuration for HA. |
| **availability_zone_node2**  integer  added in netapp.cloudmanager 21.21.0 | The node2 availability zone on the location configuration for HA. |
| **azure_encryption_parameters**  string  added in netapp.cloudmanager 21.10.0 | AZURE encryption parameters. It is required if using AZURE encryption. |
| **azure_tag**  list / elements=dictionary | Additional tags for the AZURE CVO working environment. |
| **tag_key**  string | The key of the tag. |
| **tag_value**  string | The tag value. |
| **backup_volumes_to_cbs**  boolean | Automatically enable back up of all volumes to S3.  Choices:   - `false` ← (default) - `true` |
| **capacity_package_name**  string  added in netapp.cloudmanager 21.12.0 | Capacity package name is required when selecting a capacity based license.  Essential only available with Bring Your Own License Capacity-Based.  Professional available as an annual contract from a cloud provider or Bring Your Own License Capacity-Based.  Choices:   - `"Professional"` - `"Essential"` ← (default) - `"Freemium"` |
| **capacity_tier**  string | Whether to enable data tiering for the first data aggregate.  Choices:   - `"Blob"` ← (default) - `"NONE"` |
| **cidr**  string / required | The CIDR of the VNET. If not provided, resource needs az login to authorize and fetch the cidr details from Azure. |
| **client_id**  string / required | The connector ID of the Cloud Manager Connector.  You can find the ID from the Connector tab on [<https://cloudmanager.netapp.com>]. |
| **cloud_provider_account**  string | The cloud provider credentials id to use when deploying the Cloud Volumes ONTAP system.  You can find the ID in Cloud Manager from the Settings > Credentials page.  If not specified, Cloud Manager uses the instance profile of the Connector. |
| **data_encryption_type**  string | The type of encryption to use for the working environment.  Choices:   - `"AZURE"` ← (default) - `"NONE"` |
| **disk_size**  integer | Azure volume size for the first data aggregate.  For GB, the value can be [100, 500].  For TB, the value can be [1,2,4,8,16].  Default: `1` |
| **disk_size_unit**  string | The unit for disk size.  Choices:   - `"GB"` - `"TB"` ← (default) |
| **enable_compliance**  boolean | Enable the Cloud Compliance service on the working environment.  Choices:   - `false` ← (default) - `true` |
| **enable_monitoring**  boolean | Enable the Monitoring service on the working environment.  Choices:   - `false` ← (default) - `true` |
| **environment**  string  added in netapp.cloudmanager 21.8.0 | The environment for NetApp Cloud Manager API operations.  Choices:   - `"prod"` ← (default) - `"stage"` |
| **feature_flags**  dictionary  added in netapp.cloudmanager 21.11.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **ha_enable_https**  boolean  added in netapp.cloudmanager 21.10.0 | For HA, enable the HTTPS connection from CVO to storage accounts. This can impact write performance. The default is false.  Choices:   - `false` - `true` |
| **instance_type**  string | The type of instance to use, which depends on the license type you chose.  Explore [‘Standard_DS3_v2’].  Standard [‘Standard_DS4_v2, Standard_DS13_v2, Standard_L8s_v2’].  Premium [‘Standard_DS5_v2’, ‘Standard_DS14_v2’].  For more supported instance types, refer to Cloud Volumes ONTAP Release Notes.  Default: `"Standard_DS4_v2"` |
| **is_ha**  boolean | Indicate whether the working environment is an HA pair or not.  Choices:   - `false` ← (default) - `true` |
| **license_type**  string | The type of license to use.  For single node by Capacity [‘capacity-paygo’].  For single node by Node paygo [‘azure-cot-explore-paygo’, ‘azure-cot-standard-paygo’, ‘azure-cot-premium-paygo’].  For single node by Node byol [‘azure-cot-premium-byol’].  For HA by Capacity [‘ha-capacity-paygo’].  For HA by Node paygo [‘azure-ha-cot-standard-paygo’, ‘azure-ha-cot-premium-paygo’].  For HA by Node byol [‘azure-ha-cot-premium-byol’].  Choices:   - `"azure-cot-standard-paygo"` - `"azure-cot-premium-paygo"` - `"azure-cot-premium-byol"` - `"azure-cot-explore-paygo"` - `"azure-ha-cot-standard-paygo"` - `"azure-ha-cot-premium-paygo"` - `"azure-ha-cot-premium-byol"` - `"capacity-paygo"` ← (default) - `"ha-capacity-paygo"` |
| **location**  string / required | The location where the working environment will be created. |
| **name**  string / required | The name of the Cloud Manager CVO for AZURE to manage. |
| **nss_account**  string | The NetApp Support Site account ID to use with this Cloud Volumes ONTAP system.  If the license type is BYOL and an NSS account isn’t provided, Cloud Manager tries to use the first existing NSS account. |
| **ontap_version**  string | The required ONTAP version. Ignored if ‘use_latest_version’ is set to true.  Default: `"latest"` |
| **platform_serial_number_node1**  string | For HA BYOL, the serial number for the first node. |
| **platform_serial_number_node2**  string | For HA BYOL, the serial number for the second node. |
| **provided_license**  string | Using a NLF license file for BYOL deployment. |
| **refresh_token**  string | The refresh token for NetApp Cloud Manager API operations. |
| **resource_group**  string | The resource_group where Cloud Volumes ONTAP will be created.  If not provided, Cloud Manager generates the resource group name (name of the working environment/CVO with suffix ‘-rg’).  If the resource group does not exist, it is created. |
| **sa_client_id**  string | The service account secret client ID for NetApp Cloud Manager API operations. |
| **sa_secret_key**  string | The service account secret key for NetApp Cloud Manager API operations. |
| **security_group_id**  string | The ID of the security group for the working environment. If not provided, Cloud Manager creates the security group. |
| **serial_number**  string | The serial number for the cluster.  Required when using one of these, ‘azure-cot-premium-byol’ or ‘azure-ha-cot-premium-byol’. |
| **state**  string | Whether the specified Cloud Manager CVO for AZURE should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **storage_type**  string | The type of storage for the first data aggregate.  Choices:   - `"Premium_LRS"` ← (default) - `"Standard_LRS"` - `"StandardSSD_LRS"` - `"Premium_ZRS"` |
| **subnet_id**  string / required | The name of the subnet for the Cloud Volumes ONTAP system. |
| **subscription_id**  string / required | The ID of the Azure subscription. |
| **svm_password**  string / required | The admin password for Cloud Volumes ONTAP.  It will be updated on each run. |
| **tier_level**  string | If capacity_tier is Blob, this argument indicates the tiering level.  Choices:   - `"normal"` ← (default) - `"cool"` |
| **update_svm_password**  boolean  added in netapp.cloudmanager 21.13.0 | Indicates whether to update svm_password on the CVO.  When set to true, the module is not idempotent, as we cannot read the current password.  Choices:   - `false` ← (default) - `true` |
| **upgrade_ontap_version**  boolean  added in netapp.cloudmanager 21.13.0 | Indicates whether to upgrade ONTAP image on the CVO.  If the current version already matches the desired version, no action is taken.  Choices:   - `false` ← (default) - `true` |
| **use_latest_version**  boolean | Indicates whether to use the latest available ONTAP version.  Choices:   - `false` - `true` ← (default) |
| **vnet_id**  string / required | The name of the virtual network. |
| **vnet_resource_group**  string | The resource group in Azure associated to the virtual network. |
| **workspace_id**  string | The ID of the Cloud Manager workspace where you want to deploy Cloud Volumes ONTAP.  If not provided, Cloud Manager uses the first workspace.  You can find the ID from the Workspace tab on [<https://cloudmanager.netapp.com>]. |
| **writing_speed_state**  string | The write speed setting for Cloud Volumes ONTAP [‘NORMAL’,’HIGH’].  This argument is not relevant for HA pairs. |

## [Notes](na_cloudmanager_cvo_azure_module.md#id3)

> **Note:**
>
> - The modules prefixed with na_cloudmanager are built to manage CloudManager and CVO deployments in AWS/GCP/Azure clouds.
> - If sa_client_id and sa_secret_key are provided, service account will be used in operations. refresh_token will be ignored.

## [Examples](na_cloudmanager_cvo_azure_module.md#id4)

```yaml+jinja
- name: create NetApp Cloud Manager CVO for Azure single
  netapp.cloudmanager.na_cloudmanager_cvo_azure:
    state: present
    refresh_token: "{{ xxxxxxxxxxxxxxx }}"
    name: AnsibleCVO
    location: westus
    subnet_id: subnet-xxxxxxx
    vnet_id: vnetxxxxxxxx
    svm_password: P@assword!
    client_id: "{{ xxxxxxxxxxxxxxx }}"
    writing_speed_state: NORMAL
    azure_tag: [
        {tag_key: abc,
        tag_value: a123}]

- name: create NetApp Cloud Manager CVO for Azure HA
  netapp.cloudmanager.na_cloudmanager_cvo_azure:
    state: present
    refresh_token: "{{ xxxxxxxxxxxxxxx }}"
    name: AnsibleCVO
    location: westus
    subnet_id: subnet-xxxxxxx
    vnet_id: vnetxxxxxxxx
    svm_password: P@assword!
    client_id: "{{ xxxxxxxxxxxxxxx }}"
    writing_speed_state: NORMAL
    azure_tag: [
        {tag_key: abc,
        tag_value: a123}]
    is_ha: true

- name: delete NetApp Cloud Manager cvo for Azure
  netapp.cloudmanager.na_cloudmanager_cvo_azure:
    state: absent
    name: ansible
    refresh_token: "{{ xxxxxxxxxxxxxxx }}"
    location: westus
    subnet_id: subnet-xxxxxxx
    vnet_id: vnetxxxxxxxx
    svm_password: P@assword!
    client_id: "{{ xxxxxxxxxxxxxxx }}"
```

## [Return Values](na_cloudmanager_cvo_azure_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **working_environment_id**  string | Newly created AZURE CVO working_environment_id.  Returned: success |

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.cloudmanager)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.cloudmanager)
