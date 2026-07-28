---
collection: ansible
version: "6"
title: "community.aws.aws_waf_rule module – Create and delete WAF Rules"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/aws_waf_rule_module.html
fetched_at: 2026-07-27T17:03:39+00:00
---
# community.aws.aws_waf_rule module – Create and delete WAF Rules

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
> see [Requirements](aws_waf_rule_module.md#ansible-collections-community-aws-aws-waf-rule-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.aws_waf_rule`.

New in community.aws 1.0.0

- [Synopsis](aws_waf_rule_module.md#synopsis)
- [Requirements](aws_waf_rule_module.md#requirements)
- [Parameters](aws_waf_rule_module.md#parameters)
- [Notes](aws_waf_rule_module.md#notes)
- [Examples](aws_waf_rule_module.md#examples)
- [Return Values](aws_waf_rule_module.md#return-values)

## [Synopsis](aws_waf_rule_module.md#id1)

- Read the AWS documentation for WAF <https://aws.amazon.com/documentation/waf/>.

## [Requirements](aws_waf_rule_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](aws_waf_rule_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **conditions**  list / elements=dictionary | List of conditions used in the rule. [community.aws.aws_waf_condition](aws_waf_condition_module.md#ansible-collections-community-aws-aws-waf-condition-module) can be used to create new conditions. |
| **condition**  string / required | The name of the condition. The condition must already exist. |
| **negated**  boolean / required | Whether the condition should be negated.  Choices:   - `false` - `true` |
| **type**  string / required | The type of rule to match.  Choices:   - `"byte"` - `"geo"` - `"ip"` - `"size"` - `"sql"` - `"xss"` |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **metric_name**  string | A friendly name or description for the metrics for the rule.  The name can contain only alphanumeric characters (A-Z, a-z, 0-9); the name can’t contain whitespace.  You can’t change *metric_name* after you create the rule.  Defaults to the same as *name* with disallowed characters removed. |
| **name**  string / required | Name of the Web Application Firewall rule. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_conditions**  boolean | Whether or not to remove conditions that are not passed when updating *conditions*.  Choices:   - `false` ← (default) - `true` |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Whether the rule should be present or absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **waf_regional**  boolean | Whether to use waf-regional module.  Choices:   - `false` ← (default) - `true` |

## [Notes](aws_waf_rule_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](aws_waf_rule_module.md#id5)

```yaml+jinja
- name: create WAF rule
  community.aws.aws_waf_rule:
    name: my_waf_rule
    conditions:
      - name: my_regex_condition
        type: regex
        negated: no
      - name: my_geo_condition
        type: geo
        negated: no
      - name: my_byte_condition
        type: byte
        negated: yes

- name: remove WAF rule
  community.aws.aws_waf_rule:
    name: "my_waf_rule"
    state: absent
```

## [Return Values](aws_waf_rule_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **rule**  complex | WAF rule contents  Returned: always |
| **metric_name**  string | Metric name for the rule.  Returned: always  Sample: `"ansibletest1234rule"` |
| **name**  string | Friendly name for the rule.  Returned: always  Sample: `"ansible-test-1234_rule"` |
| **predicates**  complex | List of conditions used in the rule.  Returned: always |
| **data_id**  string | ID of the condition.  Returned: always  Sample: `"8251acdb-526c-42a8-92bc-d3d13e584166"` |
| **negated**  boolean | Whether the sense of the condition is negated.  Returned: always  Sample: `false` |
| **type**  string | type of the condition.  Returned: always  Sample: `"ByteMatch"` |
| **rule_id**  string | ID of the WAF rule.  Returned: always  Sample: `"15de0cbc-9204-4e1f-90e6-69b2f415c261"` |

### Authors

- Mike Mochan (@mmochan)
- Will Thames (@willthames)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
