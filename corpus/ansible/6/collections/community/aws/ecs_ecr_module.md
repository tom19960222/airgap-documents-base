---
collection: ansible
version: "6"
title: "community.aws.ecs_ecr module – Manage Elastic Container Registry repositories"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/ecs_ecr_module.html
fetched_at: 2026-07-27T17:04:17+00:00
---
# community.aws.ecs_ecr module – Manage Elastic Container Registry repositories

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
> see [Requirements](ecs_ecr_module.md#ansible-collections-community-aws-ecs-ecr-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.ecs_ecr`.

New in community.aws 1.0.0

- [Synopsis](ecs_ecr_module.md#synopsis)
- [Requirements](ecs_ecr_module.md#requirements)
- [Parameters](ecs_ecr_module.md#parameters)
- [Notes](ecs_ecr_module.md#notes)
- [Examples](ecs_ecr_module.md#examples)
- [Return Values](ecs_ecr_module.md#return-values)

## [Synopsis](ecs_ecr_module.md#id1)

- Manage Elastic Container Registry repositories.

## [Requirements](ecs_ecr_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ecs_ecr_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **force_set_policy**  boolean | If *force_set_policy=false*, it prevents setting a policy that would prevent you from setting another policy in the future.  Choices:   - `false` ← (default) - `true` |
| **image_tag_mutability**  string | Configure whether repository should be mutable (ie. an already existing tag can be overwritten) or not.  Choices:   - `"mutable"` ← (default) - `"immutable"` |
| **lifecycle_policy**  json | JSON or dict that represents the new lifecycle policy. |
| **name**  string / required | The name of the repository. |
| **policy**  json | JSON or dict that represents the new policy. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_lifecycle_policy**  boolean | if `true`, remove the lifecycle policy from the repository.  Defaults to `false`.  Choices:   - `false` - `true` |
| **purge_policy**  aliases: delete_policy  boolean | If yes, remove the policy from the repository.  Alias `delete_policy` has been deprecated and will be removed after 2022-06-01.  Defaults to `false`.  Choices:   - `false` - `true` |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **registry_id**  string | AWS account id associated with the registry.  If not specified, the default registry is assumed. |
| **scan_on_push**  boolean  added in community.aws 1.3.0 | if `true`, images are scanned for known vulnerabilities after being pushed to the repository.  Choices:   - `false` ← (default) - `true` |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Create or destroy the repository.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](ecs_ecr_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ecs_ecr_module.md#id5)

```yaml+jinja
# If the repository does not exist, it is created. If it does exist, would not
# affect any policies already on it.
- name: ecr-repo
  community.aws.ecs_ecr:
    name: super/cool

- name: destroy-ecr-repo
  community.aws.ecs_ecr:
    name: old/busted
    state: absent

- name: Cross account ecr-repo
  community.aws.ecs_ecr:
    registry_id: 999999999999
    name: cross/account

- name: set-policy as object
  community.aws.ecs_ecr:
    name: needs-policy-object
    policy:
      Version: '2008-10-17'
      Statement:
        - Sid: read-only
          Effect: Allow
          Principal:
            AWS: '{{ read_only_arn }}'
          Action:
            - ecr:GetDownloadUrlForLayer
            - ecr:BatchGetImage
            - ecr:BatchCheckLayerAvailability

- name: set-policy as string
  community.aws.ecs_ecr:
    name: needs-policy-string
    policy: "{{ lookup('template', 'policy.json.j2') }}"

- name: delete-policy
  community.aws.ecs_ecr:
    name: needs-no-policy
    purge_policy: yes

- name: create immutable ecr-repo
  community.aws.ecs_ecr:
    name: super/cool
    image_tag_mutability: immutable

- name: set-lifecycle-policy
  community.aws.ecs_ecr:
    name: needs-lifecycle-policy
    scan_on_push: yes
    lifecycle_policy:
      rules:
        - rulePriority: 1
          description: new policy
          selection:
            tagStatus: untagged
            countType: sinceImagePushed
            countUnit: days
            countNumber: 365
          action:
            type: expire

- name: purge-lifecycle-policy
  community.aws.ecs_ecr:
    name: needs-no-lifecycle-policy
    purge_lifecycle_policy: true
```

## [Return Values](ecs_ecr_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **created**  boolean | If true, the repository was created  Returned: always |
| **name**  string | The name of the repository  Returned: when state == ‘absent’ |
| **repository**  dictionary | The created or updated repository  Returned: when state == ‘present’  Sample: `{"createdAt": "2017-01-17T08:41:32-06:00", "registryId": "999999999999", "repositoryArn": "arn:aws:ecr:us-east-1:999999999999:repository/ecr-test-1484664090", "repositoryName": "ecr-test-1484664090", "repositoryUri": "999999999999.dkr.ecr.us-east-1.amazonaws.com/ecr-test-1484664090"}` |
| **state**  string | The asserted state of the repository (present, absent)  Returned: always |

### Authors

- David M. Lee (@leedm777)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
