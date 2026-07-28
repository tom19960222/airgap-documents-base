---
collection: ansible
version: "8"
title: "community.aws.data_pipeline module – Create and manage AWS Datapipelines"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/data_pipeline_module.html
fetched_at: 2026-07-28T01:40:30+00:00
---
# community.aws.data_pipeline module – Create and manage AWS Datapipelines

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
> see [Requirements](data_pipeline_module.md#ansible-collections-community-aws-data-pipeline-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.data_pipeline`.

New in community.aws 1.0.0

- [Synopsis](data_pipeline_module.md#synopsis)
- [Requirements](data_pipeline_module.md#requirements)
- [Parameters](data_pipeline_module.md#parameters)
- [Notes](data_pipeline_module.md#notes)
- [Examples](data_pipeline_module.md#examples)
- [Return Values](data_pipeline_module.md#return-values)

## [Synopsis](data_pipeline_module.md#id1)

- Create and manage AWS Datapipelines. Creation is not idempotent in AWS, so the `uniqueId` is created by hashing the options (minus objects) given to the datapipeline.
- The pipeline definition must be in the format given here <https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_PutPipelineDefinition.html#API_PutPipelineDefinition_RequestSyntax>.
- Operations will wait for a configurable amount of time to ensure the pipeline is in the requested state.

## [Requirements](data_pipeline_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](data_pipeline_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **description**  string | An optional description for the pipeline being created.  **Default:** `""` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **name**  string / required | The name of the Datapipeline to create/modify/delete. |
| **objects**  list / elements=dictionary | A list of pipeline object definitions, each of which is a dict that takes the keys *id*, *name* and *fields*.  **Default:** `[]` |
| **fields**  list / elements=dictionary | Key-value pairs that define the properties of the object.  The value is specified as a reference to another object *refValue* or as a string value *stringValue* but not as both. |
| **key**  string | The field identifier. |
| **refValue**  string | The field value, expressed as the identifier of another object.  Exactly one of *stringValue* and *refValue* may be specified. |
| **stringValue**  string | The field value.  Exactly one of *stringValue* and *refValue* may be specified. |
| **id**  string | The ID of the object. |
| **name**  string | The name of the object. |
| **parameters**  list / elements=dictionary | A list of parameter objects (dicts) in the pipeline definition.  **Default:** `[]` |
| **attributes**  list / elements=dictionary | A list of attributes (dicts) of the parameter object. |
| **key**  string | The field identifier. |
| **stringValue**  string | The field value. |
| **id**  string | The ID of the parameter object. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | The requested state of the pipeline.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"active"` - `"inactive"` |
| **tags**  aliases: resource_tags  dictionary | A dict of key:value pair(s) to add to the pipeline.  **Default:** `{}` |
| **timeout**  integer | Time in seconds to wait for the pipeline to transition to the requested state, fail otherwise.  **Default:** `300` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **values**  list / elements=dictionary | A list of parameter values (dicts) in the pipeline definition.  **Default:** `[]` |
| **id**  string | The ID of the parameter value |
| **stringValue**  string | The field value |

## [Notes](data_pipeline_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](data_pipeline_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

# Create pipeline
- community.aws.data_pipeline:
    name: test-dp
    region: us-west-2
    objects: "{{pipelineObjects}}"
    parameters: "{{pipelineParameters}}"
    values: "{{pipelineValues}}"
    tags:
      key1: val1
      key2: val2
    state: present

# Example populating and activating a pipeline that demonstrates two ways of providing pipeline objects
- community.aws.data_pipeline:
  name: test-dp
  objects:
    - "id": "DefaultSchedule"
      "name": "Every 1 day"
      "fields":
        - "key": "period"
          "stringValue": "1 days"
        - "key": "type"
          "stringValue": "Schedule"
        - "key": "startAt"
          "stringValue": "FIRST_ACTIVATION_DATE_TIME"
    - "id": "Default"
      "name": "Default"
      "fields": [ { "key": "resourceRole", "stringValue": "my_resource_role" },
                  { "key": "role", "stringValue": "DataPipelineDefaultRole" },
                  { "key": "pipelineLogUri", "stringValue": "s3://my_s3_log.txt" },
                  { "key": "scheduleType", "stringValue": "cron" },
                  { "key": "schedule", "refValue": "DefaultSchedule" },
                  { "key": "failureAndRerunMode", "stringValue": "CASCADE" } ]
  state: active

# Activate pipeline
- community.aws.data_pipeline:
    name: test-dp
    region: us-west-2
    state: active

# Delete pipeline
- community.aws.data_pipeline:
    name: test-dp
    region: us-west-2
    state: absent
```

## [Return Values](data_pipeline_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | whether the data pipeline has been modified  **Returned:** always  **Sample:** `{"changed": true}` |
| **result**  dictionary | Contains the data pipeline data (data_pipeline) and a return message (msg). If the data pipeline exists data_pipeline will contain the keys description, name, pipeline_id, state, tags, and unique_id. If the data pipeline does not exist then data_pipeline will be an empty dict. The msg describes the status of the operation.  **Returned:** always |

### Authors

- Raghu Udiyar (@raags)
- Sloane Hertel (@s-hertel)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
