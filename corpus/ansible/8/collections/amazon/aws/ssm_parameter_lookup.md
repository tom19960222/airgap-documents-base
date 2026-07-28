---
collection: ansible
version: "8"
title: "amazon.aws.ssm_parameter lookup – gets the value for a SSM parameter or all parameters under a path"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/ssm_parameter_lookup.html
fetched_at: 2026-07-28T01:05:31+00:00
---
# amazon.aws.ssm_parameter lookup – gets the value for a SSM parameter or all parameters under a path

> **Note:**
>
> This lookup plugin is part of the [amazon.aws collection](https://galaxy.ansible.com/ui/repo/published/amazon/aws/) (version 6.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install amazon.aws`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](ssm_parameter_lookup.md#ansible-collections-amazon-aws-ssm-parameter-lookup-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.ssm_parameter`.

- [Synopsis](ssm_parameter_lookup.md#synopsis)
- [Requirements](ssm_parameter_lookup.md#requirements)
- [Keyword parameters](ssm_parameter_lookup.md#keyword-parameters)
- [Notes](ssm_parameter_lookup.md#notes)
- [Examples](ssm_parameter_lookup.md#examples)

## [Synopsis](ssm_parameter_lookup.md#id1)

- Get the value for an Amazon Simple Systems Manager parameter or a hierarchy of parameters. The first argument you pass the lookup can either be a parameter name or a hierarchy of parameters. Hierarchies start with a forward slash and end with the parameter name. Up to 5 layers may be specified.
- If looking up an explicitly listed parameter by name which does not exist then the lookup will generate an error. You can use the `default` filter to give a default value in this case but must set the *on_missing* parameter to `skip` or `warn`. You must also set the second parameter of the `default` filter to `true` (see examples below).
- When looking up a path for parameters under it a dictionary will be returned for each path. If there is no parameter under that path then the lookup will generate an error.
- If the lookup fails due to lack of permissions or due to an AWS client error then the aws_ssm will generate an error. If you want to continue in this case then you will have to set up two ansible tasks, one which sets a variable and ignores failures and one which uses the value of that variable with a default. See the examples below.
- Prior to release 6.0.0 this module was known as `aws_ssm`, the usage remains the same.

Aliases: aws_ssm

## [Requirements](ssm_parameter_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Keyword parameters](ssm_parameter_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('amazon.aws.ssm_parameter', key1=value1, key2=value2, ...)` and `query('amazon.aws.ssm_parameter', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  **Configuration:**   - Environment variable: [`AWS_ACCESS_KEY_ID`](../../environment_variables.md#envvar-AWS_ACCESS_KEY_ID) - Environment variable: [`AWS_ACCESS_KEY`](../../environment_variables.md#envvar-AWS_ACCESS_KEY) - Environment variable: [`EC2_ACCESS_KEY`](../../environment_variables.md#envvar-EC2_ACCESS_KEY)  Removed in: major release after 2024-12-01  Why: EC2 in the name implied it was limited to EC2 resources. However, it is used for all connections.  Alternative: AWS_ACCESS_KEY_ID |
| **bypath**  boolean | A boolean to indicate whether the parameter is provided as a hierarchy.  **Choices:**   - `false` ← (default) - `true` |
| **decrypt**  boolean | A boolean to indicate whether to decrypt the parameter.  **Choices:**   - `false` - `true` ← (default) |
| **endpoint_url**  aliases: aws_endpoint_url, endpoint  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The *endpoint* alias has been deprecated and will be removed in a release after 2024-12-01.  **Configuration:**   - Environment variable: [`AWS_URL`](../../environment_variables.md#envvar-AWS_URL) - Environment variable: [`EC2_URL`](../../environment_variables.md#envvar-EC2_URL)  Removed in: major release after 2024-12-01  Why: EC2 in the name implied it was limited to EC2 resources. However, it is used for all connections.  Alternative: AWS_URL |
| **on_denied**  string  *added in amazon.aws 2.0.0* | Action to take if access to the SSM parameter is denied.  `error` will raise a fatal error when access to the SSM parameter is denied.  `skip` will silently ignore the denied SSM parameter.  `warn` will skip over the denied SSM parameter but issue a warning.  **Choices:**   - `"error"` ← (default) - `"skip"` - `"warn"` |
| **on_missing**  string  *added in amazon.aws 2.0.0* | Action to take if the SSM parameter is missing.  `error` will raise a fatal error when the SSM parameter is missing.  `skip` will silently ignore the missing SSM parameter.  `warn` will skip over the missing SSM parameter but issue a warning.  **Choices:**   - `"error"` ← (default) - `"skip"` - `"warn"` |
| **profile**  aliases: aws_profile, boto_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options.  The *boto_profile* alias has been deprecated and will be removed in a release after 2024-12-01.  **Configuration:**   - Environment variable: [`AWS_PROFILE`](../../environment_variables.md#envvar-AWS_PROFILE) - Environment variable: [`AWS_DEFAULT_PROFILE`](../../environment_variables.md#envvar-AWS_DEFAULT_PROFILE) |
| **recursive**  boolean | A boolean to indicate whether to retrieve all parameters within a hierarchy.  **Choices:**   - `false` ← (default) - `true` |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  **Configuration:**   - Environment variable: [`AWS_REGION`](../../environment_variables.md#envvar-AWS_REGION) - Environment variable: [`EC2_REGION`](../../environment_variables.md#envvar-EC2_REGION)  Removed in: major release after 2024-12-01  Why: EC2 in the name implied it was limited to EC2 resources, when it is used for all connections  Alternative: |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  **Configuration:**   - Environment variable: [`AWS_SECRET_ACCESS_KEY`](../../environment_variables.md#envvar-AWS_SECRET_ACCESS_KEY) - Environment variable: [`AWS_SECRET_KEY`](../../environment_variables.md#envvar-AWS_SECRET_KEY) - Environment variable: [`EC2_SECRET_KEY`](../../environment_variables.md#envvar-EC2_SECRET_KEY)  Removed in: major release after 2024-12-01  Why: EC2 in the name implied it was limited to EC2 resources. However, it is used for all connections.  Alternative: AWS_SECRET_ACCESS_KEY |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  **Configuration:**   - Environment variable: [`AWS_SESSION_TOKEN`](../../environment_variables.md#envvar-AWS_SESSION_TOKEN) - Environment variable: [`AWS_SECURITY_TOKEN`](../../environment_variables.md#envvar-AWS_SECURITY_TOKEN)  Removed in: major release after 2024-12-01  Why: AWS_SECURITY_TOKEN was used for compatibility with the original boto SDK, support for which has been dropped  Alternative: AWS_SESSION_TOKEN - Environment variable: [`EC2_SECURITY_TOKEN`](../../environment_variables.md#envvar-EC2_SECURITY_TOKEN)  Removed in: major release after 2024-12-01  Why: EC2 in the name implied it was limited to EC2 resources. However, it is used for all connections.  Alternative: AWS_SESSION_TOKEN |
| **shortnames**  boolean | Indicates whether to return the name only without path if using a parameter hierarchy.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ssm_parameter_lookup.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](ssm_parameter_lookup.md#id5)

```yaml+jinja
# lookup sample:
- name: lookup ssm parameter store in the current region
  debug: msg="{{ lookup('amazon.aws.aws_ssm', 'Hello' ) }}"

- name: lookup ssm parameter store in specified region
  debug: msg="{{ lookup('amazon.aws.aws_ssm', 'Hello', region='us-east-2' ) }}"

- name: lookup ssm parameter store without decryption
  debug: msg="{{ lookup('amazon.aws.aws_ssm', 'Hello', decrypt=False ) }}"

- name: lookup ssm parameter store using a specified aws profile
  debug: msg="{{ lookup('amazon.aws.aws_ssm', 'Hello', profile='myprofile' ) }}"

- name: lookup ssm parameter store using explicit aws credentials
  debug: msg="{{ lookup('amazon.aws.aws_ssm', 'Hello', access_key=my_aws_access_key, secret_key=my_aws_secret_key, session_token=my_session_token ) }}" # noqa: E501

- name: lookup ssm parameter store with all options
  debug: msg="{{ lookup('amazon.aws.aws_ssm', 'Hello', decrypt=false, region='us-east-2', profile='myprofile') }}"

- name: lookup ssm parameter and fail if missing
  debug: msg="{{ lookup('amazon.aws.aws_ssm', 'missing-parameter') }}"

- name: lookup a key which doesn't exist, returning a default ('root')
  debug: msg="{{ lookup('amazon.aws.aws_ssm', 'AdminID', on_missing="skip") | default('root', true) }}"

- name: lookup a key which doesn't exist failing to store it in a fact
  set_fact:
    temp_secret: "{{ lookup('amazon.aws.aws_ssm', '/NoAccess/hiddensecret') }}"
  ignore_errors: true

- name: show fact default to "access failed" if we don't have access
  debug: msg="{{ 'the secret was:' ~ temp_secret | default('could not access secret') }}"

- name: return a dictionary of ssm parameters from a hierarchy path
  debug: msg="{{ lookup('amazon.aws.aws_ssm', '/PATH/to/params', region='ap-southeast-2', bypath=true, recursive=true ) }}"

- name: return a dictionary of ssm parameters from a hierarchy path with shortened names (param instead of /PATH/to/param)
  debug: msg="{{ lookup('amazon.aws.aws_ssm', '/PATH/to/params', region='ap-southeast-2', shortnames=true, bypath=true, recursive=true ) }}"

- name: Iterate over a parameter hierarchy (one iteration per parameter)
  debug: msg='Key contains {{ item.key }} , with value {{ item.value }}'
  loop: "{{ lookup('amazon.aws.aws_ssm', '/demo/', region='ap-southeast-2', bypath=True) | dict2items }}"

- name: Iterate over multiple paths as dictionaries (one iteration per path)
  debug: msg='Path contains {{ item }}'
  loop: "{{ lookup('amazon.aws.aws_ssm', '/demo/', '/demo1/', bypath=True)}}"

- name: lookup ssm parameter warn if access is denied
  debug: msg="{{ lookup('amazon.aws.aws_ssm', 'missing-parameter', on_denied="warn" ) }}"
```

### Authors

- Bill Wang <ozbillwang(at)gmail.com>
- Marat Bakeev <hawara(at)gmail.com>
- Michael De La Rue

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
