---
collection: ansible
version: "8"
title: "infoblox.nios_modules.nios_network module – Configure Infoblox NIOS network object"
source_url: https://docs.ansible.com/projects/ansible/8/collections/infoblox/nios_modules/nios_network_module.html
fetched_at: 2026-07-28T02:36:02+00:00
---
# infoblox.nios_modules.nios_network module – Configure Infoblox NIOS network object

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
> see [Requirements](nios_network_module.md#ansible-collections-infoblox-nios-modules-nios-network-module-requirements) for details.
>
> To use it in a playbook, specify: `infoblox.nios_modules.nios_network`.

New in infoblox.nios_modules 1.0.0

- [Synopsis](nios_network_module.md#synopsis)
- [Requirements](nios_network_module.md#requirements)
- [Parameters](nios_network_module.md#parameters)
- [Notes](nios_network_module.md#notes)
- [Examples](nios_network_module.md#examples)

## [Synopsis](nios_network_module.md#id1)

- Adds and/or removes instances of network objects from Infoblox NIOS servers. This module manages NIOS `network` objects using the Infoblox WAPI interface over REST.
- Supports both IPV4 and IPV6 internet protocols.

## [Requirements](nios_network_module.md#id2)

The below requirements are needed on the host that executes this module.

- infoblox-client

## [Parameters](nios_network_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **comment**  string | Configures a text string comment to be associated with the instance of this object. The provided text string will be configured on the object instance. |
| **container**  boolean | If set to true it’ll create the network container to be added or removed from the system.  **Choices:**   - `false` - `true` |
| **extattrs**  dictionary | Allows for the configuration of Extensible Attributes on the instance of the object. This argument accepts a set of key / value pairs for configuration. |
| **members**  list / elements=dictionary | Configures the Nios Menber assignment for the configured network instance. This argument accepts a list of member names (see suboptions). When omitted a default value of an empty list is used. If the field ‘container’ is set to true this field is ignored.  **Default:** `[]` |
| **name**  string | The name of the Nios member to be assigned to this network. |
| **network**  aliases: name, cidr  string / required | Specifies the network to add or remove from the system. The value should use CIDR notation. |
| **network_view**  string | Configures the name of the network view to associate with this configured instance.  **Default:** `"default"` |
| **options**  list / elements=dictionary | Configures the set of DHCP options to be included as part of the configured network instance. This argument accepts a list of values (see suboptions). When configuring suboptions at least one of `name` or `num` must be specified. |
| **name**  string | The name of the DHCP option to configure. The standard options are `router`, `router-templates`, `domain-name-servers`, `domain-name`, `broadcast-address`, `broadcast-address-offset`, `dhcp-lease-time`, and `dhcp6.name-servers`. |
| **num**  integer | The number of the DHCP option to configure |
| **use_option**  boolean | Only applies to a subset of options (see NIOS API documentation)  **Choices:**   - `false` - `true` ← (default) |
| **value**  string / required | The value of the DHCP option specified by `name` |
| **vendor_class**  string | The name of the space this DHCP option is associated to  **Default:** `"DHCP"` |
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
| **state**  string | Configures the intended state of the instance of the object on the NIOS server. When this value is set to `present`, the object is configured on the device and when this value is set to `absent` the value is removed (if necessary) from the device.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **template**  string | If set on creation, the network is created according to the values specified in the selected template. |

## [Notes](nios_network_module.md#id4)

> **Note:**
>
> - This module supports `check_mode`.
> - This module must be run locally, which can be achieved by specifying `connection: local`.
> - Please read the :ref:`nios_guide` for more detailed information on how to use Infoblox with Ansible.

## [Examples](nios_network_module.md#id5)

```yaml+jinja
- name: Configure a network ipv4
  infoblox.nios_modules.nios_network:
    network: 192.168.10.0/24
    comment: this is a test comment
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Configure a network ipv6
  infoblox.nios_modules.nios_network:
    network: fe80::/64
    comment: this is a test comment
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Create network with member assignment for a network ipv4
  infoblox.nios_modules.nios_network:
    network: 192.168.10.0/24
    comment: This is a test comment
    members:
      - name: member1.infoblox
      - name: member2.infoblox
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Remove member assignment form ipv4 network
  infoblox.nios_modules.nios_network:
    network: 192.168.10.0/24
    comment: This is a test comment
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Set dhcp options for a network ipv4
  infoblox.nios_modules.nios_network:
    network: 192.168.10.0/24
    comment: this is a test comment
    options:
      - name: domain-name
        value: ansible.com
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Remove a network ipv4
  infoblox.nios_modules.nios_network:
    network: 192.168.10.0/24
    state: absent
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Configure an ipv4 network container
  infoblox.nios_modules.nios_network:
    network: 192.168.10.0/24
    container: true
    comment: test network container
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Configure an ipv6 network container
  infoblox.nios_modules.nios_network:
    network: fe80::/64
    container: true
    comment: test network container
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Remove an ipv4 network container
  infoblox.nios_modules.nios_network:
    networkr: 192.168.10.0/24
    container: true
    comment: test network container
    state: absent
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local
```

### Authors

- Peter Sprygada (@privateip)
- Matthew Dennett (@matthewdennett)

### Collection links

- [Issue Tracker](https://github.com/infobloxopen/infoblox-ansible/issues)
- [Homepage](https://github.com/infobloxopen/infoblox-ansible)
- [Repository (Sources)](https://github.com/infobloxopen/infoblox-ansible/tree/master)
