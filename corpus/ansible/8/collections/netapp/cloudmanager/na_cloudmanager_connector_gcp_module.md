---
collection: ansible
version: "8"
title: "netapp.cloudmanager.na_cloudmanager_connector_gcp module – NetApp Cloud Manager connector for GCP."
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/cloudmanager/na_cloudmanager_connector_gcp_module.html
fetched_at: 2026-07-28T02:41:07+00:00
---
# netapp.cloudmanager.na_cloudmanager_connector_gcp module – NetApp Cloud Manager connector for GCP.

> **Note:**
>
> This module is part of the [netapp.cloudmanager collection](https://galaxy.ansible.com/ui/repo/published/netapp/cloudmanager/) (version 21.22.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.cloudmanager`.
>
> To use it in a playbook, specify: `netapp.cloudmanager.na_cloudmanager_connector_gcp`.

New in netapp.cloudmanager 21.4.0

- [Synopsis](na_cloudmanager_connector_gcp_module.md#synopsis)
- [Parameters](na_cloudmanager_connector_gcp_module.md#parameters)
- [Notes](na_cloudmanager_connector_gcp_module.md#notes)
- [Examples](na_cloudmanager_connector_gcp_module.md#examples)
- [Return Values](na_cloudmanager_connector_gcp_module.md#return-values)

## [Synopsis](na_cloudmanager_connector_gcp_module.md#id1)

- Create or delete Cloud Manager connector for GCP.

## [Parameters](na_cloudmanager_connector_gcp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **account_id**  string | The NetApp account ID that the Connector will be associated with.  If not provided, Cloud Manager uses the first account. If no account exists, Cloud Manager creates a new account.  You can find the account ID in the account tab of Cloud Manager at [<https://cloudmanager.netapp.com](https://cloudmanager.netapp.com>). |
| **associate_public_ip**  boolean | Indicates whether to associate a public IP address to the virtual machine.  **Choices:**   - `false` - `true` ← (default) |
| **client_id**  string | The client ID of the Cloud Manager Connector.  The connector ID.  If state is absent, the client id is used to identify the agent and delete it.  If state is absent and this parameter is not set, all agents associated with `name` are deleted.  Ignored when state is present. |
| **company**  string / required | The name of the company of the user. |
| **environment**  string  *added in netapp.cloudmanager 21.8.0* | The environment for NetApp Cloud Manager API operations.  **Choices:**   - `"prod"` ← (default) - `"stage"` |
| **feature_flags**  dictionary  *added in netapp.cloudmanager 21.11.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **firewall_tags**  boolean | Indicates whether to add firewall_tags to the connector VM (HTTP and HTTP).  **Choices:**   - `false` - `true` ← (default) |
| **gcp_service_account_email**  aliases: service_account_email  string / required  *added in netapp.cloudmanager 21.7.0* | The email of the service_account for the connector instance. This service account is used to allow the Connector to create Cloud Volume ONTAP. |
| **gcp_service_account_path**  aliases: service_account_path  string  *added in netapp.cloudmanager 21.7.0* | The local path of the service_account JSON file for GCP authorization purposes. This service account is used to create the Connector in GCP. |
| **machine_type**  string | The machine_type for the Connector VM.  **Default:** `"n2-standard-4"` |
| **name**  string / required | The name of the Cloud Manager connector for GCP to manage. |
| **network_project_id**  string | The project id in GCP associated with the Subnet. If not provided, it is assumed that the Subnet is within the previously specified project id. |
| **project_id**  string / required | The GCP project_id where the connector will be created. |
| **proxy_certificates**  list / elements=string | The proxy certificates. A list of certificate file names. |
| **proxy_password**  string | The proxy password, if using a proxy to connect to the internet. |
| **proxy_url**  string | The proxy URL, if using a proxy to connect to the internet. |
| **proxy_user_name**  string | The proxy user name, if using a proxy to connect to the internet. |
| **refresh_token**  string | The refresh token for NetApp Cloud Manager API operations. |
| **sa_client_id**  string | The service account secret client ID for NetApp Cloud Manager API operations. |
| **sa_secret_key**  string | The service account secret key for NetApp Cloud Manager API operations. |
| **state**  string | Whether the specified Cloud Manager connector for GCP should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subnet_id**  string | The name of the subnet for the virtual machine.  **Default:** `"default"` |
| **zone**  string / required | The GCP zone where the Connector will be created. |

## [Notes](na_cloudmanager_connector_gcp_module.md#id3)

> **Note:**
>
> - The modules prefixed with na_cloudmanager are built to manage CloudManager and CVO deployments in AWS/GCP/Azure clouds.
> - If sa_client_id and sa_secret_key are provided, service account will be used in operations. refresh_token will be ignored.

## [Examples](na_cloudmanager_connector_gcp_module.md#id4)

```yaml+jinja
- name: Create NetApp Cloud Manager connector for GCP
  netapp.cloudmanager.na_cloudmanager_connector_gcp:
    state: present
    name: ansible-occm-gcp
    project_id: xxxxxxx-support
    zone: us-east4-b
    company: NetApp
    gcp_service_account_email: xxxxxxxx@xxxxxxx-support.iam.gserviceaccount.com
    gcp_service_account_path: gcp_creds.json
    proxy_user_name: test
    proxy_password: test
    proxy_url: http://abcdefg.com
    proxy_certificates: ["D-TRUST_Root_Class_3_CA_2_2009.crt", "DigiCertGlobalRootCA.crt", "DigiCertGlobalRootG2.crt"]
    account_id: account-xxxxXXXX
    refresh_token: "{{ xxxxxxxxxxxxxxx }}"

- name: Delete NetApp Cloud Manager connector for GCP
  netapp.cloudmanager.na_cloudmanager_connector_gcp:
    state: absent
    name: ansible-occm-gcp
    refresh_token: "{{ xxxxxxxxxxxxxxx }}"
    client_id: "{{ wwwwwwwwww }}"
    project_id: xxxxxxx-support
    zone: us-east4-b
    company: NetApp
    gcp_service_account_email: xxxxxxxx@xxxxxxx-support.iam.gserviceaccount.com
    gcp_service_account_path: gcp_creds.json
    account_id: account-xxxxXXXX
```

## [Return Values](na_cloudmanager_connector_gcp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **client_id**  string | Newly created GCP connector id on cloud manager.  **Returned:** success  **Sample:** `"FDQE8SwrbjVS6mqUgZoOHQmu2DvBNRRW"` |
| **client_ids**  list / elements=string | a list of client ids matching the name and provider if the connector already exists.  ideally the list should be empty, or contain a single element matching client_id.  **Returned:** success  **Sample:** `["FDQE8SwrbjVS6mqUgZoOHQmu2DvBNRRW"]` |

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.cloudmanager)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.cloudmanager)
