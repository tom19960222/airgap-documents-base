---
collection: ansible
version: "8"
title: "azure.azcollection.azure_rm_iothub_info module – Get IoT Hub facts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/azure/azcollection/azure_rm_iothub_info_module.html
fetched_at: 2026-07-28T01:13:34+00:00
---
# azure.azcollection.azure_rm_iothub_info module – Get IoT Hub facts

> **Note:**
>
> This module is part of the [azure.azcollection collection](https://galaxy.ansible.com/ui/repo/published/azure/azcollection/) (version 1.19.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install azure.azcollection`.
> You need further requirements to be able to use this module,
> see [Requirements](azure_rm_iothub_info_module.md#ansible-collections-azure-azcollection-azure-rm-iothub-info-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_iothub_info`.

New in azure.azcollection 0.1.2

- [Synopsis](azure_rm_iothub_info_module.md#synopsis)
- [Requirements](azure_rm_iothub_info_module.md#requirements)
- [Parameters](azure_rm_iothub_info_module.md#parameters)
- [Notes](azure_rm_iothub_info_module.md#notes)
- [See Also](azure_rm_iothub_info_module.md#see-also)
- [Examples](azure_rm_iothub_info_module.md#examples)
- [Return Values](azure_rm_iothub_info_module.md#return-values)

## [Synopsis](azure_rm_iothub_info_module.md#id1)

- Get facts for a specific IoT Hub or all IoT Hubs.

## [Requirements](azure_rm_iothub_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_iothub_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  *added in azure.azcollection 0.0.1* | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  *added in azure.azcollection 0.0.1* | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  **Default:** `"latest"` |
| **auth_source**  string  *added in azure.azcollection 0.0.1* | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  **Choices:**   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **cert_validation_mode**  string  *added in azure.azcollection 0.0.1* | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  **Choices:**   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  *added in azure.azcollection 0.0.1* | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  **Default:** `"AzureCloud"` |
| **list_consumer_groups**  boolean | List the consumer group of the built-in event hub.  **Choices:**   - `false` - `true` |
| **list_keys**  boolean | List the keys of IoT Hub.  Note this will have network overhead for each IoT Hub.  **Choices:**   - `false` - `true` |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **name**  string | Limit results to a specific resource group. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **resource_group**  string | The resource group to search for the desired IoT Hub. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **show_endpoint_health**  boolean | Get the health for routing endpoints.  Note this will have network overhead for each IoT Hub.  **Choices:**   - `false` - `true` |
| **show_quota_metrics**  boolean | Get the quota metrics for an IoT hub.  Note this will have network overhead for each IoT Hub.  **Choices:**   - `false` - `true` |
| **show_stats**  boolean | Show the statistics for IoT Hub.  Note this will have network overhead for each IoT Hub.  **Choices:**   - `false` - `true` |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  list / elements=string | Limit results by providing a list of tags. Format tags as ‘key’ or ‘key:value’. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **test_route_message**  string | Test routes message. It will be used to test all routes. |
| **thumbprint**  string  *added in azure.azcollection 1.14.0* | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **x509_certificate_path**  path  *added in azure.azcollection 1.14.0* | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_iothub_info_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_iothub_info_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_iothub_info_module.md#id6)

```yaml+jinja
- name: Get facts for one IoT Hub
  azure_rm_iothub_info:
    name: Testing
    resource_group: myResourceGroup

- name: Get facts for all IoT Hubs
  azure_rm_iothub_info:

- name: Get facts for all IoT Hubs in a specific resource group
  azure_rm_iothub_info:
    resource_group: myResourceGroup

- name: Get facts by tags
  azure_rm_iothub_info:
    tags:
      - testing
```

## [Return Values](azure_rm_iothub_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **azure_iothubs**  complex | List of IoT Hub dicts.  **Returned:** always |
| **cloud_to_device**  complex | Cloud to device message properties.  **Returned:** always |
| **max_delivery_count**  integer | The number of times the IoT hub attempts to deliver a message on the feedback queue.  See <https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging#cloud-to-device-messages>.  **Returned:** always  **Sample:** `10` |
| **ttl_as_iso8601**  string | The period of time for which a message is available to consume before it is expired by the IoT hub.  See <https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging#cloud-to-device-messages>.  **Returned:** always  **Sample:** `"1:00:00"` |
| **enable_file_upload_notifications**  string | Whether file upload notifications are enabled.  **Returned:** always  **Sample:** `"True"` |
| **event_endpoints**  complex | Built-in endpoint where to deliver device message.  **Returned:** always |
| **endpoint**  string | The Event Hub-compatible endpoint.  **Returned:** always  **Sample:** `"sb://iothub-ns-testing-1478811-9bbc4a15f0.servicebus.windows.net/"` |
| **partition_count**  integer | The number of partitions for receiving device-to-cloud messages in the Event Hub-compatible endpoint.  See <https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging#device-to-cloud-messages>.  **Returned:** always  **Sample:** `2` |
| **partition_ids**  list / elements=string | List of the partition id for the event endpoint.  **Returned:** always  **Sample:** `["0", "1"]` |
| **retention_time_in_days**  integer | The retention time for device-to-cloud messages in days.  See <https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging#device-to-cloud-messages>.  **Returned:** always  **Sample:** `1` |
| **host_name**  string | Host of the IoT hub.  **Returned:** always  **Sample:** `"testing.azure-devices.net"` |
| **id**  string | Resource ID of the IoT hub.  **Returned:** always  **Sample:** `"/subscriptions/XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX/resourceGroups/myResourceGroup/providers/Microsoft.Devices/IotHubs/Testing"` |
| **ip_filters**  complex | Configure rules for rejecting or accepting traffic from specific IPv4 addresses.  **Returned:** always |
| **action**  string | The desired action for requests captured by this rule.  **Returned:** always  **Sample:** `"Reject"` |
| **ip_mask**  string | A string that contains the IP address range in CIDR notation for the rule.  **Returned:** always  **Sample:** `"40.54.7.3"` |
| **name**  string | Name of the filter.  **Returned:** always  **Sample:** `"filter"` |
| **location**  string | Location of the IoT hub.  **Returned:** always  **Sample:** `"eastus"` |
| **name**  string | Name of the IoT hub.  **Returned:** always  **Sample:** `"Testing"` |
| **resource_group**  string | Resource group of the IoT hub.  **Returned:** always  **Sample:** `"myResourceGroup."` |
| **routes**  complex | Route device-to-cloud messages to service-facing endpoints.  **Returned:** always |
| **condition**  boolean | The query expression for the routing query that is run against the message application properties, system properties, message body, device twin tags, and device twin properties to determine if it is a match for the endpoint.  For more information about constructing a query, see <https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-routing-query-syntax>  **Returned:** always  **Sample:** `true` |
| **enabled**  boolean | Whether to enable the route.  **Returned:** always  **Sample:** `true` |
| **endpoint_name**  string | The name of the endpoint in *routing_endpoints* where IoT Hub sends messages that match the query.  **Returned:** always  **Sample:** `"foo"` |
| **name**  string | Name of the route.  **Returned:** always  **Sample:** `"route1"` |
| **source**  string | The origin of the data stream to be acted upon.  **Returned:** always  **Sample:** `"device_messages"` |
| **routing_endpoints**  complex | Custom endpoints.  **Returned:** always |
| **event_hubs**  complex | List of custom endpoints of event hubs.  **Returned:** always |
| **connection_string**  string | Connection string of the custom endpoint.  **Returned:** always  **Sample:** `"Endpoint=sb://quux.servicebus.windows.net:5671/;SharedAccessKeyName=qux;SharedAccessKey=****;EntityPath=foo"` |
| **name**  string | Name of the custom endpoint.  **Returned:** always  **Sample:** `"foo"` |
| **resource_group**  string | Resource group of the endpoint.  **Returned:** always  **Sample:** `"bar"` |
| **subscription**  string | Subscription ID of the endpoint.  **Returned:** always  **Sample:** `"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"` |
| **service_bus_queues**  complex | List of custom endpoints of service bus queue.  **Returned:** always |
| **connection_string**  string | Connection string of the custom endpoint.  **Returned:** always  **Sample:** `"Endpoint=sb://quux.servicebus.windows.net:5671/;SharedAccessKeyName=qux;SharedAccessKey=****;EntityPath=foo"` |
| **name**  string | Name of the custom endpoint.  **Returned:** always  **Sample:** `"foo"` |
| **resource_group**  string | Resource group of the endpoint.  **Returned:** always  **Sample:** `"bar"` |
| **subscription**  string | Subscription ID of the endpoint.  **Returned:** always  **Sample:** `"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"` |
| **service_bus_topics**  complex | List of custom endpoints of service bus topic.  **Returned:** always |
| **connection_string**  string | Connection string of the custom endpoint.  **Returned:** always  **Sample:** `"Endpoint=sb://quux.servicebus.windows.net:5671/;SharedAccessKeyName=qux;SharedAccessKey=****;EntityPath=foo"` |
| **name**  string | Name of the custom endpoint.  **Returned:** always  **Sample:** `"foo"` |
| **resource_group**  string | Resource group of the endpoint.  **Returned:** always  **Sample:** `"bar"` |
| **subscription**  string | Subscription ID of the endpoint.  **Returned:** always  **Sample:** `"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"` |
| **storage_containers**  complex | List of custom endpoints of storage.  **Returned:** always |
| **connection_string**  string | Connection string of the custom endpoint.  **Returned:** always  **Sample:** `"Endpoint=sb://quux.servicebus.windows.net:5671/;SharedAccessKeyName=qux;SharedAccessKey=****;EntityPath=foo"` |
| **name**  string | Name of the custom endpoint.  **Returned:** always  **Sample:** `"foo"` |
| **resource_group**  string | Resource group of the endpoint.  **Returned:** always  **Sample:** `"bar"` |
| **subscription**  string | Subscription ID of the endpoint.  **Returned:** always  **Sample:** `"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"` |
| **sku**  string | Pricing tier for Azure IoT Hub.  **Returned:** always  **Sample:** `"f1"` |
| **tags**  dictionary | Limit results by providing a list of tags. Format tags as ‘key’ or ‘key:value’.  **Returned:** always  **Sample:** `{"key1": "value1"}` |
| **unit**  integer | Units in the IoT Hub.  **Returned:** always  **Sample:** `1` |

### Authors

- Yuwei Zhou (@yuwzho)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/azure/issues)
- [Homepage](https://azure.microsoft.com)
- [Repository (Sources)](https://github.com/ansible-collections/azure)
