---
collection: ansible
version: "8"
title: "community.aws.codecommit_repository module – Manage repositories in AWS CodeCommit"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/codecommit_repository_module.html
fetched_at: 2026-07-28T01:40:25+00:00
---
# community.aws.codecommit_repository module – Manage repositories in AWS CodeCommit

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
> see [Requirements](codecommit_repository_module.md#ansible-collections-community-aws-codecommit-repository-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.codecommit_repository`.

New in community.aws 1.0.0

- [Synopsis](codecommit_repository_module.md#synopsis)
- [Requirements](codecommit_repository_module.md#requirements)
- [Parameters](codecommit_repository_module.md#parameters)
- [Notes](codecommit_repository_module.md#notes)
- [Examples](codecommit_repository_module.md#examples)
- [Return Values](codecommit_repository_module.md#return-values)

## [Synopsis](codecommit_repository_module.md#id1)

- Supports creation and deletion of CodeCommit repositories.
- See <https://aws.amazon.com/codecommit/> for more information about CodeCommit.
- Prior to release 5.0.0 this module was called `community.aws.aws_codecommit`. The usage did not change.

Aliases: aws_codecommit

## [Requirements](codecommit_repository_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](codecommit_repository_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **description**  aliases: comment  string | Description or comment of repository.  **Default:** `""` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **name**  string / required | Name of repository. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string / required | Specifies the state of repository.  **Choices:**   - `"present"` - `"absent"` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](codecommit_repository_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](codecommit_repository_module.md#id5)

```yaml+jinja
# Create a new repository
- community.aws.codecommit_repository:
    name: repo
    state: present

# Delete a repository
- community.aws.codecommit_repository:
    name: repo
    state: absent
```

## [Return Values](codecommit_repository_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **repository_metadata**  complex | Information about the repository.  **Returned:** always |
| **account_id**  string | The ID of the AWS account associated with the repository.  **Returned:** when state is present  **Sample:** `"123456789012"` |
| **arn**  string | The Amazon Resource Name (ARN) of the repository.  **Returned:** when state is present  **Sample:** `"arn:aws:codecommit:ap-northeast-1:123456789012:username"` |
| **clone_url_http**  string | The URL to use for cloning the repository over HTTPS.  **Returned:** when state is present  **Sample:** `"https://git-codecommit.ap-northeast-1.amazonaws.com/v1/repos/reponame"` |
| **clone_url_ssh**  string | The URL to use for cloning the repository over SSH.  **Returned:** when state is present  **Sample:** `"ssh://git-codecommit.ap-northeast-1.amazonaws.com/v1/repos/reponame"` |
| **creation_date**  string | The date and time the repository was created, in timestamp format.  **Returned:** when state is present  **Sample:** `"2018-10-16T13:21:41.261000+09:00"` |
| **last_modified_date**  string | The date and time the repository was last modified, in timestamp format.  **Returned:** when state is present  **Sample:** `"2018-10-16T13:21:41.261000+09:00"` |
| **repository_description**  string | A comment or description about the repository.  **Returned:** when state is present  **Sample:** `"test from ptux"` |
| **repository_id**  string | The ID of the repository that was created or deleted  **Returned:** always  **Sample:** `"e62a5c54-i879-497b-b62f-9f99e4ebfk8e"` |
| **repository_name**  string | The repository’s name.  **Returned:** when state is present  **Sample:** `"reponame"` |
| **response_metadata**  complex | Information about the response.  **Returned:** always |
| **http_headers**  dictionary | http headers of http response  **Returned:** always |
| **http_status_code**  string | http status code of http response  **Returned:** always  **Sample:** `"200"` |
| **request_id**  string | http request id  **Returned:** always  **Sample:** `"fb49cfca-d0fa-11e8-85cb-b3cc4b5045ef"` |
| **retry_attempts**  string | numbers of retry attempts  **Returned:** always  **Sample:** `"0"` |

### Authors

- Shuang Wang (@ptux)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
