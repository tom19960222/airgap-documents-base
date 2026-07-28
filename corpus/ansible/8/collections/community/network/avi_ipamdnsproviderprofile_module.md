---
collection: ansible
version: "8"
title: "community.network.avi_ipamdnsproviderprofile module – Module for setup of IpamDnsProviderProfile Avi RESTful Object"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/avi_ipamdnsproviderprofile_module.html
fetched_at: 2026-07-28T01:54:44+00:00
---
# community.network.avi_ipamdnsproviderprofile module – Module for setup of IpamDnsProviderProfile Avi RESTful Object

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
> see [Requirements](avi_ipamdnsproviderprofile_module.md#ansible-collections-community-network-avi-ipamdnsproviderprofile-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.avi_ipamdnsproviderprofile`.

- [Synopsis](avi_ipamdnsproviderprofile_module.md#synopsis)
- [Requirements](avi_ipamdnsproviderprofile_module.md#requirements)
- [Parameters](avi_ipamdnsproviderprofile_module.md#parameters)
- [Notes](avi_ipamdnsproviderprofile_module.md#notes)
- [Examples](avi_ipamdnsproviderprofile_module.md#examples)
- [Return Values](avi_ipamdnsproviderprofile_module.md#return-values)

## [Synopsis](avi_ipamdnsproviderprofile_module.md#id1)

- This module is used to configure IpamDnsProviderProfile object
- more examples at <https://github.com/avinetworks/devops>

Aliases: network.avi.avi_ipamdnsproviderprofile

## [Requirements](avi_ipamdnsproviderprofile_module.md#id2)

The below requirements are needed on the host that executes this module.

- avisdk

## [Parameters](avi_ipamdnsproviderprofile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allocate_ip_in_vrf**  boolean | If this flag is set, only allocate ip from networks in the virtual service vrf.  Applicable for avi vantage ipam only.  Field introduced in 17.2.4.  Default value when not specified in API or module is interpreted by Avi Controller as False.  **Choices:**   - `false` - `true` |
| **api_context**  dictionary | Avi API context that includes current session ID and CSRF Token.  This allows user to perform single login and re-use the session. |
| **api_version**  string | Avi API version of to use for Avi API and objects.  **Default:** `"16.4.4"` |
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
| **aws_profile**  string | Provider details if type is aws. |
| **azure_profile**  string | Provider details if type is microsoft azure.  Field introduced in 17.2.1. |
| **controller**  string | IP address or hostname of the controller. The default value is the environment variable `AVI_CONTROLLER`. |
| **custom_profile**  string | Provider details if type is custom.  Field introduced in 17.1.1. |
| **gcp_profile**  string | Provider details if type is google cloud. |
| **infoblox_profile**  string | Provider details if type is infoblox. |
| **internal_profile**  string | Provider details if type is avi. |
| **name**  string / required | Name for the ipam/dns provider profile. |
| **oci_profile**  string | Provider details for oracle cloud.  Field introduced in 18.2.1,18.1.3. |
| **openstack_profile**  string | Provider details if type is openstack. |
| **password**  string | Password of Avi user in Avi controller. The default value is the environment variable `AVI_PASSWORD`. |
| **proxy_configuration**  string | Field introduced in 17.1.1. |
| **state**  string | The state that should be applied on the entity.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **tenant**  string | Name of tenant used for all Avi API calls and context of object.  **Default:** `"admin"` |
| **tenant_ref**  string | It is a reference to an object of type tenant. |
| **tenant_uuid**  string | UUID of tenant used for all Avi API calls and context of object.  **Default:** `""` |
| **tencent_profile**  string | Provider details for tencent cloud.  Field introduced in 18.2.3. |
| **type**  string / required | Provider type for the ipam/dns provider profile.  Enum options - IPAMDNS_TYPE_INFOBLOX, IPAMDNS_TYPE_AWS, IPAMDNS_TYPE_OPENSTACK, IPAMDNS_TYPE_GCP, IPAMDNS_TYPE_INFOBLOX_DNS, IPAMDNS_TYPE_CUSTOM,  IPAMDNS_TYPE_CUSTOM_DNS, IPAMDNS_TYPE_AZURE, IPAMDNS_TYPE_OCI, IPAMDNS_TYPE_TENCENT, IPAMDNS_TYPE_INTERNAL, IPAMDNS_TYPE_INTERNAL_DNS,  IPAMDNS_TYPE_AWS_DNS, IPAMDNS_TYPE_AZURE_DNS. |
| **url**  string | Avi controller URL of the object. |
| **username**  string | Username used for accessing Avi controller. The default value is the environment variable `AVI_USERNAME`. |
| **uuid**  string | Uuid of the ipam/dns provider profile. |

## [Notes](avi_ipamdnsproviderprofile_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Avi Network devices see <https://www.ansible.com/ansible-avi-networks>.

## [Examples](avi_ipamdnsproviderprofile_module.md#id5)

```yaml+jinja
- name: Create IPAM DNS provider setting
  community.network.avi_ipamdnsproviderprofile:
    controller: '{{ controller }}'
    username: '{{ username }}'
    password: '{{ password }}'
    internal_profile:
      dns_service_domain:
      - domain_name: ashish.local
        num_dns_ip: 1
        pass_through: true
        record_ttl: 100
      - domain_name: guru.local
        num_dns_ip: 1
        pass_through: true
        record_ttl: 200
      ttl: 300
    name: Ashish-DNS
    tenant_ref: Demo
    type: IPAMDNS_TYPE_INTERNAL
```

## [Return Values](avi_ipamdnsproviderprofile_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **obj**  dictionary | IpamDnsProviderProfile (api/ipamdnsproviderprofile) object  **Returned:** success, changed |

### Authors

- Gaurav Rastogi (@grastogi23)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
