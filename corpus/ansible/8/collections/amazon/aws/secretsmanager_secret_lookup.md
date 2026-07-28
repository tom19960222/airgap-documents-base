---
collection: ansible
version: "8"
title: "amazon.aws.secretsmanager_secret lookup – Look up secrets stored in AWS Secrets Manager"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/secretsmanager_secret_lookup.html
fetched_at: 2026-07-28T01:07:20+00:00
---
# amazon.aws.secretsmanager_secret lookup – Look up secrets stored in AWS Secrets Manager

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
> see [Requirements](secretsmanager_secret_lookup.md#ansible-collections-amazon-aws-secretsmanager-secret-lookup-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.secretsmanager_secret`.

- [Synopsis](secretsmanager_secret_lookup.md#synopsis)
- [Requirements](secretsmanager_secret_lookup.md#requirements)
- [Terms](secretsmanager_secret_lookup.md#terms)
- [Keyword parameters](secretsmanager_secret_lookup.md#keyword-parameters)
- [Notes](secretsmanager_secret_lookup.md#notes)
- [Examples](secretsmanager_secret_lookup.md#examples)
- [Return Value](secretsmanager_secret_lookup.md#return-value)

## [Synopsis](secretsmanager_secret_lookup.md#id1)

- Look up secrets stored in AWS Secrets Manager provided the caller has the appropriate permissions to read the secret.
- Lookup is based on the secret’s *Name* value.
- Optional parameters can be passed into this lookup; *version_id* and *version_stage*
- Prior to release 6.0.0 this module was known as `aws_ssm`, the usage remains the same.

Aliases: aws_secret

## [Requirements](secretsmanager_secret_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Terms](secretsmanager_secret_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | Name of the secret to look up in AWS Secrets Manager. |

## [Keyword parameters](secretsmanager_secret_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('amazon.aws.secretsmanager_secret', key1=value1, key2=value2, ...)` and `query('amazon.aws.secretsmanager_secret', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  **Configuration:**   - Environment variable: [`AWS_ACCESS_KEY_ID`](../../environment_variables.md#envvar-AWS_ACCESS_KEY_ID) - Environment variable: [`AWS_ACCESS_KEY`](../../environment_variables.md#envvar-AWS_ACCESS_KEY) - Environment variable: [`EC2_ACCESS_KEY`](../../environment_variables.md#envvar-EC2_ACCESS_KEY)  Removed in: major release after 2024-12-01  Why: EC2 in the name implied it was limited to EC2 resources. However, it is used for all connections.  Alternative: AWS_ACCESS_KEY_ID |
| **bypath**  boolean  *added in amazon.aws 1.4.0* | A boolean to indicate whether the parameter is provided as a hierarchy.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: aws_endpoint_url, endpoint  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The *endpoint* alias has been deprecated and will be removed in a release after 2024-12-01.  **Configuration:**   - Environment variable: [`AWS_URL`](../../environment_variables.md#envvar-AWS_URL) - Environment variable: [`EC2_URL`](../../environment_variables.md#envvar-EC2_URL)  Removed in: major release after 2024-12-01  Why: EC2 in the name implied it was limited to EC2 resources. However, it is used for all connections.  Alternative: AWS_URL |
| **join**  boolean | Join two or more entries to form an extended secret.  This is useful for overcoming the 4096 character limit imposed by AWS.  No effect when used with *bypath*.  **Choices:**   - `false` ← (default) - `true` |
| **nested**  boolean  *added in amazon.aws 1.4.0* | A boolean to indicate the secret contains nested values.  **Choices:**   - `false` ← (default) - `true` |
| **on_deleted**  string  *added in amazon.aws 2.0.0* | Action to take if the secret has been marked for deletion.  `error` will raise a fatal error when the secret has been marked for deletion.  `skip` will silently ignore the deleted secret.  `warn` will skip over the deleted secret but issue a warning.  **Choices:**   - `"error"` ← (default) - `"skip"` - `"warn"` |
| **on_denied**  string | Action to take if access to the secret is denied.  `error` will raise a fatal error when access to the secret is denied.  `skip` will silently ignore the denied secret.  `warn` will skip over the denied secret but issue a warning.  **Choices:**   - `"error"` ← (default) - `"skip"` - `"warn"` |
| **on_missing**  string | Action to take if the secret is missing.  `error` will raise a fatal error when the secret is missing.  `skip` will silently ignore the missing secret.  `warn` will skip over the missing secret but issue a warning.  **Choices:**   - `"error"` ← (default) - `"skip"` - `"warn"` |
| **profile**  aliases: aws_profile, boto_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options.  The *boto_profile* alias has been deprecated and will be removed in a release after 2024-12-01.  **Configuration:**   - Environment variable: [`AWS_PROFILE`](../../environment_variables.md#envvar-AWS_PROFILE) - Environment variable: [`AWS_DEFAULT_PROFILE`](../../environment_variables.md#envvar-AWS_DEFAULT_PROFILE) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  **Configuration:**   - Environment variable: [`AWS_REGION`](../../environment_variables.md#envvar-AWS_REGION) - Environment variable: [`EC2_REGION`](../../environment_variables.md#envvar-EC2_REGION)  Removed in: major release after 2024-12-01  Why: EC2 in the name implied it was limited to EC2 resources, when it is used for all connections  Alternative: |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  **Configuration:**   - Environment variable: [`AWS_SECRET_ACCESS_KEY`](../../environment_variables.md#envvar-AWS_SECRET_ACCESS_KEY) - Environment variable: [`AWS_SECRET_KEY`](../../environment_variables.md#envvar-AWS_SECRET_KEY) - Environment variable: [`EC2_SECRET_KEY`](../../environment_variables.md#envvar-EC2_SECRET_KEY)  Removed in: major release after 2024-12-01  Why: EC2 in the name implied it was limited to EC2 resources. However, it is used for all connections.  Alternative: AWS_SECRET_ACCESS_KEY |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  **Configuration:**   - Environment variable: [`AWS_SESSION_TOKEN`](../../environment_variables.md#envvar-AWS_SESSION_TOKEN) - Environment variable: [`AWS_SECURITY_TOKEN`](../../environment_variables.md#envvar-AWS_SECURITY_TOKEN)  Removed in: major release after 2024-12-01  Why: AWS_SECURITY_TOKEN was used for compatibility with the original boto SDK, support for which has been dropped  Alternative: AWS_SESSION_TOKEN - Environment variable: [`EC2_SECURITY_TOKEN`](../../environment_variables.md#envvar-EC2_SECURITY_TOKEN)  Removed in: major release after 2024-12-01  Why: EC2 in the name implied it was limited to EC2 resources. However, it is used for all connections.  Alternative: AWS_SESSION_TOKEN |
| **version_id**  string | Version of the secret(s). |
| **version_stage**  string | Stage of the secret version. |

## [Notes](secretsmanager_secret_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('amazon.aws.secretsmanager_secret', term1, term2, key1=value1, key2=value2)` and `query('amazon.aws.secretsmanager_secret', term1, term2, key1=value1, key2=value2)`
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](secretsmanager_secret_lookup.md#id6)

```yaml+jinja
- name: lookup secretsmanager secret in the current region
  debug: msg="{{ lookup('amazon.aws.aws_secret', '/path/to/secrets', bypath=true) }}"

- name: Create RDS instance with aws_secret lookup for password param
  rds:
    command: create
    instance_name: app-db
    db_engine: MySQL
    size: 10
    instance_type: db.m1.small
    username: dbadmin
    password: "{{ lookup('amazon.aws.aws_secret', 'DbSecret') }}"
    tags:
      Environment: staging

- name: skip if secret does not exist
  debug: msg="{{ lookup('amazon.aws.aws_secret', 'secret-not-exist', on_missing='skip')}}"

- name: warn if access to the secret is denied
  debug: msg="{{ lookup('amazon.aws.aws_secret', 'secret-denied', on_denied='warn')}}"

- name: lookup secretsmanager secret in the current region using the nested feature
  debug: msg="{{ lookup('amazon.aws.aws_secret', 'secrets.environments.production.password', nested=true) }}"
  # The secret can be queried using the following syntax: `aws_secret_object_name.key1.key2.key3`.
  # If an object is of the form `{"key1":{"key2":{"key3":1}}}` the query would return the value `1`.
- name: lookup secretsmanager secret in a specific region using specified region and aws profile using nested feature
  debug: >
   msg="{{ lookup('amazon.aws.aws_secret', 'secrets.environments.production.password', region=region, profile=aws_profile,
   access_key=aws_access_key, secret_key=aws_secret_key, nested=true) }}"
  # The secret can be queried using the following syntax: `aws_secret_object_name.key1.key2.key3`.
  # If an object is of the form `{"key1":{"key2":{"key3":1}}}` the query would return the value `1`.
  # Region is the AWS region where the AWS secret is stored.
  # AWS_profile is the aws profile to use, that has access to the AWS secret.
```

## [Return Value](secretsmanager_secret_lookup.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  string | Returns the value of the secret stored in AWS Secrets Manager.  **Returned:** success |

### Authors

- Aaron Smith

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
