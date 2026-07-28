---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_firewall_address_dynamicmapping module – Configure IPv4 addresses."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_firewall_address_dynamicmapping_module.html
fetched_at: 2026-07-28T02:11:36+00:00
---
# fortinet.fortimanager.fmgr_firewall_address_dynamicmapping module – Configure IPv4 addresses.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_address_dynamicmapping`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_firewall_address_dynamicmapping_module.md#synopsis)
- [Parameters](fmgr_firewall_address_dynamicmapping_module.md#parameters)
- [Notes](fmgr_firewall_address_dynamicmapping_module.md#notes)
- [Examples](fmgr_firewall_address_dynamicmapping_module.md#examples)
- [Return Values](fmgr_firewall_address_dynamicmapping_module.md#return-values)

## [Synopsis](fmgr_firewall_address_dynamicmapping_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_firewall_address_dynamicmapping_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **address**  string / required | the parameter (address) in requested url |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_address_dynamicmapping**  dictionary | the top level parameters set |
| **_image-base64**  string | no description |
| **_scope**  list / elements=dictionary | no description |
| **name**  string | no description |
| **vdom**  string | no description |
| **allow-routing**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **associated-interface**  string | no description |
| **cache-ttl**  integer | no description |
| **clearpass-spt**  string | no description  **Choices:**   - `"unknown"` - `"healthy"` - `"quarantine"` - `"checkup"` - `"transition"` - `"infected"` - `"transient"` |
| **color**  integer | no description |
| **comment**  any | (dict or str) no description |
| **country**  string | no description |
| **dirty**  string | To be deleted address.  **Choices:**   - `"dirty"` - `"clean"` |
| **end-ip**  string | no description |
| **end-mac**  string | no description |
| **epg-name**  string | no description |
| **fabric-object**  string | Security Fabric global object setting.  **Choices:**   - `"disable"` - `"enable"` |
| **filter**  string | no description |
| **fqdn**  string | no description |
| **fsso-group**  any | (list or str) no description |
| **global-object**  integer | no description |
| **hw-model**  string | Dynamic address matching hardware model. |
| **hw-vendor**  string | Dynamic address matching hardware vendor. |
| **interface**  string | no description |
| **macaddr**  any | (list) no description |
| **node-ip-only**  string | Enable/disable collection of node addresses only in Kubernetes.  **Choices:**   - `"disable"` - `"enable"` |
| **obj-id**  string | no description |
| **obj-tag**  string | no description |
| **obj-type**  string | no description  **Choices:**   - `"ip"` - `"mac"` |
| **organization**  string | no description |
| **os**  string | Dynamic address matching operating system. |
| **pattern-end**  integer | no description |
| **pattern-start**  integer | no description |
| **policy-group**  string | no description |
| **route-tag**  integer | route-tag address. |
| **sdn**  string | no description  **Choices:**   - `"aci"` - `"aws"` - `"nsx"` - `"nuage"` - `"azure"` - `"gcp"` - `"oci"` - `"openstack"` |
| **sdn-addr-type**  string | no description  **Choices:**   - `"private"` - `"public"` - `"all"` |
| **sdn-tag**  string | no description |
| **start-ip**  string | no description |
| **start-mac**  string | no description |
| **sub-type**  string | no description  **Choices:**   - `"sdn"` - `"clearpass-spt"` - `"fsso"` - `"ems-tag"` - `"swc-tag"` - `"fortivoice-tag"` - `"fortinac-tag"` - `"fortipolicy-tag"` - `"device-identification"` |
| **subnet**  string | no description |
| **subnet-name**  string | no description |
| **sw-version**  string | Dynamic address matching software version. |
| **tag-detection-level**  string | Tag detection level of dynamic address object. |
| **tag-type**  string | Tag type of dynamic address object. |
| **tags**  any | (list or str) no description |
| **tenant**  string | no description |
| **type**  string | no description  **Choices:**   - `"ipmask"` - `"iprange"` - `"fqdn"` - `"wildcard"` - `"geography"` - `"url"` - `"wildcard-fqdn"` - `"nsx"` - `"aws"` - `"dynamic"` - `"interface-subnet"` - `"mac"` - `"fqdn-group"` - `"route-tag"` |
| **url**  string | no description |
| **uuid**  string | no description |
| **visibility**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **wildcard**  string | no description |
| **wildcard-fqdn**  string | no description |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_firewall_address_dynamicmapping_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_firewall_address_dynamicmapping_module.md#id4)

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
   - name: Configure dynamic mappings of IPv4 address
     fmgr_firewall_address_dynamicmapping:
        bypass_validation: True
        adom: ansible
        address: 'ansible-test1' # name
        state: present
        firewall_address_dynamicmapping:
           _scope:
             -
                 name: FGT_AWS # need a valid device name
                 vdom: root # need a valid vdom name under the device
           allow-routing: disable #<value in [disable, enable]>
           cache-ttl: 0
           color: 1
           comment: 'ansible-comment'
           subnet: '222.222.222.101/32'
           subnet-name: 'ansible-test'
           type: ipmask #<value in [ipmask, iprange, fqdn, ...]>
           visibility: enable

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
   - name: retrieve all the dynamic mappings of IPv4 address
     fmgr_fact:
       facts:
           selector: 'firewall_address_dynamicmapping'
           params:
               adom: 'ansible'
               address: 'ansible-test1' # name
               dynamic_mapping: 'your_value'
```

## [Return Values](fmgr_firewall_address_dynamicmapping_module.md#id5)

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
