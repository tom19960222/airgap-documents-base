---
collection: ansible
version: "8"
title: "community.aws.glue_connection module – Manage an AWS Glue connection"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/glue_connection_module.html
fetched_at: 2026-07-28T01:41:17+00:00
---
# community.aws.glue_connection module – Manage an AWS Glue connection

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
> see [Requirements](glue_connection_module.md#ansible-collections-community-aws-glue-connection-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.glue_connection`.

New in community.aws 1.0.0

- [Synopsis](glue_connection_module.md#synopsis)
- [Requirements](glue_connection_module.md#requirements)
- [Parameters](glue_connection_module.md#parameters)
- [Notes](glue_connection_module.md#notes)
- [Examples](glue_connection_module.md#examples)
- [Return Values](glue_connection_module.md#return-values)

## [Synopsis](glue_connection_module.md#id1)

- Manage an AWS Glue connection. See <https://aws.amazon.com/glue/> for details.
- Prior to release 5.0.0 this module was called `community.aws.aws_glue_connection`. The usage did not change.

Aliases: aws_glue_connection

## [Requirements](glue_connection_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](glue_connection_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **availability_zone**  string  *added in community.aws 1.5.0* | Availability Zone used by the connection  Required when *connection_type=NETWORK*. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **catalog_id**  string | The ID of the Data Catalog in which to create the connection. If none is supplied, the AWS account ID is used by default. |
| **connection_properties**  dictionary | A dict of key-value pairs used as parameters for this connection.  Required when *state=present*. |
| **connection_type**  string | The type of the connection. Currently, SFTP is not supported.  **Choices:**   - `"CUSTOM"` - `"JDBC"` ← (default) - `"KAFKA"` - `"MARKETPLACE"` - `"MONGODB"` - `"NETWORK"` |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **description**  string | The description of the connection. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **match_criteria**  list / elements=string | A list of UTF-8 strings that specify the criteria that you can use in selecting this connection. |
| **name**  string / required | The name of the connection. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **security_groups**  list / elements=string | A list of security groups to be used by the connection. Use either security group name or ID.  Required when *connection_type=NETWORK*. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string / required | Create or delete the AWS Glue connection.  **Choices:**   - `"present"` - `"absent"` |
| **subnet_id**  string | The subnet ID used by the connection.  Required when *connection_type=NETWORK*. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](glue_connection_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](glue_connection_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

# Create an AWS Glue connection
- community.aws.glue_connection:
    name: my-glue-connection
    connection_properties:
      JDBC_CONNECTION_URL: jdbc:mysql://mydb:3306/databasename
      USERNAME: my-username
      PASSWORD: my-password
    state: present

# Create an AWS Glue network connection
- community.aws.glue_connection:
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
- community.aws.glue_connection:
    name: my-glue-connection
    state: absent
```

## [Return Values](glue_connection_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **connection_properties**  dictionary | (deprecated) A dict of key-value pairs (converted to lowercase) used as parameters for this connection.  This return key has been deprecated, and will be removed in a release after 2024-06-01.  **Returned:** when state is present  **Sample:** `{"jdbc_connection_url": "jdbc:mysql://mydb:3306/databasename", "password": "y", "username": "x"}` |
| **connection_type**  string | The type of the connection.  **Returned:** when state is present  **Sample:** `"JDBC"` |
| **creation_time**  string | The time this connection definition was created.  **Returned:** when state is present  **Sample:** `"2018-04-21T05:19:58.326000+00:00"` |
| **description**  string | Description of the job being defined.  **Returned:** when state is present  **Sample:** `"My first Glue job"` |
| **last_updated_time**  string | The last time this connection definition was updated.  **Returned:** when state is present  **Sample:** `"2018-04-21T05:19:58.326000+00:00"` |
| **match_criteria**  list / elements=string | A list of criteria that can be used in selecting this connection.  **Returned:** when state is present  **Sample:** `[]` |
| **name**  string | The name of the connection definition.  **Returned:** when state is present  **Sample:** `"my-glue-connection"` |
| **physical_connection_requirements**  dictionary | A dict of physical connection requirements, such as VPC and SecurityGroup, needed for making this connection successfully.  **Returned:** when state is present  **Sample:** `{"subnet-id": "subnet-aabbccddee"}` |
| **raw_connection_properties**  dictionary | A dict of key-value pairs used as parameters for this connection.  **Returned:** when state is present  **Sample:** `{"JDBC_CONNECTION_URL": "jdbc:mysql://mydb:3306/databasename", "PASSWORD": "y", "USERNAME": "x"}` |

### Authors

- Rob White (@wimnat)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
