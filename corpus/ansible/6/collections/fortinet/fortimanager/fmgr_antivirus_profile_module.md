---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_antivirus_profile module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_antivirus_profile_module.html
fetched_at: 2026-07-27T17:28:17+00:00
---
# fortinet.fortimanager.fmgr_antivirus_profile module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_antivirus_profile`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_antivirus_profile_module.md#synopsis)
- [Parameters](fmgr_antivirus_profile_module.md#parameters)
- [Notes](fmgr_antivirus_profile_module.md#notes)
- [Examples](fmgr_antivirus_profile_module.md#examples)
- [Return Values](fmgr_antivirus_profile_module.md#return-values)

## [Synopsis](fmgr_antivirus_profile_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_antivirus_profile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **antivirus_profile**  dictionary | the top level parameters set |
| **analytics-accept-filetype**  string | no description |
| **analytics-bl-filetype**  string | no description |
| **analytics-db**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **analytics-ignore-filetype**  string | no description |
| **analytics-max-upload**  integer | no description |
| **analytics-wl-filetype**  string | no description |
| **av-block-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **av-virus-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **cifs**  dictionary | no description |
| **archive-block**  list / elements=string | no description  Choices:   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **archive-log**  list / elements=string | no description  Choices:   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **av-scan**  string | no description  Choices:   - `"disable"` - `"monitor"` - `"block"` |
| **emulator**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **external-blocklist**  string | no description  Choices:   - `"disable"` - `"monitor"` - `"block"` |
| **fortindr**  string | no description  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortisandbox**  string | no description  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **options**  list / elements=string | no description  Choices:   - `"scan"` - `"quarantine"` - `"avmonitor"` |
| **outbreak-prevention**  string | no description  Choices:   - `"disabled"` - `"files"` - `"full-archive"` - `"disable"` - `"block"` - `"monitor"` |
| **quarantine**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **comment**  string | no description |
| **content-disarm**  dictionary | no description |
| **cover-page**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **detect-only**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **error-action**  string | no description  Choices:   - `"block"` - `"log-only"` - `"ignore"` |
| **office-action**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **office-dde**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **office-embed**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **office-hylink**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **office-linked**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **office-macro**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **original-file-destination**  string | no description  Choices:   - `"fortisandbox"` - `"quarantine"` - `"discard"` |
| **pdf-act-form**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **pdf-act-gotor**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **pdf-act-java**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **pdf-act-launch**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **pdf-act-movie**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **pdf-act-sound**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **pdf-embedfile**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **pdf-hyperlink**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **pdf-javacode**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ems-threat-feed**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **extended-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **external-blocklist**  string | no description |
| **external-blocklist-archive-scan**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **external-blocklist-enable-all**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **feature-set**  string | no description  Choices:   - `"proxy"` - `"flow"` |
| **fortindr-error-action**  string | no description  Choices:   - `"log-only"` - `"block"` - `"ignore"` |
| **fortindr-timeout-action**  string | no description  Choices:   - `"log-only"` - `"block"` - `"ignore"` |
| **fortisandbox-error-action**  string | no description  Choices:   - `"log-only"` - `"block"` - `"ignore"` |
| **fortisandbox-max-upload**  integer | no description |
| **fortisandbox-mode**  string | no description  Choices:   - `"inline"` - `"analytics-suspicious"` - `"analytics-everything"` |
| **fortisandbox-timeout-action**  string | no description  Choices:   - `"log-only"` - `"block"` - `"ignore"` |
| **ftgd-analytics**  string | no description  Choices:   - `"disable"` - `"suspicious"` - `"everything"` |
| **ftp**  dictionary | no description |
| **archive-block**  list / elements=string | no description  Choices:   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **archive-log**  list / elements=string | no description  Choices:   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **av-scan**  string | no description  Choices:   - `"disable"` - `"monitor"` - `"block"` |
| **emulator**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **external-blocklist**  string | no description  Choices:   - `"disable"` - `"monitor"` - `"block"` |
| **fortindr**  string | no description  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortisandbox**  string | no description  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **options**  list / elements=string | no description  Choices:   - `"scan"` - `"file-filter"` - `"quarantine"` - `"avquery"` - `"avmonitor"` |
| **outbreak-prevention**  string | no description  Choices:   - `"disabled"` - `"files"` - `"full-archive"` - `"disable"` - `"block"` - `"monitor"` |
| **quarantine**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **http**  dictionary | no description |
| **archive-block**  list / elements=string | no description  Choices:   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **archive-log**  list / elements=string | no description  Choices:   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **av-scan**  string | no description  Choices:   - `"disable"` - `"monitor"` - `"block"` |
| **content-disarm**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **emulator**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **external-blocklist**  string | no description  Choices:   - `"disable"` - `"monitor"` - `"block"` |
| **fortindr**  string | no description  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortisandbox**  string | no description  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **options**  list / elements=string | no description  Choices:   - `"scan"` - `"file-filter"` - `"quarantine"` - `"avquery"` - `"avmonitor"` - `"strict-file"` |
| **outbreak-prevention**  string | no description  Choices:   - `"disabled"` - `"files"` - `"full-archive"` - `"disable"` - `"block"` - `"monitor"` |
| **quarantine**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **imap**  dictionary | no description |
| **archive-block**  list / elements=string | no description  Choices:   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **archive-log**  list / elements=string | no description  Choices:   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **av-scan**  string | no description  Choices:   - `"disable"` - `"monitor"` - `"block"` |
| **content-disarm**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **emulator**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **executables**  string | no description  Choices:   - `"default"` - `"virus"` |
| **external-blocklist**  string | no description  Choices:   - `"disable"` - `"monitor"` - `"block"` |
| **fortindr**  string | no description  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortisandbox**  string | no description  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **options**  list / elements=string | no description  Choices:   - `"scan"` - `"file-filter"` - `"quarantine"` - `"avquery"` - `"avmonitor"` |
| **outbreak-prevention**  string | no description  Choices:   - `"disabled"` - `"files"` - `"full-archive"` - `"disable"` - `"block"` - `"monitor"` |
| **quarantine**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **inspection-mode**  string | no description  Choices:   - `"proxy"` - `"flow-based"` |
| **mapi**  dictionary | no description |
| **archive-block**  list / elements=string | no description  Choices:   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **archive-log**  list / elements=string | no description  Choices:   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **av-scan**  string | no description  Choices:   - `"disable"` - `"monitor"` - `"block"` |
| **emulator**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **executables**  string | no description  Choices:   - `"default"` - `"virus"` |
| **external-blocklist**  string | no description  Choices:   - `"disable"` - `"monitor"` - `"block"` |
| **fortindr**  string | no description  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortisandbox**  string | no description  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **options**  list / elements=string | no description  Choices:   - `"scan"` - `"quarantine"` - `"avquery"` - `"avmonitor"` |
| **outbreak-prevention**  string | no description  Choices:   - `"disabled"` - `"files"` - `"full-archive"` - `"disable"` - `"block"` - `"monitor"` |
| **quarantine**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mobile-malware-db**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **nac-quar**  dictionary | no description |
| **expiry**  string | no description |
| **infected**  string | no description  Choices:   - `"none"` - `"quar-src-ip"` - `"quar-interface"` |
| **log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **name**  string | no description |
| **nntp**  dictionary | no description |
| **archive-block**  list / elements=string | no description  Choices:   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **archive-log**  list / elements=string | no description  Choices:   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **av-scan**  string | no description  Choices:   - `"disable"` - `"monitor"` - `"block"` |
| **emulator**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **external-blocklist**  string | no description  Choices:   - `"disable"` - `"monitor"` - `"block"` |
| **fortindr**  string | no description  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortisandbox**  string | no description  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **options**  list / elements=string | no description  Choices:   - `"scan"` - `"file-filter"` - `"quarantine"` - `"avquery"` - `"avmonitor"` |
| **outbreak-prevention**  string | no description  Choices:   - `"disabled"` - `"files"` - `"full-archive"` - `"disable"` - `"block"` - `"monitor"` |
| **quarantine**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **outbreak-prevention**  dictionary | no description |
| **external-blocklist**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ftgd-service**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **outbreak-prevention-archive-scan**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **pop3**  dictionary | no description |
| **archive-block**  list / elements=string | no description  Choices:   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **archive-log**  list / elements=string | no description  Choices:   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **av-scan**  string | no description  Choices:   - `"disable"` - `"monitor"` - `"block"` |
| **content-disarm**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **emulator**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **executables**  string | no description  Choices:   - `"default"` - `"virus"` |
| **external-blocklist**  string | no description  Choices:   - `"disable"` - `"monitor"` - `"block"` |
| **fortindr**  string | no description  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortisandbox**  string | no description  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **options**  list / elements=string | no description  Choices:   - `"scan"` - `"file-filter"` - `"quarantine"` - `"avquery"` - `"avmonitor"` |
| **outbreak-prevention**  string | no description  Choices:   - `"disabled"` - `"files"` - `"full-archive"` - `"disable"` - `"block"` - `"monitor"` |
| **quarantine**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **replacemsg-group**  string | no description |
| **scan-mode**  string | no description  Choices:   - `"quick"` - `"full"` - `"legacy"` - `"default"` |
| **smtp**  dictionary | no description |
| **archive-block**  list / elements=string | no description  Choices:   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **archive-log**  list / elements=string | no description  Choices:   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **av-scan**  string | no description  Choices:   - `"disable"` - `"monitor"` - `"block"` |
| **content-disarm**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **emulator**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **executables**  string | no description  Choices:   - `"default"` - `"virus"` |
| **external-blocklist**  string | no description  Choices:   - `"disable"` - `"monitor"` - `"block"` |
| **fortindr**  string | no description  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortisandbox**  string | no description  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **options**  list / elements=string | no description  Choices:   - `"scan"` - `"file-filter"` - `"quarantine"` - `"avquery"` - `"avmonitor"` |
| **outbreak-prevention**  string | no description  Choices:   - `"disabled"` - `"files"` - `"full-archive"` - `"disable"` - `"block"` - `"monitor"` |
| **quarantine**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssh**  dictionary | no description |
| **archive-block**  list / elements=string | no description  Choices:   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **archive-log**  list / elements=string | no description  Choices:   - `"encrypted"` - `"corrupted"` - `"multipart"` - `"nested"` - `"mailbomb"` - `"unhandled"` - `"partiallycorrupted"` - `"fileslimit"` - `"timeout"` |
| **av-scan**  string | no description  Choices:   - `"disable"` - `"monitor"` - `"block"` |
| **emulator**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **external-blocklist**  string | no description  Choices:   - `"disable"` - `"monitor"` - `"block"` |
| **fortindr**  string | no description  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **fortisandbox**  string | no description  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **options**  list / elements=string | no description  Choices:   - `"avmonitor"` - `"quarantine"` - `"scan"` |
| **outbreak-prevention**  string | no description  Choices:   - `"disabled"` - `"files"` - `"full-archive"` - `"disable"` - `"block"` - `"monitor"` |
| **quarantine**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_antivirus_profile_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_antivirus_profile_module.md#id4)

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
   - name: Configure AntiVirus profiles.
     fmgr_antivirus_profile:
        adom: ansible
        state: present
        antivirus_profile:
           analytics-db: disable
           analytics-max-upload: 20
           av-block-log: disable
           av-virus-log: disable
           comment: 'test comment'
           extended-log: disable
           ftgd-analytics: disable
           inspection-mode: proxy
           mobile-malware-db: disable
           name: 'antivirus-profile'
           scan-mode: quick
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
   - name: retrieve all the antivirus profiles
     fmgr_fact:
       facts:
           selector: 'antivirus_profile'
           params:
               adom: 'ansible'
               profile: 'your_value'
```

## [Return Values](fmgr_antivirus_profile_module.md#id5)

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
