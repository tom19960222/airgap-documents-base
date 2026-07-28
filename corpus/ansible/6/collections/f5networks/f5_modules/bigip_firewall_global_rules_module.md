---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_firewall_global_rules module – Manage AFM global rule settings on BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_firewall_global_rules_module.html
fetched_at: 2026-07-27T17:26:41+00:00
---
# f5networks.f5_modules.bigip_firewall_global_rules module – Manage AFM global rule settings on BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_firewall_global_rules`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_firewall_global_rules_module.md#synopsis)
- [Parameters](bigip_firewall_global_rules_module.md#parameters)
- [Notes](bigip_firewall_global_rules_module.md#notes)
- [Examples](bigip_firewall_global_rules_module.md#examples)
- [Return Values](bigip_firewall_global_rules_module.md#return-values)

## [Synopsis](bigip_firewall_global_rules_module.md#id1)

- Configures the global network firewall rules on AFM (Advanced Firewall Manager). These firewall rules are applied to all packets except those going through the management interface. They are applied first, before any firewall rules for the packet’s virtual server, route domain, and/or self IP address.

## [Parameters](bigip_firewall_global_rules_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | Description for the global list of firewall rules. |
| **enforced_policy**  string | Specifies an enforced firewall policy.  `enforced_policy` rules are enforced globally. |
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
| **service_policy**  string | Specifies a service policy that would apply to traffic globally.  The service policy is applied to all flows, provided there are no other context specific service policy configurations that override the global service policy. For example, when a service policy is configured both at a global level and on a firewall rule, and a flow matches the rule, the more specific service policy configuration in the rule will override the service policy setting at the global level.  The service policy associated here can be created using the `bigip_service_policy` module. |
| **staged_policy**  string | Specifies a staged firewall policy.  `staged_policy` rules are not enforced while all the visibility aspects (statistics, reporting, and logging) function as if the staged-policy rules were enforced globally. |

## [Notes](bigip_firewall_global_rules_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_firewall_global_rules_module.md#id4)

```yaml+jinja
- name: Change enforced policy in AFM global rules
  bigip_firewall_global_rules:
    enforced_policy: enforcing1
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_firewall_global_rules_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  string | The new description.  Returned: changed  Sample: `"My description"` |
| **enforced_policy**  string | The new global Enforced Policy.  Returned: changed  Sample: `"/Common/enforced1"` |
| **service_policy**  string | The new global Service Policy.  Returned: changed  Sample: `"/Common/service1"` |
| **staged_policy**  string | The new global Staged Policy.  Returned: changed  Sample: `"/Common/staged1"` |

### Authors

- Tim Rupp (@caphrim007)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
