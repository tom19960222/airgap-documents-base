---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_device_httpd module – Manage HTTPD related settings on a BIG-IP system"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_device_httpd_module.html
fetched_at: 2026-07-28T02:05:54+00:00
---
# f5networks.f5_modules.bigip_device_httpd module – Manage HTTPD related settings on a BIG-IP system

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/ui/repo/published/f5networks/f5_modules/) (version 1.27.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
> You need further requirements to be able to use this module,
> see [Requirements](bigip_device_httpd_module.md#ansible-collections-f5networks-f5-modules-bigip-device-httpd-module-requirements) for details.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_device_httpd`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_device_httpd_module.md#synopsis)
- [Requirements](bigip_device_httpd_module.md#requirements)
- [Parameters](bigip_device_httpd_module.md#parameters)
- [Notes](bigip_device_httpd_module.md#notes)
- [Examples](bigip_device_httpd_module.md#examples)
- [Return Values](bigip_device_httpd_module.md#return-values)

## [Synopsis](bigip_device_httpd_module.md#id1)

- Manages HTTPD related settings on the BIG-IP. These settings are useful when you want to set GUI timeouts and other TMUI related settings.

## [Requirements](bigip_device_httpd_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](bigip_device_httpd_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allow**  list / elements=string | If you have enabled HTTPD access, specifies the IP address or address range for other systems that can communicate with this system.  To specify all addresses, use the value `all`.  An IP address can be specified, such as 172.27.1.10.  IP ranges can be specified, such as 172.27.\*.\* or 172.27.0.0/255.255.0.0. |
| **auth_name**  string | Sets the BIG-IP authentication realm name. |
| **auth_pam_dashboard_timeout**  boolean | Sets whether or not the BIG-IP dashboard will timeout.  **Choices:**   - `false` - `true` |
| **auth_pam_idle_timeout**  integer | Sets the GUI timeout for automatic logout, in seconds. |
| **auth_pam_validate_ip**  boolean | Sets the authPamValidateIp setting.  **Choices:**   - `false` - `true` |
| **fast_cgi_timeout**  integer | Sets the timeout of FastCGI. |
| **hostname_lookup**  boolean | Sets whether or not to display the hostname, if possible.  **Choices:**   - `false` - `true` |
| **log_level**  string | Sets the minimum HTTPD log level.  **Choices:**   - `"alert"` - `"crit"` - `"debug"` - `"emerg"` - `"error"` - `"info"` - `"notice"` - `"warn"` |
| **max_clients**  integer | Sets the maximum number of clients that can connect to the GUI at once. |
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
| **redirect_http_to_https**  boolean | Whether or not to redirect HTTP requests to the GUI to HTTPS.  **Choices:**   - `false` - `true` |
| **ssl_cipher_suite**  any | Specifies the ciphers the system uses.  The values in the suite are separated by colons (:).  Can be specified in either a string or list form. The list form is the recommended way to provide the cipher suite. See examples for usage.  Use the value `default` to set the cipher suite to the system default. This value is equivalent to specifying a list of `ECDHE-RSA-AES128-GCM-SHA256, ECDHE-RSA-AES256-GCM-SHA384,ECDHE-RSA-AES128-SHA,ECDHE-RSA-AES256-SHA, ECDHE-RSA-AES128-SHA256,ECDHE-RSA-AES256-SHA384,ECDHE-ECDSA-AES128-GCM-SHA256, ECDHE-ECDSA-AES256-GCM-SHA384,ECDHE-ECDSA-AES128-SHA,ECDHE-ECDSA-AES256-SHA, ECDHE-ECDSA-AES128-SHA256,ECDHE-ECDSA-AES256-SHA384,AES128-GCM-SHA256, AES256-GCM-SHA384,AES128-SHA,AES256-SHA,AES128-SHA256,AES256-SHA256, ECDHE-RSA-DES-CBC3-SHA,ECDHE-ECDSA-DES-CBC3-SHA,DES-CBC3-SHA`. |
| **ssl_port**  integer | The HTTPS port on which the system should listen. |
| **ssl_protocols**  any | The list of SSL protocols to accept on the management console.  A space-separated list of tokens in the format accepted by the Apache mod_ssl SSLProtocol directive.  Can be specified in either a string or list form. The list form is the recommended way to provide the cipher suite. See examples for usage.  Use the value `default` to set the SSL protocols to the system default. This value is equivalent to specifying a list of `all,-SSLv2,-SSLv3`. |

## [Notes](bigip_device_httpd_module.md#id4)

> **Note:**
>
> - Requires the **requests** Python package on the host. This is as easy as running `pip install requests`.
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_device_httpd_module.md#id5)

```yaml+jinja
- name: Set the BIG-IP authentication realm name
  bigip_device_httpd:
    auth_name: BIG-IP
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Set the auth pam timeout to 3600 seconds
  bigip_device_httpd:
    auth_pam_idle_timeout: 1200
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Set the validate IP settings
  bigip_device_httpd:
    auth_pam_validate_ip: false
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Set SSL cipher suite by list
  bigip_device_httpd:
    ssl_cipher_suite:
      - ECDHE-RSA-AES128-GCM-SHA256
      - ECDHE-RSA-AES256-GCM-SHA384
      - ECDHE-RSA-AES128-SHA
      - AES256-SHA256
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Set SSL cipher suite by string
  bigip_device_httpd:
    ssl_cipher_suite: ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-SHA:AES256-SHA256
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Set SSL protocols by list
  bigip_device_httpd:
    ssl_protocols:
      - all
      - -SSLv2
      - -SSLv3
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Set SSL protocols by string
  bigip_device_httpd:
    ssl_protocols: all -SSLv2 -SSLv3
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_device_httpd_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **auth_name**  string | The new authentication realm name.  **Returned:** changed  **Sample:** `"foo"` |
| **auth_pam_dashboard_timeout**  boolean | Whether or not the BIG-IP dashboard will timeout.  **Returned:** changed  **Sample:** `false` |
| **auth_pam_idle_timeout**  string | The new number of seconds for GUI timeout.  **Returned:** changed  **Sample:** `"1200"` |
| **auth_pam_validate_ip**  boolean | The new authPamValidateIp setting.  **Returned:** changed  **Sample:** `true` |
| **fast_cgi_timeout**  integer | The new timeout of FastCGI.  **Returned:** changed  **Sample:** `500` |
| **hostname_lookup**  boolean | Whether or not to display the hostname, if possible.  **Returned:** changed  **Sample:** `true` |
| **log_level**  string | The new minimum HTTPD log level.  **Returned:** changed  **Sample:** `"crit"` |
| **max_clients**  integer | The new maximum number of clients that can connect to the GUI at once.  **Returned:** changed  **Sample:** `20` |
| **redirect_http_to_https**  boolean | Whether or not to redirect HTTP requests to the GUI to HTTPS.  **Returned:** changed  **Sample:** `true` |
| **ssl_cipher_suite**  string | The new ciphers the system uses.  **Returned:** changed  **Sample:** `"ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-SHA"` |
| **ssl_cipher_suite_list**  string | List of the new ciphers the system uses.  **Returned:** changed  **Sample:** `"['ECDHE-RSA-AES256-GCM-SHA384', 'ECDHE-RSA-AES128-SHA']"` |
| **ssl_port**  integer | The new HTTPS port to listen on.  **Returned:** changed  **Sample:** `10443` |
| **ssl_protocols**  string | The new list of SSL protocols to accept on the management console.  **Returned:** changed  **Sample:** `"all -SSLv2 -SSLv3"` |

### Authors

- Joe Reifel (@JoeReifel)
- Tim Rupp (@caphrim007)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
