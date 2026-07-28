---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_system_sdnconnector module – Configure connection to SDN Connector."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_system_sdnconnector_module.html
fetched_at: 2026-07-28T02:20:09+00:00
---
# fortinet.fortimanager.fmgr_system_sdnconnector module – Configure connection to SDN Connector.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_sdnconnector`.

New in fortinet.fortimanager 2.0.0

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
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **system_sdnconnector**  dictionary | the top level parameters set |
| **_local_cert**  string | _Local_Cert. |
| **access-key**  string | AWS access key ID. |
| **alt-resource-ip**  string | Enable/disable AWS alternative resource IP.  **Choices:**   - `"disable"` - `"enable"` |
| **api-key**  any | (list) IBM cloud API key or service ID API key. |
| **azure-region**  string | Azure server region.  **Choices:**   - `"global"` - `"china"` - `"germany"` - `"usgov"` - `"local"` |
| **client-id**  string | Azure client ID |
| **client-secret**  any | (list) Azure client secret |
| **compartment-id**  string | Compartment ID. |
| **compartment-list**  list / elements=dictionary | no description |
| **compartment-id**  string | OCI compartment ID. |
| **compute-generation**  integer | Compute generation for IBM cloud infrastructure. |
| **domain**  string | Openstack domain. |
| **external-account-list**  list / elements=dictionary | no description |
| **external-id**  string | AWS external ID. |
| **region-list**  any | (list) no description |
| **role-arn**  string | AWS role ARN to assume. |
| **external-ip**  list / elements=dictionary | External-Ip. |
| **name**  string | External IP name. |
| **forwarding-rule**  list / elements=dictionary | no description |
| **rule-name**  string | Forwarding rule name. |
| **target**  string | Target instance name. |
| **gcp-project**  string | GCP project name. |
| **gcp-project-list**  list / elements=dictionary | no description |
| **gcp-zone-list**  any | (list) no description |
| **id**  string | GCP project ID. |
| **group-name**  string | Group name of computers. |
| **ha-status**  string | Enable/disable use for FortiGate HA service.  **Choices:**   - `"disable"` - `"enable"` |
| **ibm-region**  string | IBM cloud region name.  **Choices:**   - `"us-south"` - `"us-east"` - `"germany"` - `"great-britain"` - `"japan"` - `"australia"` - `"dallas"` - `"washington-dc"` - `"london"` - `"frankfurt"` - `"sydney"` - `"tokyo"` - `"osaka"` - `"toronto"` - `"sao-paulo"` - `"dallas-private"` - `"washington-dc-private"` - `"london-private"` - `"frankfurt-private"` - `"sydney-private"` - `"tokyo-private"` - `"osaka-private"` - `"toronto-private"` - `"sao-paulo-private"` |
| **ibm-region-gen1**  string | Ibm-Region-Gen1.  **Choices:**   - `"us-south"` - `"us-east"` - `"germany"` - `"great-britain"` - `"japan"` - `"australia"` |
| **ibm-region-gen2**  string | Ibm-Region-Gen2.  **Choices:**   - `"us-south"` - `"us-east"` - `"great-britain"` |
| **key-passwd**  any | (list) Private key password. |
| **last-update**  integer | Last-Update. |
| **login-endpoint**  string | Azure Stack login enpoint. |
| **name**  string / required | SDN connector name. |
| **nic**  list / elements=dictionary | Nic. |
| **ip**  list / elements=dictionary | Ip. |
| **name**  string | IP configuration name. |
| **public-ip**  string | Public IP name. |
| **resource-group**  string | Resource group of Azure public IP. |
| **name**  string | Network interface name. |
| **nsx-cert-fingerprint**  string | NSX certificate fingerprint. |
| **oci-cert**  string | OCI certificate. |
| **oci-fingerprint**  string | Oci-Fingerprint. |
| **oci-region**  string | OCI server region.  **Choices:**   - `"phoenix"` - `"ashburn"` - `"frankfurt"` - `"london"` - `"toronto"` |
| **oci-region-list**  list / elements=dictionary | no description |
| **region**  string | OCI region. |
| **oci-region-type**  string | OCI region type.  **Choices:**   - `"commercial"` - `"government"` |
| **password**  any | (list) Password of the remote SDN connector as login credentials. |
| **private-key**  string | Private key of GCP service account. |
| **proxy**  string | SDN proxy. |
| **region**  string | AWS region name. |
| **resource-group**  string | Azure resource group. |
| **resource-url**  string | Azure Stack resource URL. |
| **rest-interface**  string | Interface name for REST service to listen on.  **Choices:**   - `"mgmt"` - `"sync"` |
| **rest-password**  any | (list) Password for REST service. |
| **rest-sport**  integer | REST service access port |
| **rest-ssl**  string | Rest-Ssl.  **Choices:**   - `"disable"` - `"enable"` |
| **route**  list / elements=dictionary | Route. |
| **name**  string | Route name. |
| **route-table**  list / elements=dictionary | Route-Table. |
| **name**  string | Route table name. |
| **resource-group**  string | Resource group of Azure route table. |
| **route**  list / elements=dictionary | Route. |
| **name**  string | Route name. |
| **next-hop**  string | Next hop address. |
| **subscription-id**  string | Subscription ID of Azure route table. |
| **secret-key**  any | (list) AWS / ACS secret access key. |
| **secret-token**  string | Secret token of Kubernetes service account. |
| **server**  string | Server address of the remote SDN connector. |
| **server-ca-cert**  string | Trust only those servers whose certificate is directly/indirectly signed by this certificate. |
| **server-cert**  string | Trust servers that contain this certificate only. |
| **server-ip**  string | IP address of the remote SDN connector. |
| **server-list**  any | (list) Server address list of the remote SDN connector. |
| **server-port**  integer | Port number of the remote SDN connector. |
| **service-account**  string | GCP service account email. |
| **status**  string | Enable/disable connection to the remote SDN connector.  **Choices:**   - `"disable"` - `"enable"` |
| **subscription-id**  string | Azure subscription ID. |
| **tenant-id**  string | Tenant ID |
| **type**  string | Type of SDN connector.  **Choices:**   - `"aci"` - `"aws"` - `"nsx"` - `"nuage"` - `"azure"` - `"gcp"` - `"oci"` - `"openstack"` - `"kubernetes"` - `"vmware"` - `"acs"` - `"alicloud"` - `"sepm"` - `"aci-direct"` - `"ibm"` - `"nutanix"` - `"sap"` |
| **update-interval**  integer | Dynamic object update interval |
| **updating**  integer | Updating. |
| **use-metadata-iam**  string | Enable/disable using IAM role from metadata to call API.  **Choices:**   - `"disable"` - `"enable"` |
| **user-id**  string | User ID. |
| **username**  string | Username of the remote SDN connector as login credentials. |
| **vcenter-password**  any | (list) vCenter server password for NSX quarantine. |
| **vcenter-server**  string | vCenter server address for NSX quarantine. |
| **vcenter-username**  string | vCenter server username for NSX quarantine. |
| **verify-certificate**  string | Enable/disable server certificate verification.  **Choices:**   - `"disable"` - `"enable"` |
| **vmx-image-url**  string | URL of web-hosted VMX image. |
| **vmx-service-name**  string | VMX Service name. |
| **vpc-id**  string | AWS VPC ID. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

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
