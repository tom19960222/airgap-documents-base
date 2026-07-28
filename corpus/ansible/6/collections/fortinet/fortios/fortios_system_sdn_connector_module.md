---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_system_sdn_connector module – Configure connection to SDN Connector in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_system_sdn_connector_module.html
fetched_at: 2026-07-27T17:45:24+00:00
---
# fortinet.fortios.fortios_system_sdn_connector module – Configure connection to SDN Connector in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/fortinet/fortios) (version 2.2.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_system_sdn_connector_module.md#ansible-collections-fortinet-fortios-fortios-system-sdn-connector-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_sdn_connector`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_sdn_connector_module.md#synopsis)
- [Requirements](fortios_system_sdn_connector_module.md#requirements)
- [Parameters](fortios_system_sdn_connector_module.md#parameters)
- [Notes](fortios_system_sdn_connector_module.md#notes)
- [Examples](fortios_system_sdn_connector_module.md#examples)
- [Return Values](fortios_system_sdn_connector_module.md#return-values)

## [Synopsis](fortios_system_sdn_connector_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and sdn_connector category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_sdn_connector_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_system_sdn_connector_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **system_sdn_connector**  dictionary | Configure connection to SDN Connector. |
| **access_key**  string | AWS / ACS access key ID. |
| **api_key**  string | IBM cloud API key or service ID API key. |
| **azure_region**  string | Azure server region.  Choices:   - `"global"` - `"china"` - `"germany"` - `"usgov"` - `"local"` |
| **client_id**  string | Azure client ID (application ID). |
| **client_secret**  string | Azure client secret (application key). |
| **compartment_id**  string | Compartment ID. |
| **compute_generation**  integer | Compute generation for IBM cloud infrastructure. |
| **domain**  string | Domain name. |
| **external_account_list**  list / elements=dictionary | Configure AWS external account list. |
| **external_id**  string | AWS external ID. |
| **region_list**  list / elements=dictionary | AWS region name list. |
| **region**  string | AWS region name. |
| **role_arn**  string | AWS role ARN to assume. |
| **external_ip**  list / elements=dictionary | Configure GCP external IP. |
| **name**  string | External IP name. |
| **forwarding_rule**  list / elements=dictionary | Configure GCP forwarding rule. |
| **rule_name**  string | Forwarding rule name. |
| **target**  string | Target instance name. |
| **gcp_project**  string | GCP project name. |
| **gcp_project_list**  list / elements=dictionary | Configure GCP project list. |
| **gcp_zone_list**  list / elements=dictionary | Configure GCP zone list. |
| **name**  string | GCP zone name. |
| **id**  string | GCP project ID. |
| **group_name**  string | Group name of computers. |
| **ha_status**  string | Enable/disable use for FortiGate HA service.  Choices:   - `"disable"` - `"enable"` |
| **ibm_region**  string | IBM cloud region name.  Choices:   - `"dallas"` - `"washington-dc"` - `"london"` - `"frankfurt"` - `"sydney"` - `"tokyo"` - `"osaka"` - `"toronto"` - `"sao-paulo"` - `"us-south"` - `"us-east"` - `"germany"` - `"great-britain"` - `"japan"` - `"australia"` |
| **ibm_region_gen1**  string | IBM cloud compute generation 1 region name.  Choices:   - `"us-south"` - `"us-east"` - `"germany"` - `"great-britain"` - `"japan"` - `"australia"` |
| **ibm_region_gen2**  string | IBM cloud compute generation 2 region name.  Choices:   - `"us-south"` - `"us-east"` - `"great-britain"` |
| **key_passwd**  string | Private key password. |
| **login_endpoint**  string | Azure Stack login endpoint. |
| **name**  string / required | SDN connector name. |
| **nic**  list / elements=dictionary | Configure Azure network interface. |
| **ip**  list / elements=dictionary | Configure IP configuration. |
| **name**  string | IP configuration name. |
| **public_ip**  string | Public IP name. |
| **resource_group**  string | Resource group of Azure public IP. |
| **name**  string | Network interface name. |
| **oci_cert**  string | OCI certificate. Source certificate.local.name. |
| **oci_fingerprint**  string | OCI pubkey fingerprint. |
| **oci_region**  string | OCI server region.  Choices:   - `"phoenix"` - `"ashburn"` - `"frankfurt"` - `"london"` |
| **oci_region_type**  string | OCI region type.  Choices:   - `"commercial"` - `"government"` |
| **password**  string | Password of the remote SDN connector as login credentials. |
| **private_key**  string | Private key of GCP service account. |
| **region**  string | AWS / ACS region name. |
| **resource_group**  string | Azure resource group. |
| **resource_url**  string | Azure Stack resource URL. |
| **route**  list / elements=dictionary | Configure GCP route. |
| **name**  string | Route name. |
| **route_table**  list / elements=dictionary | Configure Azure route table. |
| **name**  string | Route table name. |
| **resource_group**  string | Resource group of Azure route table. |
| **route**  list / elements=dictionary | Configure Azure route. |
| **name**  string | Route name. |
| **next_hop**  string | Next hop address. |
| **subscription_id**  string | Subscription ID of Azure route table. |
| **secret_key**  string | AWS / ACS secret access key. |
| **secret_token**  string | Secret token of Kubernetes service account. |
| **server**  string | Server address of the remote SDN connector. |
| **server_list**  list / elements=dictionary | Server address list of the remote SDN connector. |
| **ip**  string | IPv4 address. |
| **server_port**  integer | Port number of the remote SDN connector. |
| **service_account**  string | GCP service account email. |
| **status**  string | Enable/disable connection to the remote SDN connector.  Choices:   - `"disable"` - `"enable"` |
| **subscription_id**  string | Azure subscription ID. |
| **tenant_id**  string | Tenant ID (directory ID). |
| **type**  string | Type of SDN connector.  Choices:   - `"aci"` - `"alicloud"` - `"aws"` - `"azure"` - `"gcp"` - `"nsx"` - `"nuage"` - `"oci"` - `"openstack"` - `"kubernetes"` - `"vmware"` - `"sepm"` - `"aci-direct"` - `"ibm"` - `"nutanix"` - `"sap"` |
| **update_interval**  integer | Dynamic object update interval (30 - 3600 sec). |
| **use_metadata_iam**  string | Enable/disable use of IAM role from metadata to call API.  Choices:   - `"disable"` - `"enable"` |
| **user_id**  string | User ID. |
| **username**  string | Username of the remote SDN connector as login credentials. |
| **vcenter_password**  string | vCenter server password for NSX quarantine. |
| **vcenter_server**  string | vCenter server address for NSX quarantine. |
| **vcenter_username**  string | vCenter server username for NSX quarantine. |
| **verify_certificate**  string | Enable/disable server certificate verification.  Choices:   - `"disable"` - `"enable"` |
| **vpc_id**  string | AWS VPC ID. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_system_sdn_connector_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_sdn_connector_module.md#id5)

```yaml+jinja
- hosts: fortigates
  collections:
    - fortinet.fortios
  connection: httpapi
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:
  - name: Configure connection to SDN Connector.
    fortios_system_sdn_connector:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_sdn_connector:
        access_key: "<your_own_value>"
        api_key: "<your_own_value>"
        azure_region: "global"
        client_id: "<your_own_value>"
        client_secret: "<your_own_value>"
        compartment_id: "<your_own_value>"
        compute_generation: "2"
        domain: "<your_own_value>"
        external_account_list:
         -
            external_id: "<your_own_value>"
            region_list:
             -
                region: "<your_own_value>"
            role_arn: "<your_own_value>"
        external_ip:
         -
            name: "default_name_17"
        forwarding_rule:
         -
            rule_name: "<your_own_value>"
            target: "<your_own_value>"
        gcp_project: "<your_own_value>"
        gcp_project_list:
         -
            gcp_zone_list:
             -
                name: "default_name_24"
            id:  "25"
        group_name: "<your_own_value>"
        ha_status: "disable"
        ibm_region: "dallas"
        ibm_region_gen1: "us-south"
        ibm_region_gen2: "us-south"
        key_passwd: "<your_own_value>"
        login_endpoint: "<your_own_value>"
        name: "default_name_33"
        nic:
         -
            ip:
             -
                name: "default_name_36"
                public_ip: "<your_own_value>"
                resource_group: "<your_own_value>"
            name: "default_name_39"
        oci_cert: "<your_own_value> (source certificate.local.name)"
        oci_fingerprint: "<your_own_value>"
        oci_region: "phoenix"
        oci_region_type: "commercial"
        password: "<your_own_value>"
        private_key: "<your_own_value>"
        region: "<your_own_value>"
        resource_group: "<your_own_value>"
        resource_url: "<your_own_value>"
        route:
         -
            name: "default_name_50"
        route_table:
         -
            name: "default_name_52"
            resource_group: "<your_own_value>"
            route:
             -
                name: "default_name_55"
                next_hop: "<your_own_value>"
            subscription_id: "<your_own_value>"
        secret_key: "<your_own_value>"
        secret_token: "<your_own_value>"
        server: "192.168.100.40"
        server_list:
         -
            ip: "<your_own_value>"
        server_port: "0"
        service_account: "<your_own_value>"
        status: "disable"
        subscription_id: "<your_own_value>"
        tenant_id: "<your_own_value>"
        type: "aci"
        update_interval: "60"
        use_metadata_iam: "disable"
        user_id: "<your_own_value>"
        username: "<your_own_value>"
        vcenter_password: "<your_own_value>"
        vcenter_server: "<your_own_value>"
        vcenter_username: "<your_own_value>"
        verify_certificate: "disable"
        vpc_id: "<your_own_value>"
```

## [Return Values](fortios_system_sdn_connector_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  Returned: always  Sample: `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  Returned: always  Sample: `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  Returned: always  Sample: `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  Returned: success  Sample: `"id"` |
| **name**  string | Name of the table used to fulfill the request  Returned: always  Sample: `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  Returned: always  Sample: `"webfilter"` |
| **revision**  string | Internal revision number  Returned: always  Sample: `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  Returned: always  Sample: `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  Returned: always  Sample: `"success"` |
| **vdom**  string | Virtual domain used  Returned: always  Sample: `"root"` |
| **version**  string | Version of the FortiGate  Returned: always  Sample: `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
[Homepage](https://www.fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
