---
collection: ansible
version: "6"
title: "community.aws.ec2_lc module – Create or delete AWS Autoscaling Launch Configurations"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/ec2_lc_module.html
fetched_at: 2026-07-27T17:04:01+00:00
---
# community.aws.ec2_lc module – Create or delete AWS Autoscaling Launch Configurations

> **Note:**
>
> This module is part of the [community.aws collection](https://galaxy.ansible.com/community/aws) (version 3.6.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.aws`.
> You need further requirements to be able to use this module,
> see [Requirements](ec2_lc_module.md#ansible-collections-community-aws-ec2-lc-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.ec2_lc`.

New in community.aws 1.0.0

- [Synopsis](ec2_lc_module.md#synopsis)
- [Requirements](ec2_lc_module.md#requirements)
- [Parameters](ec2_lc_module.md#parameters)
- [Notes](ec2_lc_module.md#notes)
- [Examples](ec2_lc_module.md#examples)
- [Return Values](ec2_lc_module.md#return-values)

## [Synopsis](ec2_lc_module.md#id1)

- Can create or delete AWS Autoscaling Configurations.
- Works with the ec2_asg module to manage Autoscaling Groups.

## [Requirements](ec2_lc_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_lc_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **assign_public_ip**  boolean | Used for Auto Scaling groups that launch instances into an Amazon Virtual Private Cloud. Specifies whether to assign a public IP address to each instance launched in a Amazon VPC.  Choices:   - `false` - `true` |
| **associate_public_ip_address**  boolean | The *associate_public_ip_address* option does nothing and will be removed after 2022-06-01  Choices:   - `false` - `true` |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **classic_link_vpc_id**  string | Id of ClassicLink enabled VPC |
| **classic_link_vpc_security_groups**  list / elements=string | A list of security group IDs with which to associate the ClassicLink VPC instances. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ebs_optimized**  boolean | Specifies whether the instance is optimized for EBS I/O (true) or not (false).  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **image_id**  string | The AMI unique identifier to be used for the group. |
| **instance_id**  string | The Id of a running instance to use as a basis for a launch configuration. Can be used in place of *image_id* and *instance_type*. |
| **instance_monitoring**  boolean | Specifies whether instances are launched with detailed monitoring.  Choices:   - `false` ← (default) - `true` |
| **instance_profile_name**  string | The name or the Amazon Resource Name (ARN) of the instance profile associated with the IAM role for the instances. |
| **instance_type**  string | Instance type to use for the instance.  Required when creating a new Launch Configuration. |
| **kernel_id**  string | Kernel id for the EC2 instance. |
| **key_name**  string | The SSH key name to be used for access to managed instances. |
| **name**  string / required | Unique name for configuration. |
| **placement_tenancy**  string | Determines whether the instance runs on single-tenant hardware or not.  When not set AWS will default to `default`.  Choices:   - `"default"` - `"dedicated"` |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **ramdisk_id**  string | A RAM disk id for the instances. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_groups**  list / elements=string | A list of security groups to apply to the instances. Since version 2.4 you can specify either security group names or IDs or a mix. Previous to 2.4, for VPC instances, specify security group IDs and for EC2-Classic, specify either security group names or IDs. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **spot_price**  float | The spot price you are bidding. Only applies for an autoscaling group with spot instances. |
| **state**  string | Register or deregister the instance.  Choices:   - `"present"` ← (default) - `"absent"` |
| **user_data**  string | Opaque blob of data which is made available to the ec2 instance. Mutually exclusive with *user_data_path*. |
| **user_data_path**  path | Path to the file that contains userdata for the ec2 instances. Mutually exclusive with *user_data*. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **volumes**  list / elements=dictionary | A list dictionaries defining the volumes to create.  For any volume, a volume size less than 1 will be interpreted as a request not to create the volume. |
| **delete_on_termination**  boolean | Whether the volume should be automatically deleted when the instance is terminated.  Choices:   - `false` ← (default) - `true` |
| **device_name**  string / required | The name for the volume (For example `/dev/sda`). |
| **encrypted**  boolean | Whether the volume should be encrypted using the ‘aws/ebs’ KMS CMK.  Choices:   - `false` ← (default) - `true` |
| **ephemeral**  string | Whether the volume should be ephemeral.  Data on ephemeral volumes is lost when the instance is stopped.  Mutually exclusive with the *snapshot* parameter. |
| **iops**  integer | The number of IOPS per second to provision for the volume.  Required when *volume_type=io1*. |
| **no_device**  boolean | When *no_device=true* the device will not be created.  Choices:   - `false` - `true` |
| **snapshot**  string | The ID of an EBS snapshot to copy when creating the volume.  Mutually exclusive with the *ephemeral* parameter. |
| **throughput**  integer  added in community.aws 3.1.0 | The throughput to provision for a gp3 volume.  Valid Range is a minimum value of 125 and a maximum value of 1000. |
| **volume_size**  integer | The size of the volume (in GiB).  Required unless one of *ephemeral*, *snapshot* or *no_device* is set. |
| **volume_type**  string | The type of volume to create.  See <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html> for more information on the available volume types. |
| **vpc_id**  string | VPC ID, used when resolving security group names to IDs. |

## [Notes](ec2_lc_module.md#id4)

> **Note:**
>
> - Amazon ASG Autoscaling Launch Configurations are immutable once created, so modifying the configuration after it is changed will not modify the launch configuration on AWS. You must create a new config and assign it to the ASG instead.
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_lc_module.md#id5)

```yaml+jinja
- name: create a launch configuration with an encrypted volume
  community.aws.ec2_lc:
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
  community.aws.ec2_lc:
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
  community.aws.ec2_lc:
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
          encrypted: no

  - name: Create launch configuration
    community.aws.ec2_lc:
      name: lc1
      image_id: ami-xxxx
      assign_public_ip: yes
      instance_type: t2.medium
      key_name: my-key
      security_groups: "['sg-xxxx']"
      volumes: "{{ volumes }}"
    register: lc_info
```

## [Return Values](ec2_lc_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **arn**  string | The Amazon Resource Name of the launch configuration.  Returned: when *state=present*  Sample: `"arn:aws:autoscaling:us-east-1:148830907657:launchConfiguration:888d9b58-d93a-40c4-90cf-759197a2621a:launchConfigurationName/launch_config_name"` |
| **changed**  boolean | Whether the state of the launch configuration has changed.  Returned: always  Sample: `false` |
| **created_time**  string | The creation date and time for the launch configuration.  Returned: when *state=present*  Sample: `"2017-11-03 23:46:44.841000"` |
| **image_id**  string | The ID of the Amazon Machine Image used by the launch configuration.  Returned: when *state=present*  Sample: `"ami-9be6f38c"` |
| **instance_type**  string | The instance type for the instances.  Returned: when *state=present*  Sample: `"t1.micro"` |
| **name**  string | The name of the launch configuration.  Returned: when *state=present*  Sample: `"launch_config_name"` |
| **result**  complex | The specification details for the launch configuration.  Returned: when *state=present* |
| **associate_public_ip_address**  boolean | (EC2-VPC) Indicates whether to assign a public IP address to each instance.  Returned: when *state=present*  Sample: `false` |
| **block_device_mappings**  complex | A block device mapping, which specifies the block devices.  Returned: when *state=present* |
| **device_name**  string | The device name exposed to the EC2 instance (for example, /dev/sdh or xvdh).  Returned: when *state=present*  Sample: `"/dev/sda1"` |
| **ebs**  complex | The information about the Amazon EBS volume.  Returned: when *state=present* |
| **snapshot_id**  string | The ID of the snapshot.  Returned: when *state=present* |
| **volume_size**  string | The volume size, in GiB.  Returned: when *state=present*  Sample: `"100"` |
| **virtual_name**  string | The name of the virtual device (for example, ephemeral0).  Returned: when *state=present*  Sample: `"ephemeral0"` |
| **classic_link_vpc_id**  string | The ID of a ClassicLink-enabled VPC to link your EC2-Classic instances to.  Returned: when *state=present* |
| **classic_link_vpc_security_groups**  list / elements=string | The IDs of one or more security groups for the VPC specified in ClassicLinkVPCId.  Returned: when *state=present*  Sample: `[]` |
| **created_time**  string | The creation date and time for the launch configuration.  Returned: when *state=present*  Sample: `"2017-11-03 23:46:44.841000"` |
| **delete_on_termination**  boolean | Indicates whether the volume is deleted on instance termination.  Returned: when *state=present*  Sample: `true` |
| **ebs_optimized**  boolean | Indicates whether the instance is optimized for EBS I/O (true) or not (false).  Returned: when *state=present*  Sample: `false` |
| **image_id**  string | The ID of the Amazon Machine Image used by the launch configuration.  Returned: when *state=present*  Sample: `"ami-9be6f38c"` |
| **instance_monitoring**  boolean | Indicates whether instances in this group are launched with detailed (true) or basic (false) monitoring.  Returned: when *state=present*  Sample: `true` |
| **instance_profile_name**  string | The name or Amazon Resource Name (ARN) of the instance profile associated with the IAM role for the instance.  Returned: when *state=present* |
| **instance_type**  string | The instance type for the instances.  Returned: when *state=present*  Sample: `"t1.micro"` |
| **iops**  integer | The number of I/O operations per second (IOPS) to provision for the volume.  Returned: when *state=present* |
| **kernel_id**  string | The ID of the kernel associated with the AMI.  Returned: when *state=present*  Sample: `""` |
| **key_name**  string | The name of the key pair.  Returned: when *state=present*  Sample: `"testkey"` |
| **launch_configuration_arn**  string | The Amazon Resource Name (ARN) of the launch configuration.  Returned: when *state=present*  Sample: `"arn:aws:autoscaling:us-east-1:148830907657:launchConfiguration:888d9b58-d93a-40c4-90cf-759197a2621a:launchConfigurationName/launch_config_name"` |
| **member**  string | Returned: when *state=present*  Sample: `"\n      "` |
| **name**  string | The name of the launch configuration.  Returned: when *state=present*  Sample: `"launch_config_name"` |
| **PlacementTenancy**  string | The tenancy of the instances, either default or dedicated.  Returned: when *state=present*  Sample: `"default"` |
| **ramdisk_id**  string | The ID of the RAM disk associated with the AMI.  Returned: when *state=present*  Sample: `""` |
| **security_groups**  list / elements=string | The security groups to associate with the instances.  Returned: when *state=present*  Sample: `["sg-5e27db2f"]` |
| **spot_price**  float | The price to bid when launching Spot Instances.  Returned: when *state=present* |
| **use_block_device_types**  boolean | Indicates whether to suppress a device mapping.  Returned: when *state=present*  Sample: `false` |
| **user_data**  string | The user data available to the instances.  Returned: when *state=present*  Sample: `""` |
| **volume_type**  string | The volume type (one of standard, io1, gp2).  Returned: when *state=present*  Sample: `"io1"` |
| **security_groups**  list / elements=string | The security groups to associate with the instances.  Returned: when *state=present*  Sample: `["sg-5e27db2f"]` |

### Authors

- Gareth Rushgrove (@garethr)
- Willem van Ketwich (@wilvk)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
