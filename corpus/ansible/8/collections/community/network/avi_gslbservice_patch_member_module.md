---
collection: ansible
version: "8"
title: "community.network.avi_gslbservice_patch_member module – Avi API Module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/avi_gslbservice_patch_member_module.html
fetched_at: 2026-07-28T01:54:41+00:00
---
# community.network.avi_gslbservice_patch_member module – Avi API Module

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
> see [Requirements](avi_gslbservice_patch_member_module.md#ansible-collections-community-network-avi-gslbservice-patch-member-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.avi_gslbservice_patch_member`.

- [Synopsis](avi_gslbservice_patch_member_module.md#synopsis)
- [Requirements](avi_gslbservice_patch_member_module.md#requirements)
- [Parameters](avi_gslbservice_patch_member_module.md#parameters)
- [Notes](avi_gslbservice_patch_member_module.md#notes)
- [Examples](avi_gslbservice_patch_member_module.md#examples)
- [Return Values](avi_gslbservice_patch_member_module.md#return-values)

## [Synopsis](avi_gslbservice_patch_member_module.md#id1)

- This module can be used for calling any resources defined in Avi REST API. <https://avinetworks.com/>
- This module is useful for invoking HTTP Patch methods and accessing resources that do not have an REST object associated with them.

Aliases: network.avi.avi_gslbservice_patch_member

## [Requirements](avi_gslbservice_patch_member_module.md#id2)

The below requirements are needed on the host that executes this module.

- avisdk

## [Parameters](avi_gslbservice_patch_member_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_context**  dictionary | Avi API context that includes current session ID and CSRF Token.  This allows user to perform single login and re-use the session. |
| **api_version**  string | Avi API version of to use for Avi API and objects.  **Default:** `"16.4.4"` |
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
| **data**  string | HTTP body of GSLB Service Member in YAML or JSON format. |
| **name**  string / required | Name of the GSLB Service |
| **params**  string | Query parameters passed to the HTTP API. |
| **password**  string | Password of Avi user in Avi controller. The default value is the environment variable `AVI_PASSWORD`. |
| **state**  string | The state that should be applied to the member. Member is  identified using field member.ip.addr.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **tenant**  string | Name of tenant used for all Avi API calls and context of object.  **Default:** `"admin"` |
| **tenant_uuid**  string | UUID of tenant used for all Avi API calls and context of object.  **Default:** `""` |
| **username**  string | Username used for accessing Avi controller. The default value is the environment variable `AVI_USERNAME`. |

## [Notes](avi_gslbservice_patch_member_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage Avi Network devices see <https://www.ansible.com/ansible-avi-networks>.

## [Examples](avi_gslbservice_patch_member_module.md#id5)

```yaml+jinja
- name: Patch GSLB Service to add a new member and group
  community.network.avi_gslbservice_patch_member:
    controller: "{{ controller }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: gs-3
    api_version: 17.2.1
    data:
      group:
        name: newfoo
        priority: 60
        members:
          - enabled: true
            ip:
              addr:  10.30.10.66
              type: V4
            ratio: 3
- name: Patch GSLB Service to delete an existing member
  community.network.avi_gslbservice_patch_member:
    controller: "{{ controller }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: gs-3
    state: absent
    api_version: 17.2.1
    data:
      group:
        name: newfoo
        members:
          - enabled: true
            ip:
              addr:  10.30.10.68
              type: V4
            ratio: 3
- name: Update priority of GSLB Service Pool
  community.network.avi_gslbservice_patch_member:
    controller: ""
    username: ""
    password: ""
    name: gs-3
    state: present
    api_version: 17.2.1
    data:
      group:
        name: newfoo
        priority: 42
```

## [Return Values](avi_gslbservice_patch_member_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **obj**  dictionary | Avi REST resource  **Returned:** success, changed |

### Authors

- Gaurav Rastogi (@grastogi23)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
