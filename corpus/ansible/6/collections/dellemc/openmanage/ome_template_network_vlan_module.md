---
collection: ansible
version: "6"
title: "dellemc.openmanage.ome_template_network_vlan module – Set tagged and untagged vlans to native network card supported by a template on OpenManage Enterprise"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/ome_template_network_vlan_module.html
fetched_at: 2026-07-27T17:25:52+00:00
---
# dellemc.openmanage.ome_template_network_vlan module – Set tagged and untagged vlans to native network card supported by a template on OpenManage Enterprise

> **Note:**
>
> This module is part of the [dellemc.openmanage collection](https://galaxy.ansible.com/dellemc/openmanage) (version 5.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.openmanage`.
> You need further requirements to be able to use this module,
> see [Requirements](ome_template_network_vlan_module.md#ansible-collections-dellemc-openmanage-ome-template-network-vlan-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_template_network_vlan`.

New in dellemc.openmanage 2.0.0

- [Synopsis](ome_template_network_vlan_module.md#synopsis)
- [Requirements](ome_template_network_vlan_module.md#requirements)
- [Parameters](ome_template_network_vlan_module.md#parameters)
- [Notes](ome_template_network_vlan_module.md#notes)
- [Examples](ome_template_network_vlan_module.md#examples)
- [Return Values](ome_template_network_vlan_module.md#return-values)

## [Synopsis](ome_template_network_vlan_module.md#id1)

- This module allows to set tagged and untagged vlans to native network card supported by a template on OpenManage Enterprise.

## [Requirements](ome_template_network_vlan_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_template_network_vlan_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **nic_identifier**  string / required | Display name of NIC port in the template for VLAN configuration. |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  Default: `443` |
| **propagate_vlan**  boolean  added in dellemc.openmanage 3.4.0 | To deploy the modified VLAN settings immediately without rebooting the server.  This option will be applied only when there are changes to the VLAN configuration.  Choices:   - `false` - `true` ← (default) |
| **tagged_networks**  list / elements=dictionary | List of tagged VLANs and their corresponding NIC ports. |
| **port**  integer / required | NIC port number of the tagged VLAN |
| **tagged_network_ids**  list / elements=integer | List of IDs of the tagged VLANs  Enter [] to remove the tagged VLAN from a port.  List of *tagged_network_ids* is combined with list of *tagged_network_names* when adding tagged VLANs to a port.  To get the VLAN network ID use the API %20https://I%28hostname/api/NetworkConfigurationService/Networks) |
| **tagged_network_names**  list / elements=string | List of names of tagged VLANs  Enter [] to remove the tagged VLAN from a port.  List of *tagged_network_names* is combined with list of *tagged_network_ids* when adding tagged VLANs to a port. |
| **template_id**  integer | Id of the template.  It is mutually exclusive with *template_name*. |
| **template_name**  string | Name of the template.  It is mutually exclusive with *template_id*. |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **untagged_networks**  list / elements=dictionary | List of untagged networks and their corresponding NIC ports. |
| **port**  integer / required | NIC port number of the untagged VLAN. |
| **untagged_network_id**  integer | ID of the untagged VLAN  Enter 0 to clear the untagged VLAN from the port.  This option is mutually exclusive with *untagged_network_name*  To get the VLAN network ID use the API %20https://I%28hostname/api/NetworkConfigurationService/Networks) |
| **untagged_network_name**  string | name of the vlan for untagging  provide 0 for clearing the untagging for this *port*  This parameter is mutually exclusive with *untagged_network_id* |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](ome_template_network_vlan_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to DellEMC OpenManage Enterprise.
> - This module supports `check_mode`.

## [Examples](ome_template_network_vlan_module.md#id5)

```yaml+jinja
---
- name: Add tagged or untagged VLANs to a template using VLAN ID and name
  dellemc.openmanage.ome_template_network_vlan:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    template_id: 78
    nic_identifier: NIC Slot 4
    untagged_networks:
      - port: 1
        untagged_network_id: 127656
      - port: 2
        untagged_network_name: vlan2
    tagged_networks:
      - port: 1
        tagged_network_ids:
          - 12767
          - 12768
      - port: 4
        tagged_network_ids:
          - 12767
          - 12768
        tagged_network_names:
          - vlan3
      - port: 2
        tagged_network_names:
          - vlan4
          - vlan1

- name: Clear the tagged and untagged VLANs from a template
  dellemc.openmanage.ome_template_network_vlan:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    template_id: 78
    nic_identifier: NIC Slot 4
    untagged_networks:
      # For removing the untagged VLANs for the port 1 and 2
      - port: 1
        untagged_network_id: 0
      - port: 2
        untagged_network_name: 0
    tagged_networks:
      # For removing the tagged VLANs for port 1, 4 and 2
      - port: 1
        tagged_network_ids: []
      - port: 4
        tagged_network_ids: []
        tagged_network_names: []
      - port: 2
        tagged_network_names: []
```

## [Return Values](ome_template_network_vlan_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  Returned: on HTTP error  Sample: `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to complete the request because TemplateId  does not exist or is not applicable for the resource URI.", "MessageArgs": ["TemplateId"], "MessageId": "CGEN1004", "RelatedProperties": [], "Resolution": "Check the request resource URI. Refer to the OpenManage Enterprise-Modular User's Guide for more information about resource URI and its properties.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Overall status of the template vlan operation.  Returned: always  Sample: `"Successfully applied the network settings to template."` |

### Authors

- Jagadeesh N V(@jagadeeshnv)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
