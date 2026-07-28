---
collection: ansible
version: "8"
title: "dellemc.openmanage.ome_template_network_vlan_info module – Retrieves network configuration of template."
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/ome_template_network_vlan_info_module.html
fetched_at: 2026-07-28T02:04:53+00:00
---
# dellemc.openmanage.ome_template_network_vlan_info module – Retrieves network configuration of template.

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
> see [Requirements](ome_template_network_vlan_info_module.md#ansible-collections-dellemc-openmanage-ome-template-network-vlan-info-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_template_network_vlan_info`.

New in dellemc.openmanage 7.2.0

- [Synopsis](ome_template_network_vlan_info_module.md#synopsis)
- [Requirements](ome_template_network_vlan_info_module.md#requirements)
- [Parameters](ome_template_network_vlan_info_module.md#parameters)
- [Notes](ome_template_network_vlan_info_module.md#notes)
- [Examples](ome_template_network_vlan_info_module.md#examples)
- [Return Values](ome_template_network_vlan_info_module.md#return-values)

## [Synopsis](ome_template_network_vlan_info_module.md#id1)

- This module retrieves the network configuration of a template on OpenManage Enterprise or OpenManage Enterprise Modular.

## [Requirements](ome_template_network_vlan_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.9.6

## [Parameters](ome_template_network_vlan_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  **Default:** `443` |
| **template_id**  integer | Id of the template.  This is mutually exclusive with *template_name*. |
| **template_name**  string | Name of the template.  This is mutually exclusive with *template_id*.  `Note` If *template_id* or *template_name* option is not provided, the module retrieves network VLAN info of all templates. |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ome_template_network_vlan_info_module.md#id4)

> **Note:**
>
> - Run this module on a system that has direct access to Dell OpenManage Enterprise.
> - This module supports `check_mode`.

## [Examples](ome_template_network_vlan_info_module.md#id5)

```yaml+jinja
---
- name: Retrieve network details of all templates.
  dellemc.openmanage.ome_template_network_vlan_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"

- name: Retrieve network details using template ID
  dellemc.openmanage.ome_template_network_vlan_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    template_id: 1234

- name: Retrieve network details using template name
  dellemc.openmanage.ome_template_network_vlan_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    template_name: template1
```

## [Return Values](ome_template_network_vlan_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Status of template VLAN information retrieval.  **Returned:** always  **Sample:** `"Successfully retrieved the template network VLAN information."` |
| **vlan_info**  list / elements=dictionary | Information about the template network VLAN.  **Returned:** success  **Sample:** `[{"NicBondingTechnology": "LACP", "NicModel": {"NIC in Mezzanine 1A": {"1": {"NIC Bonding Enabled": "true", "Port": 1, "Vlan Tagged": ["32656", "32658"], "Vlan UnTagged": "25367"}, "2": {"NIC Bonding Enabled": "false", "Port": 2, "Vlan Tagged": ["21474"], "Vlan UnTagged": "32656"}}, "NIC in Mezzanine 1B": {"1": {"NICBondingEnabled": "false", "Port": 1, "Vlan Tagged": ["25367", "32656", "32658", "26898"], "Vlan UnTagged": "21474"}, "2": {"NIC Bonding Enabled": "true", "Port": 2, "Vlan Tagged": [], "Vlan UnTagged": "32658"}}}, "TemplateId": 58, "TemplateName": "t2"}]` |

### Authors

- Jagadeesh N V(@jagadeeshnv)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
