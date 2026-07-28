---
collection: ansible
version: "8"
title: "community.aws.networkfirewall_policy_info module – describe AWS Network Firewall policies"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/networkfirewall_policy_info_module.html
fetched_at: 2026-07-28T01:41:39+00:00
---
# community.aws.networkfirewall_policy_info module – describe AWS Network Firewall policies

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
> see [Requirements](networkfirewall_policy_info_module.md#ansible-collections-community-aws-networkfirewall-policy-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.networkfirewall_policy_info`.

New in community.aws 4.0.0

- [Synopsis](networkfirewall_policy_info_module.md#synopsis)
- [Requirements](networkfirewall_policy_info_module.md#requirements)
- [Parameters](networkfirewall_policy_info_module.md#parameters)
- [Notes](networkfirewall_policy_info_module.md#notes)
- [Examples](networkfirewall_policy_info_module.md#examples)
- [Return Values](networkfirewall_policy_info_module.md#return-values)

## [Synopsis](networkfirewall_policy_info_module.md#id1)

- A module for describing AWS Network Firewall policies.

## [Requirements](networkfirewall_policy_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](networkfirewall_policy_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **arn**  string | The ARN of the Network Firewall policy.  Mutually exclusive with *name*. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **name**  string | The name of the Network Firewall policy.  Mutually exclusive with *arn*. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](networkfirewall_policy_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](networkfirewall_policy_info_module.md#id5)

```yaml+jinja
# Describe all Firewall policies in an account
- community.aws.networkfirewall_policy_info: {}

# Describe a Firewall policy by ARN
- community.aws.networkfirewall_policy_info:
    arn: arn:aws:network-firewall:us-east-1:123456789012:firewall-policy/ExamplePolicy

# Describe a Firewall policy by name
- community.aws.networkfirewall_policy_info:
    name: ExamplePolicy
```

## [Return Values](networkfirewall_policy_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **policies**  list / elements=dictionary | The details of the policies  **Returned:** success |
| **policy**  dictionary | The details of the policy  **Returned:** success |
| **stateful_engine_options**  dictionary | Extra options describing how the stateful rules should be handled.  **Returned:** success |
| **rule_order**  string | How rule group evaluation will be ordered.  For more information on rule evaluation ordering see the AWS documentation <https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-rule-evaluation-order.html>.  **Returned:** success  **Sample:** `"DEFAULT_ACTION_ORDER"` |
| **stateful_rule_group_references**  list / elements=dictionary | Information about the stateful rule groups attached to the policy.  **Returned:** success |
| **priority**  integer | An integer that indicates the order in which to run the stateful rule groups in a single policy.  This only applies to policies that specify the STRICT_ORDER rule order in the stateful engine options settings.  **Returned:** success  **Sample:** `1234` |
| **resource_arn**  string | The ARN of the rule group.  **Returned:** success  **Sample:** `"arn:aws:network-firewall:us-east-1:aws-managed:stateful-rulegroup/AbusedLegitMalwareDomainsActionOrder"` |
| **stateless_custom_actions**  list / elements=dictionary | A description of additional custom actions available for use as default rules to apply to stateless packets.  **Returned:** success |
| **action_definition**  dictionary | The action to perform.  **Returned:** success |
| **publish_metric_action**  dictionary | Definition of a custom metric to be published to CloudWatch.  <https://docs.aws.amazon.com/network-firewall/latest/developerguide/monitoring-cloudwatch.html>  **Returned:** success |
| **dimensions**  list / elements=dictionary | The values of the CustomAction dimension to set on the metrics.  The dimensions of a metric are used to identify unique streams of data.  **Returned:** success |
| **value**  string | A value of the CustomAction dimension to set on the metrics.  **Returned:** success  **Sample:** `"ExampleRule"` |
| **action_name**  string | A name for the action.  **Returned:** success  **Sample:** `"ExampleAction"` |
| **stateless_default_actions**  list / elements=string | The default actions to take on a packet that doesn’t match any stateful rules.  **Returned:** success  **Sample:** `["aws:alert_strict"]` |
| **stateless_fragment_default_actions**  list / elements=string | The actions to take on a packet if it doesn’t match any of the stateless rules in the policy.  **Returned:** success  **Sample:** `["aws:pass"]` |
| **stateless_rule_group_references**  list / elements=dictionary | Information about the stateful rule groups attached to the policy.  **Returned:** success |
| **priority**  string | An integer that indicates the order in which to run the stateless rule groups in a single policy.  **Returned:** success  **Sample:** `"12345"` |
| **resource_arn**  string | The ARN of the rule group.  **Returned:** success  **Sample:** `"arn:aws:network-firewall:us-east-1:123456789012:stateless-rulegroup/ExampleGroup"` |
| **policy_metadata**  dictionary | Metadata about the policy  **Returned:** success |
| **consumed_stateful_rule_capacity**  integer | The total number of capacity units used by the stateful rule groups.  **Returned:** success  **Sample:** `165` |
| **consumed_stateless_rule_capacity**  integer | The total number of capacity units used by the stateless rule groups.  **Returned:** success  **Sample:** `2010` |
| **firewall_policy_arn**  string | The ARN of the policy.  **Returned:** success  **Sample:** `"arn:aws:network-firewall:us-east-1:123456789012:firewall-policy/ExamplePolicy"` |
| **firewall_policy_id**  string | The unique ID of the policy.  **Returned:** success  **Sample:** `"12345678-abcd-1234-5678-123456789abc"` |
| **firewall_policy_name**  string | The name of the policy.  **Returned:** success  **Sample:** `"ExamplePolicy"` |
| **firewall_policy_status**  string | The current status of the policy.  **Returned:** success  **Sample:** `"ACTIVE"` |
| **number_of_associations**  integer | The number of firewalls the policy is associated to.  **Returned:** success  **Sample:** `1` |
| **tags**  dictionary | A dictionary representing the tags associated with the policy.  **Returned:** success  **Sample:** `{"tagName": "Some Value"}` |
| **policy_list**  list / elements=string | A list of ARNs of the matching policies.  **Returned:** When a policy name isn’t specified  **Sample:** `["arn:aws:network-firewall:us-east-1:123456789012:firewall-policy/Example1", "arn:aws:network-firewall:us-east-1:123456789012:firewall-policy/Example2"]` |

### Authors

- Mark Chappell (@tremble)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
