---
collection: ansible
version: "6"
title: "amazon.aws.ec2 module – create, terminate, start or stop an instance in ec2"
source_url: https://docs.ansible.com/projects/ansible/6/collections/amazon/aws/ec2_module.html
fetched_at: 2026-07-27T16:43:41+00:00
---
# amazon.aws.ec2 module – create, terminate, start or stop an instance in ec2

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
> see [Requirements](ec2_module.md#ansible-collections-amazon-aws-ec2-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.ec2`.

New in amazon.aws 1.0.0

- [DEPRECATED](ec2_module.md#deprecated)
- [Synopsis](ec2_module.md#synopsis)
- [Requirements](ec2_module.md#requirements)
- [Parameters](ec2_module.md#parameters)
- [Notes](ec2_module.md#notes)
- [Examples](ec2_module.md#examples)
- [Return Values](ec2_module.md#return-values)
- [Status](ec2_module.md#status)

## [DEPRECATED](ec2_module.md#id1)

Removed in:
:   version 4.0.0

Why:
:   The ec2 module is based upon a deprecated version of the AWS SDK.

Alternative:
:   Use [amazon.aws.ec2_instance](ec2_instance_module.md#ansible-collections-amazon-aws-ec2-instance-module).

## [Synopsis](ec2_module.md#id2)

- Creates or terminates ec2 instances.
- Note: This module uses the older boto Python module to interact with the EC2 API. [amazon.aws.ec2](ec2_module.md#ansible-collections-amazon-aws-ec2-module) will still receive bug fixes, but no new features. Consider using the [amazon.aws.ec2_instance](ec2_instance_module.md#ansible-collections-amazon-aws-ec2-instance-module) module instead. If [amazon.aws.ec2_instance](ec2_instance_module.md#ansible-collections-amazon-aws-ec2-instance-module) does not support a feature you need that is available in [amazon.aws.ec2](ec2_module.md#ansible-collections-amazon-aws-ec2-module), please file a feature request.

## [Requirements](ec2_module.md#id3)

The below requirements are needed on the host that executes this module.

- boto
- boto3 >= 1.16.0
- botocore >= 1.19.0
- python >= 2.6
- python >= 3.6

## [Parameters](ec2_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **assign_public_ip**  boolean | When provisioning within vpc, assign a public IP address. Boto library must be 2.13.0+.  Choices:   - `false` - `true` |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **count**  integer | Number of instances to launch.  Default: `1` |
| **count_tag**  any | Used with *exact_count* to determine how many nodes based on a specific tag criteria should be running. This can be expressed in multiple ways and is shown in the EXAMPLES section. For instance, one can request 25 servers that are tagged with `class=webserver`. The specified tag must already exist or be passed in as the *instance_tags* option. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ebs_optimized**  boolean | Whether instance is using optimized EBS volumes, see <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html>.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **exact_count**  integer | An integer value which indicates how many instances that match the ‘count_tag’ parameter should be running. Instances are either created or terminated based on this value. |
| **group**  aliases: groups  list / elements=string | Security group (or list of groups) to use with the instance. |
| **group_id**  list / elements=string | Security group id (or list of ids) to use with the instance. |
| **id**  string | Identifier for this instance or set of instances, so that the module will be idempotent with respect to EC2 instances.  This identifier is valid for at least 24 hours after the termination of the instance, and should not be reused for another call later on.  For details, see the description of client token at <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Run_Instance_Idempotency.html>. |
| **image**  string | *ami* ID to use for the instance.  Required when *state=present*. |
| **instance_ids**  aliases: instance_id  list / elements=string | list of instance ids, currently used for states: absent, running, stopped |
| **instance_initiated_shutdown_behavior**  string | Set whether AWS will Stop or Terminate an instance on shutdown. This parameter is ignored when using instance-store. images (which require termination on shutdown).  Choices:   - `"stop"` ← (default) - `"terminate"` |
| **instance_profile_name**  string | Name of the IAM instance profile (i.e. what the EC2 console refers to as an “IAM Role”) to use. Boto library must be 2.5.0+. |
| **instance_tags**  dictionary | A hash/dictionary of tags to add to the new instance or for instances to start/stop by tag. For example `{"key":"value"}` or `{"key":"value","key2":"value2"}`. |
| **instance_type**  aliases: type  string | Instance type to use for the instance, see <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html>.  Required when creating a new instance. |
| **kernel**  string | Kernel eki to use for the instance. |
| **key_name**  aliases: keypair  string | Key pair to use on the instance.  The SSH key must already exist in AWS in order to use this argument.  Keys can be created / deleted using the [amazon.aws.ec2_key](ec2_key_module.md#ansible-collections-amazon-aws-ec2-key-module) module. |
| **monitoring**  boolean | Enable detailed monitoring (CloudWatch) for the instance.  Choices:   - `false` ← (default) - `true` |
| **network_interfaces**  aliases: network_interface  list / elements=string | A list of existing network interfaces to attach to the instance at launch. When specifying existing network interfaces, none of the *assign_public_ip*, *private_ip*, *vpc_subnet_id*, *group*, or *group_id* parameters may be used. (Those parameters are for creating a new network interface at launch.) |
| **placement_group**  string | Placement group for the instance when using EC2 Clustered Compute. |
| **private_ip**  string | The private ip address to assign the instance (from the vpc subnet). |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **ramdisk**  string | Ramdisk eri to use for the instance. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **source_dest_check**  boolean | Enable or Disable the Source/Destination checks (for NAT instances and Virtual Routers). When initially creating an instance the EC2 API defaults this to `True`.  Choices:   - `false` - `true` |
| **spot_launch_group**  string | Launch group for spot requests, see <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-spot-instances-work.html#spot-launch-group>. |
| **spot_price**  string | Maximum spot price to bid. If not set, a regular on-demand instance is requested.  A spot request is made with this maximum bid. When it is filled, the instance is started. |
| **spot_type**  string | The type of spot request.  After being interrupted a `persistent` spot instance will be started once there is capacity to fill the request again.  Choices:   - `"one-time"` ← (default) - `"persistent"` |
| **spot_wait_timeout**  integer | How long to wait for the spot instance request to be fulfilled. Affects ‘Request valid until’ for setting spot request lifespan.  Default: `600` |
| **state**  string | Create, terminate, start, stop or restart instances.  When *state=absent*, *instance_ids* is required.  When *state=running*, *state=stopped* or *state=restarted* then either *instance_ids* or *instance_tags* is required.  Choices:   - `"absent"` - `"present"` ← (default) - `"restarted"` - `"running"` - `"stopped"` |
| **tenancy**  string | An instance with a tenancy of `dedicated` runs on single-tenant hardware and can only be launched into a VPC.  Note that to use dedicated tenancy you MUST specify a *vpc_subnet_id* as well.  Dedicated tenancy is not available for EC2 “micro” instances.  Choices:   - `"default"` ← (default) - `"dedicated"` |
| **termination_protection**  boolean | Enable or Disable the Termination Protection.  Defaults to `false`.  Choices:   - `false` - `true` |
| **user_data**  string | Opaque blob of data which is made available to the EC2 instance. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **volumes**  list / elements=dictionary | A list of hash/dictionaries of volumes to add to the new instance. |
| **delete_on_termination**  boolean | Whether the volume should be automatically deleted when the instance is terminated.  Choices:   - `false` ← (default) - `true` |
| **device_name**  string / required | A name for the device (For example `/dev/sda`). |
| **encrypted**  boolean | Whether the volume should be encrypted using the ‘aws/ebs’ KMS CMK.  Choices:   - `false` ← (default) - `true` |
| **ephemeral**  string | Whether the volume should be ephemeral.  Data on ephemeral volumes is lost when the instance is stopped.  Mutually exclusive with the *snapshot* parameter. |
| **iops**  integer | The number of IOPS per second to provision for the volume.  Required when *volume_type=io1*. |
| **snapshot**  string | The ID of an EBS snapshot to copy when creating the volume.  Mutually exclusive with the *ephemeral* parameter. |
| **volume_size**  integer | The size of the volume (in GiB). |
| **volume_type**  string | The type of volume to create.  See <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html> for more information on the available volume types. |
| **vpc_subnet_id**  string | The subnet ID in which to launch the instance (VPC). |
| **wait**  boolean | Wait for the instance to reach its desired state before returning.  Does not wait for SSH, see the ‘wait_for_connection’ example for details.  Choices:   - `false` ← (default) - `true` |
| **wait_timeout**  integer | How long before wait gives up, in seconds.  Default: `300` |
| **zone**  aliases: aws_zone, ec2_zone  string | AWS availability zone in which to launch the instance. |

## [Notes](ec2_module.md#id5)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_module.md#id6)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

# Basic provisioning example
- amazon.aws.ec2:
    key_name: mykey
    instance_type: t2.micro
    image: ami-123456
    wait: yes
    group: webserver
    count: 3
    vpc_subnet_id: subnet-29e63245
    assign_public_ip: yes

# Advanced example with tagging and CloudWatch
- amazon.aws.ec2:
    key_name: mykey
    group: databases
    instance_type: t2.micro
    image: ami-123456
    wait: yes
    wait_timeout: 500
    count: 5
    instance_tags:
       db: postgres
    monitoring: yes
    vpc_subnet_id: subnet-29e63245
    assign_public_ip: yes

# Single instance with additional IOPS volume from snapshot and volume delete on termination
- amazon.aws.ec2:
    key_name: mykey
    group: webserver
    instance_type: c3.medium
    image: ami-123456
    wait: yes
    wait_timeout: 500
    volumes:
      - device_name: /dev/sdb
        snapshot: snap-abcdef12
        volume_type: io1
        iops: 1000
        volume_size: 100
        delete_on_termination: true
    monitoring: yes
    vpc_subnet_id: subnet-29e63245
    assign_public_ip: yes

# Single instance with ssd gp2 root volume
- amazon.aws.ec2:
    key_name: mykey
    group: webserver
    instance_type: c3.medium
    image: ami-123456
    wait: yes
    wait_timeout: 500
    volumes:
      - device_name: /dev/xvda
        volume_type: gp2
        volume_size: 8
    vpc_subnet_id: subnet-29e63245
    assign_public_ip: yes
    count_tag:
      Name: dbserver
    exact_count: 1

# Multiple groups example
- amazon.aws.ec2:
    key_name: mykey
    group: ['databases', 'internal-services', 'sshable', 'and-so-forth']
    instance_type: m1.large
    image: ami-6e649707
    wait: yes
    wait_timeout: 500
    count: 5
    instance_tags:
        db: postgres
    monitoring: yes
    vpc_subnet_id: subnet-29e63245
    assign_public_ip: yes

# Multiple instances with additional volume from snapshot
- amazon.aws.ec2:
    key_name: mykey
    group: webserver
    instance_type: m1.large
    image: ami-6e649707
    wait: yes
    wait_timeout: 500
    count: 5
    volumes:
    - device_name: /dev/sdb
      snapshot: snap-abcdef12
      volume_size: 10
    monitoring: yes
    vpc_subnet_id: subnet-29e63245
    assign_public_ip: yes

# Dedicated tenancy example
- amazon.aws.ec2:
    assign_public_ip: yes
    group_id: sg-1dc53f72
    key_name: mykey
    image: ami-6e649707
    instance_type: m1.small
    tenancy: dedicated
    vpc_subnet_id: subnet-29e63245
    wait: yes

# Spot instance example
- amazon.aws.ec2:
    spot_price: 0.24
    spot_wait_timeout: 600
    keypair: mykey
    group_id: sg-1dc53f72
    instance_type: m1.small
    image: ami-6e649707
    wait: yes
    vpc_subnet_id: subnet-29e63245
    assign_public_ip: yes
    spot_launch_group: report_generators
    instance_initiated_shutdown_behavior: terminate

# Examples using pre-existing network interfaces
- amazon.aws.ec2:
    key_name: mykey
    instance_type: t2.small
    image: ami-f005ba11
    network_interface: eni-deadbeef

- amazon.aws.ec2:
    key_name: mykey
    instance_type: t2.small
    image: ami-f005ba11
    network_interfaces: ['eni-deadbeef', 'eni-5ca1ab1e']

# Launch instances, runs some tasks
# and then terminate them

- name: Create a sandbox instance
  hosts: localhost
  gather_facts: False
  vars:
    keypair: my_keypair
    instance_type: m1.small
    security_group: my_securitygroup
    image: my_ami_id
    region: us-east-1
  tasks:
    - name: Launch instance
      amazon.aws.ec2:
         key_name: "{{ keypair }}"
         group: "{{ security_group }}"
         instance_type: "{{ instance_type }}"
         image: "{{ image }}"
         wait: true
         region: "{{ region }}"
         vpc_subnet_id: subnet-29e63245
         assign_public_ip: yes
      register: ec2

    - name: Add new instance to host group
      add_host:
        hostname: "{{ item.public_ip }}"
        groupname: launched
      loop: "{{ ec2.instances }}"

    - name: Wait for SSH to come up
      delegate_to: "{{ item.public_dns_name }}"
      wait_for_connection:
        delay: 60
        timeout: 320
      loop: "{{ ec2.instances }}"

- name: Configure instance(s)
  hosts: launched
  become: True
  gather_facts: True
  roles:
    - my_awesome_role
    - my_awesome_test

- name: Terminate instances
  hosts: localhost
  tasks:
    - name: Terminate instances that were previously launched
      amazon.aws.ec2:
        state: 'absent'
        instance_ids: '{{ ec2.instance_ids }}'

# Start a few existing instances, run some tasks
# and stop the instances

- name: Start sandbox instances
  hosts: localhost
  gather_facts: false
  vars:
    instance_ids:
      - 'i-xxxxxx'
      - 'i-xxxxxx'
      - 'i-xxxxxx'
    region: us-east-1
  tasks:
    - name: Start the sandbox instances
      amazon.aws.ec2:
        instance_ids: '{{ instance_ids }}'
        region: '{{ region }}'
        state: running
        wait: True
        vpc_subnet_id: subnet-29e63245
        assign_public_ip: yes
  roles:
    - do_neat_stuff
    - do_more_neat_stuff

- name: Stop sandbox instances
  hosts: localhost
  gather_facts: false
  vars:
    instance_ids:
      - 'i-xxxxxx'
      - 'i-xxxxxx'
      - 'i-xxxxxx'
    region: us-east-1
  tasks:
    - name: Stop the sandbox instances
      amazon.aws.ec2:
        instance_ids: '{{ instance_ids }}'
        region: '{{ region }}'
        state: stopped
        wait: True
        vpc_subnet_id: subnet-29e63245
        assign_public_ip: yes

#
# Start stopped instances specified by tag
#
- amazon.aws.ec2:
    instance_tags:
        Name: ExtraPower
    state: running

#
# Restart instances specified by tag
#
- amazon.aws.ec2:
    instance_tags:
        Name: ExtraPower
    state: restarted

#
# Enforce that 5 instances with a tag "foo" are running
# (Highly recommended!)
#

- amazon.aws.ec2:
    key_name: mykey
    instance_type: c1.medium
    image: ami-40603AD1
    wait: yes
    group: webserver
    instance_tags:
        foo: bar
    exact_count: 5
    count_tag: foo
    vpc_subnet_id: subnet-29e63245
    assign_public_ip: yes

#
# Enforce that 5 running instances named "database" with a "dbtype" of "postgres"
#

- amazon.aws.ec2:
    key_name: mykey
    instance_type: c1.medium
    image: ami-40603AD1
    wait: yes
    group: webserver
    instance_tags:
        Name: database
        dbtype: postgres
    exact_count: 5
    count_tag:
        Name: database
        dbtype: postgres
    vpc_subnet_id: subnet-29e63245
    assign_public_ip: yes

#
# count_tag complex argument examples
#

    # instances with tag foo
- amazon.aws.ec2:
    count_tag:
        foo:

    # instances with tag foo=bar
- amazon.aws.ec2:
    count_tag:
        foo: bar

    # instances with tags foo=bar & baz
- amazon.aws.ec2:
    count_tag:
        foo: bar
        baz:

    # instances with tags foo & bar & baz=bang
- amazon.aws.ec2:
    count_tag:
        - foo
        - bar
        - baz: bang
```

## [Return Values](ec2_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | If the EC2 instance has changed.  Returned: always  Sample: `true` |
| **instances**  list / elements=string | The instances.  Returned: always |
| **ami_launch_index**  integer | The AMI launch index, which can be used to find this instance in the launch group.  Returned: always  Sample: `0` |
| **architecture**  string | The architecture of the image.  Returned: always  Sample: `"x86_64"` |
| **block_device_mapping**  dictionary | Any block device mapping entries for the instance.  Returned: always  Sample: `{"/dev/xvda": {"delete_on_termination": true, "status": "attached", "volume_id": "vol-06d364586f5550b62"}}` |
| **capacity_reservation_specification**  dictionary | Information about the Capacity Reservation targeting option.  Returned: always  Sample: `{"capacity_reservation_preference": "open"}` |
| **client_token**  string | The idempotency token you provided when you launched the instance, if applicable.  Returned: always  Sample: `""` |
| **cpu_options**  dictionary | The CPU options for the instance.  Returned: always  Sample: `{"core_count": 1, "threads_per_core": 1}` |
| **dns_name**  string | The public DNS name assigned to the instance.  Returned: always  Sample: `"ec2-203-0-113-1.z-2.compute-1.amazonaws.com"` |
| **ebs_optimized**  boolean | Indicates whether the instance is optimized for Amazon EBS I/O.  Returned: always  Sample: `false` |
| **ena_support**  boolean | Specifies whether enhanced networking with ENA is enabled.  Returned: always  Sample: `true` |
| **enclave_options**  dictionary | Indicates whether the instance is enabled for AWS Nitro Enclaves.  Returned: always  Sample: `{"enabled": false}` |
| **groups**  dictionary | One or more security groups.  Returned: always  Sample: `{"sg-0c6562ab3d435619f": "ansible-test--88312190_setup"}` |
| **hibernation_options**  dictionary | Indicates whether the instance is enabled for hibernation.  Returned: always  Sample: `{"configured": false}` |
| **hypervisor**  string | The hypervisor type of the instance.  Returned: always  Sample: `"xen"` |
| **image_id**  string | The ID of the AMI used to launch the instance.  Returned: always  Sample: `"ami-0d5eff06f840b45e9"` |
| **instance_id**  string | The ID of the instance.  Returned: always  Sample: `"i-0250719204c428be1"` |
| **instance_type**  string | The instance type.  Returned: always  Sample: `"t2.micro"` |
| **kernel**  string | The kernel associated with this instance, if applicable.  Returned: always  Sample: `""` |
| **key_name**  string | The name of the key pair, if this instance was launched with an associated key pair.  Returned: always  Sample: `"ansible-test-88312190_setup"` |
| **launch_time**  string | The time the instance was launched.  Returned: always  Sample: `"2021-05-09T19:30:26.000Z"` |
| **metadata**  dictionary | The metadata options for the instance.  Returned: always  Sample: `{"http_endpoint": "enabled", "http_put_response_hop_limit": 1, "http_tokens": "optional", "state": "applied"}` |
| **monitoring**  dictionary | The monitoring for the instance.  Returned: always  Sample: `{"state": "disabled"}` |
| **network_interfaces**  list / elements=string | The network interfaces for the instance.  Returned: always  Sample: `[{"attachment": {"attach_time": "2021-05-09T19:30:57+00:00", "attachment_id": "eni-attach-07341f2560be6c8fc", "delete_on_termination": true, "device_index": 0, "network_card_index": 0, "status": "attached"}, "description": "", "groups": [{"group_id": "sg-0c6562ab3d435619f", "group_name": "ansible-test-88312190_setup"}], "interface_type": "interface", "ipv6_addresses": [], "mac_address": "0e:0e:36:60:67:cf", "network_interface_id": "eni-061dee20eba3b445a", "owner_id": "721066863947", "private_dns_name": "ip-10-176-1-178.ec2.internal", "private_ip_address": "10.176.1.178", "private_ip_addresses": [{"primary": true, "private_dns_name": "ip-10-176-1-178.ec2.internal", "private_ip_address": "10.176.1.178"}], "source_dest_check": true, "status": "in-use", "subnet_id": "subnet-069d3e2eab081955d", "vpc_id": "vpc-0b6879b6ca2e9be2b"}]` |
| **placement**  dictionary | The location where the instance launched, if applicable.  Returned: always  Sample: `{"availability_zone": "us-east-1a", "group_name": "", "tenancy": "default"}` |
| **private_dns_name**  string | The private DNS hostname name assigned to the instance.  Returned: always  Sample: `"ip-10-176-1-249.ec2.internal"` |
| **private_ip**  string | The private IPv4 address assigned to the instance.  Returned: always  Sample: `"10.176.1.249"` |
| **public_dns_name**  string | The public DNS name assigned to the instance.  Returned: always  Sample: `"ec2-203-0-113-1.z-2.compute-1.amazonaws.com"` |
| **public_ip**  string | The public IPv4 address, or the Carrier IP address assigned to the instance, if applicable.  Returned: always  Sample: `"203.0.113.1"` |
| **ramdisk**  string | The RAM disk associated with this instance, if applicable.  Returned: always  Sample: `""` |
| **root_device_name**  string | The device name of the root device volume.  Returned: always  Sample: `"/dev/xvda"` |
| **root_device_type**  string | The root device type used by the AMI.  Returned: always  Sample: `"ebs"` |
| **security_groups**  list / elements=string | The security groups for the instance.  Returned: always  Sample: `[{"group_id": "sg-0c6562ab3d435619f", "group_name": "ansible-test-alinas-mbp-88312190_setup"}]` |
| **source_dest_check**  boolean | Indicates whether source/destination checking is enabled.  Returned: always  Sample: `true` |
| **state**  dictionary | The current state of the instance.  Returned: always  Sample: `{"code": 80, "name": "stopped"}` |
| **state_reason**  dictionary | The reason for the most recent state transition.  Returned: always  Sample: `{"code": "Client.UserInitiatedShutdown", "message": "Client.UserInitiatedShutdown: User initiated shutdown"}` |
| **state_transition_reason**  string | The reason for the most recent state transition. This might be an empty string.  Returned: always  Sample: `"User initiated (2021-05-09 19:31:28 GMT)"` |
| **subnet_id**  string | The ID of the subnet in which the instance is running.  Returned: always  Sample: `"subnet-069d3e2eab081955d"` |
| **tags**  dictionary | Any tags assigned to the instance.  Returned: always  Sample: `{"ResourcePrefix": "ansible-test-88312190-integration_tests"}` |
| **tenancy**  string | The tenancy of the instance (if the instance is running in a VPC).  Returned: always  Sample: `"default"` |
| **virtualization_type**  string | The virtualization type of the instance.  Returned: always  Sample: `"hvm"` |
| **vpc_id**  string | The ID of the VPC in which the instance is running.  Returned: always  Sample: `"vpc-0b6879b6ca2e9be2b"` |

## [Status](ec2_module.md#id8)

- This module will be removed in version 4.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](ec2_module.md#deprecated).

### Authors

- Tim Gerla (@tgerla)
- Lester Wade (@lwade)
- Seth Vidal (@skvidal)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
[Communication](index.md#communication-for-amazon-aws)
