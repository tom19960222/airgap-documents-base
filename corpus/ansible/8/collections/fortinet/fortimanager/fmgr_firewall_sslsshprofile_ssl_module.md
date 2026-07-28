---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_firewall_sslsshprofile_ssl module – Configure SSL options."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_firewall_sslsshprofile_ssl_module.html
fetched_at: 2026-07-28T02:13:00+00:00
---
# fortinet.fortimanager.fmgr_firewall_sslsshprofile_ssl module – Configure SSL options.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_sslsshprofile_ssl`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_firewall_sslsshprofile_ssl_module.md#synopsis)
- [Parameters](fmgr_firewall_sslsshprofile_ssl_module.md#parameters)
- [Notes](fmgr_firewall_sslsshprofile_ssl_module.md#notes)
- [Examples](fmgr_firewall_sslsshprofile_ssl_module.md#examples)
- [Return Values](fmgr_firewall_sslsshprofile_ssl_module.md#return-values)

## [Synopsis](fmgr_firewall_sslsshprofile_ssl_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_firewall_sslsshprofile_ssl_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_sslsshprofile_ssl**  dictionary | the top level parameters set |
| **allow-invalid-server-cert**  string | When enabled, allows SSL sessions whose server certificate validation failed.  **Choices:**   - `"disable"` - `"enable"` |
| **cert-probe-failure**  string | Action based on certificate probe failure.  **Choices:**   - `"block"` - `"allow"` |
| **cert-validation-failure**  string | Action based on certificate validation failure.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **cert-validation-timeout**  string | Action based on certificate validation timeout.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **client-cert-request**  string | Action based on client certificate request.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **client-certificate**  string | Action based on received client certificate.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **expired-server-cert**  string | Action based on server certificate is expired.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **inspect-all**  string | Level of SSL inspection.  **Choices:**   - `"disable"` - `"certificate-inspection"` - `"deep-inspection"` |
| **invalid-server-cert**  string | Allow or block the invalid SSL session server certificate.  **Choices:**   - `"allow"` - `"block"` |
| **min-allowed-ssl-version**  string | Minimum SSL version to be allowed.  **Choices:**   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **revoked-server-cert**  string | Action based on server certificate is revoked.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **sni-server-cert-check**  string | Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.  **Choices:**   - `"disable"` - `"enable"` - `"strict"` |
| **unsupported-ssl**  string | Action based on the SSL encryption used being unsupported.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **unsupported-ssl-cipher**  string | Action based on the SSL cipher used being unsupported.  **Choices:**   - `"allow"` - `"block"` |
| **unsupported-ssl-negotiation**  string | Action based on the SSL negotiation used being unsupported.  **Choices:**   - `"allow"` - `"block"` |
| **unsupported-ssl-version**  string | Action based on the SSL version used being unsupported.  **Choices:**   - `"block"` - `"allow"` - `"inspect"` |
| **untrusted-cert**  string | Allow, ignore, or block the untrusted SSL session server certificate.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **untrusted-server-cert**  string | Allow, ignore, or block the untrusted SSL session server certificate.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **ssl-ssh-profile**  string / required | the parameter (ssl-ssh-profile) in requested url |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_firewall_sslsshprofile_ssl_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_firewall_sslsshprofile_ssl_module.md#id4)

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
    - name: Configure SSL options.
      fmgr_firewall_sslsshprofile_ssl:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        ssl-ssh-profile: <your own value>
        firewall_sslsshprofile_ssl:
          allow-invalid-server-cert: <value in [disable, enable]>
          client-cert-request: <value in [bypass, inspect, block]>
          inspect-all: <value in [disable, certificate-inspection, deep-inspection]>
          unsupported-ssl: <value in [bypass, inspect, block]>
          untrusted-cert: <value in [allow, block, ignore]>
          invalid-server-cert: <value in [allow, block]>
          sni-server-cert-check: <value in [disable, enable, strict]>
          untrusted-server-cert: <value in [allow, block, ignore]>
          cert-validation-failure: <value in [allow, block, ignore]>
          cert-validation-timeout: <value in [allow, block, ignore]>
          client-certificate: <value in [bypass, inspect, block]>
          expired-server-cert: <value in [allow, block, ignore]>
          revoked-server-cert: <value in [allow, block, ignore]>
          unsupported-ssl-cipher: <value in [allow, block]>
          unsupported-ssl-negotiation: <value in [allow, block]>
          cert-probe-failure: <value in [block, allow]>
          min-allowed-ssl-version: <value in [ssl-3.0, tls-1.0, tls-1.1, ...]>
          unsupported-ssl-version: <value in [block, allow, inspect]>
```

## [Return Values](fmgr_firewall_sslsshprofile_ssl_module.md#id5)

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
