---
collection: ansible
version: "8"
title: "community.aws.codebuild_project module – Create or delete an AWS CodeBuild project"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/codebuild_project_module.html
fetched_at: 2026-07-28T01:40:24+00:00
---
# community.aws.codebuild_project module – Create or delete an AWS CodeBuild project

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
> see [Requirements](codebuild_project_module.md#ansible-collections-community-aws-codebuild-project-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.codebuild_project`.

New in community.aws 1.0.0

- [Synopsis](codebuild_project_module.md#synopsis)
- [Requirements](codebuild_project_module.md#requirements)
- [Parameters](codebuild_project_module.md#parameters)
- [Notes](codebuild_project_module.md#notes)
- [Examples](codebuild_project_module.md#examples)
- [Return Values](codebuild_project_module.md#return-values)

## [Synopsis](codebuild_project_module.md#id1)

- Create or delete a CodeBuild projects on AWS, used for building code artifacts from source code.
- Prior to release 5.0.0 this module was called `community.aws.aws_codebuild`. The usage did not change.

Aliases: aws_codebuild

## [Requirements](codebuild_project_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](codebuild_project_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **artifacts**  dictionary | Information about the build output artifacts for the build project.  *artifacts* is required when creating a new project. |
| **location**  string | Information about the build output artifact location. When choosing *type* `S3`, set the bucket name here. |
| **name**  string | Along with path and namespace_type, the pattern that AWS CodeBuild will use to name and store the output artifact. |
| **namespace_type**  string | Along with path and name, the pattern that AWS CodeBuild will use to determine the name and location to store the output artifacts.  Accepts `BUILD_ID` and `NONE`.  See docs here: <http://boto3.readthedocs.io/en/latest/reference/services/codebuild.html#CodeBuild.Client.create_project>. |
| **packaging**  string | The type of build output artifact to create on S3, can be NONE for creating a folder or ZIP for a ZIP file. |
| **path**  string | Along with namespace_type and name, the pattern that AWS CodeBuild will use to name and store the output artifacts.  Used for path in S3 bucket when type is `S3`. |
| **type**  string / required | The type of build output for artifacts. Can be one of the following: `CODEPIPELINE`, `NO_ARTIFACTS`, `S3`. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **cache**  dictionary | Caching params to speed up following builds. |
| **location**  string / required | Caching location on S3. |
| **type**  string / required | Cache type. Can be `NO_CACHE` or `S3`. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **description**  string | Descriptive text of the CodeBuild project. |
| **encryption_key**  string | The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build output artifacts. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **environment**  dictionary | Information about the build environment for the build project. |
| **compute_type**  string / required | Information about the compute resources the build project will use.  Available values include: `BUILD_GENERAL1_SMALL`, `BUILD_GENERAL1_MEDIUM`, `BUILD_GENERAL1_LARGE`. |
| **environment_variables**  string | A set of environment variables to make available to builds for the build project. List of dictionaries with name and value fields.  Example: { name: ‘MY_ENV_VARIABLE’, value: ‘test’ } |
| **image**  string / required | The ID of the Docker image to use for this build project. |
| **privileged_mode**  string | Enables running the Docker daemon inside a Docker container.  Set to `true` only if the build project is be used to build Docker images. |
| **type**  string / required | The type of build environment to use for the project. Usually `LINUX_CONTAINER`. |
| **name**  string / required | Name of the CodeBuild project. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **service_role**  string | The ARN of the AWS IAM role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **source**  dictionary | Configure service and location for the build input source.  *source* is required when creating a new project. |
| **buildspec**  string | The build spec declaration to use for the builds in this build project. Leave empty if part of the CodeBuild project. |
| **git_clone_depth**  integer | When using git you can specify the clone depth as an integer here. |
| **insecure_ssl**  boolean | Enable this flag to ignore SSL warnings while connecting to the project source code.  **Choices:**   - `false` - `true` |
| **location**  string | Information about the location of the source code to be built. For *type* `CODEPIPELINE` location should not be specified. |
| **type**  string / required | The type of the source. Allows one of these: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `S3`, `BITBUCKET`, `GITHUB_ENTERPRISE`. |
| **state**  string | Create or remove CodeBuild project.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **timeout_in_minutes**  integer | How long CodeBuild should wait until timing out any build that has not been marked as completed.  **Default:** `60` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **vpc_config**  dictionary | The VPC config enables AWS CodeBuild to access resources in an Amazon VPC. |

## [Notes](codebuild_project_module.md#id4)

> **Note:**
>
> - For details of the parameters and returns see <http://boto3.readthedocs.io/en/latest/reference/services/codebuild.html>.
> - *tags* changed from boto3 format to standard dict format in release 6.0.0.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](codebuild_project_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- community.aws.codebuild_project:
    name: my_project
    description: My nice little project
    service_role: "arn:aws:iam::123123:role/service-role/code-build-service-role"
    source:
        # Possible values: BITBUCKET, CODECOMMIT, CODEPIPELINE, GITHUB, S3
        type: CODEPIPELINE
        buildspec: ''
    artifacts:
        namespaceType: NONE
        packaging: NONE
        type: CODEPIPELINE
        name: my_project
    environment:
        computeType: BUILD_GENERAL1_SMALL
        privilegedMode: "true"
        image: "aws/codebuild/docker:17.09.0"
        type: LINUX_CONTAINER
        environmentVariables:
            - { name: 'PROFILE', value: 'staging' }
    encryption_key: "arn:aws:kms:us-east-1:123123:alias/aws/s3"
    region: us-east-1
    state: present
```

## [Return Values](codebuild_project_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **project**  complex | Returns the dictionary describing the code project configuration.  **Returned:** success |
| **arn**  string | ARN of the CodeBuild project.  **Returned:** always  **Sample:** `"arn:aws:codebuild:us-east-1:123123123:project/vod-api-app-builder"` |
| **artifacts**  complex | Information about the output of build artifacts  **Returned:** always |
| **location**  string | Output location for build artifacts.  **Returned:** when configured |
| **type**  string | The type of build artifact.  **Returned:** always  **Sample:** `"CODEPIPELINE"` |
| **cache**  dictionary | Cache settings for the build project.  **Returned:** when configured |
| **created**  string | Timestamp of the create time of the project.  **Returned:** always  **Sample:** `"2018-04-17T16:56:03.245000+02:00"` |
| **description**  string | A description of the CodeBuild project.  **Returned:** always  **Sample:** `"My nice little project"` |
| **environment**  dictionary | Environment settings for the build.  **Returned:** always |
| **name**  string | Name of the CodeBuild project.  **Returned:** always  **Sample:** `"my_project"` |
| **reource_tags**  dictionary  *added in community.aws 4.0.0* | A simple dictionary representing the tags added to the project.  *tags* and *reource_tags* represent the same information in different formats.  **Returned:** when configured |
| **service_role**  string | IAM role to be used during build to access other AWS services.  **Returned:** always  **Sample:** `"arn:aws:iam::123123123:role/codebuild-service-role"` |
| **source**  complex | Information about the build input source code.  **Returned:** always |
| **auth**  complex | Information about the authorization settings for AWS CodeBuild to access the source code to be built.  **Returned:** when configured |
| **build_spec**  string | The build spec declaration to use for the builds in this build project.  **Returned:** always |
| **git_clone_depth**  integer | The git clone depth.  **Returned:** when configured |
| **insecure_ssl**  boolean | True if set to ignore SSL warnings.  **Returned:** when configured |
| **location**  string | Location identifier, depending on the source type.  **Returned:** when configured |
| **type**  string | The type of the repository.  **Returned:** always  **Sample:** `"CODEPIPELINE"` |
| **tags**  list / elements=string | Tags added to the project in the boto3 list of dictionaries format.  *tags* and *reource_tags* represent the same information in different formats.  **Returned:** when configured |
| **timeout_in_minutes**  integer | The timeout of a build in minutes.  **Returned:** always  **Sample:** `60` |

### Authors

- Stefan Horning (@stefanhorning)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
