---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_firewall_profileprotocoloptions module – Configure protocol options."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_firewall_profileprotocoloptions_module.html
fetched_at: 2026-07-28T02:12:30+00:00
---
# fortinet.fortimanager.fmgr_firewall_profileprotocoloptions module – Configure protocol options.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_profileprotocoloptions`.

New in fortinet.fortimanager 2.0.0

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
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_profileprotocoloptions**  dictionary | the top level parameters set |
| **cifs**  dictionary | no description |
| **domain-controller**  string | Domain for which to decrypt CIFS traffic. |
| **file-filter**  dictionary | no description |
| **entries**  list / elements=dictionary | Entries. |
| **action**  string | Action taken for matched file.  **Choices:**   - `"log"` - `"block"` |
| **comment**  string | Comment. |
| **direction**  string | Match files transmitted in the sessions originating or reply direction.  **Choices:**   - `"any"` - `"incoming"` - `"outgoing"` |
| **file-type**  any | (list) Select file type. |
| **filter**  string | Add a file filter. |
| **protocol**  list / elements=string | Protocols to apply with.  **Choices:**   - `"cifs"` |
| **log**  string | Enable/disable file filter logging.  **Choices:**   - `"disable"` - `"enable"` |
| **status**  string | Enable/disable file filter.  **Choices:**   - `"disable"` - `"enable"` |
| **options**  list / elements=string | One or more options that can be applied to the session.  **Choices:**   - `"oversize"` |
| **oversize-limit**  integer | Maximum in-memory file size that can be scanned |
| **ports**  any | (list) Ports to scan for content |
| **scan-bzip2**  string | Enable/disable scanning of BZip2 compressed files.  **Choices:**   - `"disable"` - `"enable"` |
| **server-credential-type**  string | CIFS server credential type.  **Choices:**   - `"none"` - `"credential-replication"` - `"credential-keytab"` |
| **server-keytab**  list / elements=dictionary | Server-Keytab. |
| **keytab**  string | Base64 encoded keytab file containing credential of the server. |
| **password**  any | (list) Password for keytab. |
| **principal**  string | Service principal. |
| **status**  string | Enable/disable the active status of scanning for this protocol.  **Choices:**   - `"disable"` - `"enable"` |
| **tcp-window-maximum**  integer | Maximum dynamic TCP window size |
| **tcp-window-minimum**  integer | Minimum dynamic TCP window size |
| **tcp-window-size**  integer | Set TCP static window size |
| **tcp-window-type**  string | Specify type of TCP window to use for this protocol.  **Choices:**   - `"system"` - `"static"` - `"dynamic"` - `"auto-tuning"` |
| **uncompressed-nest-limit**  integer | Maximum nested levels of compression that can be uncompressed and scanned |
| **uncompressed-oversize-limit**  integer | Maximum in-memory uncompressed file size that can be scanned |
| **comment**  string | Optional comments. |
| **dns**  dictionary | no description |
| **ports**  any | (list) Ports to scan for content |
| **status**  string | Enable/disable the active status of scanning for this protocol.  **Choices:**   - `"disable"` - `"enable"` |
| **feature-set**  string | Flow/proxy feature set.  **Choices:**   - `"proxy"` - `"flow"` |
| **ftp**  dictionary | no description |
| **comfort-amount**  integer | Amount of data to send in a transmission for client comforting |
| **comfort-interval**  integer | Period of time between start, or last transmission, and the next client comfort transmission of data |
| **explicit-ftp-tls**  string | Enable/disable FTP redirection for explicit FTPS.  **Choices:**   - `"disable"` - `"enable"` |
| **inspect-all**  string | Enable/disable the inspection of all ports for the protocol.  **Choices:**   - `"disable"` - `"enable"` |
| **options**  list / elements=string | One or more options that can be applied to the session.  **Choices:**   - `"clientcomfort"` - `"no-content-summary"` - `"oversize"` - `"splice"` - `"bypass-rest-command"` - `"bypass-mode-command"` |
| **oversize-limit**  integer | Maximum in-memory file size that can be scanned |
| **ports**  any | (list) Ports to scan for content |
| **scan-bzip2**  string | Enable/disable scanning of BZip2 compressed files.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-offloaded**  string | SSL decryption and encryption performed by an external device.  **Choices:**   - `"no"` - `"yes"` |
| **status**  string | Enable/disable the active status of scanning for this protocol.  **Choices:**   - `"disable"` - `"enable"` |
| **stream-based-uncompressed-limit**  integer | Maximum stream-based uncompressed data size that will be scanned |
| **tcp-window-maximum**  integer | Maximum dynamic TCP window size. |
| **tcp-window-minimum**  integer | Minimum dynamic TCP window size. |
| **tcp-window-size**  integer | Set TCP static window size. |
| **tcp-window-type**  string | TCP window type to use for this protocol.  **Choices:**   - `"system"` - `"static"` - `"dynamic"` - `"auto-tuning"` |
| **uncompressed-nest-limit**  integer | Maximum nested levels of compression that can be uncompressed and scanned |
| **uncompressed-oversize-limit**  integer | Maximum in-memory uncompressed file size that can be scanned |
| **http**  dictionary | no description |
| **address-ip-rating**  string | Enable/disable IP based URL rating.  **Choices:**   - `"disable"` - `"enable"` |
| **block-page-status-code**  integer | Code number returned for blocked HTTP pages |
| **comfort-amount**  integer | Amount of data to send in a transmission for client comforting |
| **comfort-interval**  integer | Period of time between start, or last transmission, and the next client comfort transmission of data |
| **fortinet-bar**  string | Enable/disable Fortinet bar on HTML content.  **Choices:**   - `"disable"` - `"enable"` |
| **fortinet-bar-port**  integer | Port for use by Fortinet Bar |
| **h2c**  string | Enable/disable h2c HTTP connection upgrade.  **Choices:**   - `"disable"` - `"enable"` |
| **http-policy**  string | Enable/disable HTTP policy check.  **Choices:**   - `"disable"` - `"enable"` |
| **inspect-all**  string | Enable/disable the inspection of all ports for the protocol.  **Choices:**   - `"disable"` - `"enable"` |
| **options**  list / elements=string | One or more options that can be applied to the session.  **Choices:**   - `"oversize"` - `"chunkedbypass"` - `"clientcomfort"` - `"no-content-summary"` - `"servercomfort"` |
| **oversize-limit**  integer | Maximum in-memory file size that can be scanned |
| **ports**  any | (list) Ports to scan for content |
| **post-lang**  list / elements=string | ID codes for character sets to be used to convert to UTF-8 for banned words and DLP on HTTP posts  **Choices:**   - `"jisx0201"` - `"jisx0208"` - `"jisx0212"` - `"gb2312"` - `"ksc5601-ex"` - `"euc-jp"` - `"sjis"` - `"iso2022-jp"` - `"iso2022-jp-1"` - `"iso2022-jp-2"` - `"euc-cn"` - `"ces-gbk"` - `"hz"` - `"ces-big5"` - `"euc-kr"` - `"iso2022-jp-3"` - `"iso8859-1"` - `"tis620"` - `"cp874"` - `"cp1252"` - `"cp1251"` |
| **proxy-after-tcp-handshake**  string | Proxy traffic after the TCP 3-way handshake has been established  **Choices:**   - `"disable"` - `"enable"` |
| **range-block**  string | Enable/disable blocking of partial downloads.  **Choices:**   - `"disable"` - `"enable"` |
| **retry-count**  integer | Number of attempts to retry HTTP connection |
| **scan-bzip2**  string | Enable/disable scanning of BZip2 compressed files.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-offloaded**  string | SSL decryption and encryption performed by an external device.  **Choices:**   - `"no"` - `"yes"` |
| **status**  string | Enable/disable the active status of scanning for this protocol.  **Choices:**   - `"disable"` - `"enable"` |
| **stream-based-uncompressed-limit**  integer | Maximum stream-based uncompressed data size that will be scanned |
| **streaming-content-bypass**  string | Enable/disable bypassing of streaming content from buffering.  **Choices:**   - `"disable"` - `"enable"` |
| **strip-x-forwarded-for**  string | Enable/disable stripping of HTTP X-Forwarded-For header.  **Choices:**   - `"disable"` - `"enable"` |
| **switching-protocols**  string | Bypass from scanning, or block a connection that attempts to switch protocol.  **Choices:**   - `"bypass"` - `"block"` |
| **tcp-window-maximum**  integer | Maximum dynamic TCP window size |
| **tcp-window-minimum**  integer | Minimum dynamic TCP window size |
| **tcp-window-size**  integer | Set TCP static window size |
| **tcp-window-type**  string | Specify type of TCP window to use for this protocol.  **Choices:**   - `"system"` - `"static"` - `"dynamic"` - `"auto-tuning"` |
| **tunnel-non-http**  string | Configure how to process non-HTTP traffic when a profile configured for HTTP traffic accepts a non-HTTP session.  **Choices:**   - `"disable"` - `"enable"` |
| **uncompressed-nest-limit**  integer | Maximum nested levels of compression that can be uncompressed and scanned |
| **uncompressed-oversize-limit**  integer | Maximum in-memory uncompressed file size that can be scanned |
| **unknown-content-encoding**  string | Configure the action the FortiGate unit will take on unknown content-encoding.  **Choices:**   - `"block"` - `"inspect"` - `"bypass"` |
| **unknown-http-version**  string | How to handle HTTP sessions that do not comply with HTTP 0.  **Choices:**   - `"best-effort"` - `"reject"` - `"tunnel"` |
| **verify-dns-for-policy-matching**  string | Enable/disable verification of DNS for policy matching.  **Choices:**   - `"disable"` - `"enable"` |
| **imap**  dictionary | no description |
| **inspect-all**  string | Enable/disable the inspection of all ports for the protocol.  **Choices:**   - `"disable"` - `"enable"` |
| **options**  list / elements=string | One or more options that can be applied to the session.  **Choices:**   - `"oversize"` - `"fragmail"` - `"no-content-summary"` |
| **oversize-limit**  integer | Maximum in-memory file size that can be scanned |
| **ports**  any | (list) Ports to scan for content |
| **proxy-after-tcp-handshake**  string | Proxy traffic after the TCP 3-way handshake has been established  **Choices:**   - `"disable"` - `"enable"` |
| **scan-bzip2**  string | Enable/disable scanning of BZip2 compressed files.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-offloaded**  string | SSL decryption and encryption performed by an external device.  **Choices:**   - `"no"` - `"yes"` |
| **status**  string | Enable/disable the active status of scanning for this protocol.  **Choices:**   - `"disable"` - `"enable"` |
| **uncompressed-nest-limit**  integer | Maximum nested levels of compression that can be uncompressed and scanned |
| **uncompressed-oversize-limit**  integer | Maximum in-memory uncompressed file size that can be scanned |
| **mail-signature**  dictionary | no description |
| **signature**  string | Email signature to be added to outgoing email |
| **status**  string | Enable/disable adding an email signature to SMTP email messages as they pass through the FortiGate.  **Choices:**   - `"disable"` - `"enable"` |
| **mapi**  dictionary | no description |
| **options**  list / elements=string | One or more options that can be applied to the session.  **Choices:**   - `"fragmail"` - `"oversize"` - `"no-content-summary"` |
| **oversize-limit**  integer | Maximum in-memory file size that can be scanned |
| **ports**  any | (list) Ports to scan for content |
| **scan-bzip2**  string | Enable/disable scanning of BZip2 compressed files.  **Choices:**   - `"disable"` - `"enable"` |
| **status**  string | Enable/disable the active status of scanning for this protocol.  **Choices:**   - `"disable"` - `"enable"` |
| **uncompressed-nest-limit**  integer | Maximum nested levels of compression that can be uncompressed and scanned |
| **uncompressed-oversize-limit**  integer | Maximum in-memory uncompressed file size that can be scanned |
| **name**  string / required | Name. |
| **nntp**  dictionary | no description |
| **inspect-all**  string | Enable/disable the inspection of all ports for the protocol.  **Choices:**   - `"disable"` - `"enable"` |
| **options**  list / elements=string | One or more options that can be applied to the session.  **Choices:**   - `"oversize"` - `"no-content-summary"` - `"splice"` |
| **oversize-limit**  integer | Maximum in-memory file size that can be scanned |
| **ports**  any | (list) Ports to scan for content |
| **proxy-after-tcp-handshake**  string | Proxy traffic after the TCP 3-way handshake has been established  **Choices:**   - `"disable"` - `"enable"` |
| **scan-bzip2**  string | Enable/disable scanning of BZip2 compressed files.  **Choices:**   - `"disable"` - `"enable"` |
| **status**  string | Enable/disable the active status of scanning for this protocol.  **Choices:**   - `"disable"` - `"enable"` |
| **uncompressed-nest-limit**  integer | Maximum nested levels of compression that can be uncompressed and scanned |
| **uncompressed-oversize-limit**  integer | Maximum in-memory uncompressed file size that can be scanned |
| **oversize-log**  string | Enable/disable logging for antivirus oversize file blocking.  **Choices:**   - `"disable"` - `"enable"` |
| **pop3**  dictionary | no description |
| **inspect-all**  string | Enable/disable the inspection of all ports for the protocol.  **Choices:**   - `"disable"` - `"enable"` |
| **options**  list / elements=string | One or more options that can be applied to the session.  **Choices:**   - `"oversize"` - `"fragmail"` - `"no-content-summary"` |
| **oversize-limit**  integer | Maximum in-memory file size that can be scanned |
| **ports**  any | (list) Ports to scan for content |
| **proxy-after-tcp-handshake**  string | Proxy traffic after the TCP 3-way handshake has been established  **Choices:**   - `"disable"` - `"enable"` |
| **scan-bzip2**  string | Enable/disable scanning of BZip2 compressed files.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-offloaded**  string | SSL decryption and encryption performed by an external device.  **Choices:**   - `"no"` - `"yes"` |
| **status**  string | Enable/disable the active status of scanning for this protocol.  **Choices:**   - `"disable"` - `"enable"` |
| **uncompressed-nest-limit**  integer | Maximum nested levels of compression that can be uncompressed and scanned |
| **uncompressed-oversize-limit**  integer | Maximum in-memory uncompressed file size that can be scanned |
| **replacemsg-group**  string | Name of the replacement message group to be used |
| **rpc-over-http**  string | Enable/disable inspection of RPC over HTTP.  **Choices:**   - `"disable"` - `"enable"` |
| **smtp**  dictionary | no description |
| **inspect-all**  string | Enable/disable the inspection of all ports for the protocol.  **Choices:**   - `"disable"` - `"enable"` |
| **options**  list / elements=string | One or more options that can be applied to the session.  **Choices:**   - `"oversize"` - `"fragmail"` - `"no-content-summary"` - `"splice"` |
| **oversize-limit**  integer | Maximum in-memory file size that can be scanned |
| **ports**  any | (list) Ports to scan for content |
| **proxy-after-tcp-handshake**  string | Proxy traffic after the TCP 3-way handshake has been established  **Choices:**   - `"disable"` - `"enable"` |
| **scan-bzip2**  string | Enable/disable scanning of BZip2 compressed files.  **Choices:**   - `"disable"` - `"enable"` |
| **server-busy**  string | Enable/disable SMTP server busy when server not available.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-offloaded**  string | SSL decryption and encryption performed by an external device.  **Choices:**   - `"no"` - `"yes"` |
| **status**  string | Enable/disable the active status of scanning for this protocol.  **Choices:**   - `"disable"` - `"enable"` |
| **uncompressed-nest-limit**  integer | Maximum nested levels of compression that can be uncompressed and scanned |
| **uncompressed-oversize-limit**  integer | Maximum in-memory uncompressed file size that can be scanned |
| **ssh**  dictionary | no description |
| **comfort-amount**  integer | Amount of data to send in a transmission for client comforting |
| **comfort-interval**  integer | Period of time between start, or last transmission, and the next client comfort transmission of data |
| **options**  list / elements=string | One or more options that can be applied to the session.  **Choices:**   - `"oversize"` - `"clientcomfort"` - `"servercomfort"` |
| **oversize-limit**  integer | Maximum in-memory file size that can be scanned |
| **scan-bzip2**  string | Enable/disable scanning of BZip2 compressed files.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-offloaded**  string | SSL decryption and encryption performed by an external device.  **Choices:**   - `"no"` - `"yes"` |
| **stream-based-uncompressed-limit**  integer | Maximum stream-based uncompressed data size that will be scanned |
| **tcp-window-maximum**  integer | Maximum dynamic TCP window size. |
| **tcp-window-minimum**  integer | Minimum dynamic TCP window size. |
| **tcp-window-size**  integer | Set TCP static window size. |
| **tcp-window-type**  string | TCP window type to use for this protocol.  **Choices:**   - `"system"` - `"static"` - `"dynamic"` - `"auto-tuning"` |
| **uncompressed-nest-limit**  integer | Maximum nested levels of compression that can be uncompressed and scanned |
| **uncompressed-oversize-limit**  integer | Maximum in-memory uncompressed file size that can be scanned |
| **switching-protocols-log**  string | Enable/disable logging for HTTP/HTTPS switching protocols.  **Choices:**   - `"disable"` - `"enable"` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

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
