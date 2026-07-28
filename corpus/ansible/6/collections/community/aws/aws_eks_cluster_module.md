---
collection: ansible
version: "6"
title: "community.aws.aws_eks_cluster module – Manage Elastic Kubernetes Service Clusters"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/aws_eks_cluster_module.html
fetched_at: 2026-07-27T17:03:24+00:00
---
# community.aws.aws_eks_cluster module – Manage Elastic Kubernetes Service Clusters

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
> see [Requirements](aws_eks_cluster_module.md#ansible-collections-community-aws-aws-eks-cluster-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.aws_eks_cluster`.

New in community.aws 1.0.0

- [Synopsis](aws_eks_cluster_module.md#synopsis)
- [Requirements](aws_eks_cluster_module.md#requirements)
- [Parameters](aws_eks_cluster_module.md#parameters)
- [Notes](aws_eks_cluster_module.md#notes)
- [Examples](aws_eks_cluster_module.md#examples)
- [Return Values](aws_eks_cluster_module.md#return-values)

## [Synopsis](aws_eks_cluster_module.md#id1)

- Manage Elastic Kubernetes Service Clusters

## [Requirements](aws_eks_cluster_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](aws_eks_cluster_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **name**  string / required | Name of EKS cluster |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **role_arn**  string | ARN of IAM role used by the EKS cluster |
| **security_groups**  list / elements=string | list of security group names or IDs |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | desired state of the EKS cluster  Choices:   - `"absent"` - `"present"` ← (default) |
| **subnets**  list / elements=string | list of subnet IDs for the Kubernetes cluster |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **version**  string | Kubernetes version - defaults to latest |
| **wait**  boolean | Specifies whether the module waits until the cluster is active or deleted before moving on. It takes “usually less than 10 minutes” per AWS documentation.  Choices:   - `false` ← (default) - `true` |
| **wait_timeout**  integer | The duration in seconds to wait for the cluster to become active. Defaults to 1200 seconds (20 minutes).  Default: `1200` |

## [Notes](aws_eks_cluster_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](aws_eks_cluster_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Create an EKS cluster
  community.aws.aws_eks_cluster:
    name: my_cluster
    version: 1.14
    role_arn: my_eks_role
    subnets:
      - subnet-aaaa1111
    security_groups:
      - my_eks_sg
      - sg-abcd1234
  register: caller_facts

- name: Remove an EKS cluster
  community.aws.aws_eks_cluster:
    name: my_cluster
    wait: yes
    state: absent
```

## [Return Values](aws_eks_cluster_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **arn**  string | ARN of the EKS cluster  Returned: when state is present  Sample: `"arn:aws:eks:us-west-2:111111111111:cluster/my-eks-cluster"` |
| **certificate_authority**  complex | Dictionary containing Certificate Authority Data for cluster  Returned: after creation |
| **data**  string | Base-64 encoded Certificate Authority Data for cluster  Returned: when the cluster has been created and is active |
| **created_at**  string | Cluster creation date and time  Returned: when state is present  Sample: `"2018-06-06T11:56:56.242000+00:00"` |
| **endpoint**  string | Kubernetes API server endpoint  Returned: when the cluster has been created and is active  Sample: `"https://API_SERVER_ENDPOINT.yl4.us-west-2.eks.amazonaws.com"` |
| **name**  string | EKS cluster name  Returned: when state is present  Sample: `"my-eks-cluster"` |
| **resources_vpc_config**  complex | VPC configuration of the cluster  Returned: when state is present |
| **security_group_ids**  list / elements=string | List of security group IDs  Returned: always  Sample: `["sg-abcd1234", "sg-aaaa1111"]` |
| **subnet_ids**  list / elements=string | List of subnet IDs  Returned: always  Sample: `["subnet-abcdef12", "subnet-345678ab", "subnet-cdef1234"]` |
| **vpc_id**  string | VPC id  Returned: always  Sample: `"vpc-a1b2c3d4"` |
| **role_arn**  string | ARN of the IAM role used by the cluster  Returned: when state is present  Sample: `"arn:aws:iam::111111111111:role/aws_eks_cluster_role"` |
| **status**  string | status of the EKS cluster  Returned: when state is present  Sample: `"['CREATING', 'ACTIVE']"` |
| **version**  string | Kubernetes version of the cluster  Returned: when state is present  Sample: `"1.10"` |

### Authors

- Will Thames (@willthames)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
