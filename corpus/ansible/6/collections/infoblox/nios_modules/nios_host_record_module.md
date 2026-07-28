---
collection: ansible
version: "6"
title: "infoblox.nios_modules.nios_host_record module – Configure Infoblox NIOS host records"
source_url: https://docs.ansible.com/projects/ansible/6/collections/infoblox/nios_modules/nios_host_record_module.html
fetched_at: 2026-07-27T17:50:58+00:00
---
# infoblox.nios_modules.nios_host_record module – Configure Infoblox NIOS host records

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
> see [Requirements](nios_host_record_module.md#ansible-collections-infoblox-nios-modules-nios-host-record-module-requirements) for details.
>
> To use it in a playbook, specify: `infoblox.nios_modules.nios_host_record`.

New in infoblox.nios_modules 1.0.0

- [Synopsis](nios_host_record_module.md#synopsis)
- [Requirements](nios_host_record_module.md#requirements)
- [Parameters](nios_host_record_module.md#parameters)
- [Notes](nios_host_record_module.md#notes)
- [Examples](nios_host_record_module.md#examples)

## [Synopsis](nios_host_record_module.md#id1)

- Adds and/or removes instances of host record objects from Infoblox NIOS servers. This module manages NIOS `record:host` objects using the Infoblox WAPI interface over REST.
- Updates instances of host record object from Infoblox NIOS servers.

## [Requirements](nios_host_record_module.md#id2)

The below requirements are needed on the host that executes this module.

- infoblox-client

## [Parameters](nios_host_record_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aliases**  list / elements=string | Configures an optional list of additional aliases to add to the host record. These are equivalent to CNAMEs but held within a host record. Must be in list format. |
| **comment**  string | Configures a text string comment to be associated with the instance of this object. The provided text string will be configured on the object instance. |
| **configure_for_dns**  aliases: dns  boolean | Sets the DNS to particular parent. If user needs to bypass DNS user can make the value to false.  Choices:   - `false` - `true` ← (default) |
| **extattrs**  dictionary | Allows for the configuration of Extensible Attributes on the instance of the object. This argument accepts a set of key / value pairs for configuration. |
| **ipv4addrs**  aliases: ipv4  list / elements=dictionary | Configures the IPv4 addresses for this host record. This argument accepts a list of values (see suboptions). |
| **add**  aliases: add  boolean  added in infoblox.nios_modules 1.0.0 | If user wants to add the ipv4 address to an existing host record. Note that with *add* user will have to keep the *state* as *present*, as new IP address is allocated to existing host record. See examples.  Choices:   - `false` - `true` |
| **configure_for_dhcp**  aliases: dhcp  boolean | Configure the host_record over DHCP instead of DNS, if user changes it to true, user need to mention MAC address to configure.  Choices:   - `false` - `true` |
| **ipv4addr**  aliases: address  string / required | Configures the IPv4 address for the host record. Users can dynamically allocate ipv4 address to host record by passing dictionary containing, *nios_next_ip* and *CIDR network range*. If user wants to add or remove the ipv4 address from existing record, *add/remove* params need to be used. See examples. |
| **mac**  aliases: mac  string | Configures the hardware MAC address for the host record. If user makes DHCP to true, user need to mention MAC address. |
| **remove**  aliases: remove  boolean  added in infoblox.nios_modules 1.0.0 | If user wants to remove the ipv4 address from an existing host record. Note that with *remove* user will have to change the *state* to *absent*, as IP address is de-allocated from an existing host record. See examples.  Choices:   - `false` - `true` |
| **ipv6addrs**  aliases: ipv6  list / elements=dictionary | Configures the IPv6 addresses for the host record. This argument accepts a list of values (see options). |
| **configure_for_dhcp**  boolean | Configure the host_record over DHCP instead of DNS, if user changes it to true, user need to mention MAC address to configure.  Choices:   - `false` - `true` |
| **ipv6addr**  aliases: address  string / required | Configures the IPv6 address for the host record. |
| **mac**  aliases: mac  string | Configures the hardware MAC address for the host record. If user makes DHCP to true, user need to mention MAC address. |
| **name**  string / required | Specifies the fully qualified hostname to add or remove from the system. User can also update the hostname as it is possible to pass a dict containing *new_name*, *old_name*. See examples. |
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
| **state**  string | Configures the intended state of the instance of the object on the NIOS server. When this value is set to `present`, the object is configured on the device and when this value is set to `absent` the value is removed (if necessary) from the device.  Choices:   - `"present"` ← (default) - `"absent"` |
| **ttl**  integer | Configures the TTL to be associated with this host record. |
| **view**  aliases: dns_view  string | Sets the DNS view to associate this host record with. The DNS view must already be configured on the system.  Default: `"default"` |

## [Notes](nios_host_record_module.md#id4)

> **Note:**
>
> - This module supports `check_mode`.
> - This module must be run locally, which can be achieved by specifying `connection: local`.
> - Please read the :ref:`nios_guide` for more detailed information on how to use Infoblox with Ansible.

## [Examples](nios_host_record_module.md#id5)

```yaml+jinja
- name: Configure an ipv4 host record
  infoblox.nios_modules.nios_host_record:
    name: host.ansible.com
    ipv4:
      - address: 192.168.10.1
    aliases:
      - cname.ansible.com
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Add a comment to an existing host record
  infoblox.nios_modules.nios_host_record:
    name: host.ansible.com
    ipv4:
      - address: 192.168.10.1
    comment: this is a test comment
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Remove a host record from the system
  infoblox.nios_modules.nios_host_record:
    name: host.ansible.com
    state: absent
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Update an ipv4 host record
  infoblox.nios_modules.nios_host_record:
    name: {new_name: host-new.ansible.com, old_name: host.ansible.com}
    ipv4:
      - address: 192.168.10.1
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Create an ipv4 host record bypassing DNS
  infoblox.nios_modules.nios_host_record:
    name: new_host
    ipv4:
      - address: 192.168.10.1
    dns: false
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Create an ipv4 host record over DHCP
  infoblox.nios_modules.nios_host_record:
    name: host.ansible.com
    ipv4:
      - address: 192.168.10.1
        dhcp: true
        mac: 00-80-C8-E3-4C-BD
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Dynamically add host record to next available ip
  infoblox.nios_modules.nios_host_record:
    name: host.ansible.com
    ipv4:
      - address: {nios_next_ip: 192.168.10.0/24}
    comment: this is a test comment
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Add ip to host record
  infoblox.nios_modules.nios_host_record:
    name: host.ansible.com
    ipv4:
      - address: 192.168.10.2
        add: true
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Remove ip from host record
  infoblox.nios_modules.nios_host_record:
    name: host.ansible.com
    ipv4:
      - address: 192.168.10.1
        remove: true
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
