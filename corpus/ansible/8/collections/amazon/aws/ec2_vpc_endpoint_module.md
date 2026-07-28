---
collection: ansible
version: "8"
title: "amazon.aws.ec2_vpc_endpoint module – Create and delete AWS VPC endpoints"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/ec2_vpc_endpoint_module.html
fetched_at: 2026-07-28T01:06:38+00:00
---
# amazon.aws.ec2_vpc_endpoint module – Create and delete AWS VPC endpoints

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
> see [Requirements](ec2_vpc_endpoint_module.md#ansible-collections-amazon-aws-ec2-vpc-endpoint-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.ec2_vpc_endpoint`.

New in amazon.aws 1.0.0

- [Synopsis](ec2_vpc_endpoint_module.md#synopsis)
- [Requirements](ec2_vpc_endpoint_module.md#requirements)
- [Parameters](ec2_vpc_endpoint_module.md#parameters)
- [Notes](ec2_vpc_endpoint_module.md#notes)
- [Examples](ec2_vpc_endpoint_module.md#examples)
- [Return Values](ec2_vpc_endpoint_module.md#return-values)

## [Synopsis](ec2_vpc_endpoint_module.md#id1)

- Creates AWS VPC endpoints.
- Deletes AWS VPC endpoints.
- This module supports check mode.

## [Requirements](ec2_vpc_endpoint_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ec2_vpc_endpoint_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **client_token**  string | Optional client token to ensure idempotency. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **policy**  json | A properly formatted JSON policy as string, see <https://github.com/ansible/ansible/issues/7005#issuecomment-42894813>.  Option when creating an endpoint. If not provided AWS will utilise a default policy which provides full access to the service. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **route_table_ids**  list / elements=string | List of one or more route table IDs to attach to the endpoint.  A route is added to the route table with the destination of the endpoint if provided.  Route table IDs are only valid for `Gateway` endpoints. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **service**  string | An AWS supported VPC endpoint service. Use the [amazon.aws.ec2_vpc_endpoint_info](ec2_vpc_endpoint_info_module.md#ansible-collections-amazon-aws-ec2-vpc-endpoint-info-module) module to describe the supported endpoint services.  Required when creating an endpoint. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | `present` to ensure resource is created.  `absent` to remove resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **vpc_endpoint_id**  string | One or more VPC endpoint IDs to remove from the AWS account.  Required if *state=absent*. |
| **vpc_endpoint_security_groups**  list / elements=string  *added in amazon.aws 2.1.0* | The list of security groups to attach to the endpoint.  Requires *vpc_endpoint_type=GatewayLoadBalancer* or *vpc_endpoint_type=Interface*. |
| **vpc_endpoint_subnets**  list / elements=string  *added in amazon.aws 2.1.0* | The list of subnets to attach to the endpoint.  Requires *vpc_endpoint_type=GatewayLoadBalancer* or *vpc_endpoint_type=Interface*. |
| **vpc_endpoint_type**  string  *added in amazon.aws 1.5.0* | The type of endpoint.  **Choices:**   - `"Interface"` - `"Gateway"` ← (default) - `"GatewayLoadBalancer"` |
| **vpc_id**  string | Required when creating a VPC endpoint. |
| **wait**  boolean | When specified, will wait for status to reach `available` for *state=present*.  Unfortunately this is ignored for delete actions due to a difference in behaviour from AWS.  **Choices:**   - `false` ← (default) - `true` |
| **wait_timeout**  integer | Used in conjunction with *wait*.  Number of seconds to wait for status.  Unfortunately this is ignored for delete actions due to a difference in behaviour from AWS.  **Default:** `320` |

## [Notes](ec2_vpc_endpoint_module.md#id4)

> **Note:**
>
> - Support for *tags* and *purge_tags* was added in release 1.5.0.
> - The `policy_file` paramater was removed in release 6.0.0 please use the *policy* option and a file lookup instead.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](ec2_vpc_endpoint_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Create new vpc endpoint with a json template for policy
  amazon.aws.ec2_vpc_endpoint:
    state: present
    region: ap-southeast-2
    vpc_id: vpc-12345678
    service: com.amazonaws.ap-southeast-2.s3
    policy: " {{ lookup( 'template', 'endpoint_policy.json.j2') }} "
    route_table_ids:
      - rtb-12345678
      - rtb-87654321
  register: new_vpc_endpoint

- name: Create new vpc endpoint with the default policy
  amazon.aws.ec2_vpc_endpoint:
    state: present
    region: ap-southeast-2
    vpc_id: vpc-12345678
    service: com.amazonaws.ap-southeast-2.s3
    route_table_ids:
      - rtb-12345678
      - rtb-87654321
  register: new_vpc_endpoint

- name: Delete newly created vpc endpoint
  amazon.aws.ec2_vpc_endpoint:
    state: absent
    vpc_endpoint_id: "{{ new_vpc_endpoint.result['VpcEndpointId'] }}"
    region: ap-southeast-2
```

## [Return Values](ec2_vpc_endpoint_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **endpoints**  list / elements=string | The resulting endpoints from the module call  **Returned:** success  **Sample:** `[{"creation_timestamp": "2017-02-20T05:04:15+00:00", "policy_document": {"Id": "Policy1450910922815", "Statement": [{"Action": "s3:*", "Effect": "Allow", "Principal": "*", "Resource": ["arn:aws:s3:::*/*", "arn:aws:s3:::*"], "Sid": "Stmt1450910920641"}], "Version": "2012-10-17"}, "route_table_ids": ["rtb-abcd1234"], "service_name": "com.amazonaws.ap-southeast-2.s3", "vpc_endpoint_id": "vpce-a1b2c3d4", "vpc_id": "vpc-abbad0d0"}]` |

### Authors

- Karen Cheng (@Etherdaemon)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
