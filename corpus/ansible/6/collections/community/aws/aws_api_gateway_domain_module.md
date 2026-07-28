---
collection: ansible
version: "6"
title: "community.aws.aws_api_gateway_domain module – Manage AWS API Gateway custom domains"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/aws_api_gateway_domain_module.html
fetched_at: 2026-07-27T17:03:12+00:00
---
# community.aws.aws_api_gateway_domain module – Manage AWS API Gateway custom domains

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
> see [Requirements](aws_api_gateway_domain_module.md#ansible-collections-community-aws-aws-api-gateway-domain-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.aws_api_gateway_domain`.

New in community.aws 3.3.0

- [Synopsis](aws_api_gateway_domain_module.md#synopsis)
- [Requirements](aws_api_gateway_domain_module.md#requirements)
- [Parameters](aws_api_gateway_domain_module.md#parameters)
- [Notes](aws_api_gateway_domain_module.md#notes)
- [Examples](aws_api_gateway_domain_module.md#examples)
- [Return Values](aws_api_gateway_domain_module.md#return-values)

## [Synopsis](aws_api_gateway_domain_module.md#id1)

- Manages API Gateway custom domains for API GW Rest APIs.
- AWS API Gateway custom domain setups use CloudFront behind the scenes. So you will get a CloudFront distribution as a result, configured to be aliased with your domain.

## [Requirements](aws_api_gateway_domain_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](aws_api_gateway_domain_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **certificate_arn**  string / required | AWS Certificate Manger (ACM) TLS certificate ARN. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **domain_mappings**  list / elements=dictionary / required | Map your domain base paths to your API GW REST APIs, that you previously created. Use provided ID of the API setup and the release stage.  domain_mappings should be a list of dictionaries containing three keys: base_path, rest_api_id and stage.  Example: *[{ base_path: v1, rest_api_id: abc123, stage: production }]*  if you want base path to be just */* omit the param completely or set it to empty string. |
| **domain_name**  string / required | Domain name you want to use for your API GW deployment. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **endpoint_type**  string | API endpoint configuration for domain. Use EDGE for edge-optimized endpoint, or use `REGIONAL` or `PRIVATE`.  Choices:   - `"EDGE"` ← (default) - `"REGIONAL"` - `"PRIVATE"` |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_policy**  string | Set allowed TLS versions through AWS defined policies. Currently only `TLS_1_0` and `TLS_1_2` are available.  Choices:   - `"TLS_1_0"` - `"TLS_1_2"` ← (default) |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Create or delete custom domain setup.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](aws_api_gateway_domain_module.md#id4)

> **Note:**
>
> - Does not create a DNS entry on Route53, for that use the route53 module.
> - Only supports TLS certificates from AWS ACM that can just be referenced by the ARN, while the AWS API still offers (deprecated) options to add own Certificates.
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](aws_api_gateway_domain_module.md#id5)

```yaml+jinja
- name: Setup endpoint for a custom domain for your API Gateway HTTP API
  community.aws.aws_api_gateway_domain:
    domain_name: myapi.foobar.com
    certificate_arn: 'arn:aws:acm:us-east-1:1231123123:certificate/8bd89412-abc123-xxxxx'
    security_policy: TLS_1_2
    endpoint_type: EDGE
    domain_mappings:
        - { rest_api_id: abc123, stage: production }
    state: present
  register: api_gw_domain_result

- name: Create a DNS record for your custom domain on route 53 (using route53 module)
  community.aws.route53:
    record: myapi.foobar.com
    value: "{{ api_gw_domain_result.response.domain.distribution_domain_name }}"
    type: A
    alias: true
    zone: foobar.com
    alias_hosted_zone_id: "{{ api_gw_domain_result.response.domain.distribution_hosted_zone_id }}"
    command: create
```

## [Return Values](aws_api_gateway_domain_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **response**  dictionary | The data returned by create_domain_name (or update and delete) and create_base_path_mapping methods by boto3.  Returned: success  Sample: `{"domain": {"certificate_arn": "arn:aws:acm:xxxxxx", "distribution_domain_name": "xxxx.cloudfront.net", "distribution_hosted_zone_id": "ABC123123", "domain_name": "mydomain.com", "domain_name_status": "AVAILABLE", "endpoint_configuration": {"types": ["EDGE"]}, "security_policy": "TLS_1_2", "tags": {}}, "path_mappings": [{"base_path": "(empty)", "rest_api_id": "abcd123", "stage": "production"}]}` |

### Authors

- Stefan Horning (@stefanhorning)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
