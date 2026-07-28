---
collection: ansible
version: "8"
title: "community.general.ali_instance module – Create, Start, Stop, Restart or Terminate an Instance in ECS; Add or Remove Instance to/from a Security Group"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/ali_instance_module.html
fetched_at: 2026-07-28T01:44:36+00:00
---
# community.general.ali_instance module – Create, Start, Stop, Restart or Terminate an Instance in ECS; Add or Remove Instance to/from a Security Group

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
> see [Requirements](ali_instance_module.md#ansible-collections-community-general-ali-instance-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.ali_instance`.

- [Synopsis](ali_instance_module.md#synopsis)
- [Requirements](ali_instance_module.md#requirements)
- [Parameters](ali_instance_module.md#parameters)
- [Attributes](ali_instance_module.md#attributes)
- [Notes](ali_instance_module.md#notes)
- [Examples](ali_instance_module.md#examples)
- [Return Values](ali_instance_module.md#return-values)

## [Synopsis](ali_instance_module.md#id1)

- Create, start, stop, restart, modify or terminate ecs instances.
- Add or remove ecs instances to/from security group.

Aliases: cloud.alicloud.ali_instance

## [Requirements](ali_instance_module.md#id2)

The below requirements are needed on the host that executes this module.

- footmark >= 1.19.0
- python >= 3.6

## [Parameters](ali_instance_module.md#id3)

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
| **allocate_public_ip**  aliases: assign_public_ip  boolean | Whether allocate a public ip for the new instance.  **Choices:**   - `false` ← (default) - `true` |
| **auto_renew**  boolean | Whether automate renew the charge of the instance.  **Choices:**   - `false` ← (default) - `true` |
| **auto_renew_period**  integer | The duration of the automatic renew the charge of the instance. Required when `auto_renew=true`.  **Choices:**   - `1` - `2` - `3` - `6` - `12` |
| **availability_zone**  aliases: alicloud_zone, zone_id  string | Aliyun availability zone ID in which to launch the instance. If it is not specified, it will be allocated by system automatically. |
| **count**  integer | The number of the new instance. An integer value which indicates how many instances that match `count_tag` should be running. Instances are either created or terminated based on this value.  **Default:** `1` |
| **count_tag**  string | `count` determines how many instances based on a specific tag criteria should be present. This can be expressed in multiple ways and is shown in the EXAMPLES section. The specified count_tag must already exist or be passed in as the `tags` option. If it is not specified, it will be replaced by `instance_name`. |
| **description**  string | The description of ECS instance, which is a string of 2 to 256 characters. It cannot begin with <http://> or [https://](ali_instance_module.md). |
| **dry_run**  boolean  *added in community.general 0.2.0* | Specifies whether to send a dry-run request.  If `dry_run=true`, Only a dry-run request is sent and no instance is created. The system checks whether the required parameters are set, and validates the request format, service permissions, and available ECS instances. If the validation fails, the corresponding error code is returned. If the validation succeeds, the DryRunOperation error code is returned.  If `dry_run=false`, A request is sent. If the validation succeeds, the instance is created.  **Choices:**   - `false` ← (default) - `true` |
| **ecs_role_name**  aliases: role_name  string | The RAM Role Name attached on a ECS instance for API operations. You can retrieve this from the ‘Access Control’ section of the Alibaba Cloud console.  If you’re running Ansible from an ECS instance with RAM Instance using RAM Role, Ansible will just access the metadata <http://100.100.100.200/latest/meta-data/ram/security-credentials/%3Cecs_role_name%3E> to obtain the STS credential. This is a preferred approach over any other when running in ECS as you can avoid hard coding credentials. Instead these are leased on-the-fly by Ansible which reduces the chance of leakage. |
| **force**  boolean | Whether the current operation needs to be execute forcibly.  **Choices:**   - `false` ← (default) - `true` |
| **host_name**  string | Instance host name. Ordered hostname is not supported. |
| **image_id**  aliases: image  string | Image ID used to launch instances. Required when `state=present` and creating new ECS instances. |
| **include_data_disks**  boolean  *added in community.general 0.2.0* | Whether to change instance disks charge type when changing instance charge type.  **Choices:**   - `false` - `true` ← (default) |
| **instance_charge_type**  string | The charge type of the instance.  **Choices:**   - `"PrePaid"` - `"PostPaid"` ← (default) |
| **instance_ids**  list / elements=string | A list of instance ids. It is required when need to operate existing instances. If it is specified, `count` will lose efficacy. |
| **instance_name**  aliases: name  string | The name of ECS instance, which is a string of 2 to 128 Chinese or English characters. It must begin with an uppercase/lowercase letter or a Chinese character and can contain numerals, “.”, “_” or “-”. It cannot begin with <http://> or [https://](ali_instance_module.md). |
| **instance_type**  aliases: type  string | Instance type used to launch instances. Required when `state=present` and creating new ECS instances. |
| **internet_charge_type**  string | Internet charge type of ECS instance.  **Choices:**   - `"PayByBandwidth"` ← (default) - `"PayByTraffic"` |
| **key_name**  aliases: keypair  string | The name of key pair which is used to access ECS instance in SSH. |
| **max_bandwidth_in**  integer | Maximum incoming bandwidth from the public network, measured in Mbps (Megabits per second).  **Default:** `200` |
| **max_bandwidth_out**  integer | Maximum outgoing bandwidth to the public network, measured in Mbps (Megabits per second). Required when `allocate_public_ip=true`. Ignored when `allocate_public_ip=false`.  **Default:** `0` |
| **password**  string | The password to login instance. After rebooting instances, modified password will take effect. |
| **period**  integer | The charge duration of the instance, in months. Required when `instance_charge_type=PrePaid`.  The valid value are [1-9, 12, 24, 36].  **Default:** `1` |
| **period_unit**  string  *added in community.general 0.2.0* | The duration unit that you will buy the resource. It is valid when `instance_charge_type=PrePaid`.  **Choices:**   - `"Month"` ← (default) - `"Week"` |
| **profile**  string | This is the Alicloud profile name as set in the shared credentials file. It can also be sourced from the `ALICLOUD_PROFILE` environment variable. |
| **purge_tags**  boolean  *added in community.general 0.2.0* | Delete any tags not specified in the task that are on the instance. If True, it means you have to specify all the desired tags on each task affecting an instance.  **Choices:**   - `false` ← (default) - `true` |
| **ram_role_name**  string  *added in community.general 0.2.0* | The name of the instance RAM role. |
| **security_groups**  aliases: group_ids  list / elements=string | A list of security group IDs. |
| **shared_credentials_file**  string | This is the path to the shared credentials file. It can also be sourced from the `ALICLOUD_SHARED_CREDENTIALS_FILE` environment variable.  If this is not set and a profile is specified, ~/.aliyun/config.json will be used. |
| **spot_price_limit**  float  *added in community.general 0.2.0* | The maximum hourly price for the preemptible instance. This parameter supports a maximum of three decimal places and takes effect when the SpotStrategy parameter is set to SpotWithPriceLimit. |
| **spot_strategy**  string  *added in community.general 0.2.0* | The bidding mode of the pay-as-you-go instance. This parameter is valid when InstanceChargeType is set to PostPaid.  **Choices:**   - `"NoSpot"` ← (default) - `"SpotWithPriceLimit"` - `"SpotAsPriceGo"` |
| **state**  string | The state of the instance after operating.  **Choices:**   - `"present"` ← (default) - `"running"` - `"stopped"` - `"restarted"` - `"absent"` |
| **system_disk_category**  string | Category of the system disk.  **Choices:**   - `"cloud_efficiency"` ← (default) - `"cloud_ssd"` |
| **system_disk_description**  string | Description of the system disk. |
| **system_disk_name**  string | Name of the system disk. |
| **system_disk_size**  integer | Size of the system disk, in GB. The valid values are 40~500.  **Default:** `40` |
| **tags**  aliases: instance_tags  dictionary  *added in community.general 0.2.0* | A hash/dictionaries of instance tags, to add to the new instance or for starting/stopping instance by tag. `{"key":"value"}` |
| **unique_suffix**  boolean  *added in community.general 0.2.0* | Specifies whether to add sequential suffixes to the host_name. The sequential suffix ranges from 001 to 999.  **Choices:**   - `false` ← (default) - `true` |
| **user_data**  string | User-defined data to customize the startup behaviors of an ECS instance and to pass data into an ECS instance. It only will take effect when launching the new ECS instances. |
| **vswitch_id**  aliases: subnet_id  string | The subnet ID in which to launch the instances (VPC). |

## [Attributes](ali_instance_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](ali_instance_module.md#id5)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `ALICLOUD_ACCESS_KEY` or `ALICLOUD_ACCESS_KEY_ID`, `ALICLOUD_SECRET_KEY` or `ALICLOUD_SECRET_ACCESS_KEY`, `ALICLOUD_REGION` or `ALICLOUD_REGION_ID`, `ALICLOUD_SECURITY_TOKEN`, `ALICLOUD_ECS_ROLE_NAME`, `ALICLOUD_SHARED_CREDENTIALS_FILE`, `ALICLOUD_PROFILE`, `ALICLOUD_ASSUME_ROLE_ARN`, `ALICLOUD_ASSUME_ROLE_SESSION_NAME`, `ALICLOUD_ASSUME_ROLE_SESSION_EXPIRATION`,
> - `ALICLOUD_REGION` or `ALICLOUD_REGION_ID` can be typically be used to specify the ALICLOUD region, when required, but this can also be configured in the footmark config file

## [Examples](ali_instance_module.md#id6)

```yaml+jinja
# basic provisioning example vpc network
- name: Basic provisioning example
  hosts: localhost
  vars:
    alicloud_access_key: <your-alicloud-access-key-id>
    alicloud_secret_key: <your-alicloud-access-secret-key>
    alicloud_region: cn-beijing
    image: ubuntu1404_64_40G_cloudinit_20160727.raw
    instance_type: ecs.n4.small
    vswitch_id: vsw-abcd1234
    assign_public_ip: true
    max_bandwidth_out: 10
    host_name: myhost
    password: mypassword
    system_disk_category: cloud_efficiency
    system_disk_size: 100
    internet_charge_type: PayByBandwidth
    security_groups: ["sg-f2rwnfh23r"]

    instance_ids: ["i-abcd12346", "i-abcd12345"]
    force: true

  tasks:
    - name: Launch ECS instance in VPC network
      community.general.ali_instance:
        alicloud_access_key: '{{ alicloud_access_key }}'
        alicloud_secret_key: '{{ alicloud_secret_key }}'
        alicloud_region: '{{ alicloud_region }}'
        image: '{{ image }}'
        system_disk_category: '{{ system_disk_category }}'
        system_disk_size: '{{ system_disk_size }}'
        instance_type: '{{ instance_type }}'
        vswitch_id: '{{ vswitch_id }}'
        assign_public_ip: '{{ assign_public_ip }}'
        internet_charge_type: '{{ internet_charge_type }}'
        max_bandwidth_out: '{{ max_bandwidth_out }}'
        tags:
            Name: created_one
        host_name: '{{ host_name }}'
        password: '{{ password }}'

    - name: With count and count_tag to create a number of instances
      community.general.ali_instance:
        alicloud_access_key: '{{ alicloud_access_key }}'
        alicloud_secret_key: '{{ alicloud_secret_key }}'
        alicloud_region: '{{ alicloud_region }}'
        image: '{{ image }}'
        system_disk_category: '{{ system_disk_category }}'
        system_disk_size: '{{ system_disk_size }}'
        instance_type: '{{ instance_type }}'
        assign_public_ip: '{{ assign_public_ip }}'
        security_groups: '{{ security_groups }}'
        internet_charge_type: '{{ internet_charge_type }}'
        max_bandwidth_out: '{{ max_bandwidth_out }}'
        tags:
            Name: created_one
            Version: 0.1
        count: 2
        count_tag:
            Name: created_one
        host_name: '{{ host_name }}'
        password: '{{ password }}'

    - name: Start instance
      community.general.ali_instance:
        alicloud_access_key: '{{ alicloud_access_key }}'
        alicloud_secret_key: '{{ alicloud_secret_key }}'
        alicloud_region: '{{ alicloud_region }}'
        instance_ids: '{{ instance_ids }}'
        state: 'running'

    - name: Reboot instance forcibly
      ecs:
        alicloud_access_key: '{{ alicloud_access_key }}'
        alicloud_secret_key: '{{ alicloud_secret_key }}'
        alicloud_region: '{{ alicloud_region }}'
        instance_ids: '{{ instance_ids }}'
        state: 'restarted'
        force: '{{ force }}'

    - name: Add instances to an security group
      ecs:
        alicloud_access_key: '{{ alicloud_access_key }}'
        alicloud_secret_key: '{{ alicloud_secret_key }}'
        alicloud_region: '{{ alicloud_region }}'
        instance_ids: '{{ instance_ids }}'
        security_groups: '{{ security_groups }}'
```

## [Return Values](ali_instance_module.md#id7)

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
| **spot_price_limit**  float | The maximum hourly price for the preemptible instance.  **Returned:** always  **Sample:** `0.97` |
| **spot_strategy**  string | The bidding mode of the pay-as-you-go instance.  **Returned:** always  **Sample:** `"NoSpot"` |
| **status**  string | The current status of the instance.  **Returned:** always  **Sample:** `"running"` |
| **tags**  dictionary | Any tags assigned to the instance.  **Returned:** always |
| **user_data**  dictionary | User-defined data.  **Returned:** always |
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
