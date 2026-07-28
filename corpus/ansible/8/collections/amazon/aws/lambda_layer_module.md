---
collection: ansible
version: "8"
title: "amazon.aws.lambda_layer module – Creates an AWS Lambda layer or deletes an AWS Lambda layer version"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/lambda_layer_module.html
fetched_at: 2026-07-28T01:07:00+00:00
---
# amazon.aws.lambda_layer module – Creates an AWS Lambda layer or deletes an AWS Lambda layer version

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
> see [Requirements](lambda_layer_module.md#ansible-collections-amazon-aws-lambda-layer-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.lambda_layer`.

New in amazon.aws 5.5.0

- [Synopsis](lambda_layer_module.md#synopsis)
- [Requirements](lambda_layer_module.md#requirements)
- [Parameters](lambda_layer_module.md#parameters)
- [Notes](lambda_layer_module.md#notes)
- [Examples](lambda_layer_module.md#examples)
- [Return Values](lambda_layer_module.md#return-values)

## [Synopsis](lambda_layer_module.md#id1)

- This module allows the management of AWS Lambda functions aliases via the Ansible
- Creates an Lambda layer from a ZIP archive. Each time you call this module with the same layer name, a new version is created.
- Deletes a version of an Lambda layer.

## [Requirements](lambda_layer_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](lambda_layer_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **compatible_architectures**  list / elements=string | A list of compatible instruction set architectures. For example, x86_64.  Mutually exclusive with *version*. |
| **compatible_runtimes**  list / elements=string | A list of compatible function runtimes.  Ignored when *state=absent*.  Mutually exclusive with *version*. |
| **content**  dictionary | The function layer archive.  Required when *state=present*.  Ignored when *state=absent*.  Mutually exclusive with *version*. |
| **s3_bucket**  string | The Amazon S3 bucket of the layer archive. |
| **s3_key**  string | The Amazon S3 key of the layer archive. |
| **s3_object_version**  string | For versioned objects, the version of the layer archive object to use. |
| **zip_file**  path | Path to the base64-encoded file of the layer archive. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **description**  string | The description of the version.  Ignored when *state=absent*.  Mutually exclusive with *version*. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **license_info**  string | The layer’s software license. It can be any of an SPDX license identifier, the URL of a license hosted on the internet or the full text of the license.  Ignored when *state=absent*.  Mutually exclusive with *version*. |
| **name**  aliases: layer_name  string / required | The name or Amazon Resource Name (ARN) of the Lambda layer. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Determines if an Lambda layer should be created, or deleted. When set to `present`, an Lambda layer version will be created. If set to `absent`, an existing Lambda layer version will be deleted.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **version**  integer | The version number of the layer to delete.  Set to `-1` to delete all versions for the specified layer name.  Required when *state=absent*.  Ignored when *state=present*.  Mutually exclusive with *description*, *content*, *compatible_runtimes*, *license_info*, *compatible_architectures*. |

## [Notes](lambda_layer_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](lambda_layer_module.md#id5)

```yaml+jinja
---
# Create a new Python library layer version from a zip archive located into a S3 bucket
- name: Create a new python library layer
  amazon.aws.lambda_layer:
    state: present
    name: sample-layer
    description: 'My Python layer'
    content:
      s3_bucket: 'lambda-layers-us-west-2-123456789012'
      s3_key: 'python_layer.zip'
    compatible_runtimes:
      - python3.6
      - python3.7
    license_info: MIT
    compatible_architectures:
      - x86_64

# Create a layer version from a zip in the local filesystem
- name: Create a new layer from a zip in the local filesystem
  amazon.aws.lambda_layer:
    state: present
    name: sample-layer
    description: 'My Python layer'
    content:
      zip_file: 'python_layer.zip'
    compatible_runtimes:
      - python3.6
      - python3.7
    license_info: MIT
    compatible_architectures:
      - x86_64

# Delete a layer version
- name: Delete a layer version
  amazon.aws.lambda_layer:
    state: absent
    name: sample-layer
    version: 2

# Delete all versions of test-layer
- name: Delete all versions
  amazon.aws.lambda_layer:
    state: absent
    name: test-layer
    version: -1
```

## [Return Values](lambda_layer_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **layer_version**  list / elements=dictionary | info about the layer version that was created or deleted.  **Returned:** always |
| **compatible_architectures**  list / elements=string | A list of compatible instruction set architectures.  **Returned:** if it was defined for the layer version. |
| **compatible_runtimes**  list / elements=string | A list of compatible runtimes.  **Returned:** if it was defined for the layer version.  **Sample:** `["python3.7"]` |
| **content**  complex | Details about the layer version.  **Returned:** *state=present* |
| **code_sha256**  string | The SHA-256 hash of the layer archive.  **Returned:** *state=present*  **Sample:** `"VLluleJZ3HTwDrdYolSMrS+8iPwEkcoXXaegjXf+dmc="` |
| **code_size**  integer | The size of the layer archive in bytes.  **Returned:** *state=present*  **Sample:** `9473675` |
| **location**  string | A link to the layer archive in Amazon S3 that is valid for 10 minutes.  **Returned:** *state=present*  **Sample:** `"https://awslambda-us-east-1-layers.s3.us-east-1.amazonaws.com/snapshots/123456789012/pylayer-9da91deffd3b4941b8baeeae5daeffe4"` |
| **signing_job_arn**  string | The Amazon Resource Name (ARN) of a signing job.  **Returned:** When a signing profile is defined |
| **signing_profile_version_arn**  string | The Amazon Resource Name (ARN) for a signing profile version.  **Returned:** When a signing profile is defined |
| **created_date**  string | The date that the layer version was created, in ISO-8601 format (YYYY-MM-DDThh:mm:ss.sTZD).  **Returned:** if the layer version exists or has been created  **Sample:** `"2022-09-28T14:27:35.866+0000"` |
| **description**  string | The description of the version.  **Returned:** *state=present* |
| **layer_arn**  string | The ARN of the layer.  **Returned:** if the layer version exists or has been created  **Sample:** `"arn:aws:lambda:eu-west-2:123456789012:layer:pylayer"` |
| **layer_version_arn**  string | The ARN of the layer version.  **Returned:** if the layer version exists or has been created  **Sample:** `"arn:aws:lambda:eu-west-2:123456789012:layer:pylayer:2"` |
| **license_info**  string | The layer’s software license.  **Returned:** if it was defined for the layer version.  **Sample:** `"GPL-3.0-only"` |
| **version**  integer | The version number.  **Returned:** if the layer version exists or has been created  **Sample:** `1` |

### Authors

- Aubin Bikouo (@abikouo)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
