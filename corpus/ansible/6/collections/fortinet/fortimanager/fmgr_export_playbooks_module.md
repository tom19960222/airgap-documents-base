---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_export_playbooks module – Export fortimanager configuration as playbooks."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_export_playbooks_module.html
fetched_at: 2026-07-27T17:30:25+00:00
---
# fortinet.fortimanager.fmgr_export_playbooks module – Export fortimanager configuration as playbooks.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_export_playbooks`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_export_playbooks_module.md#synopsis)
- [Parameters](fmgr_export_playbooks_module.md#parameters)
- [Notes](fmgr_export_playbooks_module.md#notes)
- [Examples](fmgr_export_playbooks_module.md#examples)
- [Return Values](fmgr_export_playbooks_module.md#return-values)

## [Synopsis](fmgr_export_playbooks_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_export_playbooks_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **export_playbooks**  dictionary | the top level parameters set |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_export_playbooks_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_export_playbooks_module.md#id4)

```yaml+jinja
- name: gathering fortimanager facts
  hosts: fortimanager00
  gather_facts: no
  connection: httpapi
  collections:
    - fortinet.fortimanager
  vars:
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_port: 443
  tasks:
   - name: Export Playbooks
     fmgr_export_playbooks:
        export_playbooks:
            selector:
                - all
            path: './exported'
            params:
                all:
                  adom: root
```

## [Return Values](fmgr_export_playbooks_module.md#id5)

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
