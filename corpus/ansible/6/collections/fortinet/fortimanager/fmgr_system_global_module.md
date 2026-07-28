---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_system_global module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_system_global_module.html
fetched_at: 2026-07-27T17:36:08+00:00
---
# fortinet.fortimanager.fmgr_system_global module – no description

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
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **system_global**  dictionary | the top level parameters set |
| **admin-lockout-duration**  integer | no description  Default: `60` |
| **admin-lockout-threshold**  integer | no description  Default: `3` |
| **adom-mode**  string | no description  no description  no description  Choices:   - `"normal"` ← (default) - `"advanced"` |
| **adom-rev-auto-delete**  string | no description  no description  no description  no description  Choices:   - `"disable"` - `"by-revisions"` ← (default) - `"by-days"` |
| **adom-rev-max-backup-revisions**  integer | no description  Default: `5` |
| **adom-rev-max-days**  integer | no description  Default: `30` |
| **adom-rev-max-revisions**  integer | no description  Default: `120` |
| **adom-select**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **adom-status**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **clone-name-option**  string | no description  no description  no description  Choices:   - `"default"` ← (default) - `"keep"` |
| **clt-cert-req**  string | no description  no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` - `"optional"` |
| **console-output**  string | no description  no description  no description  Choices:   - `"standard"` ← (default) - `"more"` |
| **country-flag**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **create-revision**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **daylightsavetime**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **default-disk-quota**  integer | no description  Default: `1000` |
| **detect-unregistered-log-device**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **device-view-mode**  string | no description  no description  no description  Choices:   - `"regular"` ← (default) - `"tree"` |
| **dh-params**  string | no description  no description  no description  no description  no description  no description  no description  no description  Choices:   - `"1024"` - `"1536"` - `"2048"` ← (default) - `"3072"` - `"4096"` - `"6144"` - `"8192"` |
| **disable-module**  list / elements=string | no description  Choices:   - `"fortiview-noc"` - `"none"` - `"fortirecorder"` - `"siem"` - `"soc"` - `"ai"` |
| **enc-algorithm**  string | no description  no description  no description  no description  Choices:   - `"low"` - `"medium"` - `"high"` ← (default) - `"custom"` |
| **faz-status**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **fgfm-ca-cert**  string | no description |
| **fgfm-local-cert**  string | no description |
| **fgfm-ssl-protocol**  string | no description  no description  no description  no description  no description  Choices:   - `"sslv3"` - `"tlsv1.0"` - `"tlsv1.1"` - `"tlsv1.2"` - `"tlsv1.3"`   Default: `"tlsv1."` |
| **ha-member-auto-grouping**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **hitcount_concurrent**  integer | no description  Default: `100` |
| **hitcount_interval**  integer | no description  Default: `300` |
| **hostname**  string | no description  Default: `"FMG-VM64"` |
| **import-ignore-addr-cmt**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **language**  string | no description  no description  no description  no description  no description  no description  no description  Choices:   - `"english"` ← (default) - `"simch"` - `"japanese"` - `"korean"` - `"spanish"` - `"trach"` |
| **latitude**  string | no description |
| **ldap-cache-timeout**  integer | no description  Default: `86400` |
| **ldapconntimeout**  integer | no description  Default: `60000` |
| **lock-preempt**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **log-checksum**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"md5"` - `"md5-auth"` |
| **log-forward-cache-size**  integer | no description  Default: `0` |
| **longitude**  string | no description |
| **max-log-forward**  integer | no description  Default: `5` |
| **max-running-reports**  integer | no description  Default: `1` |
| **mc-policy-disabled-adoms**  list / elements=string | no description |
| **adom-name**  string | no description |
| **multiple-steps-upgrade-in-autolink**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **normalized-intf-zone-only**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **object-revision-db-max**  integer | no description  Default: `100000` |
| **object-revision-mandatory-note**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **object-revision-object-max**  integer | no description  Default: `100` |
| **object-revision-status**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **oftp-ssl-protocol**  string | no description  no description  no description  no description  no description  Choices:   - `"sslv3"` - `"tlsv1.0"` - `"tlsv1.1"` - `"tlsv1.2"` - `"tlsv1.3"`   Default: `"tlsv1."` |
| **partial-install**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **partial-install-force**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **partial-install-rev**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **per-policy-lock**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **perform-improve-by-ha**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **policy-hit-count**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **policy-object-icon**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **policy-object-in-dual-pane**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **pre-login-banner**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **pre-login-banner-message**  string | no description |
| **private-data-encryption**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **remoteauthtimeout**  integer | no description  Default: `10` |
| **search-all-adoms**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **ssl-cipher-suites**  list / elements=string | description |
| **cipher**  string | no description |
| **priority**  integer | no description  Default: `0` |
| **version**  string | no description  no description  no description  Choices:   - `"tls1.2-or-below"` - `"tls1.3"`   Default: `"tls1."` |
| **ssl-low-encryption**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **ssl-protocol**  list / elements=string | no description  Choices:   - `"tlsv1.2"` - `"tlsv1.1"` - `"tlsv1.0"` - `"sslv3"` - `"tlsv1.3"` |
| **ssl-static-key-ciphers**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **task-list-size**  integer | no description  Default: `2000` |
| **tftp**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **timezone**  string | no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  Choices:   - `"00"` - `"01"` - `"02"` - `"03"` - `"04"` ← (default) - `"05"` - `"06"` - `"07"` - `"08"` - `"09"` - `"10"` - `"11"` - `"12"` - `"13"` - `"14"` - `"15"` - `"16"` - `"17"` - `"18"` - `"19"` - `"20"` - `"21"` - `"22"` - `"23"` - `"24"` - `"25"` - `"26"` - `"27"` - `"28"` - `"29"` - `"30"` - `"31"` - `"32"` - `"33"` - `"34"` - `"35"` - `"36"` - `"37"` - `"38"` - `"39"` - `"40"` - `"41"` - `"42"` - `"43"` - `"44"` - `"45"` - `"46"` - `"47"` - `"48"` - `"49"` - `"50"` - `"51"` - `"52"` - `"53"` - `"54"` - `"55"` - `"56"` - `"57"` - `"58"` - `"59"` - `"60"` - `"61"` - `"62"` - `"63"` - `"64"` - `"65"` - `"66"` - `"67"` - `"68"` - `"69"` - `"70"` - `"71"` - `"72"` - `"73"` - `"74"` - `"75"` - `"76"` - `"77"` - `"78"` - `"79"` - `"80"` - `"81"` - `"82"` - `"83"` - `"84"` - `"85"` - `"86"` - `"87"` - `"88"` - `"89"` - `"90"` - `"91"` |
| **tunnel-mtu**  integer | no description  Default: `1500` |
| **usg**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **vdom-mirror**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **webservice-proto**  list / elements=string | no description  Choices:   - `"tlsv1.2"` - `"tlsv1.1"` - `"tlsv1.0"` - `"sslv3"` - `"sslv2"` - `"tlsv1.3"` |
| **workflow-max-sessions**  integer | no description  Default: `500` |
| **workspace-mode**  string | no description  no description  no description  no description  Choices:   - `"disabled"` ← (default) - `"normal"` - `"workflow"` - `"per-adom"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

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
