---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_cloud_orchestawstemplate_autoscaletgwnewvpc module – no description"
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_cloud_orchestawstemplate_autoscaletgwnewvpc_module.html
fetched_at: 2026-07-28T02:08:37+00:00
---
# fortinet.fortimanager.fmgr_cloud_orchestawstemplate_autoscaletgwnewvpc module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_cloud_orchestawstemplate_autoscaletgwnewvpc`.

New in fortinet.fortimanager 2.2.0

- [Synopsis](fmgr_cloud_orchestawstemplate_autoscaletgwnewvpc_module.md#synopsis)
- [Parameters](fmgr_cloud_orchestawstemplate_autoscaletgwnewvpc_module.md#parameters)
- [Notes](fmgr_cloud_orchestawstemplate_autoscaletgwnewvpc_module.md#notes)
- [Examples](fmgr_cloud_orchestawstemplate_autoscaletgwnewvpc_module.md#examples)
- [Return Values](fmgr_cloud_orchestawstemplate_autoscaletgwnewvpc_module.md#return-values)

## [Synopsis](fmgr_cloud_orchestawstemplate_autoscaletgwnewvpc_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_cloud_orchestawstemplate_autoscaletgwnewvpc_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **cloud_orchestawstemplate_autoscaletgwnewvpc**  dictionary | the top level parameters set |
| **availability-zones**  string | no description |
| **bgp-asn**  integer | no description |
| **custom-asset-container**  string | no description |
| **custom-asset-directory**  string | no description |
| **custom-identifier**  string | no description |
| **faz-autoscale-admin-password**  any | (list) no description |
| **faz-autoscale-admin-username**  string | no description |
| **faz-custom-private-ipaddress**  string | no description |
| **faz-instance-type**  string | no description  **Choices:**   - `"h1.2xlarge"` - `"h1.4xlarge"` - `"h1.8xlarge"` - `"m5.large"` - `"m5.xlarge"` - `"m5.2xlarge"` - `"m5.4xlarge"` - `"m5.12xlarge"` - `"t2.medium"` - `"t2.large"` - `"t2.xlarge"` |
| **faz-integration-options**  string | no description  **Choices:**   - `"no"` - `"yes"` |
| **faz-version**  string | no description |
| **fgt-admin-cidr**  string | no description |
| **fgt-admin-port**  integer | no description |
| **fgt-instance-type**  string | no description  **Choices:**   - `"t2.small"` - `"c5.large"` - `"c5.xlarge"` - `"c5.2xlarge"` - `"c5.4xlarge"` - `"c5.9xlarge"` |
| **fgt-psk-secret**  string | no description |
| **fgtasg-cool-down**  integer | no description |
| **fgtasg-desired-capacity-byol**  integer | no description |
| **fgtasg-desired-capacity-payg**  integer | no description |
| **fgtasg-health-check-grace-period**  integer | no description |
| **fgtasg-max-size-byol**  integer | no description |
| **fgtasg-max-size-payg**  integer | no description |
| **fgtasg-min-size-byol**  integer | no description |
| **fgtasg-min-size-payg**  integer | no description |
| **fgtasg-scale-in-threshold**  integer | no description |
| **fgtasg-scale-out-threshold**  integer | no description |
| **fos-version**  string | no description |
| **get-license-grace-period**  integer | no description |
| **heartbeat-delay-allowance**  integer | no description |
| **heartbeat-interval**  integer | no description |
| **heartbeat-loss-count**  integer | no description |
| **key-pair-name**  string | no description |
| **lifecycle-hook-timeout**  integer | no description |
| **name**  string / required | no description |
| **notification-email**  string | no description |
| **primary-election-timeout**  integer | no description |
| **public-subnet1-cidr**  string | no description |
| **public-subnet2-cidr**  string | no description |
| **resource-tag-prefix**  string | no description |
| **s3-bucket-name**  string | no description |
| **s3-key-prefix**  string | no description |
| **sync-recovery-count**  integer | no description |
| **terminate-unhealthy-vm**  string | no description  **Choices:**   - `"no"` - `"yes"` |
| **transit-gateway-id**  string | no description |
| **transit-gateway-support-options**  string | no description  **Choices:**   - `"create one"` - `"use an existing one"` |
| **use-custom-asset-location**  string | no description  **Choices:**   - `"no"` - `"yes"` |
| **vpc-cidr**  string | no description |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_cloud_orchestawstemplate_autoscaletgwnewvpc_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_cloud_orchestawstemplate_autoscaletgwnewvpc_module.md#id4)

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
    - name: no description
      fmgr_cloud_orchestawstemplate_autoscaletgwnewvpc:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        cloud_orchestawstemplate_autoscaletgwnewvpc:
          availability-zones: <string>
          bgp-asn: <integer>
          custom-asset-container: <string>
          custom-asset-directory: <string>
          custom-identifier: <string>
          faz-autoscale-admin-password: <list or string>
          faz-autoscale-admin-username: <string>
          faz-custom-private-ipaddress: <string>
          faz-instance-type: <value in [h1.2xlarge, h1.4xlarge, h1.8xlarge, ...]>
          faz-integration-options: <value in [no, yes]>
          faz-version: <string>
          fgt-admin-cidr: <string>
          fgt-admin-port: <integer>
          fgt-instance-type: <value in [t2.small, c5.large, c5.xlarge, ...]>
          fgt-psk-secret: <string>
          fgtasg-cool-down: <integer>
          fgtasg-desired-capacity-byol: <integer>
          fgtasg-desired-capacity-payg: <integer>
          fgtasg-health-check-grace-period: <integer>
          fgtasg-max-size-byol: <integer>
          fgtasg-max-size-payg: <integer>
          fgtasg-min-size-byol: <integer>
          fgtasg-min-size-payg: <integer>
          fgtasg-scale-in-threshold: <integer>
          fgtasg-scale-out-threshold: <integer>
          fos-version: <string>
          get-license-grace-period: <integer>
          heartbeat-delay-allowance: <integer>
          heartbeat-interval: <integer>
          heartbeat-loss-count: <integer>
          key-pair-name: <string>
          lifecycle-hook-timeout: <integer>
          name: <string>
          notification-email: <string>
          primary-election-timeout: <integer>
          public-subnet1-cidr: <string>
          public-subnet2-cidr: <string>
          resource-tag-prefix: <string>
          s3-bucket-name: <string>
          s3-key-prefix: <string>
          sync-recovery-count: <integer>
          terminate-unhealthy-vm: <value in [no, yes]>
          transit-gateway-id: <string>
          transit-gateway-support-options: <value in [create one, use an existing one]>
          use-custom-asset-location: <value in [no, yes]>
          vpc-cidr: <string>
```

## [Return Values](fmgr_cloud_orchestawstemplate_autoscaletgwnewvpc_module.md#id5)

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
