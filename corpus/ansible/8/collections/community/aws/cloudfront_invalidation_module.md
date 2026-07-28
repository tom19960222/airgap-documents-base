---
collection: ansible
version: "8"
title: "community.aws.cloudfront_invalidation module – create invalidations for AWS CloudFront distributions"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/cloudfront_invalidation_module.html
fetched_at: 2026-07-28T01:40:22+00:00
---
# community.aws.cloudfront_invalidation module – create invalidations for AWS CloudFront distributions

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
> see [Requirements](cloudfront_invalidation_module.md#ansible-collections-community-aws-cloudfront-invalidation-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.cloudfront_invalidation`.

New in community.aws 1.0.0

- [Synopsis](cloudfront_invalidation_module.md#synopsis)
- [Requirements](cloudfront_invalidation_module.md#requirements)
- [Parameters](cloudfront_invalidation_module.md#parameters)
- [Notes](cloudfront_invalidation_module.md#notes)
- [Examples](cloudfront_invalidation_module.md#examples)
- [Return Values](cloudfront_invalidation_module.md#return-values)

## [Synopsis](cloudfront_invalidation_module.md#id1)

- Allows for invalidation of a batch of paths for a CloudFront distribution.

## [Requirements](cloudfront_invalidation_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](cloudfront_invalidation_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **alias**  string | The alias of the CloudFront distribution to invalidate paths for. Can be specified instead of distribution_id. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **caller_reference**  string | A unique reference identifier for the invalidation paths.  Defaults to current datetime stamp. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **distribution_id**  string | The ID of the CloudFront distribution to invalidate paths for. Can be specified instead of the alias. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **target_paths**  list / elements=string / required | A list of paths on the distribution to invalidate. Each path should begin with `/`. Wildcards are allowed. eg. `/foo/bar/*` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](cloudfront_invalidation_module.md#id4)

> **Note:**
>
> - does not support check mode
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](cloudfront_invalidation_module.md#id5)

```yaml+jinja
- name: create a batch of invalidations using a distribution_id for a reference
  community.aws.cloudfront_invalidation:
    distribution_id: E15BU8SDCGSG57
    caller_reference: testing 123
    target_paths:
      - /testpathone/test1.css
      - /testpathtwo/test2.js
      - /testpaththree/test3.ss

- name: create a batch of invalidations using an alias as a reference and one path using a wildcard match
  community.aws.cloudfront_invalidation:
    alias: alias.test.com
    caller_reference: testing 123
    target_paths:
      - /testpathone/test4.css
      - /testpathtwo/test5.js
      - /testpaththree/*
```

## [Return Values](cloudfront_invalidation_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **invalidation**  complex | The invalidation’s information.  **Returned:** always |
| **create_time**  string | The date and time the invalidation request was first made.  **Returned:** always  **Sample:** `"2018-02-01T15:50:41.159000+00:00"` |
| **id**  string | The identifier for the invalidation request.  **Returned:** always  **Sample:** `"I2G9MOWJZFV612"` |
| **invalidation_batch**  complex | The current invalidation information for the batch request.  **Returned:** always |
| **caller_reference**  string | The value used to uniquely identify an invalidation request.  **Returned:** always  **Sample:** `"testing 123"` |
| **paths**  complex | A dict that contains information about the objects that you want to invalidate.  **Returned:** always |
| **items**  list / elements=string | A list of the paths that you want to invalidate.  **Returned:** always  **Sample:** `["/testpathtwo/test2.js", "/testpathone/test1.css", "/testpaththree/test3.ss"]` |
| **quantity**  integer | The number of objects that you want to invalidate.  **Returned:** always  **Sample:** `3` |
| **status**  string | The status of the invalidation request.  **Returned:** always  **Sample:** `"Completed"` |
| **location**  string | The fully qualified URI of the distribution and invalidation batch request.  **Returned:** always  **Sample:** `"https://cloudfront.amazonaws.com/2017-03-25/distribution/E1ZID6KZJECZY7/invalidation/I2G9MOWJZFV622"` |

### Authors

- Willem van Ketwich (@wilvk)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
