---
collection: ansible
version: "8"
title: "cisco.ise.node_services_profiler_probe_config module – Resource module for Node Services Profiler Probe Config"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ise/node_services_profiler_probe_config_module.html
fetched_at: 2026-07-28T01:29:52+00:00
---
# cisco.ise.node_services_profiler_probe_config module – Resource module for Node Services Profiler Probe Config

> **Note:**
>
> This module is part of the [cisco.ise collection](https://galaxy.ansible.com/ui/repo/published/cisco/ise/) (version 2.6.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ise`.
> You need further requirements to be able to use this module,
> see [Requirements](node_services_profiler_probe_config_module.md#ansible-collections-cisco-ise-node-services-profiler-probe-config-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.node_services_profiler_probe_config`.

New in cisco.ise 2.1.0

- [Synopsis](node_services_profiler_probe_config_module.md#synopsis)
- [Requirements](node_services_profiler_probe_config_module.md#requirements)
- [Parameters](node_services_profiler_probe_config_module.md#parameters)
- [Notes](node_services_profiler_probe_config_module.md#notes)
- [See Also](node_services_profiler_probe_config_module.md#see-also)
- [Examples](node_services_profiler_probe_config_module.md#examples)
- [Return Values](node_services_profiler_probe_config_module.md#return-values)

## [Synopsis](node_services_profiler_probe_config_module.md#id1)

- Manage operation update of the resource Node Services Profiler Probe Config.
- This API updates the profiler probe configuration of a PSN.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](node_services_profiler_probe_config_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.1.1
- python >= 3.5

## [Parameters](node_services_profiler_probe_config_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **activeDirectory**  dictionary | The Active Directory probe queries the Active Directory for Windows information. |
| **daysBeforeRescan**  integer | Node Services Profiler Probe Config’s daysBeforeRescan. |
| **dhcp**  dictionary | The DHCP probe listens for DHCP packets from IP helpers. |
| **interfaces**  list / elements=dictionary | Node Services Profiler Probe Config’s interfaces. |
| **interface**  string | Node Services Profiler Probe Config’s interface. |
| **port**  integer | Node Services Profiler Probe Config’s port. |
| **dhcpSpan**  dictionary | The DHCP SPAN probe collects DHCP packets. |
| **interfaces**  list / elements=dictionary | Node Services Profiler Probe Config’s interfaces. |
| **interface**  string | Node Services Profiler Probe Config’s interface. |
| **dns**  dictionary | The DNS probe performs a DNS lookup for the FQDN. |
| **timeout**  integer | Node Services Profiler Probe Config’s timeout. |
| **hostname**  string | Hostname path parameter. Hostname of the node. |
| **http**  dictionary | The HTTP probe receives and parses HTTP packets. |
| **interfaces**  list / elements=dictionary | Node Services Profiler Probe Config’s interfaces. |
| **interface**  string | Node Services Profiler Probe Config’s interface. |
| **ise_debug**  boolean | Flag for Identity Services Engine SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **ise_hostname**  string / required | The Identity Services Engine hostname. |
| **ise_password**  string / required | The Identity Services Engine password to authenticate. |
| **ise_single_request_timeout**  integer  *added in cisco.ise 3.0.0* | Timeout (in seconds) for RESTful HTTP requests.  **Default:** `60` |
| **ise_username**  string / required | The Identity Services Engine username to authenticate. |
| **ise_uses_api_gateway**  boolean  *added in cisco.ise 1.1.0* | Flag that informs the SDK whether to use the Identity Services Engine’s API Gateway to send requests.  If it is true, it uses the ISE’s API Gateway and sends requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}.  If it is false, it sends the requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).  **Choices:**   - `false` - `true` ← (default) |
| **ise_uses_csrf_token**  boolean  *added in cisco.ise 3.0.0* | Flag that informs the SDK whether we send the CSRF token to ISE’s ERS APIs.  If it is True, the SDK assumes that your ISE CSRF Check is enabled.  If it is True, it assumes you need the SDK to manage the CSRF token automatically for you.  **Choices:**   - `false` ← (default) - `true` |
| **ise_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **ise_version**  string | Informs the SDK which version of Identity Services Engine to use.  **Default:** `"3.1_Patch_1"` |
| **ise_wait_on_rate_limit**  boolean | Flag for Identity Services Engine SDK to enable automatic rate-limit handling.  **Choices:**   - `false` - `true` ← (default) |
| **netflow**  dictionary | The NetFlow probe collects the NetFlow packets that are sent to it from routers. |
| **interfaces**  list / elements=dictionary | Node Services Profiler Probe Config’s interfaces. |
| **interface**  string | Node Services Profiler Probe Config’s interface. |
| **port**  integer | Node Services Profiler Probe Config’s port. |
| **nmap**  list / elements=dictionary | The NMAP probe scans endpoints for open ports and OS. |
| **pxgrid**  list / elements=dictionary | The pxGrid probe fetches attributes of MAC address or IP address as a subscriber from the pxGrid queue. |
| **radius**  list / elements=dictionary | The RADIUS probe collects RADIUS session attributes as well as CDP, LLDP, DHCP, HTTP, and MDM attributes from IOS Sensors. |
| **snmpQuery**  dictionary | The SNMP query probe collects details from network devices such as interface, CDP, LLDP, and ARP. |
| **eventTimeout**  integer | Node Services Profiler Probe Config’s eventTimeout. |
| **retries**  integer | Node Services Profiler Probe Config’s retries. |
| **timeout**  integer | Node Services Profiler Probe Config’s timeout. |
| **snmpTrap**  dictionary | The SNMP trap probe receives linkup, linkdown, and MAC notification traps from network devices. |
| **interfaces**  list / elements=dictionary | Node Services Profiler Probe Config’s interfaces. |
| **interface**  string | Node Services Profiler Probe Config’s interface. |
| **linkTrapQuery**  boolean | LinkTrapQuery flag.  **Choices:**   - `false` - `true` |
| **macTrapQuery**  boolean | MacTrapQuery flag.  **Choices:**   - `false` - `true` |
| **port**  integer | Node Services Profiler Probe Config’s port. |

## [Notes](node_services_profiler_probe_config_module.md#id4)

> **Note:**
>
> - SDK Method used are node_services.NodeServices.set_profiler_probe_config,
> - Paths used are put /api/v1/profile/{hostname},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [See Also](node_services_profiler_probe_config_module.md#id5)

> **See also:**
>
> [Cisco ISE documentation for Node Services](https://developer.cisco.com/docs/identity-services-engine/v1/#!deployment-openapi)
> :   Complete reference of the Node Services API.

## [Examples](node_services_profiler_probe_config_module.md#id6)

```yaml+jinja
- name: Update by name
  cisco.ise.node_services_profiler_probe_config:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    activeDirectory:
      daysBeforeRescan: 0
    dhcp:
      interfaces:
      - interface: string
      port: 0
    dhcpSpan:
      interfaces:
      - interface: string
    dns:
      timeout: 0
    hostname: string
    http:
      interfaces:
      - interface: string
    netflow:
      interfaces:
      - interface: string
      port: 0
    nmap:
    - {}
    pxgrid:
    - {}
    radius:
    - {}
    snmpQuery:
      eventTimeout: 0
      retries: 0
      timeout: 0
    snmpTrap:
      interfaces:
      - interface: string
      linkTrapQuery: true
      macTrapQuery: true
      port: 0
```

## [Return Values](node_services_profiler_probe_config_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"activeDirectory": {"daysBeforeRescan": 0}, "dhcp": {"interfaces": [{"interface": "string"}], "port": 0}, "dhcpSpan": {"interfaces": [{"interface": "string"}]}, "dns": {"timeout": 0}, "http": {"interfaces": [{"interface": "string"}]}, "netflow": {"interfaces": [{"interface": "string"}], "port": 0}, "nmap": [{}], "pxgrid": [{}], "radius": [{}], "snmpQuery": {"eventTimeout": 0, "retries": 0, "timeout": 0}, "snmpTrap": {"interfaces": [{"interface": "string"}], "linkTrapQuery": true, "macTrapQuery": true, "port": 0}}` |
| **ise_update_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"success": {"message": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
- [Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
