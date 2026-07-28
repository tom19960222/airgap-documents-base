---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_user_exchange module – Configure MS Exchange server entries."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_user_exchange_module.html
fetched_at: 2026-07-28T02:20:48+00:00
---
# fortinet.fortimanager.fmgr_user_exchange module – Configure MS Exchange server entries.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_user_exchange`.

New in fortinet.fortimanager 2.1.0

- [Synopsis](fmgr_user_exchange_module.md#synopsis)
- [Parameters](fmgr_user_exchange_module.md#parameters)
- [Notes](fmgr_user_exchange_module.md#notes)
- [Examples](fmgr_user_exchange_module.md#examples)
- [Return Values](fmgr_user_exchange_module.md#return-values)

## [Synopsis](fmgr_user_exchange_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_user_exchange_module.md#id2)

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
| **user_exchange**  dictionary | the top level parameters set |
| **addr-type**  string | Indicate whether the server IP-address is IPv4 or IPv6.  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **auth-level**  string | Authentication security level used for the RPC protocol layer.  **Choices:**   - `"low"` - `"medium"` - `"normal"` - `"high"` - `"connect"` - `"call"` - `"packet"` - `"integrity"` - `"privacy"` |
| **auth-type**  string | Authentication security type used for the RPC protocol layer.  **Choices:**   - `"spnego"` - `"ntlm"` - `"kerberos"` |
| **auto-discover-kdc**  string | Enable/disable automatic discovery of KDC IP addresses.  **Choices:**   - `"disable"` - `"enable"` |
| **connect-protocol**  string | Connection protocol used to connect to MS Exchange service.  **Choices:**   - `"rpc-over-tcp"` - `"rpc-over-http"` - `"rpc-over-https"` |
| **domain-name**  string | MS Exchange server fully qualified domain name. |
| **http-auth-type**  string | Authentication security type used for the HTTP transport.  **Choices:**   - `"ntlm"` - `"basic"` |
| **ip**  string | Server IPv4 address. |
| **ip6**  string | Server IPv6 address. |
| **kdc-ip**  any | (list) KDC IPv4 addresses for Kerberos authentication. |
| **name**  string / required | MS Exchange server entry name. |
| **password**  any | (list) Password for the specified username. |
| **server-name**  string | MS Exchange server hostname. |
| **ssl-min-proto-version**  string | Minimum SSL/TLS protocol version for HTTPS transport  **Choices:**   - `"default"` - `"TLSv1-1"` - `"TLSv1-2"` - `"SSLv3"` - `"TLSv1"` - `"TLSv1-3"` |
| **username**  string | User name used to sign in to the server. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_user_exchange_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_user_exchange_module.md#id4)

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
    - name: Configure MS Exchange server entries.
      fmgr_user_exchange:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        user_exchange:
          addr-type: <value in [ipv4, ipv6]>
          auth-level: <value in [low, medium, normal, ...]>
          auth-type: <value in [spnego, ntlm, kerberos]>
          connect-protocol: <value in [rpc-over-tcp, rpc-over-http, rpc-over-https]>
          domain-name: <string>
          http-auth-type: <value in [ntlm, basic]>
          ip: <string>
          ip6: <string>
          kdc-ip: <list or string>
          name: <string>
          password: <list or string>
          server-name: <string>
          ssl-min-proto-version: <value in [default, TLSv1-1, TLSv1-2, ...]>
          username: <string>
          auto-discover-kdc: <value in [disable, enable]>
```

## [Return Values](fmgr_user_exchange_module.md#id5)

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
