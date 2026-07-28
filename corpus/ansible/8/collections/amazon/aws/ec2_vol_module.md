---
collection: ansible
version: "8"
title: "amazon.aws.ec2_vol module – Create and attach a volume, return volume ID and device map"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/ec2_vol_module.html
fetched_at: 2026-07-28T01:06:35+00:00
---
# amazon.aws.ec2_vol module – Create and attach a volume, return volume ID and device map

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
> see [Requirements](ec2_vol_module.md#ansible-collections-amazon-aws-ec2-vol-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.ec2_vol`.

New in amazon.aws 1.0.0

- [Synopsis](ec2_vol_module.md#synopsis)
- [Requirements](ec2_vol_module.md#requirements)
- [Parameters](ec2_vol_module.md#parameters)
- [Notes](ec2_vol_module.md#notes)
- [Examples](ec2_vol_module.md#examples)
- [Return Values](ec2_vol_module.md#return-values)

## [Synopsis](ec2_vol_module.md#id1)

- Creates an EBS volume and optionally attaches it to an instance.
- If both *instance* and *name* are given and the instance has a device at the device name, then no volume is created and no attachment is made.

## [Requirements](ec2_vol_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ec2_vol_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **delete_on_termination**  boolean | When set to `true`, the volume will be deleted upon instance termination.  **Choices:**   - `false` ← (default) - `true` |
| **device_name**  string | Device ID to override device mapping. Assumes /dev/sdf for Linux/UNIX and /dev/xvdf for Windows. |
| **encrypted**  boolean | Enable encryption at rest for this volume.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **id**  string | Volume ID if you wish to attach an existing volume (requires instance) or remove an existing volume. |
| **instance**  string | Instance ID if you wish to attach the volume.  Set to `None` to detach the volume. |
| **iops**  integer | The provisioned IOPs you want to associate with this volume (integer). |
| **kms_key_id**  string | Specify the ID of the KMS key to use. |
| **modify_volume**  boolean  *added in amazon.aws 1.4.0* | The volume won’t be modified unless this key is `true`.  **Choices:**   - `false` ← (default) - `true` |
| **multi_attach**  boolean  *added in amazon.aws 2.0.0* | If set to `true`, Multi-Attach will be enabled when creating the volume.  When you create a new volume, Multi-Attach is disabled by default.  This parameter is supported with io1 and io2 volumes only.  **Choices:**   - `false` - `true` |
| **name**  string | Volume Name tag if you wish to attach an existing volume (requires instance). |
| **outpost_arn**  string  *added in amazon.aws 3.1.0* | The Amazon Resource Name (ARN) of the Outpost.  If set, allows to create volume in an Outpost. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **snapshot**  string | Snapshot ID on which to base the volume. |
| **state**  string | Whether to ensure the volume is present or absent.  *state=list* was deprecated in release 1.1.0 and is no longer available with release 4.0.0.  The `list` functionality has been moved to a dedicated module [amazon.aws.ec2_vol_info](ec2_vol_info_module.md#ansible-collections-amazon-aws-ec2-vol-info-module).  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **throughput**  integer  *added in amazon.aws 1.4.0* | Volume throughput in MB/s.  This parameter is only valid for gp3 volumes.  Valid range is from 125 to 1000. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **volume_size**  integer | Size of volume (in GiB) to create. |
| **volume_type**  string | Type of EBS volume; `standard` (magnetic), `gp2` (SSD), `gp3` (SSD), `io1` (Provisioned IOPS), `io2` (Provisioned IOPS), `st1` (Throughput Optimized HDD), `sc1` (Cold HDD).  `standard` is the old EBS default and continues to remain the Ansible default for backwards compatibility.  **Choices:**   - `"standard"` ← (default) - `"gp2"` - `"io1"` - `"st1"` - `"sc1"` - `"gp3"` - `"io2"` |
| **zone**  aliases: availability_zone, aws_zone, ec2_zone  string | Zone in which to create the volume, if unset uses the zone the instance is in (if set). |

## [Notes](ec2_vol_module.md#id4)

> **Note:**
>
> - Support for *purge_tags* was added in release 1.5.0.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](ec2_vol_module.md#id5)

```yaml+jinja
# Simple attachment action
- amazon.aws.ec2_vol:
    instance: XXXXXX
    volume_size: 5
    device_name: sdd
    region: us-west-2

# Example using custom iops params
- amazon.aws.ec2_vol:
    instance: XXXXXX
    volume_size: 5
    iops: 100
    device_name: sdd
    region: us-west-2

# Example using snapshot id
- amazon.aws.ec2_vol:
    instance: XXXXXX
    snapshot: "{{ snapshot }}"

# Playbook example combined with instance launch
- amazon.aws.ec2:
    keypair: "{{ keypair }}"
    image: "{{ image }}"
    wait: true
    count: 3
  register: ec2
- amazon.aws.ec2_vol:
    instance: "{{ item.id }}"
    volume_size: 5
  loop: "{{ ec2.instances }}"
  register: ec2_vol

# Example: Launch an instance and then add a volume if not already attached
#   * Volume will be created with the given name if not already created.
#   * Nothing will happen if the volume is already attached.

- amazon.aws.ec2:
    keypair: "{{ keypair }}"
    image: "{{ image }}"
    zone: YYYYYY
    id: my_instance
    wait: true
    count: 1
  register: ec2

- amazon.aws.ec2_vol:
    instance: "{{ item.id }}"
    name: my_existing_volume_Name_tag
    device_name: /dev/xvdf
  loop: "{{ ec2.instances }}"
  register: ec2_vol

# Remove a volume
- amazon.aws.ec2_vol:
    id: vol-XXXXXXXX
    state: absent

# Detach a volume (since 1.9)
- amazon.aws.ec2_vol:
    id: vol-XXXXXXXX
    instance: None
    region: us-west-2

# Create new volume using SSD storage
- amazon.aws.ec2_vol:
    instance: XXXXXX
    volume_size: 50
    volume_type: gp2
    device_name: /dev/xvdf

# Create new volume with multi-attach enabled
- amazon.aws.ec2_vol:
    zone: XXXXXX
    multi_attach: true
    volume_size: 4
    volume_type: io1
    iops: 102

# Attach an existing volume to instance. The volume will be deleted upon instance termination.
- amazon.aws.ec2_vol:
    instance: XXXXXX
    id: XXXXXX
    device_name: /dev/sdf
    delete_on_termination: true
```

## [Return Values](ec2_vol_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **device**  string | device name of attached volume  **Returned:** when success  **Sample:** `"/dev/sdf"` |
| **volume**  string | a dictionary containing detailed attributes of the volume  **Returned:** when success  **Sample:** `"{'attachment_set': [{'attach_time': '2015-10-23T00:22:29.000Z', 'deleteOnTermination': 'false', 'device': '/dev/sdf', 'instance_id': 'i-8356263c', 'status': 'attached'}], 'create_time': '2015-10-21T14:36:08.870Z', 'encrypted': False, 'id': 'vol-35b333d9', 'iops': None, 'size': 1, 'snapshot_id': '', 'status': 'in-use', 'tags': {'env': 'dev'}, 'type': 'standard', 'zone': 'us-east-1b'}"` |
| **volume_id**  string | the id of volume  **Returned:** when success  **Sample:** `"vol-35b333d9"` |
| **volume_type**  string | the volume type  **Returned:** when success  **Sample:** `"standard"` |

### Authors

- Lester Wade (@lwade)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
