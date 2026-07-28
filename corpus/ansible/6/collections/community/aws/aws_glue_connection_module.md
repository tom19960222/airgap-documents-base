---
collection: ansible
version: "6"
title: "community.aws.aws_glue_connection module – Manage an AWS Glue connection"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/aws_glue_connection_module.html
fetched_at: 2026-07-27T17:03:26+00:00
---
# community.aws.aws_glue_connection module – Manage an AWS Glue connection

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
> see [Requirements](aws_glue_connection_module.md#ansible-collections-community-aws-aws-glue-connection-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.aws_glue_connection`.

New in community.aws 1.0.0

- [Synopsis](aws_glue_connection_module.md#synopsis)
- [Requirements](aws_glue_connection_module.md#requirements)
- [Parameters](aws_glue_connection_module.md#parameters)
- [Notes](aws_glue_connection_module.md#notes)
- [Examples](aws_glue_connection_module.md#examples)
- [Return Values](aws_glue_connection_module.md#return-values)

## [Synopsis](aws_glue_connection_module.md#id1)

- Manage an AWS Glue connection. See <https://aws.amazon.com/glue/> for details.

## [Requirements](aws_glue_connection_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](aws_glue_connection_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **availability_zone**  string  added in community.aws 1.5.0 | Availability Zone used by the connection  Required when *connection_type=NETWORK*. |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **catalog_id**  string | The ID of the Data Catalog in which to create the connection. If none is supplied, the AWS account ID is used by default. |
| **connection_properties**  dictionary | A dict of key-value pairs used as parameters for this connection.  Required when *state=present*. |
| **connection_type**  string | The type of the connection. Currently, SFTP is not supported.  Choices:   - `"CUSTOM"` - `"JDBC"` ← (default) - `"KAFKA"` - `"MARKETPLACE"` - `"MONGODB"` - `"NETWORK"` |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **description**  string | The description of the connection. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **match_criteria**  list / elements=string | A list of UTF-8 strings that specify the criteria that you can use in selecting this connection. |
| **name**  string / required | The name of the connection. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_groups**  list / elements=string | A list of security groups to be used by the connection. Use either security group name or ID.  Required when *connection_type=NETWORK*. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string / required | Create or delete the AWS Glue connection.  Choices:   - `"present"` - `"absent"` |
| **subnet_id**  string | The subnet ID used by the connection.  Required when *connection_type=NETWORK*. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](aws_glue_connection_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](aws_glue_connection_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

# Create an AWS Glue connection
- community.aws.aws_glue_connection:
    name: my-glue-connection
    connection_properties:
      JDBC_CONNECTION_URL: jdbc:mysql://mydb:3306/databasename
      USERNAME: my-username
      PASSWORD: my-password
    state: present

# Create an AWS Glue network connection
- community.aws.aws_glue_connection:
    name: my-glue-network-connection
    availability_zone: us-east-1a
    connection_properties:
      JDBC_ENFORCE_SSL: "false"
    connection_type: NETWORK
    description: Test connection
    security_groups:
      - sg-glue
    subnet_id: subnet-123abc
    state: present

# Delete an AWS Glue connection
- community.aws.aws_glue_connection:
    name: my-glue-connection
    state: absent
```

## [Return Values](aws_glue_connection_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **connection_properties**  dictionary | A dict of key-value pairs used as parameters for this connection.  Returned: when state is present  Sample: `{"JDBC_CONNECTION_URL": "jdbc:mysql://mydb:3306/databasename", "PASSWORD": "y", "USERNAME": "x"}` |
| **connection_type**  string | The type of the connection.  Returned: when state is present  Sample: `"JDBC"` |
| **creation_time**  string | The time this connection definition was created.  Returned: when state is present  Sample: `"2018-04-21T05:19:58.326000+00:00"` |
| **description**  string | Description of the job being defined.  Returned: when state is present  Sample: `"My first Glue job"` |
| **last_updated_time**  string | The last time this connection definition was updated.  Returned: when state is present  Sample: `"2018-04-21T05:19:58.326000+00:00"` |
| **match_criteria**  list / elements=string | A list of criteria that can be used in selecting this connection.  Returned: when state is present  Sample: `[]` |
| **name**  string | The name of the connection definition.  Returned: when state is present  Sample: `"my-glue-connection"` |
| **physical_connection_requirements**  dictionary | A dict of physical connection requirements, such as VPC and SecurityGroup, needed for making this connection successfully.  Returned: when state is present  Sample: `{"subnet-id": "subnet-aabbccddee"}` |

### Authors

- Rob White (@wimnat)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
