---
collection: ansible
version: "8"
title: "community.aws.route53_wait module – wait for changes in Amazons Route 53 DNS service to propagate"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/route53_wait_module.html
fetched_at: 2026-07-28T01:41:46+00:00
---
# community.aws.route53_wait module – wait for changes in Amazons Route 53 DNS service to propagate

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
> see [Requirements](route53_wait_module.md#ansible-collections-community-aws-route53-wait-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.route53_wait`.

New in community.aws 6.3.0

- [Synopsis](route53_wait_module.md#synopsis)
- [Requirements](route53_wait_module.md#requirements)
- [Parameters](route53_wait_module.md#parameters)
- [Notes](route53_wait_module.md#notes)
- [Examples](route53_wait_module.md#examples)

## [Synopsis](route53_wait_module.md#id1)

- When using [amazon.aws.route53](../../amazon/aws/route53_module.md#ansible-collections-amazon-aws-route53-module) with *wait=false*, this module allows to wait for the module’s propagation to finish at a later point of time.

## [Requirements](route53_wait_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](route53_wait_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  string | This setting is ignored by the module. It is only present to make it possible to have *region* present in the module default group. |
| **result**  aliases: results  dictionary / required | The registered result of one or multiple [amazon.aws.route53](../../amazon/aws/route53_module.md#ansible-collections-amazon-aws-route53-module) invocations. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **wait_timeout**  integer | How long to wait for the changes to be replicated, in seconds.  This timeout will be used for every changed result in *result*.  **Default:** `300` |

## [Notes](route53_wait_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](route53_wait_module.md#id5)

```yaml+jinja
# Example when using a single route53 invocation:

- name: Add new.foo.com as an A record with 3 IPs
  amazon.aws.route53:
    state: present
    zone: foo.com
    record: new.foo.com
    type: A
    ttl: 7200
    value:
      - 1.1.1.1
      - 2.2.2.2
      - 3.3.3.3
  register: module_result

# do something else

- name: Wait for the changes of the above route53 invocation to propagate
  community.aws.route53_wait:
    result: "{{ module_result }}"

#########################################################################
# Example when using a loop over amazon.aws.route53:

- name: Add various A records
  amazon.aws.route53:
    state: present
    zone: foo.com
    record: "{{ item.record }}"
    type: A
    ttl: 300
    value: "{{ item.value }}"
  loop:
    - record: new.foo.com
      value: 1.1.1.1
    - record: foo.foo.com
      value: 2.2.2.2
    - record: bar.foo.com
      value:
        - 3.3.3.3
        - 4.4.4.4
  register: module_results

# do something else

- name: Wait for the changes of the above three route53 invocations to propagate
  community.aws.route53_wait:
    results: "{{ module_results }}"
```

### Authors

- Felix Fontein (@felixfontein)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
