---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_system_npu_fpanomaly module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_system_npu_fpanomaly_module.html
fetched_at: 2026-07-27T17:36:45+00:00
---
# fortinet.fortimanager.fmgr_system_npu_fpanomaly module – no description

> **Note:**
>
> This module is part of the [fortinet.fortimanager collection](https://galaxy.ansible.com/fortinet/fortimanager) (version 2.1.7).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortimanager`.
>
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_npu_fpanomaly`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_system_npu_fpanomaly_module.md#synopsis)
- [Parameters](fmgr_system_npu_fpanomaly_module.md#parameters)
- [Notes](fmgr_system_npu_fpanomaly_module.md#notes)
- [Examples](fmgr_system_npu_fpanomaly_module.md#examples)
- [Return Values](fmgr_system_npu_fpanomaly_module.md#return-values)

## [Synopsis](fmgr_system_npu_fpanomaly_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_npu_fpanomaly_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **system_npu_fpanomaly**  dictionary | the top level parameters set |
| **esp-minlen-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **icmp-csum-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **icmp-minlen-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **ipv4-csum-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **ipv4-ihl-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **ipv4-len-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **ipv4-opt-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **ipv4-ttlzero-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **ipv4-ver-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **ipv6-exthdr-len-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **ipv6-exthdr-order-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **ipv6-ihl-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **ipv6-plen-zero**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **ipv6-ver-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **tcp-csum-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **tcp-hlen-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **tcp-plen-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **udp-csum-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **udp-hlen-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **udp-len-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **udp-plen-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **udplite-cover-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **udplite-csum-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **unknproto-minlen-err**  string | no description  Choices:   - `"drop"` - `"trap-to-host"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_system_npu_fpanomaly_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_npu_fpanomaly_module.md#id4)

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
     fmgr_system_npu_fpanomaly:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        system_npu_fpanomaly:
           esp-minlen-err: <value in [drop, trap-to-host]>
           icmp-csum-err: <value in [drop, trap-to-host]>
           icmp-minlen-err: <value in [drop, trap-to-host]>
           ipv4-csum-err: <value in [drop, trap-to-host]>
           ipv4-ihl-err: <value in [drop, trap-to-host]>
           ipv4-len-err: <value in [drop, trap-to-host]>
           ipv4-opt-err: <value in [drop, trap-to-host]>
           ipv4-ttlzero-err: <value in [drop, trap-to-host]>
           ipv4-ver-err: <value in [drop, trap-to-host]>
           ipv6-exthdr-len-err: <value in [drop, trap-to-host]>
           ipv6-exthdr-order-err: <value in [drop, trap-to-host]>
           ipv6-ihl-err: <value in [drop, trap-to-host]>
           ipv6-plen-zero: <value in [drop, trap-to-host]>
           ipv6-ver-err: <value in [drop, trap-to-host]>
           tcp-csum-err: <value in [drop, trap-to-host]>
           tcp-hlen-err: <value in [drop, trap-to-host]>
           tcp-plen-err: <value in [drop, trap-to-host]>
           udp-csum-err: <value in [drop, trap-to-host]>
           udp-hlen-err: <value in [drop, trap-to-host]>
           udp-len-err: <value in [drop, trap-to-host]>
           udp-plen-err: <value in [drop, trap-to-host]>
           udplite-cover-err: <value in [drop, trap-to-host]>
           udplite-csum-err: <value in [drop, trap-to-host]>
           unknproto-minlen-err: <value in [drop, trap-to-host]>
```

## [Return Values](fmgr_system_npu_fpanomaly_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **request_url**  string | The full url requested  Returned: always  Sample: `"/sys/login/user"` |
| **response_code**  integer | The status of api request  Returned: always  Sample: `0` |
| **response_message**  string | The descriptive message of the api response  Returned: always  Sample: `"OK."` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/issues)
[Homepage](https://fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/tree/galaxy/2.1.7)
