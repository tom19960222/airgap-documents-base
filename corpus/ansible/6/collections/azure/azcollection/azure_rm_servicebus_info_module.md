---
collection: ansible
version: "6"
title: "azure.azcollection.azure_rm_servicebus_info module – Get servicebus facts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/azure/azcollection/azure_rm_servicebus_info_module.html
fetched_at: 2026-07-27T16:47:04+00:00
---
# azure.azcollection.azure_rm_servicebus_info module – Get servicebus facts

> **Note:**
>
> This module is part of the [azure.azcollection collection](https://galaxy.ansible.com/azure/azcollection) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install azure.azcollection`.
> You need further requirements to be able to use this module,
> see [Requirements](azure_rm_servicebus_info_module.md#ansible-collections-azure-azcollection-azure-rm-servicebus-info-module-requirements) for details.
>
> To use it in a playbook, specify: `azure.azcollection.azure_rm_servicebus_info`.

New in azure.azcollection 0.1.2

- [Synopsis](azure_rm_servicebus_info_module.md#synopsis)
- [Requirements](azure_rm_servicebus_info_module.md#requirements)
- [Parameters](azure_rm_servicebus_info_module.md#parameters)
- [Notes](azure_rm_servicebus_info_module.md#notes)
- [See Also](azure_rm_servicebus_info_module.md#see-also)
- [Examples](azure_rm_servicebus_info_module.md#examples)
- [Return Values](azure_rm_servicebus_info_module.md#return-values)

## [Synopsis](azure_rm_servicebus_info_module.md#id1)

- Get facts for a specific servicebus or all servicebus in a resource group or subscription.

## [Requirements](azure_rm_servicebus_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection’s requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found <https://galaxy.ansible.com/azure/azcollection>

## [Parameters](azure_rm_servicebus_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_user**  string | Active Directory username. Use when authenticating with an Active Directory user rather than service principal. |
| **adfs_authority_url**  string  added in azure.azcollection 0.0.1 | Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority. |
| **api_profile**  string  added in azure.azcollection 0.0.1 | Selects an API profile to use when communicating with Azure services. Default value of `latest` is appropriate for public clouds; future values will allow use with Azure Stack.  Default: `"latest"` |
| **auth_source**  string  added in azure.azcollection 0.0.1 | Controls the source of the credentials to use for authentication.  Can also be set via the `ANSIBLE_AZURE_AUTH_SOURCE` environment variable.  When set to `auto` (the default) the precedence is module parameters -> `env` -> `credential_file` -> `cli`.  When set to `env`, the credentials will be read from the environment variables  When set to `credential_file`, it will read the profile from `~/.azure/credentials`.  When set to `cli`, the credentials will be sources from the Azure CLI profile. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.  When set to `msi`, the host machine must be an azure resource with an enabled MSI extension. `subscription_id` or the environment variable `AZURE_SUBSCRIPTION_ID` can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.  The `msi` was added in Ansible 2.6.  Choices:   - `"auto"` ← (default) - `"cli"` - `"credential_file"` - `"env"` - `"msi"` |
| **cert_validation_mode**  string  added in azure.azcollection 0.0.1 | Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing `ignore`. Can also be set via credential file profile or the `AZURE_CERT_VALIDATION` environment variable.  Choices:   - `"ignore"` - `"validate"` |
| **client_id**  string | Azure client ID. Use when authenticating with a Service Principal. |
| **cloud_environment**  string  added in azure.azcollection 0.0.1 | For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, `AzureChinaCloud`, `AzureUSGovernment`), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the `AZURE_CLOUD_ENVIRONMENT` environment variable.  Default: `"AzureCloud"` |
| **log_mode**  string | Parent argument. |
| **log_path**  string | Parent argument. |
| **name**  string | Limit results to a specific servicebus. |
| **namespace**  string | Servicebus namespace name.  A namespace is a scoping container for all messaging components.  Multiple queues and topics can reside within a single namespace, and namespaces often serve as application containers.  Required when *type=namespace*. |
| **password**  string | Active Directory user password. Use when authenticating with an Active Directory user rather than service principal. |
| **profile**  string | Security profile found in ~/.azure/credentials file. |
| **resource_group**  string | Limit results in a specific resource group. |
| **secret**  string | Azure client secret. Use when authenticating with a Service Principal. |
| **show_sas_policies**  boolean | Whether to show the SAS policies.  Not support when *type=subscription*.  Note if enable this option, the facts module will raise two more HTTP call for each resources, need more network overhead.  Choices:   - `false` - `true` |
| **subscription_id**  string | Your Azure subscription Id. |
| **tags**  list / elements=string | Limit results by providing a list of tags. Format tags as ‘key’ or ‘key:value’. |
| **tenant**  string | Azure tenant ID. Use when authenticating with a Service Principal. |
| **thumbprint**  string  added in azure.azcollection 1.14.0 | The thumbprint of the private key specified in *x509_certificate_path*.  Use when authenticating with a Service Principal.  Required if *x509_certificate_path* is defined. |
| **topic**  string | Topic name.  Required when *type=subscription*. |
| **type**  string | Type of the resource.  Choices:   - `"namespace"` - `"queue"` - `"topic"` - `"subscription"` |
| **x509_certificate_path**  path  added in azure.azcollection 1.14.0 | Path to the X509 certificate used to create the service principal in PEM format.  The certificate must be appended to the private key.  Use when authenticating with a Service Principal. |

## [Notes](azure_rm_servicebus_info_module.md#id4)

> **Note:**
>
> - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with `az login`.
> - Authentication is also possible using a service principal or Active Directory user.
> - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
> - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
> - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.

## [See Also](azure_rm_servicebus_info_module.md#id5)

> **See also:**
>
> [Sign in with Azure CLI](https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest)
> :   How to authenticate using the `az login` command.

## [Examples](azure_rm_servicebus_info_module.md#id6)

```yaml+jinja
- name: Get all namespaces under a resource group
  azure_rm_servicebus_info:
    resource_group: myResourceGroup
    type: namespace

- name: Get all topics under a namespace
  azure_rm_servicebus_info:
    resource_group: myResourceGroup
    namespace: bar
    type: topic

- name: Get a single queue with SAS policies
  azure_rm_servicebus_info:
    resource_group: myResourceGroup
    namespace: bar
    type: queue
    name: sbqueue
    show_sas_policies: true

- name: Get all subscriptions under a resource group
  azure_rm_servicebus_info:
    resource_group: myResourceGroup
    type: subscription
    namespace: bar
    topic: sbtopic
```

## [Return Values](azure_rm_servicebus_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **servicebuses**  complex | List of servicebus dicts.  Returned: always |
| **accessed_at**  string | Last time the message was sent, or a request was received for this topic.  Returned: always  Sample: `"2019-01-25 02:46:55.543953+00:00"` |
| **auto_delete_on_idle_in_seconds**  integer | ISO 8061 timeSpan idle interval after which the queue or topic is automatically deleted.  The minimum duration is 5 minutes.  Returned: always  Sample: `true` |
| **count_details**  complex | Message count details.  Returned: always |
| **active_message_count**  integer | Number of active messages in the `queue`, `topic`, or `subscription`.  Returned: always  Sample: `0` |
| **dead_letter_message_count**  integer | Number of messages that are dead lettered.  Returned: always  Sample: `0` |
| **scheduled_message_count**  integer | Number of scheduled messages.  Returned: always  Sample: `0` |
| **transfer_dead_letter_message_count**  integer | Number of messages transferred into dead letters.  Returned: always  Sample: `0` |
| **transfer_message_count**  integer | Number of messages transferred to another `queue`, `topic`, or `subscription`.  Returned: always  Sample: `0` |
| **created_at**  string | Exact time the message was created.  Returned: always  Sample: `"2019-01-25 02:46:55.543953+00:00"` |
| **dead_lettering_on_filter_evaluation_exceptions**  integer | Value that indicates whether a subscription has dead letter support on filter evaluation exceptions.  Returned: always  Sample: `0` |
| **dead_lettering_on_message_expiration**  integer | A value that indicates whether this `queue` or `topic` has dead letter support when a message expires.  Returned: always  Sample: `0` |
| **default_message_time_to_live_seconds**  integer | ISO 8061 Default message timespan to live value.  This is the duration after which the message expires, starting from when the message is sent to Service Bus.  This is the default value used when TimeToLive is not set on a message itself.  Returned: always  Sample: `0` |
| **duplicate_detection_time_in_seconds**  integer | ISO 8601 timeSpan structure that defines the duration of the duplicate detection history.  Returned: always  Sample: `600` |
| **enable_batched_operations**  boolean | Value that indicates whether server-side batched operations are enabled.  Returned: always  Sample: `true` |
| **enable_express**  boolean | Value that indicates whether Express Entities are enabled.  An express topic holds a message in memory temporarily before writing it to persistent storage.  Returned: always  Sample: `true` |
| **enable_partitioning**  boolean | Value that indicates whether the `queue` or `topic` to be partitioned across multiple message brokers is enabled.  Returned: always  Sample: `true` |
| **forward_dead_lettered_messages_to**  string | `queue` or `topic` name to forward the Dead Letter message.  Returned: always  Sample: `"corge"` |
| **forward_to**  string | `queue` or `topic` name to forward the messages.  Returned: always  Sample: `"quux"` |
| **id**  string | Resource ID.  Returned: always  Sample: `"/subscriptions/XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX/resourceGroups/foo/providers/Microsoft.ServiceBus/ namespaces/bar/topics/baz/subscriptions/qux"` |
| **location**  string | The Geo-location where the resource lives.  Returned: always  Sample: `"eastus"` |
| **lock_duration_in_seconds**  integer | ISO 8601 timespan duration of a peek-lock.  The amount of time that the message is locked for other receivers.  The maximum value for LockDuration is 5 minutes.  Returned: always  Sample: `60` |
| **max_delivery_count**  integer | The maximum delivery count.  A message is automatically deadlettered after this number of deliveries.  Returned: always  Sample: `10` |
| **max_size_in_mb**  integer | Maximum size of the `queue` or `topic` in megabytes, which is the size of the memory allocated for the `topic`.  Returned: always  Sample: `5120` |
| **message_count**  integer | Number of messages.  Returned: always  Sample: `10` |
| **metric_id**  string | Identifier for Azure Insights metrics of namespace.  Returned: always  Sample: `"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX:bar"` |
| **name**  string | Resource name.  Returned: always  Sample: `"qux"` |
| **namespace**  string | *namespace* name of the `queue` or `topic`, `subscription`.  Returned: always  Sample: `"bar"` |
| **provisioning_state**  string | Provisioning state of the namespace.  Returned: always  Sample: `"Succeeded"` |
| **requires_duplicate_detection**  boolean | A value indicating if this `queue` or `topic` requires duplicate detection.  Returned: always  Sample: `true` |
| **requires_session**  boolean | A value that indicates whether the `queue` or `topic` supports the concept of sessions.  Returned: always  Sample: `true` |
| **sas_policies**  dictionary | Dict of SAS policies.  Will not be returned until *show_sas_policy* set.  Returned: always  Sample: `{"testpolicy1": {"id": "/subscriptions/XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX/resourceGroups/ foo/providers/Microsoft.ServiceBus/namespaces/bar/queues/qux/authorizationRules/testpolicy1", "keys": {"key_name": "testpolicy1", "primary_connection_string": "Endpoint=sb://bar.servicebus.windows.net/; SharedAccessKeyName=testpolicy1;SharedAccessKey=XXXXXXXXXXXXXXXXX;EntityPath=qux", "primary_key": "XXXXXXXXXXXXXXXXX", "secondary_connection_string": "Endpoint=sb://bar.servicebus.windows.net/; SharedAccessKeyName=testpolicy1;SharedAccessKey=XXXXXXXXXXXXXXX;EntityPath=qux", "secondary_key": "XXXXXXXXXXXXXXX"}, "name": "testpolicy1", "rights": "listen_send", "type": "Microsoft.ServiceBus/Namespaces/Queues/AuthorizationRules"}}` |
| **service_bus_endpoint**  string | Endpoint you can use to perform Service Bus operations.  Returned: always  Sample: `"https://bar.servicebus.windows.net:443/"` |
| **size_in_bytes**  integer | The size of the `queue` or `topic` in bytes.  Returned: always  Sample: `0` |
| **sku**  string | Properties of namespace’s SKU.  Returned: always  Sample: `"Standard"` |
| **status**  string | The status of a messaging entity.  Returned: always  Sample: `"active"` |
| **subscription_count**  integer | Number of subscriptions under a topic.  Returned: always  Sample: `1` |
| **support_ordering**  boolean | Value that indicates whether the `topic` supports ordering.  Returned: always  Sample: `true` |
| **tags**  dictionary | Resource tags.  Returned: always  Sample: `{"env": "sandbox"}` |
| **topic**  string | Topic name of a subscription.  Returned: always  Sample: `"baz"` |
| **type**  string | Resource type.  Namespace is a scoping container for all messaging components.  Queue enables you to store messages until the receiving application is available to receive and process them.  Topic and subscriptions enable 1:n relationships between publishers and subscribers.  Returned: always  Sample: `"Microsoft.ServiceBus/Namespaces/Topics"` |
| **updated_at**  string | The exact time the message was updated.  Returned: always  Sample: `"2019-01-25 02:46:55.543953+00:00"` |

### Authors

- Yuwei Zhou (@yuwzho)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/azure/issues)
[Homepage](https://azure.microsoft.com)
[Repository (Sources)](https://github.com/ansible-collections/azure)
