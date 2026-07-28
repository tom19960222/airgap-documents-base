---
collection: ansible
version: "8"
title: "community.aws.waf_rule module – Create and delete WAF Rules"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/waf_rule_module.html
fetched_at: 2026-07-28T01:42:07+00:00
---
# community.aws.waf_rule module – Create and delete WAF Rules

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
> see [Requirements](waf_rule_module.md#ansible-collections-community-aws-waf-rule-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.waf_rule`.

New in community.aws 1.0.0

- [Synopsis](waf_rule_module.md#synopsis)
- [Requirements](waf_rule_module.md#requirements)
- [Parameters](waf_rule_module.md#parameters)
- [Notes](waf_rule_module.md#notes)
- [Examples](waf_rule_module.md#examples)
- [Return Values](waf_rule_module.md#return-values)

## [Synopsis](waf_rule_module.md#id1)

- Read the AWS documentation for WAF <https://aws.amazon.com/documentation/waf/>.
- Prior to release 5.0.0 this module was called `community.aws.aws_waf_rule`. The usage did not change.

Aliases: aws_waf_rule

## [Requirements](waf_rule_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](waf_rule_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **conditions**  list / elements=dictionary | List of conditions used in the rule. [community.aws.waf_condition](waf_condition_module.md#ansible-collections-community-aws-waf-condition-module) can be used to create new conditions. |
| **condition**  string / required | The name of the condition. The condition must already exist. |
| **negated**  boolean / required | Whether the condition should be negated.  **Choices:**   - `false` - `true` |
| **type**  string / required | The type of rule to match.  **Choices:**   - `"byte"` - `"geo"` - `"ip"` - `"size"` - `"sql"` - `"xss"` |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **metric_name**  string | A friendly name or description for the metrics for the rule.  The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name may not contain whitespace.  You can’t change *metric_name* after you create the rule.  Defaults to the same as *name* with disallowed characters removed. |
| **name**  string / required | Name of the Web Application Firewall rule. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_conditions**  boolean | Whether or not to remove conditions that are not passed when updating *conditions*.  **Choices:**   - `false` ← (default) - `true` |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Whether the rule should be present or absent.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **waf_regional**  boolean | Whether to use `waf-regional` module.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](waf_rule_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](waf_rule_module.md#id5)

```yaml+jinja
- name: create WAF rule
  community.aws.waf_rule:
    name: my_waf_rule
    conditions:
      - name: my_regex_condition
        type: regex
        negated: false
      - name: my_geo_condition
        type: geo
        negated: false
      - name: my_byte_condition
        type: byte
        negated: true

- name: remove WAF rule
  community.aws.waf_rule:
    name: "my_waf_rule"
    state: absent
```

## [Return Values](waf_rule_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **rule**  complex | WAF rule contents  **Returned:** always |
| **metric_name**  string | Metric name for the rule.  **Returned:** always  **Sample:** `"ansibletest1234rule"` |
| **name**  string | Friendly name for the rule.  **Returned:** always  **Sample:** `"ansible-test-1234_rule"` |
| **predicates**  complex | List of conditions used in the rule.  **Returned:** always |
| **data_id**  string | ID of the condition.  **Returned:** always  **Sample:** `"8251acdb-526c-42a8-92bc-d3d13e584166"` |
| **negated**  boolean | Whether the sense of the condition is negated.  **Returned:** always  **Sample:** `false` |
| **type**  string | type of the condition.  **Returned:** always  **Sample:** `"ByteMatch"` |
| **rule_id**  string | ID of the WAF rule.  **Returned:** always  **Sample:** `"15de0cbc-9204-4e1f-90e6-69b2f415c261"` |

### Authors

- Mike Mochan (@mmochan)
- Will Thames (@willthames)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
