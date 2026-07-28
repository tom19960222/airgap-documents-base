---
collection: ansible
version: "6"
title: "netapp.cloudmanager.na_cloudmanager_connector_aws module – NetApp Cloud Manager connector for AWS"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/cloudmanager/na_cloudmanager_connector_aws_module.html
fetched_at: 2026-07-27T17:55:54+00:00
---
# netapp.cloudmanager.na_cloudmanager_connector_aws module – NetApp Cloud Manager connector for AWS

> **Note:**
>
> This module is part of the [netapp.cloudmanager collection](https://galaxy.ansible.com/netapp/cloudmanager) (version 21.21.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.cloudmanager`.
>
> To use it in a playbook, specify: `netapp.cloudmanager.na_cloudmanager_connector_aws`.

New in netapp.cloudmanager 21.3.0

- [Synopsis](na_cloudmanager_connector_aws_module.md#synopsis)
- [Parameters](na_cloudmanager_connector_aws_module.md#parameters)
- [Notes](na_cloudmanager_connector_aws_module.md#notes)
- [Examples](na_cloudmanager_connector_aws_module.md#examples)
- [Return Values](na_cloudmanager_connector_aws_module.md#return-values)

## [Synopsis](na_cloudmanager_connector_aws_module.md#id1)

- Create or delete Cloud Manager connector for AWS.
- This module requires to be authenticated with AWS. This can be done with `aws configure`.

## [Parameters](na_cloudmanager_connector_aws_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **account_id**  string | The NetApp tenancy account ID. |
| **ami**  string | The image ID. |
| **associate_public_ip_address**  boolean | Indicates whether to associate a public IP address to the instance. If not provided, the association will be done based on the subnet’s configuration.  Choices:   - `false` - `true` ← (default) |
| **aws_tag**  list / elements=dictionary | Additional tags for the AWS EC2 instance. |
| **tag_key**  string | The key of the tag. |
| **tag_value**  string | The tag value. |
| **client_id**  string | The unique client ID of the Connector.  The connector ID. |
| **company**  string | The name of the company of the user. |
| **enable_termination_protection**  boolean | Indicates whether to enable termination protection on the instance.  Choices:   - `false` ← (default) - `true` |
| **environment**  string  added in netapp.cloudmanager 21.8.0 | The environment for NetApp Cloud Manager API operations.  Choices:   - `"prod"` ← (default) - `"stage"` |
| **feature_flags**  dictionary  added in netapp.cloudmanager 21.11.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **iam_instance_profile_name**  string | The name of the instance profile for the Connector. |
| **instance_id**  string | The ID of the EC2 instance used for delete. |
| **instance_type**  string | The type of instance (for example, t3.xlarge). At least 4 CPU and 16 GB of memory are required.  Default: `"t3.xlarge"` |
| **key_name**  string | The name of the key pair to use for the Connector instance. |
| **name**  string / required | The name of the Cloud Manager connector for AWS to manage. |
| **proxy_certificates**  list / elements=string  added in netapp.cloudmanager 21.5.0 | The proxy certificates, a list of certificate file names. |
| **proxy_password**  string | The proxy password, if using a proxy to connect to the internet. |
| **proxy_url**  string | The proxy URL, if using a proxy to connect to the internet. |
| **proxy_user_name**  string | The proxy user name, if using a proxy to connect to the internet. |
| **refresh_token**  string | The refresh token for NetApp Cloud Manager API operations. |
| **region**  string / required | The region where the Cloud Manager Connector will be created. |
| **sa_client_id**  string | The service account secret client ID for NetApp Cloud Manager API operations. |
| **sa_secret_key**  string | The service account secret key for NetApp Cloud Manager API operations. |
| **security_group_ids**  list / elements=string | The IDs of the security groups for the instance, multiple security groups can be provided separated by ‘,’. |
| **state**  string | Whether the specified Cloud Manager connector for AWS should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **subnet_id**  string | The ID of the subnet for the instance. |

## [Notes](na_cloudmanager_connector_aws_module.md#id3)

> **Note:**
>
> - Support check_mode.
> - The modules prefixed with na_cloudmanager are built to manage CloudManager and CVO deployments in AWS/GCP/Azure clouds.
> - If sa_client_id and sa_secret_key are provided, service account will be used in operations. refresh_token will be ignored.

## [Examples](na_cloudmanager_connector_aws_module.md#id4)

```yaml+jinja
- name: Create NetApp Cloud Manager connector for AWS
  netapp.cloudmanager.na_cloudmanager_connector_aws:
    state: present
    refresh_token: "{{ xxxxxxxxxxxxxxx }}"
    name: bsuhas_ansible_occm
    region: us-west-1
    key_name: dev_automation
    subnet_id: subnet-xxxxx
    security_group_ids: [sg-xxxxxxxxxxx]
    iam_instance_profile_name: OCCM_AUTOMATION
    account_id: "{{ account-xxxxxxx }}"
    company: NetApp
    proxy_url: abc.com
    proxy_user_name: xyz
    proxy_password: abcxyz
    proxy_certificates: [abc.crt.txt, xyz.crt.txt]
    aws_tag: [
        {tag_key: abc,
        tag_value: a123}]

- name: Delete NetApp Cloud Manager connector for AWS
  netapp.cloudmanager.na_cloudmanager_connector_aws:
    state: absent
    name: ansible
    region: us-west-1
    account_id: "{{ account-xxxxxxx }}"
    instance_id: i-xxxxxxxxxxxxx
    client_id: xxxxxxxxxxxxxxxxxxx
```

## [Return Values](na_cloudmanager_connector_aws_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ids**  dictionary | Newly created AWS client ID in cloud manager, instance ID and account ID.  Returned: success |

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.cloudmanager)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.cloudmanager)
