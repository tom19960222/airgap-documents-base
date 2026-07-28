---
collection: ansible
version: "6"
title: "community.aws.aws_codepipeline module – Create or delete AWS CodePipelines"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/aws_codepipeline_module.html
fetched_at: 2026-07-27T17:03:17+00:00
---
# community.aws.aws_codepipeline module – Create or delete AWS CodePipelines

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
> see [Requirements](aws_codepipeline_module.md#ansible-collections-community-aws-aws-codepipeline-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.aws_codepipeline`.

New in community.aws 1.0.0

- [Synopsis](aws_codepipeline_module.md#synopsis)
- [Requirements](aws_codepipeline_module.md#requirements)
- [Parameters](aws_codepipeline_module.md#parameters)
- [Notes](aws_codepipeline_module.md#notes)
- [Examples](aws_codepipeline_module.md#examples)
- [Return Values](aws_codepipeline_module.md#return-values)

## [Synopsis](aws_codepipeline_module.md#id1)

- Create or delete a CodePipeline on AWS.

## [Requirements](aws_codepipeline_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](aws_codepipeline_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **artifact_store**  dictionary / required | Location information where artifacts are stored (on S3). Dictionary with fields type and location. |
| **location**  string | Bucket name for artifacts. |
| **type**  string | Type of the artifacts storage (only ‘S3’ is currently supported). |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **name**  string / required | Name of the pipeline |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **role_arn**  string / required | ARN of the IAM role to use when executing the pipeline |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **stages**  list / elements=dictionary / required | List of stages to perform in the CodePipeline. List of dictionaries containing name and actions for each stage. |
| **actions**  list / elements=dictionary | List of action configurations for that stage.  See the boto3 documentation for full documentation of suboptions:  <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.create_pipeline> |
| **name**  string | Name of the stage (step) in the codepipeline |
| **state**  string | Create or remove code pipeline  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **version**  integer | Version number of the pipeline. This number is automatically incremented when a pipeline is updated. |

## [Notes](aws_codepipeline_module.md#id4)

> **Note:**
>
> - for details of the parameters and returns see <http://boto3.readthedocs.io/en/latest/reference/services/codepipeline.html>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](aws_codepipeline_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

# Example for creating a pipeline for continuous deploy of Github code to an ECS cluster (container)
- community.aws.aws_codepipeline:
    name: my_deploy_pipeline
    role_arn: arn:aws:iam::123456:role/AWS-CodePipeline-Service
    artifact_store:
      type: S3
      location: my_s3_codepipline_bucket
    stages:
      - name: Get_source
        actions:
          -
            name: Git_pull
            actionTypeId:
              category: Source
              owner: ThirdParty
              provider: GitHub
              version: '1'
            outputArtifacts:
              - { name: my-app-source }
            configuration:
              Owner: mediapeers
              Repo: my_gh_repo
              PollForSourceChanges: 'true'
              Branch: master
              # Generate token like this:
              # https://docs.aws.amazon.com/codepipeline/latest/userguide/GitHub-rotate-personal-token-CLI.html
              # GH Link: https://github.com/settings/tokens
              OAuthToken: 'abc123def456'
            runOrder: 1
      - name: Build
        actions:
          -
            name: CodeBuild
            actionTypeId:
              category: Build
              owner: AWS
              provider: CodeBuild
              version: '1'
            inputArtifacts:
              - { name: my-app-source }
            outputArtifacts:
              - { name: my-app-build }
            configuration:
              # A project with that name needs to be setup on AWS CodeBuild already (use code_build module).
              ProjectName: codebuild-project-name
            runOrder: 1
      - name: ECS_deploy
        actions:
          -
            name: ECS_deploy
            actionTypeId:
              category: Deploy
              owner: AWS
              provider: ECS
              version: '1'
            inputArtifacts:
              - { name: vod-api-app-build }
            configuration:
              # an ECS cluster with that name needs to be setup on AWS ECS already (use ecs_cluster and ecs_service module)
              ClusterName: ecs-cluster-name
              ServiceName: ecs-cluster-service-name
              FileName: imagedefinitions.json
    region: us-east-1
    state: present
```

## [Return Values](aws_codepipeline_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **pipeline**  complex | Returns the dictionary describing the code pipeline configuration.  Returned: success |
| **artifact_store**  complex | Information about where the build artifacts are stored  Returned: always |
| **encryption_key**  string | The encryption key used to encrypt the artifacts store, such as an AWS KMS key.  Returned: when configured |
| **location**  string | The location of the artifacts storage (s3 bucket name)  Returned: always  Sample: `"my_s3_codepipline_bucket"` |
| **type**  string | The type of the artifacts store, such as S3  Returned: always  Sample: `"S3"` |
| **name**  string | Name of the CodePipeline  Returned: always  Sample: `"my_deploy_pipeline"` |
| **role_arn**  string | ARN of the IAM role attached to the code pipeline  Returned: always  Sample: `"arn:aws:iam::123123123:role/codepipeline-service-role"` |
| **stages**  list / elements=string | List of stages configured for this pipeline  Returned: always |
| **version**  integer | The version number of the pipeline. This number is auto incremented when pipeline params are changed.  Returned: always |

### Authors

- Stefan Horning (@stefanhorning)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
