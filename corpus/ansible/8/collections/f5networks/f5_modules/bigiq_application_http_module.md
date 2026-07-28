---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigiq_application_http module – Manages BIG-IQ HTTP applications"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigiq_application_http_module.html
fetched_at: 2026-07-28T02:07:38+00:00
---
# f5networks.f5_modules.bigiq_application_http module – Manages BIG-IQ HTTP applications

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigiq_application_http`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigiq_application_http_module.md#synopsis)
- [Parameters](bigiq_application_http_module.md#parameters)
- [Notes](bigiq_application_http_module.md#notes)
- [Examples](bigiq_application_http_module.md#examples)
- [Return Values](bigiq_application_http_module.md#return-values)

## [Synopsis](bigiq_application_http_module.md#id1)

- Manages BIG-IQ applications used for load balancing an HTTP application on port 80 on BIG-IP systems.

## [Parameters](bigiq_application_http_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **add_analytics**  boolean | Collects statistics of the BIG-IP to which the application is deployed.  This parameter is only relevant when specifying a `service_environment` which is a BIG-IP; not an SSG.  **Choices:**   - `false` ← (default) - `true` |
| **description**  string | Description of the application. |
| **inbound_virtual**  dictionary | Settings to configure the virtual which receives the inbound connection.  This virtual is used to host the HTTP endpoint of the application. |
| **address**  string / required | Specifies destination IP address information to which the virtual server sends traffic.  This parameter is required when creating a new application. |
| **netmask**  string / required | Specifies the netmask to associate with the given `destination`.  This parameter is required when creating a new application. |
| **port**  integer | The port on which the virtual listens for connections.  When creating a new application, if this parameter is not specified, the default value is `80`.  **Default:** `80` |
| **name**  string / required | Name of the new application. |
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
| **servers**  list / elements=dictionary | A list of servers on which the application is hosted.  If you are familiar with other BIG-IP settings, you might also refer to this list as the list of pool members.  When creating a new application, at least one server is required. |
| **address**  string / required | The IP address of the server. |
| **port**  integer | The port of the server.  When creating a new application and specifying a server, if this parameter is not provided, the default is `80`.  **Default:** `80` |
| **service_environment**  string | Specifies the name of service environment to which the application is deployed.  When creating a new application, this parameter is required.  The service environment type is automatically discovered by this module. Therefore, it is crucial that you maintain unique names for items in the different service environment types (at this time, SSGs and BIG-IPs). |
| **state**  string | The state of the resource on the system.  When `present`, guarantees the resource exists with the provided attributes.  When `absent`, removes the resource from the system.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **wait**  boolean | If the module should wait for the application to be created, deleted, or updated.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](bigiq_application_http_module.md#id3)

> **Note:**
>
> - This module does not support updating of your application (whether deployed or not). If you need to update the application, we recommend removing and recreating it.
> - This module will not work on BIG-IQ version 6.1.x or greater.
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigiq_application_http_module.md#id4)

```yaml+jinja
- name: BIG-IQ CM an HTTP application on port 80 on BIG-IP
  bigiq_application_http:
    name: my-app
    description: Redirect HTTP to HTTPS
    service_environment: my-ssg
    servers:
      - address: 1.2.3.4
        port: 8080
      - address: 5.6.7.8
        port: 8080
    inbound_virtual:
      name: foo
      address: 2.2.2.2
      netmask: 255.255.255.255
      port: 443
    provider:
      password: secret
      server: cm.mydomain.com
      user: admin
    state: present
  delegate_to: localhost
```

## [Return Values](bigiq_application_http_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  string | The new description of the application of the resource.  **Returned:** changed  **Sample:** `"My application"` |
| **inbound_virtual_destination**  string | The destination of the virtual that was created.  **Returned:** changed  **Sample:** `"6.7.8.9"` |
| **inbound_virtual_netmask**  string | The network mask of the provided inbound destination.  **Returned:** changed  **Sample:** `"255.255.255.0"` |
| **inbound_virtual_port**  integer | The port on which the inbound virtual address listens.  **Returned:** changed  **Sample:** `80` |
| **servers**  complex | List of servers, and their ports, that make up the application.  **Returned:** changed  **Sample:** `"hash/dictionary of values"` |
| **address**  string | The IP address of the server.  **Returned:** changed  **Sample:** `"2.3.4.5"` |
| **port**  integer | The port on which the server listens.  **Returned:** changed  **Sample:** `8080` |
| **service_environment**  string | The environment to which the service was deployed.  **Returned:** changed  **Sample:** `"my-ssg1"` |

### Authors

- Tim Rupp (@caphrim007)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
