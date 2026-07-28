---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_tunnel module – Manage tunnels on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_tunnel_module.html
fetched_at: 2026-07-28T02:07:29+00:00
---
# f5networks.f5_modules.bigip_tunnel module – Manage tunnels on a BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_tunnel`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_tunnel_module.md#synopsis)
- [Parameters](bigip_tunnel_module.md#parameters)
- [Notes](bigip_tunnel_module.md#notes)
- [Examples](bigip_tunnel_module.md#examples)
- [Return Values](bigip_tunnel_module.md#return-values)

## [Synopsis](bigip_tunnel_module.md#id1)

- Manages tunnels on a BIG-IP. Tunnels are usually based upon a tunnel profile which defines both default arguments and constraints for the tunnel.
- Due to this, this module exposes a number of settings that may or may not be related to the type of tunnel you are working with. It is important that you take this into consideration when declaring your tunnel config.
- If a specific tunnel does not support the parameter you are considering, the documentation of the parameter will usually make mention of this. Otherwise, when configuring that parameter on the device, the device will notify you.

## [Parameters](bigip_tunnel_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auto_last_hop**  string | Allows you to configure auto last hop on a per-tunnel basis.  When creating a new tunnel, if this parameter is supported by the tunnel profile but not specified, the default is `default`.  When `default`, means that the system uses the global auto-lasthop setting to send back the request.  When `enabled`, allows the system to send return traffic to the MAC address that transmitted the request, even if the routing table points to a different network or interface. As a result, the system can send return traffic to clients even when there is no matching route.  **Choices:**   - `"default"` - `"enabled"` - `"disabled"` |
| **description**  string | Description of the tunnel. |
| **key**  integer | When applied to a GRE tunnel, this value specifies an optional field in the GRE header, used to authenticate the source of the packet.  When applied to a VXLAN or Geneve tunnel, this value specifies the Virtual Network Identifier (VNI).  When applied to an NVGRE tunnel, this value specifies the Virtual Subnet Identifier (VSID).  When creating a new tunnel, if this parameter is supported by the tunnel profile but not specified, the default value is `0`. |
| **local_address**  string | Specifies the IP address of the local endpoint of the tunnel. |
| **mode**  string | Specifies how the tunnel carries traffic.  When creating a new tunnel, if this parameter is supported by the tunnel profile but not specified, the default is `bidirectional`.  When `bidirectional`, specifies that the tunnel carries both inbound and outbound traffic.  When `inbound`, specifies that the tunnel carries only incoming traffic.  When `outbound`, specifies that the tunnel carries only outgoing traffic.  **Choices:**   - `"bidirectional"` - `"inbound"` - `"outbound"` |
| **mtu**  integer | Specifies the maximum transmission unit (MTU) of the tunnel.  When creating a new tunnel, if this parameter is supported by the tunnel profile but not specified, the default value is `0`.  The valid range is from `0` to `65515`. |
| **name**  string / required | Specifies the name of the tunnel. |
| **partition**  string | Device partition to manage resources on.  **Default:** `"Common"` |
| **profile**  string | Specifies the profile to associate with the tunnel for handling traffic.  Depending on your selection, other settings become available or disappear.  This parameter may not be changed after it is set. |
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
| **remote_address**  string | Specifies the IP address of the remote endpoint of the tunnel.  For `dslite`, `fec` (when configuring the FEC tunnel for receiving traffic only), `v6rd` (configured as a border relay), or `map`, the tunnel must have an unspecified remote address (any). |
| **secondary_address**  string | Specifies a non-floating IP address for the tunnel, to be used with host-initiated traffic. |
| **state**  string | When `present`, ensures that the tunnel exists.  When `absent`, ensures the tunnel is removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tos**  string | Specifies the Type of Service (TOS) value to insert in the encapsulating header of transmitted packets.  When creating a new tunnel, if this parameter is supported by the tunnel profile but not specified, the default value is `preserve`.  When `preserve`, the system copies the TOS value from the inner header to the outer header.  You may also specify a numeric value. The possible values are from `0` to `255`. |
| **traffic_group**  string | Specifies the traffic group to associate with the tunnel.  This value cannot be changed after it is set. This is a limitation of BIG-IP. |
| **transparent**  boolean | Specifies that the tunnel operates in transparent mode.  When `true`, you can inspect and manipulate the encapsulated traffic flowing through the BIG-IP system.  A transparent tunnel terminates a tunnel while presenting the illusion that the tunnel transits the device unmodified (that is, the BIG-IP system appears as if it were an intermediate router that simply routes IP traffic through the device).  **Choices:**   - `false` - `true` |
| **use_pmtu**  boolean | Enables or disables the tunnel to use the PMTU (Path MTU) information provided by ICMP NeedFrag error messages.  If `true` and the tunnel `mtu` is set to `0`, the tunnel will use the PMTU information.  If `true` and the tunnel `mtu` is fixed to a non-zero value, the tunnel will use the minimum of PMTU and MTU.  If `false`, the tunnel will use fixed MTU or calculate its MTU using tunnel encapsulation configurations.  **Choices:**   - `false` - `true` |

## [Notes](bigip_tunnel_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_tunnel_module.md#id4)

```yaml+jinja
- name: Create a VXLAN tunnel
  bigip_tunnel:
    name: openshift-tunnel
    local_address: 192.1681.240
    key: 0
    secondary_address: 192.168.1.100
    mtu: 0
    use_pmtu: true
    tos: preserve
    auto_last_hop: default
    traffic_group: traffic-group-1
    state: present
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_tunnel_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **param1**  boolean | The new param1 value of the resource.  **Returned:** changed  **Sample:** `true` |
| **param2**  string | The new param2 value of the resource.  **Returned:** changed  **Sample:** `"Foo is bar"` |

### Authors

- Tim Rupp (@caphrim007)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
