---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_switchcontroller_lldpprofile module – Configure FortiSwitch LLDP profiles."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_switchcontroller_lldpprofile_module.html
fetched_at: 2026-07-28T02:17:15+00:00
---
# fortinet.fortimanager.fmgr_switchcontroller_lldpprofile module – Configure FortiSwitch LLDP profiles.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_switchcontroller_lldpprofile`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_switchcontroller_lldpprofile_module.md#synopsis)
- [Parameters](fmgr_switchcontroller_lldpprofile_module.md#parameters)
- [Notes](fmgr_switchcontroller_lldpprofile_module.md#notes)
- [Examples](fmgr_switchcontroller_lldpprofile_module.md#examples)
- [Return Values](fmgr_switchcontroller_lldpprofile_module.md#return-values)

## [Synopsis](fmgr_switchcontroller_lldpprofile_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_switchcontroller_lldpprofile_module.md#id2)

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
| **switchcontroller_lldpprofile**  dictionary | the top level parameters set |
| **802.1-tlvs**  list / elements=string | Transmitted IEEE 802.  **Choices:**   - `"port-vlan-id"` |
| **802.3-tlvs**  list / elements=string | Transmitted IEEE 802.  **Choices:**   - `"max-frame-size"` - `"power-negotiation"` |
| **auto-isl**  string | Enable/disable auto inter-switch LAG.  **Choices:**   - `"disable"` - `"enable"` |
| **auto-isl-auth**  string | Auto inter-switch LAG authentication mode.  **Choices:**   - `"legacy"` - `"strict"` - `"relax"` |
| **auto-isl-auth-encrypt**  string | Auto inter-switch LAG encryption mode.  **Choices:**   - `"none"` - `"mixed"` - `"must"` |
| **auto-isl-auth-identity**  string | Auto inter-switch LAG authentication identity. |
| **auto-isl-auth-macsec-profile**  string | Auto inter-switch LAG macsec profile for encryption. |
| **auto-isl-auth-reauth**  integer | Auto inter-switch LAG authentication reauth period in seconds |
| **auto-isl-auth-user**  string | Auto inter-switch LAG authentication user certificate. |
| **auto-isl-hello-timer**  integer | Auto inter-switch LAG hello timer duration |
| **auto-isl-port-group**  integer | Auto inter-switch LAG port group ID |
| **auto-isl-receive-timeout**  integer | Auto inter-switch LAG timeout if no response is received |
| **auto-mclag-icl**  string | Enable/disable MCLAG inter chassis link.  **Choices:**   - `"disable"` - `"enable"` |
| **custom-tlvs**  list / elements=dictionary | Custom-Tlvs. |
| **information-string**  string | Organizationally defined information string |
| **name**  string | TLV name |
| **oui**  string | Organizationally unique identifier |
| **subtype**  integer | Organizationally defined subtype |
| **med-location-service**  list / elements=dictionary | Med-Location-Service. |
| **name**  string | Location service type name. |
| **status**  string | Enable or disable this TLV.  **Choices:**   - `"disable"` - `"enable"` |
| **sys-location-id**  string | Location service ID. |
| **med-network-policy**  list / elements=dictionary | Med-Network-Policy. |
| **assign-vlan**  string | Enable/disable VLAN assignment when this profile is applied on managed FortiSwitch port.  **Choices:**   - `"disable"` - `"enable"` |
| **dscp**  integer | Advertised Differentiated Services Code Point |
| **name**  string | Policy type name. |
| **priority**  integer | Advertised Layer 2 priority |
| **status**  string | Enable or disable this TLV.  **Choices:**   - `"disable"` - `"enable"` |
| **vlan**  integer | ID of VLAN to advertise, if configured on port |
| **vlan-intf**  string | VLAN interface to advertise; if configured on port. |
| **med-tlvs**  list / elements=string | Transmitted LLDP-MED TLVs  **Choices:**   - `"inventory-management"` - `"network-policy"` - `"power-management"` - `"location-identification"` |
| **name**  string / required | Profile name. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_switchcontroller_lldpprofile_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_switchcontroller_lldpprofile_module.md#id4)

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
    - name: Configure FortiSwitch LLDP profiles.
      fmgr_switchcontroller_lldpprofile:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        switchcontroller_lldpprofile:
          802.1-tlvs:
            - port-vlan-id
          802.3-tlvs:
            - max-frame-size
            - power-negotiation
          auto-isl: <value in [disable, enable]>
          auto-isl-hello-timer: <integer>
          auto-isl-port-group: <integer>
          auto-isl-receive-timeout: <integer>
          custom-tlvs:
            -
              information-string: <string>
              name: <string>
              oui: <string>
              subtype: <integer>
          med-network-policy:
            -
              dscp: <integer>
              name: <string>
              priority: <integer>
              status: <value in [disable, enable]>
              vlan: <integer>
              vlan-intf: <string>
              assign-vlan: <value in [disable, enable]>
          med-tlvs:
            - inventory-management
            - network-policy
            - power-management
            - location-identification
          name: <string>
          med-location-service:
            -
              name: <string>
              status: <value in [disable, enable]>
              sys-location-id: <string>
          auto-mclag-icl: <value in [disable, enable]>
          auto-isl-auth: <value in [legacy, strict, relax]>
          auto-isl-auth-encrypt: <value in [none, mixed, must]>
          auto-isl-auth-identity: <string>
          auto-isl-auth-macsec-profile: <string>
          auto-isl-auth-reauth: <integer>
          auto-isl-auth-user: <string>
```

## [Return Values](fmgr_switchcontroller_lldpprofile_module.md#id5)

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
