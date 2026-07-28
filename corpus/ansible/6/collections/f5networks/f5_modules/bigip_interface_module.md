---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_interface module – Module to manage BIG-IP physical interfaces."
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_interface_module.html
fetched_at: 2026-07-27T17:27:01+00:00
---
# f5networks.f5_modules.bigip_interface module – Module to manage BIG-IP physical interfaces.

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/f5networks/f5_modules) (version 1.21.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_interface`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_interface_module.md#synopsis)
- [Parameters](bigip_interface_module.md#parameters)
- [Notes](bigip_interface_module.md#notes)
- [Examples](bigip_interface_module.md#examples)
- [Return Values](bigip_interface_module.md#return-values)

## [Synopsis](bigip_interface_module.md#id1)

- Module to manage BIG-IP physical interfaces.

## [Parameters](bigip_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bundle**  string | Enables or disables bundle capability.  This option is only supported on select hardware platforms and interfaces.  Attempting to enable this option on a `VE` or any other unsupported platform/interface will result in module run failure.  Choices:   - `"enabled"` - `"disabled"` - `"not-supported"` |
| **bundle_speed**  string | Sets the bundle speed, which is applicable only when the bundle is `yes`.  This option is only supported on selected hardware platforms and interfaces.  Attempting to enable this option on a `VE` or any other unsupported platform/interface will result in module run failure.  Choices:   - `"100G"` - `"40G"` - `"not-supported"` |
| **description**  string | User defined description. |
| **enabled**  boolean | Specifies the current status of the interface.  When `yes`, enables the interface to pass traffic.  When `no`, disables the interface from passing traffic.  Choices:   - `false` - `true` |
| **flow_control**  string | Specifies how the system controls the sending of PAUSE frames.  When `tx-rx`, the interface honors pause frames from its partner, and also generates pause frames when necessary.  When `tx`, the interface ignores pause frames from its partner, and generates pause frames when necessary.  When `rx`, the interface honors pause frames from its partner, but does not generate pause frames.  When (none), the flow control is disabled on the interface.  Choices:   - `"none"` - `"rx"` - `"tx"` - `"tx-rx"` |
| **force_gigabit_fiber**  boolean | Enables or disables forcing of gigabit fiber media.  When `yes` for a gigabit fiber interface, the media setting will be forced, and no auto-negotiation will be performed.  When `no` auto-negotiation will be performed with just a single gigabit fiber option advertised.  Choices:   - `false` - `true` |
| **forward_error_correction**  string | Enables or disables IEEE 802.3bm Clause 91 Reed-Solomon Forward Error Correction on 100G interfaces. Not valid for LR4 media.  This option is only supported on selected hardware platforms and interfaces.  Attempting to enable this option on a `VE` or any other unsupported platform/interface will result in module run failure.  Choices:   - `"enabled"` - `"disabled"` - `"not-supported"` - `"auto"` |
| **lldp_admin**  string | Specifies LLDP settings on an interface level.  When `disabled`, the interface neither transmits (sends) LLDP messages to nor receives LLDP messages from neighboring devices.  When `txonly`, the interface transmits LLDP messages to neighbor devices, but does not receive LLDP messages from neighbor devices.  When `rxonly`, the interface receives LLDP messages from neighbor devices, but does not transmit LLDP messages to neighbor devices.  When `txrx`, the interface transmits LLDP messages to and receives LLDP messages from neighboring devices.  Choices:   - `"disable"` - `"rxonly"` - `"txonly"` - `"txrx"` |
| **lldp_tlvmap**  integer | Specifies the content of an LLDP message being sent or received.  Each LLDP attribute specified with this setting is optional and is in the form of Type, Length, Value (TLV).  The three mandatory TLVs not taken into account when calculating this value are: `Chassis ID`, `Port ID`, and `TTL`.  The optional attributes that are available have a specific TLV numeric value mapped to them.  The `Port Description` attribute has a TLV value of `8`.  The `System Name` attribute has a TLV value of `16`.  The `System Description` attribute has a TLV value of `32`.  The `System Capabilities` attribute has a TLV value of `64`.  The `Management Address` attribute has a TLV value of `128`.  The `Port VLAN ID` attribute has a TLV value of `256`.  The `VLAN Name` attribute has a TLV value of `512`.  The `Port and Protocol VLAN ID` attribute has a TLV value of `1024`.  The `Protocol Identity` attribute has a TLV value of `2048`.  The `MAC/PHY Config Status` attribute has a TLV value of `4096`.  The `Link Aggregation` attribute has a TLV value of `8192`.  The `Max Frame Size` attribute has a TLV value of `32768`.  The `Product Model` attribute has a TLV value of `65536`.  The `lldp_tlvmap` is a numeric value that is a sum of all TLV values of selected attributes.  Setting `lldp_tlvmap` to `0` will remove all attributes from the interface.  Setting `lldp_tlvmap` to `114680` will add all attributes to the interface. |
| **media_fixed**  string | Specifies the settings for a fixed (non-pluggable) interface.  Use this option only with a combo port to specify the media type for the fixed interface, when it is not the preferred port.  Choices:   - `"100000-FD"` - `"100000LR4-FD"` - `"10000LR-FD"` - `"10000T-FD"` - `"1000SX-FD"` - `"100TX-FD"` - `"10T-HD"` - `"20000-FD"` - `"40000LR4-FD"` - `"100000AR4-FD"` - `"100000SR4-FD"` - `"10000SFPCU-FD"` - `"1000CX-FD"` - `"1000T-FD"` - `"100TX-HD"` - `"12000-FD"` - `"21000-FD"` - `"40000SR4-FD"` - `"100000CR4-FD"` - `"10000ER-FD"` - `"10000SR-FD"` - `"1000LX-FD"` - `"1000T-HD"` - `"10T-FD"` - `"16000-FD"` - `"40000-FD"` - `"42000-FD"` - `"auto"` - `"no-phy"` |
| **media_sfp**  string | Specifies the settings for an SFP (pluggable) interface.  Use this option only with a combo port to specify the media type for the SFP interface, when it is not the preferred port.  Choices:   - `"100000-FD"` - `"100000LR4-FD"` - `"10000LR-FD"` - `"10000T-FD"` - `"1000SX-FD"` - `"100TX-FD"` - `"10T-HD"` - `"20000-FD"` - `"40000LR4-FD"` - `"100000AR4-FD"` - `"100000SR4-FD"` - `"10000SFPCU-FD"` - `"1000CX-FD"` - `"1000T-FD"` - `"100TX-HD"` - `"12000-FD"` - `"21000-FD"` - `"40000SR4-FD"` - `"100000CR4-FD"` - `"10000ER-FD"` - `"10000SR-FD"` - `"1000LX-FD"` - `"1000T-HD"` - `"10T-FD"` - `"16000-FD"` - `"40000-FD"` - `"42000-FD"` - `"auto"` - `"no-phy"` |
| **name**  string / required | Specifies the name of the interface to manage. |
| **port_fwd_mode**  string | Specifies the operation mode.  Choices:   - `"l3"` - `"passive"` - `"virtual-wire"` |
| **prefer_port**  string | Indicates which side of a combo port the interface uses, if both sides have the potential for an external link.  The default value for a combo port is sfp. Do not use this option for non-combo ports.  Choices:   - `"sfp"` - `"fixed"` |
| **provider**  dictionary  added in f5networks.f5_modules 1.0.0 | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  Choices:   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  Default: `443` |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"rest"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP with. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  Choices:   - `false` - `true` ← (default) |
| **sflow**  dictionary | Specifies sFlow settings for the interface. |
| **poll_interval**  integer | Specifies the maximum interval between two pollings, in seconds.  For this setting to take effect, `poll_interval_global` must be set to `no`.  The valid range is 0 - 4294967295. |
| **poll_interval_global**  boolean | Specifies whether the global interface `poll_interval` setting overrides the object-level `poll_interval` setting.  When `yes` the `poll_interval` setting does not take effect.  Choices:   - `false` - `true` |
| **stp**  boolean | Enables or disables STP.  Choices:   - `false` - `true` |
| **stp_auto_edge_port**  boolean | Sets STP automatic edge port detection for the interface.  When `yes`, the system monitors the interface for incoming STP, RSTP, or MSTP packets. If no such packets are received for a sufficient period of time (about three seconds), the interface is automatically given edge port status.  When `no`, the system never gives the interface edge port status automatically. Any STP setting set on a per-interface basis applies to all spanning tree instances.  Choices:   - `false` - `true` |
| **stp_edge_port**  boolean | Specifies whether the interface connects to an end station instead of another spanning tree bridge.  Choices:   - `false` - `true` |
| **stp_link_type**  string | Specifies the STP link type for the interface.  Choices:   - `"auto"` - `"p2p"` - `"shared"` |

## [Notes](bigip_interface_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_interface_module.md#id4)

```yaml+jinja
- name: Update Interface Settings
  bigip_interface:
    name: 1.1
    stp: yes
    stp_auto_edge_port: no
    stp_edge_port: yes
    stp_link_type: shared
    description: my description
    flow_control: tx
    lldp_admin: txrx
    lldp_tlvmap: 8
    force_gigabit_fiber: no
    sflow:
      - poll_interval: 10
      - poll_interval_global: no
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Disable Interface
  bigip_interface:
    name: 1.1
    enabled: no
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Change sflow interface settings
  bigip_interface:
    name: 1.1
    sflow:
      - poll_interval: 0
      - poll_interval_global: yes
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_interface_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **bundle**  string | Enables or disables bundle capability.  Returned: changed  Sample: `"not-supported"` |
| **bundle_speed**  string | The bundle speed.  Returned: changed  Sample: `"100G"` |
| **description**  string | User defined description.  Returned: changed  Sample: `"my description"` |
| **enabled**  boolean | The current status of the interface.  Returned: changed  Sample: `true` |
| **flow_control**  string | Specifies how the system controls the sending of PAUSE frames.  Returned: changed  Sample: `"tx"` |
| **force_gigabit_fiber**  boolean | Enables or disables forcing of gigabit fiber media.  Returned: changed  Sample: `true` |
| **forward_error_correction**  string | Enables or disables Forward Error Correction.  Returned: changed  Sample: `"auto"` |
| **lldp_admin**  string | The LLDP settings on an interface level.  Returned: changed  Sample: `"txrx"` |
| **lldp_tlvmap**  integer | The content of an LLDP message being sent or received.  Returned: changed  Sample: `136` |
| **media_fixed**  string | The settings for a fixed interface.  Returned: changed  Sample: `"100000-FD"` |
| **media_sfp**  string | The settings for a SFP interface.  Returned: changed  Sample: `"100000-FD"` |
| **port_fwd_mode**  string | The operation mode.  Returned: changed  Sample: `"passive"` |
| **prefer_port**  string | The side of a combo port the interface uses.  Returned: changed  Sample: `"fixed"` |
| **sflow**  complex | Specifies sFlow settings for the interface.  Returned: changed  Sample: `"hash/dictionary of values"` |
| **poll_interval**  integer | The maximum interval in seconds between two pollings.  Returned: changed  Sample: `128` |
| **poll_interval_global**  boolean | The global sFlow settings override.  Returned: changed  Sample: `true` |
| **stp**  boolean | Enables or disables STP.  Returned: changed  Sample: `false` |
| **stp_auto_edge_port**  boolean | Sets STP automatic edge port detection for the interface.  Returned: changed  Sample: `true` |
| **stp_edge_port**  boolean | Specifies whether the interface connects to an end station instead of another spanning tree bridge.  Returned: changed  Sample: `false` |
| **stp_link_type**  string | The STP link type for the interface.  Returned: changed  Sample: `"shared"` |

### Authors

- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
