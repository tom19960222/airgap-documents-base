---
collection: ansible
version: "8"
title: "community.aws.eks_fargate_profile module – Manage EKS Fargate Profile"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/eks_fargate_profile_module.html
fetched_at: 2026-07-28T01:41:05+00:00
---
# community.aws.eks_fargate_profile module – Manage EKS Fargate Profile

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
> see [Requirements](eks_fargate_profile_module.md#ansible-collections-community-aws-eks-fargate-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.eks_fargate_profile`.

New in community.aws 4.0.0

- [Synopsis](eks_fargate_profile_module.md#synopsis)
- [Requirements](eks_fargate_profile_module.md#requirements)
- [Parameters](eks_fargate_profile_module.md#parameters)
- [Notes](eks_fargate_profile_module.md#notes)
- [Examples](eks_fargate_profile_module.md#examples)
- [Return Values](eks_fargate_profile_module.md#return-values)

## [Synopsis](eks_fargate_profile_module.md#id1)

- Manage EKS Fargate Profile.

## [Requirements](eks_fargate_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](eks_fargate_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **cluster_name**  string / required | Name of EKS Cluster. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **name**  string / required | Name of EKS Fargate Profile. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **role_arn**  string | ARN of IAM role used by the EKS cluster.  Required when *state=present*. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **selectors**  list / elements=dictionary | A list of selectors to use in fargate profile.  Required when *state=present*. |
| **labels**  dictionary | A dictionary of labels used in fargate profile.  **Default:** `{}` |
| **namespace**  string | A namespace used in fargate profile. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Create or delete the Fargate Profile.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **subnets**  list / elements=string | list of subnet IDs for the Kubernetes cluster.  Required when *state=present*. |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **wait**  boolean | Specifies whether the module waits until the profile is created or deleted before moving on.  **Choices:**   - `false` ← (default) - `true` |
| **wait_timeout**  integer | The duration in seconds to wait for the cluster to become active. Defaults to 1200 seconds (20 minutes).  **Default:** `1200` |

## [Notes](eks_fargate_profile_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](eks_fargate_profile_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Create an EKS Fargate Profile
  community.aws.eks_fargate_profile:
    name: test_fargate
    cluster_name: test_cluster
    role_arn: my_eks_role
    subnets:
      - subnet-aaaa1111
    selectors:
      - namespace: nm-test
        labels:
          - label1: test
    state: present
    wait: true

- name: Remove an EKS Fargate Profile
  community.aws.eks_fargate_profile:
    name: test_fargate
    cluster_name: test_cluster
    wait: true
    state: absent
```

## [Return Values](eks_fargate_profile_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cluster_name**  string | Name of EKS Cluster.  **Returned:** when state is present  **Sample:** `"test-cluster"` |
| **created_at**  string | Fargate Profile creation date and time.  **Returned:** when state is present  **Sample:** `"2022-01-18T20:00:00.111000+00:00"` |
| **fargate_profile_arn**  string | ARN of the Fargate Profile.  **Returned:** when state is present  **Sample:** `"arn:aws:eks:us-east-1:1231231123:safd"` |
| **fargate_profile_name**  string | Name of Fargate Profile.  **Returned:** when state is present  **Sample:** `"test_profile"` |
| **pod_execution_role_arn**  string | ARN of the IAM Role used by Fargate Profile.  **Returned:** when state is present  **Sample:** `"arn:aws:eks:us-east-1:1231231123:role/asdf"` |
| **selectors**  complex | Selector configuration.  **Returned:** when state is present |
| **labels**  list / elements=string | List of kubernetes labels used in profile.  **Returned:** when state is present  **Sample:** `[{"label1": "test1"}, {"label2": "test2"}]` |
| **namespace**  string | Name of the kubernetes namespace used in profile.  **Returned:** when state is present  **Sample:** `"nm-test"` |
| **status**  string | status of the EKS Fargate Profile.  **Returned:** when state is present  **Sample:** `"['CREATING', 'ACTIVE']"` |
| **subnets**  list / elements=string | List of subnets used in Fargate Profile.  **Returned:** when state is present  **Sample:** `["subnet-qwerty123", "subnet-asdfg456"]` |
| **tags**  dictionary | A dictionary of resource tags.  **Returned:** when state is present  **Sample:** `{"env": "test", "foo": "bar"}` |

### Authors

- Tiago Jarra (@tjarra)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
