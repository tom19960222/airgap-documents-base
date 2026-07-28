---
collection: ansible
version: "6"
title: "amazon.aws.aws_secret lookup – Look up secrets stored in AWS Secrets Manager."
source_url: https://docs.ansible.com/projects/ansible/6/collections/amazon/aws/aws_secret_lookup.html
fetched_at: 2026-07-27T16:43:56+00:00
---
# amazon.aws.aws_secret lookup – Look up secrets stored in AWS Secrets Manager.

> **Note:**
>
> This lookup plugin is part of the [amazon.aws collection](https://galaxy.ansible.com/amazon/aws) (version 3.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install amazon.aws`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](aws_secret_lookup.md#ansible-collections-amazon-aws-aws-secret-lookup-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.aws_secret`.

- [Synopsis](aws_secret_lookup.md#synopsis)
- [Requirements](aws_secret_lookup.md#requirements)
- [Terms](aws_secret_lookup.md#terms)
- [Keyword parameters](aws_secret_lookup.md#keyword-parameters)
- [Notes](aws_secret_lookup.md#notes)
- [Examples](aws_secret_lookup.md#examples)
- [Return Value](aws_secret_lookup.md#return-value)

## [Synopsis](aws_secret_lookup.md#id1)

- Look up secrets stored in AWS Secrets Manager provided the caller has the appropriate permissions to read the secret.
- Lookup is based on the secret’s *Name* value.
- Optional parameters can be passed into this lookup; *version_id* and *version_stage*

## [Requirements](aws_secret_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Terms](aws_secret_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | Name of the secret to look up in AWS Secrets Manager. |

## [Keyword parameters](aws_secret_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('amazon.aws.aws_secret', key1=value1, key2=value2, ...)` and `query('amazon.aws.aws_secret', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: aws_access_key_id  string | The AWS access key to use.  Configuration:   - Environment variable: [`EC2_ACCESS_KEY`](../../environment_variables.md#envvar-EC2_ACCESS_KEY) - Environment variable: [`AWS_ACCESS_KEY`](../../environment_variables.md#envvar-AWS_ACCESS_KEY) - Environment variable: [`AWS_ACCESS_KEY_ID`](../../environment_variables.md#envvar-AWS_ACCESS_KEY_ID) |
| **aws_profile**  aliases: boto_profile  string | The AWS profile  Configuration:   - Environment variable: [`AWS_DEFAULT_PROFILE`](../../environment_variables.md#envvar-AWS_DEFAULT_PROFILE) - Environment variable: [`AWS_PROFILE`](../../environment_variables.md#envvar-AWS_PROFILE) |
| **aws_secret_key**  aliases: aws_secret_access_key  string | The AWS secret key that corresponds to the access key.  Configuration:   - Environment variable: [`EC2_SECRET_KEY`](../../environment_variables.md#envvar-EC2_SECRET_KEY) - Environment variable: [`AWS_SECRET_KEY`](../../environment_variables.md#envvar-AWS_SECRET_KEY) - Environment variable: [`AWS_SECRET_ACCESS_KEY`](../../environment_variables.md#envvar-AWS_SECRET_ACCESS_KEY) |
| **aws_security_token**  string | The AWS security token if using temporary access and secret keys.  Configuration:   - Environment variable: [`EC2_SECURITY_TOKEN`](../../environment_variables.md#envvar-EC2_SECURITY_TOKEN) - Environment variable: [`AWS_SESSION_TOKEN`](../../environment_variables.md#envvar-AWS_SESSION_TOKEN) - Environment variable: [`AWS_SECURITY_TOKEN`](../../environment_variables.md#envvar-AWS_SECURITY_TOKEN) |
| **bypath**  boolean  added in amazon.aws 1.4.0 | A boolean to indicate whether the parameter is provided as a hierarchy.  Choices:   - `false` ← (default) - `true` |
| **join**  boolean | Join two or more entries to form an extended secret.  This is useful for overcoming the 4096 character limit imposed by AWS.  No effect when used with *bypath*.  Choices:   - `false` ← (default) - `true` |
| **nested**  boolean  added in amazon.aws 1.4.0 | A boolean to indicate the secret contains nested values.  Choices:   - `false` ← (default) - `true` |
| **on_deleted**  string  added in amazon.aws 2.0.0 | Action to take if the secret has been marked for deletion.  `error` will raise a fatal error when the secret has been marked for deletion.  `skip` will silently ignore the deleted secret.  `warn` will skip over the deleted secret but issue a warning.  Choices:   - `"error"` ← (default) - `"skip"` - `"warn"` |
| **on_denied**  string | Action to take if access to the secret is denied.  `error` will raise a fatal error when access to the secret is denied.  `skip` will silently ignore the denied secret.  `warn` will skip over the denied secret but issue a warning.  Choices:   - `"error"` ← (default) - `"skip"` - `"warn"` |
| **on_missing**  string | Action to take if the secret is missing.  `error` will raise a fatal error when the secret is missing.  `skip` will silently ignore the missing secret.  `warn` will skip over the missing secret but issue a warning.  Choices:   - `"error"` ← (default) - `"skip"` - `"warn"` |
| **region**  string | The region for which to create the connection.  Configuration:   - Environment variable: [`EC2_REGION`](../../environment_variables.md#envvar-EC2_REGION) - Environment variable: [`AWS_REGION`](../../environment_variables.md#envvar-AWS_REGION) |
| **version_id**  string | Version of the secret(s). |
| **version_stage**  string | Stage of the secret version. |

## [Notes](aws_secret_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('amazon.aws.aws_secret', term1, term2, key1=value1, key2=value2)` and `query('amazon.aws.aws_secret', term1, term2, key1=value1, key2=value2)`

## [Examples](aws_secret_lookup.md#id6)

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
   msg="{{ lookup('amazon.aws.aws_secret', 'secrets.environments.production.password', region=region, aws_profile=aws_profile,
   aws_access_key=aws_access_key, aws_secret_key=aws_secret_key, nested=true) }}"
  # The secret can be queried using the following syntax: `aws_secret_object_name.key1.key2.key3`.
  # If an object is of the form `{"key1":{"key2":{"key3":1}}}` the query would return the value `1`.
  # Region is the AWS region where the AWS secret is stored.
  # AWS_profile is the aws profile to use, that has access to the AWS secret.
```

## [Return Value](aws_secret_lookup.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  string | Returns the value of the secret stored in AWS Secrets Manager.  Returned: success |

### Authors

- Aaron Smith

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
[Communication](index.md#communication-for-amazon-aws)
