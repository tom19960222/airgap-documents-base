---
collection: ansible
version: "8"
title: "dellemc.openmanage.ome_identity_pool module – Manages identity pool settings on OpenManage Enterprise"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/ome_identity_pool_module.html
fetched_at: 2026-07-28T02:04:39+00:00
---
# dellemc.openmanage.ome_identity_pool module – Manages identity pool settings on OpenManage Enterprise

> **Note:**
>
> This module is part of the [dellemc.openmanage collection](https://galaxy.ansible.com/ui/repo/published/dellemc/openmanage/) (version 7.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.openmanage`.
> You need further requirements to be able to use this module,
> see [Requirements](ome_identity_pool_module.md#ansible-collections-dellemc-openmanage-ome-identity-pool-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_identity_pool`.

New in dellemc.openmanage 2.1.0

- [Synopsis](ome_identity_pool_module.md#synopsis)
- [Requirements](ome_identity_pool_module.md#requirements)
- [Parameters](ome_identity_pool_module.md#parameters)
- [Notes](ome_identity_pool_module.md#notes)
- [Examples](ome_identity_pool_module.md#examples)
- [Return Values](ome_identity_pool_module.md#return-values)

## [Synopsis](ome_identity_pool_module.md#id1)

- This module allows to create, modify, or delete a single identity pool on OpenManage Enterprise.

## [Requirements](ome_identity_pool_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_identity_pool_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **ethernet_settings**  dictionary | Applicable for creating and modifying an identity pool using Ethernet settings.  *starting_mac_address* and *identity_count* are required to create an identity pool. |
| **identity_count**  integer | Number of MAC addresses. |
| **starting_mac_address**  string | Starting MAC address of the ethernet setting. |
| **fc_settings**  dictionary | Applicable for creating and modifying an identity pool using fibre channel(FC) settings.  This option allows OpenManage Enterprise to generate a Worldwide port name (WWPN) and Worldwide node name (WWNN) address.  The value 0x2001 is beginning to the starting address for the generation of a WWPN, and 0x2000 for a WWNN.  *starting_address* and *identity_count* are required to create an identity pool. |
| **identity_count**  integer | Number of MAC addresses.*identity_count* is required to option to create FC settings. |
| **starting_address**  string | Starting MAC Address of FC setting.*starting_address* is required to option to create FC settings. |
| **fcoe_settings**  dictionary | Applicable for creating and modifying an identity pool using FCoE settings.  *starting_mac_address* and *identity_count* are required to create an identity pool. |
| **identity_count**  integer | Number of MAC addresses. |
| **starting_mac_address**  string | Starting MAC Address of the FCoE setting. |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **iscsi_settings**  dictionary | Applicable for creating and modifying an identity pool using ISCSI settings.  *starting_mac_address*, *identity_count*, *iqn_prefix*, *ip_range* and *subnet_mask* are required to create an identity pool. |
| **identity_count**  integer | Number of MAC addresses. |
| **initiator_config**  dictionary | Applicable for creating and modifying an identity pool using iSCSI Initiator settings. |
| **iqn_prefix**  string | IQN prefix addresses. |
| **initiator_ip_pool_settings**  dictionary | Applicable for creating and modifying an identity pool using ISCSI Initiator IP pool settings. |
| **gateway**  string | IP address of gateway. |
| **ip_range**  string | Range of non-multicast IP addresses. |
| **primary_dns_server**  string | IP address of the primary DNS server. |
| **secondary_dns_server**  string | IP address of the secondary DNS server. |
| **subnet_mask**  string | Subnet mask for *ip_range*. |
| **starting_mac_address**  string | Starting MAC address of the iSCSI setting.This is required option for iSCSI setting. |
| **new_pool_name**  string | After creating an identity pool, *pool_name* can be changed to *new_pool_name*.  This option is ignored when creating an identity pool. |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **pool_description**  string | Description of the identity pool. |
| **pool_name**  string / required | This option is mandatory for *state* when creating, modifying and deleting an identity pool. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  **Default:** `443` |
| **state**  string | `present` modifies an existing identity pool. If the provided I (pool_name) does not exist, it creates an identity pool. - `absent` deletes an existing identity pool.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ome_identity_pool_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Dell OpenManage Enterprise.
> - This module supports `check_mode`.

## [Examples](ome_identity_pool_module.md#id5)

```yaml+jinja
---
- name: Create an identity pool using ethernet, FCoE, iSCSI and FC settings
  dellemc.openmanage.ome_identity_pool:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: present
    pool_name: "pool1"
    pool_description: "Identity pool with Ethernet, FCoE, iSCSI and FC settings"
    ethernet_settings:
        starting_mac_address: "50:50:50:50:50:00"
        identity_count: 60
    fcoe_settings:
        starting_mac_address: "70:70:70:70:70:00"
        identity_count: 75
    iscsi_settings:
        starting_mac_address: "60:60:60:60:60:00"
        identity_count: 30
        initiator_config:
            iqn_prefix: "iqn.myprefix."
        initiator_ip_pool_settings:
            ip_range: "10.33.0.1-10.33.0.255"
            subnet_mask: "255.255.255.0"
            gateway: "192.168.4.1"
            primary_dns_server : "10.8.8.8"
            secondary_dns_server : "8.8.8.8"
    fc_settings:
        starting_address: "30:30:30:30:30:00"
        identity_count: 45

- name: Create an identity pool using only ethernet settings
  dellemc.openmanage.ome_identity_pool:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    pool_name: "pool2"
    pool_description: "create identity pool with ethernet"
    ethernet_settings:
        starting_mac_address: "aa-bb-cc-dd-ee-aa"
        identity_count: 80

- name: Modify an identity pool
  dellemc.openmanage.ome_identity_pool:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    pool_name: "pool2"
    new_pool_name: "pool3"
    pool_description: "modifying identity pool with ethernet and fcoe settings"
    ethernet_settings:
        starting_mac_address: "90-90-90-90-90-90"
        identity_count: 61
    fcoe_settings:
        starting_mac_address: "aabb.ccdd.5050"
        identity_count: 77

- name: Modify an identity pool using iSCSI and FC settings
  dellemc.openmanage.ome_identity_pool:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    ca_path: "/path/to/ca_cert.pem"
    pool_name: "pool_new"
    new_pool_name: "pool_new2"
    pool_description: "modifying identity pool with iscsi and fc settings"
    iscsi_settings:
      identity_count: 99
      initiator_config:
        iqn_prefix: "iqn1.myprefix2."
      initiator_ip_pool_settings:
        gateway: "192.168.4.5"
    fc_settings:
      starting_address: "10:10:10:10:10:10"
      identity_count: 98

- name: Delete an identity pool
  dellemc.openmanage.ome_identity_pool:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: "absent"
    pool_name: "pool2"
```

## [Return Values](ome_identity_pool_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred: Ethernet-MAC Range overlap found (in this Identity Pool or in a different one) .", "MessageArgs": ["Ethernet-MAC Range overlap found (in this Identity Pool or in a different one)\""], "MessageId": "CGEN6001", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Overall status of the identity pool operation.  **Returned:** always  **Sample:** `"Successfully created an identity pool."` |
| **pool_status**  dictionary | Details of the user operation, when *state* is `present`.  **Returned:** success  **Sample:** `{"Id": 29, "IsSuccessful": true, "Issues": []}` |

### Authors

- Sajna Shetty(@Sajna-Shetty)
- Deepak Joshi(@Dell-Deepak-Joshi))

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
