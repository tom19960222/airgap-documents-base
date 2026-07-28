---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_iapp_template module – Manages TCL iApp templates on a BIG-IP."
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_iapp_template_module.html
fetched_at: 2026-07-27T17:26:59+00:00
---
# f5networks.f5_modules.bigip_iapp_template module – Manages TCL iApp templates on a BIG-IP.

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_iapp_template`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_iapp_template_module.md#synopsis)
- [Parameters](bigip_iapp_template_module.md#parameters)
- [Notes](bigip_iapp_template_module.md#notes)
- [Examples](bigip_iapp_template_module.md#examples)

## [Synopsis](bigip_iapp_template_module.md#id1)

- Manages TCL iApp templates on a BIG-IP. This module allows you to deploy iApp templates to the BIG-IP and manage their lifecycle. The conventional way to use this module is to import new iApps as needed, or by extracting the contents of the iApp archive that is provided at downloads.f5.com, and then importing all the iApps with this module. This module can also update existing iApps provided the source of the iApp changed while the name stayed the same. Note that this module will not reconfigure any services that may have been created using the `bigip_iapp_service` module. iApps are normally not updated in production. Instead, new versions are deployed and then existing services are changed to consume that new template. As such, the ability to update templates in-place requires using the `force` option.

## [Parameters](bigip_iapp_template_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **content**  string | Sets the contents of an iApp template directly to the specified value. This is for simple values, but can be used with lookup plugins for anything complex or with formatting. `content` must be provided when creating new templates. |
| **force**  boolean | Specifies whether or not to force the uploading of an iApp. When `yes`, the system will force update the iApp even if there are iApp services using it. This will not update the running service, use `bigip_iapp_service` to do that. When `no`, the system updates the iApp only if there are no iApp services using the template.  Choices:   - `false` - `true` |
| **name**  string | The name of the iApp template you want to delete. This option is only available when specifying a `state` of `absent` and is provided as a way to delete templates that you may no longer have the source of. |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
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
| **state**  string | Whether the iApp template should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](bigip_iapp_template_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_iapp_template_module.md#id4)

```yaml+jinja
- name: Add the iApp contained in template iapp.tmpl
  bigip_iapp_template:
    content: "{{ lookup('template', 'iapp.tmpl') }}"
    state: present
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Update a template in place
  bigip_iapp_template:
    content: "{{ lookup('template', 'iapp-new.tmpl') }}"
    state: present
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Update a template in place that has existing services created from it.
  bigip_iapp_template:
    content: "{{ lookup('template', 'iapp-new.tmpl') }}"
    force: yes
    state: present
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost
```

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
