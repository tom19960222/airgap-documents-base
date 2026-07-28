---
collection: ansible
version: "8"
title: "community.aws.s3_website module – Configure an s3 bucket as a website"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/s3_website_module.html
fetched_at: 2026-07-28T01:41:52+00:00
---
# community.aws.s3_website module – Configure an s3 bucket as a website

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
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](s3_website_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **error_key**  string | The object key name to use when a 4XX class error occurs. To remove an error key, set to None. |
| **name**  string / required | Name of the s3 bucket |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **redirect_all_requests**  string | Describes the redirect behavior for every request to this s3 bucket website endpoint |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string / required | Add or remove s3 website configuration  **Choices:**   - `"present"` - `"absent"` |
| **suffix**  string | Suffix that is appended to a request that is for a directory on the website endpoint (e.g. if the suffix is index.html and you make a request to samplebucket/images/ the data that is returned will be for the object with the key name images/index.html). The suffix must not include a slash character.  **Default:** `"index.html"` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](s3_website_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

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
| **error_document**  complex | error document  **Returned:** always |
| **key**  string | object key name to use when a 4XX class error occurs  **Returned:** when error_document parameter set  **Sample:** `"error.html"` |
| **index_document**  complex | index document  **Returned:** always |
| **suffix**  string | suffix that is appended to a request that is for a directory on the website endpoint  **Returned:** success  **Sample:** `"index.html"` |
| **redirect_all_requests_to**  complex | where to redirect requests  **Returned:** always |
| **host_name**  string | name of the host where requests will be redirected.  **Returned:** when redirect all requests parameter set  **Sample:** `"ansible.com"` |
| **protocol**  string | protocol to use when redirecting requests.  **Returned:** when redirect all requests parameter set  **Sample:** `"https"` |
| **routing_rules**  list / elements=string | routing rules  **Returned:** always |
| **condition**  complex | A container for describing a condition that must be met for the specified redirect to apply.  **Returned:** success |
| **http_error_code_returned_equals**  string | The HTTP error code when the redirect is applied.  **Returned:** always |
| **key_prefix_equals**  string | object key name prefix when the redirect is applied. For example, to redirect requests for ExamplePage.html, the key prefix will be ExamplePage.html  **Returned:** when routing rule present  **Sample:** `"docs/"` |
| **redirect**  complex | Container for redirect information.  **Returned:** always |
| **host_name**  string | name of the host where requests will be redirected.  **Returned:** when host name set as part of redirect rule  **Sample:** `"ansible.com"` |
| **http_redirect_code**  string | The HTTP redirect code to use on the response.  **Returned:** when routing rule present |
| **protocol**  string | Protocol to use when redirecting requests.  **Returned:** when routing rule present  **Sample:** `"http"` |
| **replace_key_prefix_with**  string | object key prefix to use in the redirect request  **Returned:** when routing rule present  **Sample:** `"documents/"` |
| **replace_key_with**  string | object key prefix to use in the redirect request  **Returned:** when routing rule present  **Sample:** `"documents/"` |

### Authors

- Rob White (@wimnat)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
