---
collection: ansible
version: "8"
title: "community.general.ali_instance_info module – Gather information on instances of Alibaba Cloud ECS"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/ali_instance_info_module.html
fetched_at: 2026-07-28T01:44:37+00:00
---
# community.general.ali_instance_info module – Gather information on instances of Alibaba Cloud ECS

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
> see [Requirements](ali_instance_info_module.md#ansible-collections-community-general-ali-instance-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.ali_instance_info`.

- [Synopsis](ali_instance_info_module.md#synopsis)
- [Requirements](ali_instance_info_module.md#requirements)
- [Parameters](ali_instance_info_module.md#parameters)
- [Attributes](ali_instance_info_module.md#attributes)
- [Notes](ali_instance_info_module.md#notes)
- [Examples](ali_instance_info_module.md#examples)
- [Return Values](ali_instance_info_module.md#return-values)

## [Synopsis](ali_instance_info_module.md#id1)

- This module fetches data from the Open API in Alicloud. The module must be called from within the ECS instance itself.
- This module was called `ali_instance_facts` before Ansible 2.9. The usage did not change.

Aliases: cloud.alicloud.ali_instance_info

## [Requirements](ali_instance_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- footmark >= 1.13.0
- python >= 3.6

## [Parameters](ali_instance_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **alicloud_access_key**  aliases: access_key_id, access_key  string | Alibaba Cloud access key. If not set then the value of environment variable `ALICLOUD_ACCESS_KEY`, `ALICLOUD_ACCESS_KEY_ID` will be used instead. |
| **alicloud_assume_role**  aliases: assume_role  dictionary | If provided with a role ARN, Ansible will attempt to assume this role using the supplied credentials.  The nested assume_role block supports `alicloud_assume_role_arn`, `alicloud_assume_role_session_name`, `alicloud_assume_role_session_expiration` and `alicloud_assume_role_policy`. |
| **alicloud_assume_role_arn**  aliases: assume_role_arn  string | The Alibaba Cloud role_arn. The ARN of the role to assume. If ARN is set to an empty string, it does not perform role switching. It supports environment variable `ALICLOUD_ASSUME_ROLE_ARN`. ansible will execute with provided credentials. |
| **alicloud_assume_role_session_expiration**  aliases: assume_role_session_expiration  integer | The Alibaba Cloud session_expiration. The time after which the established session for assuming role expires. Valid value range 900-3600 seconds. Default to 3600 (in this case Alicloud use own default value). It supports environment variable `ALICLOUD_ASSUME_ROLE_SESSION_EXPIRATION`. |
| **alicloud_assume_role_session_name**  aliases: assume_role_session_name  string | The Alibaba Cloud session_name. The session name to use when assuming the role. If omitted, ‘ansible’ is passed to the AssumeRole call as session name. It supports environment variable `ALICLOUD_ASSUME_ROLE_SESSION_NAME`. |
| **alicloud_region**  aliases: region, region_id  string / required | The Alibaba Cloud region to use. If not specified then the value of environment variable `ALICLOUD_REGION`, `ALICLOUD_REGION_ID` will be used instead. |
| **alicloud_secret_key**  aliases: secret_access_key, secret_key  string | Alibaba Cloud secret key. If not set then the value of environment variable `ALICLOUD_SECRET_KEY`, `ALICLOUD_SECRET_ACCESS_KEY` will be used instead. |
| **alicloud_security_token**  aliases: security_token  string | The Alibaba Cloud security token. If not specified then the value of environment variable `ALICLOUD_SECURITY_TOKEN` will be used instead. |
| **ecs_role_name**  aliases: role_name  string | The RAM Role Name attached on a ECS instance for API operations. You can retrieve this from the ‘Access Control’ section of the Alibaba Cloud console.  If you’re running Ansible from an ECS instance with RAM Instance using RAM Role, Ansible will just access the metadata <http://100.100.100.200/latest/meta-data/ram/security-credentials/%3Cecs_role_name%3E> to obtain the STS credential. This is a preferred approach over any other when running in ECS as you can avoid hard coding credentials. Instead these are leased on-the-fly by Ansible which reduces the chance of leakage. |
| **filters**  dictionary  *added in community.general 0.2.0* | A dict of filters to apply. Each dict item consists of a filter key and a filter value. The filter keys can be all of request parameters. See <https://www.alibabacloud.com/help/doc-detail/25506.htm> for parameter details. Filter keys can be same as request parameter name or be lower case and use underscore (`"_"`) or dash (`"-"`) to connect different words in one parameter. `InstanceIds` should be a list. `Tag.n.Key` and `Tag.n.Value` should be a dict and using `tags` instead. |
| **name_prefix**  string  *added in community.general 0.2.0* | Use a instance name prefix to filter ecs instances. |
| **profile**  string | This is the Alicloud profile name as set in the shared credentials file. It can also be sourced from the `ALICLOUD_PROFILE` environment variable. |
| **shared_credentials_file**  string | This is the path to the shared credentials file. It can also be sourced from the `ALICLOUD_SHARED_CREDENTIALS_FILE` environment variable.  If this is not set and a profile is specified, ~/.aliyun/config.json will be used. |
| **tags**  aliases: instance_tags  dictionary | A hash/dictionaries of instance tags. `{"key":"value"}` |

## [Attributes](ali_instance_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  *added in community.general 3.3.0*  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](ali_instance_info_module.md#id5)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `ALICLOUD_ACCESS_KEY` or `ALICLOUD_ACCESS_KEY_ID`, `ALICLOUD_SECRET_KEY` or `ALICLOUD_SECRET_ACCESS_KEY`, `ALICLOUD_REGION` or `ALICLOUD_REGION_ID`, `ALICLOUD_SECURITY_TOKEN`, `ALICLOUD_ECS_ROLE_NAME`, `ALICLOUD_SHARED_CREDENTIALS_FILE`, `ALICLOUD_PROFILE`, `ALICLOUD_ASSUME_ROLE_ARN`, `ALICLOUD_ASSUME_ROLE_SESSION_NAME`, `ALICLOUD_ASSUME_ROLE_SESSION_EXPIRATION`,
> - `ALICLOUD_REGION` or `ALICLOUD_REGION_ID` can be typically be used to specify the ALICLOUD region, when required, but this can also be configured in the footmark config file

## [Examples](ali_instance_info_module.md#id6)

```yaml+jinja
# Fetch instances details according to setting different filters

- name: Find all instances in the specified region
  community.general.ali_instance_info:
  register: all_instances

- name: Find all instances based on the specified ids
  community.general.ali_instance_info:
    instance_ids:
      - "i-35b333d9"
      - "i-ddav43kd"
  register: instances_by_ids

- name: Find all instances based on the specified name_prefix
  community.general.ali_instance_info:
    name_prefix: "ecs_instance_"
  register: instances_by_name_prefix

- name: Find instances based on tags
  community.general.ali_instance_info:
    tags:
      Test: "add"
```

## [Return Values](ali_instance_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ids**  list / elements=string | List of ECS instance IDs  **Returned:** always  **Sample:** `["i-12345er", "i-3245fs"]` |
| **instances**  complex | List of ECS instances  **Returned:** always |
| **availability_zone**  string | The availability zone of the instance is in.  **Returned:** always  **Sample:** `"cn-beijing-a"` |
| **block_device_mappings**  complex | Any block device mapping entries for the instance.  **Returned:** always |
| **attach_time**  string | The time stamp when the attachment initiated.  **Returned:** always  **Sample:** `"2018-06-25T04:08:26Z"` |
| **delete_on_termination**  boolean | Indicates whether the volume is deleted on instance termination.  **Returned:** always  **Sample:** `true` |
| **device_name**  string | The device name exposed to the instance (for example, /dev/xvda).  **Returned:** always  **Sample:** `"/dev/xvda"` |
| **status**  string | The attachment state.  **Returned:** always  **Sample:** `"in_use"` |
| **volume_id**  string | The ID of the cloud disk.  **Returned:** always  **Sample:** `"d-2zei53pjsi117y6gf9t6"` |
| **cpu**  integer | The CPU core count of the instance.  **Returned:** always  **Sample:** `4` |
| **creation_time**  string | The time the instance was created.  **Returned:** always  **Sample:** `"2018-06-25T04:08Z"` |
| **description**  string | The instance description.  **Returned:** always  **Sample:** `"my ansible instance"` |
| **eip**  complex | The attribution of EIP associated with the instance.  **Returned:** always |
| **allocation_id**  string | The ID of the EIP.  **Returned:** always  **Sample:** `"eip-12345"` |
| **internet_charge_type**  string | The internet charge type of the EIP.  **Returned:** always  **Sample:** `"paybybandwidth"` |
| **ip_address**  string | EIP address.  **Returned:** always  **Sample:** `"42.10.2.2"` |
| **expired_time**  string | The time the instance will expire.  **Returned:** always  **Sample:** `"2099-12-31T15:59Z"` |
| **gpu**  complex | The attribution of instance GPU.  **Returned:** always |
| **amount**  integer | The count of the GPU.  **Returned:** always  **Sample:** `0` |
| **spec**  string | The specification of the GPU.  **Returned:** always  **Sample:** `""` |
| **host_name**  string | The host name of the instance.  **Returned:** always  **Sample:** `"iZ2zewaoZ"` |
| **id**  string | Alias of instance_id.  **Returned:** always  **Sample:** `"i-abc12345"` |
| **image_id**  string | The ID of the image used to launch the instance.  **Returned:** always  **Sample:** `"m-0011223344"` |
| **inner_ip_address**  string | The inner IPv4 address of the classic instance.  **Returned:** always  **Sample:** `"10.0.0.2"` |
| **instance_charge_type**  string | The instance charge type.  **Returned:** always  **Sample:** `"PostPaid"` |
| **instance_id**  string | ECS instance resource ID.  **Returned:** always  **Sample:** `"i-abc12345"` |
| **instance_name**  string | The name of the instance.  **Returned:** always  **Sample:** `"my-ecs"` |
| **instance_type**  string | The instance type of the running instance.  **Returned:** always  **Sample:** `"ecs.sn1ne.xlarge"` |
| **instance_type_family**  string | The instance type family of the instance belongs.  **Returned:** always  **Sample:** `"ecs.sn1ne"` |
| **internet_charge_type**  string | The billing method of the network bandwidth.  **Returned:** always  **Sample:** `"PayByBandwidth"` |
| **internet_max_bandwidth_in**  integer | Maximum incoming bandwidth from the internet network.  **Returned:** always  **Sample:** `200` |
| **internet_max_bandwidth_out**  integer | Maximum incoming bandwidth from the internet network.  **Returned:** always  **Sample:** `20` |
| **io_optimized**  boolean | Indicates whether the instance is optimized for EBS I/O.  **Returned:** always  **Sample:** `false` |
| **memory**  integer | Memory size of the instance.  **Returned:** always  **Sample:** `8192` |
| **network_interfaces**  complex | One or more network interfaces for the instance.  **Returned:** always |
| **mac_address**  string | The MAC address.  **Returned:** always  **Sample:** `"00:11:22:33:44:55"` |
| **network_interface_id**  string | The ID of the network interface.  **Returned:** always  **Sample:** `"eni-01234567"` |
| **primary_ip_address**  string | The primary IPv4 address of the network interface within the vswitch.  **Returned:** always  **Sample:** `"10.0.0.1"` |
| **osname**  string | The operation system name of the instance owned.  **Returned:** always  **Sample:** `"CentOS"` |
| **ostype**  string | The operation system type of the instance owned.  **Returned:** always  **Sample:** `"linux"` |
| **private_ip_address**  string | The IPv4 address of the network interface within the subnet.  **Returned:** always  **Sample:** `"10.0.0.1"` |
| **public_ip_address**  string | The public IPv4 address assigned to the instance or eip address  **Returned:** always  **Sample:** `"43.0.0.1"` |
| **resource_group_id**  string | The id of the resource group to which the instance belongs.  **Returned:** always  **Sample:** `"my-ecs-group"` |
| **security_groups**  list / elements=dictionary | One or more security groups for the instance.  **Returned:** always |
| **group_id**  string | The ID of the security group.  **Returned:** always  **Sample:** `"sg-0123456"` |
| **group_name**  string | The name of the security group.  **Returned:** always  **Sample:** `"my-security-group"` |
| **status**  string | The current status of the instance.  **Returned:** always  **Sample:** `"running"` |
| **tags**  dictionary | Any tags assigned to the instance.  **Returned:** always |
| **vpc_id**  string | The ID of the VPC the instance is in.  **Returned:** always  **Sample:** `"vpc-0011223344"` |
| **vswitch_id**  string | The ID of the vswitch in which the instance is running.  **Returned:** always  **Sample:** `"vsw-dew00abcdef"` |

### Authors

- He Guimin (@xiaozhu36)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
