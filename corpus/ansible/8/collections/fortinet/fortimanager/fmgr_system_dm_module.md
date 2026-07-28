---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_system_dm module – Configure dm."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_system_dm_module.html
fetched_at: 2026-07-28T02:18:28+00:00
---
# fortinet.fortimanager.fmgr_system_dm module – Configure dm.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_dm`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_system_dm_module.md#synopsis)
- [Parameters](fmgr_system_dm_module.md#parameters)
- [Notes](fmgr_system_dm_module.md#notes)
- [Examples](fmgr_system_dm_module.md#examples)
- [Return Values](fmgr_system_dm_module.md#return-values)

## [Synopsis](fmgr_system_dm_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_dm_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **system_dm**  dictionary | the top level parameters set |
| **concurrent-install-image-limit**  integer | Maximum number of concurrent install image |
| **concurrent-install-limit**  integer | Maximum number of concurrent installs |
| **concurrent-install-script-limit**  integer | Maximum number of concurrent install scripts |
| **conf-merge-after-script**  string | Merge config after run script on remote device, instead of full retrieve.  disable - Disable.  enable - Enable.  **Choices:**   - `"disable"` - `"enable"` |
| **discover-timeout**  integer | Check connection timeout when discover device |
| **dpm-logsize**  integer | Maximum dpm log size per device |
| **fgfm-auto-retrieve-timeout**  integer | Maximum waiting time for auto retrieve |
| **fgfm-install-refresh-count**  integer | Maximum FGFM install refresh attempt. |
| **fgfm-sock-timeout**  integer | Maximum FGFM socket idle time |
| **fgfm_keepalive_itvl**  integer | FGFM protocol keep alive interval |
| **force-remote-diff**  string | Always use remote diff when installing.  disable - Disable.  enable - Enable.  **Choices:**   - `"disable"` - `"enable"` |
| **fortiap-refresh-cnt**  integer | Max auto refresh FortiAP number each time |
| **fortiap-refresh-itvl**  integer | Auto refresh FortiAP status interval |
| **fortiext-refresh-cnt**  integer | Max device number for FortiExtender auto refresh |
| **install-fds-timeout**  integer | Maximum waiting time for fgt update during install |
| **install-image-timeout**  integer | Maximum waiting time for image transfer and device upgrade |
| **install-tunnel-retry-itvl**  integer | Time to re-establish tunnel during install |
| **log-autoupdate**  string | Enable/disable autoupdate debug logging.  disable - Disable.  enable - Enable.  **Choices:**   - `"disable"` - `"enable"` |
| **max-revs**  integer | Maximum number of revisions saved |
| **nr-retry**  integer | Number of retries. |
| **retry**  string | Enable/disable configuration install retry.  disable - Disable.  enable - Enable.  **Choices:**   - `"disable"` - `"enable"` |
| **retry-intvl**  integer | Retry interval. |
| **rollback-allow-reboot**  string | Enable/disable FortiGate reboot to rollback when installing script/config.  disable - Disable.  enable - Enable.  **Choices:**   - `"disable"` - `"enable"` |
| **script-logsize**  integer | Maximum script log size per device |
| **skip-scep-check**  string | Enable/disable installing scep related objects even if scep url is configured.  disable - Disable.  enable - Enable.  **Choices:**   - `"disable"` - `"enable"` |
| **skip-tunnel-fcp-req**  string | Enable/disable skip the fcp request sent from fgfm tunnel  disable - Disable.  enable - Enable.  **Choices:**   - `"disable"` - `"enable"` |
| **verify-install**  string | Verify install against remote configuration.  disable - Disable.  optimal - Verify installation for command errors.  enable - Always verify installation.  **Choices:**   - `"disable"` - `"optimal"` - `"enable"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_system_dm_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_dm_module.md#id4)

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
    - name: Configure dm.
      fmgr_system_dm:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        system_dm:
          concurrent-install-image-limit: <integer>
          concurrent-install-limit: <integer>
          concurrent-install-script-limit: <integer>
          discover-timeout: <integer>
          dpm-logsize: <integer>
          fgfm-sock-timeout: <integer>
          fgfm_keepalive_itvl: <integer>
          force-remote-diff: <value in [disable, enable]>
          fortiap-refresh-cnt: <integer>
          fortiap-refresh-itvl: <integer>
          fortiext-refresh-cnt: <integer>
          install-image-timeout: <integer>
          install-tunnel-retry-itvl: <integer>
          max-revs: <integer>
          nr-retry: <integer>
          retry: <value in [disable, enable]>
          retry-intvl: <integer>
          rollback-allow-reboot: <value in [disable, enable]>
          script-logsize: <integer>
          skip-scep-check: <value in [disable, enable]>
          skip-tunnel-fcp-req: <value in [disable, enable]>
          verify-install: <value in [disable, optimal, enable]>
          fgfm-install-refresh-count: <integer>
          conf-merge-after-script: <value in [disable, enable]>
          log-autoupdate: <value in [disable, enable]>
          fgfm-auto-retrieve-timeout: <integer>
          install-fds-timeout: <integer>
```

## [Return Values](fmgr_system_dm_module.md#id5)

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
