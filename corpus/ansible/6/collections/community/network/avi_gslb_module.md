---
collection: ansible
version: "6"
title: "community.network.avi_gslb module – Module for setup of Gslb Avi RESTful Object"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/avi_gslb_module.html
fetched_at: 2026-07-27T17:16:43+00:00
---
# community.network.avi_gslb module – Module for setup of Gslb Avi RESTful Object

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
> see [Requirements](avi_gslb_module.md#ansible-collections-community-network-avi-gslb-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.avi_gslb`.

- [Synopsis](avi_gslb_module.md#synopsis)
- [Requirements](avi_gslb_module.md#requirements)
- [Parameters](avi_gslb_module.md#parameters)
- [Notes](avi_gslb_module.md#notes)
- [Examples](avi_gslb_module.md#examples)
- [Return Values](avi_gslb_module.md#return-values)

## [Synopsis](avi_gslb_module.md#id1)

- This module is used to configure Gslb object
- more examples at <https://github.com/avinetworks/devops>

## [Requirements](avi_gslb_module.md#id2)

The below requirements are needed on the host that executes this module.

- avisdk

## [Parameters](avi_gslb_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_context**  dictionary | Avi API context that includes current session ID and CSRF Token.  This allows user to perform single login and re-use the session. |
| **api_version**  string | Avi API version of to use for Avi API and objects.  Default: `"16.4.4"` |
| **async_interval**  string | Frequency with which messages are propagated to vs mgr.  Value of 0 disables async behavior and rpc are sent inline.  Allowed values are 0-5.  Field introduced in 18.2.3.  Default value when not specified in API or module is interpreted by Avi Controller as 0. |
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
| **clear_on_max_retries**  string | Max retries after which the remote site is treated as a fresh start.  In fresh start all the configs are downloaded.  Allowed values are 1-1024.  Default value when not specified in API or module is interpreted by Avi Controller as 20. |
| **client_ip_addr_group**  string | Group to specify if the client ip addresses are public or private.  Field introduced in 17.1.2. |
| **controller**  string | IP address or hostname of the controller. The default value is the environment variable `AVI_CONTROLLER`. |
| **description**  string | User defined description for the object. |
| **dns_configs**  string | Sub domain configuration for the gslb.  Gslb service’s fqdn must be a match one of these subdomains. |
| **is_federated**  boolean | This field indicates that this object is replicated across gslb federation.  Field introduced in 17.1.3.  Default value when not specified in API or module is interpreted by Avi Controller as True.  Choices:   - `false` - `true` |
| **leader_cluster_uuid**  string / required | Mark this site as leader of gslb configuration.  This site is the one among the avi sites. |
| **maintenance_mode**  boolean | This field disables the configuration operations on the leader for all federated objects.  Cud operations on gslb, gslbservice, gslbgeodbprofile and other federated objects will be rejected.  The rest-api disabling helps in upgrade scenarios where we don’t want configuration sync operations to the gslb member when the member is being  upgraded.  This configuration programmatically blocks the leader from accepting new gslb configuration when member sites are undergoing upgrade.  Field introduced in 17.2.1.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **name**  string / required | Name for the gslb object. |
| **password**  string | Password of Avi user in Avi controller. The default value is the environment variable `AVI_PASSWORD`. |
| **send_interval**  string | Frequency with which group members communicate.  Allowed values are 1-3600.  Default value when not specified in API or module is interpreted by Avi Controller as 15. |
| **send_interval_prior_to_maintenance_mode**  string | The user can specify a send-interval while entering maintenance mode.  The validity of this ‘maintenance send-interval’ is only during maintenance mode.  When the user leaves maintenance mode, the original send-interval is reinstated.  This internal variable is used to store the original send-interval.  Field introduced in 18.2.3. |
| **sites**  string | Select avi site member belonging to this gslb. |
| **state**  string | The state that should be applied on the entity.  Choices:   - `"absent"` - `"present"` ← (default) |
| **tenant**  string | Name of tenant used for all Avi API calls and context of object.  Default: `"admin"` |
| **tenant_ref**  string | It is a reference to an object of type tenant. |
| **tenant_uuid**  string | UUID of tenant used for all Avi API calls and context of object.  Default: `""` |
| **third_party_sites**  string | Third party site member belonging to this gslb.  Field introduced in 17.1.1. |
| **url**  string | Avi controller URL of the object. |
| **username**  string | Username used for accessing Avi controller. The default value is the environment variable `AVI_USERNAME`. |
| **uuid**  string | Uuid of the gslb object. |
| **view_id**  string | The view-id is used in change-leader mode to differentiate partitioned groups while they have the same gslb namespace.  Each partitioned group will be able to operate independently by using the view-id.  Default value when not specified in API or module is interpreted by Avi Controller as 0. |

## [Notes](avi_gslb_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Avi Network devices see <https://www.ansible.com/ansible-avi-networks>.

## [Examples](avi_gslb_module.md#id5)

```yaml+jinja
- name: Example to create Gslb object
  community.network.avi_gslb:
    name: "test-gslb"
    avi_credentials:
      username: '{{ username }}'
      password: '{{ password }}'
      controller: '{{ controller }}'
    sites:
      - name: "test-site1"
        username: "gslb_username"
        password: "gslb_password"
        ip_addresses:
          - type: "V4"
            addr: "10.10.28.83"
        enabled: True
        member_type: "GSLB_ACTIVE_MEMBER"
        port: 443
        cluster_uuid: "cluster-d4ee5fcc-3e0a-4d4f-9ae6-4182bc605829"
      - name: "test-site2"
        username: "gslb_username"
        password: "gslb_password"
        ip_addresses:
          - type: "V4"
            addr: "10.10.28.86"
        enabled: True
        member_type: "GSLB_ACTIVE_MEMBER"
        port: 443
        cluster_uuid: "cluster-0c37ae8d-ab62-410c-ad3e-06fa831950b1"
    dns_configs:
      - domain_name: "test1.com"
      - domain_name: "test2.com"
    leader_cluster_uuid: "cluster-d4ee5fcc-3e0a-4d4f-9ae6-4182bc605829"

- name: Update Gslb site's configurations (Patch Add Operation)
  community.network.avi_gslb:
    avi_credentials:
      username: '{{ username }}'
      password: '{{ password }}'
      controller: '{{ controller }}'
    avi_api_update_method: patch
    avi_api_patch_op: add
    leader_cluster_uuid: "cluster-d4ee5fcc-3e0a-4d4f-9ae6-4182bc605829"
    name: "test-gslb"
    dns_configs:
      - domain_name: "temp1.com"
      - domain_name: "temp2.com"
    gslb_sites_config:
      - ip_addr: "10.10.28.83"
        dns_vses:
          - dns_vs_uuid: "virtualservice-f2a711cd-5e78-473f-8f47-d12de660fd62"
            domain_names:
              - "test1.com"
              - "test2.com"
      - ip_addr: "10.10.28.86"
        dns_vses:
          - dns_vs_uuid: "virtualservice-c1a63a16-f2a1-4f41-aab4-1e90f92a5e49"
            domain_names:
              - "temp1.com"
              - "temp2.com"

- name: Update Gslb site's configurations (Patch Replace Operation)
  community.network.avi_gslb:
    avi_credentials:
      username: "{{ username }}"
      password: "{{ password }}"
      controller: "{{ controller }}"
    # On basis of cluster leader uuid dns_configs is set for that particular leader cluster
    leader_cluster_uuid: "cluster-84aa795f-8f09-42bb-97a4-5103f4a53da9"
    name: "test-gslb"
    avi_api_update_method: patch
    avi_api_patch_op: replace
    dns_configs:
      - domain_name: "test3.com"
      - domain_name: "temp3.com"
    gslb_sites_config:
      # Ip address is mapping key for dns_vses field update. For the given IP address,
      # dns_vses is updated.
      - ip_addr: "10.10.28.83"
        dns_vses:
          - dns_vs_uuid: "virtualservice-7c947ed4-77f3-4a52-909c-4f12afaf5bb0"
            domain_names:
              - "test3.com"
      - ip_addr: "10.10.28.86"
        dns_vses:
          - dns_vs_uuid: "virtualservice-799b2c6d-7f2d-4c3f-94c6-6e813b20b674"
            domain_names:
              - "temp3.com"

- name: Update Gslb site's configurations (Patch Delete Operation)
  community.network.avi_gslb:
    avi_credentials:
      username: "{{ username }}"
      password: "{{ password }}"
      controller: "{{ controller }}"
    # On basis of cluster leader uuid dns_configs is set for that particular leader cluster
    leader_cluster_uuid: "cluster-84aa795f-8f09-42bb-97a4-5103f4a53da9"
    name: "test-gslb"
    avi_api_update_method: patch
    avi_api_patch_op: delete
    dns_configs:
    gslb_sites_config:
      - ip_addr: "10.10.28.83"
      - ip_addr: "10.10.28.86"
```

## [Return Values](avi_gslb_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **obj**  dictionary | Gslb (api/gslb) object  Returned: success, changed |

### Authors

- Gaurav Rastogi (@grastogi23)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
