---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_asm_policy_server_technology module – Manages Server Technology on an ASM policy"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_asm_policy_server_technology_module.html
fetched_at: 2026-07-28T02:05:40+00:00
---
# f5networks.f5_modules.bigip_asm_policy_server_technology module – Manages Server Technology on an ASM policy

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_asm_policy_server_technology`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_asm_policy_server_technology_module.md#synopsis)
- [Parameters](bigip_asm_policy_server_technology_module.md#parameters)
- [Notes](bigip_asm_policy_server_technology_module.md#notes)
- [Examples](bigip_asm_policy_server_technology_module.md#examples)
- [Return Values](bigip_asm_policy_server_technology_module.md#return-values)

## [Synopsis](bigip_asm_policy_server_technology_module.md#id1)

- Manages Server Technology on ASM policies.

## [Parameters](bigip_asm_policy_server_technology_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  string / required | Specifies the name of the server technology to apply on, or remove from, the ASM policy.  **Choices:**   - `"jQuery"` - `"Java Servlets/JSP"` - `"ASP"` - `"WebDAV"` - `"IIS"` - `"Front Page Server Extensions (FPSE)"` - `"ASP.NET"` - `"Microsoft Windows"` - `"Unix/Linux"` - `"Macromedia ColdFusion"` - `"WordPress"` - `"Apache Tomcat"` - `"Apache/NCSA HTTP Server"` - `"Outlook Web Access"` - `"PHP"` - `"Microsoft SQL Server"` - `"Oracle"` - `"MySQL"` - `"Lotus Domino"` - `"BEA Systems WebLogic Server"` - `"Macromedia JRun"` - `"Novell"` - `"Cisco"` - `"SSI (Server Side Includes)"` - `"Proxy Servers"` - `"CGI"` - `"Sybase/ASE"` - `"IBM DB2"` - `"PostgreSQL"` - `"XML"` - `"Apache Struts"` - `"Elasticsearch"` - `"JBoss"` - `"Citrix"` - `"Node.js"` - `"Django"` - `"MongoDB"` - `"Ruby"` - `"JavaServer Faces (JSF)"` - `"Joomla"` - `"Jetty"` |
| **partition**  string | This parameter is only used when identifying an ASM policy.  **Default:** `"Common"` |
| **policy_name**  string / required | Specifies the name of an existing ASM policy to add or remove a server technology to. |
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
| **state**  string | When `present`, ensures the resource exists.  When `absent`, ensures the resource is removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](bigip_asm_policy_server_technology_module.md#id3)

> **Note:**
>
> - This module is primarily used as a component of configuring an ASM policy in the Ansible Galaxy ASM Policy Role.
> - Requires BIG-IP >= 13.0.0
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_asm_policy_server_technology_module.md#id4)

```yaml+jinja
- name: Add Server Technology to ASM Policy
  bigip_asm_policy_server_technology:
    name: Joomla
    policy_name: FooPolicy
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
- name: Remove Server Technology from ASM Policy
  bigip_asm_policy_server_technology:
    name: Joomla
    policy_name: FooPolicy
    state: absent
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_asm_policy_server_technology_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **name**  string | The name of Server Technology added/removed on the ASM policy.  **Returned:** changed  **Sample:** `"Joomla"` |
| **policy_name**  string | The name of the ASM policy  **Returned:** changed  **Sample:** `"FooPolicy"` |

### Authors

- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
