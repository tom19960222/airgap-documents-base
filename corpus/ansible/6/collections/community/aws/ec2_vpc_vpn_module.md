---
collection: ansible
version: "6"
title: "community.aws.ec2_vpc_vpn module – Create, modify, and delete EC2 VPN connections."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/ec2_vpc_vpn_module.html
fetched_at: 2026-07-27T17:04:14+00:00
---
# community.aws.ec2_vpc_vpn module – Create, modify, and delete EC2 VPN connections.

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
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_vpc_vpn_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **connection_type**  string | The type of VPN connection.  At this time only `ipsec.1` is supported.  Default: `"ipsec.1"` |
| **customer_gateway_id**  string | The ID of the customer gateway. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **delay**  integer | The time, in seconds, to wait before checking operation again.  Default: `15` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **filters**  dictionary | An alternative to using *vpn_connection_id*. If multiple matches are found, vpn_connection_id is required. If one of the following suboptions is a list of items to filter by, only one item needs to match to find the VPN that correlates. e.g. if the filter *cidr* is `['194.168.2.0/24', '192.168.2.0/24']` and the VPN route only has the destination cidr block of `192.168.2.0/24` it will be found with this filter (assuming there are not multiple VPNs that are matched). Another example, if the filter *vpn* is equal to `['vpn-ccf7e7ad', 'vpn-cb0ae2a2']` and one of of the VPNs has the state deleted (exists but is unmodifiable) and the other exists and is not deleted, it will be found via this filter. See examples. |
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
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_routes**  boolean | Whether or not to delete VPN connections routes that are not specified in the task.  Choices:   - `false` ← (default) - `true` |
| **purge_tags**  boolean | Whether or not to delete VPN connections tags that are associated with the connection but not specified in the task.  Choices:   - `false` ← (default) - `true` |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **routes**  list / elements=string | Routes to add to the connection. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | The desired state of the VPN connection.  Choices:   - `"present"` ← (default) - `"absent"` |
| **static_only**  boolean | Indicates whether the VPN connection uses static routes only. Static routes must be used for devices that don’t support BGP.  Choices:   - `false` ← (default) - `true` |
| **tags**  dictionary | Tags to attach to the VPN connection. |
| **tunnel_options**  list / elements=dictionary | An optional list object containing no more than two dict members, each of which may contain *TunnelInsideCidr* and/or *PreSharedKey* keys with appropriate string values. AWS defaults will apply in absence of either of the aforementioned keys. |
| **PreSharedKey**  string | The pre-shared key (PSK) to establish initial authentication between the virtual private gateway and customer gateway. |
| **TunnelInsideCidr**  string | The range of inside IP addresses for the tunnel. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **vpn_connection_id**  string | The ID of the VPN connection. Required to modify or delete a connection if the filters option does not provide a unique match. |
| **vpn_gateway_id**  string | The ID of the virtual private gateway. |
| **wait_timeout**  integer | How long, in seconds, before wait gives up.  Default: `600` |

## [Notes](ec2_vpc_vpn_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_vpc_vpn_module.md#id5)

```yaml+jinja
# Note: None of these examples set aws_access_key, aws_secret_key, or region.
# It is assumed that their matching environment variables are set.

- name: create a VPN connection
  community.aws.ec2_vpc_vpn:
    state: present
    vpn_gateway_id: vgw-XXXXXXXX
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
| **changed**  boolean | If the VPN connection has changed.  Returned: always  Sample: `{"changed": true}` |
| **customer_gateway_configuration**  string | The configuration of the VPN connection.  Returned: *state=present* |
| **customer_gateway_id**  string | The customer gateway connected via the connection.  Returned: *state=present*  Sample: `"{'customer_gateway_id': 'cgw-1220c87b'}"` |
| **options**  complex | The VPN connection options (currently only containing static_routes_only).  Returned: *state=present* |
| **static_routes_only**  string | If the VPN connection only allows static routes.  Returned: *state=present*  Sample: `"{'static_routes_only': True}"` |
| **routes**  list / elements=string | The routes of the VPN connection.  Returned: *state=present*  Sample: `{"routes": [{"destination_cidr_block": "192.168.1.0/24", "state": "available"}]}` |
| **state**  string | The status of the VPN connection.  Returned: *state=present*  Sample: `"{'state': 'available'}"` |
| **tags**  dictionary | The tags associated with the connection.  Returned: *state=present*  Sample: `{"tags": {"name": "ansible-test", "other": "tag"}}` |
| **type**  string | The type of VPN connection (currently only ipsec.1 is available).  Returned: *state=present*  Sample: `"{'type': 'ipsec.1'}"` |
| **vgw_telemetry**  list / elements=string | The telemetry for the VPN tunnel.  Returned: *state=present*  Sample: `{"vgw_telemetry": [{"accepted_route_count": 123, "last_status_change": "datetime(2015, 1, 1)", "outside_ip_address": "string", "status": "up", "status_message": "string"}]}` |
| **vpn_connection_id**  string | The identifier for the VPN connection.  Returned: *state=present*  Sample: `"{'vpn_connection_id': 'vpn-781e0e19'}"` |
| **vpn_gateway_id**  string | The virtual private gateway connected via the connection.  Returned: *state=present*  Sample: `"{'vpn_gateway_id': 'vgw-cb0ae2a2'}"` |

### Authors

- Sloane Hertel (@s-hertel)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
