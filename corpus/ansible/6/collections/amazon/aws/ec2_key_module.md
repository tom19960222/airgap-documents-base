---
collection: ansible
version: "6"
title: "amazon.aws.ec2_key module – create or delete an ec2 key pair"
source_url: https://docs.ansible.com/projects/ansible/6/collections/amazon/aws/ec2_key_module.html
fetched_at: 2026-07-27T16:43:44+00:00
---
# amazon.aws.ec2_key module – create or delete an ec2 key pair

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
> see [Requirements](ec2_key_module.md#ansible-collections-amazon-aws-ec2-key-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.ec2_key`.

New in amazon.aws 1.0.0

- [Synopsis](ec2_key_module.md#synopsis)
- [Requirements](ec2_key_module.md#requirements)
- [Parameters](ec2_key_module.md#parameters)
- [Notes](ec2_key_module.md#notes)
- [Examples](ec2_key_module.md#examples)
- [Return Values](ec2_key_module.md#return-values)

## [Synopsis](ec2_key_module.md#id1)

- create or delete an ec2 key pair.

## [Requirements](ec2_key_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_key_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **force**  boolean | Force overwrite of already existing key pair if key has changed.  Choices:   - `false` - `true` ← (default) |
| **key_material**  string | Public key material. |
| **key_type**  string  added in amazon.aws 3.1.0 | The type of key pair to create.  Note that ED25519 keys are not supported for Windows instances, EC2 Instance Connect, and EC2 Serial Console.  By default Amazon will create an RSA key.  Mutually exclusive with parameter *key_material*.  Requires at least botocore version 1.21.23.  Choices:   - `"rsa"` - `"ed25519"` |
| **name**  string / required | Name of the key pair. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_tags**  boolean  added in amazon.aws 2.1.0 | Delete any tags not specified in *tags*.  Choices:   - `false` ← (default) - `true` |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | create or delete keypair  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  dictionary  added in amazon.aws 2.1.0 | A dictionary of tags to set on the key pair. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **wait**  boolean | This option has no effect since version 2.5 and will be removed after 2022-06-01.  Choices:   - `false` - `true` |
| **wait_timeout**  integer | This option has no effect since version 2.5 and will be removed after 2022-06-01. |

## [Notes](ec2_key_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_key_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: create a new ec2 key pair, returns generated private key
  amazon.aws.ec2_key:
    name: my_keypair

- name: create key pair using provided key_material
  amazon.aws.ec2_key:
    name: my_keypair
    key_material: 'ssh-rsa AAAAxyz...== me@example.com'

- name: create key pair using key_material obtained using 'file' lookup plugin
  amazon.aws.ec2_key:
    name: my_keypair
    key_material: "{{ lookup('file', '/path/to/public_key/id_rsa.pub') }}"

- name: Create ED25519 key pair
  amazon.aws.ec2_key:
    name: my_keypair
    key_type: ed25519

# try creating a key pair with the name of an already existing keypair
# but don't overwrite it even if the key is different (force=false)
- name: try creating a key pair with name of an already existing keypair
  amazon.aws.ec2_key:
    name: my_existing_keypair
    key_material: 'ssh-rsa AAAAxyz...== me@example.com'
    force: false

- name: remove key pair by name
  amazon.aws.ec2_key:
    name: my_keypair
    state: absent
```

## [Return Values](ec2_key_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | whether a keypair was created/deleted  Returned: always  Sample: `true` |
| **key**  complex | details of the keypair (this is set to null when state is absent)  Returned: always |
| **fingerprint**  string | fingerprint of the key  Returned: when state is present  Sample: `"b0:22:49:61:d9:44:9d:0c:7e:ac:8a:32:93:21:6c:e8:fb:59:62:43"` |
| **id**  string | id of the keypair  Returned: when state is present  Sample: `"key-123456789abc"` |
| **name**  string | name of the keypair  Returned: when state is present  Sample: `"my_keypair"` |
| **private_key**  string | private key of a newly created keypair  Returned: when a new keypair is created by AWS (key_material is not provided)  Sample: `"-----BEGIN RSA PRIVATE KEY----- MIIEowIBAAKC... -----END RSA PRIVATE KEY-----"` |
| **tags**  dictionary | a dictionary representing the tags attached to the key pair  Returned: when state is present  Sample: `{"my_key": "my value"}` |
| **type**  string  added in amazon.aws 3.1.0 | type of a newly created keypair  Returned: when a new keypair is created by AWS  Sample: `"rsa"` |
| **msg**  string | short message describing the action taken  Returned: always  Sample: `"key pair created"` |

### Authors

- Vincent Viallet (@zbal)
- Prasad Katti (@prasadkatti)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
[Communication](index.md#communication-for-amazon-aws)
