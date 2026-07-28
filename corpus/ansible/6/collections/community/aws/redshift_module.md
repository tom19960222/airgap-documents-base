---
collection: ansible
version: "6"
title: "community.aws.redshift module – create, delete, or modify an Amazon Redshift instance"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/redshift_module.html
fetched_at: 2026-07-27T17:04:56+00:00
---
# community.aws.redshift module – create, delete, or modify an Amazon Redshift instance

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
> see [Requirements](redshift_module.md#ansible-collections-community-aws-redshift-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.redshift`.

New in community.aws 1.0.0

- [Synopsis](redshift_module.md#synopsis)
- [Requirements](redshift_module.md#requirements)
- [Parameters](redshift_module.md#parameters)
- [Notes](redshift_module.md#notes)
- [Examples](redshift_module.md#examples)
- [Return Values](redshift_module.md#return-values)

## [Synopsis](redshift_module.md#id1)

- Creates, deletes, or modifies Amazon Redshift cluster instances.

## [Requirements](redshift_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](redshift_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allow_version_upgrade**  aliases: version_upgrade  boolean | When *allow_version_upgrade=true* the cluster may be automatically upgraded during the maintenance window.  Choices:   - `false` - `true` ← (default) |
| **automated_snapshot_retention_period**  aliases: retention_period  integer | The number of days that automated snapshots are retained. |
| **availability_zone**  aliases: zone, aws_zone  string | Availability zone in which to launch cluster. |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **cluster_parameter_group_name**  aliases: param_group_name  string | Name of the cluster parameter group. |
| **cluster_security_groups**  aliases: security_groups  list / elements=string | In which security group the cluster belongs. |
| **cluster_subnet_group_name**  aliases: subnet  string | Which subnet to place the cluster. |
| **cluster_type**  string | The type of cluster.  Choices:   - `"multi-node"` - `"single-node"` ← (default) |
| **cluster_version**  aliases: version  string | Which version the cluster should have.  Choices:   - `"1.0"` |
| **command**  string / required | Specifies the action to take.  Choices:   - `"create"` - `"facts"` - `"delete"` - `"modify"` |
| **db_name**  string | Name of the database. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **elastic_ip**  string | An Elastic IP to use for the cluster. |
| **encrypted**  boolean | If the cluster is encrypted or not.  Choices:   - `false` ← (default) - `true` |
| **enhanced_vpc_routing**  boolean | Whether the cluster should have enhanced VPC routing enabled.  Choices:   - `false` ← (default) - `true` |
| **final_cluster_snapshot_identifier**  aliases: final_snapshot_id  string | Identifier of the final snapshot to be created before deleting the cluster.  If this parameter is provided, *skip_final_cluster_snapshot* must be `false`.  Used only when *command=delete*. |
| **identifier**  string / required | Redshift cluster identifier. |
| **new_cluster_identifier**  aliases: new_identifier  string | Only used when command=modify. |
| **node_type**  string | The node type of the cluster.  Require when *command=create*.  Choices:   - `"ds1.xlarge"` - `"ds1.8xlarge"` - `"ds2.xlarge"` - `"ds2.8xlarge"` - `"dc1.large"` - `"dc2.large"` - `"dc1.8xlarge"` - `"dw1.xlarge"` - `"dw1.8xlarge"` - `"dw2.large"` - `"dw2.8xlarge"` |
| **number_of_nodes**  integer | Number of nodes.  Only used when *cluster_type=multi-node*. |
| **password**  string | Master database password.  Used only when *command=create*. |
| **port**  integer | Which port the cluster is listening on. |
| **preferred_maintenance_window**  aliases: maintance_window, maint_window  string | Maintenance window in format of `ddd:hh24:mi-ddd:hh24:mi`. (Example: `Mon:22:00-Mon:23:15`)  Times are specified in UTC.  If not specified then a random 30 minute maintenance window is assigned. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **publicly_accessible**  boolean | If the cluster is accessible publicly or not.  Choices:   - `false` ← (default) - `true` |
| **purge_tags**  boolean  added in community.aws 1.3.0 | Purge existing tags that are not found in the cluster  Choices:   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **skip_final_cluster_snapshot**  aliases: skip_final_snapshot  boolean | Skip a final snapshot before deleting the cluster.  Used only when *command=delete*.  Choices:   - `false` ← (default) - `true` |
| **tags**  aliases: resource_tags  dictionary  added in community.aws 1.3.0 | A dictionary of resource tags. |
| **username**  string | Master database username.  Used only when *command=create*. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **vpc_security_group_ids**  aliases: vpc_security_groups  list / elements=string | VPC security group |
| **wait**  boolean | When *command=create*, *command=modify* or *command=restore* then wait for the database to enter the ‘available’ state.  When *command=delete* wait for the database to be terminated.  Choices:   - `false` ← (default) - `true` |
| **wait_timeout**  integer | When *wait=true* defines how long in seconds before giving up.  Default: `300` |

## [Notes](redshift_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](redshift_module.md#id5)

```yaml+jinja
- name: Basic cluster provisioning example
  community.aws.redshift:
    command: create
    node_type: ds1.xlarge
    identifier: new_cluster
    username: cluster_admin
    password: 1nsecure

- name: Cluster delete example
  community.aws.redshift:
    command: delete
    identifier: new_cluster
    skip_final_cluster_snapshot: true
    wait: true
```

## [Return Values](redshift_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cluster**  complex | dictionary containing all the cluster information  Returned: success |
| **availability_zone**  string | Amazon availability zone where the cluster is located. “None” until cluster is available.  Returned: success  Sample: `"us-east-1b"` |
| **create_time**  float | Time of the cluster creation as timestamp.  Returned: success  Sample: `1430158536.308` |
| **db_name**  string | Name of the database.  Returned: success  Sample: `"new_db_name"` |
| **enhanced_vpc_routing**  boolean | status of the enhanced vpc routing feature.  Returned: success |
| **identifier**  string | Id of the cluster.  Returned: success  Sample: `"new_redshift_cluster"` |
| **maintenance_window**  string | Time frame when maintenance/upgrade are done.  Returned: success  Sample: `"sun:09:30-sun:10:00"` |
| **port**  integer | Port of the cluster. “None” until cluster is available.  Returned: success  Sample: `5439` |
| **private_ip_address**  string | Private IP address of the main node.  Returned: success  Sample: `"10.10.10.10"` |
| **public_ip_address**  string | Public IP address of the main node. “None” when enhanced_vpc_routing is enabled.  Returned: success  Sample: `"0.0.0.0"` |
| **status**  string | Status of the cluster.  Returned: success  Sample: `"available"` |
| **tags**  dictionary | aws tags for cluster.  Returned: success |
| **url**  string | FQDN of the main cluster node. “None” until cluster is available.  Returned: success  Sample: `"new-redshift_cluster.jfkdjfdkj.us-east-1.redshift.amazonaws.com"` |

### Authors

- Jens Carl (@j-carl), Hothead Games Inc.
- Rafael Driutti (@rafaeldriutti)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
