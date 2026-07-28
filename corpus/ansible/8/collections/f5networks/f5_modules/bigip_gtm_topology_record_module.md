---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_gtm_topology_record module – Manages GTM Topology Records"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_gtm_topology_record_module.html
fetched_at: 2026-07-28T02:06:22+00:00
---
# f5networks.f5_modules.bigip_gtm_topology_record module – Manages GTM Topology Records

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/ui/repo/published/f5networks/f5_modules/) (version 1.27.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_gtm_topology_record`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_gtm_topology_record_module.md#synopsis)
- [Parameters](bigip_gtm_topology_record_module.md#parameters)
- [Notes](bigip_gtm_topology_record_module.md#notes)
- [Examples](bigip_gtm_topology_record_module.md#examples)
- [Return Values](bigip_gtm_topology_record_module.md#return-values)

## [Synopsis](bigip_gtm_topology_record_module.md#id1)

- Manages GTM (now BIG-IP DNS) Topology Records. Once created, only topology record `weight` can be modified.

## [Parameters](bigip_gtm_topology_record_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **destination**  dictionary / required | Specifies where the system directs the incoming DNS request. |
| **continent**  string | Specifies one of the seven continents, along with the `Unknown` setting.  Specifying `Unknown` forces the system to use a default resolution if the system cannot determine the location of the local DNS making the request.  Full continent names and their abbreviated versions are supported. |
| **country**  string | Specifies a country.  Full continent names and their abbreviated versions are supported. |
| **datacenter**  string | Specifies the name of GTM data center already defined in the configuration. |
| **geo_isp**  string | Specifies a geolocation ISP |
| **isp**  string | Specifies an Internet service provider.  **Choices:**   - `"AOL"` - `"BeijingCNC"` - `"CNC"` - `"ChinaEducationNetwork"` - `"ChinaMobilNetwork"` - `"ChinaRailwayTelcom"` - `"ChinaTelecom"` - `"ChinaUnicom"` - `"Comcast"` - `"Earthlink"` - `"ShanghaiCNC"` - `"ShanghaiTelecom"` |
| **negate**  boolean | When set to `true` the system selects this topology record, when the request destination does not match.  **Choices:**   - `false` ← (default) - `true` |
| **pool**  string | Specifies the name of GTM pool already defined in the configuration. |
| **region**  string | Specifies the name of region already defined in the configuration. |
| **state**  string | Specifies a state in a given country.  This parameter requires the `country` option. |
| **subnet**  string | An IP address and network mask in the CIDR format. |
| **partition**  string | Device partition to manage resources on.  Partition parameter is taken into account when used in conjunction with `pool`, `data_center`, and `region` parameters, otherwise it is ignored.  **Default:** `"Common"` |
| **provider**  dictionary  *added in f5networks.f5_modules 1.0.0* | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  **Choices:**   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP or the BIG-IQ.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host or the BIG-IQ host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  **Default:** `443` |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  **Choices:**   - `"rest"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP or the BIG-IQ. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  **Choices:**   - `false` - `true` ← (default) |
| **source**  dictionary / required | Specifies the origination of an incoming DNS request. |
| **continent**  string | Specifies one of the seven continents, along with the `Unknown` setting.  Specifying `Unknown` forces the system to use a default resolution if the system cannot determine the location of the local DNS making the request.  Full continent names and their abbreviated versions are supported. |
| **country**  string | Specifies a country.  In addition to the country full names, you may also specify their abbreviated form, such as `US` instead of `United States`.  Valid country codes can be found here <https://countrycode.org/>. |
| **geo_isp**  string | Specifies a geolocation ISP. |
| **isp**  string | Specifies an Internet service provider.  **Choices:**   - `"AOL"` - `"BeijingCNC"` - `"CNC"` - `"ChinaEducationNetwork"` - `"ChinaMobilNetwork"` - `"ChinaRailwayTelcom"` - `"ChinaTelecom"` - `"ChinaUnicom"` - `"Comcast"` - `"Earthlink"` - `"ShanghaiCNC"` - `"ShanghaiTelecom"` |
| **negate**  boolean | When set to c(true) the system selects this topology record, when the request source does not match.  **Choices:**   - `false` ← (default) - `true` |
| **region**  string | Specifies the name of region already defined in the configuration. |
| **state**  string | Specifies a state in a given country.  This parameter requires the `country` option. |
| **subnet**  string | An IP address and network mask in the CIDR format. |
| **state**  string | When `state` is `present`, ensures the record exists.  When `state` is `absent`, ensures the record is removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **weight**  integer | Specifies the weight of the topology record.  The system finds the weight of the first topology record that matches the server object (pool or pool member) and the local DNS. The system then assigns that weight as the topology score for that server object.  The system load balances to the server object with the highest topology score.  If the system finds no topology record that matches both the server object and the local DNS, then the system assigns that server object a zero score.  If the option is not specified when the record is created the system will set it at a default value of `1`  Valid range is (0 - 4294967295) |

## [Notes](bigip_gtm_topology_record_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_gtm_topology_record_module.md#id4)

```yaml+jinja
- name: Create an IP Subnet and an ISP based topology record
  bigip_gtm_topology_record:
    source:
      - subnet: 192.168.1.0/24
    destination:
      - isp: AOL
    weight: 10
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Create a region and a pool based topology record
  bigip_gtm_topology_record:
    source:
      - region: Foo
    destination:
      - pool: FooPool
    partition: FooBar
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Create a negative region and a negative data center based topology record
  bigip_gtm_topology_record:
    source:
      - region: Baz
      - negate: true
    destination:
      - datacenter: Baz-DC
      - negate: true
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_gtm_topology_record_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **weight**  integer | The weight of the topology record.  **Returned:** changed  **Sample:** `20` |

### Authors

- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
