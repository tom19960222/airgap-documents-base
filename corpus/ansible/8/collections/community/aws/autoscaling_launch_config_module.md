---
collection: ansible
version: "8"
title: "community.aws.autoscaling_launch_config module – Create or delete AWS Autoscaling Launch Configurations"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/autoscaling_launch_config_module.html
fetched_at: 2026-07-28T01:40:10+00:00
---
# community.aws.autoscaling_launch_config module – Create or delete AWS Autoscaling Launch Configurations

> **Note:**
>
> This module is part of the [community.aws collection](https://galaxy.ansible.com/ui/repo/published/community/aws/) (version 6.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.aws`.
> You need further requirements to be able to use this module,
> see [Requirements](autoscaling_launch_config_module.md#ansible-collections-community-aws-autoscaling-launch-config-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.autoscaling_launch_config`.

New in community.aws 1.0.0

- [Synopsis](autoscaling_launch_config_module.md#synopsis)
- [Requirements](autoscaling_launch_config_module.md#requirements)
- [Parameters](autoscaling_launch_config_module.md#parameters)
- [Notes](autoscaling_launch_config_module.md#notes)
- [Examples](autoscaling_launch_config_module.md#examples)
- [Return Values](autoscaling_launch_config_module.md#return-values)

## [Synopsis](autoscaling_launch_config_module.md#id1)

- Can create or delete AWS Autoscaling Configurations.
- Works with the [community.aws.autoscaling_group](autoscaling_group_module.md#ansible-collections-community-aws-autoscaling-group-module) module to manage Autoscaling Groups.
- Prior to release 5.0.0 this module was called `community.aws.ec2_lc`. The usage did not change.

Aliases: ec2_lc

## [Requirements](autoscaling_launch_config_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](autoscaling_launch_config_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **assign_public_ip**  boolean | Used for Auto Scaling groups that launch instances into an Amazon Virtual Private Cloud. Specifies whether to assign a public IP address to each instance launched in a Amazon VPC.  **Choices:**   - `false` - `true` |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **classic_link_vpc_id**  string | Id of ClassicLink enabled VPC |
| **classic_link_vpc_security_groups**  list / elements=string | A list of security group IDs with which to associate the ClassicLink VPC instances. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **ebs_optimized**  boolean | Specifies whether the instance is optimized for EBS I/O (true) or not (false).  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **image_id**  string | The AMI unique identifier to be used for the group. |
| **instance_id**  string | The Id of a running instance to use as a basis for a launch configuration. Can be used in place of *image_id* and *instance_type*. |
| **instance_monitoring**  boolean | Specifies whether instances are launched with detailed monitoring.  **Choices:**   - `false` ← (default) - `true` |
| **instance_profile_name**  string | The name or the Amazon Resource Name (ARN) of the instance profile associated with the IAM role for the instances. |
| **instance_type**  string | Instance type to use for the instance.  Required when creating a new Launch Configuration. |
| **kernel_id**  string | Kernel id for the EC2 instance. |
| **key_name**  string | The SSH key name to be used for access to managed instances. |
| **name**  string / required | Unique name for configuration. |
| **placement_tenancy**  string | Determines whether the instance runs on single-tenant hardware or not.  When not set AWS will default to `default`.  **Choices:**   - `"default"` - `"dedicated"` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **ramdisk_id**  string | A RAM disk id for the instances. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **security_groups**  list / elements=string | A list of security groups to apply to the instances.  You can specify either security group names or IDs or a mix.  **Default:** `[]` |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **spot_price**  float | The spot price you are bidding. Only applies for an autoscaling group with spot instances. |
| **state**  string | Register or deregister the instance.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **user_data**  string | Opaque blob of data which is made available to the ec2 instance. Mutually exclusive with *user_data_path*. |
| **user_data_path**  path | Path to the file that contains userdata for the ec2 instances. Mutually exclusive with *user_data*. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **volumes**  list / elements=dictionary | A list dictionaries defining the volumes to create.  For any volume, a volume size less than `1` will be interpreted as a request not to create the volume. |
| **delete_on_termination**  boolean | Whether the volume should be automatically deleted when the instance is terminated.  **Choices:**   - `false` ← (default) - `true` |
| **device_name**  string / required | The name for the volume (For example `/dev/sda`). |
| **encrypted**  boolean | Whether the volume should be encrypted using the ‘aws/ebs’ KMS CMK.  **Choices:**   - `false` ← (default) - `true` |
| **ephemeral**  string | Whether the volume should be ephemeral.  Data on ephemeral volumes is lost when the instance is stopped.  Mutually exclusive with the *snapshot* parameter. |
| **iops**  integer | The number of IOPS per second to provision for the volume.  Required when *volume_type=io1*. |
| **no_device**  boolean | When *no_device=true* the device will not be created.  **Choices:**   - `false` - `true` |
| **snapshot**  string | The ID of an EBS snapshot to copy when creating the volume.  Mutually exclusive with the *ephemeral* parameter. |
| **throughput**  integer  *added in community.aws 3.1.0* | The throughput to provision for a gp3 volume.  Valid Range is a minimum value of 125 and a maximum value of 1000. |
| **volume_size**  integer | The size of the volume (in GiB).  Required unless one of *ephemeral*, *snapshot* or *no_device* is set. |
| **volume_type**  string | The type of volume to create.  See <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html> for more information on the available volume types. |
| **vpc_id**  string | VPC ID, used when resolving security group names to IDs. |

## [Notes](autoscaling_launch_config_module.md#id4)

> **Note:**
>
> - Amazon ASG Autoscaling Launch Configurations are immutable once created, so modifying the configuration after it is changed will not modify the launch configuration on AWS. You must create a new config and assign it to the ASG instead.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](autoscaling_launch_config_module.md#id5)

```yaml+jinja
- name: create a launch configuration with an encrypted volume
  community.aws.autoscaling_launch_config:
    name: special
    image_id: ami-XXX
    key_name: default
    security_groups: ['group', 'group2' ]
    instance_type: t1.micro
    volumes:
    - device_name: /dev/sda1
      volume_size: 100
      volume_type: io1
      iops: 3000
      delete_on_termination: true
      encrypted: true
    - device_name: /dev/sdb
      ephemeral: ephemeral0

- name: create a launch configuration using a running instance id as a basis
  community.aws.autoscaling_launch_config:
    name: special
    instance_id: i-00a48b207ec59e948
    key_name: default
    security_groups: ['launch-wizard-2' ]
    volumes:
    - device_name: /dev/sda1
      volume_size: 120
      volume_type: io1
      iops: 3000
      delete_on_termination: true

- name: create a launch configuration to omit the /dev/sdf EBS device that is included in the AMI image
  community.aws.autoscaling_launch_config:
    name: special
    image_id: ami-XXX
    key_name: default
    security_groups: ['group', 'group2' ]
    instance_type: t1.micro
    volumes:
    - device_name: /dev/sdf
      no_device: true

- name: Use EBS snapshot ID for volume
  block:
  - name: Set Volume Facts
    ansible.builtin.set_fact:
      volumes:
      - device_name: /dev/sda1
        volume_size: 20
        ebs:
          snapshot: snap-XXXX
          volume_type: gp2
          delete_on_termination: true
          encrypted: false

  - name: Create launch configuration
    community.aws.autoscaling_launch_config:
      name: lc1
      image_id: ami-xxxx
      assign_public_ip: true
      instance_type: t2.medium
      key_name: my-key
      security_groups: "['sg-xxxx']"
      volumes: "{{ volumes }}"
    register: lc_info
```

## [Return Values](autoscaling_launch_config_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **arn**  string | The Amazon Resource Name of the launch configuration.  **Returned:** when *state=present*  **Sample:** `"arn:aws:autoscaling:us-east-1:123456789012:launchConfiguration:888d9b58-d93a-40c4-90cf-759197a2621a:launchConfigurationName/launch_config_name"` |
| **changed**  boolean | Whether the state of the launch configuration has changed.  **Returned:** always  **Sample:** `false` |
| **created_time**  string | The creation date and time for the launch configuration.  **Returned:** when *state=present*  **Sample:** `"2017-11-03 23:46:44.841000"` |
| **image_id**  string | The ID of the Amazon Machine Image used by the launch configuration.  **Returned:** when *state=present*  **Sample:** `"ami-9be6f38c"` |
| **instance_type**  string | The instance type for the instances.  **Returned:** when *state=present*  **Sample:** `"t1.micro"` |
| **name**  string | The name of the launch configuration.  **Returned:** when *state=present*  **Sample:** `"launch_config_name"` |
| **result**  complex | The specification details for the launch configuration.  **Returned:** when *state=present* |
| **associate_public_ip_address**  boolean | (EC2-VPC) Indicates whether to assign a public IP address to each instance.  **Returned:** when *state=present*  **Sample:** `false` |
| **block_device_mappings**  complex | A block device mapping, which specifies the block devices.  **Returned:** when *state=present* |
| **device_name**  string | The device name exposed to the EC2 instance (for example, /dev/sdh or xvdh).  **Returned:** when *state=present*  **Sample:** `"/dev/sda1"` |
| **ebs**  complex | The information about the Amazon EBS volume.  **Returned:** when *state=present* |
| **snapshot_id**  string | The ID of the snapshot.  **Returned:** when *state=present* |
| **volume_size**  string | The volume size, in GiB.  **Returned:** when *state=present*  **Sample:** `"100"` |
| **virtual_name**  string | The name of the virtual device (for example, ephemeral0).  **Returned:** when *state=present*  **Sample:** `"ephemeral0"` |
| **classic_link_vpc_id**  string | The ID of a ClassicLink-enabled VPC to link your EC2-Classic instances to.  **Returned:** when *state=present* |
| **classic_link_vpc_security_groups**  list / elements=string | The IDs of one or more security groups for the VPC specified in ClassicLinkVPCId.  **Returned:** when *state=present*  **Sample:** `[]` |
| **created_time**  string | The creation date and time for the launch configuration.  **Returned:** when *state=present*  **Sample:** `"2017-11-03 23:46:44.841000"` |
| **delete_on_termination**  boolean | Indicates whether the volume is deleted on instance termination.  **Returned:** when *state=present*  **Sample:** `true` |
| **ebs_optimized**  boolean | Indicates whether the instance is optimized for EBS I/O `true` or not `false`.  **Returned:** when *state=present*  **Sample:** `false` |
| **image_id**  string | The ID of the Amazon Machine Image used by the launch configuration.  **Returned:** when *state=present*  **Sample:** `"ami-9be6f38c"` |
| **instance_monitoring**  boolean | Indicates whether instances in this group are launched with detailed `true` or basic `false` monitoring.  **Returned:** when *state=present*  **Sample:** `true` |
| **instance_profile_name**  string | The name or Amazon Resource Name (ARN) of the instance profile associated with the IAM role for the instance.  **Returned:** when *state=present* |
| **instance_type**  string | The instance type for the instances.  **Returned:** when *state=present*  **Sample:** `"t1.micro"` |
| **iops**  integer | The number of I/O operations per second (IOPS) to provision for the volume.  **Returned:** when *state=present* |
| **kernel_id**  string | The ID of the kernel associated with the AMI.  **Returned:** when *state=present*  **Sample:** `""` |
| **key_name**  string | The name of the key pair.  **Returned:** when *state=present*  **Sample:** `"testkey"` |
| **launch_configuration_arn**  string | The Amazon Resource Name (ARN) of the launch configuration.  **Returned:** when *state=present*  **Sample:** `"arn:aws:autoscaling:us-east-1:123456789012:launchConfiguration:888d9b58-d93a-40c4-90cf-759197a2621a:launchConfigurationName/launch_config_name"` |
| **member**  string | **Returned:** when *state=present*  **Sample:** `"\n      "` |
| **name**  string | The name of the launch configuration.  **Returned:** when *state=present*  **Sample:** `"launch_config_name"` |
| **PlacementTenancy**  string | The tenancy of the instances, either default or dedicated.  **Returned:** when *state=present*  **Sample:** `"default"` |
| **ramdisk_id**  string | The ID of the RAM disk associated with the AMI.  **Returned:** when *state=present*  **Sample:** `""` |
| **security_groups**  list / elements=string | The security groups to associate with the instances.  **Returned:** when *state=present*  **Sample:** `["sg-5e27db2f"]` |
| **spot_price**  float | The price to bid when launching Spot Instances.  **Returned:** when *state=present* |
| **use_block_device_types**  boolean | Indicates whether to suppress a device mapping.  **Returned:** when *state=present*  **Sample:** `false` |
| **user_data**  string | The user data available to the instances.  **Returned:** when *state=present*  **Sample:** `""` |
| **volume_type**  string | The volume type (one of standard, io1, gp2).  **Returned:** when *state=present*  **Sample:** `"io1"` |
| **security_groups**  list / elements=string | The security groups to associate with the instances.  **Returned:** when *state=present*  **Sample:** `["sg-5e27db2f"]` |

### Authors

- Gareth Rushgrove (@garethr)
- Willem van Ketwich (@wilvk)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
