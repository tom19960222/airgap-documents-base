---
collection: ansible
version: "8"
title: "community.aws.mq_broker module – MQ broker management"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/mq_broker_module.html
fetched_at: 2026-07-28T01:41:31+00:00
---
# community.aws.mq_broker module – MQ broker management

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
> see [Requirements](mq_broker_module.md#ansible-collections-community-aws-mq-broker-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.mq_broker`.

New in community.aws 6.0.0

- [Synopsis](mq_broker_module.md#synopsis)
- [Requirements](mq_broker_module.md#requirements)
- [Parameters](mq_broker_module.md#parameters)
- [Notes](mq_broker_module.md#notes)
- [Examples](mq_broker_module.md#examples)
- [Return Values](mq_broker_module.md#return-values)

## [Synopsis](mq_broker_module.md#id1)

- Create/update/delete a broker.
- Reboot a broker.

## [Requirements](mq_broker_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](mq_broker_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **authentication_strategy**  string | Choose between locally and remotely managed users.  **Choices:**   - `"SIMPLE"` - `"LDAP"` |
| **auto_minor_version_upgrade**  boolean | Allow/disallow automatic minor version upgrades.  **Choices:**   - `false` - `true` ← (default) |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **broker_name**  string / required | The Name of the MQ broker to work on. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **deployment_mode**  string | Set broker deployment type.  Can be used only during creation.  Defaults to `SINGLE_INSTANCE`.  **Choices:**   - `"SINGLE_INSTANCE"` - `"ACTIVE_STANDBY_MULTI_AZ"` - `"CLUSTER_MULTI_AZ"` |
| **enable_audit_log**  boolean | Enable/disable to push audit logs to AWS CloudWatch.  **Choices:**   - `false` ← (default) - `true` |
| **enable_general_log**  boolean | Enable/disable to push general logs to AWS CloudWatch.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **engine_type**  string | Set broker engine type.  Can be used only during creation.  Defaults to `ACTIVEMQ`.  **Choices:**   - `"ACTIVEMQ"` - `"RABBITMQ"` |
| **engine_version**  string | Set engine version of broker.  The special value `latest` will pick the latest available version.  The special value `latest` is ignored on update. |
| **host_instance_type**  string | Instance type of broker instances. |
| **kms_key_id**  string | Use referenced key to encrypt broker data at rest.  Can be used only during creation. |
| **maintenance_window_start_time**  dictionary | Set maintenance window for automatic minor upgrades.  Can be used only during creation.  Not providing any value means “no maintenance window”. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **publicly_accessible**  boolean | Allow/disallow public access.  Can be used only during creation.  Defaults to `false`.  **Choices:**   - `false` - `true` |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **security_groups**  list / elements=string | Associate security groups with broker.  At least one must be provided during creation. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | `present`: Create/update broker.  `absent`: Delete broker.  `restarted`: Reboot broker.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"restarted"` |
| **storage_type**  string | Set underlying storage type.  Can be used only during creation.  Defaults to `EFS`.  **Choices:**   - `"EBS"` - `"EFS"` |
| **subnet_ids**  list / elements=string | Defines where deploy broker instances to.  Minimum required number depends on deployment type.  Can be used only during creation. |
| **tags**  dictionary | Tag newly created brokers.  Can be used only during creation. |
| **use_aws_owned_key**  boolean | Must be set to `false` if *kms_key_id* is provided as well.  Can be used only during creation.  Defaults to `true`.  **Choices:**   - `false` - `true` |
| **users**  list / elements=dictionary | This parameter allows to use a custom set of initial user(s).  [community.aws.mq_user](mq_user_module.md#ansible-collections-community-aws-mq-user-module) is the preferred way to manage (local) users however a broker cannot be created without any user.  If nothing is specified a default `admin` user will be created along with brokers.  Can be used only during creation. Use [community.aws.mq_user](mq_user_module.md#ansible-collections-community-aws-mq-user-module) module for updates. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](mq_broker_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](mq_broker_module.md#id5)

```yaml+jinja
- name: create broker (if missing) with minimal required parameters
  community.aws.mq_broker:
    broker_name: "{{ broker_name }}"
    security_groups:
      - sg_xxxxxxx
    subnet_ids:
      - subnet_xxx
      - subnet_yyy
    register: result

- set_fact:
    broker_id: "{{ result.broker['BrokerId'] }}"

- name: use mq_broker_info to wait until broker is ready
  community.aws.mq_broker_info:
    broker_id: "{{ broker_id }}"
  register: result
  until: "result.broker['BrokerState'] == 'RUNNING'"
  retries: 15
  delay:   60

- name: create or update broker with almost all parameter set including credentials
  community.aws.mq_broker:
    broker_name: "my_broker_2"
    state: present
    deployment_mode: 'ACTIVE_STANDBY_MULTI_AZ'
    use_aws_owned_key: false
    kms_key_id: 'my-precreted-key-id'
    engine_type: 'ACTIVEMQ'
    maintenance_window_start_time:
      DayOfWeek: 'MONDAY'
      TimeOfDay: '03:15'
      TimeZone: 'Europe/Berlin'
    publicly_accessible: true
    storage_type: 'EFS'
    security_groups:
      - sg_xxxxxxx
    subnet_ids:
      - subnet_xxx
      - subnet_yyy
    users:
    - Username: 'initial-user'
      Password: 'plain-text-password'
      ConsoleAccess: true
    tags:
    - env: Test
      creator: ansible
    authentication_strategy: 'SIMPLE'
    auto_minor_version_upgrade: true
    engine_version: "5.15.13"
    host_instance_type: 'mq.t3.micro'
    enable_audit_log: true
    enable_general_log: true

- name: reboot a broker
  community.aws.mq_broker:
    broker_name: "my_broker_2"
    state: restarted

- name: delete a broker
  community.aws.mq_broker:
    broker_name: "my_broker_2"
    state: absent
```

## [Return Values](mq_broker_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **broker**  dictionary | All API responses are converted to snake yaml except ‘Tags’  ‘state=present’: API response of create_broker() or update_broker() call  ‘state=absent’: result of describe_broker() call before delete_broker() is triggerd  ‘state=restarted’: result of describe_broker() after reboot has been triggered  **Returned:** success |

### Authors

- FCO (@fotto)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
