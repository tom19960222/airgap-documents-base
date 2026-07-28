---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_provision module – Manage BIG-IP module provisioning"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_provision_module.html
fetched_at: 2026-07-27T17:27:38+00:00
---
# f5networks.f5_modules.bigip_provision module – Manage BIG-IP module provisioning

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_provision`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_provision_module.md#synopsis)
- [Parameters](bigip_provision_module.md#parameters)
- [Notes](bigip_provision_module.md#notes)
- [Examples](bigip_provision_module.md#examples)
- [Return Values](bigip_provision_module.md#return-values)

## [Synopsis](bigip_provision_module.md#id1)

- Manage BIG-IP module provisioning. This module will only provision at the standard levels of Dedicated, Nominal, and Minimum.

## [Parameters](bigip_provision_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **level**  string | Sets the provisioning level for the requested modules. Changing the level for one module may require modifying the level of another module. For example, changing one module to `dedicated` requires setting all others to `none`. Setting the level of a module to `none` means the module is not activated.  Use a `state` of **absent** to set c(level) to none and de-provision the module.  This parameter is not relevant to `cgnat - pre tmos 15.0` or `mgmt` and will not be applied to the `cgnat - pre tmos 15.0` or `mgmt` module.  Choices:   - `"dedicated"` - `"nominal"` ← (default) - `"minimum"` |
| **memory**  string | Sets additional memory for the management module. This is in addition to minimum allocated RAM of 1264MB.  The accepted value range is `0 - 8192`. Maximum value is restricted by the available RAM in the system.  Specifying `large` reserves an additional 500MB for the mgmt module.  Specifying `medium` reserves an additional 200MB for the mgmt module.  Specifying `small` reserves no additional RAM for the mgmt module.  Use `large` for configurations containing more than 2000 objects, or more specifically, for any configuration that exceeds 1000 objects per 2 GB of installed memory. Changing the Management `mgmt` size after initial provisioning causes a reprovision operation. |
| **module**  aliases: name  string / required | The module to provision in BIG-IP.  Choices:   - `"am"` - `"afm"` - `"apm"` - `"asm"` - `"avr"` - `"cgnat"` - `"fps"` - `"gtm"` - `"ilx"` - `"lc"` - `"ltm"` - `"mgmt"` - `"pem"` - `"sam"` - `"sslo"` - `"swg"` - `"urldb"` - `"vcmp"` |
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
| **state**  string | The state of the provisioned module on the system. When `present`, guarantees the specified module is provisioned at the requested level, provided there are sufficient resources on the device (such as physical RAM) to support the module.  When `absent`, de-provision the module.  `absent`, is not a relevent option for the `mgmt` module, as it can not be de-provisioned.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](bigip_provision_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_provision_module.md#id4)

```yaml+jinja
- name: Provision PEM at "nominal" level
  bigip_provision:
    module: pem
    level: nominal
    provider:
      server: lb.mydomain.com
      password: secret
      user: admin
  delegate_to: localhost

- name: Provision a dedicated SWG. This will unprovision every other module
  bigip_provision:
    module: swg
    level: dedicated
    provider:
      server: lb.mydomain.com
      password: secret
      user: admin
  delegate_to: localhost

- name: Provision mgmt with medium amount of memory.
  bigip_provision:
    module: mgmt
    memory: medium
    provider:
      server: lb.mydomain.com
      password: secret
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_provision_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **level**  string | The new provisioning level of the module.  Returned: changed  Sample: `"minimum"` |
| **memory**  string | The new provisioned amount of memory for mgmt module.  Returned: changed  Sample: `"large"` |

### Authors

- Tim Rupp (@caphrim007)
- Greg Crosby (@crosbygw)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
