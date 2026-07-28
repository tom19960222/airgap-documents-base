---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_system_admin_profile module – Admin profile."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_system_admin_profile_module.html
fetched_at: 2026-07-28T02:17:55+00:00
---
# fortinet.fortimanager.fmgr_system_admin_profile module – Admin profile.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_admin_profile`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_system_admin_profile_module.md#synopsis)
- [Parameters](fmgr_system_admin_profile_module.md#parameters)
- [Notes](fmgr_system_admin_profile_module.md#notes)
- [Examples](fmgr_system_admin_profile_module.md#examples)
- [Return Values](fmgr_system_admin_profile_module.md#return-values)

## [Synopsis](fmgr_system_admin_profile_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_admin_profile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **system_admin_profile**  dictionary | the top level parameters set |
| **adom-lock**  string | ADOM locking  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **adom-policy-packages**  string | ADOM policy packages.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **adom-switch**  string | Administrator domain.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **allow-to-install**  string | Enable/disable the restricted user to install objects to the devices.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **app-filter**  string | App filter.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **assignment**  string | Assignment permission.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **change-password**  string | Enable/disable restricted user to change self password.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **config-retrieve**  string | Configuration retrieve.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **config-revert**  string | Revert Configuration from Revision History  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **consistency-check**  string | Consistency check.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **datamask**  string | Enable/disable data masking.  disable - Disable data masking.  enable - Enable data masking.  **Choices:**   - `"disable"` - `"enable"` |
| **datamask-custom-fields**  list / elements=dictionary | Datamask-Custom-Fields. |
| **field-category**  list / elements=string | Field categories.  log - Log.  fortiview - FortiView.  alert - Event management.  ueba - UEBA.  all - All.  **Choices:**   - `"log"` - `"fortiview"` - `"alert"` - `"ueba"` - `"all"` |
| **field-name**  string | Field name. |
| **field-status**  string | Field status.  disable - Disable field.  enable - Enable field.  **Choices:**   - `"disable"` - `"enable"` |
| **field-type**  string | Field type.  string - String.  ip - IP.  mac - MAC address.  email - Email address.  unknown - Unknown.  **Choices:**   - `"string"` - `"ip"` - `"mac"` - `"email"` - `"unknown"` |
| **datamask-custom-priority**  string | Prioritize custom fields.  disable - Disable custom field search priority.  enable - Enable custom field search priority.  **Choices:**   - `"disable"` - `"enable"` |
| **datamask-fields**  list / elements=string | Data masking fields.  user - User name.  srcip - Source IP.  srcname - Source name.  srcmac - Source MAC.  dstip - Destination IP.  dstname - Dst name.  email - Email.  message - Message.  domain - Domain.  **Choices:**   - `"user"` - `"srcip"` - `"srcname"` - `"srcmac"` - `"dstip"` - `"dstname"` - `"email"` - `"message"` - `"domain"` |
| **datamask-key**  any | (list) Data masking encryption key. |
| **datamask-unmasked-time**  integer | Time in days without data masking. |
| **deploy-management**  string | Install to devices.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **description**  string | Description. |
| **device-ap**  string | Manage AP.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **device-config**  string | Manage device configurations.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **device-forticlient**  string | Manage FortiClient.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **device-fortiextender**  string | Manage FortiExtender.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **device-fortiswitch**  string | Manage FortiSwitch.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **device-manager**  string | Device manager.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **device-op**  string | Device add/delete/edit.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **device-policy-package-lock**  string | Device/Policy Package locking  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **device-profile**  string | Device profile permission.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **device-revision-deletion**  string | Delete device revision.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **device-wan-link-load-balance**  string | Manage WAN link load balance.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **event-management**  string | Event management.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **extension-access**  string | Manage extension access.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **fabric-viewer**  string | Fabric viewer.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **fgd-center-advanced**  string | FortiGuard Center Advanced.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **fgd-center-fmw-mgmt**  string | FortiGuard Center Firmware Management.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **fgd-center-licensing**  string | FortiGuard Center Licensing.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **fgd_center**  string | FortiGuard Center.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **global-policy-packages**  string | Global policy packages.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **import-policy-packages**  string | Import Policy Package.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **intf-mapping**  string | Interface Mapping  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **ips-baseline-cfg**  string | Ips baseline sensor configration.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **ips-baseline-ovrd**  string | Enable/disable override baseline ips sensor.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **ips-filter**  string | IPS filter.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **ips-lock**  string | IPS locking  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **ips-objects**  string | Ips objects configuration.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **ipv6_trusthost1**  string | Admin user trusted host IPv6, default |
| **ipv6_trusthost10**  string | Admin user trusted host IPv6, default ffff |
| **ipv6_trusthost2**  string | Admin user trusted host IPv6, default ffff |
| **ipv6_trusthost3**  string | Admin user trusted host IPv6, default ffff |
| **ipv6_trusthost4**  string | Admin user trusted host IPv6, default ffff |
| **ipv6_trusthost5**  string | Admin user trusted host IPv6, default ffff |
| **ipv6_trusthost6**  string | Admin user trusted host IPv6, default ffff |
| **ipv6_trusthost7**  string | Admin user trusted host IPv6, default ffff |
| **ipv6_trusthost8**  string | Admin user trusted host IPv6, default ffff |
| **ipv6_trusthost9**  string | Admin user trusted host IPv6, default ffff |
| **log-viewer**  string | Log viewer.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **policy-objects**  string | Policy objects permission.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **profileid**  string / required | Profile ID. |
| **read-passwd**  string | View password in clear text.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **realtime-monitor**  string | Realtime monitor.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **report-viewer**  string | Report viewer.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **rpc-permit**  string | Set none/read/read-write rpc-permission  read-write - Read-write permission.  none - No permission.  read - Read-only permission.  **Choices:**   - `"read-write"` - `"none"` - `"read"` |
| **run-report**  string | Run reports.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **scope**  string | Scope.  global - Global scope.  adom - ADOM scope.  **Choices:**   - `"global"` - `"adom"` |
| **script-access**  string | Script access.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **set-install-targets**  string | Edit installation targets.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **super-user-profile**  string | Enable/disable super user profile  disable - Disable super user profile  enable - Enable super user profile  **Choices:**   - `"disable"` - `"enable"` |
| **system-setting**  string | System setting.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **term-access**  string | Terminal access.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **triage-events**  string | Triage events.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **trusthost1**  string | Admin user trusted host IP, default 0. |
| **trusthost10**  string | Admin user trusted host IP, default 255. |
| **trusthost2**  string | Admin user trusted host IP, default 255. |
| **trusthost3**  string | Admin user trusted host IP, default 255. |
| **trusthost4**  string | Admin user trusted host IP, default 255. |
| **trusthost5**  string | Admin user trusted host IP, default 255. |
| **trusthost6**  string | Admin user trusted host IP, default 255. |
| **trusthost7**  string | Admin user trusted host IP, default 255. |
| **trusthost8**  string | Admin user trusted host IP, default 255. |
| **trusthost9**  string | Admin user trusted host IP, default 255. |
| **type**  string | profile type.  system - System admin.  restricted - Restricted admin.  **Choices:**   - `"system"` - `"restricted"` |
| **update-incidents**  string | Create/update incidents.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **vpn-manager**  string | VPN manager.  none - No permission.  read - Read permission.  read-write - Read-write permission.  **Choices:**   - `"none"` - `"read"` - `"read-write"` |
| **web-filter**  string | Web filter.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_system_admin_profile_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_admin_profile_module.md#id4)

```yaml+jinja
- name: gathering fortimanager facts
  hosts: fortimanager00
  gather_facts: no
  connection: httpapi
  collections:
    - fortinet.fortimanager
  vars:
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_port: 443
  tasks:
   - name: retrieve all the admin profiles
     fmgr_fact:
       facts:
           selector: 'system_admin_profile'
           params:
               profile: 'your_value'
- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Admin profile.
     fmgr_system_admin_profile:
        bypass_validation: False
        state: present
        system_admin_profile:
           description: ansible-test-description
           profileid: ansible-test-profile
           scope: adom #<value in [global, adom]>
           type: system #<value in [system, restricted]>
```

## [Return Values](fmgr_system_admin_profile_module.md#id5)

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
