---
collection: ansible
version: "6"
title: "infoblox.nios_modules.nios_zone module – Configure Infoblox NIOS DNS zones"
source_url: https://docs.ansible.com/projects/ansible/6/collections/infoblox/nios_modules/nios_zone_module.html
fetched_at: 2026-07-27T17:51:06+00:00
---
# infoblox.nios_modules.nios_zone module – Configure Infoblox NIOS DNS zones

> **Note:**
>
> This module is part of the [infoblox.nios_modules collection](https://galaxy.ansible.com/infoblox/nios_modules) (version 1.4.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install infoblox.nios_modules`.
> You need further requirements to be able to use this module,
> see [Requirements](nios_zone_module.md#ansible-collections-infoblox-nios-modules-nios-zone-module-requirements) for details.
>
> To use it in a playbook, specify: `infoblox.nios_modules.nios_zone`.

New in infoblox.nios_modules 1.0.0

- [Synopsis](nios_zone_module.md#synopsis)
- [Requirements](nios_zone_module.md#requirements)
- [Parameters](nios_zone_module.md#parameters)
- [Notes](nios_zone_module.md#notes)
- [Examples](nios_zone_module.md#examples)

## [Synopsis](nios_zone_module.md#id1)

- Adds and/or removes instances of DNS zone objects from Infoblox NIOS servers. This module manages NIOS `zone_auth` objects using the Infoblox WAPI interface over REST.

## [Requirements](nios_zone_module.md#id2)

The below requirements are needed on the host that executes this module.

- infoblox-client

## [Parameters](nios_zone_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **comment**  string | Configures a text string comment to be associated with the instance of this object. The provided text string will be configured on the object instance. |
| **extattrs**  dictionary | Allows for the configuration of Extensible Attributes on the instance of the object. This argument accepts a set of key / value pairs for configuration. |
| **fqdn**  aliases: name  string / required | Specifies the qualified domain name to either add or remove from the NIOS instance based on the configured `state` value. |
| **grid_primary**  list / elements=dictionary | Configures the grid primary servers for this zone. |
| **name**  string / required | The name of the grid primary server |
| **grid_secondaries**  list / elements=dictionary | Configures the grid secondary servers for this zone. |
| **name**  string / required | The name of the grid secondary server |
| **ns_group**  string | Configures the name server group for this zone. Name server group is mutually exclusive with grid primary and grid secondaries. |
| **provider**  dictionary | A dict object containing connection details. |
| **cert**  string | Specifies the client certificate file with digest of x509 config for extra layer secure connection the remote instance of NIOS.  Value can also be specified using `INFOBLOX_CERT` environment variable. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote instance of NIOS WAPI over REST  Value can also be specified using `INFOBLOX_HOST` environment variable. |
| **http_pool_connections**  integer | Insert decription here  Default: `10` |
| **http_pool_maxsize**  integer | Insert description here  Default: `10` |
| **http_request_timeout**  integer | The amount of time before to wait before receiving a response  Value can also be specified using `INFOBLOX_HTTP_REQUEST_TIMEOUT` environment variable.  Default: `10` |
| **key**  string | Specifies private key file for encryption with the certificate in order to connect with remote instance of NIOS.  Value can also be specified using `INFOBLOX_KEY` environment variable. |
| **max_results**  integer | Specifies the maximum number of objects to be returned, if set to a negative number the appliance will return an error when the number of returned objects would exceed the setting.  Value can also be specified using `INFOBLOX_MAX_RESULTS` environment variable.  Default: `1000` |
| **max_retries**  integer | Configures the number of attempted retries before the connection is declared usable  Value can also be specified using `INFOBLOX_MAX_RETRIES` environment variable.  Default: `3` |
| **password**  string | Specifies the password to use to authenticate the connection to the remote instance of NIOS.  Value can also be specified using `INFOBLOX_PASSWORD` environment variable. |
| **silent_ssl_warnings**  boolean | Insert description here  Choices:   - `false` - `true` ← (default) |
| **username**  string | Configures the username to use to authenticate the connection to the remote instance of NIOS.  Value can also be specified using `INFOBLOX_USERNAME` environment variable. |
| **validate_certs**  aliases: ssl_verify  boolean | Boolean value to enable or disable verifying SSL certificates  Value can also be specified using `INFOBLOX_SSL_VERIFY` environment variable.  Choices:   - `false` ← (default) - `true` |
| **wapi_version**  string | Specifies the version of WAPI to use  Value can also be specified using `INFOBLOX_WAP_VERSION` environment variable.  Until ansible 2.8 the default WAPI was 1.4  Default: `"2.1"` |
| **restart_if_needed**  boolean | If set to true, causes the NIOS DNS service to restart and load the new zone configuration.  Choices:   - `false` - `true` |
| **state**  string | Configures the intended state of the instance of the object on the NIOS server. When this value is set to `present`, the object is configured on the device and when this value is set to `absent` the value is removed (if necessary) from the device.  Choices:   - `"present"` ← (default) - `"absent"` |
| **view**  aliases: dns_view  string | Configures the DNS view name for the configured resource. The specified DNS zone must already exist on the running NIOS instance prior to configuring zones.  Default: `"default"` |
| **zone_format**  string | Create an authorative Reverse-Mapping Zone which is an area of network space for which one or more name servers-primary and secondary-have the responsibility to respond to address-to-name queries. It supports reverse-mapping zones for both IPv4 and IPv6 addresses.  Default: `"FORWARD"` |

## [Notes](nios_zone_module.md#id4)

> **Note:**
>
> - This module supports `check_mode`.
> - This module must be run locally, which can be achieved by specifying `connection: local`.
> - Please read the :ref:`nios_guide` for more detailed information on how to use Infoblox with Ansible.

## [Examples](nios_zone_module.md#id5)

```yaml+jinja
- name: Configure a zone on the system using grid primary and secondaries
  infoblox.nios_modules.nios_zone:
    name: ansible.com
    grid_primary:
      - name: gridprimary.grid.com
    grid_secondaries:
      - name: gridsecondary1.grid.com
      - name: gridsecondary2.grid.com
    restart_if_needed: true
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Configure a zone on the system using a name server group
  infoblox.nios_modules.nios_zone:
    name: ansible.com
    ns_group: examplensg
    restart_if_needed: true
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Configure a reverse mapping zone on the system using IPV4 zone format
  infoblox.nios_modules.nios_zone:
    name: 10.10.10.0/24
    zone_format: IPV4
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Configure a reverse mapping zone on the system using IPV6 zone format
  infoblox.nios_modules.nios_zone:
    name: 100::1/128
    zone_format: IPV6
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Update the comment and ext attributes for an existing zone
  infoblox.nios_modules.nios_zone:
    name: ansible.com
    comment: this is an example comment
    extattrs:
      Site: west-dc
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Remove the dns zone
  infoblox.nios_modules.nios_zone:
    name: ansible.com
    state: absent
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Remove the reverse mapping dns zone from the system with IPV4 zone format
  infoblox.nios_modules.nios_zone:
    name: 10.10.10.0/24
    zone_format: IPV4
    state: absent
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local
```

### Authors

- Peter Sprygada (@privateip)

### Collection links

[Issue Tracker](https://github.com/infobloxopen/infoblox-ansible/issues)
[Homepage](https://github.com/infobloxopen/infoblox-ansible)
[Repository (Sources)](https://github.com/infobloxopen/infoblox-ansible/tree/master)
