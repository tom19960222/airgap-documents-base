---
collection: ansible
version: "8"
title: "amazon.aws.elb_classic_lb module – Creates, updates or destroys an Amazon ELB"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/elb_classic_lb_module.html
fetched_at: 2026-07-28T01:06:49+00:00
---
# amazon.aws.elb_classic_lb module – Creates, updates or destroys an Amazon ELB

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
> see [Requirements](elb_classic_lb_module.md#ansible-collections-amazon-aws-elb-classic-lb-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.elb_classic_lb`.

New in amazon.aws 1.0.0

- [Synopsis](elb_classic_lb_module.md#synopsis)
- [Requirements](elb_classic_lb_module.md#requirements)
- [Parameters](elb_classic_lb_module.md#parameters)
- [Notes](elb_classic_lb_module.md#notes)
- [Examples](elb_classic_lb_module.md#examples)
- [Return Values](elb_classic_lb_module.md#return-values)

## [Synopsis](elb_classic_lb_module.md#id1)

- Creates, updates or destroys an Amazon Elastic Load Balancer (ELB).
- This module was renamed from `amazon.aws.ec2_elb_lb` to [amazon.aws.elb_classic_lb](elb_classic_lb_module.md#ansible-collections-amazon-aws-elb-classic-lb-module) in version 2.1.0 of the amazon.aws collection.

Aliases: ec2_elb_lb

## [Requirements](elb_classic_lb_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](elb_classic_lb_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **access_logs**  dictionary | A dictionary of access logs configuration settings (see examples). |
| **enabled**  boolean | When set to `True` will configure delivery of access logs to an S3 bucket.  When set to `False` will disable delivery of access logs.  **Choices:**   - `false` - `true` ← (default) |
| **interval**  integer | The interval for publishing the access logs to S3.  **Choices:**   - `5` - `60` ← (default) |
| **s3_location**  string | The S3 bucket to deliver access logs to.  See <https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-access-logs.html> for more information about the necessary S3 bucket policies.  Required when *enabled=True*. |
| **s3_prefix**  string | Where in the S3 bucket to deliver the logs.  If the prefix is not provided or set to `""`, the log is placed at the root level of the bucket.  **Default:** `""` |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **connection_draining_timeout**  integer | Wait a specified timeout allowing connections to drain before terminating an instance.  Set to `0` to disable connection draining. |
| **cross_az_load_balancing**  boolean | Distribute load across all configured Availability Zones.  Defaults to `false`.  **Choices:**   - `false` - `true` |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **health_check**  dictionary | A dictionary of health check configuration settings (see examples). |
| **healthy_threshold**  integer / required | The number of consecutive health checks successes required before moving the instance to the Healthy state. |
| **interval**  integer / required | The approximate interval, in seconds, between health checks of an individual instance. |
| **ping_path**  string | The URI path which the ELB health check will query when performing a health check.  Required when *ping_protocol=HTTP* or *ping_protocol=HTTPS*. |
| **ping_port**  integer / required | The TCP port to which the ELB will connect when performing a health check. |
| **ping_protocol**  string / required | The protocol which the ELB health check will use when performing a health check.  Valid values are `'HTTP'`, `'HTTPS'`, `'TCP'` and `'SSL'`. |
| **timeout**  aliases: response_timeout  integer / required | The amount of time, in seconds, after which no response means a failed health check. |
| **unhealthy_threshold**  integer / required | The number of consecutive health check failures required before moving the instance to the Unhealthy state. |
| **idle_timeout**  integer | ELB connections from clients and to servers are timed out after this amount of time. |
| **instance_ids**  list / elements=string | List of instance ids to attach to this ELB. |
| **listeners**  list / elements=dictionary | List of ports/protocols for this ELB to listen on (see examples).  Required when *state=present* and the ELB doesn’t exist. |
| **instance_port**  integer / required | The port on which the instance is listening. |
| **instance_protocol**  string | The protocol to use for routing traffic to instances.  Valid values are `HTTP`, `HTTPS`, `TCP`, or `SSL`, |
| **load_balancer_port**  integer / required | The port on which the load balancer will listen. |
| **protocol**  string / required | The transport protocol to use for routing.  Valid values are `HTTP`, `HTTPS`, `TCP`, or `SSL`. |
| **proxy_protocol**  boolean | Enable proxy protocol for the listener.  Beware, ELB controls for the proxy protocol are based on the *instance_port*. If you have multiple listeners talking to the same *instance_port*, this will affect all of them.  **Choices:**   - `false` - `true` |
| **ssl_certificate_id**  string | The Amazon Resource Name (ARN) of the SSL certificate. |
| **name**  string / required | The name of the ELB.  The name of an ELB must be less than 32 characters and unique per-region per-account. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_instance_ids**  boolean | Purge existing instance ids on ELB that are not found in *instance_ids*.  **Choices:**   - `false` ← (default) - `true` |
| **purge_listeners**  boolean | Purge existing listeners on ELB that are not found in listeners.  **Choices:**   - `false` - `true` ← (default) |
| **purge_subnets**  boolean | Purge existing subnets on the ELB that are not found in *subnets*.  Because it is not permitted to add multiple subnets from the same availability zone, subnets to be purged will be removed before new subnets are added. This may cause a brief outage if you try to replace all subnets at once.  **Choices:**   - `false` ← (default) - `true` |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **purge_zones**  boolean | Purge existing availability zones on ELB that are not found in *zones*.  **Choices:**   - `false` ← (default) - `true` |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **scheme**  string | The scheme to use when creating the ELB.  For a private VPC-visible ELB use `internal`.  If you choose to update your scheme with a different value the ELB will be destroyed and a new ELB created.  Defaults to *scheme=internet-facing*.  **Choices:**   - `"internal"` - `"internet-facing"` |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **security_group_ids**  list / elements=string | A list of security groups to apply to the ELB. |
| **security_group_names**  list / elements=string | A list of security group names to apply to the ELB. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string / required | Create or destroy the ELB.  **Choices:**   - `"absent"` - `"present"` |
| **stickiness**  dictionary | A dictionary of stickiness policy settings.  Policy will be applied to all listeners (see examples). |
| **cookie**  string | The name of the application cookie used for stickiness.  Required if *enabled=true* and *type=application*.  Ignored if *enabled=false*. |
| **enabled**  boolean | When *enabled=false* session stickiness will be disabled for all listeners.  **Choices:**   - `false` - `true` ← (default) |
| **expiration**  integer | The time period, in seconds, after which the cookie should be considered stale.  If this parameter is not specified, the stickiness session lasts for the duration of the browser session.  Ignored if *enabled=false*. |
| **type**  string | The type of stickiness policy to apply.  Required if *enabled=true*.  Ignored if *enabled=false*.  **Choices:**   - `"application"` - `"loadbalancer"` |
| **subnets**  list / elements=string | A list of VPC subnets to use when creating the ELB.  Mutually exclusive with *zones*. |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **wait**  boolean | When creating, deleting, or adding instances to an ELB, if *wait=true* Ansible will wait for both the load balancer and related network interfaces to finish creating/deleting.  Support for waiting when adding instances was added in release 2.1.0.  **Choices:**   - `false` ← (default) - `true` |
| **wait_timeout**  integer | Used in conjunction with wait. Number of seconds to wait for the ELB to be terminated.  A maximum of 600 seconds (10 minutes) is allowed.  **Default:** `180` |
| **zones**  list / elements=string | List of availability zones to enable on this ELB.  Mutually exclusive with *subnets*. |

## [Notes](elb_classic_lb_module.md#id4)

> **Note:**
>
> - The ec2_elb fact previously set by this module was deprecated in release 2.1.0 and since release 4.0.0 is no longer set.
> - Support for *purge_tags* was added in release 2.1.0.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](elb_classic_lb_module.md#id5)

```yaml+jinja
# Note: None of these examples set aws_access_key, aws_secret_key, or region.
# It is assumed that their matching environment variables are set.

# Basic provisioning example (non-VPC)

- amazon.aws.elb_classic_lb:
    name: "test-please-delete"
    state: present
    zones:
      - us-east-1a
      - us-east-1d
    listeners:
      - protocol: http # options are http, https, ssl, tcp
        load_balancer_port: 80
        instance_port: 80
        proxy_protocol: True
      - protocol: https
        load_balancer_port: 443
        instance_protocol: http # optional, defaults to value of protocol setting
        instance_port: 80
        # ssl certificate required for https or ssl
        ssl_certificate_id: "arn:aws:iam::123456789012:server-certificate/company/servercerts/ProdServerCert"

# Internal ELB example

- amazon.aws.elb_classic_lb:
    name: "test-vpc"
    scheme: internal
    state: present
    instance_ids:
      - i-abcd1234
    purge_instance_ids: true
    subnets:
      - subnet-abcd1234
      - subnet-1a2b3c4d
    listeners:
      - protocol: http # options are http, https, ssl, tcp
        load_balancer_port: 80
        instance_port: 80

# Configure a health check and the access logs
- amazon.aws.elb_classic_lb:
    name: "test-please-delete"
    state: present
    zones:
      - us-east-1d
    listeners:
      - protocol: http
        load_balancer_port: 80
        instance_port: 80
    health_check:
        ping_protocol: http # options are http, https, ssl, tcp
        ping_port: 80
        ping_path: "/index.html" # not required for tcp or ssl
        response_timeout: 5 # seconds
        interval: 30 # seconds
        unhealthy_threshold: 2
        healthy_threshold: 10
    access_logs:
        interval: 5 # minutes (defaults to 60)
        s3_location: "my-bucket" # This value is required if access_logs is set
        s3_prefix: "logs"

# Ensure ELB is gone
- amazon.aws.elb_classic_lb:
    name: "test-please-delete"
    state: absent

# Ensure ELB is gone and wait for check (for default timeout)
- amazon.aws.elb_classic_lb:
    name: "test-please-delete"
    state: absent
    wait: true

# Ensure ELB is gone and wait for check with timeout value
- amazon.aws.elb_classic_lb:
    name: "test-please-delete"
    state: absent
    wait: true
    wait_timeout: 600

# Normally, this module will purge any listeners that exist on the ELB
# but aren't specified in the listeners parameter. If purge_listeners is
# false it leaves them alone
- amazon.aws.elb_classic_lb:
    name: "test-please-delete"
    state: present
    zones:
      - us-east-1a
      - us-east-1d
    listeners:
      - protocol: http
        load_balancer_port: 80
        instance_port: 80
    purge_listeners: false

# Normally, this module will leave availability zones that are enabled
# on the ELB alone. If purge_zones is true, then any extraneous zones
# will be removed
- amazon.aws.elb_classic_lb:
    name: "test-please-delete"
    state: present
    zones:
      - us-east-1a
      - us-east-1d
    listeners:
      - protocol: http
        load_balancer_port: 80
        instance_port: 80
    purge_zones: true

# Creates a ELB and assigns a list of subnets to it.
- amazon.aws.elb_classic_lb:
    state: present
    name: 'New ELB'
    security_group_ids: 'sg-123456, sg-67890'
    subnets: 'subnet-123456,subnet-67890'
    purge_subnets: true
    listeners:
      - protocol: http
        load_balancer_port: 80
        instance_port: 80

# Create an ELB with connection draining, increased idle timeout and cross availability
# zone load balancing
- amazon.aws.elb_classic_lb:
    name: "New ELB"
    state: present
    connection_draining_timeout: 60
    idle_timeout: 300
    cross_az_load_balancing: "yes"
    zones:
      - us-east-1a
      - us-east-1d
    listeners:
      - protocol: http
        load_balancer_port: 80
        instance_port: 80

# Create an ELB with load balancer stickiness enabled
- amazon.aws.elb_classic_lb:
    name: "New ELB"
    state: present
    zones:
      - us-east-1a
      - us-east-1d
    listeners:
      - protocol: http
        load_balancer_port: 80
        instance_port: 80
    stickiness:
      type: loadbalancer
      enabled: true
      expiration: 300

# Create an ELB with application stickiness enabled
- amazon.aws.elb_classic_lb:
    name: "New ELB"
    state: present
    zones:
      - us-east-1a
      - us-east-1d
    listeners:
      - protocol: http
        load_balancer_port: 80
        instance_port: 80
    stickiness:
      type: application
      enabled: true
      cookie: SESSIONID

# Create an ELB and add tags
- amazon.aws.elb_classic_lb:
    name: "New ELB"
    state: present
    zones:
      - us-east-1a
      - us-east-1d
    listeners:
      - protocol: http
        load_balancer_port: 80
        instance_port: 80
    tags:
      Name: "New ELB"
      stack: "production"
      client: "Bob"

# Delete all tags from an ELB
- amazon.aws.elb_classic_lb:
    name: "New ELB"
    state: present
    zones:
      - us-east-1a
      - us-east-1d
    listeners:
      - protocol: http
        load_balancer_port: 80
        instance_port: 80
    tags: {}
```

## [Return Values](elb_classic_lb_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **elb**  dictionary | Load Balancer attributes  **Returned:** always |
| **app_cookie_policy**  string | The name of the policy used to control if the ELB is using a application cookie stickiness policy.  **Returned:** when state is not ‘absent’  **Sample:** `"ec2-elb-lb-AppCookieStickinessPolicyType"` |
| **backends**  string | A description of the backend policy applied to the ELB (instance-port:policy-name).  **Returned:** when state is not ‘absent’  **Sample:** `"8181:ProxyProtocol-policy"` |
| **connection_draining_timeout**  integer | The maximum time, in seconds, to keep the existing connections open before deregistering the instances.  **Returned:** when state is not ‘absent’  **Sample:** `25` |
| **cross_az_load_balancing**  string | Either `'yes'` if cross-AZ load balancing is enabled, or `'no'` if cross-AZ load balancing is disabled.  **Returned:** when state is not ‘absent’  **Sample:** `"yes"` |
| **dns_name**  string | The DNS name of the ELB.  **Returned:** when state is not ‘absent’  **Sample:** `"internal-ansible-test-935c585850ac-1516306744.us-east-1.elb.amazonaws.com"` |
| **health_check**  dictionary | A dictionary describing the health check used for the ELB.  **Returned:** when state is not ‘absent’ |
| **healthy_threshold**  integer | The number of consecutive successful health checks before marking an instance as healthy.  **Returned:** success  **Sample:** `2` |
| **interval**  integer | The time, in seconds, between each health check.  **Returned:** success  **Sample:** `10` |
| **target**  string | The Protocol, Port, and for HTTP(S) health checks the path tested by the health check.  **Returned:** success  **Sample:** `"TCP:22"` |
| **timeout**  integer | The time, in seconds, after which an in progress health check is considered failed due to a timeout.  **Returned:** success  **Sample:** `5` |
| **unhealthy_threshold**  integer | The number of consecutive failed health checks before marking an instance as unhealthy.  **Returned:** success  **Sample:** `2` |
| **hosted_zone_id**  string | The ID of the Amazon Route 53 hosted zone for the load balancer.  **Returned:** when state is not ‘absent’  **Sample:** `"Z35SXDOTRQ7X7K"` |
| **hosted_zone_name**  string | The DNS name of the load balancer when using a custom hostname.  **Returned:** when state is not ‘absent’  **Sample:** `"ansible-module.example"` |
| **idle_timeout**  integer | The length of of time before an idle connection is dropped by the ELB.  **Returned:** when state is not ‘absent’  **Sample:** `50` |
| **in_service_count**  integer | The number of instances attached to the ELB in an in-service state.  **Returned:** when state is not ‘absent’  **Sample:** `1` |
| **instance_health**  list / elements=dictionary | A list of dictionaries describing the health of each instance attached to the ELB.  **Returned:** when state is not ‘absent’ |
| **description**  string | A human readable description of why the instance is not in service.  **Returned:** when state is not ‘absent’  **Sample:** `"N/A"` |
| **instance_id**  string | The ID of the instance.  **Returned:** when state is not ‘absent’  **Sample:** `"i-03dcc8953a03d6435"` |
| **reason_code**  string | A code describing why the instance is not in service.  **Returned:** when state is not ‘absent’  **Sample:** `"N/A"` |
| **state**  string | The current service state of the instance.  **Returned:** when state is not ‘absent’  **Sample:** `"InService"` |
| **instances**  list / elements=string | A list of the IDs of instances attached to the ELB.  **Returned:** when state is not ‘absent’  **Sample:** `["i-03dcc8953a03d6435"]` |
| **lb_cookie_policy**  string | The name of the policy used to control if the ELB is using a cookie stickiness policy.  **Returned:** when state is not ‘absent’  **Sample:** `"ec2-elb-lb-LBCookieStickinessPolicyType"` |
| **listeners**  list / elements=list | A list of lists describing the listeners attached to the ELB.  The nested list contains the listener port, the instance port, the listener protoco, the instance port, and where appropriate the ID of the SSL certificate for the port.  **Returned:** when state is not ‘absent’  **Sample:** `[[22, 22, "TCP", "TCP"], [80, 8181, "HTTP", "HTTP"]]` |
| **name**  string | The name of the ELB. This name is unique per-region, per-account.  **Returned:** when state is not ‘absent’  **Sample:** `"ansible-test-935c585850ac"` |
| **out_of_service_count**  integer | The number of instances attached to the ELB in an out-of-service state.  **Returned:** when state is not ‘absent’  **Sample:** `0` |
| **proxy_policy**  string | The name of the policy used to control if the ELB operates using the Proxy protocol.  **Returned:** when the proxy protocol policy exists.  **Sample:** `"ProxyProtocol-policy"` |
| **region**  string | The AWS region in which the ELB is running.  **Returned:** always  **Sample:** `"us-east-1"` |
| **scheme**  string | Whether the ELB is an `'internal'` or a `'internet-facing'` load balancer.  **Returned:** when state is not ‘absent’  **Sample:** `"internal"` |
| **security_group_ids**  list / elements=string | A list of the IDs of the Security Groups attached to the ELB.  **Returned:** when state is not ‘absent’  **Sample:** `["sg-0c12ebd82f2fb97dc", "sg-01ec7378d0c7342e6"]` |
| **status**  string | A minimal description of the current state of the ELB. Valid values are `'exists'`, `'gone'`, `'deleted'`, `'created'`.  **Returned:** always  **Sample:** `"exists"` |
| **subnets**  list / elements=string | A list of the subnet IDs attached to the ELB.  **Returned:** when state is not ‘absent’  **Sample:** `["subnet-00d9d0f70c7e5f63c", "subnet-03fa5253586b2d2d5"]` |
| **tags**  dictionary | A dictionary describing the tags attached to the ELB.  **Returned:** when state is not ‘absent’  **Sample:** `{"ExampleTag": "Example Value", "Name": "ansible-test-935c585850ac"}` |
| **unknown_instance_state_count**  integer | The number of instances attached to the ELB in an unknown state.  **Returned:** when state is not ‘absent’  **Sample:** `0` |
| **zones**  list / elements=string | A list of the AWS regions in which the ELB is running.  **Returned:** when state is not ‘absent’  **Sample:** `["us-east-1b", "us-east-1a"]` |

### Authors

- Jim Dalton (@jsdalton)
- Mark Chappell (@tremble)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
