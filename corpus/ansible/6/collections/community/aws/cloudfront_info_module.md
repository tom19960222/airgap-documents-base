---
collection: ansible
version: "6"
title: "community.aws.cloudfront_info module – Obtain facts about an AWS CloudFront distribution"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/cloudfront_info_module.html
fetched_at: 2026-07-27T17:03:43+00:00
---
# community.aws.cloudfront_info module – Obtain facts about an AWS CloudFront distribution

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
> see [Requirements](cloudfront_info_module.md#ansible-collections-community-aws-cloudfront-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.cloudfront_info`.

New in community.aws 1.0.0

- [Synopsis](cloudfront_info_module.md#synopsis)
- [Requirements](cloudfront_info_module.md#requirements)
- [Parameters](cloudfront_info_module.md#parameters)
- [Notes](cloudfront_info_module.md#notes)
- [Examples](cloudfront_info_module.md#examples)
- [Return Values](cloudfront_info_module.md#return-values)

## [Synopsis](cloudfront_info_module.md#id1)

- Gets information about an AWS CloudFront distribution.

## [Requirements](cloudfront_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](cloudfront_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **all_lists**  boolean | Get all CloudFront lists that do not require parameters.  Choices:   - `false` ← (default) - `true` |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **distribution**  boolean | Get information about a distribution.  Requires *distribution_id* or *domain_name_alias* to be specified.  Choices:   - `false` ← (default) - `true` |
| **distribution_config**  boolean | Get the configuration information about a distribution.  Requires *distribution_id* or *domain_name_alias* to be specified.  Choices:   - `false` ← (default) - `true` |
| **distribution_id**  string | The id of the CloudFront distribution. Used with *distribution*, *distribution_config*, *invalidation*, *streaming_distribution*, *streaming_distribution_config*, *list_invalidations*. |
| **domain_name_alias**  string | Can be used instead of *distribution_id* - uses the aliased CNAME for the CloudFront distribution to get the distribution id where required. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **invalidation**  boolean | Get information about an invalidation.  Requires *invalidation_id* to be specified.  Choices:   - `false` ← (default) - `true` |
| **invalidation_id**  string | The id of the invalidation to get information about.  Used with *invalidation*. |
| **list_distributions**  boolean | Get a list of CloudFront distributions.  Choices:   - `false` ← (default) - `true` |
| **list_distributions_by_web_acl_id**  boolean | Get a list of distributions using web acl id as a filter.  Requires *web_acl_id* to be set.  Choices:   - `false` ← (default) - `true` |
| **list_invalidations**  boolean | Get a list of invalidations.  Requires *distribution_id* or *domain_name_alias* to be specified.  Choices:   - `false` ← (default) - `true` |
| **list_origin_access_identities**  boolean | Get a list of CloudFront origin access identities.  Requires *origin_access_identity_id* to be set.  Choices:   - `false` ← (default) - `true` |
| **list_streaming_distributions**  boolean | Get a list of streaming distributions.  Choices:   - `false` ← (default) - `true` |
| **origin_access_identity**  boolean | Get information about an origin access identity.  Requires *origin_access_identity_id* to be specified.  Choices:   - `false` ← (default) - `true` |
| **origin_access_identity_config**  boolean | Get the configuration information about an origin access identity.  Requires *origin_access_identity_id* to be specified.  Choices:   - `false` ← (default) - `true` |
| **origin_access_identity_id**  string | The id of the CloudFront origin access identity to get information about. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **streaming_distribution**  boolean | Get information about a specified RTMP distribution.  Requires *distribution_id* or *domain_name_alias* to be specified.  Choices:   - `false` ← (default) - `true` |
| **streaming_distribution_config**  boolean | Get the configuration information about a specified RTMP distribution.  Requires *distribution_id* or *domain_name_alias* to be specified.  Choices:   - `false` ← (default) - `true` |
| **summary**  boolean | Returns a summary of all distributions, streaming distributions and origin_access_identities.  This is the default behaviour if no option is selected.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](cloudfront_info_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](cloudfront_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Get a summary of distributions
  community.aws.cloudfront_info:
    summary: true
  register: result

- name: Get information about a distribution
  community.aws.cloudfront_info:
    distribution: true
    distribution_id: my-cloudfront-distribution-id
  register: result_did
- ansible.builtin.debug:
    msg: "{{ result_did['cloudfront']['my-cloudfront-distribution-id'] }}"

- name: Get information about a distribution using the CNAME of the cloudfront distribution.
  community.aws.cloudfront_info:
    distribution: true
    domain_name_alias: www.my-website.com
  register: result_website
- ansible.builtin.debug:
    msg: "{{ result_website['cloudfront']['www.my-website.com'] }}"

- name: Get all information about an invalidation for a distribution.
  community.aws.cloudfront_info:
    invalidation: true
    distribution_id: my-cloudfront-distribution-id
    invalidation_id: my-cloudfront-invalidation-id

- name: Get all information about a CloudFront origin access identity.
  community.aws.cloudfront_info:
    origin_access_identity: true
    origin_access_identity_id: my-cloudfront-origin-access-identity-id

- name: Get all information about lists not requiring parameters (ie. list_origin_access_identities, list_distributions, list_streaming_distributions)
  community.aws.cloudfront_info:
    origin_access_identity: true
    origin_access_identity_id: my-cloudfront-origin-access-identity-id

- name: Get all information about lists not requiring parameters (ie. list_origin_access_identities, list_distributions, list_streaming_distributions)
  community.aws.cloudfront_info:
    all_lists: true
```

## [Return Values](cloudfront_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **distribution**  dictionary | Facts about a CloudFront distribution. Requires *distribution_id* or *domain_name_alias* to be specified. Requires *origin_access_identity_id* to be set.  Returned: only if distribution is true |
| **distribution_config**  dictionary | Facts about a CloudFront distribution’s config. Requires *distribution_id* or *domain_name_alias* to be specified.  Returned: only if *distribution_config* is true |
| **invalidation**  dictionary | Describes the invalidation information for the distribution. Requires *invalidation_id* to be specified and either *distribution_id* or *domain_name_alias.*  Returned: only if invalidation is true |
| **origin_access_identity**  dictionary | Describes the origin access identity information. Requires *origin_access_identity_id* to be set.  Returned: only if *origin_access_identity* is true |
| **origin_access_identity_configuration**  dictionary | Describes the origin access identity information configuration information. Requires *origin_access_identity_id* to be set.  Returned: only if *origin_access_identity_configuration* is true |
| **result**  dictionary | Result dict not nested under the CloudFront ID to access results of module without the knowledge of that id as figuring out the DistributionId is usually the reason one uses this module in the first place.  Returned: always |
| **streaming_distribution**  dictionary | Describes the streaming information for the distribution. Requires *distribution_id* or *domain_name_alias* to be specified.  Returned: only if *streaming_distribution* is true |
| **streaming_distribution_config**  dictionary | Describes the streaming configuration information for the distribution. Requires *distribution_id* or *domain_name_alias* to be specified.  Returned: only if *streaming_distribution_config* is true |
| **summary**  dictionary | Gives a summary of distributions, streaming distributions and origin access identities.  Returned: as default or if summary is true |

### Authors

- Willem van Ketwich (@wilvk)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
