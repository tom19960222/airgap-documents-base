---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_qkview module – Manage QKviews on the device"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_qkview_module.html
fetched_at: 2026-07-28T02:07:09+00:00
---
# f5networks.f5_modules.bigip_qkview module – Manage QKviews on the device

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_qkview`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_qkview_module.md#synopsis)
- [Parameters](bigip_qkview_module.md#parameters)
- [Notes](bigip_qkview_module.md#notes)
- [Examples](bigip_qkview_module.md#examples)

## [Synopsis](bigip_qkview_module.md#id1)

- Manages creating and downloading QKviews from a BIG-IP. The qkview utility automatically collects configuration and diagnostic information from BIG-IP systems, and combines the data into a QKView file. F5 Support may request you send or upload this QKview to assist in troubleshooting.

## [Parameters](bigip_qkview_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **asm_request_log**  boolean | When `true`, includes ASM request log data. When `False`, excludes ASM request log data.  **Choices:**   - `false` ← (default) - `true` |
| **complete_information**  boolean | Include complete (all applicable) information in the QKview.  **Choices:**   - `false` ← (default) - `true` |
| **dest**  path | Destination on your local filesystem where you want to save the QKview. |
| **exclude**  list / elements=string | Exclude various file from the QKview.  **Choices:**   - `"all"` - `"audit"` - `"secure"` - `"bash_history"` |
| **exclude_core**  boolean | Exclude core files from the QKview.  **Choices:**   - `false` ← (default) - `true` |
| **filename**  string | Name of the QKview file to create on the remote BIG-IP.  **Default:** `"localhost.localdomain.qkview"` |
| **force**  boolean | If `no`, the file will only be transferred if the destination does not exist.  **Choices:**   - `false` - `true` ← (default) |
| **max_file_size**  integer | Maximum file size of the QKview file, in bytes. By default, no max file size is specified. |
| **only_create_file**  boolean  *added in f5networks.f5_modules 1.20.0* | If `true`, the file is created on the device and not downloaded. The file will not be deleted by the module from the device.  **Choices:**   - `false` ← (default) - `true` |
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

## [Notes](bigip_qkview_module.md#id3)

> **Note:**
>
> - This module does not include the “max time” or “restrict to blade” options.
> - If you are using this module with either Ansible Tower or Ansible AWX, you should be aware of how these Ansible products execute jobs in restricted environments. More information can be found here <https://clouddocs.f5.com/products/orchestration/ansible/devel/usage/module-usage-with-tower.html>
> - Some longer running tasks might cause the REST interface on BIG-IP to time out, to avoid this adjust the timers as per this KB article <https://support.f5.com/csp/article/K94602685>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_qkview_module.md#id4)

```yaml+jinja
- name: Fetch a qkview from the remote device
  bigip_qkview:
    asm_request_log: true
    exclude:
      - audit
      - secure
    dest: /tmp/localhost.localdomain.qkview
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

### Authors

- Tim Rupp (@caphrim007)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
