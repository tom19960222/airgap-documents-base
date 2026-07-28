---
collection: ansible
version: "6"
title: "cisco.ucs.ucs_service_profile_from_template module – Configures Service Profiles from templates on Cisco UCS Manager"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ucs/ucs_service_profile_from_template_module.html
fetched_at: 2026-07-27T17:02:53+00:00
---
# cisco.ucs.ucs_service_profile_from_template module – Configures Service Profiles from templates on Cisco UCS Manager

> **Note:**
>
> This module is part of the [cisco.ucs collection](https://galaxy.ansible.com/cisco/ucs) (version 1.8.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ucs`.
> You need further requirements to be able to use this module,
> see [Requirements](ucs_service_profile_from_template_module.md#ansible-collections-cisco-ucs-ucs-service-profile-from-template-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ucs.ucs_service_profile_from_template`.

New in cisco.ucs 2.5

- [Synopsis](ucs_service_profile_from_template_module.md#synopsis)
- [Requirements](ucs_service_profile_from_template_module.md#requirements)
- [Parameters](ucs_service_profile_from_template_module.md#parameters)
- [Examples](ucs_service_profile_from_template_module.md#examples)

## [Synopsis](ucs_service_profile_from_template_module.md#id1)

- Configures Service Profile created from templates on Cisco UCS Manager.

## [Requirements](ucs_service_profile_from_template_module.md#id2)

The below requirements are needed on the host that executes this module.

- ucsmsdk

## [Parameters](ucs_service_profile_from_template_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string | Optional  The Description of the service profile |
| **hostname**  string / required | IP address or hostname of Cisco UCS Manager.  Modules can be used with the UCS Platform Emulator <https://cs.co/ucspe> |
| **name**  string / required | The name of the service profile.  This name can be between 2 and 32 alphanumeric characters.  You cannot use spaces or any special characters other than - (hyphen), “_” (underscore), : (colon), and . (period).  This name must be unique across all service profiles and service profile templates within the same organization. |
| **org_dn**  string | Org dn (distinguished name)  Default: `"org-root"` |
| **password**  string / required | Password for Cisco UCS Manager authentication. |
| **port**  integer | Port number to be used during connection (by default uses 443 for https and 80 for http connection). |
| **power_state**  string | The power state to be applied when this service profile is associated with a server.  If no value is provided, the power_state for the service profile will not be modified.  Choices:   - `"up"` - `"down"` |
| **proxy**  string | If use_proxy is no, specfies proxy to be used for connection. e.g. ‘<http://proxy.xy.z:8080>’ |
| **source_template**  string / required | The name of the service profile template used to create this serivce profile. |
| **state**  string | If `present`, will verify Service Profiles are present and will create if needed.  If `absent`, will verify Service Profiles are absent and will delete if needed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **use_proxy**  boolean | If `no`, will not use the proxy as defined by system environment variable.  Choices:   - `false` - `true` ← (default) |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  Choices:   - `false` - `true` ← (default) |
| **user_label**  string | The User Label you want to assign to this service profile. |
| **username**  string | Username for Cisco UCS Manager authentication.  Default: `"admin"` |

## [Examples](ucs_service_profile_from_template_module.md#id4)

```yaml+jinja
- name: Configure Service Profile from Template
  cisco.ucs.ucs_service_profile_from_template:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: test-sp-instance1
    source_template: test-sp
    discription: Created from Ansible

- name: Remove Service Profile
  cisco.ucs.ucs_service_profile_from_template:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: test-sp-instance1
    state: absent
```

### Authors

- David Soper (@dsoper2)
- CiscoUcs (@CiscoUcs)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-ucs)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-ucs)
