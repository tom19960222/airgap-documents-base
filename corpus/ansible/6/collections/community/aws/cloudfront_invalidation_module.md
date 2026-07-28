---
collection: ansible
version: "6"
title: "community.aws.cloudfront_invalidation module – create invalidations for AWS CloudFront distributions"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/cloudfront_invalidation_module.html
fetched_at: 2026-07-27T17:03:43+00:00
---
# community.aws.cloudfront_invalidation module – create invalidations for AWS CloudFront distributions

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
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](cloudfront_invalidation_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **alias**  string | The alias of the CloudFront distribution to invalidate paths for. Can be specified instead of distribution_id. |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **caller_reference**  string | A unique reference identifier for the invalidation paths.  Defaults to current datetime stamp. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **distribution_id**  string | The ID of the CloudFront distribution to invalidate paths for. Can be specified instead of the alias. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **target_paths**  list / elements=string / required | A list of paths on the distribution to invalidate. Each path should begin with `/`. Wildcards are allowed. eg. `/foo/bar/*` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](cloudfront_invalidation_module.md#id4)

> **Note:**
>
> - does not support check mode
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

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
| **invalidation**  complex | The invalidation’s information.  Returned: always |
| **create_time**  string | The date and time the invalidation request was first made.  Returned: always  Sample: `"2018-02-01T15:50:41.159000+00:00"` |
| **id**  string | The identifier for the invalidation request.  Returned: always  Sample: `"I2G9MOWJZFV612"` |
| **invalidation_batch**  complex | The current invalidation information for the batch request.  Returned: always |
| **caller_reference**  string | The value used to uniquely identify an invalidation request.  Returned: always  Sample: `"testing 123"` |
| **paths**  complex | A dict that contains information about the objects that you want to invalidate.  Returned: always |
| **items**  list / elements=string | A list of the paths that you want to invalidate.  Returned: always  Sample: `["/testpathtwo/test2.js", "/testpathone/test1.css", "/testpaththree/test3.ss"]` |
| **quantity**  integer | The number of objects that you want to invalidate.  Returned: always  Sample: `3` |
| **status**  string | The status of the invalidation request.  Returned: always  Sample: `"Completed"` |
| **location**  string | The fully qualified URI of the distribution and invalidation batch request.  Returned: always  Sample: `"https://cloudfront.amazonaws.com/2017-03-25/distribution/E1ZID6KZJECZY7/invalidation/I2G9MOWJZFV622"` |

### Authors

- Willem van Ketwich (@wilvk)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
