---
collection: ansible
version: "8"
title: "community.aws.directconnect_connection module – Creates, deletes, modifies a DirectConnect connection"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/directconnect_connection_module.html
fetched_at: 2026-07-28T01:40:32+00:00
---
# community.aws.directconnect_connection module – Creates, deletes, modifies a DirectConnect connection

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
> see [Requirements](directconnect_connection_module.md#ansible-collections-community-aws-directconnect-connection-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.directconnect_connection`.

New in community.aws 1.0.0

- [Synopsis](directconnect_connection_module.md#synopsis)
- [Requirements](directconnect_connection_module.md#requirements)
- [Parameters](directconnect_connection_module.md#parameters)
- [Notes](directconnect_connection_module.md#notes)
- [Examples](directconnect_connection_module.md#examples)
- [Return Values](directconnect_connection_module.md#return-values)

## [Synopsis](directconnect_connection_module.md#id1)

- Create, update, or delete a Direct Connect connection between a network and a specific AWS Direct Connect location.
- Upon creation the connection may be added to a link aggregation group or established as a standalone connection.
- The connection may later be associated or disassociated with a link aggregation group.
- Prior to release 5.0.0 this module was called `community.aws.aws_direct_connect_connection`. The usage did not change.

Aliases: aws_direct_connect_connection

## [Requirements](directconnect_connection_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](directconnect_connection_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **bandwidth**  string | The bandwidth of the Direct Connect connection.  Required when *state=present*.  **Choices:**   - `"1Gbps"` - `"10Gbps"` |
| **connection_id**  string | The ID of the Direct Connect connection.  Modifying attributes of a connection with *forced_update* will result in a new Direct Connect connection ID.  One of *connection_id* or *name* must be specified. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **forced_update**  boolean | To modify *bandwidth* or *location* the connection needs to be deleted and recreated.  By default this will not happen. This option must be explicitly set to `true` to change *bandwith* or *location*.  **Choices:**   - `false` ← (default) - `true` |
| **link_aggregation_group**  string | The ID of the link aggregation group you want to associate with the connection.  This is optional when a stand-alone connection is desired. |
| **location**  string | Where the Direct Connect connection is located.  Required when *state=present*. |
| **name**  string | The name of the Direct Connect connection. This is required to create a new connection.  One of *connection_id* or *name* must be specified. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string / required | The state of the Direct Connect connection.  **Choices:**   - `"present"` - `"absent"` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](directconnect_connection_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](directconnect_connection_module.md#id5)

```yaml+jinja
# create a Direct Connect connection
- community.aws.directconnect_connection:
    name: ansible-test-connection
    state: present
    location: EqDC2
    link_aggregation_group: dxlag-xxxxxxxx
    bandwidth: 1Gbps
  register: dc

# disassociate the LAG from the connection
- community.aws.directconnect_connection:
    state: present
    connection_id: dc.connection.connection_id
    location: EqDC2
    bandwidth: 1Gbps

# replace the connection with one with more bandwidth
- community.aws.directconnect_connection:
    state: present
    name: ansible-test-connection
    location: EqDC2
    bandwidth: 10Gbps
    forced_update: true

# delete the connection
- community.aws.directconnect_connection:
    state: absent
    name: ansible-test-connection
```

## [Return Values](directconnect_connection_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **connection**  complex | The attributes of the direct connect connection.  **Returned:** *state=present* |
| **aws_device**  string | The endpoint which the physical connection terminates on.  **Returned:** when the requested state is no longer ‘requested’  **Sample:** `"EqDC2-12pmo7hemtz1z"` |
| **bandwidth**  string | The bandwidth of the connection.  **Returned:** always  **Sample:** `"1Gbps"` |
| **connection_id**  string | The ID of the connection.  **Returned:** always  **Sample:** `"dxcon-ffy9ywed"` |
| **connection_name**  string | The name of the connection.  **Returned:** always  **Sample:** `"ansible-test-connection"` |
| **connection_state**  string | The state of the connection.  **Returned:** always  **Sample:** `"pending"` |
| **loa_issue_time**  string | The issue time of the connection’s Letter of Authorization - Connecting Facility Assignment.  **Returned:** when the LOA-CFA has been issued (the connection state will no longer be ‘requested’)  **Sample:** `"2018-03-20T17:36:26-04:00"` |
| **location**  string | The location of the connection.  **Returned:** always  **Sample:** `"EqDC2"` |
| **owner_account**  string | The account that owns the direct connect connection.  **Returned:** always  **Sample:** `"123456789012"` |
| **region**  string | The region in which the connection exists.  **Returned:** always  **Sample:** `"us-east-1"` |

### Authors

- Sloane Hertel (@s-hertel)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
