---
collection: ansible
version: "8"
title: "community.aws.ec2_vpc_vpn module – Create, modify, and delete EC2 VPN connections"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/ec2_vpc_vpn_module.html
fetched_at: 2026-07-28T01:40:52+00:00
---
# community.aws.ec2_vpc_vpn module – Create, modify, and delete EC2 VPN connections

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
> see [Requirements](ec2_vpc_vpn_module.md#ansible-collections-community-aws-ec2-vpc-vpn-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.ec2_vpc_vpn`.

New in community.aws 1.0.0

- [Synopsis](ec2_vpc_vpn_module.md#synopsis)
- [Requirements](ec2_vpc_vpn_module.md#requirements)
- [Parameters](ec2_vpc_vpn_module.md#parameters)
- [Notes](ec2_vpc_vpn_module.md#notes)
- [Examples](ec2_vpc_vpn_module.md#examples)
- [Return Values](ec2_vpc_vpn_module.md#return-values)

## [Synopsis](ec2_vpc_vpn_module.md#id1)

- This module creates, modifies, and deletes VPN connections. Idempotence is achieved by using the filters option or specifying the VPN connection identifier.

## [Requirements](ec2_vpc_vpn_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ec2_vpc_vpn_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **connection_type**  string | The type of VPN connection.  At this time only `ipsec.1` is supported.  **Default:** `"ipsec.1"` |
| **customer_gateway_id**  string | The ID of the customer gateway. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **delay**  integer | The time, in seconds, to wait before checking operation again.  **Default:** `15` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **filters**  dictionary | An alternative to using *vpn_connection_id*. If multiple matches are found, vpn_connection_id is required. If one of the following suboptions is a list of items to filter by, only one item needs to match to find the VPN that correlates. e.g. if the filter *cidr* is `['194.168.2.0/24', '192.168.2.0/24']` and the VPN route only has the destination cidr block of `192.168.2.0/24` it will be found with this filter (assuming there are not multiple VPNs that are matched). Another example, if the filter *vpn* is equal to `['vpn-ccf7e7ad', 'vpn-cb0ae2a2']` and one of of the VPNs has the state deleted (exists but is unmodifiable) and the other exists and is not deleted, it will be found via this filter. See examples.  **Default:** `{}` |
| **bgp**  string | The BGP ASN number associated with a BGP device. Only works if the connection is attached. This filtering option is currently not working. |
| **cgw**  string | The customer gateway id as a string or a list of those strings. |
| **cgw-config**  string | The customer gateway configuration of the VPN as a string (in the format of the return value) or a list of those strings. |
| **cidr**  string | The destination cidr of the VPN’s route as a string or a list of those strings. |
| **static-routes-only**  string | The type of routing; `true` or `false`. |
| **tag-keys**  string | The key of a tag as a string or a list of those strings. |
| **tag-values**  string | The value of a tag as a string or a list of those strings. |
| **tags**  string | A dict of key value pairs. |
| **vgw**  string | The virtual private gateway as a string or a list of those strings. |
| **vpn**  string | The VPN connection id as a string or a list of those strings. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_routes**  boolean | Whether or not to delete VPN connections routes that are not specified in the task.  **Choices:**   - `false` ← (default) - `true` |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **routes**  list / elements=string | Routes to add to the connection.  **Default:** `[]` |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | The desired state of the VPN connection.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **static_only**  boolean | Indicates whether the VPN connection uses static routes only. Static routes must be used for devices that don’t support BGP.  **Choices:**   - `false` ← (default) - `true` |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **transit_gateway_id**  string  *added in community.aws 6.2.0* | The ID of the transit gateway.  Mutually exclusive with *vpn_gateway_id*. |
| **tunnel_options**  list / elements=dictionary | An optional list object containing no more than two dict members, each of which may contain *TunnelInsideCidr* and/or *PreSharedKey* keys with appropriate string values. AWS defaults will apply in absence of either of the aforementioned keys.  **Default:** `[]` |
| **PreSharedKey**  string | The pre-shared key (PSK) to establish initial authentication between the virtual private gateway and customer gateway. |
| **TunnelInsideCidr**  string | The range of inside IP addresses for the tunnel. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **vpn_connection_id**  string | The ID of the VPN connection. Required to modify or delete a connection if the filters option does not provide a unique match. |
| **vpn_gateway_id**  string | The ID of the virtual private gateway.  Mutually exclusive with *transit_gateway_id*. |
| **wait_timeout**  integer | How long, in seconds, before wait gives up.  **Default:** `600` |

## [Notes](ec2_vpc_vpn_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](ec2_vpc_vpn_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: create a VPN connection with vpn_gateway_id
  community.aws.ec2_vpc_vpn:
    state: present
    vpn_gateway_id: vgw-XXXXXXXX
    customer_gateway_id: cgw-XXXXXXXX

- name: Attach a vpn connection to transit gateway
  community.aws.ec2_vpc_vpn:
    state: present
    transit_gateway_id: tgw-XXXXXXXX
    customer_gateway_id: cgw-XXXXXXXX

- name: modify VPN connection tags
  community.aws.ec2_vpc_vpn:
    state: present
    vpn_connection_id: vpn-XXXXXXXX
    tags:
      Name: ansible-tag-1
      Other: ansible-tag-2

- name: delete a connection
  community.aws.ec2_vpc_vpn:
    vpn_connection_id: vpn-XXXXXXXX
    state: absent

- name: modify VPN tags (identifying VPN by filters)
  community.aws.ec2_vpc_vpn:
    state: present
    filters:
      cidr: 194.168.1.0/24
      tag-keys:
        - Ansible
        - Other
    tags:
      New: Tag
    purge_tags: true
    static_only: true

- name: set up VPN with tunnel options utilizing 'TunnelInsideCidr' only
  community.aws.ec2_vpc_vpn:
    state: present
    filters:
      vpn: vpn-XXXXXXXX
    static_only: true
    tunnel_options:
      -
        TunnelInsideCidr: '169.254.100.1/30'
      -
        TunnelInsideCidr: '169.254.100.5/30'

- name: add routes and remove any preexisting ones
  community.aws.ec2_vpc_vpn:
    state: present
    filters:
      vpn: vpn-XXXXXXXX
    routes:
      - 195.168.2.0/24
      - 196.168.2.0/24
    purge_routes: true

- name: remove all routes
  community.aws.ec2_vpc_vpn:
    state: present
    vpn_connection_id: vpn-XXXXXXXX
    routes: []
    purge_routes: true

- name: delete a VPN identified by filters
  community.aws.ec2_vpc_vpn:
    state: absent
    filters:
      tags:
        Ansible: Tag
```

## [Return Values](ec2_vpc_vpn_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | If the VPN connection has changed.  **Returned:** always  **Sample:** `{"changed": true}` |
| **customer_gateway_configuration**  string | The configuration of the VPN connection.  **Returned:** *state=present* |
| **customer_gateway_id**  string | The customer gateway connected via the connection.  **Returned:** *state=present*  **Sample:** `"{'customer_gateway_id': 'cgw-1220c87b'}"` |
| **options**  complex | The VPN connection options (currently only containing static_routes_only).  **Returned:** *state=present* |
| **static_routes_only**  string | If the VPN connection only allows static routes.  **Returned:** *state=present*  **Sample:** `"{'static_routes_only': True}"` |
| **routes**  list / elements=string | The routes of the VPN connection.  **Returned:** *state=present*  **Sample:** `{"routes": [{"destination_cidr_block": "192.168.1.0/24", "state": "available"}]}` |
| **state**  string | The status of the VPN connection.  **Returned:** *state=present*  **Sample:** `"{'state': 'available'}"` |
| **tags**  dictionary | The tags associated with the connection.  **Returned:** *state=present*  **Sample:** `{"tags": {"name": "ansible-test", "other": "tag"}}` |
| **transit_gateway_id**  string | The transit gateway id to which the vpn connection can be attached.  **Returned:** *state=present*  **Sample:** `"{'transit_gateway_id': 'tgw-cb0ae2a2'}"` |
| **type**  string | The type of VPN connection (currently only ipsec.1 is available).  **Returned:** *state=present*  **Sample:** `"{'type': 'ipsec.1'}"` |
| **vgw_telemetry**  list / elements=string | The telemetry for the VPN tunnel.  **Returned:** *state=present*  **Sample:** `{"vgw_telemetry": [{"accepted_route_count": 123, "last_status_change": "datetime(2015, 1, 1)", "outside_ip_address": "string", "status": "up", "status_message": "string"}]}` |
| **vpn_connection_id**  string | The identifier for the VPN connection.  **Returned:** *state=present*  **Sample:** `"{'vpn_connection_id': 'vpn-781e0e19'}"` |
| **vpn_gateway_id**  string | The virtual private gateway connected via the connection.  **Returned:** *state=present*  **Sample:** `"{'vpn_gateway_id': 'vgw-cb0ae2a2'}"` |

### Authors

- Sloane Hertel (@s-hertel)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
