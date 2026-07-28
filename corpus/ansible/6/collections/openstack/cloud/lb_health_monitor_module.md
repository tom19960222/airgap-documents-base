---
collection: ansible
version: "6"
title: "openstack.cloud.lb_health_monitor module – Add/Delete a health m nonitor to a pool in the load balancing service from OpenStack Cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/openstack/cloud/lb_health_monitor_module.html
fetched_at: 2026-07-28T00:16:48+00:00
---
# openstack.cloud.lb_health_monitor module – Add/Delete a health m nonitor to a pool in the load balancing service from OpenStack Cloud

> **Note:**
>
> This module is part of the [openstack.cloud collection](https://galaxy.ansible.com/openstack/cloud) (version 1.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install openstack.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](lb_health_monitor_module.md#ansible-collections-openstack-cloud-lb-health-monitor-module-requirements) for details.
>
> To use it in a playbook, specify: `openstack.cloud.lb_health_monitor`.

- [Synopsis](lb_health_monitor_module.md#synopsis)
- [Requirements](lb_health_monitor_module.md#requirements)
- [Parameters](lb_health_monitor_module.md#parameters)
- [Notes](lb_health_monitor_module.md#notes)
- [Examples](lb_health_monitor_module.md#examples)
- [Return Values](lb_health_monitor_module.md#return-values)

## [Synopsis](lb_health_monitor_module.md#id1)

- Add or Remove a health monitor to/from a pool in the OpenStack load-balancer service.

## [Requirements](lb_health_monitor_module.md#id2)

The below requirements are needed on the host that executes this module.

- openstacksdk
- openstacksdk >= 0.36, < 0.99.0
- python >= 3.6

## [Parameters](lb_health_monitor_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **admin_state_up**  boolean | The admin state of the helath monitor true for up or false for down  Choices:   - `false` - `true` ← (default) |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **availability_zone**  string | Ignored. Present for backwards compatibility |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **delay**  string / required | the interval, in seconds, between health checks. |
| **expected_codes**  string | The list of HTTP status codes expected in response from the member to declare it healthy. Specify one of the following values A single value, such as 200 A list, such as 200, 202 A range, such as 200-204  Default: `"200"` |
| **http_method**  string | The HTTP method that the health monitor uses for requests. One of CONNECT, DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT, or TRACE. The default is GET.  Choices:   - `"GET"` ← (default) - `"CONNECT"` - `"DELETE"` - `"HEAD"` - `"OPTIONS"` - `"PATCH"` - `"POST"` - `"PUT"` - `"TRACE"` |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  Choices:   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **max_retries**  string / required | The number of successful checks before changing the operating status of the member to ONLINE. |
| **max_retries_down**  string | The number of allowed check failures before changing the operating status of the member to ERROR. A valid value is from 1 to 10. The default is 3.  Default: `"3"` |
| **name**  string / required | Name that has to be given to the health monitor |
| **pool**  string / required | The pool name or id to monitor by the health monitor. |
| **region_name**  string | Name of the region. |
| **resp_timeout**  integer / required | The time, in seconds, after which a health check times out. Must be less than delay |
| **sdk_log_level**  string | Log level of the OpenStackSDK  Choices:   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Should the resource be present or absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  Default: `180` |
| **type**  string | One of HTTP, HTTPS, PING, SCTP, TCP, TLS-HELLO, or UDP-CONNECT.  Choices:   - `"HTTP"` ← (default) - `"HTTPS"` - `"PING"` - `"SCTP"` - `"TCP"` - `"TLS-HELLO"` - `"UDP-CONNECT"` |
| **url_path**  string | The HTTP URL path of the request sent by the monitor to test the health of a backend member. Must be a string that begins with a forward slash (/). The default URL path is /.  Default: `"/"` |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `yes`.  Choices:   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  Choices:   - `false` - `true` ← (default) |

## [Notes](lb_health_monitor_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](lb_health_monitor_module.md#id5)

```yaml+jinja
#Create a healtmonitor named healthmonitor01 with method HEAD url_path /status and expect code 200
- openstack.cloud.lb_health_monitor:
    auth:
      auth_url: "{{keystone_url}}"
      username: "{{username}}"
      password: "{{password}}"
      project_domain_name: "{{domain_name}}"
      user_domain_name: "{{domain_name}}"
      project_name: "{{project_name}}"
    wait: true
    admin_state_up: True
    expected_codes: '200'
    max_retries_down: '4'
    http_method: GET
    url_path: "/status"
    pool: '{{pool_id}}'
    name: 'healthmonitor01'
    delay: '10'
    max_retries: '3'
    resp_timeout: '5'
    state: present
```

## [Return Values](lb_health_monitor_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **health_monitor**  complex | Dictionary describing the health monitor.  Returned: On success when `state=present` |
| **admin_state_up**  boolean | The administrative state of the resource.  Returned: On success when `state=present` |
| **created_at**  string | The UTC date and timestamp when the resource was created.  Returned: On success when `state=present` |
| **delay**  integer | The time, in seconds, between sending probes to members.  Returned: On success when `state=present` |
| **expected_codes**  string | The list of HTTP status codes expected in response from the member to declare it healthy.  Returned: On success when `state=present` |
| **http_method**  string | The HTTP method that the health monitor uses for requests.  Returned: On success when `state=present` |
| **id**  string | The health monitor UUID.  Returned: On success when `state=present` |
| **max_retries**  string | The number of successful checks before changing the operating status of the member to ONLINE.  Returned: On success when `state=present` |
| **max_retries_down**  string | The number of allowed check failures before changing the operating status of the member to ERROR.  Returned: On success when `state=present` |
| **name**  string | Human-readable name of the resource.  Returned: On success when `state=present` |
| **operating_status**  string | The operating status of the resource.  Returned: On success when `state=present` |
| **pool_id**  string | The id of the pool.  Returned: On success when `state=present` |
| **project_id**  string | The ID of the project owning this resource.  Returned: On success when `state=present` |
| **provisioning_status**  string | The provisioning status of the resource.  Returned: On success when `state=present` |
| **timeout**  integer | The maximum time, in seconds, that a monitor waits to connect before it times out.  Returned: On success when `state=present` |
| **type**  string | The type of health monitor.  Returned: On success when `state=present` |
| **updated_at**  string | The UTC date and timestamp when the resource was last updated.  Returned: On success when `state=present` |
| **url_path**  string | The HTTP URL path of the request sent by the monitor to test the health of a backend member.  Returned: On success when `state=present` |

### Authors

- OpenStack Ansible SIG

### Collection links

[Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
[Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
