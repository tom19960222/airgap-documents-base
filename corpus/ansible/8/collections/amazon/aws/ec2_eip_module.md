---
collection: ansible
version: "8"
title: "amazon.aws.ec2_eip module – manages EC2 elastic IP (EIP) addresses."
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/ec2_eip_module.html
fetched_at: 2026-07-28T01:06:22+00:00
---
# amazon.aws.ec2_eip module – manages EC2 elastic IP (EIP) addresses.

> **Note:**
>
> This module is part of the [amazon.aws collection](https://galaxy.ansible.com/ui/repo/published/amazon/aws/) (version 6.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install amazon.aws`.
> You need further requirements to be able to use this module,
> see [Requirements](ec2_eip_module.md#ansible-collections-amazon-aws-ec2-eip-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.ec2_eip`.

New in amazon.aws 5.0.0

- [Synopsis](ec2_eip_module.md#synopsis)
- [Requirements](ec2_eip_module.md#requirements)
- [Parameters](ec2_eip_module.md#parameters)
- [Notes](ec2_eip_module.md#notes)
- [Examples](ec2_eip_module.md#examples)
- [Return Values](ec2_eip_module.md#return-values)

## [Synopsis](ec2_eip_module.md#id1)

- This module can allocate or release an EIP.
- This module can associate/disassociate an EIP with instances or network interfaces.
- This module was originally added to `community.aws` in release 1.0.0.

## [Requirements](ec2_eip_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ec2_eip_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **allow_reassociation**  boolean | Specify this option to allow an Elastic IP address that is already associated with another network interface or instance to be re-associated with the specified instance or interface.  **Choices:**   - `false` ← (default) - `true` |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **device_id**  string | The id of the device for the EIP.  Can be an EC2 Instance id or Elastic Network Interface (ENI) id.  When specifying an ENI id, *in_vpc* must be `true`  The `instance_id` alias was removed in release 6.0.0. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **in_vpc**  boolean | Allocate an EIP inside a VPC or not.  Required if specifying an ENI with *device_id*.  **Choices:**   - `false` ← (default) - `true` |
| **private_ip_address**  string | The primary or secondary private IP address to associate with the Elastic IP address. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **public_ip**  aliases: ip  string | The IP address of a previously allocated EIP.  When *state=present* and device is specified, the EIP is associated with the device.  When *state=absent* and device is specified, the EIP is disassociated from the device. |
| **public_ipv4_pool**  string | Allocates the new Elastic IP from the provided public IPv4 pool (BYOIP) only applies to newly allocated Elastic IPs, isn’t validated when *reuse_existing_ip_allowed=true*. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **release_on_disassociation**  boolean | Whether or not to automatically release the EIP when it is disassociated.  **Choices:**   - `false` ← (default) - `true` |
| **reuse_existing_ip_allowed**  boolean | Reuse an EIP that is not associated to a device (when available), instead of allocating a new one.  **Choices:**   - `false` ← (default) - `true` |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | When `state=present`, allocate an EIP or associate an existing EIP with a device.  When `state=absent`, disassociate the EIP from the device and optionally release it.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tag_name**  string | When *reuse_existing_ip_allowed=true*, supplement with this option to only reuse an Elastic IP if it is tagged with *tag_name*. |
| **tag_value**  string | Supplements *tag_name* but also checks that the value of the tag provided in *tag_name* matches *tag_value*. |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ec2_eip_module.md#id4)

> **Note:**
>
> - There may be a delay between the time the EIP is assigned and when the cloud instance is reachable via the new address. Use wait_for and pause to delay further playbook execution until the instance is reachable, if necessary.
> - This module returns multiple changed statuses on disassociation or release. It returns an overall status based on any changes occurring. It also returns individual changed statuses for disassociation and release.
> - Support for *tags* and *purge_tags* was added in release 2.1.0.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](ec2_eip_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: associate an elastic IP with an instance
  amazon.aws.ec2_eip:
    device_id: i-1212f003
    ip: 93.184.216.119

- name: associate an elastic IP with a device
  amazon.aws.ec2_eip:
    device_id: eni-c8ad70f3
    ip: 93.184.216.119

- name: associate an elastic IP with a device and allow reassociation
  amazon.aws.ec2_eip:
    device_id: eni-c8ad70f3
    public_ip: 93.184.216.119
    allow_reassociation: true

- name: disassociate an elastic IP from an instance
  amazon.aws.ec2_eip:
    device_id: i-1212f003
    ip: 93.184.216.119
    state: absent

- name: disassociate an elastic IP with a device
  amazon.aws.ec2_eip:
    device_id: eni-c8ad70f3
    ip: 93.184.216.119
    state: absent

- name: allocate a new elastic IP and associate it with an instance
  amazon.aws.ec2_eip:
    device_id: i-1212f003

- name: allocate a new elastic IP without associating it to anything
  amazon.aws.ec2_eip:
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
  amazon.aws.ec2_eip:
    device_id: "{{ item }}"
  loop: "{{ ec2.instance_ids }}"

- name: allocate a new elastic IP inside a VPC in us-west-2
  amazon.aws.ec2_eip:
    region: us-west-2
    in_vpc: true
  register: eip

- name: output the IP
  ansible.builtin.debug:
    msg: "Allocated IP inside a VPC is {{ eip.public_ip }}"

- name: allocate eip - reuse unallocated ips (if found) with FREE tag
  amazon.aws.ec2_eip:
    region: us-east-1
    in_vpc: true
    reuse_existing_ip_allowed: true
    tag_name: FREE

- name: allocate eip - reuse unallocated ips if tag reserved is nope
  amazon.aws.ec2_eip:
    region: us-east-1
    in_vpc: true
    reuse_existing_ip_allowed: true
    tag_name: reserved
    tag_value: nope

- name: allocate new eip - from servers given ipv4 pool
  amazon.aws.ec2_eip:
    region: us-east-1
    in_vpc: true
    public_ipv4_pool: ipv4pool-ec2-0588c9b75a25d1a02

- name: allocate eip - from a given pool (if no free addresses where dev-servers tag is dynamic)
  amazon.aws.ec2_eip:
    region: us-east-1
    in_vpc: true
    reuse_existing_ip_allowed: true
    tag_name: dev-servers
    public_ipv4_pool: ipv4pool-ec2-0588c9b75a25d1a02

- name: allocate eip from pool - check if tag reserved_for exists and value is our hostname
  amazon.aws.ec2_eip:
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
| **allocation_id**  string | allocation_id of the elastic ip  **Returned:** on success  **Sample:** `"eipalloc-51aa3a6c"` |
| **public_ip**  string | an elastic ip address  **Returned:** on success  **Sample:** `"52.88.159.209"` |

### Authors

- Rick Mendes (@rickmendes)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
