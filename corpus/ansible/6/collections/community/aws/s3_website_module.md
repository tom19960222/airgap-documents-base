---
collection: ansible
version: "6"
title: "community.aws.s3_website module – Configure an s3 bucket as a website"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/s3_website_module.html
fetched_at: 2026-07-27T17:05:05+00:00
---
# community.aws.s3_website module – Configure an s3 bucket as a website

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
> see [Requirements](s3_website_module.md#ansible-collections-community-aws-s3-website-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.s3_website`.

New in community.aws 1.0.0

- [Synopsis](s3_website_module.md#synopsis)
- [Requirements](s3_website_module.md#requirements)
- [Parameters](s3_website_module.md#parameters)
- [Notes](s3_website_module.md#notes)
- [Examples](s3_website_module.md#examples)
- [Return Values](s3_website_module.md#return-values)

## [Synopsis](s3_website_module.md#id1)

- Configure an s3 bucket as a website

## [Requirements](s3_website_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](s3_website_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **error_key**  string | The object key name to use when a 4XX class error occurs. To remove an error key, set to None. |
| **name**  string / required | Name of the s3 bucket |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **redirect_all_requests**  string | Describes the redirect behavior for every request to this s3 bucket website endpoint |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string / required | Add or remove s3 website configuration  Choices:   - `"present"` - `"absent"` |
| **suffix**  string | Suffix that is appended to a request that is for a directory on the website endpoint (e.g. if the suffix is index.html and you make a request to samplebucket/images/ the data that is returned will be for the object with the key name images/index.html). The suffix must not include a slash character.  Default: `"index.html"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](s3_website_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](s3_website_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Configure an s3 bucket to redirect all requests to example.com
  community.aws.s3_website:
    name: mybucket.com
    redirect_all_requests: example.com
    state: present

- name: Remove website configuration from an s3 bucket
  community.aws.s3_website:
    name: mybucket.com
    state: absent

- name: Configure an s3 bucket as a website with index and error pages
  community.aws.s3_website:
    name: mybucket.com
    suffix: home.htm
    error_key: errors/404.htm
    state: present
```

## [Return Values](s3_website_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_document**  complex | error document  Returned: always |
| **key**  string | object key name to use when a 4XX class error occurs  Returned: when error_document parameter set  Sample: `"error.html"` |
| **index_document**  complex | index document  Returned: always |
| **suffix**  string | suffix that is appended to a request that is for a directory on the website endpoint  Returned: success  Sample: `"index.html"` |
| **redirect_all_requests_to**  complex | where to redirect requests  Returned: always |
| **host_name**  string | name of the host where requests will be redirected.  Returned: when redirect all requests parameter set  Sample: `"ansible.com"` |
| **protocol**  string | protocol to use when redirecting requests.  Returned: when redirect all requests parameter set  Sample: `"https"` |
| **routing_rules**  list / elements=string | routing rules  Returned: always |
| **condition**  complex | A container for describing a condition that must be met for the specified redirect to apply.  Returned: success |
| **http_error_code_returned_equals**  string | The HTTP error code when the redirect is applied.  Returned: always |
| **key_prefix_equals**  string | object key name prefix when the redirect is applied. For example, to redirect requests for ExamplePage.html, the key prefix will be ExamplePage.html  Returned: when routing rule present  Sample: `"docs/"` |
| **redirect**  complex | Container for redirect information.  Returned: always |
| **host_name**  string | name of the host where requests will be redirected.  Returned: when host name set as part of redirect rule  Sample: `"ansible.com"` |
| **http_redirect_code**  string | The HTTP redirect code to use on the response.  Returned: when routing rule present |
| **protocol**  string | Protocol to use when redirecting requests.  Returned: when routing rule present  Sample: `"http"` |
| **replace_key_prefix_with**  string | object key prefix to use in the redirect request  Returned: when routing rule present  Sample: `"documents/"` |
| **replace_key_with**  string | object key prefix to use in the redirect request  Returned: when routing rule present  Sample: `"documents/"` |

### Authors

- Rob White (@wimnat)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
