---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_vpnmgr_vpntable module – no description"
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_vpnmgr_vpntable_module.html
fetched_at: 2026-07-28T02:21:47+00:00
---
# fortinet.fortimanager.fmgr_vpnmgr_vpntable module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_vpnmgr_vpntable`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_vpnmgr_vpntable_module.md#synopsis)
- [Parameters](fmgr_vpnmgr_vpntable_module.md#parameters)
- [Notes](fmgr_vpnmgr_vpntable_module.md#notes)
- [Examples](fmgr_vpnmgr_vpntable_module.md#examples)
- [Return Values](fmgr_vpnmgr_vpntable_module.md#return-values)

## [Synopsis](fmgr_vpnmgr_vpntable_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_vpnmgr_vpntable_module.md#id2)

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
| **vpnmgr_vpntable**  dictionary | the top level parameters set |
| **authmethod**  string | Authmethod.  **Choices:**   - `"psk"` - `"rsa-signature"` - `"signature"` |
| **auto-zone-policy**  string | Auto-Zone-Policy.  **Choices:**   - `"disable"` - `"enable"` |
| **certificate**  any | (list or str) Certificate. |
| **description**  string | Description. |
| **dpd**  string | Dpd.  **Choices:**   - `"disable"` - `"enable"` - `"on-idle"` - `"on-demand"` |
| **dpd-retrycount**  integer | Dpd-Retrycount. |
| **dpd-retryinterval**  any | (list) Dpd-Retryinterval. |
| **fcc-enforcement**  string | Fcc-Enforcement.  **Choices:**   - `"disable"` - `"enable"` |
| **hub2spoke-zone**  any | (list or str) Hub2Spoke-Zone. |
| **ike-version**  string | Ike-Version.  **Choices:**   - `"1"` - `"2"` |
| **ike1dhgroup**  list / elements=string | Ike1Dhgroup.  **Choices:**   - `"1"` - `"2"` - `"5"` - `"14"` - `"15"` - `"16"` - `"17"` - `"18"` - `"19"` - `"20"` - `"21"` - `"27"` - `"28"` - `"29"` - `"30"` - `"31"` - `"32"` |
| **ike1dpd**  string | Ike1Dpd.  **Choices:**   - `"disable"` - `"enable"` |
| **ike1keylifesec**  integer | Ike1Keylifesec. |
| **ike1localid**  string | Ike1Localid. |
| **ike1mode**  string | Ike1Mode.  **Choices:**   - `"main"` - `"aggressive"` |
| **ike1natkeepalive**  integer | Ike1Natkeepalive. |
| **ike1nattraversal**  string | Ike1Nattraversal.  **Choices:**   - `"disable"` - `"enable"` - `"forced"` |
| **ike1proposal**  string | Ike1Proposal.  **Choices:**   - `"des-md5"` - `"des-sha1"` - `"3des-md5"` - `"3des-sha1"` - `"aes128-md5"` - `"aes128-sha1"` - `"aes192-md5"` - `"aes192-sha1"` - `"aes256-md5"` - `"aes256-sha1"` - `"des-sha256"` - `"3des-sha256"` - `"aes128-sha256"` - `"aes192-sha256"` - `"aes256-sha256"` - `"des-sha384"` - `"des-sha512"` - `"3des-sha384"` - `"3des-sha512"` - `"aes128-sha384"` - `"aes128-sha512"` - `"aes192-sha384"` - `"aes192-sha512"` - `"aes256-sha384"` - `"aes256-sha512"` - `"aria128-md5"` - `"aria128-sha1"` - `"aria128-sha256"` - `"aria128-sha384"` - `"aria128-sha512"` - `"aria192-md5"` - `"aria192-sha1"` - `"aria192-sha256"` - `"aria192-sha384"` - `"aria192-sha512"` - `"aria256-md5"` - `"aria256-sha1"` - `"aria256-sha256"` - `"aria256-sha384"` - `"aria256-sha512"` - `"seed-md5"` - `"seed-sha1"` - `"seed-sha256"` - `"seed-sha384"` - `"seed-sha512"` - `"aes128gcm-prfsha1"` - `"aes128gcm-prfsha256"` - `"aes128gcm-prfsha384"` - `"aes128gcm-prfsha512"` - `"aes256gcm-prfsha1"` - `"aes256gcm-prfsha256"` - `"aes256gcm-prfsha384"` - `"aes256gcm-prfsha512"` - `"chacha20poly1305-prfsha1"` - `"chacha20poly1305-prfsha256"` - `"chacha20poly1305-prfsha384"` - `"chacha20poly1305-prfsha512"` |
| **ike2autonego**  string | Ike2Autonego.  **Choices:**   - `"disable"` - `"enable"` |
| **ike2dhgroup**  list / elements=string | Ike2Dhgroup.  **Choices:**   - `"1"` - `"2"` - `"5"` - `"14"` - `"15"` - `"16"` - `"17"` - `"18"` - `"19"` - `"20"` - `"21"` - `"27"` - `"28"` - `"29"` - `"30"` - `"31"` - `"32"` |
| **ike2keepalive**  string | Ike2Keepalive.  **Choices:**   - `"disable"` - `"enable"` |
| **ike2keylifekbs**  integer | Ike2Keylifekbs. |
| **ike2keylifesec**  integer | Ike2Keylifesec. |
| **ike2keylifetype**  string | Ike2Keylifetype.  **Choices:**   - `"seconds"` - `"kbs"` - `"both"` |
| **ike2proposal**  string | Ike2Proposal.  **Choices:**   - `"null-md5"` - `"null-sha1"` - `"des-null"` - `"3des-null"` - `"des-md5"` - `"des-sha1"` - `"3des-md5"` - `"3des-sha1"` - `"aes128-md5"` - `"aes128-sha1"` - `"aes192-md5"` - `"aes192-sha1"` - `"aes256-md5"` - `"aes256-sha1"` - `"aes128-null"` - `"aes192-null"` - `"aes256-null"` - `"null-sha256"` - `"des-sha256"` - `"3des-sha256"` - `"aes128-sha256"` - `"aes192-sha256"` - `"aes256-sha256"` - `"des-sha384"` - `"des-sha512"` - `"3des-sha384"` - `"3des-sha512"` - `"aes128-sha384"` - `"aes128-sha512"` - `"aes192-sha384"` - `"aes192-sha512"` - `"aes256-sha384"` - `"aes256-sha512"` - `"null-sha384"` - `"null-sha512"` - `"aria128-null"` - `"aria128-md5"` - `"aria128-sha1"` - `"aria128-sha256"` - `"aria128-sha384"` - `"aria128-sha512"` - `"aria192-null"` - `"aria192-md5"` - `"aria192-sha1"` - `"aria192-sha256"` - `"aria192-sha384"` - `"aria192-sha512"` - `"aria256-null"` - `"aria256-md5"` - `"aria256-sha1"` - `"aria256-sha256"` - `"aria256-sha384"` - `"aria256-sha512"` - `"seed-null"` - `"seed-md5"` - `"seed-sha1"` - `"seed-sha256"` - `"seed-sha384"` - `"seed-sha512"` - `"aes128gcm"` - `"aes256gcm"` - `"chacha20poly1305"` |
| **inter-vdom**  string | Inter-Vdom.  **Choices:**   - `"disable"` - `"enable"` |
| **intf-mode**  string | Intf-Mode.  **Choices:**   - `"off"` - `"on"` |
| **localid-type**  string | Localid-Type.  **Choices:**   - `"auto"` - `"fqdn"` - `"user-fqdn"` - `"keyid"` - `"address"` - `"asn1dn"` |
| **name**  string / required | Name. |
| **negotiate-timeout**  integer | Negotiate-Timeout. |
| **network-id**  integer | Network-Id. |
| **network-overlay**  string | Network-Overlay.  **Choices:**   - `"disable"` - `"enable"` |
| **npu-offload**  string | Npu-Offload.  **Choices:**   - `"disable"` - `"enable"` |
| **pfs**  string | Pfs.  **Choices:**   - `"disable"` - `"enable"` |
| **psk-auto-generate**  string | Psk-Auto-Generate.  **Choices:**   - `"disable"` - `"enable"` |
| **psksecret**  any | (list) Psksecret. |
| **replay**  string | Replay.  **Choices:**   - `"disable"` - `"enable"` |
| **rsa-certificate**  string | Rsa-Certificate. |
| **spoke2hub-zone**  any | (list or str) Spoke2Hub-Zone. |
| **topology**  string | Topology.  **Choices:**   - `"meshed"` - `"star"` - `"dialup"` |
| **vpn-zone**  any | (list or str) Vpn-Zone. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_vpnmgr_vpntable_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_vpnmgr_vpntable_module.md#id4)

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
      fmgr_vpnmgr_vpntable:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        vpnmgr_vpntable:
          authmethod: <value in [psk, rsa-signature, signature]>
          auto-zone-policy: <value in [disable, enable]>
          certificate: <list or string>
          description: <string>
          dpd: <value in [disable, enable, on-idle, ...]>
          dpd-retrycount: <integer>
          dpd-retryinterval: <list or integer>
          fcc-enforcement: <value in [disable, enable]>
          hub2spoke-zone: <list or string>
          ike-version: <value in [1, 2]>
          ike1dhgroup:
            - 1
            - 2
            - 5
            - 14
            - 15
            - 16
            - 17
            - 18
            - 19
            - 20
            - 21
            - 27
            - 28
            - 29
            - 30
            - 31
            - 32
          ike1dpd: <value in [disable, enable]>
          ike1keylifesec: <integer>
          ike1localid: <string>
          ike1mode: <value in [main, aggressive]>
          ike1natkeepalive: <integer>
          ike1nattraversal: <value in [disable, enable, forced]>
          ike1proposal: <value in [des-md5, des-sha1, 3des-md5, ...]>
          ike2autonego: <value in [disable, enable]>
          ike2dhgroup:
            - 1
            - 2
            - 5
            - 14
            - 15
            - 16
            - 17
            - 18
            - 19
            - 20
            - 21
            - 27
            - 28
            - 29
            - 30
            - 31
            - 32
          ike2keepalive: <value in [disable, enable]>
          ike2keylifekbs: <integer>
          ike2keylifesec: <integer>
          ike2keylifetype: <value in [seconds, kbs, both]>
          ike2proposal: <value in [null-md5, null-sha1, des-null, ...]>
          inter-vdom: <value in [disable, enable]>
          intf-mode: <value in [off, on]>
          localid-type: <value in [auto, fqdn, user-fqdn, ...]>
          name: <string>
          negotiate-timeout: <integer>
          npu-offload: <value in [disable, enable]>
          pfs: <value in [disable, enable]>
          psk-auto-generate: <value in [disable, enable]>
          psksecret: <list or string>
          replay: <value in [disable, enable]>
          rsa-certificate: <string>
          spoke2hub-zone: <list or string>
          topology: <value in [meshed, star, dialup]>
          vpn-zone: <list or string>
          network-id: <integer>
          network-overlay: <value in [disable, enable]>
```

## [Return Values](fmgr_vpnmgr_vpntable_module.md#id5)

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
