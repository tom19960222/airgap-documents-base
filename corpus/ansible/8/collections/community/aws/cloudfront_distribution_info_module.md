---
collection: ansible
version: "8"
title: "community.aws.cloudfront_distribution_info module – Obtain facts about an AWS CloudFront distribution"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/cloudfront_distribution_info_module.html
fetched_at: 2026-07-28T01:40:21+00:00
---
# community.aws.cloudfront_distribution_info module – Obtain facts about an AWS CloudFront distribution

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
> see [Requirements](cloudfront_distribution_info_module.md#ansible-collections-community-aws-cloudfront-distribution-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.cloudfront_distribution_info`.

New in community.aws 1.0.0

- [Synopsis](cloudfront_distribution_info_module.md#synopsis)
- [Requirements](cloudfront_distribution_info_module.md#requirements)
- [Parameters](cloudfront_distribution_info_module.md#parameters)
- [Notes](cloudfront_distribution_info_module.md#notes)
- [Examples](cloudfront_distribution_info_module.md#examples)
- [Return Values](cloudfront_distribution_info_module.md#return-values)

## [Synopsis](cloudfront_distribution_info_module.md#id1)

- Gets information about an AWS CloudFront distribution.
- Prior to release 5.0.0 this module was called `community.aws.cloudfront_info`. The usage did not change.

Aliases: cloudfront_info

## [Requirements](cloudfront_distribution_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](cloudfront_distribution_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **all_lists**  boolean | Get all CloudFront lists that do not require parameters.  **Choices:**   - `false` ← (default) - `true` |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **distribution**  boolean | Get information about a distribution.  Requires *distribution_id* or *domain_name_alias* to be specified.  **Choices:**   - `false` ← (default) - `true` |
| **distribution_config**  boolean | Get the configuration information about a distribution.  Requires *distribution_id* or *domain_name_alias* to be specified.  **Choices:**   - `false` ← (default) - `true` |
| **distribution_id**  string | The id of the CloudFront distribution. Used with *distribution*, *distribution_config*, *invalidation*, *streaming_distribution*, *streaming_distribution_config*, *list_invalidations*. |
| **domain_name_alias**  string | Can be used instead of *distribution_id* - uses the aliased CNAME for the CloudFront distribution to get the distribution id where required. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **invalidation**  boolean | Get information about an invalidation.  Requires *invalidation_id* to be specified.  **Choices:**   - `false` ← (default) - `true` |
| **invalidation_id**  string | The id of the invalidation to get information about.  Used with *invalidation*. |
| **list_distributions**  boolean | Get a list of CloudFront distributions.  **Choices:**   - `false` ← (default) - `true` |
| **list_distributions_by_web_acl_id**  boolean | Get a list of distributions using web acl id as a filter.  Requires *web_acl_id* to be set.  **Choices:**   - `false` ← (default) - `true` |
| **list_invalidations**  boolean | Get a list of invalidations.  Requires *distribution_id* or *domain_name_alias* to be specified.  **Choices:**   - `false` ← (default) - `true` |
| **list_origin_access_identities**  boolean | Get a list of CloudFront origin access identities.  Requires *origin_access_identity_id* to be set.  **Choices:**   - `false` ← (default) - `true` |
| **list_streaming_distributions**  boolean | Get a list of streaming distributions.  **Choices:**   - `false` ← (default) - `true` |
| **origin_access_identity**  boolean | Get information about an origin access identity.  Requires *origin_access_identity_id* to be specified.  **Choices:**   - `false` ← (default) - `true` |
| **origin_access_identity_config**  boolean | Get the configuration information about an origin access identity.  Requires *origin_access_identity_id* to be specified.  **Choices:**   - `false` ← (default) - `true` |
| **origin_access_identity_id**  string | The id of the CloudFront origin access identity to get information about. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **streaming_distribution**  boolean | Get information about a specified RTMP distribution.  Requires *distribution_id* or *domain_name_alias* to be specified.  **Choices:**   - `false` ← (default) - `true` |
| **streaming_distribution_config**  boolean | Get the configuration information about a specified RTMP distribution.  Requires *distribution_id* or *domain_name_alias* to be specified.  **Choices:**   - `false` ← (default) - `true` |
| **summary**  boolean | Returns a summary of all distributions, streaming distributions and origin_access_identities.  This is the default behaviour if no option is selected.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](cloudfront_distribution_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](cloudfront_distribution_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Get a summary of distributions
  community.aws.cloudfront_distribution_info:
    summary: true
  register: result

- name: Get information about a distribution
  community.aws.cloudfront_distribution_info:
    distribution: true
    distribution_id: my-cloudfront-distribution-id
  register: result_did
- ansible.builtin.debug:
    msg: "{{ result_did['cloudfront']['my-cloudfront-distribution-id'] }}"

- name: Get information about a distribution using the CNAME of the cloudfront distribution.
  community.aws.cloudfront_distribution_info:
    distribution: true
    domain_name_alias: www.my-website.com
  register: result_website
- ansible.builtin.debug:
    msg: "{{ result_website['cloudfront']['www.my-website.com'] }}"

- name: Get all information about an invalidation for a distribution.
  community.aws.cloudfront_distribution_info:
    invalidation: true
    distribution_id: my-cloudfront-distribution-id
    invalidation_id: my-cloudfront-invalidation-id

- name: Get all information about a CloudFront origin access identity.
  community.aws.cloudfront_distribution_info:
    origin_access_identity: true
    origin_access_identity_id: my-cloudfront-origin-access-identity-id

- name: Get all information about lists not requiring parameters (ie. list_origin_access_identities, list_distributions, list_streaming_distributions)
  community.aws.cloudfront_distribution_info:
    origin_access_identity: true
    origin_access_identity_id: my-cloudfront-origin-access-identity-id

- name: Get all information about lists not requiring parameters (ie. list_origin_access_identities, list_distributions, list_streaming_distributions)
  community.aws.cloudfront_distribution_info:
    all_lists: true
```

## [Return Values](cloudfront_distribution_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **distribution**  dictionary | Facts about a CloudFront distribution. Requires *distribution_id* or *domain_name_alias* to be specified. Requires *origin_access_identity_id* to be set.  **Returned:** only if distribution is true |
| **distribution_config**  dictionary | Facts about a CloudFront distribution’s config. Requires *distribution_id* or *domain_name_alias* to be specified.  **Returned:** only if *distribution_config* is true |
| **invalidation**  dictionary | Describes the invalidation information for the distribution. Requires *invalidation_id* to be specified and either *distribution_id* or *domain_name_alias.*  **Returned:** only if invalidation is true |
| **origin_access_identity**  dictionary | Describes the origin access identity information. Requires *origin_access_identity_id* to be set.  **Returned:** only if *origin_access_identity* is true |
| **origin_access_identity_configuration**  dictionary | Describes the origin access identity information configuration information. Requires *origin_access_identity_id* to be set.  **Returned:** only if *origin_access_identity_configuration* is true |
| **result**  dictionary | Result dict not nested under the CloudFront ID to access results of module without the knowledge of that id as figuring out the DistributionId is usually the reason one uses this module in the first place.  **Returned:** always |
| **streaming_distribution**  dictionary | Describes the streaming information for the distribution. Requires *distribution_id* or *domain_name_alias* to be specified.  **Returned:** only if *streaming_distribution* is true |
| **streaming_distribution_config**  dictionary | Describes the streaming configuration information for the distribution. Requires *distribution_id* or *domain_name_alias* to be specified.  **Returned:** only if *streaming_distribution_config* is true |
| **summary**  dictionary | Gives a summary of distributions, streaming distributions and origin access identities.  **Returned:** as default or if summary is true |

### Authors

- Willem van Ketwich (@wilvk)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
