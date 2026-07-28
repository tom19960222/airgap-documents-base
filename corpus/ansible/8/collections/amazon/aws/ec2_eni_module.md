---
collection: ansible
version: "8"
title: "amazon.aws.ec2_eni module – Create and optionally attach an Elastic Network Interface (ENI) to an instance"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/ec2_eni_module.html
fetched_at: 2026-07-28T01:06:24+00:00
---
# amazon.aws.ec2_eni module – Create and optionally attach an Elastic Network Interface (ENI) to an instance

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
> see [Requirements](ec2_eni_module.md#ansible-collections-amazon-aws-ec2-eni-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.ec2_eni`.

New in amazon.aws 1.0.0

- [Synopsis](ec2_eni_module.md#synopsis)
- [Requirements](ec2_eni_module.md#requirements)
- [Parameters](ec2_eni_module.md#parameters)
- [Notes](ec2_eni_module.md#notes)
- [Examples](ec2_eni_module.md#examples)
- [Return Values](ec2_eni_module.md#return-values)

## [Synopsis](ec2_eni_module.md#id1)

- Create and optionally attach an Elastic Network Interface (ENI) to an instance.
- If *eni_id* or *private_ip* is provided, the existing ENI (if any) will be modified.
- The *attached* parameter controls the attachment status of the network interface.

## [Requirements](ec2_eni_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ec2_eni_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **allow_reassignment**  boolean | Indicates whether to allow an IP address that is already assigned to another network interface or instance to be reassigned to the specified network interface.  **Choices:**   - `false` ← (default) - `true` |
| **attached**  boolean | Specifies if network interface should be attached or detached from instance. If omitted, attachment status won’t change  **Choices:**   - `false` - `true` |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **delete_on_termination**  boolean | Delete the interface when the instance it is attached to is terminated. You can only specify this flag when the interface is being modified, not on creation.  **Choices:**   - `false` - `true` |
| **description**  string | Optional description of the ENI. |
| **device_index**  integer | The index of the device for the network interface attachment on the instance.  **Default:** `0` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **eni_id**  string | The ID of the ENI (to modify).  If *eni_id=None* and *state=present*, a new ENI will be created. |
| **force_detach**  boolean | Force detachment of the interface. This applies either when explicitly detaching the interface by setting *instance_id=None* or when deleting an interface with *state=absent*.  **Choices:**   - `false` ← (default) - `true` |
| **instance_id**  string | Instance ID that you wish to attach ENI to. |
| **name**  string | Name for the ENI. This will create a tag with the key `Name` and the value assigned here.  This can be used in conjunction with *subnet_id* as another means of identifiying a network interface.  AWS does not enforce unique `Name` tags, so duplicate names are possible if you configure it that way. If that is the case, you will need to provide other identifying information such as *private_ip_address* or *eni_id*. |
| **private_ip_address**  string | Private IP address. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_secondary_private_ip_addresses**  boolean | To be used with *secondary_private_ip_addresses* to determine whether or not to remove any secondary IP addresses other than those specified.  Set *secondary_private_ip_addresses=[]* to purge all secondary addresses.  **Choices:**   - `false` ← (default) - `true` |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secondary_private_ip_address_count**  integer | The number of secondary IP addresses to assign to the network interface.  This option is mutually exclusive of *secondary_private_ip_addresses*. |
| **secondary_private_ip_addresses**  list / elements=string | A list of IP addresses to assign as secondary IP addresses to the network interface.  This option is mutually exclusive of *secondary_private_ip_address_count*. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **security_groups**  list / elements=string | List of security groups associated with the interface.  Ignored when *state=absent*.  **Default:** `[]` |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **source_dest_check**  boolean | By default, interfaces perform source/destination checks. NAT instances however need this check to be disabled. You can only specify this flag when the interface is being modified, not on creation.  **Choices:**   - `false` - `true` |
| **state**  string | Create or delete ENI.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subnet_id**  string | ID of subnet in which to create the ENI. |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ec2_eni_module.md#id4)

> **Note:**
>
> - This module identifies and ENI based on either the *eni_id*, a combination of *private_ip_address* and *subnet_id*, or a combination of *instance_id* and *device_id*. Any of these options will let you specify a particular ENI.
> - Support for *tags* and *purge_tags* was added in release 1.3.0.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](ec2_eni_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

# Create an ENI. As no security group is defined, ENI will be created in default security group
- amazon.aws.ec2_eni:
    private_ip_address: 172.31.0.20
    subnet_id: subnet-xxxxxxxx
    state: present

# Create an ENI and attach it to an instance
- amazon.aws.ec2_eni:
    instance_id: i-xxxxxxx
    device_index: 1
    private_ip_address: 172.31.0.20
    subnet_id: subnet-xxxxxxxx
    state: present

# Create an ENI with two secondary addresses
- amazon.aws.ec2_eni:
    subnet_id: subnet-xxxxxxxx
    state: present
    secondary_private_ip_address_count: 2

# Assign a secondary IP address to an existing ENI
# This will purge any existing IPs
- amazon.aws.ec2_eni:
    subnet_id: subnet-xxxxxxxx
    eni_id: eni-yyyyyyyy
    state: present
    secondary_private_ip_addresses:
      - 172.16.1.1

# Remove any secondary IP addresses from an existing ENI
- amazon.aws.ec2_eni:
    subnet_id: subnet-xxxxxxxx
    eni_id: eni-yyyyyyyy
    state: present
    secondary_private_ip_address_count: 0

# Destroy an ENI, detaching it from any instance if necessary
- amazon.aws.ec2_eni:
    eni_id: eni-xxxxxxx
    force_detach: true
    state: absent

# Update an ENI
- amazon.aws.ec2_eni:
    eni_id: eni-xxxxxxx
    description: "My new description"
    state: present

# Update an ENI using name and subnet_id
- amazon.aws.ec2_eni:
    name: eni-20
    subnet_id: subnet-xxxxxxx
    description: "My new description"
    state: present

# Update an ENI identifying it by private_ip_address and subnet_id
- amazon.aws.ec2_eni:
    subnet_id: subnet-xxxxxxx
    private_ip_address: 172.16.1.1
    description: "My new description"

# Detach an ENI from an instance
- amazon.aws.ec2_eni:
    eni_id: eni-xxxxxxx
    instance_id: None
    state: present

### Delete an interface on termination
# First create the interface
- amazon.aws.ec2_eni:
    instance_id: i-xxxxxxx
    device_index: 1
    private_ip_address: 172.31.0.20
    subnet_id: subnet-xxxxxxxx
    state: present
  register: eni

# Modify the interface to enable the delete_on_terminaton flag
- amazon.aws.ec2_eni:
    eni_id: "{{ eni.interface.id }}"
    delete_on_termination: true
```

## [Return Values](ec2_eni_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **interface**  complex | Network interface attributes  **Returned:** when state != absent |
| **description**  string | interface description  **Returned:** success  **Sample:** `"Firewall network interface"` |
| **groups**  list / elements=dictionary | list of security groups  **Returned:** success  **Sample:** `[{"sg-f8a8a9da": "default"}]` |
| **id**  string | network interface id  **Returned:** success  **Sample:** `"eni-1d889198"` |
| **mac_address**  string | interface’s physical address  **Returned:** success  **Sample:** `"00:00:5E:00:53:23"` |
| **name**  string | The name of the ENI  **Returned:** success  **Sample:** `"my-eni-20"` |
| **owner_id**  string | aws account id  **Returned:** success  **Sample:** `"812381371"` |
| **private_ip_address**  string | primary ip address of this interface  **Returned:** success  **Sample:** `"10.20.30.40"` |
| **private_ip_addresses**  list / elements=dictionary | list of all private ip addresses associated to this interface  **Returned:** success  **Sample:** `[{"primary_address": true, "private_ip_address": "10.20.30.40"}]` |
| **source_dest_check**  boolean | value of source/dest check flag  **Returned:** success  **Sample:** `true` |
| **status**  string | network interface status  **Returned:** success  **Sample:** `"pending"` |
| **subnet_id**  string | which vpc subnet the interface is bound  **Returned:** success  **Sample:** `"subnet-b0a0393c"` |
| **tags**  dictionary | The dictionary of tags associated with the ENI  **Returned:** success  **Sample:** `{"Name": "my-eni", "group": "Finance"}` |
| **vpc_id**  string | which vpc this network interface is bound  **Returned:** success  **Sample:** `"vpc-9a9a9da"` |

### Authors

- Rob White (@wimnat)
- Mike Healey (@healem)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
