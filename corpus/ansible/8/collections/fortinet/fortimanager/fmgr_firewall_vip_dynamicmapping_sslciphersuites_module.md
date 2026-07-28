---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_firewall_vip_dynamicmapping_sslciphersuites module – SSL/TLS cipher suites acceptable from a client, ordered by priority."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_firewall_vip_dynamicmapping_sslciphersuites_module.html
fetched_at: 2026-07-28T02:13:17+00:00
---
# fortinet.fortimanager.fmgr_firewall_vip_dynamicmapping_sslciphersuites module – SSL/TLS cipher suites acceptable from a client, ordered by priority.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_vip_dynamicmapping_sslciphersuites`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_firewall_vip_dynamicmapping_sslciphersuites_module.md#synopsis)
- [Parameters](fmgr_firewall_vip_dynamicmapping_sslciphersuites_module.md#parameters)
- [Notes](fmgr_firewall_vip_dynamicmapping_sslciphersuites_module.md#notes)
- [Examples](fmgr_firewall_vip_dynamicmapping_sslciphersuites_module.md#examples)
- [Return Values](fmgr_firewall_vip_dynamicmapping_sslciphersuites_module.md#return-values)

## [Synopsis](fmgr_firewall_vip_dynamicmapping_sslciphersuites_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_firewall_vip_dynamicmapping_sslciphersuites_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **dynamic_mapping**  string / required | the parameter (dynamic_mapping) in requested url |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_vip_dynamicmapping_sslciphersuites**  dictionary | the top level parameters set |
| **cipher**  string | no description  **Choices:**   - `"TLS-RSA-WITH-RC4-128-MD5"` - `"TLS-RSA-WITH-RC4-128-SHA"` - `"TLS-RSA-WITH-DES-CBC-SHA"` - `"TLS-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-RSA-WITH-AES-256-CBC-SHA256"` - `"TLS-RSA-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-RSA-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-RSA-WITH-SEED-CBC-SHA"` - `"TLS-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-DHE-RSA-WITH-DES-CBC-SHA"` - `"TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-AES-256-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-SEED-CBC-SHA"` - `"TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-RC4-128-SHA"` - `"TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-DHE-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-DHE-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-DHE-DSS-WITH-AES-128-CBC-SHA"` - `"TLS-DHE-DSS-WITH-AES-256-CBC-SHA"` - `"TLS-DHE-DSS-WITH-AES-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-AES-128-GCM-SHA256"` - `"TLS-DHE-DSS-WITH-AES-256-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-AES-256-GCM-SHA384"` - `"TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384"` - `"TLS-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-SEED-CBC-SHA"` - `"TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA"` - `"TLS-DHE-DSS-WITH-DES-CBC-SHA"` - `"TLS-AES-128-GCM-SHA256"` - `"TLS-AES-256-GCM-SHA384"` - `"TLS-CHACHA20-POLY1305-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA"` |
| **id**  integer / required | no description |
| **priority**  integer | no description |
| **versions**  list / elements=string | no description  **Choices:**   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **vip**  string / required | the parameter (vip) in requested url |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_firewall_vip_dynamicmapping_sslciphersuites_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_firewall_vip_dynamicmapping_sslciphersuites_module.md#id4)

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
    - name: SSL/TLS cipher suites acceptable from a client, ordered by priority.
      fmgr_firewall_vip_dynamicmapping_sslciphersuites:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        vip: <your own value>
        dynamic_mapping: <your own value>
        state: <value in [present, absent]>
        firewall_vip_dynamicmapping_sslciphersuites:
          cipher: <value in [TLS-RSA-WITH-RC4-128-MD5, TLS-RSA-WITH-RC4-128-SHA, TLS-RSA-WITH-DES-CBC-SHA, ...]>
          id: <integer>
          versions:
            - ssl-3.0
            - tls-1.0
            - tls-1.1
            - tls-1.2
            - tls-1.3
          priority: <integer>
```

## [Return Values](fmgr_firewall_vip_dynamicmapping_sslciphersuites_module.md#id5)

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
