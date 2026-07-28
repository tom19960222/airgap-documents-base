---
collection: ansible
version: "8"
title: "community.aws.codepipeline module – Create or delete AWS CodePipelines"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/codepipeline_module.html
fetched_at: 2026-07-28T01:40:25+00:00
---
# community.aws.codepipeline module – Create or delete AWS CodePipelines

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
> see [Requirements](codepipeline_module.md#ansible-collections-community-aws-codepipeline-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.codepipeline`.

New in community.aws 1.0.0

- [Synopsis](codepipeline_module.md#synopsis)
- [Requirements](codepipeline_module.md#requirements)
- [Parameters](codepipeline_module.md#parameters)
- [Notes](codepipeline_module.md#notes)
- [Examples](codepipeline_module.md#examples)
- [Return Values](codepipeline_module.md#return-values)

## [Synopsis](codepipeline_module.md#id1)

- Create or delete a CodePipeline on AWS.
- Prior to release 5.0.0 this module was called `community.aws.aws_codepipeline`. The usage did not change.

Aliases: aws_codepipeline

## [Requirements](codepipeline_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](codepipeline_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **artifact_store**  dictionary / required | Location information where artifacts are stored (on S3). Dictionary with fields type and location. |
| **location**  string | Bucket name for artifacts. |
| **type**  string | Type of the artifacts storage (only ‘S3’ is currently supported). |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **name**  string / required | Name of the CodePipeline. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **role_arn**  string / required | ARN of the IAM role to use when executing the CodePipeline. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **stages**  list / elements=dictionary / required | List of stages to perform in the CodePipeline. List of dictionaries containing name and actions for each stage. |
| **actions**  list / elements=dictionary | List of action configurations for that stage.  See the boto3 documentation for full documentation of suboptions:  <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client.create_pipeline> |
| **name**  string | Name of the stage (step) in the CodePipeline. |
| **state**  string | Create or remove CodePipeline.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **version**  integer | Version number of the CodePipeline. This number is automatically incremented when a CodePipeline is updated. |

## [Notes](codepipeline_module.md#id4)

> **Note:**
>
> - For details of the parameters and returns see <http://boto3.readthedocs.io/en/latest/reference/services/codepipeline.html>.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](codepipeline_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

# Example for creating a pipeline for continuous deploy of Github code to an ECS cluster (container)
- community.aws.codepipeline:
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

## [Return Values](codepipeline_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **pipeline**  complex | Returns the dictionary describing the CodePipeline configuration.  **Returned:** success |
| **artifact_store**  complex | Information about where the build artifacts are stored  **Returned:** always |
| **encryption_key**  string | The encryption key used to encrypt the artifacts store, such as an AWS KMS key.  **Returned:** when configured |
| **location**  string | The location of the artifacts storage (s3 bucket name)  **Returned:** always  **Sample:** `"my_s3_codepipline_bucket"` |
| **type**  string | The type of the artifacts store, such as S3  **Returned:** always  **Sample:** `"S3"` |
| **name**  string | Name of the CodePipeline  **Returned:** always  **Sample:** `"my_deploy_pipeline"` |
| **role_arn**  string | ARN of the IAM role attached to the CodePipeline  **Returned:** always  **Sample:** `"arn:aws:iam::123123123:role/codepipeline-service-role"` |
| **stages**  list / elements=string | List of stages configured for this CodePipeline  **Returned:** always |
| **version**  integer | The version number of the CodePipeline.  This number is auto incremented when CodePipeline params are changed.  **Returned:** always |

### Authors

- Stefan Horning (@stefanhorning)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
