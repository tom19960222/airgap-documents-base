---
collection: ansible
version: "6"
title: "community.network.avi_cloud module – Module for setup of Cloud Avi RESTful Object"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/avi_cloud_module.html
fetched_at: 2026-07-27T17:16:36+00:00
---
# community.network.avi_cloud module – Module for setup of Cloud Avi RESTful Object

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
> see [Requirements](avi_cloud_module.md#ansible-collections-community-network-avi-cloud-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.avi_cloud`.

- [Synopsis](avi_cloud_module.md#synopsis)
- [Requirements](avi_cloud_module.md#requirements)
- [Parameters](avi_cloud_module.md#parameters)
- [Notes](avi_cloud_module.md#notes)
- [Examples](avi_cloud_module.md#examples)
- [Return Values](avi_cloud_module.md#return-values)

## [Synopsis](avi_cloud_module.md#id1)

- This module is used to configure Cloud object
- more examples at <https://github.com/avinetworks/devops>

## [Requirements](avi_cloud_module.md#id2)

The below requirements are needed on the host that executes this module.

- avisdk

## [Parameters](avi_cloud_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_context**  dictionary | Avi API context that includes current session ID and CSRF Token.  This allows user to perform single login and re-use the session. |
| **api_version**  string | Avi API version of to use for Avi API and objects.  Default: `"16.4.4"` |
| **apic_configuration**  string | Apicconfiguration settings for cloud. |
| **apic_mode**  boolean | Boolean flag to set apic_mode.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **autoscale_polling_interval**  string | Cloudconnector polling interval for external autoscale groups.  Field introduced in 18.2.2.  Default value when not specified in API or module is interpreted by Avi Controller as 60. |
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
| **aws_configuration**  string | Awsconfiguration settings for cloud. |
| **azure_configuration**  string | Field introduced in 17.2.1. |
| **cloudstack_configuration**  string | Cloudstackconfiguration settings for cloud. |
| **controller**  string | IP address or hostname of the controller. The default value is the environment variable `AVI_CONTROLLER`. |
| **custom_tags**  string | Custom tags for all avi created resources in the cloud infrastructure.  Field introduced in 17.1.5. |
| **dhcp_enabled**  boolean | Select the ip address management scheme.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **dns_provider_ref**  string | Dns profile for the cloud.  It is a reference to an object of type ipamdnsproviderprofile. |
| **docker_configuration**  string | Dockerconfiguration settings for cloud. |
| **east_west_dns_provider_ref**  string | Dns profile for east-west services.  It is a reference to an object of type ipamdnsproviderprofile. |
| **east_west_ipam_provider_ref**  string | Ipam profile for east-west services.  Warning - please use virtual subnets in this ipam profile that do not conflict with the underlay networks or any overlay networks in the cluster.  For example in aws and gcp, 169.254.0.0/16 is used for storing instance metadata.  Hence, it should not be used in this profile.  It is a reference to an object of type ipamdnsproviderprofile. |
| **enable_vip_static_routes**  boolean | Use static routes for vip side network resolution during virtualservice placement.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **gcp_configuration**  string | Google cloud platform configuration.  Field introduced in 18.2.1. |
| **ip6_autocfg_enabled**  boolean | Enable ipv6 auto configuration.  Field introduced in 18.1.1.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **ipam_provider_ref**  string | Ipam profile for the cloud.  It is a reference to an object of type ipamdnsproviderprofile. |
| **license_tier**  string | Specifies the default license tier which would be used by new se groups.  This field by default inherits the value from system configuration.  Enum options - ENTERPRISE_16, ENTERPRISE_18.  Field introduced in 17.2.5. |
| **license_type**  string | If no license type is specified then default license enforcement for the cloud type is chosen.  The default mappings are container cloud is max ses, openstack and vmware is cores and linux it is sockets.  Enum options - LIC_BACKEND_SERVERS, LIC_SOCKETS, LIC_CORES, LIC_HOSTS, LIC_SE_BANDWIDTH, LIC_METERED_SE_BANDWIDTH. |
| **linuxserver_configuration**  string | Linuxserverconfiguration settings for cloud. |
| **mesos_configuration**  string | Field deprecated in 18.2.2. |
| **mtu**  string | Mtu setting for the cloud.  Default value when not specified in API or module is interpreted by Avi Controller as 1500. |
| **name**  string / required | Name of the object. |
| **nsx_configuration**  string | Configuration parameters for nsx manager.  Field introduced in 17.1.1. |
| **obj_name_prefix**  string | Default prefix for all automatically created objects in this cloud.  This prefix can be overridden by the se-group template. |
| **openstack_configuration**  string | Openstackconfiguration settings for cloud. |
| **oshiftk8s_configuration**  string | Oshiftk8sconfiguration settings for cloud. |
| **password**  string | Password of Avi user in Avi controller. The default value is the environment variable `AVI_PASSWORD`. |
| **prefer_static_routes**  boolean | Prefer static routes over interface routes during virtualservice placement.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **proxy_configuration**  string | Proxyconfiguration settings for cloud. |
| **rancher_configuration**  string | Rancherconfiguration settings for cloud. |
| **state**  string | The state that should be applied on the entity.  Choices:   - `"absent"` - `"present"` ← (default) |
| **state_based_dns_registration**  boolean | Dns records for vips are added/deleted based on the operational state of the vips.  Field introduced in 17.1.12.  Default value when not specified in API or module is interpreted by Avi Controller as True.  Choices:   - `false` - `true` |
| **tenant**  string | Name of tenant used for all Avi API calls and context of object.  Default: `"admin"` |
| **tenant_ref**  string | It is a reference to an object of type tenant. |
| **tenant_uuid**  string | UUID of tenant used for all Avi API calls and context of object.  Default: `""` |
| **url**  string | Avi controller URL of the object. |
| **username**  string | Username used for accessing Avi controller. The default value is the environment variable `AVI_USERNAME`. |
| **uuid**  string | Unique object identifier of the object. |
| **vca_configuration**  string | Vcloudairconfiguration settings for cloud. |
| **vcenter_configuration**  string | Vcenterconfiguration settings for cloud. |
| **vtype**  string / required | Cloud type.  Enum options - CLOUD_NONE, CLOUD_VCENTER, CLOUD_OPENSTACK, CLOUD_AWS, CLOUD_VCA, CLOUD_APIC, CLOUD_MESOS, CLOUD_LINUXSERVER, CLOUD_DOCKER_UCP,  CLOUD_RANCHER, CLOUD_OSHIFT_K8S, CLOUD_AZURE, CLOUD_GCP.  Default value when not specified in API or module is interpreted by Avi Controller as CLOUD_NONE. |

## [Notes](avi_cloud_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Avi Network devices see <https://www.ansible.com/ansible-avi-networks>.

## [Examples](avi_cloud_module.md#id5)

```yaml+jinja
- name: Create a VMware cloud with write access mode
  community.network.avi_cloud:
    username: '{{ username }}'
    controller: '{{ controller }}'
    password: '{{ password }}'
    apic_mode: false
    dhcp_enabled: true
    enable_vip_static_routes: false
    license_type: LIC_CORES
    mtu: 1500
    name: vCenter Cloud
    prefer_static_routes: false
    tenant_ref: admin
    vcenter_configuration:
      datacenter_ref: /api/vimgrdcruntime/datacenter-2-10.10.20.100
      management_network: /api/vimgrnwruntime/dvportgroup-103-10.10.20.100
      password: password
      privilege: WRITE_ACCESS
      username: user
      vcenter_url: 10.10.20.100
    vtype: CLOUD_VCENTER
```

## [Return Values](avi_cloud_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **obj**  dictionary | Cloud (api/cloud) object  Returned: success, changed |

### Authors

- Gaurav Rastogi (@grastogi23)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
