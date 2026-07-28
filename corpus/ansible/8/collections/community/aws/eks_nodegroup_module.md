---
collection: ansible
version: "8"
title: "community.aws.eks_nodegroup module – Manage EKS Nodegroup module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/eks_nodegroup_module.html
fetched_at: 2026-07-28T01:41:06+00:00
---
# community.aws.eks_nodegroup module – Manage EKS Nodegroup module

> **Note:**
>
> This module is part of the [community.aws collection](https://galaxy.ansible.com/ui/repo/published/community/aws/) (version 6.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.aws`.
>
> To use it in a playbook, specify: `community.aws.eks_nodegroup`.

New in community.aws 5.3.0

- [Synopsis](eks_nodegroup_module.md#synopsis)
- [Parameters](eks_nodegroup_module.md#parameters)
- [Notes](eks_nodegroup_module.md#notes)
- [Examples](eks_nodegroup_module.md#examples)
- [Return Values](eks_nodegroup_module.md#return-values)

## [Synopsis](eks_nodegroup_module.md#id1)

- Manage EKS Nodegroup.

## [Parameters](eks_nodegroup_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **ami_type**  string | The AMI type for your node group.  **Choices:**   - `"AL2_x86_64"` - `"AL2_x86_64_GPU"` - `"AL2_ARM_64"` - `"CUSTOM"` - `"BOTTLEROCKET_ARM_64"` - `"BOTTLEROCKET_x86_64"` |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **capacity_type**  string | The capacity type for your node group.  **Choices:**   - `"ON_DEMAND"` ← (default) - `"SPOT"` |
| **cluster_name**  string / required | Name of EKS Cluster. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **disk_size**  integer | Size of disk in nodegroup nodes. If you specify *launch_template*, then don’t specify *disk_size*, or the node group deployment will fail. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **instance_types**  list / elements=string | Specify the instance types for a node group. If you specify *launch_template*, then don’t specify *instance_types*, or the node group deployment will fail. |
| **labels**  dictionary | The Kubernetes labels to be applied to the nodes in the node group when they are created.  **Default:** `{}` |
| **launch_template**  dictionary | An object representing a node group’s launch template specification.  If specified, then do not specify *instanceTypes*, *diskSize*, or *remoteAccess*. |
| **id**  string | The ID of the launch template. |
| **name**  string | The name of the launch template. |
| **version**  string | The version of the launch template to use.  If no version is specified, then the template’s default version is used. |
| **name**  string / required | Name of EKS Nodegroup. |
| **node_role**  string | ARN of IAM role used by the EKS cluster Nodegroup. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_tags**  boolean | Purge existing tags that are not found in the nodegroup.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **release_version**  string | The AMI version of the Amazon EKS optimized AMI to use with your node group. |
| **remote_access**  dictionary | The remote access (SSH) configuration to use with your node group. If you specify *launch_template*, then don’t specify *remote_access*, or the node group deployment will fail. |
| **ec2_ssh_key**  string | The Amazon EC2 SSH key that provides access for SSH communication with the nodes in the managed node group. |
| **source_sg**  list / elements=string | The security groups that are allowed SSH access (port 22) to the nodes. |
| **scaling_config**  dictionary | The scaling configuration details for the Auto Scaling group that is created for your node group.  **Default:** `{"desired_size": 1, "max_size": 2, "min_size": 1}` |
| **desired_size**  integer | The current number of nodes that the managed node group should maintain. |
| **max_size**  integer | The maximum number of nodes that the managed node group can scale out to. |
| **min_size**  integer | The minimum number of nodes that the managed node group can scale in to. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Create or delete the Nodegroup.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **subnets**  list / elements=string | list of subnet IDs for the Kubernetes cluster. |
| **tags**  aliases: resource_tags  dictionary | A dictionary of resource tags. |
| **taints**  list / elements=dictionary | The Kubernetes taints to be applied to the nodes in the node group.  **Default:** `[]` |
| **effect**  string | The effect of the taint.  **Choices:**   - `"NO_SCHEDULE"` - `"NO_EXECUTE"` - `"PREFER_NO_SCHEDULE"` |
| **key**  string | The key of the taint. |
| **value**  string | The value of the taint. |
| **update_config**  dictionary | The node group update configuration.  **Default:** `{"max_unavailable": 1}` |
| **max_unavailable**  integer | The maximum number of nodes unavailable at once during a version update. |
| **max_unavailable_percentage**  integer | The maximum percentage of nodes unavailable during a version update. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **wait**  boolean | Specifies whether the module waits until the profile is created or deleted before moving on.  **Choices:**   - `false` ← (default) - `true` |
| **wait_timeout**  integer | The duration in seconds to wait for the nodegroup to become active. Defaults to `1200` seconds.  **Default:** `1200` |

## [Notes](eks_nodegroup_module.md#id3)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](eks_nodegroup_module.md#id4)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: create nodegroup
  community.aws.eks_nodegroup:
    name: test_nodegroup
    state: present
    cluster_name: test_cluster
    node_role: arn:aws:eks:us-east-1:1231231123:role/asdf
    subnets:
      - subnet-qwerty123
      - subnet-asdfg456
    scaling_config:
      - min_size: 1
      - max_size: 2
      - desired_size: 1
    disk_size: 20
    instance_types: 't3.micro'
    ami_type: 'AL2_x86_64'
    labels:
      - 'teste': 'test'
    taints:
      - key: 'test'
        value: 'test'
        effect: 'NO_SCHEDULE'
    capacity_type: 'on_demand'

- name: Remove an EKS Nodegrop
  community.aws.eks_nodegroup:
    name: test_nodegroup
    cluster_name: test_cluster
    wait: yes
    state: absent
```

## [Return Values](eks_nodegroup_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ami_type**  string | This is the AMI type that was specified in the node group configuration.  **Returned:** when state is present  **Sample:** `"need_validate"` |
| **capacity_type**  string | The capacity type of your managed node group.  **Returned:** when state is present  **Sample:** `"need_validate"` |
| **cluster_name**  string | Name of EKS Cluster  **Returned:** when state is present  **Sample:** `"test_cluster"` |
| **created_at**  string | Nodegroup creation date and time.  **Returned:** when state is present  **Sample:** `"2022-01-18T20:00:00.111000+00:00"` |
| **diskSize**  integer | This is the disk size in the node group configuration.  **Returned:** when state is present  **Sample:** `20` |
| **health**  dictionary | The health status of the node group.  **Returned:** when state is present  **Sample:** `"need_validate"` |
| **instance_types**  list / elements=string | This is the instance type that is associated with the node group.  **Returned:** when state is present  **Sample:** `["need_validate"]` |
| **labels**  dictionary | The Kubernetes labels applied to the nodes in the node group.  **Returned:** when state is present  **Sample:** `"need_validate"` |
| **launch_template**  dictionary | If a launch template was used to create the node group, then this is the launch template that was used.  **Returned:** when state is present  **Sample:** `"need_validate"` |
| **modified_at**  string | Nodegroup modified date and time.  **Returned:** when state is present  **Sample:** `"2022-01-18T20:00:00.111000+00:00"` |
| **node_role**  string | ARN of the IAM Role used by Nodegroup.  **Returned:** when state is present  **Sample:** `"arn:aws:eks:us-east-1:1231231123:role/asdf"` |
| **nodegroup_arn**  string | The Amazon Resource Name (ARN) associated with the managed node group.  **Returned:** when state is present  **Sample:** `"arn:aws:eks:us-east-1:1231231123:safd"` |
| **nodegroup_name**  string | The name associated with an Amazon EKS managed node group.  **Returned:** when state is present  **Sample:** `"test_cluster"` |
| **release_version**  string | This is the version of the Amazon EKS optimized AMI that the node group was deployed with.  **Returned:** when state is present  **Sample:** `"need_validate"` |
| **remote_access**  dictionary | This is the remote access configuration that is associated with the node group.  **Returned:** when state is present  **Sample:** `"need_validate"` |
| **resources**  complex | The resources associated with the node group.  **Returned:** when state is present |
| **autoScalingGroups**  list / elements=dictionary | The Auto Scaling groups associated with the node group.  **Returned:** when state is present |
| **remoteAccessSecurityGroup**  string | The remote access security group associated with the node group.  **Returned:** when state is present |
| **scaling_config**  dictionary | The scaling configuration details for the Auto Scaling group that is associated with your node group.  **Returned:** when state is present  **Sample:** `"need_validate"` |
| **status**  string | status of the EKS Nodegroup.  **Returned:** when state is present  **Sample:** `"['CREATING', 'ACTIVE']"` |
| **subnets**  list / elements=string | List of subnets used in Fargate Profile.  **Returned:** when state is present  **Sample:** `["subnet-qwerty123", "subnet-asdfg456"]` |
| **tags**  dictionary | Nodegroup tags.  **Returned:** when state is present  **Sample:** `{"foo": "bar"}` |
| **taints**  list / elements=string | The Kubernetes taints to be applied to the nodes in the node group when they are created.  **Returned:** when state is present  **Sample:** `["need_validate"]` |
| **update_config**  dictionary | The node group update configuration.  **Returned:** when state is present |
| **maxUnavailable**  integer | The maximum number of nodes unavailable at once during a version update.  **Returned:** success |
| **maxUnavailablePercentage**  integer | The maximum percentage of nodes unavailable during a version update.  **Returned:** success |
| **version**  string | The Kubernetes version of the managed node group.  **Returned:** when state is present  **Sample:** `"need_validate"` |

### Authors

- Tiago Jarra (@tjarra)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
