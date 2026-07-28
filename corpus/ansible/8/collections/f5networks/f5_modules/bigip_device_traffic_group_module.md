---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_device_traffic_group module – Manages traffic groups on BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_device_traffic_group_module.html
fetched_at: 2026-07-28T02:05:59+00:00
---
# f5networks.f5_modules.bigip_device_traffic_group module – Manages traffic groups on BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_device_traffic_group`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_device_traffic_group_module.md#synopsis)
- [Parameters](bigip_device_traffic_group_module.md#parameters)
- [Notes](bigip_device_traffic_group_module.md#notes)
- [Examples](bigip_device_traffic_group_module.md#examples)
- [Return Values](bigip_device_traffic_group_module.md#return-values)

## [Synopsis](bigip_device_traffic_group_module.md#id1)

- Supports managing traffic groups and their attributes on a BIG-IP.

## [Parameters](bigip_device_traffic_group_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auto_failback**  boolean | Specifies whether the traffic group fails back to the initial device specified in `ha_order`.  **Choices:**   - `false` - `true` |
| **auto_failback_time**  integer | Specifies the number of seconds the system delays before failing back to the initial device specified in `ha_order`.  The correct value range is `0 - 300` inclusive. |
| **ha_group**  string | Specifies a configured `HA group` to be associated with the traffic group.  Once you create an HA group on a device and associate the HA group with a traffic group, you must create an HA group and associate it with that same traffic group on every device in the device group.  To disable an HA group failover method, specify an empty string value (`""`) to this parameter.  Disabling an HA group will revert the device back to using `Load Aware` method (the default), unless `ha_order` setting is also configured.  The `auto_failback` and `auto_failback_time` are not compatible with `ha_group`. |
| **ha_load_factor**  integer | The value of the load the traffic-group presents the system relative to other traffic groups.  This parameter only takes effect when `Load Aware` failover method is in use.  The correct value range is `1 - 1000` inclusive. |
| **ha_order**  list / elements=string | Specifies the order in which you would like to assign devices for failover.  If you configure this setting, you must configure the setting on every traffic group in the device group.  The values should be device names of the devices that belong to the failover group configured previously.  The order in which the devices are placed as arguments to this parameter determines their HA order on the device. Meaning that changing the order of the same elements will cause a change on the unit.  To disable an HA order failover method, specify an empty string value (`""`) to this parameter.  Disabling an HA order will revert the device back to using the Load Aware method (the default), unless the `ha_group` setting is also configured.  Device names will be prepended with a partition by the module, so you can provide either the full path format name `/Common/bigip1` or just the name string `bigip1`. |
| **mac_address**  string | Specifies the floating Media Access Control (MAC) address associated with the floating IP addresses defined for a traffic group.  Primarily, a MAC masquerade address minimizes ARP communications or dropped packets as a result of failover.  A MAC masquerade address ensures any traffic destined for a specific traffic group reaches an available device after failover, which happens because, along with the traffic group, the MAC masquerade address floats to the available device.  Without a MAC masquerade address, the sending host must learn the MAC address for a newly-active device, either by sending an ARP request or by relying on the gratuitous ARP from the newly-active device.  To unset the MAC address, specify an empty value (`""`) to this parameter. |
| **name**  string / required | The name of the traffic group. |
| **partition**  string | Device partition to manage resources on.  **Default:** `"Common"` |
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
| **state**  string | When `present`, ensures the traffic group exists.  When `absent`, ensures the traffic group is removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](bigip_device_traffic_group_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_device_traffic_group_module.md#id4)

```yaml+jinja
- name: Create a traffic group
  bigip_device_traffic_group:
    name: foo1
    state: present
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Create a traffic group with ha_group failover
  bigip_device_traffic_group:
    name: foo2
    state: present
    ha_group: foo_HA_grp
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Create a traffic group with ha_order failover
  bigip_device_traffic_group:
    name: foo3
    state: present
    ha_order:
      - /Common/bigip1.lab.local
      - /Common/bigip2.lab.local
    auto_failback: true
    auto_failback_time: 40
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Change traffic group ha_order to ha_group
  bigip_device_traffic_group:
    name: foo3
    state: present
    ha_group: foo_HA_grp
    ha_order: ""
    auto_failback: false
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Remove traffic group
  bigip_device_traffic_group:
    name: foo
    state: absent
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost
```

## [Return Values](bigip_device_traffic_group_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **auto_failback**  boolean | Specifies whether the traffic group fails back to the initial device specified in ha_order.  **Returned:** changed  **Sample:** `true` |
| **auto_failback_time**  integer | Specifies the number of seconds the system delays before failing back.  **Returned:** changed  **Sample:** `60` |
| **ha_group**  string | The configured HA group associated with traffic group.  **Returned:** changed  **Sample:** `"foo_HA_grp"` |
| **ha_load_factor**  integer | The value of the load the traffic-group presents the system relative to other traffic groups.  **Returned:** changed  **Sample:** `20` |
| **ha_order**  list / elements=string | Specifies the order in which the devices will failover.  **Returned:** changed  **Sample:** `["/Common/bigip1", "/Common/bigip2"]` |
| **mac_address**  string | The MAC masquerade address  **Returned:** changed  **Sample:** `"02:01:d7:93:35:08"` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
