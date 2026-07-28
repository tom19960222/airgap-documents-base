---
collection: ansible
version: "6"
title: "community.general.hwc_ecs_instance module – Creates a resource of Ecs/Instance in Huawei Cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/hwc_ecs_instance_module.html
fetched_at: 2026-07-27T17:09:24+00:00
---
# community.general.hwc_ecs_instance module – Creates a resource of Ecs/Instance in Huawei Cloud

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](hwc_ecs_instance_module.md#ansible-collections-community-general-hwc-ecs-instance-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.hwc_ecs_instance`.

New in community.general 0.2.0

- [Synopsis](hwc_ecs_instance_module.md#synopsis)
- [Requirements](hwc_ecs_instance_module.md#requirements)
- [Parameters](hwc_ecs_instance_module.md#parameters)
- [Notes](hwc_ecs_instance_module.md#notes)
- [Examples](hwc_ecs_instance_module.md#examples)
- [Return Values](hwc_ecs_instance_module.md#return-values)

## [Synopsis](hwc_ecs_instance_module.md#id1)

- instance management.

## [Requirements](hwc_ecs_instance_module.md#id2)

The below requirements are needed on the host that executes this module.

- keystoneauth1 >= 3.6.0

## [Parameters](hwc_ecs_instance_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **admin_pass**  string | Specifies the initial login password of the administrator account for logging in to an ECS using password authentication. The Linux administrator is root, and the Windows administrator is Administrator. Password complexity requirements, consists of 8 to 26 characters. The password must contain at least three of the following character types ‘uppercase letters, lowercase letters, digits, and special characters (!@$%^-_=+[{}]:,./?)’. The password cannot contain the username or the username in reverse. The Windows ECS password cannot contain the username, the username in reverse, or more than two consecutive characters in the username. |
| **availability_zone**  string / required | Specifies the name of the AZ where the ECS is located. |
| **data_volumes**  list / elements=dictionary | Specifies the data disks of ECS instance. |
| **device**  string | Specifies the disk device name. |
| **volume_id**  string / required | Specifies the disk ID. |
| **description**  string | Specifies the description of an ECS, which is a null string by default. Can contain a maximum of 85 characters. Cannot contain special characters, such as < and >. |
| **domain**  string / required | The name of the Domain to scope to (Identity v3). (currently only domain names are supported, and not domain IDs). |
| **eip_id**  string | Specifies the ID of the elastic IP address assigned to the ECS. Only elastic IP addresses in the DOWN state can be assigned. |
| **enable_auto_recovery**  boolean | Specifies whether automatic recovery is enabled on the ECS.  Choices:   - `false` - `true` |
| **enterprise_project_id**  string | Specifies the ID of the enterprise project to which the ECS belongs. |
| **flavor_name**  string / required | Specifies the name of the system flavor. |
| **id**  string | The id of resource to be managed. |
| **identity_endpoint**  string / required | The Identity authentication URL. |
| **image_id**  string / required | Specifies the ID of the system image. |
| **name**  string / required | Specifies the ECS name. Value requirements consists of 1 to 64 characters, including letters, digits, underscores `_`, hyphens (-), periods (.). |
| **nics**  list / elements=dictionary / required | Specifies the NIC information of the ECS. Constraints the network of the NIC must belong to the VPC specified by vpc_id. A maximum of 12 NICs can be attached to an ECS. |
| **ip_address**  string / required | Specifies the IP address of the NIC. The value is an IPv4 address. Its value must be an unused IP address in the network segment of the subnet. |
| **subnet_id**  string / required | Specifies the ID of subnet. |
| **password**  string / required | The password to login with. |
| **project**  string / required | The name of the Tenant (Identity v2) or Project (Identity v3). (currently only project names are supported, and not project IDs). |
| **region**  string | The region to which the project belongs. |
| **root_volume**  dictionary / required | Specifies the configuration of the ECS’s system disks. |
| **size**  integer | Specifies the system disk size, in GB. The value range is 1 to 1024. The system disk size must be greater than or equal to the minimum system disk size supported by the image (min_disk attribute of the image). If this parameter is not specified or is set to 0, the default system disk size is the minimum value of the system disk in the image (min_disk attribute of the image). |
| **snapshot_id**  string | Specifies the snapshot ID or ID of the original data disk contained in the full-ECS image. |
| **volume_type**  string / required | Specifies the ECS system disk type.  SATA is common I/O disk type.  SAS is high I/O disk type.  SSD is ultra-high I/O disk type.  co-p1 is high I/O (performance-optimized I) disk type.  uh-l1 is ultra-high I/O (latency-optimized) disk type.  NOTE is For HANA, HL1, and HL2 ECSs, use co-p1 and uh-l1 disks. For other ECSs, do not use co-p1 or uh-l1 disks. |
| **security_groups**  list / elements=string | Specifies the security groups of the ECS. If this parameter is left blank, the default security group is bound to the ECS by default. |
| **server_metadata**  dictionary | Specifies the metadata of ECS to be created. |
| **server_tags**  dictionary | Specifies the tags of an ECS. When you create ECSs, one ECS supports up to 10 tags. |
| **ssh_key_name**  string | Specifies the name of the SSH key used for logging in to the ECS. |
| **state**  string | Whether the given object should exist in Huawei Cloud.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeouts**  dictionary | The timeouts for each operations.  Default: `{}` |
| **create**  string | The timeouts for create operation.  Default: `"30m"` |
| **delete**  string | The timeouts for delete operation.  Default: `"30m"` |
| **update**  string | The timeouts for update operation.  Default: `"30m"` |
| **user**  string / required | The user name to login with (currently only user names are supported, and not user IDs). |
| **user_data**  string | Specifies the user data to be injected during the ECS creation process. Text, text files, and gzip files can be injected. The content to be injected must be encoded with base64. The maximum size of the content to be injected (before encoding) is 32 KB. For Linux ECSs, this parameter does not take effect when adminPass is used. |
| **vpc_id**  string / required | Specifies the ID of the VPC to which the ECS belongs. |

## [Notes](hwc_ecs_instance_module.md#id4)

> **Note:**
>
> - For authentication, you can set identity_endpoint using the `ANSIBLE_HWC_IDENTITY_ENDPOINT` env variable.
> - For authentication, you can set user using the `ANSIBLE_HWC_USER` env variable.
> - For authentication, you can set password using the `ANSIBLE_HWC_PASSWORD` env variable.
> - For authentication, you can set domain using the `ANSIBLE_HWC_DOMAIN` env variable.
> - For authentication, you can set project using the `ANSIBLE_HWC_PROJECT` env variable.
> - For authentication, you can set region using the `ANSIBLE_HWC_REGION` env variable.
> - Environment variables values will only be used if the playbook values are not set.

## [Examples](hwc_ecs_instance_module.md#id5)

```yaml+jinja
# create an ecs instance
- name: Create a vpc
  hwc_network_vpc:
    cidr: "192.168.100.0/24"
    name: "ansible_network_vpc_test"
  register: vpc
- name: Create a subnet
  hwc_vpc_subnet:
    gateway_ip: "192.168.100.32"
    name: "ansible_network_subnet_test"
    dhcp_enable: true
    vpc_id: "{{ vpc.id }}"
    cidr: "192.168.100.0/26"
  register: subnet
- name: Create a eip
  hwc_vpc_eip:
    dedicated_bandwidth:
      charge_mode: "traffic"
      name: "ansible_test_dedicated_bandwidth"
      size: 1
    type: "5_bgp"
  register: eip
- name: Create a disk
  hwc_evs_disk:
    availability_zone: "cn-north-1a"
    name: "ansible_evs_disk_test"
    volume_type: "SATA"
    size: 10
  register: disk
- name: Create an instance
  community.general.hwc_ecs_instance:
    data_volumes:
      - volume_id: "{{ disk.id }}"
    enable_auto_recovery: false
    eip_id: "{{ eip.id }}"
    name: "ansible_ecs_instance_test"
    availability_zone: "cn-north-1a"
    nics:
      - subnet_id: "{{ subnet.id }}"
        ip_address: "192.168.100.33"
      - subnet_id: "{{ subnet.id }}"
        ip_address: "192.168.100.34"
    server_tags:
      my_server: "my_server"
    image_id: "8da46d6d-6079-4e31-ad6d-a7167efff892"
    flavor_name: "s3.small.1"
    vpc_id: "{{ vpc.id }}"
    root_volume:
      volume_type: "SAS"
```

## [Return Values](hwc_ecs_instance_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **admin_pass**  string | Specifies the initial login password of the administrator account for logging in to an ECS using password authentication. The Linux administrator is root, and the Windows administrator is Administrator. Password complexity requirements consists of 8 to 26 characters. The password must contain at least three of the following character types “uppercase letters, lowercase letters, digits, and special characters (!@$%^-_=+[{}]:,./?)”. The password cannot contain the username or the username in reverse. The Windows ECS password cannot contain the username, the username in reverse, or more than two consecutive characters in the username.  Returned: success |
| **availability_zone**  string | Specifies the name of the AZ where the ECS is located.  Returned: success |
| **config_drive**  string | Specifies the configuration driver.  Returned: success |
| **created**  string | Specifies the time when an ECS was created.  Returned: success |
| **data_volumes**  list / elements=string | Specifies the data disks of ECS instance.  Returned: success |
| **device**  string | Specifies the disk device name.  Returned: success |
| **volume_id**  string | Specifies the disk ID.  Returned: success |
| **description**  string | Specifies the description of an ECS, which is a null string by default. Can contain a maximum of 85 characters. Cannot contain special characters, such as < and >.  Returned: success |
| **disk_config_type**  string | Specifies the disk configuration type. MANUAL is The image space is not expanded. AUTO is the image space of the system disk will be expanded to be as same as the flavor.  Returned: success |
| **eip_id**  string | Specifies the ID of the elastic IP address assigned to the ECS. Only elastic IP addresses in the DOWN state can be assigned.  Returned: success |
| **enable_auto_recovery**  boolean | Specifies whether automatic recovery is enabled on the ECS.  Returned: success |
| **enterprise_project_id**  string | Specifies the ID of the enterprise project to which the ECS belongs.  Returned: success |
| **flavor_name**  string | Specifies the name of the system flavor.  Returned: success |
| **host_name**  string | Specifies the host name of the ECS.  Returned: success |
| **image_id**  string | Specifies the ID of the system image.  Returned: success |
| **image_name**  string | Specifies the image name of the ECS.  Returned: success |
| **name**  string | Specifies the ECS name. Value requirements “Consists of 1 to 64 characters, including letters, digits, underscores `_`, hyphens (-), periods (.)”.  Returned: success |
| **nics**  list / elements=string | Specifies the NIC information of the ECS. The network of the NIC must belong to the VPC specified by vpc_id. A maximum of 12 NICs can be attached to an ECS.  Returned: success |
| **ip_address**  string | Specifies the IP address of the NIC. The value is an IPv4 address. Its value must be an unused IP address in the network segment of the subnet.  Returned: success |
| **port_id**  string | Specifies the port ID corresponding to the IP address.  Returned: success |
| **subnet_id**  string | Specifies the ID of subnet.  Returned: success |
| **power_state**  integer | Specifies the power status of the ECS.  Returned: success |
| **root_volume**  dictionary | Specifies the configuration of the ECS’s system disks.  Returned: success |
| **device**  string | Specifies the disk device name.  Returned: success |
| **size**  integer | Specifies the system disk size, in GB. The value range is 1 to 1024. The system disk size must be greater than or equal to the minimum system disk size supported by the image (min_disk attribute of the image). If this parameter is not specified or is set to 0, the default system disk size is the minimum value of the system disk in the image (min_disk attribute of the image).  Returned: success |
| **snapshot_id**  string | Specifies the snapshot ID or ID of the original data disk contained in the full-ECS image.  Returned: success |
| **volume_id**  string | Specifies the disk ID.  Returned: success |
| **volume_type**  string | Specifies the ECS system disk type.  SATA is common I/O disk type.  SAS is high I/O disk type.  SSD is ultra-high I/O disk type.  co-p1 is high I/O (performance-optimized I) disk type.  uh-l1 is ultra-high I/O (latency-optimized) disk type.  NOTE is For HANA, HL1, and HL2 ECSs, use co-p1 and uh-l1 disks. For other ECSs, do not use co-p1 or uh-l1 disks.  Returned: success |
| **security_groups**  list / elements=string | Specifies the security groups of the ECS. If this parameter is left blank, the default security group is bound to the ECS by default.  Returned: success |
| **server_alias**  string | Specifies the ECS alias.  Returned: success |
| **server_metadata**  dictionary | Specifies the metadata of ECS to be created.  Returned: success |
| **server_tags**  dictionary | Specifies the tags of an ECS. When you create ECSs, one ECS supports up to 10 tags.  Returned: success |
| **ssh_key_name**  string | Specifies the name of the SSH key used for logging in to the ECS.  Returned: success |
| **status**  string | Specifies the ECS status. Options are ACTIVE, REBOOT, HARD_REBOOT, REBUILD, MIGRATING, BUILD, SHUTOFF, RESIZE, VERIFY_RESIZE, ERROR, and DELETED.  Returned: success |
| **user_data**  string | Specifies the user data to be injected during the ECS creation process. Text, text files, and gzip files can be injected. The content to be injected must be encoded with base64. The maximum size of the content to be injected (before encoding) is 32 KB. For Linux ECSs, this parameter does not take effect when adminPass is used.  Returned: success |
| **vpc_id**  string | Specifies the ID of the VPC to which the ECS belongs.  Returned: success |

### Authors

- Huawei Inc. (@huaweicloud)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
