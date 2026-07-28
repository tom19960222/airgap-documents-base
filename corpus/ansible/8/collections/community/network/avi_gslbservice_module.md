---
collection: ansible
version: "8"
title: "community.network.avi_gslbservice module – Module for setup of GslbService Avi RESTful Object"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/avi_gslbservice_module.html
fetched_at: 2026-07-28T01:54:40+00:00
---
# community.network.avi_gslbservice module – Module for setup of GslbService Avi RESTful Object

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
> You need further requirements to be able to use this module,
> see [Requirements](avi_gslbservice_module.md#ansible-collections-community-network-avi-gslbservice-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.avi_gslbservice`.

- [Synopsis](avi_gslbservice_module.md#synopsis)
- [Requirements](avi_gslbservice_module.md#requirements)
- [Parameters](avi_gslbservice_module.md#parameters)
- [Notes](avi_gslbservice_module.md#notes)
- [Examples](avi_gslbservice_module.md#examples)
- [Return Values](avi_gslbservice_module.md#return-values)

## [Synopsis](avi_gslbservice_module.md#id1)

- This module is used to configure GslbService object
- more examples at <https://github.com/avinetworks/devops>

Aliases: network.avi.avi_gslbservice

## [Requirements](avi_gslbservice_module.md#id2)

The below requirements are needed on the host that executes this module.

- avisdk

## [Parameters](avi_gslbservice_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_context**  dictionary | Avi API context that includes current session ID and CSRF Token.  This allows user to perform single login and re-use the session. |
| **api_version**  string | Avi API version of to use for Avi API and objects.  **Default:** `"16.4.4"` |
| **application_persistence_profile_ref**  string | The federated application persistence associated with gslbservice site persistence functionality.  It is a reference to an object of type applicationpersistenceprofile.  Field introduced in 17.2.1. |
| **avi_api_patch_op**  string | Patch operation to use when using avi_api_update_method as patch.  **Choices:**   - `"add"` - `"replace"` - `"delete"` |
| **avi_api_update_method**  string | Default method for object update is HTTP PUT.  Setting to patch will override that behavior to use HTTP PATCH.  **Choices:**   - `"put"` ← (default) - `"patch"` |
| **avi_credentials**  dictionary | Avi Credentials dictionary which can be used in lieu of enumerating Avi Controller login details. |
| **api_version**  string | Avi controller version  **Default:** `"16.4.4"` |
| **controller**  string | Avi controller IP or SQDN |
| **csrftoken**  string | Avi controller API csrftoken to reuse existing session with session id  **Default:** `""` |
| **password**  string | Avi controller password |
| **port**  string | Avi controller port |
| **session_id**  string | Avi controller API session id to reuse existing session with csrftoken  **Default:** `""` |
| **tenant**  string | Avi controller tenant  **Default:** `"admin"` |
| **tenant_uuid**  string | Avi controller tenant UUID  **Default:** `""` |
| **timeout**  string | Avi controller request timeout  **Default:** `300` |
| **token**  string | Avi controller API token  **Default:** `""` |
| **username**  string | Avi controller username |
| **avi_disable_session_cache_as_fact**  boolean | It disables avi session information to be cached as a fact.  **Choices:**   - `false` ← (default) - `true` |
| **controller**  string | IP address or hostname of the controller. The default value is the environment variable `AVI_CONTROLLER`. |
| **controller_health_status_enabled**  boolean | Gs member’s overall health status is derived based on a combination of controller and datapath health-status inputs.  Note that the datapath status is determined by the association of health monitor profiles.  Only the controller provided status is determined through this configuration.  Default value when not specified in API or module is interpreted by Avi Controller as True.  **Choices:**   - `false` - `true` |
| **created_by**  string | Creator name.  Field introduced in 17.1.2. |
| **description**  string | User defined description for the object. |
| **domain_names**  string | Fully qualified domain name of the gslb service. |
| **down_response**  string | Response to the client query when the gslb service is down. |
| **enabled**  boolean | Enable or disable the gslb service.  If the gslb service is enabled, then the vips are sent in the dns responses based on reachability and configured algorithm.  If the gslb service is disabled, then the vips are no longer available in the dns response.  Default value when not specified in API or module is interpreted by Avi Controller as True.  **Choices:**   - `false` - `true` |
| **groups**  string | Select list of pools belonging to this gslb service. |
| **health_monitor_refs**  string | Verify vs health by applying one or more health monitors.  Active monitors generate synthetic traffic from dns service engine and to mark a vs up or down based on the response.  It is a reference to an object of type healthmonitor. |
| **health_monitor_scope**  string | Health monitor probe can be executed for all the members or it can be executed only for third-party members.  This operational mode is useful to reduce the number of health monitor probes in case of a hybrid scenario.  In such a case, avi members can have controller derived status while non-avi members can be probed by via health monitor probes in dataplane.  Enum options - GSLB_SERVICE_HEALTH_MONITOR_ALL_MEMBERS, GSLB_SERVICE_HEALTH_MONITOR_ONLY_NON_AVI_MEMBERS.  Default value when not specified in API or module is interpreted by Avi Controller as GSLB_SERVICE_HEALTH_MONITOR_ALL_MEMBERS. |
| **hm_off**  boolean | This field is an internal field and is used in se.  Field introduced in 18.2.2.  **Choices:**   - `false` - `true` |
| **is_federated**  boolean | This field indicates that this object is replicated across gslb federation.  Field introduced in 17.1.3.  Default value when not specified in API or module is interpreted by Avi Controller as True.  **Choices:**   - `false` - `true` |
| **min_members**  string | The minimum number of members to distribute traffic to.  Allowed values are 1-65535.  Special values are 0 - ‘disable’.  Field introduced in 17.2.4.  Default value when not specified in API or module is interpreted by Avi Controller as 0. |
| **name**  string / required | Name for the gslb service. |
| **num_dns_ip**  string | Number of ip addresses of this gslb service to be returned by the dns service.  Enter 0 to return all ip addresses.  Allowed values are 1-20.  Special values are 0- ‘return all ip addresses’. |
| **password**  string | Password of Avi user in Avi controller. The default value is the environment variable `AVI_PASSWORD`. |
| **pool_algorithm**  string | The load balancing algorithm will pick a gslb pool within the gslb service list of available pools.  Enum options - GSLB_SERVICE_ALGORITHM_PRIORITY, GSLB_SERVICE_ALGORITHM_GEO.  Field introduced in 17.2.3.  Default value when not specified in API or module is interpreted by Avi Controller as GSLB_SERVICE_ALGORITHM_PRIORITY. |
| **site_persistence_enabled**  boolean | Enable site-persistence for the gslbservice.  Field introduced in 17.2.1.  Default value when not specified in API or module is interpreted by Avi Controller as False.  **Choices:**   - `false` - `true` |
| **state**  string | The state that should be applied on the entity.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **tenant**  string | Name of tenant used for all Avi API calls and context of object.  **Default:** `"admin"` |
| **tenant_ref**  string | It is a reference to an object of type tenant. |
| **tenant_uuid**  string | UUID of tenant used for all Avi API calls and context of object.  **Default:** `""` |
| **ttl**  string | Ttl value (in seconds) for records served for this gslb service by the dns service.  Allowed values are 0-86400. |
| **url**  string | Avi controller URL of the object. |
| **use_edns_client_subnet**  boolean | Use the client ip subnet from the edns option as source ipaddress for client geo-location and consistent hash algorithm.  Default is true.  Field introduced in 17.1.1.  Default value when not specified in API or module is interpreted by Avi Controller as True.  **Choices:**   - `false` - `true` |
| **username**  string | Username used for accessing Avi controller. The default value is the environment variable `AVI_USERNAME`. |
| **uuid**  string | Uuid of the gslb service. |
| **wildcard_match**  boolean | Enable wild-card match of fqdn if an exact match is not found in the dns table, the longest match is chosen by wild-carding the fqdn in the dns  request.  Default is false.  Field introduced in 17.1.1.  Default value when not specified in API or module is interpreted by Avi Controller as False.  **Choices:**   - `false` - `true` |

## [Notes](avi_gslbservice_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Avi Network devices see <https://www.ansible.com/ansible-avi-networks>.

## [Examples](avi_gslbservice_module.md#id5)

```yaml+jinja
- name: Example to create GslbService object
  community.network.avi_gslbservice:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_gslbservice
```

## [Return Values](avi_gslbservice_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **obj**  dictionary | GslbService (api/gslbservice) object  **Returned:** success, changed |

### Authors

- Gaurav Rastogi (@grastogi23)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
