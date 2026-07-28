---
collection: ansible
version: "8"
title: "community.aws.networkfirewall_rule_group_info module – describe AWS Network Firewall rule groups"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/networkfirewall_rule_group_info_module.html
fetched_at: 2026-07-28T01:41:40+00:00
---
# community.aws.networkfirewall_rule_group_info module – describe AWS Network Firewall rule groups

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
> see [Requirements](networkfirewall_rule_group_info_module.md#ansible-collections-community-aws-networkfirewall-rule-group-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.networkfirewall_rule_group_info`.

New in community.aws 4.0.0

- [Synopsis](networkfirewall_rule_group_info_module.md#synopsis)
- [Requirements](networkfirewall_rule_group_info_module.md#requirements)
- [Parameters](networkfirewall_rule_group_info_module.md#parameters)
- [Notes](networkfirewall_rule_group_info_module.md#notes)
- [Examples](networkfirewall_rule_group_info_module.md#examples)
- [Return Values](networkfirewall_rule_group_info_module.md#return-values)

## [Synopsis](networkfirewall_rule_group_info_module.md#id1)

- A module for describing AWS Network Firewall rule groups.

## [Requirements](networkfirewall_rule_group_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](networkfirewall_rule_group_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **arn**  string | The ARN of the Network Firewall rule group.  At time of writing AWS does not support describing Managed Rules. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **name**  string | The name of the Network Firewall rule group. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **rule_type**  aliases: type  string | Indicates whether the rule group is stateless or stateful.  Required if *name* is provided.  **Choices:**   - `"stateful"` - `"stateless"` |
| **scope**  string | The scope of the request.  When *scope=’account’* returns a description of all rule groups in the account.  When *scope=’managed’* returns a list of available managed rule group arns.  By default searches only at the account scope.  *scope=’managed’* requires botocore>=1.23.23.  **Choices:**   - `"managed"` - `"account"` |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](networkfirewall_rule_group_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](networkfirewall_rule_group_info_module.md#id5)

```yaml+jinja
# Describe all Rule Groups in an account (excludes managed groups)
- community.aws.networkfirewall_rule_group_info: {}

# List the available Managed Rule groups (AWS doesn't support describing the
# groups)
- community.aws.networkfirewall_rule_group_info:
    scope: managed

# Describe a Rule Group by ARN
- community.aws.networkfirewall_rule_group_info:
    arn: arn:aws:network-firewall:us-east-1:123456789012:stateful-rulegroup/ExampleRuleGroup

# Describe a Rule Group by name
- community.aws.networkfirewall_rule_group_info:
    name: ExampleRuleGroup
    type: stateful
```

## [Return Values](networkfirewall_rule_group_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **rule_groups**  list / elements=dictionary | The details of the rule groups  **Returned:** success |
| **rule_group**  dictionary | Details of the rules in the rule group  **Returned:** success |
| **rule_variables**  complex | Settings that are available for use in the rules in the rule group.  **Returned:** When rule variables are attached to the rule group. |
| **ip_sets**  dictionary | A dictionary mapping variable names to IP addresses in CIDR format.  **Returned:** success  **Sample:** `["192.0.2.0/24"]` |
| **port_sets**  dictionary | A dictionary mapping variable names to ports  **Returned:** success  **Sample:** `["42"]` |
| **rules_source**  dictionary | DEFAULT_ACTION_ORDER  **Returned:** success |
| **rules_source_list**  dictionary | A description of the criteria for a domain list rule group.  **Returned:** When the rule group is “domain list” based. |
| **generated_rules_type**  string | Whether the rule group allows or denies access to the domains in the list.  **Returned:** success  **Sample:** `"ALLOWLIST"` |
| **target_types**  list / elements=string | The protocols to be inspected by the rule group.  **Returned:** success  **Sample:** `["TLS_SNI", "HTTP_HOST"]` |
| **targets**  list / elements=string | A list of domain names to be inspected for.  **Returned:** success  **Sample:** `["abc.example.com", ".example.net"]` |
| **rules_string**  string | A string describing the rules that the rule group is comprised of.  **Returned:** When the rule group is “rules string” based. |
| **stateful_rules**  list / elements=dictionary | A list of dictionaries describing the rules that the rule group is comprised of.  **Returned:** When the rule group is “rules list” based. |
| **action**  string | What action to perform when a flow matches the rule criteria.  **Returned:** success  **Sample:** `"PASS"` |
| **header**  dictionary | A description of the criteria used for the rule.  **Returned:** success |
| **destination**  string | The destination address or range of addresses to inspect for.  **Returned:** success  **Sample:** `"198.51.100.0/24"` |
| **destination_port**  string | The destination port to inspect for.  **Returned:** success  **Sample:** `"6666:6667"` |
| **direction**  string | The direction of traffic flow to inspect.  **Returned:** success  **Sample:** `"FORWARD"` |
| **protocol**  string | The protocol to inspect for.  **Returned:** success  **Sample:** `"IP"` |
| **source**  string | The source address or range of addresses to inspect for.  **Returned:** success  **Sample:** `"203.0.113.98"` |
| **source_port**  string | The source port to inspect for.  **Returned:** success  **Sample:** `"42"` |
| **rule_options**  list / elements=dictionary | Additional Suricata RuleOptions settings for the rule.  **Returned:** success |
| **keyword**  string | The keyword for the setting.  **Returned:** success  **Sample:** `"sid:1"` |
| **settings**  list / elements=string | A list of values passed to the setting.  **Returned:** When values are available |
| **stateless_rules_and_custom_actions**  dictionary | A description of the criteria for a stateless rule group.  **Returned:** When the rule group is a stateless rule group. |
| **custom_actions**  list / elements=dictionary | A list of individual custom action definitions that are available for use in stateless rules.  **Returned:** success |
| **action_definition**  dictionary | The custom action associated with the action name.  **Returned:** success |
| **publish_metric_action**  dictionary | The description of an action which publishes to CloudWatch.  **Returned:** When the action publishes to CloudWatch. |
| **dimensions**  list / elements=dictionary | The value to use in an Amazon CloudWatch custom metric dimension.  **Returned:** success |
| **value**  string | The value to use in the custom metric dimension.  **Returned:** success |
| **action_name**  string | The name for the custom action.  **Returned:** success |
| **stateless_rules**  list / elements=dictionary | A list of stateless rules for use in a stateless rule group.  **Returned:** success |
| **priority**  integer | Indicates the order in which to run this rule relative to all of the rules that are defined for a stateless rule group.  **Returned:** success |
| **rule_definition**  dictionary | Describes the stateless 5-tuple inspection criteria and actions for the rule.  **Returned:** success |
| **actions**  list / elements=string | The actions to take when a flow matches the rule.  **Returned:** success  **Sample:** `["aws:pass", "CustomActionName"]` |
| **match_attributes**  dictionary | Describes the stateless 5-tuple inspection criteria for the rule.  **Returned:** success |
| **destination_ports**  list / elements=dictionary | The destination port ranges to inspect for.  **Returned:** success |
| **from_port**  integer | The lower limit of the port range.  **Returned:** success |
| **to_port**  integer | The upper limit of the port range.  **Returned:** success |
| **destinations**  list / elements=dictionary | The destination IP addresses and address ranges to inspect for.  **Returned:** success |
| **address_definition**  string | An IP address or a block of IP addresses in CIDR notation.  **Returned:** success  **Sample:** `"192.0.2.3"` |
| **protocols**  list / elements=integer | The IANA protocol numbers of the protocols to inspect for.  **Returned:** success  **Sample:** `[6]` |
| **source_ports**  list / elements=dictionary | The source port ranges to inspect for.  **Returned:** success |
| **from_port**  integer | The lower limit of the port range.  **Returned:** success |
| **to_port**  integer | The upper limit of the port range.  **Returned:** success |
| **sources**  list / elements=dictionary | The source IP addresses and address ranges to inspect for.  **Returned:** success |
| **address_definition**  string | An IP address or a block of IP addresses in CIDR notation.  **Returned:** success  **Sample:** `"192.0.2.3"` |
| **tcp_flags**  list / elements=dictionary | The TCP flags and masks to inspect for.  **Returned:** success |
| **flags**  list / elements=string | Used with masks to define the TCP flags that flows are inspected for.  **Returned:** success |
| **masks**  list / elements=string | The set of flags considered during inspection.  **Returned:** success |
| **stateful_rule_options**  dictionary | Additional options governing how Network Firewall handles stateful rules.  **Returned:** When the rule group is either “rules string” or “rules list” based. |
| **rule_order**  string | The order in which rules will be evaluated.  **Returned:** success  **Sample:** `"DEFAULT_ACTION_ORDER"` |
| **rule_group_metadata**  dictionary | Details of the rules in the rule group  **Returned:** success |
| **capacity**  integer | The maximum operating resources that this rule group can use.  **Returned:** success |
| **consumed_capacity**  integer | The number of capacity units currently consumed by the rule group rules.  **Returned:** success |
| **description**  string | A description of the rule group.  **Returned:** success |
| **number_of_associations**  integer | The number of firewall policies that use this rule group.  **Returned:** success |
| **rule_group_arn**  integer | The ARN for the rule group  **Returned:** success  **Sample:** `"arn:aws:network-firewall:us-east-1:123456789012:stateful-rulegroup/ExampleGroup"` |
| **rule_group_id**  integer | A unique identifier for the rule group.  **Returned:** success  **Sample:** `"12345678-abcd-1234-abcd-123456789abc"` |
| **rule_group_name**  string | The name of the rule group.  **Returned:** success |
| **rule_group_status**  string | The current status of a rule group.  **Returned:** success  **Sample:** `"DELETING"` |
| **tags**  dictionary | A dictionary representing the tags associated with the rule group.  **Returned:** success |
| **type**  string | Whether the rule group is stateless or stateful.  **Returned:** success  **Sample:** `"STATEFUL"` |
| **rule_list**  list / elements=string | A list of ARNs of the matching rule groups.  **Returned:** When a rule name isn’t specified |

### Authors

- Mark Chappell (@tremble)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
