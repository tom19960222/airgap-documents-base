---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_endpointcontrol_fctems module – Configure FortiClient Enterprise Management Server"
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_endpointcontrol_fctems_module.html
fetched_at: 2026-07-28T02:10:41+00:00
---
# fortinet.fortimanager.fmgr_endpointcontrol_fctems module – Configure FortiClient Enterprise Management Server

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_endpointcontrol_fctems`.

New in fortinet.fortimanager 2.1.0

- [Synopsis](fmgr_endpointcontrol_fctems_module.md#synopsis)
- [Parameters](fmgr_endpointcontrol_fctems_module.md#parameters)
- [Notes](fmgr_endpointcontrol_fctems_module.md#notes)
- [Examples](fmgr_endpointcontrol_fctems_module.md#examples)
- [Return Values](fmgr_endpointcontrol_fctems_module.md#return-values)

## [Synopsis](fmgr_endpointcontrol_fctems_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_endpointcontrol_fctems_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **endpointcontrol_fctems**  dictionary | the top level parameters set |
| **admin-password**  any | (list) no description |
| **admin-username**  string | FortiClient EMS admin username. |
| **ca-cn-info**  string | no description |
| **call-timeout**  integer | FortiClient EMS call timeout in seconds |
| **capabilities**  list / elements=string | no description  **Choices:**   - `"fabric-auth"` - `"silent-approval"` - `"websocket"` - `"websocket-malware"` - `"push-ca-certs"` - `"common-tags-api"` - `"tenant-id"` - `"single-vdom-connector"` - `"client-avatars"` |
| **certificate**  string | FortiClient EMS certificate. |
| **certificate-fingerprint**  string | EMS certificate fingerprint. |
| **cloud-server-type**  string | Cloud server type.  **Choices:**   - `"production"` - `"alpha"` - `"beta"` |
| **dirty-reason**  string | Dirty Reason for FortiClient EMS.  **Choices:**   - `"none"` - `"mismatched-ems-sn"` |
| **ems-id**  integer | EMS ID in order |
| **fortinetone-cloud-authentication**  string | Enable/disable authentication of FortiClient EMS Cloud through FortiCloud account.  **Choices:**   - `"disable"` - `"enable"` |
| **https-port**  integer | FortiClient EMS HTTPS access port number. |
| **interface**  string | Specify outgoing interface to reach server. |
| **interface-select-method**  string | Specify how to select outgoing interface to reach server.  **Choices:**   - `"auto"` - `"sdwan"` - `"specify"` |
| **name**  string / required | FortiClient Enterprise Management Server |
| **out-of-sync-threshold**  integer | Outdated resource threshold in seconds |
| **preserve-ssl-session**  string | Enable/disable preservation of EMS SSL session connection.  **Choices:**   - `"disable"` - `"enable"` |
| **pull-avatars**  string | Enable/disable pulling avatars from EMS.  **Choices:**   - `"disable"` - `"enable"` |
| **pull-malware-hash**  string | Enable/disable pulling FortiClient malware hash from EMS.  **Choices:**   - `"disable"` - `"enable"` |
| **pull-sysinfo**  string | Enable/disable pulling SysInfo from EMS.  **Choices:**   - `"disable"` - `"enable"` |
| **pull-tags**  string | Enable/disable pulling FortiClient user tags from EMS.  **Choices:**   - `"disable"` - `"enable"` |
| **pull-vulnerabilities**  string | Enable/disable pulling vulnerabilities from EMS.  **Choices:**   - `"disable"` - `"enable"` |
| **serial-number**  string | FortiClient EMS Serial Number. |
| **server**  string | FortiClient EMS FQDN or IPv4 address. |
| **source-ip**  string | REST API call source IP. |
| **status**  string | Enable or disable this EMS configuration.  **Choices:**   - `"disable"` - `"enable"` |
| **status-check-interval**  integer | FortiClient EMS call timeout in seconds |
| **tenant-id**  string | EMS Tenant ID. |
| **trust-ca-cn**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **websocket-override**  string | Enable/disable override behavior for how this FortiGate unit connects to EMS using a WebSocket connection.  **Choices:**   - `"disable"` - `"enable"` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_endpointcontrol_fctems_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_endpointcontrol_fctems_module.md#id4)

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
    - name: Configure FortiClient Enterprise Management Server
      fmgr_endpointcontrol_fctems:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        endpointcontrol_fctems:
          call-timeout: <integer>
          capabilities:
            - fabric-auth
            - silent-approval
            - websocket
            - websocket-malware
            - push-ca-certs
            - common-tags-api
            - tenant-id
            - single-vdom-connector
            - client-avatars
          certificate-fingerprint: <string>
          cloud-server-type: <value in [production, alpha, beta]>
          fortinetone-cloud-authentication: <value in [disable, enable]>
          https-port: <integer>
          name: <string>
          out-of-sync-threshold: <integer>
          preserve-ssl-session: <value in [disable, enable]>
          pull-avatars: <value in [disable, enable]>
          pull-malware-hash: <value in [disable, enable]>
          pull-sysinfo: <value in [disable, enable]>
          pull-tags: <value in [disable, enable]>
          pull-vulnerabilities: <value in [disable, enable]>
          server: <string>
          source-ip: <string>
          websocket-override: <value in [disable, enable]>
          status-check-interval: <integer>
          certificate: <string>
          admin-username: <string>
          serial-number: <string>
          admin-password: <list or string>
          interface: <string>
          interface-select-method: <value in [auto, sdwan, specify]>
          dirty-reason: <value in [none, mismatched-ems-sn]>
          ems-id: <integer>
          status: <value in [disable, enable]>
          ca-cn-info: <string>
          trust-ca-cn: <value in [disable, enable]>
          tenant-id: <string>
```

## [Return Values](fmgr_endpointcontrol_fctems_module.md#id5)

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
