---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_traffic_selector module – Manage IPSec Traffic Selectors on BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_traffic_selector_module.html
fetched_at: 2026-07-28T02:07:28+00:00
---
# f5networks.f5_modules.bigip_traffic_selector module – Manage IPSec Traffic Selectors on BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_traffic_selector`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_traffic_selector_module.md#synopsis)
- [Parameters](bigip_traffic_selector_module.md#parameters)
- [Notes](bigip_traffic_selector_module.md#notes)
- [Examples](bigip_traffic_selector_module.md#examples)
- [Return Values](bigip_traffic_selector_module.md#return-values)

## [Synopsis](bigip_traffic_selector_module.md#id1)

- Manage IPSec Traffic Selectors on BIG-IP.

## [Parameters](bigip_traffic_selector_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | Description of the traffic selector. |
| **destination_address**  string | Specifies the host or network IP address to which the application traffic is destined.  When creating a new traffic selector, this parameter is required. |
| **ipsec_policy**  string | Specifies the IPsec policy that tells the BIG-IP system how to handle the packets.  When creating a new traffic selector, if this parameter is not specified, the default is `default-ipsec-policy`. |
| **name**  string / required | Specifies the name of the traffic selector. |
| **order**  integer | Specifies the order in which traffic is matched, if traffic can be matched to multiple traffic selectors.  Traffic is matched to the traffic selector with the highest priority (lowest order number).  When creating a new traffic selector, if this parameter is not specified, the default is `last`. |
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
| **source_address**  string | Specifies the host or network IP address from which the application traffic originates.  When creating a new traffic selector, this parameter is required. |
| **state**  string | When `present`, ensures the resource exists.  When `absent`, ensures the resource is removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](bigip_traffic_selector_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_traffic_selector_module.md#id4)

```yaml+jinja
- name: Create a traffic selector
  bigip_traffic_selector:
    name: selector1
    destination_address: 1.1.1.1
    ipsec_policy: policy1
    order: 1
    source_address: 2.2.2.2
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_traffic_selector_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **destination_address**  string | The new Destination IP Address.  **Returned:** changed  **Sample:** `"1.2.3.4/32"` |
| **ipsec_policy**  string | The new IPSec policy.  **Returned:** changed  **Sample:** `"/Common/policy1"` |
| **order**  integer | The new sort order.  **Returned:** changed  **Sample:** `1` |
| **source_address**  string | The new Source IP address.  **Returned:** changed  **Sample:** `"2.3.4.5/32"` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
