---
collection: ansible
version: "6"
title: "community.network.avi_healthmonitor module – Module for setup of HealthMonitor Avi RESTful Object"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/avi_healthmonitor_module.html
fetched_at: 2026-07-27T17:16:46+00:00
---
# community.network.avi_healthmonitor module – Module for setup of HealthMonitor Avi RESTful Object

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
> You need further requirements to be able to use this module,
> see [Requirements](avi_healthmonitor_module.md#ansible-collections-community-network-avi-healthmonitor-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.avi_healthmonitor`.

- [Synopsis](avi_healthmonitor_module.md#synopsis)
- [Requirements](avi_healthmonitor_module.md#requirements)
- [Parameters](avi_healthmonitor_module.md#parameters)
- [Notes](avi_healthmonitor_module.md#notes)
- [Examples](avi_healthmonitor_module.md#examples)
- [Return Values](avi_healthmonitor_module.md#return-values)

## [Synopsis](avi_healthmonitor_module.md#id1)

- This module is used to configure HealthMonitor object
- more examples at <https://github.com/avinetworks/devops>

## [Requirements](avi_healthmonitor_module.md#id2)

The below requirements are needed on the host that executes this module.

- avisdk

## [Parameters](avi_healthmonitor_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_context**  dictionary | Avi API context that includes current session ID and CSRF Token.  This allows user to perform single login and re-use the session. |
| **api_version**  string | Avi API version of to use for Avi API and objects.  Default: `"16.4.4"` |
| **avi_api_patch_op**  string | Patch operation to use when using avi_api_update_method as patch.  Choices:   - `"add"` - `"replace"` - `"delete"` |
| **avi_api_update_method**  string | Default method for object update is HTTP PUT.  Setting to patch will override that behavior to use HTTP PATCH.  Choices:   - `"put"` ← (default) - `"patch"` |
| **avi_credentials**  dictionary | Avi Credentials dictionary which can be used in lieu of enumerating Avi Controller login details. |
| **api_version**  string | Avi controller version  Default: `"16.4.4"` |
| **controller**  string | Avi controller IP or SQDN |
| **csrftoken**  string | Avi controller API csrftoken to reuse existing session with session id  Default: `""` |
| **password**  string | Avi controller password |
| **port**  string | Avi controller port |
| **session_id**  string | Avi controller API session id to reuse existing session with csrftoken  Default: `""` |
| **tenant**  string | Avi controller tenant  Default: `"admin"` |
| **tenant_uuid**  string | Avi controller tenant UUID  Default: `""` |
| **timeout**  string | Avi controller request timeout  Default: `300` |
| **token**  string | Avi controller API token  Default: `""` |
| **username**  string | Avi controller username |
| **avi_disable_session_cache_as_fact**  boolean | It disables avi session information to be cached as a fact.  Choices:   - `false` ← (default) - `true` |
| **controller**  string | IP address or hostname of the controller. The default value is the environment variable `AVI_CONTROLLER`. |
| **description**  string | User defined description for the object. |
| **dns_monitor**  string | Healthmonitordns settings for healthmonitor. |
| **external_monitor**  string | Healthmonitorexternal settings for healthmonitor. |
| **failed_checks**  string | Number of continuous failed health checks before the server is marked down.  Allowed values are 1-50.  Default value when not specified in API or module is interpreted by Avi Controller as 2. |
| **http_monitor**  string | Healthmonitorhttp settings for healthmonitor. |
| **https_monitor**  string | Healthmonitorhttp settings for healthmonitor. |
| **is_federated**  boolean | This field describes the object’s replication scope.  If the field is set to false, then the object is visible within the controller-cluster and its associated service-engines.  If the field is set to true, then the object is replicated across the federation.  Field introduced in 17.1.3.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **monitor_port**  string | Use this port instead of the port defined for the server in the pool.  If the monitor succeeds to this port, the load balanced traffic will still be sent to the port of the server defined within the pool.  Allowed values are 1-65535.  Special values are 0 - ‘use server port’. |
| **name**  string / required | A user friendly name for this health monitor. |
| **password**  string | Password of Avi user in Avi controller. The default value is the environment variable `AVI_PASSWORD`. |
| **radius_monitor**  string | Health monitor for radius.  Field introduced in 18.2.3. |
| **receive_timeout**  string | A valid response from the server is expected within the receive timeout window.  This timeout must be less than the send interval.  If server status is regularly flapping up and down, consider increasing this value.  Allowed values are 1-2400.  Default value when not specified in API or module is interpreted by Avi Controller as 4. |
| **send_interval**  string | Frequency, in seconds, that monitors are sent to a server.  Allowed values are 1-3600.  Default value when not specified in API or module is interpreted by Avi Controller as 10. |
| **sip_monitor**  string | Health monitor for sip.  Field introduced in 17.2.8, 18.1.3, 18.2.1. |
| **state**  string | The state that should be applied on the entity.  Choices:   - `"absent"` - `"present"` ← (default) |
| **successful_checks**  string | Number of continuous successful health checks before server is marked up.  Allowed values are 1-50.  Default value when not specified in API or module is interpreted by Avi Controller as 2. |
| **tcp_monitor**  string | Healthmonitortcp settings for healthmonitor. |
| **tenant**  string | Name of tenant used for all Avi API calls and context of object.  Default: `"admin"` |
| **tenant_ref**  string | It is a reference to an object of type tenant. |
| **tenant_uuid**  string | UUID of tenant used for all Avi API calls and context of object.  Default: `""` |
| **type**  string / required | Type of the health monitor.  Enum options - HEALTH_MONITOR_PING, HEALTH_MONITOR_TCP, HEALTH_MONITOR_HTTP, HEALTH_MONITOR_HTTPS, HEALTH_MONITOR_EXTERNAL, HEALTH_MONITOR_UDP,  HEALTH_MONITOR_DNS, HEALTH_MONITOR_GSLB, HEALTH_MONITOR_SIP, HEALTH_MONITOR_RADIUS. |
| **udp_monitor**  string | Healthmonitorudp settings for healthmonitor. |
| **url**  string | Avi controller URL of the object. |
| **username**  string | Username used for accessing Avi controller. The default value is the environment variable `AVI_USERNAME`. |
| **uuid**  string | Uuid of the health monitor. |

## [Notes](avi_healthmonitor_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Avi Network devices see <https://www.ansible.com/ansible-avi-networks>.

## [Examples](avi_healthmonitor_module.md#id5)

```yaml+jinja
- name: Create a HTTPS health monitor
  community.network.avi_healthmonitor:
    controller: 10.10.27.90
    username: admin
    password: AviNetworks123!
    https_monitor:
      http_request: HEAD / HTTP/1.0
      http_response_code:
        - HTTP_2XX
        - HTTP_3XX
    receive_timeout: 4
    failed_checks: 3
    send_interval: 10
    successful_checks: 3
    type: HEALTH_MONITOR_HTTPS
    name: MyWebsite-HTTPS
```

## [Return Values](avi_healthmonitor_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **obj**  dictionary | HealthMonitor (api/healthmonitor) object  Returned: success, changed |

### Authors

- Gaurav Rastogi (@grastogi23)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
