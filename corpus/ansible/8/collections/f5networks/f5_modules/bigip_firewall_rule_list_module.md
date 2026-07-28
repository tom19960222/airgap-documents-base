---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_firewall_rule_list module – Manage AFM security firewall policies on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_firewall_rule_list_module.html
fetched_at: 2026-07-28T02:06:11+00:00
---
# f5networks.f5_modules.bigip_firewall_rule_list module – Manage AFM security firewall policies on a BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_firewall_rule_list`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_firewall_rule_list_module.md#synopsis)
- [Parameters](bigip_firewall_rule_list_module.md#parameters)
- [Notes](bigip_firewall_rule_list_module.md#notes)
- [Examples](bigip_firewall_rule_list_module.md#examples)
- [Return Values](bigip_firewall_rule_list_module.md#return-values)

## [Synopsis](bigip_firewall_rule_list_module.md#id1)

- Manages AFM (Advanced Firewall Manager) security firewall policies on a BIG-IP.

## [Parameters](bigip_firewall_rule_list_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | The description to attach to the policy.  This parameter is only supported on versions of BIG-IP >= 12.1.0. On earlier versions it is ignored. |
| **name**  string / required | The name of the policy to create. |
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
| **rules**  list / elements=string | Specifies a list of rules you want associated with this policy. The order of this list is the order they will be evaluated by BIG-IP. If the specified rules do not exist (for example when creating a new policy) then they will be created.  Rules specified here, if they do not exist, will be created with “default deny” behavior. It is expected that you follow-up this module with the actual configuration for these rules.  The `bigip_firewall_rule` module can also be used to create, as well as edit, existing and new rules. |
| **state**  string | When `state` is `present`, ensures the rule list exists.  When `state` is `absent`, ensures the rule list is removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](bigip_firewall_rule_list_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_firewall_rule_list_module.md#id4)

```yaml+jinja
- name: Create a basic policy with some rule stubs
  bigip_firewall_rule_list:
    name: foo
    rules:
      - rule1
      - rule2
      - rule3
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_firewall_rule_list_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  string | The new description of the policy.  **Returned:** changed  **Sample:** `"My firewall policy"` |
| **rules**  list / elements=string | The list of rules on the device, in the order that they are evaluated.  **Returned:** changed  **Sample:** `["rule1", "rule2", "rule3"]` |

### Authors

- Tim Rupp (@caphrim007)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
