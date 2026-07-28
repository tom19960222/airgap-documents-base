---
collection: ansible
version: "6"
title: "cisco.dnac.nfv_profile module – Resource module for Nfv Profile"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/nfv_profile_module.html
fetched_at: 2026-07-27T16:53:02+00:00
---
# cisco.dnac.nfv_profile module – Resource module for Nfv Profile

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
> see [Requirements](nfv_profile_module.md#ansible-collections-cisco-dnac-nfv-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.nfv_profile`.

New in cisco.dnac 3.1.0

- [Synopsis](nfv_profile_module.md#synopsis)
- [Requirements](nfv_profile_module.md#requirements)
- [Parameters](nfv_profile_module.md#parameters)
- [Notes](nfv_profile_module.md#notes)
- [See Also](nfv_profile_module.md#see-also)
- [Examples](nfv_profile_module.md#examples)
- [Return Values](nfv_profile_module.md#return-values)

## [Synopsis](nfv_profile_module.md#id1)

- Manage operations create, update and delete of the resource Nfv Profile.
- API to create network profile for different NFV topologies.
- API to delete nfv network profile.
- API to update a NFV Network profile.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](nfv_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](nfv_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **device**  list / elements=dictionary | Nfv Profile’s device. |
| **customNetworks**  list / elements=dictionary | Nfv Profile’s customNetworks. |
| **connectionType**  string | Type of network connection from custom network (eg lan). |
| **networkName**  string | Name of custom network (eg cust-1). |
| **servicesToConnect**  list / elements=dictionary | Nfv Profile’s servicesToConnect. |
| **serviceName**  string | Name of service to be connected to the custom network (eg router-1). |
| **vlanId**  integer | Vlan id for the custom network(eg 4000). |
| **vlanMode**  string | Network mode (eg Access or Trunk). |
| **customTemplate**  list / elements=dictionary | Nfv Profile’s customTemplate. |
| **deviceType**  string | Type of the device(eg Cisco 5400 Enterprise Network Compute System), ‘Cisco Integrated Services Virtual Router’, ‘Cisco Adaptive Security Virtual Appliance (ASAv)’, ‘NFVIS’, ‘ASAV’. |
| **template**  string | Name of the template(eg NFVIS template). |
| **templateType**  string | Name of the template type to which template is associated (eg Cloud DayN Templates). Allowed values are ‘Onboarding Template(s)’ and ‘Day-N-Template(s)’. |
| **deviceTag**  string | Device Tag name(eg dev1). |
| **deviceType**  string | Name of the device used in creating nfv profile. Allowed values are ‘Cisco 5400 Enterprise Network Compute System’, ‘Cisco 5100 Enterprise Network Compute System’. |
| **directInternetAccessForFirewall**  boolean | Direct internet access value should be boolean (eg false or true).  Choices:   - `false` - `true` |
| **serviceProviderProfile**  list / elements=dictionary | Nfv Profile’s serviceProviderProfile. |
| **connect**  boolean | Connection of service provider and device value should be boolean (eg true).  Choices:   - `false` - `true` |
| **connectDefaultGatewayOnWan**  boolean | Connect default gateway connect value as boolean (eg true).  Choices:   - `false` - `true` |
| **linkType**  string | Name of connection type(eg GigabitEthernet). |
| **serviceProvider**  string | Name of the service provider(eg Airtel). |
| **services**  list / elements=dictionary | Nfv Profile’s services. |
| **firewallMode**  string | Firewall mode details example (routed, transparent). |
| **imageName**  string | Service image name (eg isrv-universalk9.16.12.01a.tar.gz). |
| **profileType**  string | Profile type of service (eg ISRv-mini). |
| **serviceName**  string | Name of the service (eg Router-1). |
| **serviceType**  string | Service type (eg ISRV). |
| **vNicMapping**  list / elements=dictionary | Nfv Profile’s vNicMapping. |
| **assignIpAddressToNetwork**  string | Assign ip address to network (eg true or false). |
| **networkType**  string | Type of connection (eg wan, lan or internal). |
| **vlanForL2**  list / elements=dictionary | Nfv Profile’s vlanForL2. |
| **vlanDescription**  string | Vlan description(eg Access 4018). |
| **vlanId**  integer | Vlan id (eg 4018). |
| **vlanType**  string | Vlan type(eg Access or Trunk). |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **id**  string | Id path parameter. Id of the NFV profile to be updated. |
| **name**  string | Name query parameter. Name of the profile to be updated. |
| **profileName**  string | Name of the profile to create NFV profile. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](nfv_profile_module.md#id4)

> **Note:**
>
> - SDK Method used are site_design.SiteDesign.create_nfv_profile, site_design.SiteDesign.delete_nfv_profile, site_design.SiteDesign.update_nfv_profile,
> - Paths used are post /dna/intent/api/v1/nfv/network-profile, delete /dna/intent/api/v1/nfv/network-profile/{id}, put /dna/intent/api/v1/nfv/network-profile/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](nfv_profile_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Site Design CreateNFVProfile](https://developer.cisco.com/docs/dna-center/#!create-nfv-profile)
> :   Complete reference of the CreateNFVProfile API.
>
> [Cisco DNA Center documentation for Site Design DeleteNFVProfile](https://developer.cisco.com/docs/dna-center/#!delete-nfv-profile)
> :   Complete reference of the DeleteNFVProfile API.
>
> [Cisco DNA Center documentation for Site Design UpdateNFVProfile](https://developer.cisco.com/docs/dna-center/#!update-nfv-profile)
> :   Complete reference of the UpdateNFVProfile API.

## [Examples](nfv_profile_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.nfv_profile:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    device:
    - customNetworks:
      - connectionType: string
        networkName: string
        servicesToConnect:
        - serviceName: string
        vlanId: 0
        vlanMode: string
      customTemplate:
      - deviceType: string
        template: string
        templateType: string
      deviceTag: string
      deviceType: string
      directInternetAccessForFirewall: true
      serviceProviderProfile:
      - connect: true
        connectDefaultGatewayOnWan: true
        linkType: string
        serviceProvider: string
      services:
      - firewallMode: string
        imageName: string
        profileType: string
        serviceName: string
        serviceType: string
        vNicMapping:
        - assignIpAddressToNetwork: string
          networkType: string
      vlanForL2:
      - vlanDescription: string
        vlanId: 0
        vlanType: string
    profileName: string

- name: Update by id
  cisco.dnac.nfv_profile:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    device:
    - currentDeviceTag: string
      customNetworks:
      - connectionType: string
        networkName: string
        servicesToConnect:
        - serviceName: string
        vlanId: 0
        vlanMode: string
      customTemplate:
      - deviceType: string
        template: string
        templateType: string
      deviceTag: string
      directInternetAccessForFirewall: true
      services:
      - firewallMode: string
        imageName: string
        profileType: string
        serviceName: string
        serviceType: string
        vNicMapping:
        - assignIpAddressToNetwork: string
          networkType: string
      vlanForL2:
      - vlanDescription: string
        vlanId: 0
        vlanType: string
    id: string
    name: string

- name: Delete by id
  cisco.dnac.nfv_profile:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string
    name: string
```

## [Return Values](nfv_profile_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"executionId": "string", "executionStatusUrl": "string", "message": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
