---
collection: ansible
version: "6"
title: "community.aws.ec2_eip module – manages EC2 elastic IP (EIP) addresses."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/ec2_eip_module.html
fetched_at: 2026-07-27T17:03:58+00:00
---
# community.aws.ec2_eip module – manages EC2 elastic IP (EIP) addresses.

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
> see [Requirements](ec2_eip_module.md#ansible-collections-community-aws-ec2-eip-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.ec2_eip`.

New in community.aws 1.0.0

- [Synopsis](ec2_eip_module.md#synopsis)
- [Requirements](ec2_eip_module.md#requirements)
- [Parameters](ec2_eip_module.md#parameters)
- [Notes](ec2_eip_module.md#notes)
- [Examples](ec2_eip_module.md#examples)
- [Return Values](ec2_eip_module.md#return-values)

## [Synopsis](ec2_eip_module.md#id1)

- This module can allocate or release an EIP.
- This module can associate/disassociate an EIP with instances or network interfaces.

## [Requirements](ec2_eip_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_eip_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allow_reassociation**  boolean | Specify this option to allow an Elastic IP address that is already associated with another network interface or instance to be re-associated with the specified instance or interface.  Choices:   - `false` ← (default) - `true` |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **device_id**  aliases: instance_id  string | The id of the device for the EIP. Can be an EC2 Instance id or Elastic Network Interface (ENI) id.  The *instance_id* alias has been deprecated and will be removed after 2022-12-01. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **in_vpc**  boolean | Allocate an EIP inside a VPC or not.  Required if specifying an ENI with *device_id*.  Choices:   - `false` ← (default) - `true` |
| **private_ip_address**  string | The primary or secondary private IP address to associate with the Elastic IP address. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **public_ip**  aliases: ip  string | The IP address of a previously allocated EIP.  When *state=present* and device is specified, the EIP is associated with the device.  When *state=absent* and device is specified, the EIP is disassociated from the device. |
| **public_ipv4_pool**  string | Allocates the new Elastic IP from the provided public IPv4 pool (BYOIP) only applies to newly allocated Elastic IPs, isn’t validated when *reuse_existing_ip_allowed=true*. |
| **purge_tags**  boolean  added in community.aws 2.1.0 | Whether the *tags* argument should cause tags not in the dictionary to be removed.  Choices:   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **release_on_disassociation**  boolean | Whether or not to automatically release the EIP when it is disassociated.  Choices:   - `false` ← (default) - `true` |
| **reuse_existing_ip_allowed**  boolean | Reuse an EIP that is not associated to a device (when available), instead of allocating a new one.  Choices:   - `false` ← (default) - `true` |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | When `state=present`, allocate an EIP or associate an existing EIP with a device.  When `state=absent`, disassociate the EIP from the device and optionally release it.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tag_name**  string | When *reuse_existing_ip_allowed=true*, supplement with this option to only reuse an Elastic IP if it is tagged with *tag_name*. |
| **tag_value**  string | Supplements *tag_name* but also checks that the value of the tag provided in *tag_name* matches *tag_value*. |
| **tags**  dictionary  added in community.aws 2.1.0 | A dictionary of tags to apply to the EIP. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **wait_timeout**  integer | The *wait_timeout* option does nothing and will be removed after 2022-06-01 |

## [Notes](ec2_eip_module.md#id4)

> **Note:**
>
> - There may be a delay between the time the EIP is assigned and when the cloud instance is reachable via the new address. Use wait_for and pause to delay further playbook execution until the instance is reachable, if necessary.
> - This module returns multiple changed statuses on disassociation or release. It returns an overall status based on any changes occurring. It also returns individual changed statuses for disassociation and release.
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_eip_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: associate an elastic IP with an instance
  community.aws.ec2_eip:
    device_id: i-1212f003
    ip: 93.184.216.119

- name: associate an elastic IP with a device
  community.aws.ec2_eip:
    device_id: eni-c8ad70f3
    ip: 93.184.216.119

- name: associate an elastic IP with a device and allow reassociation
  community.aws.ec2_eip:
    device_id: eni-c8ad70f3
    public_ip: 93.184.216.119
    allow_reassociation: true

- name: disassociate an elastic IP from an instance
  community.aws.ec2_eip:
    device_id: i-1212f003
    ip: 93.184.216.119
    state: absent

- name: disassociate an elastic IP with a device
  community.aws.ec2_eip:
    device_id: eni-c8ad70f3
    ip: 93.184.216.119
    state: absent

- name: allocate a new elastic IP and associate it with an instance
  community.aws.ec2_eip:
    device_id: i-1212f003

- name: allocate a new elastic IP without associating it to anything
  community.aws.ec2_eip:
    state: present
  register: eip

- name: output the IP
  ansible.builtin.debug:
    msg: "Allocated IP is {{ eip.public_ip }}"

- name: provision new instances with ec2
  amazon.aws.ec2:
    keypair: mykey
    instance_type: c1.medium
    image: ami-40603AD1
    wait: true
    group: webserver
    count: 3
  register: ec2

- name: associate new elastic IPs with each of the instances
  community.aws.ec2_eip:
    device_id: "{{ item }}"
  loop: "{{ ec2.instance_ids }}"

- name: allocate a new elastic IP inside a VPC in us-west-2
  community.aws.ec2_eip:
    region: us-west-2
    in_vpc: true
  register: eip

- name: output the IP
  ansible.builtin.debug:
    msg: "Allocated IP inside a VPC is {{ eip.public_ip }}"

- name: allocate eip - reuse unallocated ips (if found) with FREE tag
  community.aws.ec2_eip:
    region: us-east-1
    in_vpc: true
    reuse_existing_ip_allowed: true
    tag_name: FREE

- name: allocate eip - reuse unallocated ips if tag reserved is nope
  community.aws.ec2_eip:
    region: us-east-1
    in_vpc: true
    reuse_existing_ip_allowed: true
    tag_name: reserved
    tag_value: nope

- name: allocate new eip - from servers given ipv4 pool
  community.aws.ec2_eip:
    region: us-east-1
    in_vpc: true
    public_ipv4_pool: ipv4pool-ec2-0588c9b75a25d1a02

- name: allocate eip - from a given pool (if no free addresses where dev-servers tag is dynamic)
  community.aws.ec2_eip:
    region: us-east-1
    in_vpc: true
    reuse_existing_ip_allowed: true
    tag_name: dev-servers
    public_ipv4_pool: ipv4pool-ec2-0588c9b75a25d1a02

- name: allocate eip from pool - check if tag reserved_for exists and value is our hostname
  community.aws.ec2_eip:
    region: us-east-1
    in_vpc: true
    reuse_existing_ip_allowed: true
    tag_name: reserved_for
    tag_value: "{{ inventory_hostname }}"
    public_ipv4_pool: ipv4pool-ec2-0588c9b75a25d1a02
```

## [Return Values](ec2_eip_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **allocation_id**  string | allocation_id of the elastic ip  Returned: on success  Sample: `"eipalloc-51aa3a6c"` |
| **public_ip**  string | an elastic ip address  Returned: on success  Sample: `"52.88.159.209"` |

### Authors

- Rick Mendes (@rickmendes)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
