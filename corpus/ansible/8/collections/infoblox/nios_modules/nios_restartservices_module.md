---
collection: ansible
version: "8"
title: "infoblox.nios_modules.nios_restartservices module – Restart grid services."
source_url: https://docs.ansible.com/projects/ansible/8/collections/infoblox/nios_modules/nios_restartservices_module.html
fetched_at: 2026-07-28T02:36:06+00:00
---
# infoblox.nios_modules.nios_restartservices module – Restart grid services.

> **Note:**
>
> This module is part of the [infoblox.nios_modules collection](https://galaxy.ansible.com/ui/repo/published/infoblox/nios_modules/) (version 1.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install infoblox.nios_modules`.
> You need further requirements to be able to use this module,
> see [Requirements](nios_restartservices_module.md#ansible-collections-infoblox-nios-modules-nios-restartservices-module-requirements) for details.
>
> To use it in a playbook, specify: `infoblox.nios_modules.nios_restartservices`.

New in infoblox.nios_modules 1.1.0

- [Synopsis](nios_restartservices_module.md#synopsis)
- [Requirements](nios_restartservices_module.md#requirements)
- [Parameters](nios_restartservices_module.md#parameters)
- [Notes](nios_restartservices_module.md#notes)
- [Examples](nios_restartservices_module.md#examples)

## [Synopsis](nios_restartservices_module.md#id1)

- Restart grid services.
- When invoked without any options, will restart ALL services on the default restart group IF NEEDED.

## [Requirements](nios_restartservices_module.md#id2)

The below requirements are needed on the host that executes this module.

- infoblox-client

## [Parameters](nios_restartservices_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **groups**  list / elements=string | The list of the Service Restart Groups to restart. |
| **members**  list / elements=string | The list of the Grid Members to restart. |
| **mode**  string | The restart method in case of grid restart.  **Choices:**   - `"GROUPED"` - `"SEQUENTIAL"` - `"SIMULTANEOUS"` |
| **provider**  dictionary | A dict object containing connection details. |
| **cert**  string | Specifies the client certificate file with digest of x509 config for extra layer secure connection the remote instance of NIOS.  Value can also be specified using `INFOBLOX_CERT` environment variable. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote instance of NIOS WAPI over REST  Value can also be specified using `INFOBLOX_HOST` environment variable. |
| **http_pool_connections**  integer | Insert decription here  **Default:** `10` |
| **http_pool_maxsize**  integer | Insert description here  **Default:** `10` |
| **http_request_timeout**  integer | The amount of time before to wait before receiving a response  Value can also be specified using `INFOBLOX_HTTP_REQUEST_TIMEOUT` environment variable.  **Default:** `10` |
| **key**  string | Specifies private key file for encryption with the certificate in order to connect with remote instance of NIOS.  Value can also be specified using `INFOBLOX_KEY` environment variable. |
| **max_results**  integer | Specifies the maximum number of objects to be returned, if set to a negative number the appliance will return an error when the number of returned objects would exceed the setting.  Value can also be specified using `INFOBLOX_MAX_RESULTS` environment variable.  **Default:** `1000` |
| **max_retries**  integer | Configures the number of attempted retries before the connection is declared usable  Value can also be specified using `INFOBLOX_MAX_RETRIES` environment variable.  **Default:** `3` |
| **password**  string | Specifies the password to use to authenticate the connection to the remote instance of NIOS.  Value can also be specified using `INFOBLOX_PASSWORD` environment variable. |
| **silent_ssl_warnings**  boolean | Insert description here  **Choices:**   - `false` - `true` ← (default) |
| **username**  string | Configures the username to use to authenticate the connection to the remote instance of NIOS.  Value can also be specified using `INFOBLOX_USERNAME` environment variable. |
| **validate_certs**  aliases: ssl_verify  boolean | Boolean value to enable or disable verifying SSL certificates  Value can also be specified using `INFOBLOX_SSL_VERIFY` environment variable.  **Choices:**   - `false` ← (default) - `true` |
| **wapi_version**  string | Specifies the version of WAPI to use  Value can also be specified using `INFOBLOX_WAP_VERSION` environment variable.  Until ansible 2.8 the default WAPI was 1.4  **Default:** `"2.9"` |
| **restart_option**  string | Controls whether services are restarted unconditionally or when needed  **Choices:**   - `"RESTART_IF_NEEDED"` ← (default) - `"FORCE_RESTART"` |
| **services**  list / elements=string | The list of services the restart applicable to.  **Choices:**   - `"ALL"` ← (default) - `"DNS"` - `"DHCP"` - `"DHCPV4"` - `"DHCPV6"`   **Default:** `["ALL"]` |

## [Notes](nios_restartservices_module.md#id4)

> **Note:**
>
> - This module supports `check_mode`.
> - This module must be run locally, which can be achieved by specifying `connection: local`.
> - Please read the :ref:`nios_guide` for more detailed information on how to use Infoblox with Ansible.

## [Examples](nios_restartservices_module.md#id5)

```yaml+jinja
- name: Restart all grid services if needed.
  infoblox.nios_modules.nios_restartservices:
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Restart DNS service if needed.
  infoblox.nios_modules.nios_restartservices:
    services:
      - DNS
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local
```

### Authors

- Mauricio Teixeira (@badnetmask)

### Collection links

- [Issue Tracker](https://github.com/infobloxopen/infoblox-ansible/issues)
- [Homepage](https://github.com/infobloxopen/infoblox-ansible)
- [Repository (Sources)](https://github.com/infobloxopen/infoblox-ansible/tree/master)
