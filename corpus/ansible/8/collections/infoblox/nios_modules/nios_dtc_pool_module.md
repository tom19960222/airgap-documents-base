---
collection: ansible
version: "8"
title: "infoblox.nios_modules.nios_dtc_pool module – Configure Infoblox NIOS DTC Pool"
source_url: https://docs.ansible.com/projects/ansible/8/collections/infoblox/nios_modules/nios_dtc_pool_module.html
fetched_at: 2026-07-28T02:35:57+00:00
---
# infoblox.nios_modules.nios_dtc_pool module – Configure Infoblox NIOS DTC Pool

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
> see [Requirements](nios_dtc_pool_module.md#ansible-collections-infoblox-nios-modules-nios-dtc-pool-module-requirements) for details.
>
> To use it in a playbook, specify: `infoblox.nios_modules.nios_dtc_pool`.

New in infoblox.nios_modules 1.1.0

- [Synopsis](nios_dtc_pool_module.md#synopsis)
- [Requirements](nios_dtc_pool_module.md#requirements)
- [Parameters](nios_dtc_pool_module.md#parameters)
- [Notes](nios_dtc_pool_module.md#notes)
- [Examples](nios_dtc_pool_module.md#examples)

## [Synopsis](nios_dtc_pool_module.md#id1)

- Adds and/or removes instances of DTC Pool objects from Infoblox NIOS servers. This module manages NIOS `dtc:pool` objects using the Infoblox WAPI interface over REST. A DTC pool is a collection of IDNS resources (virtual servers).

## [Requirements](nios_dtc_pool_module.md#id2)

The below requirements are needed on the host that executes this module.

- infoblox-client

## [Parameters](nios_dtc_pool_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **comment**  string | Configures a text string comment to be associated with the instance of this object. The provided text string will be configured on the object instance. |
| **extattrs**  dictionary | Allows for the configuration of Extensible Attributes on the instance of the object. This argument accepts a set of key / value pairs for configuration. |
| **lb_preferred_method**  string / required | Configures the preferred load balancing method.  Use this to select a method type from the pool.  **Choices:**   - `"ALL_AVAILABLE"` - `"DYNAMIC_RATIO"` - `"GLOBAL_AVAILABILITY"` - `"RATIO"` - `"ROUND_ROBIN"` - `"TOPOLOGY"` |
| **monitors**  list / elements=dictionary | Specifies the health monitors related to pool.  The format of this parameter is required due to an API limitation.  This option only works if you set the `wapi_version` variable on your `provider` variable to a number higher than “2.6”. |
| **name**  string / required | Provide the name of the health monitor. |
| **type**  string / required | Provide the type of health monitor.  **Choices:**   - `"http"` - `"icmp"` - `"tcp"` - `"pdp"` - `"sip"` - `"snmp"` |
| **name**  string / required | Specifies the DTC Pool display name |
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
| **servers**  list / elements=dictionary | Configure the DTC Servers related to the pool |
| **ratio**  integer | Provide the weight of the server  **Default:** `1` |
| **server**  string / required | Provide the name of the DTC Server |
| **state**  string | Configures the intended state of the instance of the object on the NIOS server. When this value is set to `present`, the object is configured on the device and when this value is set to `absent` the value is removed (if necessary) from the device.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](nios_dtc_pool_module.md#id4)

> **Note:**
>
> - This module supports `check_mode`.
> - This module must be run locally, which can be achieved by specifying `connection: local`.
> - Please read the :ref:`nios_guide` for more detailed information on how to use Infoblox with Ansible.

## [Examples](nios_dtc_pool_module.md#id5)

```yaml+jinja
- name: Configure a DTC Pool
  infoblox.nios_modules.nios_dtc_pool:
    name: web_pool
    lb_preferred_method: ROUND_ROBIN
    servers:
      - server: a.ansible.com
      - server: b.ansible.com
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Add a comment to a DTC Pool
  infoblox.nios_modules.nios_dtc_pool:
    name: web_pool
    lb_preferred_method: ROUND_ROBIN
    comment: this is a test comment
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Remove a DTC Pool from the system
  infoblox.nios_modules.nios_dtc_pool:
    name: web_pool
    lb_preferred_method: ROUND_ROBIN
    state: absent
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
