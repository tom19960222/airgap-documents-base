---
collection: ansible
version: "8"
title: "community.aws.accessanalyzer_validate_policy_info module – Performs validation of IAM policies"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/accessanalyzer_validate_policy_info_module.html
fetched_at: 2026-07-28T01:40:03+00:00
---
# community.aws.accessanalyzer_validate_policy_info module – Performs validation of IAM policies

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
> see [Requirements](accessanalyzer_validate_policy_info_module.md#ansible-collections-community-aws-accessanalyzer-validate-policy-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.accessanalyzer_validate_policy_info`.

New in community.aws 5.0.0

- [Synopsis](accessanalyzer_validate_policy_info_module.md#synopsis)
- [Requirements](accessanalyzer_validate_policy_info_module.md#requirements)
- [Parameters](accessanalyzer_validate_policy_info_module.md#parameters)
- [Notes](accessanalyzer_validate_policy_info_module.md#notes)
- [Examples](accessanalyzer_validate_policy_info_module.md#examples)
- [Return Values](accessanalyzer_validate_policy_info_module.md#return-values)

## [Synopsis](accessanalyzer_validate_policy_info_module.md#id1)

- Requests the validation of a policy and returns a list of findings.

## [Requirements](accessanalyzer_validate_policy_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](accessanalyzer_validate_policy_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **locale**  string | The locale to use for localizing the findings.  Supported locales include `DE`, `EN`, `ES`, `FR`, `IT`, `JA`, `KO`, `PT_BR`, `ZH_CN` and `ZH_TW`.  For more information about supported locales see the AWS Documentation `https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ValidatePolicy.html`  **Default:** `"EN"` |
| **policy**  aliases: policy_document  json / required | A properly json formatted policy. |
| **policy_type**  string | The type of policy to validate.  `identity` policies grant permissions to IAM principals, including both managed and inline policies for IAM roles, users, and groups.  `resource` policies policies grant permissions on AWS resources, including trust policies for IAM roles and bucket policies for S3 buckets.  **Choices:**   - `"identity"` ← (default) - `"resource"` - `"service_control"` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **resource_type**  string | The type of resource to attach to your resource policy.  Ignored unless *policy_type=resource*.  Supported resource types include `AWS::S3::Bucket`, `AWS::S3::AccessPoint`, `AWS::S3::MultiRegionAccessPoint` and `AWS::S3ObjectLambda::AccessPoint`  For resource types not supported as valid values, IAM Access Analyzer runs policy checks that apply to all resource policies.  For more information about supported locales see the AWS Documentation `https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ValidatePolicy.html` |
| **results_filter**  list / elements=string | Filter the findings and limit them to specific finding types.  **Choices:**   - `"error"` - `"security"` - `"suggestion"` - `"warning"` |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](accessanalyzer_validate_policy_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](accessanalyzer_validate_policy_info_module.md#id5)

```yaml+jinja
# Validate a policy
- name: Validate a simple IAM policy
  community.aws.accessanalyzer_validate_policy_info:
    policy: "{{ lookup('template', 'managed_policy.json.j2') }}"
```

## [Return Values](accessanalyzer_validate_policy_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **findings**  list / elements=dictionary | The list of findings in a policy returned by IAM Access Analyzer based on its suite of policy checks.  **Returned:** success |
| **finding_details**  string | A localized message describing the finding.  **Returned:** success  **Sample:** `"Resource ARN does not match the expected ARN format. Update the resource portion of the ARN."` |
| **finding_type**  string | The severity of the finding.  **Returned:** success  **Sample:** `"ERROR"` |
| **issue_code**  string | An identifier for the type of issue found.  **Returned:** success  **Sample:** `"INVALID_ARN_RESOURCE"` |
| **learn_more_link**  string | A link to additional information about the finding type.  **Returned:** success  **Sample:** `"https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-reference-policy-checks.html"` |
| **locations**  list / elements=dictionary | The location of the item resulting in the recommendations.  **Returned:** success |
| **path**  list / elements=dictionary | A path in a policy, represented as a sequence of path elements.  **Returned:** success  **Sample:** `[{"value": "Statement"}, {"index": 0}, {"value": "Resource"}, {"index": 0}]` |
| **span**  dictionary | Where in the policy the finding refers to.  Note - when using lookups or passing dictionaries to *policy* the policy string may be converted to a single line of JSON, changing th column, line and offset values.  **Returned:** success |
| **end**  dictionary | The end position of the span.  **Returned:** success |
| **column**  integer | The column of the position, starting from `0`.  **Returned:** success |
| **line**  integer | The line of the position, starting from `1`.  **Returned:** success |
| **offset**  integer | The offset within the policy that corresponds to the position, starting from `0`.  **Returned:** success |
| **start**  dictionary | The start position of the span.  **Returned:** success |
| **column**  integer | The column of the position, starting from `0`.  **Returned:** success |
| **line**  integer | The line of the position, starting from `1`.  **Returned:** success |
| **offset**  integer | The offset within the policy that corresponds to the position, starting from `0`.  **Returned:** success |

### Authors

- Mark Chappell (@tremble)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
