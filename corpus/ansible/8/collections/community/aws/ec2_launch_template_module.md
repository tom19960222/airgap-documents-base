---
collection: ansible
version: "8"
title: "community.aws.ec2_launch_template module – Manage EC2 launch templates"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/ec2_launch_template_module.html
fetched_at: 2026-07-28T01:40:41+00:00
---
# community.aws.ec2_launch_template module – Manage EC2 launch templates

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
> see [Requirements](ec2_launch_template_module.md#ansible-collections-community-aws-ec2-launch-template-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.ec2_launch_template`.

New in community.aws 1.0.0

- [Synopsis](ec2_launch_template_module.md#synopsis)
- [Requirements](ec2_launch_template_module.md#requirements)
- [Parameters](ec2_launch_template_module.md#parameters)
- [Notes](ec2_launch_template_module.md#notes)
- [Examples](ec2_launch_template_module.md#examples)
- [Return Values](ec2_launch_template_module.md#return-values)

## [Synopsis](ec2_launch_template_module.md#id1)

- Create, modify, and delete EC2 Launch Templates, which can be used to create individual instances or with Autoscaling Groups.
- The [amazon.aws.ec2_instance](../../amazon/aws/ec2_instance_module.md#ansible-collections-amazon-aws-ec2-instance-module) and [community.aws.autoscaling_group](autoscaling_group_module.md#ansible-collections-community-aws-autoscaling-group-module) modules can, instead of specifying all parameters on those tasks, be passed a Launch Template which contains settings like instance size, disk type, subnet, and more.

## [Requirements](ec2_launch_template_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ec2_launch_template_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **block_device_mappings**  list / elements=dictionary | The block device mapping. Supplying both a snapshot ID and an encryption value as arguments for block-device mapping results in an error. This is because only blank volumes can be encrypted on start, and these are not created from a snapshot. If a snapshot is the basis for the volume, it contains data by definition and its encryption status cannot be changed using this action. |
| **device_name**  string | The device name (for example, /dev/sdh or xvdh). |
| **ebs**  dictionary | Parameters used to automatically set up EBS volumes when the instance is launched. |
| **delete_on_termination**  boolean | Indicates whether the EBS volume is deleted on instance termination.  **Choices:**   - `false` - `true` |
| **encrypted**  boolean | Indicates whether the EBS volume is encrypted. Encrypted volumes can only be attached to instances that support Amazon EBS encryption. If you are creating a volume from a snapshot, you can’t specify an encryption value.  **Choices:**   - `false` - `true` |
| **iops**  integer | The number of I/O operations per second (IOPS) that the volume supports. For io1, this represents the number of IOPS that are provisioned for the volume. For gp2, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting. For more information about General Purpose SSD baseline performance, I/O credits, and bursting, see Amazon EBS Volume Types in the Amazon Elastic Compute Cloud User Guide.  Condition: This parameter is required for requests to create io1 volumes; it is not used in requests to create gp2, st1, sc1, or standard volumes. |
| **kms_key_id**  string | The ARN of the AWS Key Management Service (AWS KMS) CMK used for encryption. |
| **snapshot_id**  string | The ID of the snapshot to create the volume from. |
| **volume_size**  integer | The size of the volume, in GiB.  Default: If you’re creating the volume from a snapshot and don’t specify a volume size, the default is the snapshot size. |
| **volume_type**  string | The volume type |
| **no_device**  string | Suppresses the specified device included in the block device mapping of the AMI. |
| **virtual_name**  string | The virtual device name (ephemeralN). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for ephemeral0 and ephemeral1. The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume. |
| **cpu_options**  dictionary | Choose CPU settings for the EC2 instances that will be created with this template.  For more information, see <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html> |
| **core_count**  integer | The number of CPU cores for the instance. |
| **threads_per_core**  integer | The number of threads per CPU core. To disable Intel Hyper-Threading Technology for the instance, specify a value of 1. Otherwise, specify the default value of 2. |
| **credit_specification**  dictionary | The credit option for CPU usage of the instance. Valid for T2 or T3 instances only. |
| **cpu_credits**  string | The credit option for CPU usage of a T2 or T3 instance. Valid values are `standard` and `unlimited`. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **default_version**  string | Which version should be the default when users spin up new instances based on this template? By default, the latest version will be made the default.  **Default:** `"latest"` |
| **disable_api_termination**  boolean | This helps protect instances from accidental termination. If set to true, you can’t terminate the instance using the Amazon EC2 console, CLI, or API. To change this attribute to false after launch, use *ModifyInstanceAttribute*.  **Choices:**   - `false` - `true` |
| **ebs_optimized**  boolean | Indicates whether the instance is optimized for Amazon EBS I/O. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal Amazon EBS I/O performance. This optimization isn’t available with all instance types. Additional usage charges apply when using an EBS-optimized instance.  **Choices:**   - `false` - `true` |
| **elastic_gpu_specifications**  list / elements=dictionary | Settings for Elastic GPU attachments. See <https://aws.amazon.com/ec2/elastic-gpus/> for details. |
| **type**  string | The type of Elastic GPU to attach |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **iam_instance_profile**  string | The name or ARN of an IAM instance profile. Requires permissions to describe existing instance roles to confirm ARN is properly formed. |
| **image_id**  string | The AMI ID to use for new instances launched with this template. This value is region-dependent since AMIs are not global resources. |
| **instance_initiated_shutdown_behavior**  string | Indicates whether an instance stops or terminates when you initiate shutdown from the instance using the operating system shutdown command.  **Choices:**   - `"stop"` - `"terminate"` |
| **instance_market_options**  dictionary | Options for alternative instance markets, currently only the spot market is supported. |
| **market_type**  string | The market type. This should always be ‘spot’. |
| **spot_options**  dictionary | Spot-market specific settings. |
| **block_duration_minutes**  integer | The required duration for the Spot Instances (also known as Spot blocks), in minutes. This value must be a multiple of 60 (60, 120, 180, 240, 300, or 360). |
| **instance_interruption_behavior**  string | The behavior when a Spot Instance is interrupted. The default is `terminate`.  **Choices:**   - `"hibernate"` - `"stop"` - `"terminate"` |
| **max_price**  string | The highest hourly price you’re willing to pay for this Spot Instance. |
| **spot_instance_type**  string | The request type to send.  **Choices:**   - `"one-time"` - `"persistent"` |
| **instance_type**  string | The instance type, such as `c5.2xlarge`. For a full list of instance types, see <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html>. |
| **kernel_id**  string | The ID of the kernel. We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedkernels.html> |
| **key_name**  string | The name of the key pair. You can create a key pair using [amazon.aws.ec2_key](../../amazon/aws/ec2_key_module.md#ansible-collections-amazon-aws-ec2-key-module).  If you do not specify a key pair, you can’t connect to the instance unless you choose an AMI that is configured to allow users another way to log in. |
| **metadata_options**  dictionary  *added in community.aws 1.5.0* | Configure EC2 Metadata options.  For more information see the IMDS documentation <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html>. |
| **http_endpoint**  string | This parameter enables or disables the HTTP metadata endpoint on your instances.  **Choices:**   - `"enabled"` ← (default) - `"disabled"` |
| **http_protocol_ipv6**  string  *added in community.aws 3.1.0* | - Wether the instance metadata endpoint is available via IPv6 (`enabled`) or not (`disabled`). - Requires botocore >= 1.21.29   **Choices:**   - `"enabled"` - `"disabled"` ← (default) |
| **http_put_response_hop_limit**  integer | The desired HTTP PUT response hop limit for instance metadata requests. The larger the number, the further instance metadata requests can travel.  **Default:** `1` |
| **http_tokens**  string | The state of token usage for your instance metadata requests.  **Choices:**   - `"optional"` ← (default) - `"required"` |
| **instance_metadata_tags**  string  *added in community.aws 3.1.0* | Wether the instance tags are availble (`enabled`) via metadata endpoint or not (`disabled`).  Requires botocore >= 1.23.30  **Choices:**   - `"enabled"` - `"disabled"` ← (default) |
| **monitoring**  dictionary | Settings for instance monitoring. |
| **enabled**  boolean | Whether to turn on detailed monitoring for new instances. This will incur extra charges.  **Choices:**   - `false` - `true` |
| **network_interfaces**  list / elements=dictionary | One or more network interfaces. |
| **associate_public_ip_address**  boolean | Associates a public IPv4 address with eth0 for a new network interface.  **Choices:**   - `false` - `true` |
| **delete_on_termination**  boolean | Indicates whether the network interface is deleted when the instance is terminated.  **Choices:**   - `false` - `true` |
| **description**  string | A description for the network interface. |
| **device_index**  integer | The device index for the network interface attachment. |
| **groups**  list / elements=string | List of security group IDs to include on this instance. |
| **ipv6_address_count**  integer | The number of IPv6 addresses to assign to a network interface. Amazon EC2 automatically selects the IPv6 addresses from the subnet range. You can’t use this option if specifying the *ipv6_addresses* option. |
| **ipv6_addresses**  list / elements=string | A list of one or more specific IPv6 addresses from the IPv6 CIDR block range of your subnet. You can’t use this option if you’re specifying the *ipv6_address_count* option. |
| **network_interface_id**  string | The eni ID of a network interface to attach. |
| **private_ip_address**  string | The primary private IPv4 address of the network interface. |
| **subnet_id**  string | The ID of the subnet for the network interface. |
| **placement**  dictionary | The placement group settings for the instance. |
| **affinity**  string | The affinity setting for an instance on a Dedicated Host. |
| **availability_zone**  string | The Availability Zone for the instance. |
| **group_name**  string | The name of the placement group for the instance. |
| **host_id**  string | The ID of the Dedicated Host for the instance. |
| **tenancy**  string | The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **ram_disk_id**  string | The ID of the RAM disk to launch the instance with. We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UserProvidedkernels.html> |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **security_group_ids**  list / elements=string | A list of security group IDs (VPC or EC2-Classic) that the new instances will be added to. |
| **security_groups**  list / elements=string | A list of security group names (Default VPC or EC2-Classic) that the new instances will be added to. For any VPC other than Default, you must use *security_group_ids*. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **source_version**  string  *added in community.aws 4.1.0* | The version number of the launch template version on which to base the new version. The new version inherits the same launch parameters as the source version, except for parameters that you explicity specify. Snapshots applied to the block device mapping are ignored when creating a new version unless they are explicitly included.  **Default:** `"latest"` |
| **state**  string | Whether the launch template should exist or not.  Deleting specific versions of a launch template is not supported at this time.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: resource_tags  dictionary | A set of key-value pairs to be applied to resources when this Launch Template is used.  Tag key constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with *aws:*  Tag value constraints: Tag values are case-sensitive and accept a maximum of 255 Unicode characters. |
| **template_id**  aliases: id  string | The ID for the launch template, can be used for all cases except creating a new Launch Template. |
| **template_name**  aliases: name  string | The template name. This must be unique in the region-account combination you are using.  If no launch template exists with the specified name, a new launch template is created.  If a launch template with the specified name already exists and the configuration has not changed, nothing happens.  If a launch template with the specified name already exists and the configuration has changed, a new version of the launch template is created. |
| **user_data**  string | The Base64-encoded user data to make available to the instance. For more information, see the Linux <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html> and Windows <http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2-instance-metadata.html#instancedata-add-user-data> documentation on user-data. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **version_description**  string  *added in community.aws 5.5.0* | The description of a launch template version.  **Default:** `""` |

## [Notes](ec2_launch_template_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](ec2_launch_template_module.md#id5)

```yaml+jinja
- name: Create an ec2 launch template
  community.aws.ec2_launch_template:
    name: "my_template"
    image_id: "ami-04b762b4289fba92b"
    key_name: my_ssh_key
    instance_type: t2.micro
    iam_instance_profile: myTestProfile
    disable_api_termination: true

- name: >
    Create a new version of an existing ec2 launch template with a different instance type,
    while leaving an older version as the default version
  community.aws.ec2_launch_template:
    name: "my_template"
    default_version: 1
    instance_type: c5.4xlarge

- name: Delete an ec2 launch template
  community.aws.ec2_launch_template:
    name: "my_template"
    state: absent

# This module does not yet allow deletion of specific versions of launch templates
```

## [Return Values](ec2_launch_template_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **default_version**  integer | The version that will be used if only the template name is specified. Often this is the same as the latest version, but not always.  **Returned:** when state=present |
| **latest_version**  integer | Latest available version of the launch template  **Returned:** when state=present |

### Authors

- Ryan Scott Brown (@ryansb)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
