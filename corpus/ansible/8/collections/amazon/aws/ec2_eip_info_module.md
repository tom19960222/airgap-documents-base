---
collection: ansible
version: "8"
title: "amazon.aws.ec2_eip_info module – List EC2 EIP details"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/ec2_eip_info_module.html
fetched_at: 2026-07-28T01:06:23+00:00
---
# amazon.aws.ec2_eip_info module – List EC2 EIP details

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
> see [Requirements](ec2_eip_info_module.md#ansible-collections-amazon-aws-ec2-eip-info-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.ec2_eip_info`.

New in amazon.aws 5.0.0

- [Synopsis](ec2_eip_info_module.md#synopsis)
- [Requirements](ec2_eip_info_module.md#requirements)
- [Parameters](ec2_eip_info_module.md#parameters)
- [Notes](ec2_eip_info_module.md#notes)
- [Examples](ec2_eip_info_module.md#examples)
- [Return Values](ec2_eip_info_module.md#return-values)

## [Synopsis](ec2_eip_info_module.md#id1)

- List details of EC2 Elastic IP addresses.
- This module was originally added to `community.aws` in release 1.0.0.

## [Requirements](ec2_eip_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ec2_eip_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **filters**  dictionary | A dict of filters to apply. Each dict item consists of a filter key and filter value. See <https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-addresses.html#options> for possible filters. Filter names and values are case sensitive.  **Default:** `{}` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ec2_eip_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](ec2_eip_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details or the AWS region,
# see the AWS Guide for details.

- name: List all EIP addresses in the current region.
  amazon.aws.ec2_eip_info:
  register: regional_eip_addresses

- name: List all EIP addresses for a VM.
  amazon.aws.ec2_eip_info:
    filters:
       instance-id: i-123456789
  register: my_vm_eips

- ansible.builtin.debug:
    msg: "{{ my_vm_eips.addresses | selectattr('private_ip_address', 'equalto', '10.0.0.5') }}"

- name: List all EIP addresses for several VMs.
  amazon.aws.ec2_eip_info:
    filters:
       instance-id:
         - i-123456789
         - i-987654321
  register: my_vms_eips

- name: List all EIP addresses using the 'Name' tag as a filter.
  amazon.aws.ec2_eip_info:
    filters:
      tag:Name: www.example.com
  register: my_vms_eips

- name: List all EIP addresses using the Allocation-id as a filter
  amazon.aws.ec2_eip_info:
    filters:
      allocation-id: eipalloc-64de1b01
  register: my_vms_eips

# Set the variable eip_alloc to the value of the first allocation_id
# and set the variable my_pub_ip to the value of the first public_ip
- ansible.builtin.set_fact:
    eip_alloc: my_vms_eips.addresses[0].allocation_id
    my_pub_ip: my_vms_eips.addresses[0].public_ip
```

## [Return Values](ec2_eip_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **addresses**  list / elements=string | Properties of all Elastic IP addresses matching the provided filters. Each element is a dict with all the information related to an EIP.  **Returned:** on success  **Sample:** `[{"allocation_id": "eipalloc-64de1b01", "association_id": "eipassoc-0fe9ce90d6e983e97", "domain": "vpc", "instance_id": "i-01020cfeb25b0c84f", "network_interface_id": "eni-02fdeadfd4beef9323b", "network_interface_owner_id": "0123456789", "private_ip_address": "10.0.0.1", "public_ip": "54.81.104.1", "tags": {"Name": "test-vm-54.81.104.1"}}]` |

### Authors

- Brad Macpherson (@iiibrad)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
