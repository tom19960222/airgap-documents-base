---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_firewall_accessproxy_serverpubkeyauthsettings module – Server SSH public key authentication settings."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_firewall_accessproxy_serverpubkeyauthsettings_module.html
fetched_at: 2026-07-28T02:11:24+00:00
---
# fortinet.fortimanager.fmgr_firewall_accessproxy_serverpubkeyauthsettings module – Server SSH public key authentication settings.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_accessproxy_serverpubkeyauthsettings`.

New in fortinet.fortimanager 2.1.0

- [Synopsis](fmgr_firewall_accessproxy_serverpubkeyauthsettings_module.md#synopsis)
- [Parameters](fmgr_firewall_accessproxy_serverpubkeyauthsettings_module.md#parameters)
- [Notes](fmgr_firewall_accessproxy_serverpubkeyauthsettings_module.md#notes)
- [Examples](fmgr_firewall_accessproxy_serverpubkeyauthsettings_module.md#examples)
- [Return Values](fmgr_firewall_accessproxy_serverpubkeyauthsettings_module.md#return-values)

## [Synopsis](fmgr_firewall_accessproxy_serverpubkeyauthsettings_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_firewall_accessproxy_serverpubkeyauthsettings_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access-proxy**  string / required | the parameter (access-proxy) in requested url |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_accessproxy_serverpubkeyauthsettings**  dictionary | the top level parameters set |
| **auth-ca**  string | Name of the SSH server public key authentication CA. |
| **cert-extension**  list / elements=dictionary | no description |
| **critical**  string | Critical option.  **Choices:**   - `"no"` - `"yes"` |
| **data**  string | Name of certificate extension. |
| **name**  string | Name of certificate extension. |
| **type**  string | Type of certificate extension.  **Choices:**   - `"fixed"` - `"user"` |
| **permit-agent-forwarding**  string | Enable/disable appending permit-agent-forwarding certificate extension.  **Choices:**   - `"disable"` - `"enable"` |
| **permit-port-forwarding**  string | Enable/disable appending permit-port-forwarding certificate extension.  **Choices:**   - `"disable"` - `"enable"` |
| **permit-pty**  string | Enable/disable appending permit-pty certificate extension.  **Choices:**   - `"disable"` - `"enable"` |
| **permit-user-rc**  string | Enable/disable appending permit-user-rc certificate extension.  **Choices:**   - `"disable"` - `"enable"` |
| **permit-x11-forwarding**  string | Enable/disable appending permit-x11-forwarding certificate extension.  **Choices:**   - `"disable"` - `"enable"` |
| **source-address**  string | Enable/disable appending source-address certificate critical option.  **Choices:**   - `"disable"` - `"enable"` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_firewall_accessproxy_serverpubkeyauthsettings_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_firewall_accessproxy_serverpubkeyauthsettings_module.md#id4)

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
    - name: Server SSH public key authentication settings.
      fmgr_firewall_accessproxy_serverpubkeyauthsettings:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        access-proxy: <your own value>
        firewall_accessproxy_serverpubkeyauthsettings:
          auth-ca: <string>
          cert-extension:
            -
              critical: <value in [no, yes]>
              data: <string>
              name: <string>
              type: <value in [fixed, user]>
          permit-agent-forwarding: <value in [disable, enable]>
          permit-port-forwarding: <value in [disable, enable]>
          permit-pty: <value in [disable, enable]>
          permit-user-rc: <value in [disable, enable]>
          permit-x11-forwarding: <value in [disable, enable]>
          source-address: <value in [disable, enable]>
```

## [Return Values](fmgr_firewall_accessproxy_serverpubkeyauthsettings_module.md#id5)

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
