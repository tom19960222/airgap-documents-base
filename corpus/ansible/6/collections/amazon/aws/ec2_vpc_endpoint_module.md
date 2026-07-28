---
collection: ansible
version: "6"
title: "amazon.aws.ec2_vpc_endpoint module – Create and delete AWS VPC Endpoints."
source_url: https://docs.ansible.com/projects/ansible/6/collections/amazon/aws/ec2_vpc_endpoint_module.html
fetched_at: 2026-07-27T16:43:49+00:00
---
# amazon.aws.ec2_vpc_endpoint module – Create and delete AWS VPC Endpoints.

> **Note:**
>
> This module is part of the [amazon.aws collection](https://galaxy.ansible.com/amazon/aws) (version 3.5.0).
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
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_vpc_endpoint_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **client_token**  string | Optional client token to ensure idempotency |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **policy**  json | A properly formatted json policy as string, see <https://github.com/ansible/ansible/issues/7005#issuecomment-42894813>. Cannot be used with *policy_file*.  Option when creating an endpoint. If not provided AWS will utilise a default policy which provides full access to the service. |
| **policy_file**  aliases: policy_path  path | The path to the properly json formatted policy file, see <https://github.com/ansible/ansible/issues/7005#issuecomment-42894813> on how to use it properly. Cannot be used with *policy*.  Option when creating an endpoint. If not provided AWS will utilise a default policy which provides full access to the service.  This option has been deprecated and will be removed after 2022-12-01 to maintain the existing functionality please use the *policy* option and a file lookup. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_tags**  boolean  added in amazon.aws 1.5.0 | Delete any tags not specified in the task that are on the instance. This means you have to specify all the desired tags on each task affecting an instance.  Choices:   - `false` ← (default) - `true` |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **route_table_ids**  list / elements=string | List of one or more route table ids to attach to the endpoint. A route is added to the route table with the destination of the endpoint if provided.  Route table ids are only valid for gateway type endpoints. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **service**  string | An AWS supported vpc endpoint service. Use the [amazon.aws.ec2_vpc_endpoint_info](ec2_vpc_endpoint_info_module.md#ansible-collections-amazon-aws-ec2-vpc-endpoint-info-module) module to describe the supported endpoint services.  Required when creating an endpoint. |
| **state**  string | present to ensure resource is created.  absent to remove resource  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  dictionary  added in amazon.aws 1.5.0 | A dict of tags to apply to the internet gateway.  To remove all tags set *tags={}* and *purge_tags=true*. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **vpc_endpoint_id**  string | One or more vpc endpoint ids to remove from the AWS account |
| **vpc_endpoint_security_groups**  list / elements=string  added in amazon.aws 2.1.0 | The list of security groups to attach to the endpoint.  Requires *vpc_endpoint_type=GatewayLoadBalancer* or *vpc_endpoint_type=Interface*. |
| **vpc_endpoint_subnets**  list / elements=string  added in amazon.aws 2.1.0 | The list of subnets to attach to the endpoint.  Requires *vpc_endpoint_type=GatewayLoadBalancer* or *vpc_endpoint_type=Interface*. |
| **vpc_endpoint_type**  string  added in amazon.aws 1.5.0 | The type of endpoint.  Choices:   - `"Interface"` - `"Gateway"` ← (default) - `"GatewayLoadBalancer"` |
| **vpc_id**  string | Required when creating a VPC endpoint. |
| **wait**  boolean | When specified, will wait for either available status for state present. Unfortunately this is ignored for delete actions due to a difference in behaviour from AWS.  Choices:   - `false` ← (default) - `true` |
| **wait_timeout**  integer | Used in conjunction with wait. Number of seconds to wait for status. Unfortunately this is ignored for delete actions due to a difference in behaviour from AWS.  Default: `320` |

## [Notes](ec2_vpc_endpoint_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

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

- name: Create new vpc endpoint with json file
  amazon.aws.ec2_vpc_endpoint:
    state: present
    region: ap-southeast-2
    vpc_id: vpc-12345678
    service: com.amazonaws.ap-southeast-2.s3
    policy_file: "{{ role_path }}/files/endpoint_policy.json"
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
| **endpoints**  list / elements=string | The resulting endpoints from the module call  Returned: success  Sample: `[{"creation_timestamp": "2017-02-20T05:04:15+00:00", "policy_document": {"Id": "Policy1450910922815", "Statement": [{"Action": "s3:*", "Effect": "Allow", "Principal": "*", "Resource": ["arn:aws:s3:::*/*", "arn:aws:s3:::*"], "Sid": "Stmt1450910920641"}], "Version": "2012-10-17"}, "route_table_ids": ["rtb-abcd1234"], "service_name": "com.amazonaws.ap-southeast-2.s3", "vpc_endpoint_id": "vpce-a1b2c3d4", "vpc_id": "vpc-abbad0d0"}]` |

### Authors

- Karen Cheng (@Etherdaemon)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
[Communication](index.md#communication-for-amazon-aws)
