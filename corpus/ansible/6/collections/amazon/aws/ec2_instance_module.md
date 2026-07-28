---
collection: ansible
version: "6"
title: "amazon.aws.ec2_instance module – Create & manage EC2 instances"
source_url: https://docs.ansible.com/projects/ansible/6/collections/amazon/aws/ec2_instance_module.html
fetched_at: 2026-07-27T16:43:44+00:00
---
# amazon.aws.ec2_instance module – Create & manage EC2 instances

> **Note:**
>
> This module is part of the [amazon.aws collection](https://galaxy.ansible.com/amazon/aws) (version 3.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install amazon.aws`.
> You need further requirements to be able to use this module,
> see [Requirements](ec2_instance_module.md#ansible-collections-amazon-aws-ec2-instance-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.ec2_instance`.

New in amazon.aws 1.0.0

- [Synopsis](ec2_instance_module.md#synopsis)
- [Requirements](ec2_instance_module.md#requirements)
- [Parameters](ec2_instance_module.md#parameters)
- [Notes](ec2_instance_module.md#notes)
- [Examples](ec2_instance_module.md#examples)
- [Return Values](ec2_instance_module.md#return-values)

## [Synopsis](ec2_instance_module.md#id2)

- Create and manage AWS EC2 instances.
- Note: This module does not support creating [EC2 Spot instances](https://aws.amazon.com/ec2/spot/). The [amazon.aws.ec2](ec2_module.md#ansible-collections-amazon-aws-ec2-module) module can create and manage spot instances.

## [Requirements](ec2_instance_module.md#id3)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_instance_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **availability_zone**  string | Specify an availability zone to use the default subnet it. Useful if not specifying the *vpc_subnet_id* parameter.  If no subnet, ENI, or availability zone is provided, the default subnet in the default VPC will be used in the first AZ (alphabetically sorted). |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **count**  integer  added in amazon.aws 2.2.0 | Number of instances to launch.  Setting this value will result in always launching new instances.  Mutually exclusive with *exact_count*. |
| **cpu_credit_specification**  string | For T series instances, choose whether to allow increased charges to buy CPU credits if the default pool is depleted.  Choose *unlimited* to enable buying additional CPU credits.  Choices:   - `"unlimited"` - `"standard"` |
| **cpu_options**  dictionary | Reduce the number of vCPU exposed to the instance.  Those parameters can only be set at instance launch. The two suboptions threads_per_core and core_count are mandatory.  See <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html> for combinations available. |
| **core_count**  integer / required | Set the number of core to enable. |
| **threads_per_core**  integer / required | Select the number of threads per core to enable. Disable or Enable Intel HT.  Choices:   - `1` - `2` |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **detailed_monitoring**  boolean | Whether to allow detailed cloudwatch metrics to be collected, enabling more detailed alerting.  Choices:   - `false` - `true` |
| **ebs_optimized**  boolean | Whether instance is should use optimized EBS volumes, see <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html>.  Choices:   - `false` - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **exact_count**  integer  added in amazon.aws 2.2.0 | An integer value which indicates how many instances that match the *filters* parameter should be running.  Instances are either created or terminated based on this value.  If termination takes place, least recently created instances will be terminated based on Launch Time.  Mutually exclusive with *count*, *instance_ids*. |
| **filters**  dictionary | A dict of filters to apply when deciding whether existing instances match and should be altered. Each dict item consists of a filter key and a filter value. See <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html>. for possible filters. Filter names and values are case sensitive.  By default, instances are filtered for counting by their “Name” tag, base AMI, state (running, by default), and subnet ID. Any queryable filter can be used. Good candidates are specific tags, SSH keys, or security groups. |
| **image**  dictionary | An image to use for the instance. The [amazon.aws.ec2_ami_info](ec2_ami_info_module.md#ansible-collections-amazon-aws-ec2-ami-info-module) module may be used to retrieve images. One of *image* or *image_id* are required when instance is not already present. |
| **id**  string | The AMI ID. |
| **kernel**  string | a string AKI to override the AMI kernel. |
| **ramdisk**  string | Overrides the AMI’s default ramdisk ID. |
| **image_id**  string | *ami* ID to use for the instance. One of *image* or *image_id* are required when instance is not already present.  This is an alias for *image.id*. |
| **instance_ids**  list / elements=string | If you specify one or more instance IDs, only instances that have the specified IDs are returned.  Mutually exclusive with *exact_count*. |
| **instance_initiated_shutdown_behavior**  string | Whether to stop or terminate an instance upon shutdown.  Choices:   - `"stop"` - `"terminate"` |
| **instance_role**  string | The ARN or name of an EC2-enabled instance role to be used. If a name is not provided in arn format then the ListInstanceProfiles permission must also be granted. <https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListInstanceProfiles.html> If no full ARN is provided, the role with a matching name will be used from the active AWS account. |
| **instance_type**  string | Instance type to use for the instance, see <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html> Only required when instance is not already present.  If not specified, t2.micro will be used. |
| **key_name**  string | Name of the SSH access key to assign to the instance - must exist in the region the instance is created. |
| **launch_template**  dictionary | The EC2 launch template to base instance configuration on. |
| **id**  string | the ID of the launch template (optional if name is specified). |
| **name**  string | the pretty name of the launch template (optional if id is specified). |
| **version**  string | the specific version of the launch template to use. If unspecified, the template default is chosen. |
| **metadata_options**  dictionary  added in amazon.aws 2.0.0 | Modify the metadata options for the instance.  See <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html> for more information.  The two suboptions *http_endpoint* and *http_tokens* are supported. |
| **http_endpoint**  string | Enables or disables the HTTP metadata endpoint on instances.  If specified a value of disabled, metadata of the instance will not be accessible.  Choices:   - `"enabled"` ← (default) - `"disabled"` |
| **http_tokens**  string | Set the state of token usage for instance metadata requests.  If the state is optional (v1 and v2), instance metadata can be retrieved with or without a signed token header on request.  If the state is required (v2), a signed token header must be sent with any instance metadata retrieval requests.  Choices:   - `"optional"` ← (default) - `"required"` |
| **name**  string | The Name tag for the instance. |
| **network**  dictionary | Either a dictionary containing the key ‘interfaces’ corresponding to a list of network interface IDs or containing specifications for a single network interface.  Use the [amazon.aws.ec2_eni](ec2_eni_module.md#ansible-collections-amazon-aws-ec2-eni-module) module to create ENIs with special settings. |
| **assign_public_ip**  boolean | when true assigns a public IP address to the interface  Choices:   - `false` - `true` |
| **delete_on_termination**  boolean | Delete the interface when the instance it is attached to is terminated.  Choices:   - `false` - `true` |
| **description**  string | a description for the network interface |
| **device_index**  integer | The index of the interface to modify |
| **groups**  list / elements=string | a list of security group IDs to attach to the interface |
| **interfaces**  list / elements=string | a list of ENI IDs (strings) or a list of objects containing the key *id*. |
| **ipv6_addresses**  list / elements=string | a list of IPv6 addresses to assign to the network interface |
| **private_ip_address**  string | an IPv4 address to assign to the interface |
| **private_ip_addresses**  list / elements=string | a list of IPv4 addresses to assign to the network interface |
| **source_dest_check**  boolean | controls whether source/destination checking is enabled on the interface  Choices:   - `false` - `true` |
| **subnet_id**  string | the subnet to connect the network interface to |
| **placement_group**  string | The placement group that needs to be assigned to the instance |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_tags**  boolean | Delete any tags not specified in the task that are on the instance. This means you have to specify all the desired tags on each task affecting an instance.  Choices:   - `false` ← (default) - `true` |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_group**  string | A security group ID or name. Mutually exclusive with *security_groups*. |
| **security_groups**  list / elements=string | A list of security group IDs or names (strings). Mutually exclusive with *security_group*. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Goal state for the instances.  *state=present*: ensures instances exist, but does not guarantee any state (e.g. running). Newly-launched instances will be run by EC2.  *state=running*: *state=present* + ensures the instances are running  *state=started*: *state=running* + waits for EC2 status checks to report OK if *wait=true*  *state=stopped*: ensures an existing instance is stopped.  *state=rebooted*: convenience alias for *state=stopped* immediately followed by *state=running*  *state=restarted*: convenience alias for *state=stopped* immediately followed by *state=started*  *state=terminated*: ensures an existing instance is terminated.  *state=absent*: alias for *state=terminated*  Choices:   - `"present"` ← (default) - `"terminated"` - `"running"` - `"started"` - `"stopped"` - `"restarted"` - `"rebooted"` - `"absent"` |
| **tags**  dictionary | A hash/dictionary of tags to add to the new instance or to add/remove from an existing one. |
| **tenancy**  string | What type of tenancy to allow an instance to use. Default is shared tenancy. Dedicated tenancy will incur additional charges.  Choices:   - `"dedicated"` - `"default"` |
| **termination_protection**  boolean | Whether to enable termination protection. This module will not terminate an instance with termination protection active, it must be turned off first.  Choices:   - `false` - `true` |
| **tower_callback**  dictionary | Preconfigured user-data to enable an instance to perform a Tower callback (Linux only).  Mutually exclusive with *user_data*.  For Windows instances, to enable remote access via Ansible set *tower_callback.windows* to true, and optionally set an admin password.  If using ‘windows’ and ‘set_password’, callback to Tower will not be performed but the instance will be ready to receive winrm connections from Ansible. |
| **host_config_key**  string | Host configuration secret key generated by the Tower job template. |
| **job_template_id**  string | Either the integer ID of the Tower Job Template, or the name (name supported only for Tower 3.2+). |
| **tower_address**  string | IP address or DNS name of Tower server. Must be accessible via this address from the VPC that this instance will be launched in. |
| **user_data**  string | Opaque blob of data which is made available to the ec2 instance |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **volumes**  list / elements=dictionary | A list of block device mappings, by default this will always use the AMI root device so the volumes option is primarily for adding more storage.  A mapping contains the (optional) keys device_name, virtual_name, ebs.volume_type, ebs.volume_size, ebs.kms_key_id, ebs.iops, and ebs.delete_on_termination.  Set ebs.throughput value requires botocore>=1.19.27.  For more information about each parameter, see <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BlockDeviceMapping.html>. |
| **vpc_subnet_id**  aliases: subnet_id  string | The subnet ID in which to launch the instance (VPC) If none is provided, [amazon.aws.ec2_instance](ec2_instance_module.md#ansible-collections-amazon-aws-ec2-instance-module) will chose the default zone of the default VPC. |
| **wait**  boolean | Whether or not to wait for the desired state (use wait_timeout to customize this).  Choices:   - `false` - `true` ← (default) |
| **wait_timeout**  integer | How long to wait (in seconds) for the instance to finish booting/terminating.  Default: `600` |

## [Notes](ec2_instance_module.md#id5)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_instance_module.md#id6)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Terminate every running instance in a region. Use with EXTREME caution.
  amazon.aws.ec2_instance:
    state: absent
    filters:
      instance-state-name: running

- name: restart a particular instance by its ID
  amazon.aws.ec2_instance:
    state: restarted
    instance_ids:
      - i-12345678

- name: start an instance with a public IP address
  amazon.aws.ec2_instance:
    name: "public-compute-instance"
    key_name: "prod-ssh-key"
    vpc_subnet_id: subnet-5ca1ab1e
    instance_type: c5.large
    security_group: default
    network:
      assign_public_ip: true
    image_id: ami-123456
    tags:
      Environment: Testing

- name: start an instance and Add EBS
  amazon.aws.ec2_instance:
    name: "public-withebs-instance"
    vpc_subnet_id: subnet-5ca1ab1e
    instance_type: t2.micro
    key_name: "prod-ssh-key"
    security_group: default
    volumes:
      - device_name: /dev/sda1
        ebs:
          volume_size: 16
          delete_on_termination: true

- name: start an instance with a cpu_options
  amazon.aws.ec2_instance:
    name: "public-cpuoption-instance"
    vpc_subnet_id: subnet-5ca1ab1e
    tags:
      Environment: Testing
    instance_type: c4.large
    volumes:
    - device_name: /dev/sda1
      ebs:
        delete_on_termination: true
    cpu_options:
        core_count: 1
        threads_per_core: 1

- name: start an instance and have it begin a Tower callback on boot
  amazon.aws.ec2_instance:
    name: "tower-callback-test"
    key_name: "prod-ssh-key"
    vpc_subnet_id: subnet-5ca1ab1e
    security_group: default
    tower_callback:
      # IP or hostname of tower server
      tower_address: 1.2.3.4
      job_template_id: 876
      host_config_key: '[secret config key goes here]'
    network:
      assign_public_ip: true
    image_id: ami-123456
    cpu_credit_specification: unlimited
    tags:
      SomeThing: "A value"

- name: start an instance with ENI (An existing ENI ID is required)
  amazon.aws.ec2_instance:
    name: "public-eni-instance"
    key_name: "prod-ssh-key"
    vpc_subnet_id: subnet-5ca1ab1e
    network:
      interfaces:
        - id: "eni-12345"
    tags:
      Env: "eni_on"
    volumes:
    - device_name: /dev/sda1
      ebs:
        delete_on_termination: true
    instance_type: t2.micro
    image_id: ami-123456

- name: add second ENI interface
  amazon.aws.ec2_instance:
    name: "public-eni-instance"
    network:
      interfaces:
        - id: "eni-12345"
        - id: "eni-67890"
    image_id: ami-123456
    tags:
      Env: "eni_on"
    instance_type: t2.micro

- name: start an instance with metadata options
  amazon.aws.ec2_instance:
    name: "public-metadataoptions-instance"
    vpc_subnet_id: subnet-5calable
    instance_type: t3.small
    image_id: ami-123456
    tags:
      Environment: Testing
    metadata_options:
      http_endpoint: enabled
      http_tokens: optional

# ensure number of instances running with a tag matches exact_count
- name: start multiple instances
  amazon.aws.ec2_instance:
    instance_type: t3.small
    image_id: ami-123456
    exact_count: 5
    region: us-east-2
    vpc_subnet_id: subnet-0123456
    network:
      assign_public_ip: yes
      security_group: default
    tags:
      foo: bar

# launches multiple instances - specific number of instances
- name: start specific number of multiple instances
  amazon.aws.ec2_instance:
    instance_type: t3.small
    image_id: ami-123456
    count: 3
    region: us-east-2
    network:
      assign_public_ip: yes
      security_group: default
      vpc_subnet_id: subnet-0123456
    state: present
    tags:
      foo: bar
```

## [Return Values](ec2_instance_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **instances**  complex | a list of ec2 instances  Returned: when wait == true |
| **ami_launch_index**  integer | The AMI launch index, which can be used to find this instance in the launch group.  Returned: always  Sample: `0` |
| **architecture**  string | The architecture of the image  Returned: always  Sample: `"x86_64"` |
| **block_device_mappings**  complex | Any block device mapping entries for the instance.  Returned: always |
| **device_name**  string | The device name exposed to the instance (for example, /dev/sdh or xvdh).  Returned: always  Sample: `"/dev/sdh"` |
| **ebs**  complex | Parameters used to automatically set up EBS volumes when the instance is launched.  Returned: always |
| **attach_time**  string | The time stamp when the attachment initiated.  Returned: always  Sample: `"2017-03-23T22:51:24+00:00"` |
| **delete_on_termination**  boolean | Indicates whether the volume is deleted on instance termination.  Returned: always  Sample: `true` |
| **status**  string | The attachment state.  Returned: always  Sample: `"attached"` |
| **volume_id**  string | The ID of the EBS volume  Returned: always  Sample: `"vol-12345678"` |
| **client_token**  string | The idempotency token you provided when you launched the instance, if applicable.  Returned: always  Sample: `"mytoken"` |
| **ebs_optimized**  boolean | Indicates whether the instance is optimized for EBS I/O.  Returned: always  Sample: `false` |
| **hypervisor**  string | The hypervisor type of the instance.  Returned: always  Sample: `"xen"` |
| **iam_instance_profile**  complex | The IAM instance profile associated with the instance, if applicable.  Returned: always |
| **arn**  string | The Amazon Resource Name (ARN) of the instance profile.  Returned: always  Sample: `"arn:aws:iam::000012345678:instance-profile/myprofile"` |
| **id**  string | The ID of the instance profile  Returned: always  Sample: `"JFJ397FDG400FG9FD1N"` |
| **image_id**  string | The ID of the AMI used to launch the instance.  Returned: always  Sample: `"ami-0011223344"` |
| **instance_id**  string | The ID of the instance.  Returned: always  Sample: `"i-012345678"` |
| **instance_type**  string | The instance type size of the running instance.  Returned: always  Sample: `"t2.micro"` |
| **key_name**  string | The name of the key pair, if this instance was launched with an associated key pair.  Returned: always  Sample: `"my-key"` |
| **launch_time**  string | The time the instance was launched.  Returned: always  Sample: `"2017-03-23T22:51:24+00:00"` |
| **monitoring**  complex | The monitoring for the instance.  Returned: always |
| **state**  string | Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled.  Returned: always  Sample: `"disabled"` |
| **network.source_dest_check**  boolean | Indicates whether source/destination checking is enabled.  Returned: always  Sample: `true` |
| **network_interfaces**  complex | One or more network interfaces for the instance.  Returned: always |
| **association**  complex | The association information for an Elastic IPv4 associated with the network interface.  Returned: always |
| **ip_owner_id**  string | The ID of the owner of the Elastic IP address.  Returned: always  Sample: `"amazon"` |
| **public_dns_name**  string | The public DNS name.  Returned: always  Sample: `""` |
| **public_ip**  string | The public IP address or Elastic IP address bound to the network interface.  Returned: always  Sample: `"1.2.3.4"` |
| **attachment**  complex | The network interface attachment.  Returned: always |
| **attach_time**  string | The time stamp when the attachment initiated.  Returned: always  Sample: `"2017-03-23T22:51:24+00:00"` |
| **attachment_id**  string | The ID of the network interface attachment.  Returned: always  Sample: `"eni-attach-3aff3f"` |
| **delete_on_termination**  boolean | Indicates whether the network interface is deleted when the instance is terminated.  Returned: always  Sample: `true` |
| **device_index**  integer | The index of the device on the instance for the network interface attachment.  Returned: always  Sample: `0` |
| **status**  string | The attachment state.  Returned: always  Sample: `"attached"` |
| **description**  string | The description.  Returned: always  Sample: `"My interface"` |
| **groups**  list / elements=dictionary | One or more security groups.  Returned: always |
| **group_id**  string | The ID of the security group.  Returned: always  Sample: `"sg-abcdef12"` |
| **group_name**  string | The name of the security group.  Returned: always  Sample: `"mygroup"` |
| **ipv6_addresses**  list / elements=dictionary | One or more IPv6 addresses associated with the network interface.  Returned: always |
| **ipv6_address**  string | The IPv6 address.  Returned: always  Sample: `"2001:0db8:85a3:0000:0000:8a2e:0370:7334"` |
| **mac_address**  string | The MAC address.  Returned: always  Sample: `"00:11:22:33:44:55"` |
| **network_interface_id**  string | The ID of the network interface.  Returned: always  Sample: `"eni-01234567"` |
| **owner_id**  string | The AWS account ID of the owner of the network interface.  Returned: always  Sample: `"01234567890"` |
| **private_ip_address**  string | The IPv4 address of the network interface within the subnet.  Returned: always  Sample: `"10.0.0.1"` |
| **private_ip_addresses**  list / elements=dictionary | The private IPv4 addresses associated with the network interface.  Returned: always |
| **association**  complex | The association information for an Elastic IP address (IPv4) associated with the network interface.  Returned: always |
| **ip_owner_id**  string | The ID of the owner of the Elastic IP address.  Returned: always  Sample: `"amazon"` |
| **public_dns_name**  string | The public DNS name.  Returned: always  Sample: `""` |
| **public_ip**  string | The public IP address or Elastic IP address bound to the network interface.  Returned: always  Sample: `"1.2.3.4"` |
| **primary**  boolean | Indicates whether this IPv4 address is the primary private IP address of the network interface.  Returned: always  Sample: `true` |
| **private_ip_address**  string | The private IPv4 address of the network interface.  Returned: always  Sample: `"10.0.0.1"` |
| **source_dest_check**  boolean | Indicates whether source/destination checking is enabled.  Returned: always  Sample: `true` |
| **status**  string | The status of the network interface.  Returned: always  Sample: `"in-use"` |
| **subnet_id**  string | The ID of the subnet for the network interface.  Returned: always  Sample: `"subnet-0123456"` |
| **vpc_id**  string | The ID of the VPC for the network interface.  Returned: always  Sample: `"vpc-0123456"` |
| **placement**  complex | The location where the instance launched, if applicable.  Returned: always |
| **availability_zone**  string | The Availability Zone of the instance.  Returned: always  Sample: `"ap-southeast-2a"` |
| **group_name**  string | The name of the placement group the instance is in (for cluster compute instances).  Returned: always  Sample: `""` |
| **tenancy**  string | The tenancy of the instance (if the instance is running in a VPC).  Returned: always  Sample: `"default"` |
| **private_dns_name**  string | The private DNS name.  Returned: always  Sample: `"ip-10-0-0-1.ap-southeast-2.compute.internal"` |
| **private_ip_address**  string | The IPv4 address of the network interface within the subnet.  Returned: always  Sample: `"10.0.0.1"` |
| **product_codes**  list / elements=dictionary | One or more product codes.  Returned: always |
| **product_code_id**  string | The product code.  Returned: always  Sample: `"aw0evgkw8ef3n2498gndfgasdfsd5cce"` |
| **product_code_type**  string | The type of product code.  Returned: always  Sample: `"marketplace"` |
| **public_dns_name**  string | The public DNS name assigned to the instance.  Returned: always |
| **public_ip_address**  string | The public IPv4 address assigned to the instance  Returned: always  Sample: `"52.0.0.1"` |
| **root_device_name**  string | The device name of the root device  Returned: always  Sample: `"/dev/sda1"` |
| **root_device_type**  string | The type of root device used by the AMI.  Returned: always  Sample: `"ebs"` |
| **security_groups**  list / elements=dictionary | One or more security groups for the instance.  Returned: always |
| **group_id**  string | The ID of the security group.  Returned: always  Sample: `"sg-0123456"` |
| **group_name**  string | The name of the security group.  Returned: always  Sample: `"my-security-group"` |
| **state**  complex | The current state of the instance.  Returned: always |
| **code**  integer | The low byte represents the state.  Returned: always  Sample: `16` |
| **name**  string | The name of the state.  Returned: always  Sample: `"running"` |
| **state_transition_reason**  string | The reason for the most recent state transition.  Returned: always |
| **subnet_id**  string | The ID of the subnet in which the instance is running.  Returned: always  Sample: `"subnet-00abcdef"` |
| **tags**  dictionary | Any tags assigned to the instance.  Returned: always |
| **virtualization_type**  string | The type of virtualization of the AMI.  Returned: always  Sample: `"hvm"` |
| **vpc_id**  dictionary | The ID of the VPC the instance is in.  Returned: always  Sample: `"vpc-0011223344"` |

### Authors

- Ryan Scott Brown (@ryansb)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
[Communication](index.md#communication-for-amazon-aws)
