---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_system_npu_npqueues_profile module – Configure a NP7 class profile."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_system_npu_npqueues_profile_module.html
fetched_at: 2026-07-28T02:19:27+00:00
---
# fortinet.fortimanager.fmgr_system_npu_npqueues_profile module – Configure a NP7 class profile.

> **Note:**
>
> This module is part of the [fortinet.fortimanager collection](https://galaxy.ansible.com/ui/repo/published/fortinet/fortimanager/) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortimanager`.
>
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_npu_npqueues_profile`.

New in fortinet.fortimanager 2.2.0

- [Synopsis](fmgr_system_npu_npqueues_profile_module.md#synopsis)
- [Parameters](fmgr_system_npu_npqueues_profile_module.md#parameters)
- [Notes](fmgr_system_npu_npqueues_profile_module.md#notes)
- [Examples](fmgr_system_npu_npqueues_profile_module.md#examples)
- [Return Values](fmgr_system_npu_npqueues_profile_module.md#return-values)

## [Synopsis](fmgr_system_npu_npqueues_profile_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_npu_npqueues_profile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **system_npu_npqueues_profile**  dictionary | the top level parameters set |
| **cos0**  string | Queue number of CoS 0.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **cos1**  string | Queue number of CoS 1.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **cos2**  string | Queue number of CoS 2.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **cos3**  string | Queue number of CoS 3.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **cos4**  string | Queue number of CoS 4.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **cos5**  string | Queue number of CoS 5.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **cos6**  string | Queue number of CoS 6.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **cos7**  string | Queue number of CoS 7.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp0**  string | Queue number of DSCP 0.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp1**  string | Queue number of DSCP 1.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp10**  string | Queue number of DSCP 10.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp11**  string | Queue number of DSCP 11.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp12**  string | Queue number of DSCP 12.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp13**  string | Queue number of DSCP 13.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp14**  string | Queue number of DSCP 14.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp15**  string | Queue number of DSCP 15.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp16**  string | Queue number of DSCP 16.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp17**  string | Queue number of DSCP 17.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp18**  string | Queue number of DSCP 18.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp19**  string | Queue number of DSCP 19.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp2**  string | Queue number of DSCP 2.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp20**  string | Queue number of DSCP 20.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp21**  string | Queue number of DSCP 21.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp22**  string | Queue number of DSCP 22.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp23**  string | Queue number of DSCP 23.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp24**  string | Queue number of DSCP 24.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp25**  string | Queue number of DSCP 25.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp26**  string | Queue number of DSCP 26.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp27**  string | Queue number of DSCP 27.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp28**  string | Queue number of DSCP 28.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp29**  string | Queue number of DSCP 29.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp3**  string | Queue number of DSCP 3.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp30**  string | Queue number of DSCP 30.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp31**  string | Queue number of DSCP 31.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp32**  string | Queue number of DSCP 32.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp33**  string | Queue number of DSCP 33.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp34**  string | Queue number of DSCP 34.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp35**  string | Queue number of DSCP 35.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp36**  string | Queue number of DSCP 36.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp37**  string | Queue number of DSCP 37.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp38**  string | Queue number of DSCP 38.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp39**  string | Queue number of DSCP 39.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp4**  string | Queue number of DSCP 4.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp40**  string | Queue number of DSCP 40.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp41**  string | Queue number of DSCP 41.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp42**  string | Queue number of DSCP 42.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp43**  string | Queue number of DSCP 43.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp44**  string | Queue number of DSCP 44.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp45**  string | Queue number of DSCP 45.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp46**  string | Queue number of DSCP 46.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp47**  string | Queue number of DSCP 47.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp48**  string | Queue number of DSCP 48.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp49**  string | Queue number of DSCP 49.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp5**  string | Queue number of DSCP 5.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp50**  string | Queue number of DSCP 50.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp51**  string | Queue number of DSCP 51.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp52**  string | Queue number of DSCP 52.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp53**  string | Queue number of DSCP 53.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp54**  string | Queue number of DSCP 54.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp55**  string | Queue number of DSCP 55.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp56**  string | Queue number of DSCP 56.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp57**  string | Queue number of DSCP 57.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp58**  string | Queue number of DSCP 58.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp59**  string | Queue number of DSCP 59.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp6**  string | Queue number of DSCP 6.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp60**  string | Queue number of DSCP 60.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp61**  string | Queue number of DSCP 61.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp62**  string | Queue number of DSCP 62.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp63**  string | Queue number of DSCP 63.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp7**  string | Queue number of DSCP 7.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp8**  string | Queue number of DSCP 8.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp9**  string | Queue number of DSCP 9.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **id**  integer / required | Profile ID. |
| **type**  string | Profile type.  **Choices:**   - `"cos"` - `"dscp"` |
| **weight**  integer | Class weight. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_system_npu_npqueues_profile_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_npu_npqueues_profile_module.md#id4)

```yaml+jinja
- hosts: fortimanager-inventory
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_port: 443
  tasks:
    - name: Configure a NP7 class profile.
      fmgr_system_npu_npqueues_profile:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        system_npu_npqueues_profile:
          cos0: <value in [queue0, queue1, queue2, ...]>
          cos1: <value in [queue0, queue1, queue2, ...]>
          cos2: <value in [queue0, queue1, queue2, ...]>
          cos3: <value in [queue0, queue1, queue2, ...]>
          cos4: <value in [queue0, queue1, queue2, ...]>
          cos5: <value in [queue0, queue1, queue2, ...]>
          cos6: <value in [queue0, queue1, queue2, ...]>
          cos7: <value in [queue0, queue1, queue2, ...]>
          dscp0: <value in [queue0, queue1, queue2, ...]>
          dscp1: <value in [queue0, queue1, queue2, ...]>
          dscp10: <value in [queue0, queue1, queue2, ...]>
          dscp11: <value in [queue0, queue1, queue2, ...]>
          dscp12: <value in [queue0, queue1, queue2, ...]>
          dscp13: <value in [queue0, queue1, queue2, ...]>
          dscp14: <value in [queue0, queue1, queue2, ...]>
          dscp15: <value in [queue0, queue1, queue2, ...]>
          dscp16: <value in [queue0, queue1, queue2, ...]>
          dscp17: <value in [queue0, queue1, queue2, ...]>
          dscp18: <value in [queue0, queue1, queue2, ...]>
          dscp19: <value in [queue0, queue1, queue2, ...]>
          dscp2: <value in [queue0, queue1, queue2, ...]>
          dscp20: <value in [queue0, queue1, queue2, ...]>
          dscp21: <value in [queue0, queue1, queue2, ...]>
          dscp22: <value in [queue0, queue1, queue2, ...]>
          dscp23: <value in [queue0, queue1, queue2, ...]>
          dscp24: <value in [queue0, queue1, queue2, ...]>
          dscp25: <value in [queue0, queue1, queue2, ...]>
          dscp26: <value in [queue0, queue1, queue2, ...]>
          dscp27: <value in [queue0, queue1, queue2, ...]>
          dscp28: <value in [queue0, queue1, queue2, ...]>
          dscp29: <value in [queue0, queue1, queue2, ...]>
          dscp3: <value in [queue0, queue1, queue2, ...]>
          dscp30: <value in [queue0, queue1, queue2, ...]>
          dscp31: <value in [queue0, queue1, queue2, ...]>
          dscp32: <value in [queue0, queue1, queue2, ...]>
          dscp33: <value in [queue0, queue1, queue2, ...]>
          dscp34: <value in [queue0, queue1, queue2, ...]>
          dscp35: <value in [queue0, queue1, queue2, ...]>
          dscp36: <value in [queue0, queue1, queue2, ...]>
          dscp37: <value in [queue0, queue1, queue2, ...]>
          dscp38: <value in [queue0, queue1, queue2, ...]>
          dscp39: <value in [queue0, queue1, queue2, ...]>
          dscp4: <value in [queue0, queue1, queue2, ...]>
          dscp40: <value in [queue0, queue1, queue2, ...]>
          dscp41: <value in [queue0, queue1, queue2, ...]>
          dscp42: <value in [queue0, queue1, queue2, ...]>
          dscp43: <value in [queue0, queue1, queue2, ...]>
          dscp44: <value in [queue0, queue1, queue2, ...]>
          dscp45: <value in [queue0, queue1, queue2, ...]>
          dscp46: <value in [queue0, queue1, queue2, ...]>
          dscp47: <value in [queue0, queue1, queue2, ...]>
          dscp48: <value in [queue0, queue1, queue2, ...]>
          dscp49: <value in [queue0, queue1, queue2, ...]>
          dscp5: <value in [queue0, queue1, queue2, ...]>
          dscp50: <value in [queue0, queue1, queue2, ...]>
          dscp51: <value in [queue0, queue1, queue2, ...]>
          dscp52: <value in [queue0, queue1, queue2, ...]>
          dscp53: <value in [queue0, queue1, queue2, ...]>
          dscp54: <value in [queue0, queue1, queue2, ...]>
          dscp55: <value in [queue0, queue1, queue2, ...]>
          dscp56: <value in [queue0, queue1, queue2, ...]>
          dscp57: <value in [queue0, queue1, queue2, ...]>
          dscp58: <value in [queue0, queue1, queue2, ...]>
          dscp59: <value in [queue0, queue1, queue2, ...]>
          dscp6: <value in [queue0, queue1, queue2, ...]>
          dscp60: <value in [queue0, queue1, queue2, ...]>
          dscp61: <value in [queue0, queue1, queue2, ...]>
          dscp62: <value in [queue0, queue1, queue2, ...]>
          dscp63: <value in [queue0, queue1, queue2, ...]>
          dscp7: <value in [queue0, queue1, queue2, ...]>
          dscp8: <value in [queue0, queue1, queue2, ...]>
          dscp9: <value in [queue0, queue1, queue2, ...]>
          id: <integer>
          type: <value in [cos, dscp]>
          weight: <integer>
```

## [Return Values](fmgr_system_npu_npqueues_profile_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meta**  dictionary | The result of the request.  **Returned:** always |
| **request_url**  string | The full url requested.  **Returned:** always  **Sample:** `"/sys/login/user"` |
| **response_code**  integer | The status of api request.  **Returned:** always  **Sample:** `0` |
| **response_data**  list / elements=string | The api response.  **Returned:** always |
| **response_message**  string | The descriptive message of the api response.  **Returned:** always  **Sample:** `"OK."` |
| **system_information**  dictionary | The information of the target system.  **Returned:** always |
| **rc**  integer | The status the request.  **Returned:** always  **Sample:** `0` |
| **version_check_warning**  list / elements=string | Warning if the parameters used in the playbook are not supported by the current FortiManager version.  **Returned:** complex |

### Authors

- Xinwei Du (@dux-fortinet)
- Xing Li (@lix-fortinet)
- Jie Xue (@JieX19)
- Link Zheng (@chillancezen)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/issues)
- [Homepage](https://fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection)
