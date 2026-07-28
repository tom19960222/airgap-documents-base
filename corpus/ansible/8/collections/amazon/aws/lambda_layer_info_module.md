---
collection: ansible
version: "8"
title: "amazon.aws.lambda_layer_info module – List lambda layer or lambda layer versions"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/lambda_layer_info_module.html
fetched_at: 2026-07-28T01:07:00+00:00
---
# amazon.aws.lambda_layer_info module – List lambda layer or lambda layer versions

> **Note:**
>
> This module is part of the [amazon.aws collection](https://galaxy.ansible.com/ui/repo/published/amazon/aws/) (version 6.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install amazon.aws`.
> You need further requirements to be able to use this module,
> see [Requirements](lambda_layer_info_module.md#ansible-collections-amazon-aws-lambda-layer-info-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.lambda_layer_info`.

New in amazon.aws 5.5.0

- [Synopsis](lambda_layer_info_module.md#synopsis)
- [Requirements](lambda_layer_info_module.md#requirements)
- [Parameters](lambda_layer_info_module.md#parameters)
- [Notes](lambda_layer_info_module.md#notes)
- [Examples](lambda_layer_info_module.md#examples)
- [Return Values](lambda_layer_info_module.md#return-values)

## [Synopsis](lambda_layer_info_module.md#id1)

- This module is used to list the versions of an Lambda layer or all available lambda layers.
- The lambda layer versions that have been deleted aren’t listed.

## [Requirements](lambda_layer_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](lambda_layer_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **compatible_architecture**  string | A compatible instruction set architectures.  Specify this option without *name* to include only to list only latest layers versions of layers that are compatible with that instruction set architecture.  Specify this option with *name* to include only layer versions that are compatible with that architecture. |
| **compatible_runtime**  string | A runtime identifier.  Specify this option without *name* to list only latest layers versions of layers that indicate that they’re compatible with that runtime.  Specify this option with *name* to list only layer versions that indicate that they’re compatible with that runtime. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **name**  aliases: layer_name  string | The name or Amazon Resource Name (ARN) of the Lambda layer. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **version_number**  aliases: layer_version  integer  *added in amazon.aws 6.0.0* | The Lambda layer version number to retrieve.  Requires *name* to be provided. |

## [Notes](lambda_layer_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](lambda_layer_info_module.md#id5)

```yaml+jinja
---
# Display information about the versions for the layer named blank-java-lib
- name: Retrieve layer versions
  amazon.aws.lambda_layer_info:
    name: blank-java-lib

# Display information about the versions for the layer named blank-java-lib compatible with architecture x86_64
- name: Retrieve layer versions
  amazon.aws.lambda_layer_info:
    name: blank-java-lib
    compatible_architecture: x86_64

# list latest versions of available layers
- name: list latest versions for all layers
  amazon.aws.lambda_layer_info:

# list latest versions of available layers compatible with runtime python3.7
- name: list latest versions for all layers
  amazon.aws.lambda_layer_info:
    compatible_runtime: python3.7

# Retrieve specific lambda layer information
- name: Get lambda layer version information
  amazon.aws.lambda_layer_info:
    name: my-layer
    version_number: 1
```

## [Return Values](lambda_layer_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **layers_versions**  list / elements=dictionary | The layers versions that exists.  **Returned:** success |
| **compatible_architectures**  list / elements=string | A list of compatible instruction set architectures.  **Returned:** if it was defined for the layer version. |
| **compatible_runtimes**  list / elements=string | A list of compatible runtimes.  **Returned:** if it was defined for the layer version.  **Sample:** `["python3.7"]` |
| **content**  complex  *added in amazon.aws 6.0.0* | Details about the layer version.  **Returned:** if *version_number* was provided |
| **code_sha256**  string | The SHA-256 hash of the layer archive.  **Returned:** success  **Sample:** `"tv9jJO+rPbXUUXuRKi7CwHzKtLDkDRJLB3cC3Z/ouXo="` |
| **code_size**  integer | The size of the layer archive in bytes.  **Returned:** success  **Sample:** `169` |
| **location**  string | A link to the layer archive in Amazon S3 that is valid for 10 minutes.  **Returned:** success  **Sample:** `"https://awslambda-us-east-2-layers.s3.us-east-2.amazonaws.com/snapshots/123456789012/mylayer-4aaa2fbb-96a?versionId=27iWyA73c..."` |
| **signing_job_arn**  string | The Amazon Resource Name (ARN) of a signing job.  **Returned:** success |
| **signing_profile_version_arn**  string | The Amazon Resource Name (ARN) for a signing profile version.  **Returned:** success |
| **created_date**  string | The date that the layer version was created, in ISO-8601 format (YYYY-MM-DDThh:mm:ss.sTZD).  **Returned:** if the layer version exists or has been created  **Sample:** `"2022-09-28T14:27:35.866+0000"` |
| **description**  string | The description of the version.  **Returned:** *state=present* |
| **layer_arn**  string | The ARN of the layer.  **Returned:** when `name` is provided  **Sample:** `"arn:aws:lambda:eu-west-2:123456789012:layer:pylayer"` |
| **layer_version_arn**  string | The ARN of the layer version.  **Returned:** if the layer version exists or has been created  **Sample:** `"arn:aws:lambda:eu-west-2:123456789012:layer:pylayer:2"` |
| **license_info**  string | The layer’s software license.  **Returned:** if it was defined for the layer version.  **Sample:** `"GPL-3.0-only"` |
| **version**  integer | The version number.  **Returned:** if the layer version exists or has been created  **Sample:** `1` |

### Authors

- Aubin Bikouo (@abikouo)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
