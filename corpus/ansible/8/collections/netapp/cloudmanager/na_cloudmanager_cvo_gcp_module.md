---
collection: ansible
version: "8"
title: "netapp.cloudmanager.na_cloudmanager_cvo_gcp module – NetApp Cloud Manager CVO for GCP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/cloudmanager/na_cloudmanager_cvo_gcp_module.html
fetched_at: 2026-07-28T02:41:10+00:00
---
# netapp.cloudmanager.na_cloudmanager_cvo_gcp module – NetApp Cloud Manager CVO for GCP

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
> To use it in a playbook, specify: `netapp.cloudmanager.na_cloudmanager_cvo_gcp`.

New in netapp.cloudmanager 21.4.0

- [Synopsis](na_cloudmanager_cvo_gcp_module.md#synopsis)
- [Parameters](na_cloudmanager_cvo_gcp_module.md#parameters)
- [Notes](na_cloudmanager_cvo_gcp_module.md#notes)
- [Examples](na_cloudmanager_cvo_gcp_module.md#examples)
- [Return Values](na_cloudmanager_cvo_gcp_module.md#return-values)

## [Synopsis](na_cloudmanager_cvo_gcp_module.md#id1)

- Create, delete, or manage Cloud Manager CVO for GCP.

## [Parameters](na_cloudmanager_cvo_gcp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **backup_volumes_to_cbs**  boolean | Automatically backup all volumes to cloud.  **Choices:**   - `false` ← (default) - `true` |
| **capacity_package_name**  string  *added in netapp.cloudmanager 21.12.0* | Capacity package name is required when selecting a capacity based license.  **Choices:**   - `"Professional"` - `"Essential"` ← (default) - `"Freemium"` |
| **capacity_tier**  string | Whether to enable data tiering for the first data aggregate.  **Choices:**   - `"cloudStorage"` |
| **client_id**  string / required | The connector ID of the Cloud Manager Connector.  You can find the ID from the Connector tab on <https://cloudmanager.netapp.com>. |
| **data_encryption_type**  string | Type of encryption to use for this working environment.  **Choices:**   - `"GCP"` |
| **enable_compliance**  boolean | Enable the Cloud Compliance service on the working environment.  **Choices:**   - `false` ← (default) - `true` |
| **environment**  string  *added in netapp.cloudmanager 21.8.0* | The environment for NetApp Cloud Manager API operations.  **Choices:**   - `"prod"` ← (default) - `"stage"` |
| **feature_flags**  dictionary  *added in netapp.cloudmanager 21.11.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **firewall_rule**  string | Firewall name for a single node cluster. |
| **gcp_encryption_parameters**  string  *added in netapp.cloudmanager 21.10.0* | The GCP encryption parameters. |
| **gcp_labels**  list / elements=dictionary | Optionally provide up to four key-value pairs with which to all GCP entities created by Cloud Manager. |
| **label_key**  string | The key of the label. |
| **label_value**  string | The label value. |
| **gcp_service_account**  string / required | The gcp_service_account email in order to enable tiering of cold data to Google Cloud Storage. |
| **gcp_volume_size**  integer | GCP volume size. |
| **gcp_volume_size_unit**  string | GCP volume size unit.  **Choices:**   - `"GB"` - `"TB"` |
| **gcp_volume_type**  string | GCP volume type.  **Choices:**   - `"pd-balanced"` - `"pd-standard"` - `"pd-ssd"` |
| **instance_type**  string | The type of instance to use, which depends on the license type you choose.  Explore [‘custom-4-16384’].  Standard [‘n1-standard-8’].  Premium [‘n1-standard-32’].  BYOL all instance types defined for PayGo.  For more supported instance types, refer to Cloud Volumes ONTAP Release Notes.  **Default:** `"n1-standard-8"` |
| **is_ha**  boolean | Indicate whether the working environment is an HA pair or not.  **Choices:**   - `false` ← (default) - `true` |
| **license_type**  string | The type of license to use.  For single node by Capacity [‘capacity-paygo’].  For single node by Node paygo [‘gcp-cot-explore-paygo’, ‘gcp-cot-standard-paygo’, ‘gcp-cot-premium-paygo’].  For single node by Node byol [‘gcp-cot-premium-byol’].  For HA by Capacity [‘ha-capacity-paygo’].  For HA by Node paygo [‘gcp-ha-cot-explore-paygo’, ‘gcp-ha-cot-standard-paygo’, ‘gcp-ha-cot-premium-paygo’].  For HA by Node byol [‘gcp-cot-premium-byol’].  **Choices:**   - `"gcp-cot-standard-paygo"` - `"gcp-cot-explore-paygo"` - `"gcp-cot-premium-paygo"` - `"gcp-cot-premium-byol"` - `"gcp-ha-cot-standard-paygo"` - `"gcp-ha-cot-premium-paygo"` - `"gcp-ha-cot-explore-paygo"` - `"gcp-ha-cot-premium-byol"` - `"capacity-paygo"` ← (default) - `"ha-capacity-paygo"` |
| **mediator_zone**  string | The zone for mediator.  Option for HA pair only. |
| **name**  string / required | The name of the Cloud Manager CVO for GCP to manage. |
| **network_project_id**  string | The project id in GCP associated with the Subnet.  If not provided, it is assumed that the Subnet is within the previously specified project id. |
| **node1_zone**  string | Zone for node 1.  Option for HA pair only. |
| **node2_zone**  string | Zone for node 2.  Option for HA pair only. |
| **nss_account**  string | The NetApp Support Site account ID to use with this Cloud Volumes ONTAP system.  If the license type is BYOL and an NSS account isn’t provided, Cloud Manager tries to use the first existing NSS account. |
| **ontap_version**  string | The required ONTAP version. Ignored if ‘use_latest_version’ is set to true.  **Default:** `"latest"` |
| **platform_serial_number**  string | The serial number for the system. Required when using ‘gcp-cot-premium-byol’. |
| **platform_serial_number_node1**  string | For HA BYOL, the serial number for the first node.  Option for HA pair only. |
| **platform_serial_number_node2**  string | For HA BYOL, the serial number for the second node.  Option for HA pair only. |
| **project_id**  string / required | The ID of the GCP project. |
| **provided_license**  string | Using a NLF license file for BYOL deployment |
| **refresh_token**  string | The refresh token for NetApp Cloud Manager API operations. |
| **sa_client_id**  string | The service account secret client ID for NetApp Cloud Manager API operations. |
| **sa_secret_key**  string | The service account secret key for NetApp Cloud Manager API operations. |
| **state**  string | Whether the specified Cloud Manager CVO for GCP should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subnet0_node_and_data_connectivity**  string | Subnet path for nic1, required for node and data connectivity.  If using shared VPC, network_project_id must be provided.  Option for HA pair only. |
| **subnet1_cluster_connectivity**  string | Subnet path for nic2, required for cluster connectivity.  Option for HA pair only. |
| **subnet2_ha_connectivity**  string | Subnet path for nic3, required for HA connectivity.  Option for HA pair only. |
| **subnet3_data_replication**  string | Subnet path for nic4, required for HA connectivity.  Option for HA pair only. |
| **subnet_id**  string | The name of the subnet for Cloud Volumes ONTAP. |
| **subnet_path**  string  *added in netapp.cloudmanager 21.20.0* | Subnet path for a single node cluster. |
| **svm_name**  string  *added in netapp.cloudmanager 21.22.0* | The name of the SVM. |
| **svm_password**  string | The admin password for Cloud Volumes ONTAP.  It will be updated on each run. |
| **tier_level**  string | The tiering level when ‘capacity_tier’ is set to ‘cloudStorage’.  **Choices:**   - `"standard"` ← (default) - `"nearline"` - `"coldline"` |
| **update_svm_password**  boolean  *added in netapp.cloudmanager 21.13.0* | Indicates whether to update svm_password on the CVO.  When set to true, the module is not idempotent, as we cannot read the current password.  **Choices:**   - `false` ← (default) - `true` |
| **upgrade_ontap_version**  boolean  *added in netapp.cloudmanager 21.13.0* | Indicates whether to upgrade ONTAP image on the CVO.  If the current version already matches the desired version, no action is taken.  **Choices:**   - `false` ← (default) - `true` |
| **use_latest_version**  boolean | Indicates whether to use the latest available ONTAP version.  **Choices:**   - `false` - `true` ← (default) |
| **vpc0_firewall_rule_name**  string | Firewall rule name for vpc1.  Option for HA pair only. |
| **vpc0_node_and_data_connectivity**  string | VPC path for nic1, required for node and data connectivity.  If using shared VPC, network_project_id must be provided.  Option for HA pair only. |
| **vpc1_cluster_connectivity**  string | VPC path for nic2, required for cluster connectivity.  Option for HA pair only. |
| **vpc1_firewall_rule_name**  string | Firewall rule name for vpc2.  Option for HA pair only. |
| **vpc2_firewall_rule_name**  string | Firewall rule name for vpc3.  Option for HA pair only. |
| **vpc2_ha_connectivity**  string | VPC path for nic3, required for HA connectivity.  Option for HA pair only. |
| **vpc3_data_replication**  string | VPC path for nic4, required for data replication.  Option for HA pair only. |
| **vpc3_firewall_rule_name**  string | Firewall rule name for vpc4.  Option for HA pair only. |
| **vpc_id**  string / required | The name of the VPC. |
| **workspace_id**  string | The ID of the Cloud Manager workspace where you want to deploy Cloud Volumes ONTAP.  If not provided, Cloud Manager uses the first workspace.  You can find the ID from the Workspace tab on [<https://cloudmanager.netapp.com>]. |
| **writing_speed_state**  string | The write speed setting for Cloud Volumes ONTAP [‘NORMAL’,’HIGH’].  Default value is ‘NORMAL’ for non-HA GCP CVO  This argument is not relevant for HA pairs. |
| **zone**  string / required | The zone of the region where the working environment will be created. |

## [Notes](na_cloudmanager_cvo_gcp_module.md#id3)

> **Note:**
>
> - Support check_mode.
> - The modules prefixed with na_cloudmanager are built to manage CloudManager and CVO deployments in AWS/GCP/Azure clouds.
> - If sa_client_id and sa_secret_key are provided, service account will be used in operations. refresh_token will be ignored.

## [Examples](na_cloudmanager_cvo_gcp_module.md#id4)

```yaml+jinja
- name: Create NetApp Cloud Manager cvo for GCP
  netapp.cloudmanager.na_cloudmanager_cvo_gcp:
    state: present
    name: ansiblecvogcp
    project_id: default-project
    zone: us-east4-b
    subnet_path: projects/<project>/regions/<region>/subnetworks/<subnetwork>
    subnet_id: projects/<project>/regions/<region>/subnetworks/<subnetwork>
    gcp_volume_type: pd-ssd
    gcp_volume_size: 500
    gcp_volume_size_unit: GB
    gcp_service_account: "{{ xxxxxxxxxxxxxxx }}"
    data_encryption_type: GCP
    svm_password: "{{ xxxxxxxxxxxxxxx }}"
    ontap_version: latest
    use_latest_version: true
    license_type: capacity-paygo
    instance_type: n1-standard-8
    client_id: "{{ xxxxxxxxxxxxxxx }}"
    workspace_id: "{{ xxxxxxxxxxxxxxx }}"
    capacity_tier: cloudStorage
    writing_speed_state: NORMAL
    refresh_token: "{{ xxxxxxxxxxxxxxx }}"
    vpc_id: default
    gcp_labels:
      - label_key: key1
        label_value: value1
      - label_key: key2
        label_value: value2

- name: Create NetApp Cloud Manager cvo ha for GCP
  netapp.cloudmanager.na_cloudmanager_cvo_gcp:
    state: present
    name: ansiblecvogcpha
    project_id: "default-project"
    zone: us-east1-b
    gcp_volume_type: pd-ssd
    gcp_volume_size: 500
    gcp_volume_size_unit: GB
    gcp_service_account: "{{ xxxxxxxxxxxxxxx }}"
    data_encryption_type: GCP
    svm_password: "{{ xxxxxxxxxxxxxxx }}"
    ontap_version: ONTAP-9.9.0.T1.gcpha
    use_latest_version: false
    license_type: ha-capacity-paygo
    instance_type: custom-4-16384
    client_id: "{{ xxxxxxxxxxxxxxx }}"
    workspace_id:  "{{ xxxxxxxxxxxxxxx }}"
    capacity_tier: cloudStorage
    writing_speed_state: NORMAL
    refresh_token: "{{ xxxxxxxxxxxxxxx }}"
    is_ha: true
    mediator_zone: us-east1-b
    node1_zone: us-east1-b
    node2_zone: us-east1-b
    subnet0_node_and_data_connectivity: default
    subnet1_cluster_connectivity: subnet2
    subnet2_ha_connectivity: subnet3
    subnet3_data_replication: subnet1
    vpc0_node_and_data_connectivity: default
    vpc1_cluster_connectivity: vpc2
    vpc2_ha_connectivity: vpc3
    vpc3_data_replication: vpc1
    vpc_id: default
    subnet_id: default
```

## [Return Values](na_cloudmanager_cvo_gcp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **working_environment_id**  string | Newly created GCP CVO working_environment_id.  **Returned:** success |

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.cloudmanager)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.cloudmanager)
