---
collection: ansible
version: "6"
title: "cisco.dnac.nfv_provision module – Resource module for Nfv Provision"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/nfv_provision_module.html
fetched_at: 2026-07-27T16:53:04+00:00
---
# cisco.dnac.nfv_provision module – Resource module for Nfv Provision

> **Note:**
>
> This module is part of the [cisco.dnac collection](https://galaxy.ansible.com/cisco/dnac) (version 6.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.dnac`.
> You need further requirements to be able to use this module,
> see [Requirements](nfv_provision_module.md#ansible-collections-cisco-dnac-nfv-provision-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.nfv_provision`.

New in cisco.dnac 3.1.0

- [Synopsis](nfv_provision_module.md#synopsis)
- [Requirements](nfv_provision_module.md#requirements)
- [Parameters](nfv_provision_module.md#parameters)
- [Notes](nfv_provision_module.md#notes)
- [See Also](nfv_provision_module.md#see-also)
- [Examples](nfv_provision_module.md#examples)
- [Return Values](nfv_provision_module.md#return-values)

## [Synopsis](nfv_provision_module.md#id1)

- Manage operation create of the resource Nfv Provision.
- Design and Provision single/multi NFV device with given site/area/building/floor .

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](nfv_provision_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](nfv_provision_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **headers**  dictionary | Additional headers. |
| **provisioning**  list / elements=dictionary | Nfv Provision’s provisioning. |
| **device**  list / elements=dictionary | Nfv Provision’s device. |
| **customNetworks**  list / elements=dictionary | Nfv Provision’s customNetworks. |
| **ipAddressPool**  string | IP address pool of sub pool (eg 175.175.140.1). |
| **name**  string | Name of custom network (eg cust-1). |
| **port**  string | Port for custom network (eg 443). |
| **deviceSerialNumber**  string | Serial number of device (eg FGL210710QY). |
| **ip**  string | IP address of the device (eg 172.20.126.90). |
| **serviceProviders**  list / elements=dictionary | Nfv Provision’s serviceProviders. |
| **serviceProvider**  string | Name of the service provider (eg Airtel). |
| **wanInterface**  dictionary | Nfv Provision’s wanInterface. |
| **bandwidth**  string | Bandwidth limit (eg 100). |
| **gateway**  string | Gateway (eg 175.175.190.1). |
| **interfaceName**  string | Name of the interface (eg GE0-0). |
| **ipAddress**  string | IP address (eg 175.175.190.205). |
| **subnetmask**  string | Subnet mask (eg 255.255.255.0). |
| **services**  list / elements=dictionary | Nfv Provision’s services. |
| **adminPasswordHash**  string | Admin password hash. |
| **centralManagerIP**  string | WAAS Package needs to be installed to populate Central Manager IP automatically. |
| **centralRegistrationKey**  string | Central registration key. |
| **commonKey**  string | Common key. |
| **disk**  string | Name of disk type (eg internal). |
| **mode**  string | Mode of firewall (eg transparent). |
| **systemIp**  string | System IP. |
| **type**  string | Type of service (eg ISR). |
| **subPools**  list / elements=dictionary | Nfv Provision’s subPools. |
| **gateway**  string | IP address for gate way (eg 175.175.140.1). |
| **ipSubnet**  string | IP pool cidir (eg 175.175.140.0). |
| **name**  string | Name of the ip sub pool (eg; Lan-65). |
| **parentPoolName**  string | Name of parent pool (global pool name). |
| **type**  string | Tyep of ip sub pool (eg Lan). |
| **tagName**  string | Name of device tag (eg dev1). |
| **templateParam**  dictionary | Nfv Provision’s templateParam. |
| **asav**  dictionary | Nfv Provision’s asav. |
| **var1**  string | Variable for asav template (eg “test” “Hello asav”). |
| **nfvis**  dictionary | Nfv Provision’s nfvis. |
| **var1**  string | Variable for nfvis template (eg “test” “Hello nfvis”). |
| **vlan**  list / elements=dictionary | Nfv Provision’s vlan. |
| **id**  string | Vlan id(e .4018). |
| **interfaces**  string | Interface (eg GigabitEathernet1/0). |
| **network**  string | Network name to connect (eg lan-net). |
| **type**  string | Vlan type(eg. Access or Trunk). |
| **site**  dictionary | Nfv Provision’s site. |
| **area**  dictionary | Nfv Provision’s area. |
| **name**  string | Name of the area (eg Area1). |
| **parentName**  string | Parent name of the area to be created. |
| **building**  dictionary | Nfv Provision’s building. |
| **address**  string | Address of the building to be created. |
| **latitude**  integer | Latitude coordinate of the building (eg 37.338). |
| **longitude**  integer | Longitude coordinate of the building (eg -121.832). |
| **name**  string | Name of the building (eg building1). |
| **parentName**  string | Address of the building to be created. |
| **floor**  dictionary | Nfv Provision’s floor. |
| **height**  integer | Height of the floor (eg 15). |
| **length**  integer | Length of the floor (eg 100). |
| **name**  string | Name of the floor (eg floor-1). |
| **parentName**  string | Parent name of the floor to be created. |
| **rfModel**  string | Type of floor (eg Cubes And Walled Offices). |
| **width**  integer | Width of the floor (eg 100). |
| **siteProfileName**  string | Name of site profile to be provision with device. |
| **siteProfile**  list / elements=dictionary | Nfv Provision’s siteProfile. |
| **device**  list / elements=dictionary | Nfv Provision’s device. |
| **customNetworks**  list / elements=dictionary | Nfv Provision’s customNetworks. |
| **connectionType**  string | Type of network connection from custom network (eg lan). |
| **name**  string | Name of custom network (eg cust-1). |
| **networkMode**  string | Network mode (eg Access or Trunk). |
| **servicesToConnect**  list / elements=dictionary | Nfv Provision’s servicesToConnect. |
| **service**  string | Name of service to be connected to the custom network (eg router-1). |
| **vlan**  string | Vlan id for the custom network(eg 4000). |
| **customServices**  list / elements=dictionary | Nfv Provision’s customServices. |
| **applicationType**  string | Application type of custom service (eg LINUX). |
| **imageName**  string | Image name of custom service (eg redhat7.tar.gz.tar.gz). |
| **name**  string | Name of custom service (eg LINUX-1). |
| **profile**  string | Profile type of service (eg rhel7-medium). |
| **topology**  dictionary | Nfv Provision’s topology. |
| **assignIp**  string | Assign ip to network (eg true). |
| **name**  string | Name of connection from custom service(eg wan-net). |
| **type**  string | Type of connection from custom service (eg wan, lan or internal). |
| **customTemplate**  list / elements=dictionary | Nfv Provision’s customTemplate. |
| **deviceType**  string | Type of the device(eg NFVIS). |
| **template**  string | Name of the template(eg NFVIS template). |
| **deviceType**  string | Name of the device used in creating nfv profile(eg ENCS5400). |
| **dia**  boolean | Direct internet access value should be boolean (eg false).  Choices:   - `false` - `true` |
| **serviceProviders**  list / elements=dictionary | Nfv Provision’s serviceProviders. |
| **connect**  boolean | Connection of service provider and device value should be boolean (eg true).  Choices:   - `false` - `true` |
| **defaultGateway**  boolean | Default gateway connect value as boolean (eg true).  Choices:   - `false` - `true` |
| **linkType**  string | Name of connection type(eg GigabitEthernet). |
| **serviceProvider**  string | Name of the service provider(eg Airtel). |
| **services**  list / elements=dictionary | Nfv Provision’s services. |
| **imageName**  string | Name of image (eg isrv-universalk9.16.06.02.tar.gz). |
| **mode**  string | Mode of firewall (eg routed, transparent). |
| **name**  string | Name of the service (eg isrv). |
| **profile**  string | Profile type of service (eg ISRv-mini). |
| **topology**  dictionary | Nfv Provision’s topology. |
| **assignIp**  string | Assign ip address to network (eg true). |
| **name**  string | Name of connection (eg wan-net). |
| **type**  string | Type of connection (eg wan, lan or internal). |
| **type**  string | Service type (eg ISRV). |
| **tagName**  string | Device Tag name(eg dev1). |
| **vlan**  list / elements=dictionary | Nfv Provision’s vlan. |
| **id**  string | Vlan id(eg.4018). |
| **type**  string | Vlan type(eg. Access or Trunk). |
| **siteProfileName**  string | Name of the profile to create site profile profile( eg profile-1). |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](nfv_provision_module.md#id4)

> **Note:**
>
> - SDK Method used are site_design.SiteDesign.provision_nfv,
> - Paths used are post /dna/intent/api/v1/business/nfv,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](nfv_provision_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Site Design ProvisionNFV](https://developer.cisco.com/docs/dna-center/#!provision-nfv)
> :   Complete reference of the ProvisionNFV API.

## [Examples](nfv_provision_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.nfv_provision:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: '{{my_headers | from_json}}'
    provisioning:
    - device:
      - customNetworks:
        - ipAddressPool: string
          name: string
          port: string
        deviceSerialNumber: string
        ip: string
        serviceProviders:
        - serviceProvider: string
          wanInterface:
            bandwidth: string
            gateway: string
            interfaceName: string
            ipAddress: string
            subnetmask: string
        services:
        - adminPasswordHash: string
          centralManagerIP: string
          centralRegistrationKey: string
          commonKey: string
          disk: string
          mode: string
          systemIp: string
          type: string
        subPools:
        - gateway: string
          ipSubnet: string
          name: string
          parentPoolName: string
          type: string
        tagName: string
        templateParam:
          asav:
            var1: string
          nfvis:
            var1: string
        vlan:
        - id: string
          interfaces: string
          network: string
          type: string
      site:
        area:
          name: string
          parentName: string
        building:
          address: string
          latitude: 0
          longitude: 0
          name: string
          parentName: string
        floor:
          height: 0
          length: 0
          name: string
          parentName: string
          rfModel: string
          width: 0
        siteProfileName: string
    siteProfile:
    - device:
      - customNetworks:
        - connectionType: string
          name: string
          networkMode: string
          servicesToConnect:
          - service: string
          vlan: string
        customServices:
        - applicationType: string
          imageName: string
          name: string
          profile: string
          topology:
            assignIp: string
            name: string
            type: string
        customTemplate:
        - deviceType: string
          template: string
        deviceType: string
        dia: true
        serviceProviders:
        - connect: true
          defaultGateway: true
          linkType: string
          serviceProvider: string
        services:
        - imageName: string
          mode: string
          name: string
          profile: string
          topology:
            assignIp: string
            name: string
            type: string
          type: string
        tagName: string
        vlan:
        - id: string
          type: string
      siteProfileName: string
```

## [Return Values](nfv_provision_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"executionId": "string", "executionStatusUrl": "string", "message": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
