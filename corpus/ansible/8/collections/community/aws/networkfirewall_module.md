---
collection: ansible
version: "8"
title: "community.aws.networkfirewall module – manage AWS Network Firewall firewalls"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/networkfirewall_module.html
fetched_at: 2026-07-28T01:41:36+00:00
---
# community.aws.networkfirewall module – manage AWS Network Firewall firewalls

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
> see [Requirements](networkfirewall_module.md#ansible-collections-community-aws-networkfirewall-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.networkfirewall`.

New in community.aws 4.0.0

- [Synopsis](networkfirewall_module.md#synopsis)
- [Requirements](networkfirewall_module.md#requirements)
- [Parameters](networkfirewall_module.md#parameters)
- [Notes](networkfirewall_module.md#notes)
- [Examples](networkfirewall_module.md#examples)
- [Return Values](networkfirewall_module.md#return-values)

## [Synopsis](networkfirewall_module.md#id1)

- A module for creating, updating and deleting AWS Network Firewall firewalls.

## [Requirements](networkfirewall_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](networkfirewall_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **arn**  aliases: firewall_arn  string | The ARN of the firewall.  Exactly one of *arn* or *name* must be provided. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **delete_protection**  boolean | When *delete_protection=True*, the firewall is protected from deletion.  Defaults to `false` when not provided on creation.  **Choices:**   - `false` - `true` |
| **description**  string | A description for the firewall. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **name**  aliases: firewall_name  string | The name of the firewall.  Cannot be updated after creation.  Exactly one of *arn* or *name* must be provided. |
| **policy**  aliases: firewall_policy_arn  string | The ARN of the Network Firewall policy to use for the firewall.  Required when creating a new firewall. |
| **policy_change_protection**  aliases: firewall_policy_change_protection  boolean | When *policy_change_protection=True*, the firewall is protected from changes to which policy is attached to the firewall.  Defaults to `false` when not provided on creation.  **Choices:**   - `false` - `true` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_subnets**  boolean | If *purge_subnets=true*, existing subnets will be removed from the firewall as necessary to match exactly what is defined by *subnets*.  **Choices:**   - `false` - `true` ← (default) |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Create or remove the firewall.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subnet_change_protection**  boolean | When *subnet_change_protection=True*, the firewall is protected from changes to which subnets is attached to the firewall.  Defaults to `false` when not provided on creation.  **Choices:**   - `false` - `true` |
| **subnets**  list / elements=string | The ID of the subnets to which the firewall will be associated.  Required when creating a new firewall. |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **wait**  boolean | On creation, whether to wait for the firewall to reach the `READY` state.  On deletion, whether to wait for the firewall to reach the `DELETED` state.  On update, whether to wait for the firewall to reach the `IN_SYNC` configuration synchronization state.  **Choices:**   - `false` - `true` ← (default) |
| **wait_timeout**  integer | Maximum time, in seconds, to wait for the firewall to reach the expected state.  Defaults to 600 seconds. |

## [Notes](networkfirewall_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](networkfirewall_module.md#id5)

```yaml+jinja
# Create an AWS Network Firewall
- community.aws.networkfirewall:
    name: 'ExampleFirewall'
    state: present
    policy: 'ExamplePolicy'
    subnets:
    - 'subnet-123456789abcdef01'

# Create an AWS Network Firewall with various options, don't wait for creation
# to finish.
- community.aws.networkfirewall:
    name: 'ExampleFirewall'
    state: present
    delete_protection: True
    description: "An example Description"
    policy: 'ExamplePolicy'
    policy_change_protection: True
    subnets:
    - 'subnet-123456789abcdef01'
    - 'subnet-abcdef0123456789a'
    subnet_change_protection: True
    tags:
      ExampleTag: Example Value
      another_tag: another_example
    wait: false

# Delete an AWS Network Firewall
- community.aws.networkfirewall:
    state: absent
    name: 'ExampleFirewall'
```

## [Return Values](networkfirewall_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **firewall**  dictionary | The full details of the firewall  **Returned:** success |
| **firewall**  dictionary | The details of the firewall  **Returned:** success |
| **delete_protection**  string | A flag indicating whether it is possible to delete the firewall.  **Returned:** success  **Sample:** `"True"` |
| **description**  string | A description of the firewall.  **Returned:** success  **Sample:** `"Description"` |
| **firewall_arn**  string | The ARN of the firewall.  **Returned:** success  **Sample:** `"arn:aws:network-firewall:us-east-1:123456789012:firewall/ExampleFirewall"` |
| **firewall_id**  string | A unique ID for the firewall.  **Returned:** success  **Sample:** `"12345678-abcd-1234-abcd-123456789abc"` |
| **firewall_name**  string | The name of the firewall.  **Returned:** success  **Sample:** `"ExampleFirewall"` |
| **firewall_policy_arn**  string | The ARN of the firewall policy used by the firewall.  **Returned:** success  **Sample:** `"arn:aws:network-firewall:us-east-1:123456789012:firewall-policy/ExamplePolicy"` |
| **firewall_policy_change_protection**  boolean | A flag indicating whether it is possible to change which firewall policy is used by the firewall.  **Returned:** success  **Sample:** `false` |
| **subnet_change_protection**  boolean | A flag indicating whether it is possible to change which subnets the firewall endpoints are in.  **Returned:** success  **Sample:** `true` |
| **subnet_mappings**  list / elements=dictionary | A list representing the subnets the firewall endpoints are in.  **Returned:** success |
| **subnet_id**  string | The ID of the subnet.  **Returned:** success  **Sample:** `"subnet-12345678"` |
| **subnets**  list / elements=string | A list of the subnets the firewall endpoints are in.  **Returned:** success  **Sample:** `["subnet-12345678", "subnet-87654321"]` |
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
