---
collection: ansible
version: "6"
title: "community.network.avi_systemconfiguration module – Module for setup of SystemConfiguration Avi RESTful Object"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/avi_systemconfiguration_module.html
fetched_at: 2026-07-27T17:17:03+00:00
---
# community.network.avi_systemconfiguration module – Module for setup of SystemConfiguration Avi RESTful Object

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
> see [Requirements](avi_systemconfiguration_module.md#ansible-collections-community-network-avi-systemconfiguration-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.avi_systemconfiguration`.

- [Synopsis](avi_systemconfiguration_module.md#synopsis)
- [Requirements](avi_systemconfiguration_module.md#requirements)
- [Parameters](avi_systemconfiguration_module.md#parameters)
- [Notes](avi_systemconfiguration_module.md#notes)
- [Examples](avi_systemconfiguration_module.md#examples)
- [Return Values](avi_systemconfiguration_module.md#return-values)

## [Synopsis](avi_systemconfiguration_module.md#id1)

- This module is used to configure SystemConfiguration object
- more examples at <https://github.com/avinetworks/devops>

## [Requirements](avi_systemconfiguration_module.md#id2)

The below requirements are needed on the host that executes this module.

- avisdk

## [Parameters](avi_systemconfiguration_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **admin_auth_configuration**  string | Adminauthconfiguration settings for systemconfiguration. |
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
| **default_license_tier**  string | Specifies the default license tier which would be used by new clouds.  Enum options - ENTERPRISE_16, ENTERPRISE_18.  Field introduced in 17.2.5.  Default value when not specified in API or module is interpreted by Avi Controller as ENTERPRISE_18. |
| **dns_configuration**  string | Dnsconfiguration settings for systemconfiguration. |
| **dns_virtualservice_refs**  string | Dns virtualservices hosting fqdn records for applications across avi vantage.  If no virtualservices are provided, avi vantage will provide dns services for configured applications.  Switching back to avi vantage from dns virtualservices is not allowed.  It is a reference to an object of type virtualservice. |
| **docker_mode**  boolean | Boolean flag to set docker_mode.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |
| **email_configuration**  string | Emailconfiguration settings for systemconfiguration. |
| **global_tenant_config**  string | Tenantconfiguration settings for systemconfiguration. |
| **linux_configuration**  string | Linuxconfiguration settings for systemconfiguration. |
| **mgmt_ip_access_control**  string | Configure ip access control for controller to restrict open access. |
| **ntp_configuration**  string | Ntpconfiguration settings for systemconfiguration. |
| **password**  string | Password of Avi user in Avi controller. The default value is the environment variable `AVI_PASSWORD`. |
| **portal_configuration**  string | Portalconfiguration settings for systemconfiguration. |
| **proxy_configuration**  string | Proxyconfiguration settings for systemconfiguration. |
| **secure_channel_configuration**  string | Configure secure channel properties.  Field introduced in 18.1.4, 18.2.1. |
| **snmp_configuration**  string | Snmpconfiguration settings for systemconfiguration. |
| **ssh_ciphers**  string | Allowed ciphers list for ssh to the management interface on the controller and service engines.  If this is not specified, all the default ciphers are allowed. |
| **ssh_hmacs**  string | Allowed hmac list for ssh to the management interface on the controller and service engines.  If this is not specified, all the default hmacs are allowed. |
| **state**  string | The state that should be applied on the entity.  Choices:   - `"absent"` - `"present"` ← (default) |
| **tenant**  string | Name of tenant used for all Avi API calls and context of object.  Default: `"admin"` |
| **tenant_uuid**  string | UUID of tenant used for all Avi API calls and context of object.  Default: `""` |
| **url**  string | Avi controller URL of the object. |
| **username**  string | Username used for accessing Avi controller. The default value is the environment variable `AVI_USERNAME`. |
| **uuid**  string | Unique object identifier of the object. |
| **welcome_workflow_complete**  boolean | This flag is set once the initial controller setup workflow is complete.  Field introduced in 18.2.3.  Default value when not specified in API or module is interpreted by Avi Controller as False.  Choices:   - `false` - `true` |

## [Notes](avi_systemconfiguration_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Avi Network devices see <https://www.ansible.com/ansible-avi-networks>.

## [Examples](avi_systemconfiguration_module.md#id5)

```yaml+jinja
- name: Example to create SystemConfiguration object
  community.network.avi_systemconfiguration:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_systemconfiguration
```

## [Return Values](avi_systemconfiguration_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **obj**  dictionary | SystemConfiguration (api/systemconfiguration) object  Returned: success, changed |

### Authors

- Gaurav Rastogi (@grastogi23)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
