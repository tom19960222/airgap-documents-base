---
collection: ansible
version: "8"
title: "cisco.ucs.ucs_storage_profile module – Configures storage profiles on Cisco UCS Manager"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ucs/ucs_storage_profile_module.html
fetched_at: 2026-07-28T01:39:43+00:00
---
# cisco.ucs.ucs_storage_profile module – Configures storage profiles on Cisco UCS Manager

> **Note:**
>
> This module is part of the [cisco.ucs collection](https://galaxy.ansible.com/ui/repo/published/cisco/ucs/) (version 1.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ucs`.
> You need further requirements to be able to use this module,
> see [Requirements](ucs_storage_profile_module.md#ansible-collections-cisco-ucs-ucs-storage-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ucs.ucs_storage_profile`.

New in cisco.ucs 2.7

- [Synopsis](ucs_storage_profile_module.md#synopsis)
- [Requirements](ucs_storage_profile_module.md#requirements)
- [Parameters](ucs_storage_profile_module.md#parameters)
- [Examples](ucs_storage_profile_module.md#examples)

## [Synopsis](ucs_storage_profile_module.md#id1)

- Configures storage profiles on Cisco UCS Manager.

## [Requirements](ucs_storage_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ucsmsdk

## [Parameters](ucs_storage_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  aliases: descr  string | The user-defined description of the storage profile.  Enter up to 256 characters.  You can use any characters or spaces except the following:  ` (accent mark), (backslash), ^ (carat), ” (double quote), = (equal sign), > (greater than), < (less than), or ‘ (single quote). |
| **hostname**  string / required | IP address or hostname of Cisco UCS Manager.  Modules can be used with the UCS Platform Emulator <https://cs.co/ucspe> |
| **local_luns**  string | List of Local LUNs used by the storage profile. |
| **auto_deploy**  string | Whether the local LUN should be automatically deployed or not.  **Choices:**   - `"auto-deploy"` ← (default) - `"no-auto-deploy"` |
| **disk_policy_name**  string | The disk group configuration policy to be applied to this local LUN. |
| **expand_to_avail**  boolean | Specifies that this LUN can be expanded to use the entire available disk group.  For each service profile, only one LUN can use this option.  Expand To Available option is not supported for already deployed LUN.  **Choices:**   - `false` ← (default) - `true` |
| **fractional_size**  string | Fractional size of this LUN in MB.  **Default:** `"0"` |
| **name**  string / required | The name of the local LUN. |
| **size**  string | Size of this LUN in GB.  The size can range from 1 to 10240 GB.  **Default:** `"1"` |
| **state**  string | If `present`, will verify local LUN is present on profile. If `absent`, will verify local LUN is absent on profile.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **name**  string / required | The name of the storage profile.  This name can be between 1 and 16 alphanumeric characters.  You cannot use spaces or any special characters other than - (hyphen), “_” (underscore), : (colon), and . (period).  You cannot change this name after profile is created. |
| **org_dn**  string | The distinguished name (dn) of the organization where the resource is assigned.  **Default:** `"org-root"` |
| **password**  string / required | Password for Cisco UCS Manager authentication. |
| **port**  integer | Port number to be used during connection (by default uses 443 for https and 80 for http connection). |
| **proxy**  string | If use_proxy is no, specfies proxy to be used for connection. e.g. ‘<http://proxy.xy.z:8080>’ |
| **state**  string | If `present`, will verify that the storage profile is present and will create if needed.  If `absent`, will verify that the storage profile is absent and will delete if needed.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **use_proxy**  boolean | If `no`, will not use the proxy as defined by system environment variable.  **Choices:**   - `false` - `true` ← (default) |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  **Choices:**   - `false` - `true` ← (default) |
| **username**  string | Username for Cisco UCS Manager authentication.  **Default:** `"admin"` |

## [Examples](ucs_storage_profile_module.md#id4)

```yaml+jinja
- name: Configure Storage Profile
  cisco.ucs.ucs_storage_profile:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: DEE-StgProf
    local_luns:
    - name: Boot-LUN
      size: '60'
      disk_policy_name: DEE-DG
    - name: Data-LUN
      size: '200'
      disk_policy_name: DEE-DG

- name: Remove Storage Profile
  cisco.ucs.ucs_storage_profile:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: DEE-StgProf
    state: absent

- name: Remove Local LUN from Storage Profile
  cisco.ucs.ucs_storage_profile:
    hostname: 172.16.143.150
    username: admin
    password: password
    name: DEE-StgProf
    local_luns:
    - name: Data-LUN
      state: absent
```

### Authors

- Sindhu Sudhir (@sisudhir)
- David Soper (@dsoper2)
- John McDonough (@movinalot)
- CiscoUcs (@CiscoUcs)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-ucs)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-ucs)
