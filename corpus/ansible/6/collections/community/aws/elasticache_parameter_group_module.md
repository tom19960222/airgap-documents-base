---
collection: ansible
version: "6"
title: "community.aws.elasticache_parameter_group module – Manage cache parameter groups in Amazon ElastiCache."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/elasticache_parameter_group_module.html
fetched_at: 2026-07-27T17:04:25+00:00
---
# community.aws.elasticache_parameter_group module – Manage cache parameter groups in Amazon ElastiCache.

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
> see [Requirements](elasticache_parameter_group_module.md#ansible-collections-community-aws-elasticache-parameter-group-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.elasticache_parameter_group`.

New in community.aws 1.0.0

- [Synopsis](elasticache_parameter_group_module.md#synopsis)
- [Requirements](elasticache_parameter_group_module.md#requirements)
- [Parameters](elasticache_parameter_group_module.md#parameters)
- [Notes](elasticache_parameter_group_module.md#notes)
- [Examples](elasticache_parameter_group_module.md#examples)
- [Return Values](elasticache_parameter_group_module.md#return-values)

## [Synopsis](elasticache_parameter_group_module.md#id1)

- Manage cache security groups in Amazon ElastiCache.
- Returns information about the specified cache cluster.

## [Requirements](elasticache_parameter_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](elasticache_parameter_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **description**  string | A user-specified description for the cache parameter group. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **group_family**  string | The name of the cache parameter group family that the cache parameter group can be used with. Required when creating a cache parameter group.  Choices:   - `"memcached1.4"` - `"memcached1.5"` - `"redis2.6"` - `"redis2.8"` - `"redis3.2"` - `"redis4.0"` - `"redis5.0"` |
| **name**  string / required | A user-specified name for the cache parameter group. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string / required | Idempotent actions that will create/modify, destroy, or reset a cache parameter group as needed.  Choices:   - `"present"` - `"absent"` - `"reset"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **values**  dictionary | A user-specified dictionary of parameters to reset or modify for the cache parameter group. |

## [Notes](elasticache_parameter_group_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](elasticache_parameter_group_module.md#id5)

```yaml+jinja
# Note: None of these examples set aws_access_key, aws_secret_key, or region.
# It is assumed that their matching environment variables are set.
---
- hosts: localhost
  connection: local
  tasks:
    - name: 'Create a test parameter group'
      community.aws.elasticache_parameter_group:
        name: 'test-param-group'
        group_family: 'redis3.2'
        description: 'This is a cache parameter group'
        state: 'present'
    - name: 'Modify a test parameter group'
      community.aws.elasticache_parameter_group:
        name: 'test-param-group'
        values:
          activerehashing: yes
          client-output-buffer-limit-normal-hard-limit: 4
        state: 'present'
    - name: 'Reset all modifiable parameters for the test parameter group'
      community.aws.elasticache_parameter_group:
        name: 'test-param-group'
        state: reset
    - name: 'Delete a test parameter group'
      community.aws.elasticache_parameter_group:
        name: 'test-param-group'
        state: 'absent'
```

## [Return Values](elasticache_parameter_group_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | if the cache parameter group has changed  Returned: always  Sample: `{"changed": true}` |
| **elasticache**  dictionary | cache parameter group information and response metadata  Returned: always  Sample: `{"cache_parameter_group": {"cache_parameter_group_family": "redis3.2", "cache_parameter_group_name": "test-please-delete", "description": "initial description"}, "response_metadata": {"http_headers": {"content-length": "562", "content-type": "text/xml", "date": "Mon, 06 Feb 2017 22:14:08 GMT", "x-amzn-requestid": "947291f9-ecb9-11e6-85bd-3baa4eca2cc1"}, "http_status_code": 200, "request_id": "947291f9-ecb9-11e6-85bd-3baa4eca2cc1", "retry_attempts": 0}}` |

### Authors

- Sloane Hertel (@s-hertel)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
