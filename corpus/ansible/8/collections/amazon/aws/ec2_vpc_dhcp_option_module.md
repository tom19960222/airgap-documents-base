---
collection: ansible
version: "8"
title: "amazon.aws.ec2_vpc_dhcp_option module – Manages DHCP Options, and can ensure the DHCP options for the given VPC match what’s requested"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/ec2_vpc_dhcp_option_module.html
fetched_at: 2026-07-28T01:06:36+00:00
---
# amazon.aws.ec2_vpc_dhcp_option module – Manages DHCP Options, and can ensure the DHCP options for the given VPC match what’s requested

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
> see [Requirements](ec2_vpc_dhcp_option_module.md#ansible-collections-amazon-aws-ec2-vpc-dhcp-option-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.ec2_vpc_dhcp_option`.

New in amazon.aws 1.0.0

- [Synopsis](ec2_vpc_dhcp_option_module.md#synopsis)
- [Requirements](ec2_vpc_dhcp_option_module.md#requirements)
- [Parameters](ec2_vpc_dhcp_option_module.md#parameters)
- [Notes](ec2_vpc_dhcp_option_module.md#notes)
- [Examples](ec2_vpc_dhcp_option_module.md#examples)
- [Return Values](ec2_vpc_dhcp_option_module.md#return-values)

## [Synopsis](ec2_vpc_dhcp_option_module.md#id1)

- This module removes, or creates DHCP option sets, and can associate them to a VPC.
- Optionally, a new DHCP Options set can be created that converges a VPC’s existing DHCP option set with values provided.
- When dhcp_options_id is provided, the module will 1. remove (with state=’absent’) 2. ensure tags are applied (if state=’present’ and tags are provided 3. attach it to a VPC (if state=’present’ and a vpc_id is provided.
- If any of the optional values are missing, they will either be treated as a no-op (i.e., inherit what already exists for the VPC)
- To remove existing options while inheriting, supply an empty value (e.g. set ntp_servers to [] if you want to remove them from the VPC’s options)

## [Requirements](ec2_vpc_dhcp_option_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ec2_vpc_dhcp_option_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **delete_old**  boolean | Whether to delete the old VPC DHCP option set when associating a new one.  This is primarily useful for debugging/development purposes when you want to quickly roll back to the old option set. Note that this setting will be ignored, and the old DHCP option set will be preserved, if it is in use by any other VPC. (Otherwise, AWS will return an error.)  **Choices:**   - `false` - `true` ← (default) |
| **dhcp_options_id**  string | The resource_id of an existing DHCP options set. If this is specified, then it will override other settings, except tags (which will be updated to match) |
| **dns_servers**  list / elements=string | A list of IP addresses to set the DNS servers for the VPC to. |
| **domain_name**  string | The domain name to set in the DHCP option sets. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **inherit_existing**  boolean | For any DHCP options not specified in these parameters, whether to inherit them from the options set already applied to *vpc_id*, or to reset them to be empty.  **Choices:**   - `false` ← (default) - `true` |
| **netbios_name_servers**  list / elements=string | List of hosts to advertise as NetBIOS servers. |
| **netbios_node_type**  integer | NetBIOS node type to advertise in the DHCP options. The AWS recommendation is to use 2 (when using netbios name services) <https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_DHCP_Options.html> |
| **ntp_servers**  list / elements=string | List of hosts to advertise as NTP servers for the VPC. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | create/assign or remove the DHCP options. If state is set to absent, then a DHCP options set matched either by id, or tags and options will be removed if possible.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **vpc_id**  string | VPC ID to associate with the requested DHCP option set.  If no VPC ID is provided, and no matching option set is found then a new DHCP option set is created. |

## [Notes](ec2_vpc_dhcp_option_module.md#id4)

> **Note:**
>
> - Support for *purge_tags* was added in release 2.0.0.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](ec2_vpc_dhcp_option_module.md#id5)

```yaml+jinja
# Completely overrides the VPC DHCP options associated with VPC vpc-123456 and deletes any existing
# DHCP option set that may have been attached to that VPC.
- amazon.aws.ec2_vpc_dhcp_option:
    domain_name: "foo.example.com"
    region: us-east-1
    dns_servers:
        - 10.0.0.1
        - 10.0.1.1
    ntp_servers:
        - 10.0.0.2
        - 10.0.1.2
    netbios_name_servers:
        - 10.0.0.1
        - 10.0.1.1
    netbios_node_type: 2
    vpc_id: vpc-123456
    delete_old: True
    inherit_existing: False

# Ensure the DHCP option set for the VPC has 10.0.0.4 and 10.0.1.4 as the specified DNS servers, but
# keep any other existing settings. Also, keep the old DHCP option set around.
- amazon.aws.ec2_vpc_dhcp_option:
    region: us-east-1
    dns_servers:
      - "{{groups['dns-primary']}}"
      - "{{groups['dns-secondary']}}"
    vpc_id: vpc-123456
    inherit_existing: True
    delete_old: False

## Create a DHCP option set with 4.4.4.4 and 8.8.8.8 as the specified DNS servers, with tags
## but do not assign to a VPC
- amazon.aws.ec2_vpc_dhcp_option:
    region: us-east-1
    dns_servers:
      - 4.4.4.4
      - 8.8.8.8
    tags:
      Name: google servers
      Environment: Test

## Delete a DHCP options set that matches the tags and options specified
- amazon.aws.ec2_vpc_dhcp_option:
    region: us-east-1
    dns_servers:
      - 4.4.4.4
      - 8.8.8.8
    tags:
      Name: google servers
      Environment: Test
    state: absent

## Associate a DHCP options set with a VPC by ID
- amazon.aws.ec2_vpc_dhcp_option:
    region: us-east-1
    dhcp_options_id: dopt-12345678
    vpc_id: vpc-123456
```

## [Return Values](ec2_vpc_dhcp_option_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether the dhcp options were changed  **Returned:** always |
| **dhcp_config**  dictionary | The boto2-style DHCP options created, associated or found  **Returned:** when available |
| **domain-name**  list / elements=string | The domain name for hosts in the DHCP option sets  **Returned:** when available  **Sample:** `["my.example.com"]` |
| **domain-name-servers**  list / elements=string | The IP addresses of up to four domain name servers, or AmazonProvidedDNS.  **Returned:** when available  **Sample:** `["10.0.0.1", "10.0.1.1"]` |
| **netbios-name-servers**  list / elements=string | The IP addresses of up to four NetBIOS name servers.  **Returned:** when available  **Sample:** `["10.0.0.1", "10.0.1.1"]` |
| **netbios-node-type**  string | The NetBIOS node type (1, 2, 4, or 8).  **Returned:** when available  **Sample:** `"2"` |
| **ntp-servers**  list / elements=string | The IP addresses of up to four Network Time Protocol (NTP) servers.  **Returned:** when available  **Sample:** `["10.0.0.1", "10.0.1.1"]` |
| **dhcp_options**  dictionary | The DHCP options created, associated or found  **Returned:** when available |
| **dhcp_configurations**  list / elements=string | The DHCP configuration for the option set  **Returned:** success  **Sample:** `["{\"key\": \"ntp-servers\", \"values\": [{\"value\": \"10.0.0.2\" , \"value\": \"10.0.1.2\"}]}", "{\"key\": \"netbios-name-servers\", \"values\": [{value\": \"10.0.0.1\"}, {\"value\": \"10.0.1.1\" }]}"]` |
| **dhcp_options_id**  string | The aws resource id of the primary DCHP options set created or found  **Returned:** success  **Sample:** `"dopt-0955331de6a20dd07"` |
| **owner_id**  string | The ID of the AWS account that owns the DHCP options set.  **Returned:** success  **Sample:** `"012345678912"` |
| **tags**  list / elements=string | The tags to be applied to a DHCP options set  **Returned:** success  **Sample:** `["{\"Key\": \"CreatedBy\", \"Value\": \"ansible-test\"}", "{\"Key\": \"Collection\", \"Value\": \"amazon.aws\"}"]` |
| **dhcp_options_id**  string | The aws resource id of the primary DCHP options set created, found or removed  **Returned:** when available |

### Authors

- Joel Thompson (@joelthompson)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
