---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_firewall_profileprotocoloptions module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_firewall_profileprotocoloptions_module.html
fetched_at: 2026-07-27T17:31:32+00:00
---
# fortinet.fortimanager.fmgr_firewall_profileprotocoloptions module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_profileprotocoloptions`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_firewall_profileprotocoloptions_module.md#synopsis)
- [Parameters](fmgr_firewall_profileprotocoloptions_module.md#parameters)
- [Notes](fmgr_firewall_profileprotocoloptions_module.md#notes)
- [Examples](fmgr_firewall_profileprotocoloptions_module.md#examples)
- [Return Values](fmgr_firewall_profileprotocoloptions_module.md#return-values)

## [Synopsis](fmgr_firewall_profileprotocoloptions_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_firewall_profileprotocoloptions_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **firewall_profileprotocoloptions**  dictionary | the top level parameters set |
| **cifs**  dictionary | no description |
| **domain-controller**  string | no description |
| **file-filter**  dictionary | no description |
| **entries**  list / elements=string | no description |
| **action**  string | no description  Choices:   - `"log"` - `"block"` |
| **comment**  string | no description |
| **direction**  string | no description  Choices:   - `"any"` - `"incoming"` - `"outgoing"` |
| **file-type**  string | no description |
| **filter**  string | no description |
| **protocol**  list / elements=string | no description  Choices:   - `"cifs"` |
| **log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **options**  list / elements=string | no description  Choices:   - `"oversize"` |
| **oversize-limit**  integer | no description |
| **ports**  integer | no description |
| **scan-bzip2**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **server-credential-type**  string | no description  Choices:   - `"none"` - `"credential-replication"` - `"credential-keytab"` |
| **server-keytab**  list / elements=string | no description |
| **keytab**  string | no description |
| **password**  string | no description |
| **principal**  string | no description |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **tcp-window-maximum**  integer | no description |
| **tcp-window-minimum**  integer | no description |
| **tcp-window-size**  integer | no description |
| **tcp-window-type**  string | no description  Choices:   - `"system"` - `"static"` - `"dynamic"` - `"auto-tuning"` |
| **uncompressed-nest-limit**  integer | no description |
| **uncompressed-oversize-limit**  integer | no description |
| **comment**  string | no description |
| **dns**  dictionary | no description |
| **ports**  integer | no description |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **feature-set**  string | no description  Choices:   - `"proxy"` - `"flow"` |
| **ftp**  dictionary | no description |
| **comfort-amount**  integer | no description |
| **comfort-interval**  integer | no description |
| **inspect-all**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **options**  list / elements=string | no description  Choices:   - `"clientcomfort"` - `"no-content-summary"` - `"oversize"` - `"splice"` - `"bypass-rest-command"` - `"bypass-mode-command"` |
| **oversize-limit**  integer | no description |
| **ports**  integer | no description |
| **scan-bzip2**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-offloaded**  string | no description  Choices:   - `"no"` - `"yes"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **stream-based-uncompressed-limit**  integer | no description |
| **tcp-window-maximum**  integer | no description |
| **tcp-window-minimum**  integer | no description |
| **tcp-window-size**  integer | no description |
| **tcp-window-type**  string | no description  Choices:   - `"system"` - `"static"` - `"dynamic"` - `"auto-tuning"` |
| **uncompressed-nest-limit**  integer | no description |
| **uncompressed-oversize-limit**  integer | no description |
| **http**  dictionary | no description |
| **address-ip-rating**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **block-page-status-code**  integer | no description |
| **comfort-amount**  integer | no description |
| **comfort-interval**  integer | no description |
| **fortinet-bar**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **fortinet-bar-port**  integer | no description |
| **h2c**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **inspect-all**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **options**  list / elements=string | no description  Choices:   - `"oversize"` - `"chunkedbypass"` - `"clientcomfort"` - `"no-content-summary"` - `"servercomfort"` |
| **oversize-limit**  integer | no description |
| **ports**  integer | no description |
| **post-lang**  list / elements=string | no description  Choices:   - `"jisx0201"` - `"jisx0208"` - `"jisx0212"` - `"gb2312"` - `"ksc5601-ex"` - `"euc-jp"` - `"sjis"` - `"iso2022-jp"` - `"iso2022-jp-1"` - `"iso2022-jp-2"` - `"euc-cn"` - `"ces-gbk"` - `"hz"` - `"ces-big5"` - `"euc-kr"` - `"iso2022-jp-3"` - `"iso8859-1"` - `"tis620"` - `"cp874"` - `"cp1252"` - `"cp1251"` |
| **proxy-after-tcp-handshake**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **range-block**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **retry-count**  integer | no description |
| **scan-bzip2**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-offloaded**  string | no description  Choices:   - `"no"` - `"yes"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **stream-based-uncompressed-limit**  integer | no description |
| **streaming-content-bypass**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **strip-x-forwarded-for**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **switching-protocols**  string | no description  Choices:   - `"bypass"` - `"block"` |
| **tcp-window-maximum**  integer | no description |
| **tcp-window-minimum**  integer | no description |
| **tcp-window-size**  integer | no description |
| **tcp-window-type**  string | no description  Choices:   - `"system"` - `"static"` - `"dynamic"` - `"auto-tuning"` |
| **tunnel-non-http**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **uncompressed-nest-limit**  integer | no description |
| **uncompressed-oversize-limit**  integer | no description |
| **unknown-http-version**  string | no description  Choices:   - `"best-effort"` - `"reject"` - `"tunnel"` |
| **imap**  dictionary | no description |
| **inspect-all**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **options**  list / elements=string | no description  Choices:   - `"oversize"` - `"fragmail"` - `"no-content-summary"` |
| **oversize-limit**  integer | no description |
| **ports**  integer | no description |
| **proxy-after-tcp-handshake**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **scan-bzip2**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-offloaded**  string | no description  Choices:   - `"no"` - `"yes"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **uncompressed-nest-limit**  integer | no description |
| **uncompressed-oversize-limit**  integer | no description |
| **mail-signature**  dictionary | no description |
| **signature**  string | no description |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mapi**  dictionary | no description |
| **options**  list / elements=string | no description  Choices:   - `"fragmail"` - `"oversize"` - `"no-content-summary"` |
| **oversize-limit**  integer | no description |
| **ports**  integer | no description |
| **scan-bzip2**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **uncompressed-nest-limit**  integer | no description |
| **uncompressed-oversize-limit**  integer | no description |
| **name**  string | no description |
| **nntp**  dictionary | no description |
| **inspect-all**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **options**  list / elements=string | no description  Choices:   - `"oversize"` - `"no-content-summary"` - `"splice"` |
| **oversize-limit**  integer | no description |
| **ports**  integer | no description |
| **proxy-after-tcp-handshake**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **scan-bzip2**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **uncompressed-nest-limit**  integer | no description |
| **uncompressed-oversize-limit**  integer | no description |
| **oversize-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **pop3**  dictionary | no description |
| **inspect-all**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **options**  list / elements=string | no description  Choices:   - `"oversize"` - `"fragmail"` - `"no-content-summary"` |
| **oversize-limit**  integer | no description |
| **ports**  integer | no description |
| **proxy-after-tcp-handshake**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **scan-bzip2**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-offloaded**  string | no description  Choices:   - `"no"` - `"yes"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **uncompressed-nest-limit**  integer | no description |
| **uncompressed-oversize-limit**  integer | no description |
| **replacemsg-group**  string | no description |
| **rpc-over-http**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **smtp**  dictionary | no description |
| **inspect-all**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **options**  list / elements=string | no description  Choices:   - `"oversize"` - `"fragmail"` - `"no-content-summary"` - `"splice"` |
| **oversize-limit**  integer | no description |
| **ports**  integer | no description |
| **proxy-after-tcp-handshake**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **scan-bzip2**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **server-busy**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-offloaded**  string | no description  Choices:   - `"no"` - `"yes"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **uncompressed-nest-limit**  integer | no description |
| **uncompressed-oversize-limit**  integer | no description |
| **ssh**  dictionary | no description |
| **comfort-amount**  integer | no description |
| **comfort-interval**  integer | no description |
| **options**  list / elements=string | no description  Choices:   - `"oversize"` - `"clientcomfort"` - `"servercomfort"` |
| **oversize-limit**  integer | no description |
| **scan-bzip2**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-offloaded**  string | no description  Choices:   - `"no"` - `"yes"` |
| **stream-based-uncompressed-limit**  integer | no description |
| **tcp-window-maximum**  integer | no description |
| **tcp-window-minimum**  integer | no description |
| **tcp-window-size**  integer | no description |
| **tcp-window-type**  string | no description  Choices:   - `"system"` - `"static"` - `"dynamic"` - `"auto-tuning"` |
| **uncompressed-nest-limit**  integer | no description |
| **uncompressed-oversize-limit**  integer | no description |
| **switching-protocols-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_firewall_profileprotocoloptions_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_firewall_profileprotocoloptions_module.md#id4)

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
   - name: Configure protocol options.
     fmgr_firewall_profileprotocoloptions:
        bypass_validation: False
        adom: ansible
        state: present
        firewall_profileprotocoloptions:
           comment: 'ansible-comment'
           name: 'ansible-test'

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
   - name: retrieve all the profile protocol options
     fmgr_fact:
       facts:
           selector: 'firewall_profileprotocoloptions'
           params:
               adom: 'ansible'
               profile-protocol-options: 'your_value'
```

## [Return Values](fmgr_firewall_profileprotocoloptions_module.md#id5)

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
