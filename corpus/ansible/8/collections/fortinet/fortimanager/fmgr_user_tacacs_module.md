---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_user_tacacs module – Configure TACACS+ server entries."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_user_tacacs_module.html
fetched_at: 2026-07-28T02:21:18+00:00
---
# fortinet.fortimanager.fmgr_user_tacacs module – Configure TACACS+ server entries.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_user_tacacs`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_user_tacacs_module.md#synopsis)
- [Parameters](fmgr_user_tacacs_module.md#parameters)
- [Notes](fmgr_user_tacacs_module.md#notes)
- [Examples](fmgr_user_tacacs_module.md#examples)
- [Return Values](fmgr_user_tacacs_module.md#return-values)

## [Synopsis](fmgr_user_tacacs_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_user_tacacs_module.md#id2)

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
| **user_tacacs**  dictionary | the top level parameters set |
| **authen-type**  string | Allowed authentication protocols/methods.  **Choices:**   - `"auto"` - `"ascii"` - `"pap"` - `"chap"` - `"mschap"` |
| **authorization**  string | Enable/disable TACACS+ authorization.  **Choices:**   - `"disable"` - `"enable"` |
| **dynamic_mapping**  list / elements=dictionary | Dynamic_Mapping. |
| **_scope**  list / elements=dictionary | _Scope. |
| **name**  string | Name. |
| **vdom**  string | Vdom. |
| **authen-type**  string | Allowed authentication protocols/methods.  **Choices:**   - `"auto"` - `"ascii"` - `"pap"` - `"chap"` - `"mschap"` |
| **authorization**  string | Enable/disable TACACS+ authorization.  **Choices:**   - `"disable"` - `"enable"` |
| **interface**  string | Specify outgoing interface to reach server. |
| **interface-select-method**  string | Specify how to select outgoing interface to reach server.  **Choices:**   - `"auto"` - `"sdwan"` - `"specify"` |
| **key**  any | (list) Key to access the primary server. |
| **port**  integer | Port number of the TACACS+ server. |
| **secondary-key**  any | (list) Key to access the secondary server. |
| **secondary-server**  string | Secondary TACACS+ server CN domain name or IP address. |
| **server**  string | Primary TACACS+ server CN domain name or IP address. |
| **source-ip**  string | source IP for communications to TACACS+ server. |
| **tertiary-key**  any | (list) Key to access the tertiary server. |
| **tertiary-server**  string | Tertiary TACACS+ server CN domain name or IP address. |
| **interface**  string | Specify outgoing interface to reach server. |
| **interface-select-method**  string | Specify how to select outgoing interface to reach server.  **Choices:**   - `"auto"` - `"sdwan"` - `"specify"` |
| **key**  any | (list) Key to access the primary server. |
| **name**  string / required | TACACS+ server entry name. |
| **port**  integer | Port number of the TACACS+ server. |
| **secondary-key**  any | (list) Key to access the secondary server. |
| **secondary-server**  string | Secondary TACACS+ server CN domain name or IP address. |
| **server**  string | Primary TACACS+ server CN domain name or IP address. |
| **source-ip**  string | source IP for communications to TACACS+ server. |
| **tertiary-key**  any | (list) Key to access the tertiary server. |
| **tertiary-server**  string | Tertiary TACACS+ server CN domain name or IP address. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_user_tacacs_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_user_tacacs_module.md#id4)

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
    - name: Configure TACACS+ server entries.
      fmgr_user_tacacs:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        user_tacacs:
          authen-type: <value in [auto, ascii, pap, ...]>
          authorization: <value in [disable, enable]>
          dynamic_mapping:
            -
              _scope:
                -
                  name: <string>
                  vdom: <string>
              authen-type: <value in [auto, ascii, pap, ...]>
              authorization: <value in [disable, enable]>
              key: <list or string>
              port: <integer>
              secondary-key: <list or string>
              secondary-server: <string>
              server: <string>
              source-ip: <string>
              tertiary-key: <list or string>
              tertiary-server: <string>
              interface: <string>
              interface-select-method: <value in [auto, sdwan, specify]>
          key: <list or string>
          name: <string>
          port: <integer>
          secondary-key: <list or string>
          secondary-server: <string>
          server: <string>
          source-ip: <string>
          tertiary-key: <list or string>
          tertiary-server: <string>
          interface: <string>
          interface-select-method: <value in [auto, sdwan, specify]>
```

## [Return Values](fmgr_user_tacacs_module.md#id5)

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
