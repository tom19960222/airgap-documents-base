---
collection: ansible
version: "8"
title: "amazon.aws.ec2_key module – Create or delete an EC2 key pair"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/ec2_key_module.html
fetched_at: 2026-07-28T01:06:27+00:00
---
# amazon.aws.ec2_key module – Create or delete an EC2 key pair

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

- Create or delete an EC2 key pair.

## [Requirements](ec2_key_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ec2_key_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **file_name**  path  *added in amazon.aws 6.4.0* | Name of the file where the generated private key will be saved.  When provided, the *key.private_key* attribute will be removed from the return value.  The file is written out on the ‘host’ side rather than the ‘controller’ side.  Ignored when *state=absent* or *key_material* is provided. |
| **force**  boolean | Force overwrite of already existing key pair if key has changed.  **Choices:**   - `false` - `true` ← (default) |
| **key_material**  string | Public key material. |
| **key_type**  string  *added in amazon.aws 3.1.0* | The type of key pair to create.  Note that ED25519 keys are not supported for Windows instances, EC2 Instance Connect, and EC2 Serial Console.  By default Amazon will create an RSA key.  Mutually exclusive with parameter *key_material*.  **Choices:**   - `"rsa"` - `"ed25519"` |
| **name**  string / required | Name of the key pair. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Create or delete keypair.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ec2_key_module.md#id4)

> **Note:**
>
> - Support for *tags* and *purge_tags* was added in release 2.1.0.
> - For security reasons, this module should be used with **no_log=true** and (register) functionalities when creating new key pair without providing *key_material*.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](ec2_key_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: create a new EC2 key pair, returns generated private key
  # use no_log to avoid private key being displayed into output
  amazon.aws.ec2_key:
    name: my_keypair
  no_log: true
  register: aws_ec2_key_pair

- name: create key pair using provided key_material
  amazon.aws.ec2_key:
    name: my_keypair
    key_material: 'ssh-rsa AAAAxyz...== me@example.com'

- name: create key pair using key_material obtained using 'file' lookup plugin
  amazon.aws.ec2_key:
    name: my_keypair
    key_material: "{{ lookup('file', '/path/to/public_key/id_rsa.pub') }}"

- name: Create ED25519 key pair and save private key into a file
  amazon.aws.ec2_key:
    name: my_keypair
    key_type: ed25519
    file_name: /tmp/aws_ssh_rsa

# try creating a key pair with the name of an already existing keypair
# but don't overwrite it even if the key is different (force=false)
- name: try creating a key pair with name of an already existing keypair
  amazon.aws.ec2_key:
    name: my_existing_keypair
    key_material: 'ssh-rsa AAAAxyz...== me@example.com'
    force: false

- name: remove key pair from AWS by name
  amazon.aws.ec2_key:
    name: my_keypair
    state: absent
```

## [Return Values](ec2_key_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | whether a keypair was created/deleted  **Returned:** always  **Sample:** `true` |
| **key**  complex | details of the keypair (this is set to null when state is absent)  **Returned:** always |
| **fingerprint**  string | fingerprint of the key  **Returned:** when state is present  **Sample:** `"b0:22:49:61:d9:44:9d:0c:7e:ac:8a:32:93:21:6c:e8:fb:59:62:43"` |
| **id**  string | id of the keypair  **Returned:** when state is present  **Sample:** `"key-123456789abc"` |
| **name**  string | name of the keypair  **Returned:** when state is present  **Sample:** `"my_keypair"` |
| **private_key**  string | private key of a newly created keypair  **Returned:** when a new keypair is created by AWS (*key_material* is not provided) and *file_name* is not provided.  **Sample:** `"-----BEGIN RSA PRIVATE KEY----- MIIEowIBAAKC... -----END RSA PRIVATE KEY-----"` |
| **tags**  dictionary | a dictionary representing the tags attached to the key pair  **Returned:** when state is present  **Sample:** `{"my_key": "my value"}` |
| **type**  string  *added in amazon.aws 3.1.0* | type of a newly created keypair  **Returned:** when a new keypair is created by AWS  **Sample:** `"rsa"` |
| **msg**  string | short message describing the action taken  **Returned:** always  **Sample:** `"key pair created"` |

### Authors

- Vincent Viallet (@zbal)
- Prasad Katti (@prasadkatti)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
