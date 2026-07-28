---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_device_auth module – Manage system authentication on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_device_auth_module.html
fetched_at: 2026-07-28T02:05:47+00:00
---
# f5networks.f5_modules.bigip_device_auth module – Manage system authentication on a BIG-IP

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_device_auth`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_device_auth_module.md#synopsis)
- [Parameters](bigip_device_auth_module.md#parameters)
- [Notes](bigip_device_auth_module.md#notes)
- [Examples](bigip_device_auth_module.md#examples)
- [Return Values](bigip_device_auth_module.md#return-values)

## [Synopsis](bigip_device_auth_module.md#id1)

- Manage the system authentication configuration. This module can assist in configuring a number of different system authentication types. Note that this module can not be used to configure APM authentication types.

## [Parameters](bigip_device_auth_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **accounting**  string | Specifies how the system returns accounting information, such as which services users access and the amount of network resources they consume, to the TACACS+ server.  When `send-to-first-server`, specifies the system transmits accounting information back to the first available TACACS+ server in the list.  When `send-to-all-servers`, specifies the system transmits accounting information back to all TACACS+ servers in the list.  This parameter is supported by the `tacacs` type.  **Choices:**   - `"send-to-first-server"` - `"send-to-all-servers"` |
| **authentication**  string | Specifies the process the system employs when sending authentication requests.  When `use-first-server`, specifies the system sends authentication attempts only to the first server in the list.  When `use-all-servers`, specifies the system sends an authentication request to each server until authentication succeeds, or until the system has sent a request to all servers in the list.  This parameter is supported by the `tacacs` type.  **Choices:**   - `"use-first-server"` - `"use-all-servers"` |
| **protocol_name**  string | Specifies the protocol associated with the value specified in `service_name`, which is a subset of the associated service being used for client authorization or system accounting.  Note that the majority of TACACS+ implementations are of protocol type `ip`, so try that first.  **Choices:**   - `"lcp"` - `"ip"` - `"ipx"` - `"atalk"` - `"vines"` - `"lat"` - `"xremote"` - `"tn3270"` - `"telnet"` - `"rlogin"` - `"pad"` - `"vpdn"` - `"ftp"` - `"http"` - `"deccp"` - `"osicp"` - `"unknown"` |
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
| **secret**  string | Secret key used to encrypt and decrypt packets sent or received from the server.  **Do not** use the pound/hash sign in the secret for TACACS+ servers.  When configuring TACACS+ auth for the first time, this value is required. |
| **servers**  any | Specifies a list of the IPv4 addresses for servers using the Terminal Access Controller Access System (TACACS)+ protocol with which the system communicates to obtain authorization data.  For each address, an alternate TCP port number may be optionally specified by specifying the `port` key.  If no port number is specified, the default port `49163` is used.  This parameter is supported by the `tacacs` type. |
| **address**  string | The IP address of the server.  This field is required, unless you are specifying a simple list of servers. In that case, the simple list can specify server IPs. See the examples for more clarification. |
| **port**  string | The port of the server. |
| **service_name**  string | Specifies the name of the service the user is requesting to be authorized to use.  Identifying what the user is asking to be authorized for enables the TACACS+ serverc to behave differently for different types of authorization requests.  This setting is required when configuring this form of system authentication.  Note that the majority of TACACS+ implementations are of service type `ppp`, so try that first.  **Choices:**   - `"slip"` - `"ppp"` - `"arap"` - `"shell"` - `"tty-daemon"` - `"connection"` - `"system"` - `"firewall"` |
| **state**  string | The state of the authentication configuration on the system.  When `present`, guarantees the system is configured for the specified `type`.  When `absent`, sets the system auth source back to `local`.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **type**  string / required | The authentication type to manage with this module.  Take special note that the parameters supported by this module will vary depending on the `type` that you are configuring.  At this time, this module only supports a subset of the total available auth types.  **Choices:**   - `"tacacs"` - `"local"` |
| **update_secret**  string | `always` will allow updating secrets if the user chooses to do so.  `on_create` will only set the secret when a `use_auth_source` is `true` and TACACS+ is not currently the auth source.  **Choices:**   - `"always"` ← (default) - `"on_create"` |
| **use_for_auth**  boolean | Specifies whether or not this auth source is put in use on the system.  **Choices:**   - `false` - `true` |

## [Notes](bigip_device_auth_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_device_auth_module.md#id4)

```yaml+jinja
- name: Set the system auth to TACACS+, default server port
  bigip_device_auth:
    type: tacacs
    authentication: use-all-servers
    accounting: send-to-all-servers
    protocol_name: ip
    secret: secret
    servers:
      - 10.10.10.10
      - 10.10.10.11
    service_name: ppp
    state: present
    use_for_auth: true
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Set the system auth to TACACS+, override server port
  bigip_device_auth:
    type: tacacs
    authentication: use-all-servers
    protocol_name: ip
    secret: secret
    servers:
      - address: 10.10.10.10
        port: 1234
      - 10.10.10.11
    service_name: ppp
    use_for_auth: true
    state: present
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_device_auth_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **accounting**  string | Which servers to send information to when using TACACS.  **Returned:** changed  **Sample:** `"send-to-all-servers"` |
| **authentication**  string | Process the system uses to serve authentication requests when using TACACS.  **Returned:** changed  **Sample:** `"use-all-servers"` |
| **protocol_name**  string | Name of the protocol associated with `service_name` used for client authentication.  **Returned:** changed  **Sample:** `"ip"` |
| **servers**  list / elements=string | List of servers used in TACACS authentication.  **Returned:** changed  **Sample:** `["1.2.2.1", "4.5.5.4"]` |
| **service_name**  string | Name of the service the user is requesting to be authorized to use.  **Returned:** changed  **Sample:** `"ppp"` |

### Authors

- Tim Rupp (@caphrim007)
- Nitin Khanna (@nitinthewiz)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
