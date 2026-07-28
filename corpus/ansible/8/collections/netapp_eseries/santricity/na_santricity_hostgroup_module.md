---
collection: ansible
version: "8"
title: "netapp_eseries.santricity.na_santricity_hostgroup module – NetApp E-Series manage array host groups"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp_eseries/santricity/na_santricity_hostgroup_module.html
fetched_at: 2026-07-28T02:44:11+00:00
---
# netapp_eseries.santricity.na_santricity_hostgroup module – NetApp E-Series manage array host groups

> **Note:**
>
> This module is part of the [netapp_eseries.santricity collection](https://galaxy.ansible.com/ui/repo/published/netapp_eseries/santricity/) (version 1.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp_eseries.santricity`.
>
> To use it in a playbook, specify: `netapp_eseries.santricity.na_santricity_hostgroup`.

- [Synopsis](na_santricity_hostgroup_module.md#synopsis)
- [Parameters](na_santricity_hostgroup_module.md#parameters)
- [Notes](na_santricity_hostgroup_module.md#notes)
- [Examples](na_santricity_hostgroup_module.md#examples)
- [Return Values](na_santricity_hostgroup_module.md#return-values)

## [Synopsis](na_santricity_hostgroup_module.md#id1)

- Create, update or destroy host groups on a NetApp E-Series storage array.

## [Parameters](na_santricity_hostgroup_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API.  Example <https://prod-1.wahoo.acme.com:8443/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **hosts**  list / elements=string | List of host names/labels to add to the group |
| **name**  string | Name of the host group to manage |
| **ssid**  string | The ID of the array to manage. This value must be unique for each array.  **Default:** `"1"` |
| **state**  string | Whether the specified host group should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Should https certificates be validated?  **Choices:**   - `false` - `true` ← (default) |

## [Notes](na_santricity_hostgroup_module.md#id3)

> **Note:**
>
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing “M(netapp_e_storage_system)” at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](na_santricity_hostgroup_module.md#id4)

```yaml+jinja
- name: Configure Hostgroup
  na_santricity_hostgroup:
    ssid: "1"
    api_url: "https://192.168.1.100:8443/devmgr/v2"
    api_username: "admin"
    api_password: "adminpass"
    validate_certs: true
    state: present
    name: example_hostgroup
    hosts:
      - host01
      - host02
```

## [Return Values](na_santricity_hostgroup_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **clusterRef**  string | The unique identification value for this object. Other objects may use this reference value to refer to the cluster.  **Returned:** always except when state is absent  **Sample:** `"3233343536373839303132333100000000000000"` |
| **confirmLUNMappingCreation**  boolean | If true, indicates that creation of LUN-to-volume mappings should require careful confirmation from the end-user, since such a mapping will alter the volume access rights of other clusters, in addition to this one.  **Returned:** always  **Sample:** `false` |
| **hosts**  list / elements=string | A list of the hosts that are part of the host group after all operations.  **Returned:** always except when state is absent  **Sample:** `["HostA", "HostB"]` |
| **id**  string | The id number of the hostgroup  **Returned:** always except when state is absent  **Sample:** `"3233343536373839303132333100000000000000"` |
| **isSAControlled**  boolean | If true, indicates that I/O accesses from this cluster are subject to the storage array’s default LUN-to-volume mappings. If false, indicates that I/O accesses from the cluster are subject to cluster-specific LUN-to-volume mappings.  **Returned:** always except when state is absent  **Sample:** `false` |
| **label**  string | The user-assigned, descriptive label string for the cluster.  **Returned:** always  **Sample:** `"MyHostGroup"` |
| **name**  string | same as label  **Returned:** always except when state is absent  **Sample:** `"MyHostGroup"` |
| **protectionInformationCapableAccessMethod**  boolean | This field is true if the host has a PI capable access method.  **Returned:** always except when state is absent  **Sample:** `true` |

### Authors

- Kevin Hulquest (@hulquest)
- Nathan Swartz (@ndswartz)

### Collection links

- [Issue Tracker](https://github.com/netappeseries/santricity/issues)
- [Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
