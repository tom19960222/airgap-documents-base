---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_system_sdnconnector module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_system_sdnconnector_module.html
fetched_at: 2026-07-27T17:37:18+00:00
---
# fortinet.fortimanager.fmgr_system_sdnconnector module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_sdnconnector`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_system_sdnconnector_module.md#synopsis)
- [Parameters](fmgr_system_sdnconnector_module.md#parameters)
- [Notes](fmgr_system_sdnconnector_module.md#notes)
- [Examples](fmgr_system_sdnconnector_module.md#examples)
- [Return Values](fmgr_system_sdnconnector_module.md#return-values)

## [Synopsis](fmgr_system_sdnconnector_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_sdnconnector_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **system_sdnconnector**  dictionary | the top level parameters set |
| **_local_cert**  string | no description |
| **access-key**  string | no description |
| **api-key**  string | no description |
| **azure-region**  string | no description  Choices:   - `"global"` - `"china"` - `"germany"` - `"usgov"` - `"local"` |
| **client-id**  string | no description |
| **client-secret**  string | no description |
| **compartment-id**  string | no description |
| **compute-generation**  integer | no description |
| **domain**  string | no description |
| **external-account-list**  list / elements=string | description |
| **region-list**  string | description |
| **role-arn**  string | no description |
| **external-ip**  list / elements=string | no description |
| **name**  string | no description |
| **forwarding-rule**  list / elements=string | description |
| **rule-name**  string | no description |
| **target**  string | no description |
| **gcp-project**  string | no description |
| **gcp-project-list**  list / elements=string | description |
| **gcp-zone-list**  string | description |
| **id**  string | no description |
| **group-name**  string | no description |
| **ha-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ibm-region**  string | no description  Choices:   - `"us-south"` - `"us-east"` - `"germany"` - `"great-britain"` - `"japan"` - `"australia"` - `"dallas"` - `"washington-dc"` - `"london"` - `"frankfurt"` - `"sydney"` - `"tokyo"` - `"osaka"` - `"toronto"` - `"sao-paulo"` - `"dallas-private"` - `"washington-dc-private"` - `"london-private"` - `"frankfurt-private"` - `"sydney-private"` - `"tokyo-private"` - `"osaka-private"` - `"toronto-private"` - `"sao-paulo-private"` |
| **ibm-region-gen1**  string | no description  Choices:   - `"us-south"` - `"us-east"` - `"germany"` - `"great-britain"` - `"japan"` - `"australia"` |
| **ibm-region-gen2**  string | no description  Choices:   - `"us-south"` - `"us-east"` - `"great-britain"` |
| **key-passwd**  string | no description |
| **last-update**  integer | no description |
| **login-endpoint**  string | no description |
| **name**  string | no description |
| **nic**  list / elements=string | no description |
| **ip**  list / elements=string | no description |
| **name**  string | no description |
| **public-ip**  string | no description |
| **resource-group**  string | no description |
| **name**  string | no description |
| **nsx-cert-fingerprint**  string | no description |
| **oci-cert**  string | no description |
| **oci-fingerprint**  string | no description |
| **oci-region**  string | no description  Choices:   - `"phoenix"` - `"ashburn"` - `"frankfurt"` - `"london"` - `"toronto"` |
| **oci-region-type**  string | no description  Choices:   - `"commercial"` - `"government"` |
| **password**  string | no description |
| **private-key**  string | no description |
| **region**  string | no description |
| **resource-group**  string | no description |
| **resource-url**  string | no description |
| **rest-interface**  string | no description  Choices:   - `"mgmt"` - `"sync"` |
| **rest-password**  string | no description |
| **rest-sport**  integer | no description |
| **rest-ssl**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **route**  list / elements=string | no description |
| **name**  string | no description |
| **route-table**  list / elements=string | no description |
| **name**  string | no description |
| **resource-group**  string | no description |
| **route**  list / elements=string | no description |
| **name**  string | no description |
| **next-hop**  string | no description |
| **subscription-id**  string | no description |
| **secret-key**  string | no description |
| **secret-token**  string | no description |
| **server**  string | no description |
| **server-list**  string | no description |
| **server-port**  integer | no description |
| **service-account**  string | no description |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **subscription-id**  string | no description |
| **tenant-id**  string | no description |
| **type**  string | no description  Choices:   - `"aci"` - `"aws"` - `"nsx"` - `"nuage"` - `"azure"` - `"gcp"` - `"oci"` - `"openstack"` - `"kubernetes"` - `"vmware"` - `"acs"` - `"alicloud"` - `"sepm"` - `"aci-direct"` - `"ibm"` - `"nutanix"` |
| **update-interval**  integer | no description |
| **updating**  integer | no description |
| **use-metadata-iam**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **user-id**  string | no description |
| **username**  string | no description |
| **vcenter-password**  string | no description |
| **vcenter-server**  string | no description |
| **vcenter-username**  string | no description |
| **verify-certificate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **vmx-image-url**  string | no description |
| **vmx-service-name**  string | no description |
| **vpc-id**  string | no description |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_system_sdnconnector_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_sdnconnector_module.md#id4)

```yaml+jinja
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
   - name: retrieve all the connections to SDN Connector
     fmgr_fact:
       facts:
           selector: 'system_sdnconnector'
           params:
               adom: 'ansible'
               sdn-connector: 'your_value'

- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Configure connection to SDN Connector.
     fmgr_system_sdnconnector:
        bypass_validation: False
        adom: ansible
        state: present
        system_sdnconnector:
           azure-region: global #<value in [global, china, germany, ...]>
           #compartment-id: 1
           name: ansible-test-sdn
           password: fortinet
           server: ALL
           status: disable
           type: aws #<value in [aci, aws, nsx, ...]>
```

## [Return Values](fmgr_system_sdnconnector_module.md#id5)

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
