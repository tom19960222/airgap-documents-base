---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_system_global module – Global range attributes."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_system_global_module.html
fetched_at: 2026-07-28T02:18:37+00:00
---
# fortinet.fortimanager.fmgr_system_global module – Global range attributes.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_global`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_system_global_module.md#synopsis)
- [Parameters](fmgr_system_global_module.md#parameters)
- [Notes](fmgr_system_global_module.md#notes)
- [Examples](fmgr_system_global_module.md#examples)
- [Return Values](fmgr_system_global_module.md#return-values)

## [Synopsis](fmgr_system_global_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **system_global**  dictionary | the top level parameters set |
| **admin-lockout-duration**  integer | Lockout duration |
| **admin-lockout-method**  string | Lockout method for administration.  ip - Lockout by IP  user - Lockout by user  **Choices:**   - `"ip"` - `"user"` |
| **admin-lockout-threshold**  integer | Lockout threshold for administration. |
| **adom-mode**  string | ADOM mode.  normal - Normal ADOM mode.  advanced - Advanced ADOM mode.  **Choices:**   - `"normal"` - `"advanced"` |
| **adom-rev-auto-delete**  string | Auto delete features for old ADOM revisions.  disable - Disable auto delete function for ADOM revision.  by-revisions - Auto delete ADOM revisions by maximum number of revisions.  by-days - Auto delete ADOM revisions by maximum days.  **Choices:**   - `"disable"` - `"by-revisions"` - `"by-days"` |
| **adom-rev-max-backup-revisions**  integer | Maximum number of ADOM revisions to backup. |
| **adom-rev-max-days**  integer | Number of days to keep old ADOM revisions. |
| **adom-rev-max-revisions**  integer | Maximum number of ADOM revisions to keep. |
| **adom-select**  string | Enable/disable select ADOM after login.  disable - Disable select ADOM after login.  enable - Enable select ADOM after login.  **Choices:**   - `"disable"` - `"enable"` |
| **adom-status**  string | ADOM status.  disable - Disable ADOM mode.  enable - Enable ADOM mode.  **Choices:**   - `"disable"` - `"enable"` |
| **apache-mode**  string | Set apache mode.  event - Apache event mode.  prefork - Apache prefork mode.  **Choices:**   - `"event"` - `"prefork"` |
| **clone-name-option**  string | set the clone object names option.  default - Add a prefix of Clone of to the clone name.  keep - Keep the original name for user to edit.  **Choices:**   - `"default"` - `"keep"` |
| **clt-cert-req**  string | Require client certificate for GUI login.  disable - Disable setting.  enable - Require client certificate for GUI login.  optional - Optional client certificate for GUI login.  **Choices:**   - `"disable"` - `"enable"` - `"optional"` |
| **console-output**  string | Console output mode.  standard - Standard output.  more - More page output.  **Choices:**   - `"standard"` - `"more"` |
| **contentpack-fgt-install**  string | Enable/disable outbreak alert auto install for FGT ADOMS .  disable - Disable the sql report auto outbreak auto install.  enable - Enable the sql report auto outbreak auto install.  **Choices:**   - `"disable"` - `"enable"` |
| **country-flag**  string | Country flag Status.  disable - Disable country flag icon beside ip address.  enable - Enable country flag icon beside ip address.  **Choices:**   - `"disable"` - `"enable"` |
| **create-revision**  string | Enable/disable create revision by default.  disable - Disable create revision by default.  enable - Enable create revision by default.  **Choices:**   - `"disable"` - `"enable"` |
| **daylightsavetime**  string | Enable/disable daylight saving time.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **default-disk-quota**  integer | Default disk quota for registered device |
| **detect-unregistered-log-device**  string | Detect unregistered logging device from log message.  disable - Disable attribute function.  enable - Enable attribute function.  **Choices:**   - `"disable"` - `"enable"` |
| **device-view-mode**  string | Set devices/groups view mode.  regular - Regular view mode.  tree - Tree view mode.  **Choices:**   - `"regular"` - `"tree"` |
| **dh-params**  string | Minimum size of Diffie-Hellman prime for SSH/HTTPS  1024 - 1024 bits.  1536 - 1536 bits.  2048 - 2048 bits.  3072 - 3072 bits.  4096 - 4096 bits.  6144 - 6144 bits.  8192 - 8192 bits.  **Choices:**   - `"1024"` - `"1536"` - `"2048"` - `"3072"` - `"4096"` - `"6144"` - `"8192"` |
| **disable-module**  list / elements=string | Disable module list.  fortiview-noc - FortiView/NOC-SOC module.  fortirecorder - FortiRecorder module.  siem - SIEM module.  soc - SOC module.  ai - AI module.  **Choices:**   - `"fortiview-noc"` - `"none"` - `"fortirecorder"` - `"siem"` - `"soc"` - `"ai"` |
| **enc-algorithm**  string | SSL communication encryption algorithms.  low - SSL communication using all available encryption algorithms.  medium - SSL communication using high and medium encryption algorithms.  high - SSL communication using high encryption algorithms.  **Choices:**   - `"low"` - `"medium"` - `"high"` - `"custom"` |
| **faz-status**  string | FAZ status.  disable - Disable FAZ feature.  enable - Enable FAZ feature.  **Choices:**   - `"disable"` - `"enable"` |
| **fgfm-ca-cert**  string | set the extra fgfm CA certificates. |
| **fgfm-cert-exclusive**  string | set if the local or CA certificates should be used exclusively.  disable - Used certificate best-effort.  enable - Used certificate exclusive.  **Choices:**   - `"disable"` - `"enable"` |
| **fgfm-local-cert**  string | set the fgfm local certificate. |
| **fgfm-ssl-protocol**  string | set the lowest SSL protocols for fgfmsd.  sslv3 - set SSLv3 as the lowest version.  tlsv1.  tlsv1.  tlsv1.  **Choices:**   - `"sslv3"` - `"tlsv1.0"` - `"tlsv1.1"` - `"tlsv1.2"` - `"tlsv1.3"` |
| **fortiservice-port**  integer | FortiService port |
| **gui-curl-timeout**  integer | GUI curl timeout in seconds |
| **gui-polling-interval**  integer | GUI polling interval in seconds |
| **ha-member-auto-grouping**  string | Enable/disable automatically group HA members feature  disable - Disable automatically grouping HA members feature.  enable - Enable automatically grouping HA members only when group name is unique in your network.  **Choices:**   - `"disable"` - `"enable"` |
| **hitcount_concurrent**  integer | The number of FortiGates that FortiManager polls at one time |
| **hitcount_interval**  integer | The interval for getting hit count from managed FortiGate devices, in seconds |
| **hostname**  string | System hostname. |
| **import-ignore-addr-cmt**  string | Enable/Disable import ignore of address comments.  disable - Disable import ignore of address comments.  enable - Enable import ignore of address comments.  **Choices:**   - `"disable"` - `"enable"` |
| **language**  string | System global language.  english - English  simch - Simplified Chinese  japanese - Japanese  korean - Korean  spanish - Spanish  trach - Traditional Chinese  **Choices:**   - `"english"` - `"simch"` - `"japanese"` - `"korean"` - `"spanish"` - `"trach"` |
| **latitude**  string | fmg location latitude |
| **ldap-cache-timeout**  integer | LDAP browser cache timeout |
| **ldapconntimeout**  integer | LDAP connection timeout |
| **lock-preempt**  string | Enable/disable ADOM lock override.  disable - Disable lock preempt.  enable - Enable lock preempt.  **Choices:**   - `"disable"` - `"enable"` |
| **log-checksum**  string | Record log file hash value, timestamp, and authentication code at transmission or rolling.  none - No record log file checksum.  md5 - Record log files MD5 hash value only.  md5-auth - Record log files MD5 hash value and authentication code.  **Choices:**   - `"none"` - `"md5"` - `"md5-auth"` |
| **log-checksum-upload**  string | Enable/disable upload log checksum with log files.  disable - Disable attribute function.  enable - Enable attribute function.  **Choices:**   - `"disable"` - `"enable"` |
| **log-forward-cache-size**  integer | Log forwarding disk cache size |
| **longitude**  string | fmg location longitude |
| **management-ip**  string | Management IP address of this FortiGate. |
| **management-port**  integer | Overriding port for management connection |
| **max-log-forward**  integer | Maximum number of log-forward and aggregation settings. |
| **max-running-reports**  integer | Maximum number of reports generating at one time. |
| **mc-policy-disabled-adoms**  list / elements=dictionary | Mc-Policy-Disabled-Adoms. |
| **adom-name**  string | Adom names. |
| **multiple-steps-upgrade-in-autolink**  string | Enable/disable multiple steps upgade in autolink process  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **no-copy-permission-check**  string | Do not perform permission check to block object changes in different adom during copy and install.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **no-vip-value-check**  string | Enable/disable skipping policy instead of throwing error when vip has no default or dynamic mapping during policy copy  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **normalized-intf-zone-only**  string | allow normalized interface to be zone only.  disable - Disable SSL low-grade encryption.  enable - Enable SSL low-grade encryption.  **Choices:**   - `"disable"` - `"enable"` |
| **object-revision-db-max**  integer | Maximum revisions for a single database |
| **object-revision-mandatory-note**  string | Enable/disable mandatory note when create revision.  disable - Disable object revision.  enable - Enable object revision.  **Choices:**   - `"disable"` - `"enable"` |
| **object-revision-object-max**  integer | Maximum revisions for a single object |
| **object-revision-status**  string | Enable/disable create revision when modify objects.  disable - Disable object revision.  enable - Enable object revision.  **Choices:**   - `"disable"` - `"enable"` |
| **oftp-ssl-protocol**  string | set the lowest SSL protocols for oftpd.  sslv3 - set SSLv3 as the lowest version.  tlsv1.  tlsv1.  tlsv1.  **Choices:**   - `"sslv3"` - `"tlsv1.0"` - `"tlsv1.1"` - `"tlsv1.2"` - `"tlsv1.3"` |
| **partial-install**  string | Enable/Disable partial install  disable - Disable partial install function.  enable - Enable partial install function.  **Choices:**   - `"disable"` - `"enable"` |
| **partial-install-force**  string | Enable/Disable partial install when devdb is modified.  disable - Disable partial install when devdb is modified.  enable - Enable partial install when devdb is modified.  **Choices:**   - `"disable"` - `"enable"` |
| **partial-install-rev**  string | Enable/Disable auto creating adom revision for partial install.  disable - Disable partial install revision.  enable - Enable partial install revision.  **Choices:**   - `"disable"` - `"enable"` |
| **per-policy-lock**  string | Enable/Disable per policy lock.  disable - Disable per policy lock.  enable - Enable per policy lock.  **Choices:**   - `"disable"` - `"enable"` |
| **perform-improve-by-ha**  string | Enable/Disable performance improvement by distributing tasks to HA slaves.  disable - Disable performance improvement by HA.  enable - Enable performance improvement by HA.  **Choices:**   - `"disable"` - `"enable"` |
| **policy-hit-count**  string | show policy hit count.  disable - Disable policy hit count.  enable - Enable policy hit count.  **Choices:**   - `"disable"` - `"enable"` |
| **policy-object-icon**  string | show icons of policy objects.  disable - Disable icon of policy objects.  enable - Enable icon of policy objects.  **Choices:**   - `"disable"` - `"enable"` |
| **policy-object-in-dual-pane**  string | show policies and objects in dual pane.  disable - Disable polices and objects in dual pane.  enable - Enable polices and objects in dual pane.  **Choices:**   - `"disable"` - `"enable"` |
| **pre-login-banner**  string | Enable/disable pre-login banner.  disable - Disable pre-login banner.  enable - Enable pre-login banner.  **Choices:**   - `"disable"` - `"enable"` |
| **pre-login-banner-message**  string | Pre-login banner message. |
| **private-data-encryption**  string | Enable/disable private data encryption using an AES 128-bit key.  disable - Disable private data encryption using an AES 128-bit key.  enable - Enable private data encryption using an AES 128-bit key.  **Choices:**   - `"disable"` - `"enable"` |
| **remoteauthtimeout**  integer | Remote authentication |
| **save-last-hit-in-adomdb**  string | Enable/Disable save last-hit value in adomdb.  disable - Disable save last-hit value in adomdb.  enable - Enable save last-hit value in adomdb.  **Choices:**   - `"disable"` - `"enable"` |
| **search-all-adoms**  string | Enable/Disable Search all ADOMs for where-used query.  disable - Disable search all ADOMs for where-used queries.  enable - Enable search all ADOMs for where-used queries.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-cipher-suites**  list / elements=dictionary | no description |
| **cipher**  string | Cipher name |
| **priority**  integer | SSL/TLS cipher suites priority. |
| **version**  string | SSL/TLS version the cipher suite can be used with.  tls1.  tls1.  **Choices:**   - `"tls1.2-or-below"` - `"tls1.3"` |
| **ssl-low-encryption**  string | SSL low-grade encryption.  disable - Disable SSL low-grade encryption.  enable - Enable SSL low-grade encryption.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-protocol**  list / elements=string | SSL protocols.  tlsv1.  tlsv1.  tlsv1.  tlsv1.  sslv3 - Enable SSLv3.  **Choices:**   - `"tlsv1.2"` - `"tlsv1.1"` - `"tlsv1.0"` - `"sslv3"` - `"tlsv1.3"` |
| **ssl-static-key-ciphers**  string | Enable/disable SSL static key ciphers.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **table-entry-blink**  string | Enable/disable table entry blink in GUI  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **task-list-size**  integer | Maximum number of completed tasks to keep. |
| **tftp**  string | Enable/disable TFTP in `exec restore image` command  disable - Disable TFTP  enable - Enable TFTP  **Choices:**   - `"disable"` - `"enable"` |
| **timezone**  string | Time zone.  00 -  01 -  02 -  03 -  04 -  05 -  06 -  07 -  08 -  09 -  10 -  11 -  12 -  13 -  14 -  15 -  16 -  17 -  18 -  19 -  20 -  21 -  22 -  23 -  24 -  25 -  26 -  27 -  28 -  29 -  30 -  31 -  32 -  33 -  34 -  35 -  36 -  37 -  38 -  39 -  40 -  41 -  42 -  43 -  44 -  45 -  46 -  47 -  48 -  49 -  50 -  51 -  52 -  53 -  54 -  55 -  56 -  57 -  58 -  59 -  60 -  61 -  62 -  63 -  64 -  65 -  66 -  67 -  68 -  69 -  70 -  71 -  72 -  73 -  74 -  75 -  76 -  77 -  78 -  79 -  80 -  81 -  82 -  83 -  84 -  85 -  86 -  87 -  88 -  89 -  **Choices:**   - `"00"` - `"01"` - `"02"` - `"03"` - `"04"` - `"05"` - `"06"` - `"07"` - `"08"` - `"09"` - `"10"` - `"11"` - `"12"` - `"13"` - `"14"` - `"15"` - `"16"` - `"17"` - `"18"` - `"19"` - `"20"` - `"21"` - `"22"` - `"23"` - `"24"` - `"25"` - `"26"` - `"27"` - `"28"` - `"29"` - `"30"` - `"31"` - `"32"` - `"33"` - `"34"` - `"35"` - `"36"` - `"37"` - `"38"` - `"39"` - `"40"` - `"41"` - `"42"` - `"43"` - `"44"` - `"45"` - `"46"` - `"47"` - `"48"` - `"49"` - `"50"` - `"51"` - `"52"` - `"53"` - `"54"` - `"55"` - `"56"` - `"57"` - `"58"` - `"59"` - `"60"` - `"61"` - `"62"` - `"63"` - `"64"` - `"65"` - `"66"` - `"67"` - `"68"` - `"69"` - `"70"` - `"71"` - `"72"` - `"73"` - `"74"` - `"75"` - `"76"` - `"77"` - `"78"` - `"79"` - `"80"` - `"81"` - `"82"` - `"83"` - `"84"` - `"85"` - `"86"` - `"87"` - `"88"` - `"89"` - `"90"` - `"91"` |
| **tunnel-mtu**  integer | Maximum transportation unit |
| **usg**  string | Enable/disable Fortiguard server restriction.  disable - Contact any Fortiguard server  enable - Contact Fortiguard server in USA only  **Choices:**   - `"disable"` - `"enable"` |
| **vdom-mirror**  string | VDOM mirror.  disable - Disable VDOM mirror function.  enable - Enable VDOM mirror function.  **Choices:**   - `"disable"` - `"enable"` |
| **webservice-proto**  list / elements=string | Web Service connection support SSL protocols.  tlsv1.  tlsv1.  tlsv1.  tlsv1.  sslv3 - Web Service connection using SSLv3 protocol.  sslv2 - Web Service connection using SSLv2 protocol.  **Choices:**   - `"tlsv1.2"` - `"tlsv1.1"` - `"tlsv1.0"` - `"sslv3"` - `"sslv2"` - `"tlsv1.3"` |
| **workflow-max-sessions**  integer | Maximum number of workflow sessions per ADOM |
| **workspace-mode**  string | Set workspace mode  disabled - Workspace disabled.  normal - Workspace lock mode.  workflow - Workspace workflow mode.  **Choices:**   - `"disabled"` - `"normal"` - `"workflow"` - `"per-adom"` |
| **workspace-unlock-after-install**  string | Enable/disable ADOM auto-unlock after device installation.  disable - Disable automatically unlock adom after device installation.  enable - Enable automatically unlock adom after device installation.  **Choices:**   - `"disable"` - `"enable"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_system_global_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_global_module.md#id4)

```yaml+jinja
- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: enable workspace mode
     fmgr_system_global:
        system_global:
             adom-status: enable
             workspace-mode: normal

   - name: Script table.
     fmgr_dvmdb_script:
        bypass_validation: False
        adom: root
        state: present
        workspace_locking_adom: 'root'
        dvmdb_script:
           content: 'ansiblt-test'
           name: 'fooscript000'
           target: device_database
           type: cli

   - name: verify script table
     fmgr_fact:
        facts:
           selector: 'dvmdb_script'
           params:
               adom: 'root'
               script: 'fooscript000'
     register: info
     failed_when: info.meta.response_code != 0

   - name: restore workspace mode
     fmgr_system_global:
        system_global:
            adom-status: enable
            workspace-mode: disabled
```

## [Return Values](fmgr_system_global_module.md#id5)

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
