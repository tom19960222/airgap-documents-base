---
collection: ansible
version: "8"
title: "dellemc.openmanage.idrac_gather_facts role – Role to get the facts from the iDRAC Server"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/idrac_gather_facts_role.html
fetched_at: 2026-07-28T02:05:02+00:00
---
# dellemc.openmanage.idrac_gather_facts role – Role to get the facts from the iDRAC Server

> **Note:**
>
> This role is part of the [dellemc.openmanage collection](https://galaxy.ansible.com/ui/repo/published/dellemc/openmanage/) (version 7.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it use: `ansible-galaxy collection install dellemc.openmanage`.
>
> To use it in a playbook, specify: `dellemc.openmanage.idrac_gather_facts`.

- [Entry point `main` – Role to get the facts from the iDRAC Server](idrac_gather_facts_role.md#entry-point-main-role-to-get-the-facts-from-the-idrac-server)

  - [Synopsis](idrac_gather_facts_role.md#synopsis)
  - [Parameters](idrac_gather_facts_role.md#parameters)

## [Entry point `main` – Role to get the facts from the iDRAC Server](idrac_gather_facts_role.md#id1)

New in dellemc.openmanage 7.4.0

### [Synopsis](idrac_gather_facts_role.md#id2)

- Role to fetch the server facts about a different components available in the PowerEdge Servers.

### [Parameters](idrac_gather_facts_role.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **computer_system_id**  string | Computer system id |
| **hostname**  string / required | iDRAC IP Address. |
| **http_timeout**  integer | The socket level timeout in seconds.  **Default:** `30` |
| **https_port**  integer | iDRAC port.  **Default:** `443` |
| **manager_id**  string | Manager/BMC id |
| **password**  string / required | iDRAC user password. |
| **target**  list / elements=string | *target* component for which information needs to be gathered.  **Choices:**   - `"IDRAC"` - `"System"` ← (default) - `"BIOS"` - `"Controller"` - `"CPU"` - `"Enclosure"` - `"EnclosureEMM"` - `"Fan"` - `"Firmware"` - `"HostNIC"` - `"License"` - `"Memory"` - `"NIC"` - `"PCIeSSDBackPlane"` - `"PowerSupply"` - `"PresenceAndStatusSensor"` - `"Sensors_Battery"` - `"Sensors_Intrusion"` - `"Sensors_Voltage"` - `"VirtualDisk"` - `"PCIeDevice"` - `"PhysicalDisk"` - `"SystemMetrics"`   **Default:** `["System"]` |
| **username**  string / required | iDRAC username. |
| **validate_certs**  boolean | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version 5.0.0, *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

#### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
