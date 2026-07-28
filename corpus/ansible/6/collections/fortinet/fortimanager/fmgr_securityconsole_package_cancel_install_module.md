---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_securityconsole_package_cancel_install module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_securityconsole_package_cancel_install_module.html
fetched_at: 2026-07-27T17:34:41+00:00
---
# fortinet.fortimanager.fmgr_securityconsole_package_cancel_install module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_securityconsole_package_cancel_install`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_securityconsole_package_cancel_install_module.md#synopsis)
- [Parameters](fmgr_securityconsole_package_cancel_install_module.md#parameters)
- [Notes](fmgr_securityconsole_package_cancel_install_module.md#notes)
- [Examples](fmgr_securityconsole_package_cancel_install_module.md#examples)
- [Return Values](fmgr_securityconsole_package_cancel_install_module.md#return-values)

## [Synopsis](fmgr_securityconsole_package_cancel_install_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_securityconsole_package_cancel_install_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **securityconsole_package_cancel_install**  dictionary | the top level parameters set |
| **adom**  string | no description |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_securityconsole_package_cancel_install_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_securityconsole_package_cancel_install_module.md#id4)

```yaml+jinja
- name: INSTALL PREVIEW - POLICY PACKAGE
  hosts: fmg
  connection: httpapi
  collections: fortinet.fortimanager
  vars:
    adom: demo
    ppkg: ppkg_hubs
    device: fgt_00_1
  tasks:
    - name: Install for policy package {{ adom }}/{{ ppkg }} [preview mode]
      fmgr_securityconsole_install_package:
        securityconsole_install_package:
          adom: "{{ adom }}"
          flags:
             - preview
          pkg: "{{ ppkg }}"
          scope:
            - name: "{{ device }}"
              vdom: root
      register: r
    - name: Poll the task
      fmgr_fact:
        facts:
          selector: 'task_task'
          params:
            task: '{{ r.meta.response_data.task }}'
      register: taskinfo
      until: taskinfo.meta.response_data.percent == 100
      retries: 30
      delay: 5
    - name: Trigger the preview report generation for policy package {{ adom }}/{{ ppkg }}
      fmgr_securityconsole_install_preview:
        securityconsole_install_preview:
          adom: "{{ adom }}"
          device: "{{ device }}"
          flags:
            - json
          vdoms: root
      register: r
    - name: Poll the task
      fmgr_fact:
        facts:
          selector: 'task_task'
          params:
            task: '{{ r.meta.response_data.task }}'
      register: taskinfo
      until: taskinfo.meta.response_data.percent == 100
      retries: 30
      delay: 5
    - name: Get the preview report for policy package {{ adom }}/{{ ppkg }}
      fmgr_securityconsole_preview_result:
        securityconsole_preview_result:
           adom: "{{ adom }}"
           device: "{{ device }}"
      register: r
    - name: Cancel install task for policy package {{ adom }}/{{ ppkg }}
      fmgr_securityconsole_package_cancel_install:
        securityconsole_package_cancel_install:
          adom: "{{ adom }}"
    - name: Show preview report
      debug:
        msg: "{{ r }}"
```

## [Return Values](fmgr_securityconsole_package_cancel_install_module.md#id5)

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
