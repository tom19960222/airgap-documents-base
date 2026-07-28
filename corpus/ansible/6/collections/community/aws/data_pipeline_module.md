---
collection: ansible
version: "6"
title: "community.aws.data_pipeline module – Create and manage AWS Datapipelines"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/data_pipeline_module.html
fetched_at: 2026-07-27T17:03:49+00:00
---
# community.aws.data_pipeline module – Create and manage AWS Datapipelines

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
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](data_pipeline_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **description**  string | An optional description for the pipeline being created.  Default: `""` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **name**  string / required | The name of the Datapipeline to create/modify/delete. |
| **objects**  list / elements=dictionary | A list of pipeline object definitions, each of which is a dict that takes the keys *id*, *name* and *fields*. |
| **fields**  list / elements=dictionary | Key-value pairs that define the properties of the object.  The value is specified as a reference to another object *refValue* or as a string value *stringValue* but not as both. |
| **key**  string | The field identifier. |
| **refValue**  string | The field value, expressed as the identifier of another object.  Exactly one of *stringValue* and *refValue* may be specified. |
| **stringValue**  string | The field value.  Exactly one of *stringValue* and *refValue* may be specified. |
| **id**  string | The ID of the object. |
| **name**  string | The name of the object. |
| **parameters**  list / elements=dictionary | A list of parameter objects (dicts) in the pipeline definition. |
| **attributes**  list / elements=dictionary | A list of attributes (dicts) of the parameter object. |
| **key**  string | The field identifier. |
| **stringValue**  string | The field value. |
| **id**  string | The ID of the parameter object. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | The requested state of the pipeline.  Choices:   - `"present"` ← (default) - `"absent"` - `"active"` - `"inactive"` |
| **tags**  dictionary | A dict of key:value pair(s) to add to the pipeline. |
| **timeout**  integer | Time in seconds to wait for the pipeline to transition to the requested state, fail otherwise.  Default: `300` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **values**  list / elements=dictionary | A list of parameter values (dicts) in the pipeline definition. |
| **id**  string | The ID of the parameter value |
| **stringValue**  string | The field value |
| **version**  string | The version option has never had any effect and will be removed after 2022-06-01. |

## [Notes](data_pipeline_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

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
| **changed**  boolean | whether the data pipeline has been modified  Returned: always  Sample: `{"changed": true}` |
| **result**  dictionary | Contains the data pipeline data (data_pipeline) and a return message (msg). If the data pipeline exists data_pipeline will contain the keys description, name, pipeline_id, state, tags, and unique_id. If the data pipeline does not exist then data_pipeline will be an empty dict. The msg describes the status of the operation.  Returned: always |

### Authors

- Raghu Udiyar (@raags)
- Sloane Hertel (@s-hertel)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
