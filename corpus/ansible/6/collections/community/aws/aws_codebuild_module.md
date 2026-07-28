---
collection: ansible
version: "6"
title: "community.aws.aws_codebuild module – Create or delete an AWS CodeBuild project"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/aws_codebuild_module.html
fetched_at: 2026-07-27T17:03:16+00:00
---
# community.aws.aws_codebuild module – Create or delete an AWS CodeBuild project

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
> see [Requirements](aws_codebuild_module.md#ansible-collections-community-aws-aws-codebuild-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.aws_codebuild`.

New in community.aws 1.0.0

- [Synopsis](aws_codebuild_module.md#synopsis)
- [Requirements](aws_codebuild_module.md#requirements)
- [Parameters](aws_codebuild_module.md#parameters)
- [Notes](aws_codebuild_module.md#notes)
- [Examples](aws_codebuild_module.md#examples)
- [Return Values](aws_codebuild_module.md#return-values)

## [Synopsis](aws_codebuild_module.md#id1)

- Create or delete a CodeBuild projects on AWS, used for building code artifacts from source code.

## [Requirements](aws_codebuild_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](aws_codebuild_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **artifacts**  dictionary | Information about the build output artifacts for the build project.  *artifacts* is required when creating a new project. |
| **location**  string | Information about the build output artifact location. When choosing type S3, set the bucket name here. |
| **name**  string | Along with path and namespace_type, the pattern that AWS CodeBuild will use to name and store the output artifact. |
| **namespace_type**  string | Along with path and name, the pattern that AWS CodeBuild will use to determine the name and location to store the output artifacts.  Accepts `BUILD_ID` and `NONE`.  See docs here: <http://boto3.readthedocs.io/en/latest/reference/services/codebuild.html#CodeBuild.Client.create_project>. |
| **packaging**  string | The type of build output artifact to create on S3, can be NONE for creating a folder or ZIP for a ZIP file. |
| **path**  string | Along with namespace_type and name, the pattern that AWS CodeBuild will use to name and store the output artifacts.  Used for path in S3 bucket when type is `S3`. |
| **type**  string / required | The type of build output for artifacts. Can be one of the following: `CODEPIPELINE`, `NO_ARTIFACTS`, `S3`. |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **cache**  dictionary | Caching params to speed up following builds. |
| **location**  string / required | Caching location on S3. |
| **type**  string / required | Cache type. Can be `NO_CACHE` or `S3`. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **description**  string | Descriptive text of the CodeBuild project. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **encryption_key**  string | The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build output artifacts. |
| **environment**  dictionary | Information about the build environment for the build project. |
| **compute_type**  string / required | Information about the compute resources the build project will use.  Available values include: `BUILD_GENERAL1_SMALL`, `BUILD_GENERAL1_MEDIUM`, `BUILD_GENERAL1_LARGE`. |
| **environment_variables**  string | A set of environment variables to make available to builds for the build project. List of dictionaries with name and value fields.  Example: { name: ‘MY_ENV_VARIABLE’, value: ‘test’ } |
| **image**  string / required | The ID of the Docker image to use for this build project. |
| **privileged_mode**  string | Enables running the Docker daemon inside a Docker container. Set to true only if the build project is be used to build Docker images. |
| **type**  string / required | The type of build environment to use for the project. Usually `LINUX_CONTAINER`. |
| **name**  string / required | Name of the CodeBuild project. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *resource_tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  Choices:   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **resource_tags**  dictionary | A dictionary representing the tags to be applied to the build project.  If the *resource_tags* parameter is not set then tags will not be modified.  Mutually exclusive with the *tags* parameter. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **service_role**  string | The ARN of the AWS IAM role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account. |
| **source**  dictionary | Configure service and location for the build input source.  *source* is required when creating a new project. |
| **buildspec**  string | The build spec declaration to use for the builds in this build project. Leave empty if part of the code project. |
| **git_clone_depth**  integer | When using git you can specify the clone depth as an integer here. |
| **insecure_ssl**  boolean | Enable this flag to ignore SSL warnings while connecting to the project source code.  Choices:   - `false` - `true` |
| **location**  string | Information about the location of the source code to be built. For type CODEPIPELINE location should not be specified. |
| **type**  string / required | The type of the source. Allows one of these: `CODECOMMIT`, `CODEPIPELINE`, `GITHUB`, `S3`, `BITBUCKET`, `GITHUB_ENTERPRISE`. |
| **state**  string | Create or remove code build project.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=dictionary | A set of tags for the build project.  Mutually exclusive with the *resource_tags* parameter.  In release 6.0.0 this parameter will accept a simple dictionary instead of the list of dictionaries format. To use the simple dictionary format prior to release 6.0.0 the *resource_tags* can be used instead of *tags*. |
| **key**  string | The name of the Tag. |
| **value**  string | The value of the Tag. |
| **timeout_in_minutes**  integer | How long CodeBuild should wait until timing out any build that has not been marked as completed.  Default: `60` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **vpc_config**  dictionary | The VPC config enables AWS CodeBuild to access resources in an Amazon VPC. |

## [Notes](aws_codebuild_module.md#id4)

> **Note:**
>
> - For details of the parameters and returns see <http://boto3.readthedocs.io/en/latest/reference/services/codebuild.html>.
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](aws_codebuild_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- community.aws.aws_codebuild:
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

## [Return Values](aws_codebuild_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **project**  complex | Returns the dictionary describing the code project configuration.  Returned: success |
| **arn**  string | ARN of the CodeBuild project  Returned: always  Sample: `"arn:aws:codebuild:us-east-1:123123123:project/vod-api-app-builder"` |
| **artifacts**  complex | Information about the output of build artifacts  Returned: always |
| **location**  string | Output location for build artifacts  Returned: when configured |
| **type**  string | The type of build artifact.  Returned: always  Sample: `"CODEPIPELINE"` |
| **cache**  dictionary | Cache settings for the build project.  Returned: when configured |
| **created**  string | Timestamp of the create time of the project  Returned: always  Sample: `"2018-04-17T16:56:03.245000+02:00"` |
| **description**  string | A description of the build project  Returned: always  Sample: `"My nice little project"` |
| **environment**  dictionary | Environment settings for the build  Returned: always |
| **name**  string | Name of the CodeBuild project  Returned: always  Sample: `"my_project"` |
| **reource_tags**  dictionary  added in community.aws 4.0.0 | A simple dictionary representing the tags added to the project.  *tags* and *reource_tags* represent the same information in different formats.  Returned: when configured |
| **service_role**  string | IAM role to be used during build to access other AWS services.  Returned: always  Sample: `"arn:aws:iam::123123123:role/codebuild-service-role"` |
| **source**  complex | Information about the build input source code.  Returned: always |
| **auth**  complex | Information about the authorization settings for AWS CodeBuild to access the source code to be built.  Returned: when configured |
| **build_spec**  string | The build spec declaration to use for the builds in this build project.  Returned: always |
| **git_clone_depth**  integer | The git clone depth  Returned: when configured |
| **insecure_ssl**  boolean | True if set to ignore SSL warnings.  Returned: when configured |
| **location**  string | Location identifier, depending on the source type.  Returned: when configured |
| **type**  string | The type of the repository  Returned: always  Sample: `"CODEPIPELINE"` |
| **tags**  list / elements=string | Tags added to the project in the boto3 list of dictionaries format.  *tags* and *reource_tags* represent the same information in different formats.  Returned: when configured |
| **timeout_in_minutes**  integer | The timeout of a build in minutes  Returned: always  Sample: `60` |

### Authors

- Stefan Horning (@stefanhorning)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
