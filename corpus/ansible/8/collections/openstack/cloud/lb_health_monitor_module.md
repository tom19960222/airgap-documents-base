---
collection: ansible
version: "8"
title: "openstack.cloud.lb_health_monitor module – Manage health monitor in a OpenStack load-balancer pool"
source_url: https://docs.ansible.com/projects/ansible/8/collections/openstack/cloud/lb_health_monitor_module.html
fetched_at: 2026-07-28T02:48:09+00:00
---
# openstack.cloud.lb_health_monitor module – Manage health monitor in a OpenStack load-balancer pool

> **Note:**
>
> This module is part of the [openstack.cloud collection](https://galaxy.ansible.com/ui/repo/published/openstack/cloud/) (version 2.2.0).
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

- Add, update or remove health monitor from a load-balancer pool in OpenStack cloud.

## [Requirements](lb_health_monitor_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- openstacksdk >= 1.0.0

## [Parameters](lb_health_monitor_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  integer | How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library. |
| **auth**  dictionary | Dictionary containing auth information as needed by the cloud’s auth plugin strategy. For the default *password* plugin, this would contain *auth_url*, *username*, *password*, *project_name* and any information about domains (for example, *user_domain_name* or *project_domain_name*) if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_\* environment variables are present. |
| **auth_type**  string | Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the *auth* parameter should be updated accordingly. |
| **ca_cert**  aliases: cacert  string | A path to a CA Cert bundle that can be used as part of verifying SSL API requests. |
| **client_cert**  aliases: cert  string | A path to a client certificate to use as part of the SSL transaction. |
| **client_key**  aliases: key  string | A path to a client key to use as part of the SSL transaction. |
| **cloud**  any | Named cloud or cloud config to operate against. If *cloud* is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for *auth* and *auth_type*. This parameter is not needed if *auth* is provided or if OpenStack OS_\* environment variables are present. If *cloud* is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml. |
| **delay**  integer | The interval, in seconds, between health checks.  Required when *state* is `present`. |
| **expected_codes**  string | The list of HTTP status codes expected in response from the member to declare it healthy. Specify one of the following values.  For example, *expected_codes* could be a single value, such as `200`, a list, such as `200, 202` or a range, such as `200-204`.  Octavia’s default for *expected_codes* is `200`. |
| **health_monitor_timeout**  aliases: resp_timeout  integer | The time, in seconds, after which a health check times out.  Must be less than *delay*.  Required when *state* is `present`. |
| **http_method**  string | The HTTP method that the health monitor uses for requests.  For example, *http_method* could be `CONNECT`, `DELETE`, `GET`, `HEAD`, `OPTIONS`, `PATCH`, `POST`, `PUT`, or `TRACE`.  Octavia’s default for *http_method* is `GET`. |
| **interface**  aliases: endpoint_type  string | Endpoint URL type to fetch from the service catalog.  **Choices:**   - `"admin"` - `"internal"` - `"public"` ← (default) |
| **is_admin_state_up**  aliases: admin_state_up  boolean | Whether the health monitor is up or down.  **Choices:**   - `false` - `true` |
| **max_retries**  integer | The number of successful checks before changing the operating status of the member to ONLINE.  Required when *state* is `present`. |
| **max_retries_down**  integer | The number of allowed check failures before changing the operating status of the member to ERROR. A valid value is from 1 to 10. |
| **name**  string / required | Name that has to be given to the health monitor.  This attribute cannot be updated. |
| **pool**  string | The pool name or id to monitor by the health monitor.  Required when *state* is `present`.  This attribute cannot be updated. |
| **region_name**  string | Name of the region. |
| **sdk_log_level**  string | Log level of the OpenStackSDK  **Choices:**   - `"INFO"` ← (default) - `"DEBUG"` |
| **sdk_log_path**  string | Path to the logfile of the OpenStackSDK. If empty no log is written |
| **state**  string | Should the resource be present or absent.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | How long should ansible wait for the requested resource.  **Default:** `180` |
| **type**  string | The type of health monitor.  For example, *type* could be `HTTP`, `HTTPS`, `PING`, `SCTP`, `TCP`, `TLS-HELLO` or `UDP-CONNECT`.  This attribute cannot be updated.  **Default:** `"HTTP"` |
| **url_path**  string | The HTTP URL path of the request sent by the monitor to test the health of a backend member.  Must be a string that begins with a forward slash (`/`).  Octavia’s default URL path is `/`. |
| **validate_certs**  aliases: verify  boolean | Whether or not SSL API requests should be verified.  Before Ansible 2.3 this defaulted to `true`.  **Choices:**   - `false` - `true` |
| **wait**  boolean | Should ansible wait until the requested resource is complete.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](lb_health_monitor_module.md#id4)

> **Note:**
>
> - The standard OpenStack environment variables, such as `OS_USERNAME` may be used instead of providing explicit values.
> - Auth information is driven by openstacksdk, which means that values can come from a yaml config file in /etc/ansible/openstack.yaml, /etc/openstack/clouds.yaml or ~/.config/openstack/clouds.yaml, then from standard environment variables, then finally by explicit parameters in plays. More information can be found at <https://docs.openstack.org/openstacksdk/>

## [Examples](lb_health_monitor_module.md#id5)

```yaml+jinja
- name: Create a load-balancer health monitor
  openstack.cloud.lb_health_monitor:
    cloud: devstack
    delay: 10
    expected_codes: '200'
    health_monitor_timeout: 5
    http_method: GET
    is_admin_state_up: true
    max_retries: 3
    max_retries_down: 4
    name: healthmonitor01
    pool: lb_pool
    state: present
    url_path: '/status'

- name: Delete a load-balancer health monitor
  openstack.cloud.lb_health_monitor:
    cloud: devstack
    name: healthmonitor01
    state: absent
```

## [Return Values](lb_health_monitor_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **health_monitor**  dictionary | Dictionary describing the load-balancer health monitor.  **Returned:** On success when *state* is `present`. |
| **created_at**  string | The UTC date and timestamp when the resource was created.  **Returned:** success |
| **delay**  integer | The time, in seconds, between sending probes to members.  **Returned:** success |
| **expected_codes**  string | The list of HTTP status codes expected in response from the member to declare it healthy.  **Returned:** success |
| **http_method**  string | The HTTP method that the health monitor uses for requests.  **Returned:** success |
| **id**  string | The health monitor UUID.  **Returned:** success |
| **is_admin_state_up**  boolean | The administrative state of the resource.  **Returned:** success |
| **max_retries**  integer | The number of successful checks before changing the operating status of the member to ONLINE.  **Returned:** success |
| **max_retries_down**  integer | The number of allowed check failures before changing the operating status of the member to ERROR.  **Returned:** success |
| **name**  string | Human-readable name of the resource.  **Returned:** success |
| **operating_status**  string | The operating status of the resource.  **Returned:** success |
| **pool_id**  string | The id of the pool.  **Returned:** success |
| **pools**  list / elements=string | List of associated pool ids.  **Returned:** success |
| **project_id**  string | The ID of the project owning this resource.  **Returned:** success |
| **provisioning_status**  string | The provisioning status of the resource.  **Returned:** success |
| **tags**  list / elements=string | A list of associated tags.  **Returned:** success |
| **timeout**  integer | The maximum time, in seconds, that a monitor waits to connect before it times out.  **Returned:** success |
| **type**  string | The type of health monitor.  **Returned:** success |
| **updated_at**  string | The UTC date and timestamp when the resource was last updated.  **Returned:** success |
| **url_path**  string | The HTTP URL path of the request sent by the monitor to test the health of a backend member.  **Returned:** success |

### Authors

- OpenStack Ansible SIG

### Collection links

- [Issue Tracker](https://storyboard.openstack.org/#!/project/openstack/ansible-collections-openstack)
- [Repository (Sources)](https://opendev.org/openstack/ansible-collections-openstack)
