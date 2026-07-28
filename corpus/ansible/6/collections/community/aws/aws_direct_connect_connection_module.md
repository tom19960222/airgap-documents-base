---
collection: ansible
version: "6"
title: "community.aws.aws_direct_connect_connection module – Creates, deletes, modifies a DirectConnect connection"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/aws_direct_connect_connection_module.html
fetched_at: 2026-07-27T17:03:22+00:00
---
# community.aws.aws_direct_connect_connection module – Creates, deletes, modifies a DirectConnect connection

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
> see [Requirements](aws_direct_connect_connection_module.md#ansible-collections-community-aws-aws-direct-connect-connection-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.aws_direct_connect_connection`.

New in community.aws 1.0.0

- [Synopsis](aws_direct_connect_connection_module.md#synopsis)
- [Requirements](aws_direct_connect_connection_module.md#requirements)
- [Parameters](aws_direct_connect_connection_module.md#parameters)
- [Notes](aws_direct_connect_connection_module.md#notes)
- [Examples](aws_direct_connect_connection_module.md#examples)
- [Return Values](aws_direct_connect_connection_module.md#return-values)

## [Synopsis](aws_direct_connect_connection_module.md#id1)

- Create, update, or delete a Direct Connect connection between a network and a specific AWS Direct Connect location. Upon creation the connection may be added to a link aggregation group or established as a standalone connection. The connection may later be associated or disassociated with a link aggregation group.

## [Requirements](aws_direct_connect_connection_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](aws_direct_connect_connection_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **bandwidth**  string | The bandwidth of the Direct Connect connection.  Required when *state=present*.  Choices:   - `"1Gbps"` - `"10Gbps"` |
| **connection_id**  string | The ID of the Direct Connect connection.  Modifying attributes of a connection with *forced_update* will result in a new Direct Connect connection ID.  One of *connection_id* or *name* must be specified. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **forced_update**  boolean | To modify *bandwidth* or *location* the connection needs to be deleted and recreated.  By default this will not happen. This option must be explicitly set to `true` to change *bandwith* or *location*.  Choices:   - `false` ← (default) - `true` |
| **link_aggregation_group**  string | The ID of the link aggregation group you want to associate with the connection.  This is optional when a stand-alone connection is desired. |
| **location**  string | Where the Direct Connect connection is located.  Required when *state=present*. |
| **name**  string | The name of the Direct Connect connection. This is required to create a new connection.  One of *connection_id* or *name* must be specified. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string / required | The state of the Direct Connect connection.  Choices:   - `"present"` - `"absent"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](aws_direct_connect_connection_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](aws_direct_connect_connection_module.md#id5)

```yaml+jinja
# create a Direct Connect connection
- community.aws.aws_direct_connect_connection:
    name: ansible-test-connection
    state: present
    location: EqDC2
    link_aggregation_group: dxlag-xxxxxxxx
    bandwidth: 1Gbps
  register: dc

# disassociate the LAG from the connection
- community.aws.aws_direct_connect_connection:
    state: present
    connection_id: dc.connection.connection_id
    location: EqDC2
    bandwidth: 1Gbps

# replace the connection with one with more bandwidth
- community.aws.aws_direct_connect_connection:
    state: present
    name: ansible-test-connection
    location: EqDC2
    bandwidth: 10Gbps
    forced_update: true

# delete the connection
- community.aws.aws_direct_connect_connection:
    state: absent
    name: ansible-test-connection
```

## [Return Values](aws_direct_connect_connection_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **connection**  complex | The attributes of the direct connect connection.  Returned: *state=present* |
| **aws_device**  string | The endpoint which the physical connection terminates on.  Returned: when the requested state is no longer ‘requested’  Sample: `"EqDC2-12pmo7hemtz1z"` |
| **bandwidth**  string | The bandwidth of the connection.  Returned: always  Sample: `"1Gbps"` |
| **connection_id**  string | The ID of the connection.  Returned: always  Sample: `"dxcon-ffy9ywed"` |
| **connection_name**  string | The name of the connection.  Returned: always  Sample: `"ansible-test-connection"` |
| **connection_state**  string | The state of the connection.  Returned: always  Sample: `"pending"` |
| **loa_issue_time**  string | The issue time of the connection’s Letter of Authorization - Connecting Facility Assignment.  Returned: when the LOA-CFA has been issued (the connection state will no longer be ‘requested’)  Sample: `"2018-03-20T17:36:26-04:00"` |
| **location**  string | The location of the connection.  Returned: always  Sample: `"EqDC2"` |
| **owner_account**  string | The account that owns the direct connect connection.  Returned: always  Sample: `"123456789012"` |
| **region**  string | The region in which the connection exists.  Returned: always  Sample: `"us-east-1"` |

### Authors

- Sloane Hertel (@s-hertel)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
