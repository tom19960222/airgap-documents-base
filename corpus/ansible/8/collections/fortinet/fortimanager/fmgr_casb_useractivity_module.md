---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_casb_useractivity module – Configure CASB user activity."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_casb_useractivity_module.html
fetched_at: 2026-07-28T02:08:25+00:00
---
# fortinet.fortimanager.fmgr_casb_useractivity module – Configure CASB user activity.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_casb_useractivity`.

New in fortinet.fortimanager 2.3.0

- [Synopsis](fmgr_casb_useractivity_module.md#synopsis)
- [Parameters](fmgr_casb_useractivity_module.md#parameters)
- [Notes](fmgr_casb_useractivity_module.md#notes)
- [Examples](fmgr_casb_useractivity_module.md#examples)
- [Return Values](fmgr_casb_useractivity_module.md#return-values)

## [Synopsis](fmgr_casb_useractivity_module.md#id2)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_casb_useractivity_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **casb_useractivity**  dictionary | the top level parameters set |
| **application**  string | CASB SaaS application name. |
| **casb-name**  string | CASB user activity signature name. |
| **category**  string | CASB user activity category.  **Choices:**   - `"activity-control"` - `"tenant-control"` - `"domain-control"` - `"safe-search-control"` - `"other"` |
| **control-options**  list / elements=dictionary | no description |
| **name**  string | CASB control option name. |
| **operations**  list / elements=dictionary | no description |
| **action**  string | CASB operation action.  **Choices:**   - `"append"` - `"prepend"` - `"replace"` - `"new"` - `"new-on-not-found"` - `"delete"` |
| **case-sensitive**  string | CASB operation search case sensitive.  **Choices:**   - `"disable"` - `"enable"` |
| **direction**  string | CASB operation direction.  **Choices:**   - `"request"` |
| **header-name**  string | CASB operation header name to search. |
| **name**  string | CASB control option operation name. |
| **search-key**  string | CASB operation key to search. |
| **search-pattern**  string | CASB operation search pattern.  **Choices:**   - `"simple"` - `"substr"` - `"regexp"` |
| **target**  string | CASB operation target.  **Choices:**   - `"header"` - `"path"` |
| **value-from-input**  string | Enable/disable value from user input.  **Choices:**   - `"disable"` - `"enable"` |
| **values**  list / elements=string | no description |
| **description**  string | CASB user activity description. |
| **match**  list / elements=dictionary | no description |
| **id**  integer | CASB user activity match rules ID. |
| **rules**  list / elements=dictionary | no description |
| **case-sensitive**  string | CASB user activity match case sensitive.  **Choices:**   - `"disable"` - `"enable"` |
| **domains**  list / elements=string | no description |
| **header-name**  string | CASB user activity rule header name. |
| **id**  integer | CASB user activity rule ID. |
| **match-pattern**  string | CASB user activity rule match pattern.  **Choices:**   - `"simple"` - `"substr"` - `"regexp"` |
| **match-value**  string | CASB user activity rule match value. |
| **methods**  list / elements=string | no description |
| **negate**  string | Enable/disable what the matching strategy must not be.  **Choices:**   - `"disable"` - `"enable"` |
| **type**  string | CASB user activity rule type.  **Choices:**   - `"domains"` - `"host"` - `"path"` - `"header"` - `"header-value"` - `"method"` |
| **strategy**  string | CASB user activity rules strategy.  **Choices:**   - `"or"` - `"and"` |
| **match-strategy**  string | CASB user activity match strategy.  **Choices:**   - `"or"` - `"and"` |
| **name**  string / required | CASB user activity name. |
| **type**  string | CASB user activity type.  **Choices:**   - `"built-in"` - `"customized"` |
| **uuid**  string | Universally Unique Identifier |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_casb_useractivity_module.md#id4)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_casb_useractivity_module.md#id5)

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
    - name: Configure CASB user activity.
      fmgr_casb_useractivity:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        casb_useractivity:
          application: <string>
          casb-name: <string>
          category: <value in [activity-control, tenant-control, domain-control, ...]>
          control-options:
            -
              name: <string>
              operations:
                -
                  action: <value in [append, prepend, replace, ...]>
                  case-sensitive: <value in [disable, enable]>
                  direction: <value in [request]>
                  header-name: <string>
                  name: <string>
                  search-key: <string>
                  search-pattern: <value in [simple, substr, regexp]>
                  target: <value in [header, path]>
                  value-from-input: <value in [disable, enable]>
                  values: <list or string>
          description: <string>
          match:
            -
              id: <integer>
              rules:
                -
                  case-sensitive: <value in [disable, enable]>
                  domains: <list or string>
                  header-name: <string>
                  id: <integer>
                  match-pattern: <value in [simple, substr, regexp]>
                  match-value: <string>
                  methods: <list or string>
                  negate: <value in [disable, enable]>
                  type: <value in [domains, host, path, ...]>
              strategy: <value in [or, and]>
          match-strategy: <value in [or, and]>
          name: <string>
          type: <value in [built-in, customized]>
          uuid: <string>
```

## [Return Values](fmgr_casb_useractivity_module.md#id6)

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
