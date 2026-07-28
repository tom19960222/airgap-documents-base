---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_system_log_settings module – Log settings."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_system_log_settings_module.html
fetched_at: 2026-07-28T02:19:06+00:00
---
# fortinet.fortimanager.fmgr_system_log_settings module – Log settings.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_log_settings`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_system_log_settings_module.md#synopsis)
- [Parameters](fmgr_system_log_settings_module.md#parameters)
- [Notes](fmgr_system_log_settings_module.md#notes)
- [Examples](fmgr_system_log_settings_module.md#examples)
- [Return Values](fmgr_system_log_settings_module.md#return-values)

## [Synopsis](fmgr_system_log_settings_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_log_settings_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **system_log_settings**  dictionary | the top level parameters set |
| **browse-max-logfiles**  integer | Maximum number of log files for each log browse attempt for each Adom. |
| **device-auto-detect**  string | Enable/Disable looking up device ID in syslog received with no encryption.  disable - Disable looking up device ID in syslog received with no encryption.  enable - Enable looking up device ID in syslog received with no encryption.  **Choices:**   - `"disable"` - `"enable"` |
| **dns-resolve-dstip**  string | Enable/Disable resolving destination IP by DNS.  disable - Disable resolving destination IP by DNS.  enable - Enable resolving destination IP by DNS.  **Choices:**   - `"disable"` - `"enable"` |
| **download-max-logs**  integer | Maximum number of logs for each log download attempt. |
| **FAC-custom-field1**  string | Name of custom log field to index. |
| **FAZ-custom-field1**  string | Name of custom log field to index. |
| **FCH-custom-field1**  string | Name of custom log field to index. |
| **FCT-custom-field1**  string | Name of custom log field to index. |
| **FDD-custom-field1**  string | Name of custom log field to index. |
| **FGT-custom-field1**  string | Name of custom log field to index. |
| **FMG-custom-field1**  string | Name of custom log field to index. |
| **FML-custom-field1**  string | Name of custom log field to index. |
| **FPX-custom-field1**  string | Name of custom log field to index. |
| **FSA-custom-field1**  string | Name of custom log field to index. |
| **FWB-custom-field1**  string | Name of custom log field to index. |
| **ha-auto-migrate**  string | Enabled/Disable automatically merging HA members logs to HA cluster.  disable - Disable automatically merging HA members logs to HA cluster.  enable - Enable automatically merging HA members logs to HA cluster.  **Choices:**   - `"disable"` - `"enable"` |
| **import-max-logfiles**  integer | Maximum number of log files for each log import attempt. |
| **keep-dev-logs**  string | Enable/Disable keeping the dev logs after the device has been deleted.  disable - Disable keeping the dev logs after the device has been deleted.  enable - Enable keeping the dev logs after the device has been deleted.  **Choices:**   - `"disable"` - `"enable"` |
| **log-file-archive-name**  string | Log file name format for archiving, such as backup, upload or download.  basic - Basic format for log archive file name, e.  extended - Extended format for log archive file name, e.  **Choices:**   - `"basic"` - `"extended"` |
| **rolling-analyzer**  dictionary | no description |
| **days**  list / elements=string | Log files rolling schedule  sun - Sunday.  mon - Monday.  tue - Tuesday.  wed - Wednesday.  thu - Thursday.  fri - Friday.  sat - Saturday.  **Choices:**   - `"sun"` - `"mon"` - `"tue"` - `"wed"` - `"thu"` - `"fri"` - `"sat"` |
| **del-files**  string | Enable/disable log file deletion after uploading.  disable - Disable log file deletion.  enable - Enable log file deletion.  **Choices:**   - `"disable"` - `"enable"` |
| **directory**  string | Upload server directory, for Unix server, use absolute |
| **file-size**  integer | Roll log files when they reach this size |
| **gzip-format**  string | Enable/disable compression of uploaded log files.  disable - Disable compression.  enable - Enable compression.  **Choices:**   - `"disable"` - `"enable"` |
| **hour**  integer | Log files rolling schedule |
| **ip**  string | Upload server IP address. |
| **ip2**  string | Upload server IP2 address. |
| **ip3**  string | Upload server IP3 address. |
| **log-format**  string | Format of uploaded log files.  native - Native format  text - Text format  csv - CSV  **Choices:**   - `"native"` - `"text"` - `"csv"` |
| **min**  integer | Log files rolling schedule |
| **password**  any | (list) Upload server login password. |
| **password2**  any | (list) Upload server login password2. |
| **password3**  any | (list) Upload server login password3. |
| **port**  integer | Upload server IP1 port number. |
| **port2**  integer | Upload server IP2 port number. |
| **port3**  integer | Upload server IP3 port number. |
| **rolling-upgrade-status**  integer | rolling upgrade status |
| **server**  string | Upload server FQDN/IP. |
| **server-type**  string | Upload server type.  ftp - Upload via FTP.  sftp - Upload via SFTP.  scp - Upload via SCP.  **Choices:**   - `"ftp"` - `"sftp"` - `"scp"` |
| **server2**  string | Upload server2 FQDN/IP. |
| **server3**  string | Upload server3 FQDN/IP. |
| **upload**  string | Enable/disable log file uploads.  disable - Disable log files uploading.  enable - Enable log files uploading.  **Choices:**   - `"disable"` - `"enable"` |
| **upload-hour**  integer | Log files upload schedule |
| **upload-mode**  string | Upload mode with multiple servers.  backup - Servers are attempted and used one after the other upon failure to connect.  mirror - All configured servers are attempted and used.  **Choices:**   - `"backup"` - `"mirror"` |
| **upload-trigger**  string | Event triggering log files upload.  on-roll - Upload log files after they are rolled.  on-schedule - Upload log files daily.  **Choices:**   - `"on-roll"` - `"on-schedule"` |
| **username**  string | Upload server login username. |
| **username2**  string | Upload server login username2. |
| **username3**  string | Upload server login username3. |
| **when**  string | Roll log files periodically.  none - Do not roll log files periodically.  daily - Roll log files daily.  weekly - Roll log files on certain days of week.  **Choices:**   - `"none"` - `"daily"` - `"weekly"` |
| **rolling-local**  dictionary | no description |
| **days**  list / elements=string | Log files rolling schedule  sun - Sunday.  mon - Monday.  tue - Tuesday.  wed - Wednesday.  thu - Thursday.  fri - Friday.  sat - Saturday.  **Choices:**   - `"sun"` - `"mon"` - `"tue"` - `"wed"` - `"thu"` - `"fri"` - `"sat"` |
| **del-files**  string | Enable/disable log file deletion after uploading.  disable - Disable log file deletion.  enable - Enable log file deletion.  **Choices:**   - `"disable"` - `"enable"` |
| **directory**  string | Upload server directory, for Unix server, use absolute |
| **file-size**  integer | Roll log files when they reach this size |
| **gzip-format**  string | Enable/disable compression of uploaded log files.  disable - Disable compression.  enable - Enable compression.  **Choices:**   - `"disable"` - `"enable"` |
| **hour**  integer | Log files rolling schedule |
| **ip**  string | Upload server IP address. |
| **ip2**  string | Upload server IP2 address. |
| **ip3**  string | Upload server IP3 address. |
| **log-format**  string | Format of uploaded log files.  native - Native format  text - Text format  csv - CSV  **Choices:**   - `"native"` - `"text"` - `"csv"` |
| **min**  integer | Log files rolling schedule |
| **password**  any | (list) Upload server login password. |
| **password2**  any | (list) Upload server login password2. |
| **password3**  any | (list) Upload server login password3. |
| **port**  integer | Upload server IP1 port number. |
| **port2**  integer | Upload server IP2 port number. |
| **port3**  integer | Upload server IP3 port number. |
| **rolling-upgrade-status**  integer | rolling upgrade status |
| **server**  string | Upload server FQDN/IP. |
| **server-type**  string | Upload server type.  ftp - Upload via FTP.  sftp - Upload via SFTP.  scp - Upload via SCP.  **Choices:**   - `"ftp"` - `"sftp"` - `"scp"` |
| **server2**  string | Upload server2 FQDN/IP. |
| **server3**  string | Upload server3 FQDN/IP. |
| **upload**  string | Enable/disable log file uploads.  disable - Disable log files uploading.  enable - Enable log files uploading.  **Choices:**   - `"disable"` - `"enable"` |
| **upload-hour**  integer | Log files upload schedule |
| **upload-mode**  string | Upload mode with multiple servers.  backup - Servers are attempted and used one after the other upon failure to connect.  mirror - All configured servers are attempted and used.  **Choices:**   - `"backup"` - `"mirror"` |
| **upload-trigger**  string | Event triggering log files upload.  on-roll - Upload log files after they are rolled.  on-schedule - Upload log files daily.  **Choices:**   - `"on-roll"` - `"on-schedule"` |
| **username**  string | Upload server login username. |
| **username2**  string | Upload server login username2. |
| **username3**  string | Upload server login username3. |
| **when**  string | Roll log files periodically.  none - Do not roll log files periodically.  daily - Roll log files daily.  weekly - Roll log files on certain days of week.  **Choices:**   - `"none"` - `"daily"` - `"weekly"` |
| **rolling-regular**  dictionary | no description |
| **days**  list / elements=string | Log files rolling schedule  sun - Sunday.  mon - Monday.  tue - Tuesday.  wed - Wednesday.  thu - Thursday.  fri - Friday.  sat - Saturday.  **Choices:**   - `"sun"` - `"mon"` - `"tue"` - `"wed"` - `"thu"` - `"fri"` - `"sat"` |
| **del-files**  string | Enable/disable log file deletion after uploading.  disable - Disable log file deletion.  enable - Enable log file deletion.  **Choices:**   - `"disable"` - `"enable"` |
| **directory**  string | Upload server directory, for Unix server, use absolute |
| **file-size**  integer | Roll log files when they reach this size |
| **gzip-format**  string | Enable/disable compression of uploaded log files.  disable - Disable compression.  enable - Enable compression.  **Choices:**   - `"disable"` - `"enable"` |
| **hour**  integer | Log files rolling schedule |
| **ip**  string | Upload server IP address. |
| **ip2**  string | Upload server IP2 address. |
| **ip3**  string | Upload server IP3 address. |
| **log-format**  string | Format of uploaded log files.  native - Native format  text - Text format  csv - CSV  **Choices:**   - `"native"` - `"text"` - `"csv"` |
| **min**  integer | Log files rolling schedule |
| **password**  any | (list) Upload server login password. |
| **password2**  any | (list) Upload server login password2. |
| **password3**  any | (list) Upload server login password3. |
| **port**  integer | Upload server IP1 port number. |
| **port2**  integer | Upload server IP2 port number. |
| **port3**  integer | Upload server IP3 port number. |
| **rolling-upgrade-status**  integer | rolling upgrade status |
| **server**  string | Upload server FQDN/IP. |
| **server-type**  string | Upload server type.  ftp - Upload via FTP.  sftp - Upload via SFTP.  scp - Upload via SCP.  **Choices:**   - `"ftp"` - `"sftp"` - `"scp"` |
| **server2**  string | Upload server2 FQDN/IP. |
| **server3**  string | Upload server3 FQDN/IP. |
| **upload**  string | Enable/disable log file uploads.  disable - Disable log files uploading.  enable - Enable log files uploading.  **Choices:**   - `"disable"` - `"enable"` |
| **upload-hour**  integer | Log files upload schedule |
| **upload-mode**  string | Upload mode with multiple servers.  backup - Servers are attempted and used one after the other upon failure to connect.  mirror - All configured servers are attempted and used.  **Choices:**   - `"backup"` - `"mirror"` |
| **upload-trigger**  string | Event triggering log files upload.  on-roll - Upload log files after they are rolled.  on-schedule - Upload log files daily.  **Choices:**   - `"on-roll"` - `"on-schedule"` |
| **username**  string | Upload server login username. |
| **username2**  string | Upload server login username2. |
| **username3**  string | Upload server login username3. |
| **when**  string | Roll log files periodically.  none - Do not roll log files periodically.  daily - Roll log files daily.  weekly - Roll log files on certain days of week.  **Choices:**   - `"none"` - `"daily"` - `"weekly"` |
| **sync-search-timeout**  integer | Maximum number of seconds for running a log search session in synchronous mode. |
| **unencrypted-logging**  string | Enable/Disable receiving syslog through UDP  disable - Disable receiving syslog through UDP  enable - Enable receiving syslog through UDP  **Choices:**   - `"disable"` - `"enable"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_system_log_settings_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_log_settings_module.md#id4)

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
    - name: Log settings.
      fmgr_system_log_settings:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        system_log_settings:
          FAC-custom-field1: <string>
          FAZ-custom-field1: <string>
          FCH-custom-field1: <string>
          FCT-custom-field1: <string>
          FDD-custom-field1: <string>
          FGT-custom-field1: <string>
          FMG-custom-field1: <string>
          FML-custom-field1: <string>
          FPX-custom-field1: <string>
          FSA-custom-field1: <string>
          FWB-custom-field1: <string>
          browse-max-logfiles: <integer>
          dns-resolve-dstip: <value in [disable, enable]>
          download-max-logs: <integer>
          ha-auto-migrate: <value in [disable, enable]>
          import-max-logfiles: <integer>
          log-file-archive-name: <value in [basic, extended]>
          rolling-analyzer:
            days:
              - sun
              - mon
              - tue
              - wed
              - thu
              - fri
              - sat
            del-files: <value in [disable, enable]>
            directory: <string>
            file-size: <integer>
            gzip-format: <value in [disable, enable]>
            hour: <integer>
            ip: <string>
            ip2: <string>
            ip3: <string>
            log-format: <value in [native, text, csv]>
            min: <integer>
            password: <list or string>
            password2: <list or string>
            password3: <list or string>
            server-type: <value in [ftp, sftp, scp]>
            upload: <value in [disable, enable]>
            upload-hour: <integer>
            upload-mode: <value in [backup, mirror]>
            upload-trigger: <value in [on-roll, on-schedule]>
            username: <string>
            username2: <string>
            username3: <string>
            when: <value in [none, daily, weekly]>
            port: <integer>
            port2: <integer>
            port3: <integer>
            rolling-upgrade-status: <integer>
            server: <string>
            server2: <string>
            server3: <string>
          rolling-local:
            days:
              - sun
              - mon
              - tue
              - wed
              - thu
              - fri
              - sat
            del-files: <value in [disable, enable]>
            directory: <string>
            file-size: <integer>
            gzip-format: <value in [disable, enable]>
            hour: <integer>
            ip: <string>
            ip2: <string>
            ip3: <string>
            log-format: <value in [native, text, csv]>
            min: <integer>
            password: <list or string>
            password2: <list or string>
            password3: <list or string>
            server-type: <value in [ftp, sftp, scp]>
            upload: <value in [disable, enable]>
            upload-hour: <integer>
            upload-mode: <value in [backup, mirror]>
            upload-trigger: <value in [on-roll, on-schedule]>
            username: <string>
            username2: <string>
            username3: <string>
            when: <value in [none, daily, weekly]>
            port: <integer>
            port2: <integer>
            port3: <integer>
            rolling-upgrade-status: <integer>
            server: <string>
            server2: <string>
            server3: <string>
          rolling-regular:
            days:
              - sun
              - mon
              - tue
              - wed
              - thu
              - fri
              - sat
            del-files: <value in [disable, enable]>
            directory: <string>
            file-size: <integer>
            gzip-format: <value in [disable, enable]>
            hour: <integer>
            ip: <string>
            ip2: <string>
            ip3: <string>
            log-format: <value in [native, text, csv]>
            min: <integer>
            password: <list or string>
            password2: <list or string>
            password3: <list or string>
            server-type: <value in [ftp, sftp, scp]>
            upload: <value in [disable, enable]>
            upload-hour: <integer>
            upload-mode: <value in [backup, mirror]>
            upload-trigger: <value in [on-roll, on-schedule]>
            username: <string>
            username2: <string>
            username3: <string>
            when: <value in [none, daily, weekly]>
            port: <integer>
            port2: <integer>
            port3: <integer>
            rolling-upgrade-status: <integer>
            server: <string>
            server2: <string>
            server3: <string>
          sync-search-timeout: <integer>
          keep-dev-logs: <value in [disable, enable]>
          device-auto-detect: <value in [disable, enable]>
          unencrypted-logging: <value in [disable, enable]>
```

## [Return Values](fmgr_system_log_settings_module.md#id5)

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
