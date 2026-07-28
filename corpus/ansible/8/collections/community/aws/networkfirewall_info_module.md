---
collection: ansible
version: "8"
title: "community.aws.networkfirewall_info module – describe AWS Network Firewall firewalls"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/networkfirewall_info_module.html
fetched_at: 2026-07-28T01:41:37+00:00
---
# community.aws.networkfirewall_info module – describe AWS Network Firewall firewalls

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
> see [Requirements](networkfirewall_info_module.md#ansible-collections-community-aws-networkfirewall-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.networkfirewall_info`.

New in community.aws 4.0.0

- [Synopsis](networkfirewall_info_module.md#synopsis)
- [Requirements](networkfirewall_info_module.md#requirements)
- [Parameters](networkfirewall_info_module.md#parameters)
- [Notes](networkfirewall_info_module.md#notes)
- [Examples](networkfirewall_info_module.md#examples)
- [Return Values](networkfirewall_info_module.md#return-values)

## [Synopsis](networkfirewall_info_module.md#id1)

- A module for describing AWS Network Firewall firewalls.

## [Requirements](networkfirewall_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](networkfirewall_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **arn**  string | The ARN of the Network Firewall.  Mutually exclusive with *name* and *vpc_ids*. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **name**  string | The name of the Network Firewall.  Mutually exclusive with *arn* and *vpc_ids*. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **vpc_ids**  aliases: vpcs, vpc_id  list / elements=string | A List of VPCs to retrieve the firewalls for.  Mutually exclusive with *name* and *arn*. |

## [Notes](networkfirewall_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](networkfirewall_info_module.md#id5)

```yaml+jinja
# Describe all firewalls in an account
- community.aws.networkfirewall_info: {}

# Describe a firewall by ARN
- community.aws.networkfirewall_info:
    arn: arn:aws:network-firewall:us-east-1:123456789012:firewall/ExampleFirewall

# Describe a firewall by name
- community.aws.networkfirewall_info:
    name: ExampleFirewall
```

## [Return Values](networkfirewall_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **firewall_list**  list / elements=string | A list of ARNs of the matching firewalls.  **Returned:** When a firewall name isn’t specified  **Sample:** `["arn:aws:network-firewall:us-east-1:123456789012:firewall/Example1", "arn:aws:network-firewall:us-east-1:123456789012:firewall/Example2"]` |
| **firewalls**  list / elements=dictionary | The details of the firewalls  **Returned:** success |
| **firewall**  dictionary | The details of the firewall  **Returned:** success |
| **delete_protection**  string | A flag indicating whether it is possible to delete the firewall.  **Returned:** success  **Sample:** `"True"` |
| **description**  string | A description of the firewall.  **Returned:** success  **Sample:** `"Description"` |
| **firewall_arn**  string | The ARN of the firewall.  **Returned:** success  **Sample:** `"arn:aws:network-firewall:us-east-1:123456789012:firewall/ExampleFirewall"` |
| **firewall_id**  string | A unique ID for the firewall.  **Returned:** success  **Sample:** `"12345678-abcd-1234-abcd-123456789abc"` |
| **firewall_name**  string | The name of the firewall.  **Returned:** success  **Sample:** `"ExampleFirewall"` |
| **firewall_policy_arn**  string | The ARN of the firewall policy used by the firewall.  **Returned:** success  **Sample:** `"arn:aws:network-firewall:us-east-1:123456789012:firewall-policy/ExamplePolicy"` |
| **firewall_policy_change_protection**  boolean | A flag indicating whether it is possible to change which firewall policy is used by the firewall.  **Returned:** success  **Sample:** `false` |
| **subnet_change_protection**  boolean | A flag indicating whether it is possible to change which subnets the firewall endpoints are in.  **Returned:** success  **Sample:** `true` |
| **subnet_mappings**  list / elements=dictionary | A list of the subnets the firewall endpoints are in.  **Returned:** success |
| **subnet_id**  string | The ID of the subnet.  **Returned:** success  **Sample:** `"subnet-12345678"` |
| **tags**  dictionary | The tags associated with the firewall.  **Returned:** success  **Sample:** `{"SomeTag": "SomeValue"}` |
| **vpc_id**  string | The ID of the VPC that the firewall is used by.  **Returned:** success  **Sample:** `"vpc-0123456789abcdef0"` |
| **firewall_metadata**  dictionary | Metadata about the firewall  **Returned:** success |
| **configuration_sync_state_summary**  string | A short summary of the synchronization status of the policy and rule groups.  **Returned:** success  **Sample:** `"IN_SYNC"` |
| **status**  string | A short summary of the status of the firewall endpoints.  **Returned:** success  **Sample:** `"READY"` |
| **sync_states**  dictionary | A description, broken down by availability zone, of the status of the firewall endpoints as well as the synchronization status of the policies and rule groups.  **Returned:** success  **Sample:** `{"us-east-1a": {"attachment": {"endpoint_id": "vpce-123456789abcdef01", "status": "READY", "subnet_id": "subnet-12345678"}, "config": {"arn:aws:network-firewall:us-east-1:123456789012:firewall-policy/Ansible-Example": {"sync_status": "IN_SYNC", "update_token": "abcdef01-0000-0000-0000-123456789abc"}, "arn:aws:network-firewall:us-east-1:123456789012:stateful-rulegroup/ExampleDomainList": {"sync_status": "IN_SYNC", "update_token": "12345678-0000-0000-0000-abcdef012345"}}}}` |

### Authors

- Mark Chappell (@tremble)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
