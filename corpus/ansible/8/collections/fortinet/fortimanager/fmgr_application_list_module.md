---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_application_list module – Configure application control lists."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_application_list_module.html
fetched_at: 2026-07-28T02:08:12+00:00
---
# fortinet.fortimanager.fmgr_application_list module – Configure application control lists.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_application_list`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_application_list_module.md#synopsis)
- [Parameters](fmgr_application_list_module.md#parameters)
- [Notes](fmgr_application_list_module.md#notes)
- [Examples](fmgr_application_list_module.md#examples)
- [Return Values](fmgr_application_list_module.md#return-values)

## [Synopsis](fmgr_application_list_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_application_list_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **application_list**  dictionary | the top level parameters set |
| **app-replacemsg**  string | Enable/disable replacement messages for blocked applications.  **Choices:**   - `"disable"` - `"enable"` |
| **comment**  string | comments |
| **control-default-network-services**  string | Enable/disable enforcement of protocols over selected ports.  **Choices:**   - `"disable"` - `"enable"` |
| **deep-app-inspection**  string | Enable/disable deep application inspection.  **Choices:**   - `"disable"` - `"enable"` |
| **default-network-services**  list / elements=dictionary | Default-Network-Services. |
| **id**  integer | Entry ID. |
| **port**  integer | Port number. |
| **services**  list / elements=string | Network protocols.  **Choices:**   - `"http"` - `"ssh"` - `"telnet"` - `"ftp"` - `"dns"` - `"smtp"` - `"pop3"` - `"imap"` - `"snmp"` - `"nntp"` - `"https"` |
| **violation-action**  string | Action for protocols not white listed under selected port.  **Choices:**   - `"block"` - `"monitor"` - `"pass"` |
| **enforce-default-app-port**  string | Enable/disable default application port enforcement for allowed applications.  **Choices:**   - `"disable"` - `"enable"` |
| **entries**  list / elements=dictionary | Entries. |
| **action**  string | Pass or block traffic, or reset connection for traffic from this application.  **Choices:**   - `"pass"` - `"block"` - `"reset"` |
| **application**  any | (list) ID of allowed applications. |
| **behavior**  any | (list) Application behavior filter. |
| **category**  any | (list or str) Category ID list. |
| **exclusion**  any | (list) ID of excluded applications. |
| **id**  integer | Entry ID. |
| **log**  string | Enable/disable logging for this application list.  **Choices:**   - `"disable"` - `"enable"` |
| **log-packet**  string | Enable/disable packet logging.  **Choices:**   - `"disable"` - `"enable"` |
| **parameters**  list / elements=dictionary | Parameters. |
| **id**  integer | Parameter ID. |
| **members**  list / elements=dictionary | Members. |
| **id**  integer | Parameter. |
| **name**  string | Parameter name. |
| **value**  string | Parameter value. |
| **value**  string | Parameter value. |
| **per-ip-shaper**  string | Per-IP traffic shaper. |
| **popularity**  list / elements=string | Application popularity filter  **Choices:**   - `"1"` - `"2"` - `"3"` - `"4"` - `"5"` |
| **protocols**  any | (list) Application protocol filter. |
| **quarantine**  string | Quarantine method.  **Choices:**   - `"none"` - `"attacker"` |
| **quarantine-expiry**  string | Duration of quarantine. |
| **quarantine-log**  string | Enable/disable quarantine logging.  **Choices:**   - `"disable"` - `"enable"` |
| **rate-count**  integer | Count of the rate. |
| **rate-duration**  integer | Duration |
| **rate-mode**  string | Rate limit mode.  **Choices:**   - `"periodical"` - `"continuous"` |
| **rate-track**  string | Track the packet protocol field.  **Choices:**   - `"none"` - `"src-ip"` - `"dest-ip"` - `"dhcp-client-mac"` - `"dns-domain"` |
| **risk**  any | (list) Risk, or impact, of allowing traffic from this application to occur |
| **session-ttl**  integer | Session TTL |
| **shaper**  string | Traffic shaper. |
| **shaper-reverse**  string | Reverse traffic shaper. |
| **sub-category**  any | (list) Application Sub-category ID list. |
| **tags**  string | Tag filter. |
| **technology**  any | (list) Application technology filter. |
| **vendor**  any | (list) Application vendor filter. |
| **extended-log**  string | Enable/disable extended logging.  **Choices:**   - `"disable"` - `"enable"` |
| **force-inclusion-ssl-di-sigs**  string | Enable/disable forced inclusion of SSL deep inspection signatures.  **Choices:**   - `"disable"` - `"enable"` |
| **name**  string / required | List name. |
| **options**  list / elements=string | Basic application protocol signatures allowed by default.  **Choices:**   - `"allow-dns"` - `"allow-icmp"` - `"allow-http"` - `"allow-ssl"` - `"allow-quic"` |
| **other-application-action**  string | Action for other applications.  **Choices:**   - `"pass"` - `"block"` |
| **other-application-log**  string | Enable/disable logging for other applications.  **Choices:**   - `"disable"` - `"enable"` |
| **p2p-black-list**  list / elements=string | P2P applications to be black listed.  **Choices:**   - `"skype"` - `"edonkey"` - `"bittorrent"` |
| **p2p-block-list**  list / elements=string | P2P applications to be blocklisted.  **Choices:**   - `"skype"` - `"edonkey"` - `"bittorrent"` |
| **replacemsg-group**  string | Replacement message group. |
| **unknown-application-action**  string | Pass or block traffic from unknown applications.  **Choices:**   - `"pass"` - `"block"` |
| **unknown-application-log**  string | Enable/disable logging for unknown applications.  **Choices:**   - `"disable"` - `"enable"` |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_application_list_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_application_list_module.md#id4)

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
   - name: Configure application control lists.
     fmgr_application_list:
        adom: ansible
        state: present
        application_list:
           app-replacemsg: enable
           comment: 'ansible-test-comment'
           deep-app-inspection: enable
           extended-log: disable
           name: 'ansible-test'
           other-application-action: pass
           other-application-log: disable
           unknown-application-action: pass
           unknown-application-log: disable
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
   - name: retrieve all the application list
     fmgr_fact:
       facts:
           selector: 'application_list'
           params:
               adom: 'ansible'
               list: 'your_value'
```

## [Return Values](fmgr_application_list_module.md#id5)

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
